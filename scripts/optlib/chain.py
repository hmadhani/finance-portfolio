"""Cboe delayed-quote option chains: fetch, parse, filter.

Data source (free, 15-min delayed, no key): https://cdn.cboe.com/api/global/delayed_quotes/
Set OPTIONS_FIXTURE_DIR to read <dir>/<name> files instead of the network (tests).
"""
import json
import math
import os
import urllib.request
from dataclasses import dataclass
from datetime import date, datetime

CBOE_OPTIONS_URL = "https://cdn.cboe.com/api/global/delayed_quotes/options/{symbol}.json"
CBOE_QUOTE_URL = "https://cdn.cboe.com/api/global/delayed_quotes/quotes/{symbol}.json"
VIX_HISTORY_URL = "https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv"
FIXTURE_ENV = "OPTIONS_FIXTURE_DIR"
STOCK_EXPIRY = date(9999, 12, 31)


def fetch_text(url: str, fixture_name: str) -> str:
    fixture_dir = os.environ.get(FIXTURE_ENV)
    if fixture_dir:
        with open(os.path.join(fixture_dir, fixture_name)) as f:
            return f.read()
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode()


def load_chain(symbol: str) -> dict:
    return json.loads(fetch_text(CBOE_OPTIONS_URL.format(symbol=symbol), f"{symbol}.json"))["data"]


def load_quote(symbol: str) -> dict:
    return json.loads(fetch_text(CBOE_QUOTE_URL.format(symbol=symbol), f"{symbol}.json"))["data"]


def load_vix_history() -> str:
    return fetch_text(VIX_HISTORY_URL, "VIX_History.csv")


def parse_occ(option: str):
    tail, root = option[-15:], option[:-15]
    expiry = datetime.strptime(tail[:6], "%y%m%d").date()
    return root, expiry, tail[6], int(tail[7:]) / 1000.0


def occ_symbol(root: str, expiry: date, kind: str, strike: float) -> str:
    return f"{root}{expiry.strftime('%y%m%d')}{kind}{int(round(strike * 1000)):08d}"


@dataclass
class Contract:
    option: str
    root: str
    expiry: date
    kind: str  # "C", "P", or "S" (shares)
    strike: float
    bid: float
    ask: float
    iv: float
    delta: float
    gamma: float
    theta: float
    vega: float
    open_interest: float
    volume: float

    @property
    def mid(self) -> float:
        return round((self.bid + self.ask) / 2.0, 4)

    def dte(self, asof: date) -> int:
        return (self.expiry - asof).days

    def row(self, asof: date) -> dict:
        return {"option": self.option, "kind": self.kind, "strike": self.strike,
                "expiry": self.expiry.isoformat(), "dte": self.dte(asof),
                "bid": self.bid, "ask": self.ask, "mid": self.mid,
                "iv": round(self.iv, 4), "delta": self.delta, "theta": self.theta,
                "vega": self.vega, "open_interest": self.open_interest}


def stock_contract(root: str, spot: float) -> Contract:
    return Contract("STOCK", root, STOCK_EXPIRY, "S", 0.0, spot, spot, 0.0,
                    1.0, 0.0, 0.0, 0.0, 0.0, 0.0)


def _f(v) -> float:
    return float(v) if v not in (None, "") else 0.0


def contracts(chain: dict) -> list:
    out = []
    for o in chain["options"]:
        root, exp, kind, strike = parse_occ(o["option"])
        out.append(Contract(o["option"], root, exp, kind, strike,
                            _f(o.get("bid")), _f(o.get("ask")), _f(o.get("iv")),
                            _f(o.get("delta")), _f(o.get("gamma")), _f(o.get("theta")),
                            _f(o.get("vega")), _f(o.get("open_interest")), _f(o.get("volume"))))
    return out


def index_contracts(cs: list) -> dict:
    return {c.option: c for c in cs}


def is_liquid(c: Contract, min_oi: float = 500, max_spread_pct: float = 0.10,
              abs_spread_ok: float = None) -> bool:
    if c.bid <= 0 or c.ask < c.bid or c.open_interest < min_oi:
        return False
    width = round(c.ask - c.bid, 4)
    if width <= max_spread_pct * c.mid:
        return True
    return abs_spread_ok is not None and width <= abs_spread_ok


def expected_move(price: float, iv_decimal: float, dte: int) -> float:
    """One-standard-deviation move implied by IV over `dte` calendar days."""
    return price * iv_decimal * math.sqrt(dte / 365.0)


def select_expiries(cs: list, asof: date, dte_min: int, dte_max: int, max_expiries: int = 2) -> list:
    exps = sorted({c.expiry for c in cs if dte_min <= c.dte(asof) <= dte_max})
    return exps[:max_expiries]


def delta_buckets(cs: list, asof: date, expiry: date, targets: list, liquid_kwargs: dict) -> list:
    """For each kind and each |delta| target, the liquid contract on `expiry` closest to it."""
    picked = {}
    for kind in ("P", "C"):
        pool = [c for c in cs if c.expiry == expiry and c.kind == kind and is_liquid(c, **liquid_kwargs)]
        for t in targets:
            if pool:
                best = min(pool, key=lambda c: abs(abs(c.delta) - t))
                picked[best.option] = best
    return sorted(picked.values(), key=lambda c: (c.kind, c.strike))
