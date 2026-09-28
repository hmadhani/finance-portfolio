#!/usr/bin/env python3
"""
options_data.py — data + deterministic math for the $50K options paper portfolio
(finance-portfolio repo, options/). Stdlib only. Data: Cboe delayed quotes
(15-min delayed, free, no key). Every number in options/learning-ledger.md
must come from one of these commands; re-running a command re-prices against
the quotes available at that time, which may differ from the cycle's.

  regime                          VIX, VIX3M, term structure, VIX 1-yr percentile, BXM/PUT levels
                                  (partial data: null fields + `errors`; exit 1 only if nothing loads)
  scan [--symbols A,B] [--dte 30-60]
                                  per symbol: price, iv30, expected move, IV rank, candidate strikes
  price-spread --symbol S --legs "SELL 1 P 95 2026-11-06; BUY 1 P 90 2026-11-06" --qty N [--with-stock]
                                  fills + per-leg quote/liquidity, max P/L, breakevens, prob. of profit,
                                  uncovered_short_puts, all_legs_liquid, net Greeks, payoff diagram
  mark [--positions PATH]         mark open positions to mid, list rule triggers
  record-iv [--symbols A,B]       append today's iv30 per symbol to the IV history CSV

Global: --asof YYYY-MM-DD (default today). Set OPTIONS_FIXTURE_DIR to run offline.
"""
import argparse
import json
import os
import sys
from datetime import date

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from optlib import chain as ch  # noqa: E402
from optlib import ivhist, marks  # noqa: E402
from optlib import strategy as st  # noqa: E402

REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
DEFAULT_IV_HISTORY = os.path.join(REPO, "options", "data", "iv-history.csv")
DEFAULT_POSITIONS = os.path.join(REPO, "options", "data", "positions.json")

ETFS = ["SPY", "QQQ", "IWM", "DIA", "XLF", "XLE", "XLK", "XLV", "GLD", "TLT"]
MEGA_CAPS = ["AAPL", "MSFT", "NVDA", "AMZN", "GOOGL", "META", "TSLA", "AMD", "AVGO", "JPM",
             "BAC", "XOM", "KO", "PFE", "INTC", "F", "T", "WFC", "DIS", "NFLX"]
UNIVERSE = ETFS + MEGA_CAPS
DELTA_TARGETS = [0.05, 0.10, 0.16, 0.20, 0.25, 0.30, 0.40, 0.50]


class UsageError(Exception):
    pass


class DataError(Exception):
    """Nothing usable could be fetched (exit 1)."""


def positive_int(s: str) -> int:
    v = int(s)
    if v <= 0:
        raise argparse.ArgumentTypeError(f"qty must be > 0: {s}")
    return v


def liquid_kwargs(symbol: str) -> dict:
    return {"abs_spread_ok": 0.05} if symbol in ETFS else {}


def cmd_regime(a):
    """Each data source is fetched independently; a field that cannot be
    filled is null and listed in `errors` as {field, error}. term_structure
    and stress need both VIX and VIX3M; unknown stress is null, never false.
    Exits non-zero (DataError) only when no field at all could be filled."""
    out = {"asof": a.asof.isoformat(), "vix": None, "vix3m": None, "term_structure": None,
           "stress": None, "vix_percentile_1y": None, "bxm": None, "put": None}
    errors = []

    def err(field, e):
        errors.append({"field": field, "error": e if isinstance(e, str) else f"{type(e).__name__}: {e}"})

    for field, sym in (("vix", "_VIX"), ("vix3m", "_VIX3M"), ("bxm", "_BXM"), ("put", "_PUT")):
        try:
            out[field] = float(ch.load_quote(sym)["current_price"])
        except Exception as e:  # one bad source must not sink the rest
            err(field, e)
    if out["vix"] is not None and out["vix3m"] is not None:
        out["stress"] = out["vix"] > out["vix3m"]
        out["term_structure"] = "backwardation" if out["stress"] else "contango"
    else:
        missing = "vix" if out["vix"] is None else "vix3m"
        err("term_structure", f"needs vix and vix3m ({missing} unavailable)")
        err("stress", f"unknown: needs vix and vix3m ({missing} unavailable)")
    if out["vix"] is None:
        err("vix_percentile_1y", "needs the current vix (unavailable)")
    else:
        try:
            out["vix_percentile_1y"] = ivhist.vix_percentile(ch.load_vix_history(), out["vix"])
            if out["vix_percentile_1y"] is None:
                err("vix_percentile_1y", "VIX history has no CLOSE values")
        except Exception as e:
            err("vix_percentile_1y", e)
    errors.sort(key=lambda x: ["vix", "vix3m", "term_structure", "stress",
                               "vix_percentile_1y", "bxm", "put"].index(x["field"]))
    out["errors"] = errors
    if all(out[k] is None for k in ("vix", "vix3m", "vix_percentile_1y", "bxm", "put")):
        raise DataError("no regime data could be fetched: " + "; ".join(
            f"{x['field']}: {x['error']}" for x in errors))
    return out


def _symbols(a):
    return [s.strip().upper() for s in a.symbols.split(",")] if a.symbols else UNIVERSE


def cmd_scan(a):
    dmin, dmax = (int(x) for x in a.dte.split("-"))
    results = []
    for sym in _symbols(a):
        try:
            raw = ch.load_chain(sym)
            cs = ch.contracts(raw)
            price, iv30 = raw["current_price"], raw["iv30"]
            exps = ch.select_expiries(cs, a.asof, dmin, dmax, a.max_expiries)
            cands = []
            for e in exps:
                cands += [c.row(a.asof) for c in ch.delta_buckets(cs, a.asof, e, DELTA_TARGETS, liquid_kwargs(sym))]
            results.append({"symbol": sym, "price": price, "iv30_pct": iv30,
                            "expected_move_30d": round(ch.expected_move(price, iv30 / 100.0, 30), 2),
                            "iv_rank": ivhist.iv_rank(ivhist.history(a.iv_history, sym), iv30),
                            "is_etf": sym in ETFS,
                            "expiries": [e.isoformat() for e in exps], "candidates": cands})
        except Exception as e:  # one bad symbol must not sink the scan
            results.append({"symbol": sym, "error": f"{type(e).__name__}: {e}"})
    return {"asof": a.asof.isoformat(), "results": results}


def cmd_price_spread(a):
    raw = ch.load_chain(a.symbol.upper())
    spot = raw["current_price"]
    idx = ch.index_contracts(ch.contracts(raw))
    try:
        legs = st.legs_from_spec(a.legs, a.symbol.upper(), idx, spot=spot, with_stock=a.with_stock)
    except (KeyError, ValueError) as e:
        raise UsageError(e.args[0])
    out = st.analyze(legs, a.qty, spot, a.asof)
    lk = liquid_kwargs(a.symbol.upper())
    for f, l in zip(out["fills"], legs):
        c = l.contract
        f.update(bid=c.bid, ask=c.ask, mid=c.mid, delta=c.delta, open_interest=c.open_interest,
                 liquid=None if c.kind == "S" else ch.is_liquid(c, **lk))  # stock legs exempt
    out["all_legs_liquid"] = all(f["liquid"] for f in out["fills"] if f["liquid"] is not None)
    out["spot"] = spot
    out["payoff_ascii"] = st.ascii_payoff(legs, a.qty, spot)
    out["position_template"] = {
        "id": "<fill-in>", "symbol": a.symbol.upper(), "strategy": "<fill-in>",
        "opened": a.asof.isoformat(), "qty": a.qty, "entry_cost": out["entry_cost_per_share"],
        "max_loss": out["max_loss"],
        "profit_target_pct": 50 if out["credit_or_debit"] == "credit" else 100,
        "legs": [{"action": l.action, "ratio": l.ratio, "option": l.contract.option} for l in legs]}
    return out


def cmd_mark(a):
    with open(a.positions) as f:
        positions = json.load(f)["positions"]
    chains = {}
    out = []
    for p in positions:
        sym = p["symbol"]
        if sym not in chains:
            try:
                raw = ch.load_chain(sym)
                chains[sym] = (ch.index_contracts(ch.contracts(raw)), raw["current_price"])
            except Exception as e:  # one bad symbol must not sink the rest of the marks
                chains[sym] = e
        cached = chains[sym]
        if isinstance(cached, Exception):
            out.append({"id": p["id"], "symbol": sym, "error": f"{type(cached).__name__}: {cached}"})
            continue
        idx, spot = cached
        out.append(marks.mark_position(p, idx, spot, a.asof))
    return {"asof": a.asof.isoformat(), "marks": out}


def cmd_record_iv(a):
    rows, errors = [], []
    for sym in _symbols(a):
        try:
            raw = ch.load_chain(sym)
            rows.append((sym, float(raw["iv30"]), float(raw["current_price"])))
        except Exception as e:
            errors.append({"symbol": sym, "error": f"{type(e).__name__}: {e}"})
    n = ivhist.record(a.iv_history, a.asof.isoformat(), rows)
    return {"asof": a.asof.isoformat(), "appended": n, "errors": errors}


def build_parser():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--asof", type=date.fromisoformat, default=date.today())
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("regime").set_defaults(fn=cmd_regime)
    s = sub.add_parser("scan")
    s.add_argument("--symbols")
    s.add_argument("--dte", default="30-60")
    s.add_argument("--max-expiries", type=int, default=2)
    s.add_argument("--iv-history", default=DEFAULT_IV_HISTORY)
    s.set_defaults(fn=cmd_scan)
    ps = sub.add_parser("price-spread")
    ps.add_argument("--symbol", required=True)
    ps.add_argument("--legs", required=True)
    ps.add_argument("--qty", type=positive_int, required=True)
    ps.add_argument("--with-stock", action="store_true")
    ps.set_defaults(fn=cmd_price_spread)
    m = sub.add_parser("mark")
    m.add_argument("--positions", default=DEFAULT_POSITIONS)
    m.set_defaults(fn=cmd_mark)
    r = sub.add_parser("record-iv")
    r.add_argument("--symbols")
    r.add_argument("--iv-history", default=DEFAULT_IV_HISTORY)
    r.set_defaults(fn=cmd_record_iv)
    return p


def main(argv=None):
    a = build_parser().parse_args(argv)
    try:
        result = a.fn(a)
    except UsageError as e:
        print(f"error: {e}", file=sys.stderr)
        return 2
    except DataError as e:
        print(f"error: {e}", file=sys.stderr)
        return 1
    json.dump(result, sys.stdout, indent=2, default=str)
    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
