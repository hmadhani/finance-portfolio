# Options Paper Portfolio Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** A $50K defined-risk options paper portfolio in the `finance-portfolio` repo, run daily by a cloud routine, with a beginner-level learning ledger that explains every decision using reproducible numbers.

**Architecture:** A stdlib-only Python package (`scripts/optlib/`) plus a CLI (`scripts/options_data.py`) fetches Cboe delayed option chains and does all deterministic math (fills, payoffs, breakevens, probability of profit, Greeks, marks, IV rank). The cloud routine's prompt makes the judgment calls (regime read, strategy choice, management) and writes the teaching. Machine state lives in `options/data/positions.json` and `options/data/iv-history.csv`; human-readable state lives in `options/options-portfolio.md` and `options/learning-ledger.md`.

**Tech Stack:** Python 3 standard library only (`urllib`, `json`, `csv`, `math`, `unittest`) — no pip installs, so it runs unchanged in the cloud sandbox. Cboe delayed-quotes CDN for data.

**Spec:** `docs/superpowers/specs/2026-09-27-options-portfolio-design.md`

## Global Constraints

- Paper only. Starting capital **$50,000**. Defined-risk strategies only — never naked short calls/puts.
- Max loss per position ≤ **3% NAV**; sum of open max losses ≤ **25% NAV**; ≤ **2** open positions per underlying; ≤ **5** new positions per calendar week.
- CSP collateral (strike × 100) ≤ **20% NAV** per position.
- Entry **30-60 DTE** (calendars: front 20-40, back 50-90); short strikes **0.16-0.30 |delta|**.
- Liquidity: open interest ≥ **500** every leg; bid-ask ≤ **10% of mid** (ETFs: or ≤ **$0.05**).
- Credit trades: take profit at **50%** of max profit, stop at loss = **2× credit**. Debit trades: stop at **50%** loss of debit. Close/roll at **21 DTE**.
- Fill model: buy at mid + **25%** of (ask − bid); sell at mid − 25% of (ask − bid); **$0.65** per contract. Marks use mid.
- Benchmarks: Cboe **BXM** and **PUT** indexes + cash.
- Commits: message body ends with `AI-assisted change.` then a blank line then `Signed-off-by: hmadhani2024@gmail.com`. Never `Co-Authored-By`. Push directly to `main`. Never use the `gh` CLI.
- Run tests with: `cd /Users/hmadhani/finance-portfolio && python3 -m unittest discover -s tests -v`
- Cboe units (verified 2026-09-27): chain-level `iv30` is **percent** (e.g. `11.982`); per-contract `iv` is **decimal** (e.g. `0.1315`); `theta` is **$ per share per calendar day**; `vega` is **$ per share per 1 IV point**. OCC option symbol = root + `YYMMDD` + `C|P` + strike×1000 zero-padded to 8 digits (e.g. `SPY261106C00771000`).

## Deviation from spec (deliberate)

- `mark` reads **`options/data/positions.json`** (machine-readable state) rather than parsing `options-portfolio.md`. Parsing markdown tables is fragile; the routine keeps both in sync. The spec allowed "or JSON".
- The canonical routine prompt is stored in the repo at `options/routine-prompt.md` so it is reviewable and diffable; the cloud routine embeds a copy.

## File Structure

| File | Responsibility |
|---|---|
| `scripts/optlib/__init__.py` | Package marker |
| `scripts/optlib/bs.py` | Black-Scholes price, Greeks, probability ITM |
| `scripts/optlib/chain.py` | Cboe fetch (with fixture override), OCC parsing, `Contract`, liquidity filter, expected move, delta-bucket selection |
| `scripts/optlib/ivhist.py` | IV history CSV append (idempotent), IV rank/percentile, VIX percentile |
| `scripts/optlib/strategy.py` | `Leg`, leg-spec parsing, fill model, fees, payoff, `analyze()`, ASCII payoff diagram |
| `scripts/optlib/marks.py` | Mark open positions from `positions.json`, rule triggers |
| `scripts/options_data.py` | CLI: `regime`, `scan`, `price-spread`, `mark`, `record-iv` |
| `tests/__init__.py`, `tests/helpers.py` | Synthetic Cboe-shaped chain + fixture-dir builder |
| `tests/test_bs.py`, `test_chain.py`, `test_ivhist.py`, `test_strategy.py`, `test_marks.py`, `test_cli.py` | Unit/CLI tests |
| `options/investor-profile.md` | Persona + every rule |
| `options/options-portfolio.md` | Human-readable portfolio state |
| `options/learning-ledger.md` | Primer, Concept Index, decision entries |
| `options/RESOURCES.md` | Verified, sourced reading list |
| `options/DECISION.md` | Deferred simplifications |
| `options/routine-prompt.md` | Canonical cloud-routine prompt |
| `options/data/positions.json` | Open positions (machine state) |
| `options/data/iv-history.csv` | Daily iv30 per symbol |
| `README.md` (modify) | Mention the options portfolio |
| `~/.claude/skills/hm-options-portfolio/SKILL.md` | Skill for manual runs |

---

### Task 1: Black-Scholes core

**Files:**
- Create: `scripts/optlib/__init__.py`, `scripts/optlib/bs.py`
- Create: `tests/__init__.py`, `tests/test_bs.py`

**Interfaces:**
- Produces: `norm_cdf(x) -> float`, `norm_pdf(x) -> float`, `bs_price(S, K, T, r, sigma, kind) -> float`, `bs_greeks(S, K, T, r, sigma, kind) -> dict[str, float]` (keys `delta`, `gamma`, `theta` per calendar day, `vega` per 1 vol point), `prob_itm(S, K, T, r, sigma, kind) -> float`. `kind` is `"C"` or `"P"`; `T` in years; `sigma` decimal.

- [ ] **Step 1: Write the failing tests**

`tests/__init__.py`: empty file.

`tests/test_bs.py`:
```python
import os
import sys
import math
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

from optlib.bs import bs_price, bs_greeks, prob_itm, norm_cdf


class TestBlackScholes(unittest.TestCase):
    # Hull, "Options, Futures, and Other Derivatives", worked example:
    # S=42, K=40, r=10%, sigma=20%, T=0.5 -> call 4.76, put 0.81
    def test_hull_example_call_and_put(self):
        self.assertAlmostEqual(bs_price(42, 40, 0.5, 0.10, 0.20, "C"), 4.76, places=2)
        self.assertAlmostEqual(bs_price(42, 40, 0.5, 0.10, 0.20, "P"), 0.81, places=2)

    def test_put_call_parity(self):
        S, K, T, r, sig = 100.0, 95.0, 0.25, 0.04, 0.3
        c = bs_price(S, K, T, r, sig, "C")
        p = bs_price(S, K, T, r, sig, "P")
        self.assertAlmostEqual(c - p, S - K * math.exp(-r * T), places=6)

    def test_expired_option_is_intrinsic(self):
        self.assertEqual(bs_price(105, 100, 0, 0.04, 0.2, "C"), 5.0)
        self.assertEqual(bs_price(105, 100, 0, 0.04, 0.2, "P"), 0.0)

    def test_greeks_signs_and_hull_delta(self):
        g = bs_greeks(42, 40, 0.5, 0.10, 0.20, "C")
        self.assertAlmostEqual(g["delta"], 0.7791, places=3)
        self.assertGreater(g["gamma"], 0)
        self.assertLess(g["theta"], 0)
        self.assertGreater(g["vega"], 0)
        gp = bs_greeks(42, 40, 0.5, 0.10, 0.20, "P")
        self.assertAlmostEqual(g["delta"] - gp["delta"], 1.0, places=6)

    def test_theta_is_per_day_and_vega_per_point(self):
        # ATM 40-day SPY-like call: theta ~ -0.16/day, vega ~ 1.0 per vol point
        g = bs_greeks(771.35, 771, 40 / 365, 0.04, 0.1315, "C")
        self.assertTrue(-0.25 < g["theta"] < -0.10, g["theta"])
        self.assertTrue(0.8 < g["vega"] < 1.3, g["vega"])

    def test_prob_itm(self):
        self.assertAlmostEqual(prob_itm(100, 100, 1e-9, 0.0, 0.2, "C"), 0.5, places=2)
        self.assertEqual(prob_itm(110, 100, 0, 0.04, 0.2, "C"), 1.0)
        self.assertEqual(prob_itm(110, 100, 0, 0.04, 0.2, "P"), 0.0)
        self.assertAlmostEqual(norm_cdf(0), 0.5)


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd /Users/hmadhani/finance-portfolio && python3 -m unittest tests.test_bs -v`
Expected: FAIL / ERROR with `ModuleNotFoundError: No module named 'optlib'`

- [ ] **Step 3: Implement**

`scripts/optlib/__init__.py`:
```python
"""optlib — deterministic options math for the finance-portfolio options paper portfolio."""
```

`scripts/optlib/bs.py`:
```python
"""Black-Scholes pricing and Greeks (European exercise, no dividends). Stdlib only.

Conventions: T in years, sigma and r as decimals, kind "C" or "P".
Greeks: delta and gamma per $1 of underlying, theta per calendar day,
vega per 1 volatility point (0.01) — the same units Cboe publishes.
"""
import math


def norm_cdf(x: float) -> float:
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def norm_pdf(x: float) -> float:
    return math.exp(-0.5 * x * x) / math.sqrt(2.0 * math.pi)


def _intrinsic(S: float, K: float, kind: str) -> float:
    return max(0.0, S - K) if kind == "C" else max(0.0, K - S)


def _d1_d2(S, K, T, r, sigma):
    v = sigma * math.sqrt(T)
    d1 = (math.log(S / K) + (r + 0.5 * sigma * sigma) * T) / v
    return d1, d1 - v


def bs_price(S: float, K: float, T: float, r: float, sigma: float, kind: str) -> float:
    if T <= 0 or sigma <= 0:
        return _intrinsic(S, K, kind)
    d1, d2 = _d1_d2(S, K, T, r, sigma)
    if kind == "C":
        return S * norm_cdf(d1) - K * math.exp(-r * T) * norm_cdf(d2)
    return K * math.exp(-r * T) * norm_cdf(-d2) - S * norm_cdf(-d1)


def bs_greeks(S: float, K: float, T: float, r: float, sigma: float, kind: str) -> dict:
    d1, d2 = _d1_d2(S, K, T, r, sigma)
    pdf = norm_pdf(d1)
    sq = math.sqrt(T)
    disc = math.exp(-r * T)
    gamma = pdf / (S * sigma * sq)
    vega = S * pdf * sq / 100.0
    decay = -S * pdf * sigma / (2.0 * sq)
    if kind == "C":
        delta = norm_cdf(d1)
        theta = (decay - r * K * disc * norm_cdf(d2)) / 365.0
    else:
        delta = norm_cdf(d1) - 1.0
        theta = (decay + r * K * disc * norm_cdf(-d2)) / 365.0
    return {"delta": delta, "gamma": gamma, "theta": theta, "vega": vega}


def prob_itm(S: float, K: float, T: float, r: float, sigma: float, kind: str) -> float:
    """Risk-neutral probability the option finishes in the money."""
    if T <= 0 or sigma <= 0:
        return 1.0 if _intrinsic(S, K, kind) > 0 else 0.0
    _, d2 = _d1_d2(S, K, T, r, sigma)
    return norm_cdf(d2) if kind == "C" else norm_cdf(-d2)
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `cd /Users/hmadhani/finance-portfolio && python3 -m unittest tests.test_bs -v`
Expected: 6 tests, OK

- [ ] **Step 5: Commit**

```bash
cd /Users/hmadhani/finance-portfolio
git add scripts/optlib/__init__.py scripts/optlib/bs.py tests/__init__.py tests/test_bs.py
git commit -m "optlib: Black-Scholes price, Greeks, prob ITM

AI-assisted change.

Signed-off-by: hmadhani2024@gmail.com"
```

---

### Task 2: Chain parsing, liquidity filter, test fixtures

**Files:**
- Create: `scripts/optlib/chain.py`
- Create: `tests/helpers.py`, `tests/test_chain.py`

**Interfaces:**
- Consumes: `bs_price`, `bs_greeks` (Task 1) — only in `tests/helpers.py`.
- Produces (in `optlib.chain`):
  - Constants `CBOE_OPTIONS_URL`, `CBOE_QUOTE_URL`, `VIX_HISTORY_URL`, `FIXTURE_ENV = "OPTIONS_FIXTURE_DIR"`, `STOCK_EXPIRY = date(9999, 12, 31)`.
  - `fetch_text(url: str, fixture_name: str) -> str` — reads `$OPTIONS_FIXTURE_DIR/<fixture_name>` when that env var is set, else HTTP GET.
  - `load_chain(symbol) -> dict` (the Cboe `data` object), `load_quote(symbol) -> dict`, `load_vix_history() -> str`.
  - `parse_occ(option: str) -> tuple[str, date, str, float]` → `(root, expiry, kind, strike)`; `occ_symbol(root, expiry, kind, strike) -> str`.
  - `@dataclass Contract(option, root, expiry, kind, strike, bid, ask, iv, delta, gamma, theta, vega, open_interest, volume)` with property `mid` and methods `dte(asof) -> int`, `row(asof) -> dict`.
  - `stock_contract(root, spot) -> Contract` (kind `"S"`, used for assigned shares).
  - `contracts(chain: dict) -> list[Contract]`, `index_contracts(cs) -> dict[str, Contract]` keyed by OCC symbol.
  - `is_liquid(c, min_oi=500, max_spread_pct=0.10, abs_spread_ok=None) -> bool`.
  - `expected_move(price, iv_decimal, dte) -> float`.
  - `select_expiries(cs, asof, dte_min, dte_max, max_expiries=2) -> list[date]`.
  - `delta_buckets(cs, asof, expiry, targets, liquid_kwargs) -> list[Contract]`.
- Produces (in `tests.helpers`): `make_chain(...) -> dict` (full Cboe response `{"timestamp", "data"}`), `make_contract(option, bid, ask, iv=0.2, delta=0.0, oi=1000) -> Contract`, `write_fixture_dir(path, chains: dict[str, dict], vix=15.0, vix3m=17.0, bxm=2560.6, put=3675.7, vix_closes=None) -> None`.

- [ ] **Step 1: Write the test helpers**

`tests/helpers.py`:
```python
"""Synthetic, deterministic Cboe-shaped data for tests."""
import json
import os
import sys
from datetime import date

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

from optlib.bs import bs_price, bs_greeks
from optlib.chain import Contract, occ_symbol, parse_occ

ASOF = date(2026, 9, 28)
EXPIRY = date(2026, 11, 6)  # 39 DTE from ASOF


def make_chain(symbol="TEST", spot=100.0, asof=ASOF, expiries=(EXPIRY,),
               strikes=range(80, 121, 5), iv=0.20, oi=1000, width=0.10):
    opts = []
    for exp in expiries:
        T = (exp - asof).days / 365.0
        for k in strikes:
            for kind in "CP":
                p = bs_price(spot, k, T, 0.04, iv, kind)
                g = bs_greeks(spot, k, T, 0.04, iv, kind)
                bid = max(round(p - width / 2, 2), 0.0)
                ask = round(bid + width, 2)
                opts.append({
                    "option": occ_symbol(symbol, exp, kind, k),
                    "bid": bid, "ask": ask, "iv": iv,
                    "open_interest": oi, "volume": 100,
                    "delta": round(g["delta"], 4), "gamma": round(g["gamma"], 4),
                    "theta": round(g["theta"], 4), "vega": round(g["vega"], 4),
                })
    return {"timestamp": f"{asof} 15:00:00",
            "data": {"symbol": symbol, "current_price": spot, "close": spot,
                     "iv30": iv * 100, "options": opts}}


def make_contract(option, bid, ask, iv=0.2, delta=0.0, oi=1000):
    root, exp, kind, strike = parse_occ(option)
    return Contract(option, root, exp, kind, strike, bid, ask, iv, delta,
                    0.0, 0.0, 0.0, oi, 0)


def write_fixture_dir(path, chains, vix=15.0, vix3m=17.0, bxm=2560.6, put=3675.7,
                      vix_closes=None):
    os.makedirs(path, exist_ok=True)
    for sym, payload in chains.items():
        with open(os.path.join(path, f"{sym}.json"), "w") as f:
            json.dump(payload, f)
    for sym, px in (("_VIX", vix), ("_VIX3M", vix3m), ("_BXM", bxm), ("_PUT", put)):
        with open(os.path.join(path, f"{sym}.json"), "w") as f:
            json.dump({"data": {"symbol": sym, "current_price": px, "close": px}}, f)
    closes = vix_closes if vix_closes is not None else [10 + i * 0.05 for i in range(300)]
    with open(os.path.join(path, "VIX_History.csv"), "w") as f:
        f.write("DATE,OPEN,HIGH,LOW,CLOSE\n")
        for i, c in enumerate(closes):
            f.write(f"01/{(i % 28) + 1:02d}/2025,{c},{c},{c},{c}\n")
```

- [ ] **Step 2: Write the failing tests**

`tests/test_chain.py`:
```python
import os
import unittest
from datetime import date

from tests.helpers import make_chain, make_contract, ASOF, EXPIRY
from optlib import chain as ch


class TestOcc(unittest.TestCase):
    def test_parse_and_build_roundtrip(self):
        root, exp, kind, strike = ch.parse_occ("SPY261106C00771000")
        self.assertEqual((root, exp, kind, strike), ("SPY", date(2026, 11, 6), "C", 771.0))
        self.assertEqual(ch.occ_symbol("SPY", date(2026, 11, 6), "C", 771.0), "SPY261106C00771000")

    def test_fractional_strike_and_long_root(self):
        self.assertEqual(ch.parse_occ("GOOGL261106P00172500")[3], 172.5)
        self.assertEqual(ch.parse_occ("GOOGL261106P00172500")[0], "GOOGL")


class TestContracts(unittest.TestCase):
    def setUp(self):
        self.cs = ch.contracts(make_chain()["data"])

    def test_contract_count_and_mid(self):
        self.assertEqual(len(self.cs), 9 * 2)
        c = self.cs[0]
        self.assertAlmostEqual(c.mid, (c.bid + c.ask) / 2, places=4)
        self.assertEqual(c.dte(ASOF), 39)

    def test_index_by_symbol(self):
        idx = ch.index_contracts(self.cs)
        self.assertIn("TEST261106P00095000", idx)

    def test_stock_contract(self):
        s = ch.stock_contract("KO", 87.66)
        self.assertEqual((s.kind, s.bid, s.ask, s.delta), ("S", 87.66, 87.66, 1.0))
        self.assertEqual(s.expiry, ch.STOCK_EXPIRY)


class TestLiquidity(unittest.TestCase):
    def test_rules(self):
        ok = make_contract("X261106P00095000", 1.00, 1.08, oi=600)
        wide = make_contract("X261106P00095000", 1.00, 1.30, oi=600)
        thin = make_contract("X261106P00095000", 1.00, 1.05, oi=100)
        zero_bid = make_contract("X261106P00095000", 0.0, 0.05, oi=5000)
        cheap_etf = make_contract("X261106P00095000", 0.20, 0.25, oi=5000)
        self.assertTrue(ch.is_liquid(ok))
        self.assertFalse(ch.is_liquid(wide))
        self.assertFalse(ch.is_liquid(thin))
        self.assertFalse(ch.is_liquid(zero_bid))
        self.assertFalse(ch.is_liquid(cheap_etf))            # 0.05 wide on 0.225 mid = 22%
        self.assertTrue(ch.is_liquid(cheap_etf, abs_spread_ok=0.05))


class TestSelection(unittest.TestCase):
    def test_expected_move(self):
        self.assertAlmostEqual(ch.expected_move(100, 0.20, 365), 20.0, places=6)
        self.assertAlmostEqual(ch.expected_move(100, 0.20, 36.5), 20.0 * (0.1 ** 0.5), places=6)

    def test_select_expiries_in_window(self):
        exps = (date(2026, 10, 9), date(2026, 11, 6), date(2026, 11, 20), date(2026, 12, 31))
        cs = ch.contracts(make_chain(expiries=exps)["data"])
        self.assertEqual(ch.select_expiries(cs, ASOF, 30, 60), [date(2026, 11, 6), date(2026, 11, 20)])
        self.assertEqual(ch.select_expiries(cs, ASOF, 30, 60, max_expiries=1), [date(2026, 11, 6)])

    def test_delta_buckets_pick_nearest_liquid(self):
        cs = ch.contracts(make_chain(strikes=range(70, 131, 1), width=0.05)["data"])
        picked = ch.delta_buckets(cs, ASOF, EXPIRY, [0.16, 0.30, 0.50], {"abs_spread_ok": 0.05})
        puts = [c for c in picked if c.kind == "P"]
        calls = [c for c in picked if c.kind == "C"]
        self.assertEqual(len(puts), 3)
        self.assertEqual(len(calls), 3)
        best16 = min((c for c in cs if c.kind == "P"), key=lambda c: abs(abs(c.delta) - 0.16))
        self.assertIn(best16.option, [c.option for c in puts])


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 3: Run tests to verify they fail**

Run: `cd /Users/hmadhani/finance-portfolio && python3 -m unittest tests.test_chain -v`
Expected: ERROR — `ImportError: cannot import name ... from 'optlib.chain'` / `ModuleNotFoundError`

- [ ] **Step 4: Implement**

`scripts/optlib/chain.py`:
```python
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
```

- [ ] **Step 5: Run tests to verify they pass**

Run: `cd /Users/hmadhani/finance-portfolio && python3 -m unittest tests.test_chain tests.test_bs -v`
Expected: all OK

- [ ] **Step 6: Commit**

```bash
cd /Users/hmadhani/finance-portfolio
git add scripts/optlib/chain.py tests/helpers.py tests/test_chain.py
git commit -m "optlib: Cboe chain parsing, liquidity filter, delta buckets

AI-assisted change.

Signed-off-by: hmadhani2024@gmail.com"
```

---

### Task 3: IV history and IV rank

**Files:**
- Create: `scripts/optlib/ivhist.py`
- Create: `tests/test_ivhist.py`

**Interfaces:**
- Produces (in `optlib.ivhist`): `FIELDS = ["date", "symbol", "iv30", "price"]`, `MIN_OBS = 20`,
  `record(path: str, day: str, rows: list[tuple[str, float, float]]) -> int` (rows are `(symbol, iv30_percent, price)`; returns count appended; idempotent per `(day, symbol)`),
  `history(path: str, symbol: str, lookback: int = 252) -> list[float]` (iv30 percent values, oldest first),
  `iv_rank(values: list[float], current: float) -> dict` (keys `iv_rank`, `iv_percentile`, `n_obs`, `note`),
  `vix_percentile(csv_text: str, current: float, lookback: int = 252) -> float`.

- [ ] **Step 1: Write the failing tests**

`tests/test_ivhist.py`:
```python
import os
import tempfile
import unittest

import tests.helpers  # noqa: F401  (adds scripts/ to sys.path)
from optlib import ivhist


class TestRecord(unittest.TestCase):
    def test_append_and_idempotent(self):
        with tempfile.TemporaryDirectory() as d:
            p = os.path.join(d, "iv.csv")
            self.assertEqual(ivhist.record(p, "2026-09-28", [("SPY", 11.982, 771.35), ("QQQ", 15.1, 745.4)]), 2)
            self.assertEqual(ivhist.record(p, "2026-09-28", [("SPY", 12.5, 772.0)]), 0)
            self.assertEqual(ivhist.record(p, "2026-09-29", [("SPY", 12.5, 772.0)]), 1)
            with open(p) as f:
                lines = f.read().strip().splitlines()
            self.assertEqual(lines[0], "date,symbol,iv30,price")
            self.assertEqual(len(lines), 4)
            self.assertEqual(ivhist.history(p, "SPY"), [11.982, 12.5])

    def test_history_missing_file(self):
        self.assertEqual(ivhist.history("/nonexistent/iv.csv", "SPY"), [])


class TestRank(unittest.TestCase):
    def test_insufficient_history(self):
        r = ivhist.iv_rank([10.0] * 5, 12.0)
        self.assertIsNone(r["iv_rank"])
        self.assertEqual(r["n_obs"], 5)
        self.assertIn("VIX percentile", r["note"])

    def test_rank_and_percentile(self):
        values = [10.0 + i for i in range(21)]  # 10..30
        r = ivhist.iv_rank(values, 25.0)
        self.assertEqual(r["iv_rank"], 75.0)                 # (25-10)/(30-10)
        self.assertAlmostEqual(r["iv_percentile"], 15 / 21 * 100, places=1)

    def test_rank_clamped(self):
        values = [10.0 + i for i in range(21)]
        self.assertEqual(ivhist.iv_rank(values, 40.0)["iv_rank"], 100.0)
        self.assertEqual(ivhist.iv_rank(values, 5.0)["iv_rank"], 0.0)

    def test_vix_percentile(self):
        csv_text = "DATE,OPEN,HIGH,LOW,CLOSE\n" + "".join(
            f"01/01/2025,{c},{c},{c},{c}\n" for c in range(1, 101))
        self.assertEqual(ivhist.vix_percentile(csv_text, 50.5, lookback=100), 50.0)
        self.assertEqual(ivhist.vix_percentile(csv_text, 50.5, lookback=10), 0.0)  # last 10 are 91..100


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run to verify failure**

Run: `cd /Users/hmadhani/finance-portfolio && python3 -m unittest tests.test_ivhist -v`
Expected: ERROR — `ImportError: cannot import name 'ivhist'`

- [ ] **Step 3: Implement**

`scripts/optlib/ivhist.py`:
```python
"""Daily 30-day implied-volatility history and IV rank.

IV rank = where today's IV sits between the lowest and highest IV of the
lookback window (0 = at the low, 100 = at the high). IV percentile = share of
days in the window with IV below today's. Both need history, which this
portfolio builds itself from inception — until MIN_OBS days exist, callers
fall back to the VIX percentile as a market-wide proxy.
"""
import csv
import io
import os

FIELDS = ["date", "symbol", "iv30", "price"]
MIN_OBS = 20


def _rows(path: str) -> list:
    if not os.path.exists(path) or os.path.getsize(path) == 0:
        return []
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


def record(path: str, day: str, rows: list) -> int:
    existing = {(r["date"], r["symbol"]) for r in _rows(path)}
    new = [r for r in rows if (day, r[0]) not in existing]
    write_header = not os.path.exists(path) or os.path.getsize(path) == 0
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    with open(path, "a", newline="") as f:
        w = csv.writer(f)
        if write_header:
            w.writerow(FIELDS)
        for symbol, iv30, price in new:
            w.writerow([day, symbol, f"{iv30:.3f}", f"{price:.2f}"])
    return len(new)


def history(path: str, symbol: str, lookback: int = 252) -> list:
    rows = sorted((r for r in _rows(path) if r["symbol"] == symbol), key=lambda r: r["date"])
    return [float(r["iv30"]) for r in rows][-lookback:]


def iv_rank(values: list, current: float) -> dict:
    n = len(values)
    if n < MIN_OBS:
        return {"iv_rank": None, "iv_percentile": None, "n_obs": n,
                "note": f"only {n} days of IV history (need {MIN_OBS}); use the VIX percentile as the regime proxy"}
    lo, hi = min(values), max(values)
    rank = 0.0 if hi == lo else (current - lo) / (hi - lo) * 100.0
    pct = sum(1 for v in values if v < current) / n * 100.0
    return {"iv_rank": round(max(0.0, min(100.0, rank)), 1),
            "iv_percentile": round(pct, 1), "n_obs": n, "note": ""}


def vix_percentile(csv_text: str, current: float, lookback: int = 252) -> float:
    closes = [float(r["CLOSE"]) for r in csv.DictReader(io.StringIO(csv_text))][-lookback:]
    return round(sum(1 for c in closes if c < current) / len(closes) * 100.0, 1)
```

- [ ] **Step 4: Run to verify pass**

Run: `cd /Users/hmadhani/finance-portfolio && python3 -m unittest tests.test_ivhist -v`
Expected: 6 tests OK

- [ ] **Step 5: Commit**

```bash
cd /Users/hmadhani/finance-portfolio
git add scripts/optlib/ivhist.py tests/test_ivhist.py
git commit -m "optlib: IV history CSV, IV rank/percentile, VIX percentile

AI-assisted change.

Signed-off-by: hmadhani2024@gmail.com"
```

---

### Task 4: Strategy math — fills, payoff, analysis, ASCII diagram

**Files:**
- Create: `scripts/optlib/strategy.py`
- Create: `tests/test_strategy.py`

**Interfaces:**
- Consumes: `bs_price`, `norm_cdf` (Task 1); `Contract`, `index_contracts`, `occ_symbol`, `stock_contract` (Task 2).
- Produces (in `optlib.strategy`):
  - Constants `MULTIPLIER = 100`, `FEE_PER_CONTRACT = 0.65`, `SLIPPAGE_FRACTION = 0.25`, `RISK_FREE = 0.04`.
  - `@dataclass Leg(action: str, ratio: int, contract: Contract)` with property `sign` (+1 BUY, −1 SELL).
  - `parse_leg_spec(spec: str) -> list[tuple[str, int, str, float, date]]` — spec like `"SELL 1 P 95 2026-11-06; BUY 1 P 90 2026-11-06"`.
  - `legs_from_spec(spec, root, cs_index, spot=None, with_stock=False) -> list[Leg]` — raises `KeyError` naming the missing OCC symbol.
  - `fill_price(leg) -> float`, `entry_cost(legs) -> float` (per share per unit; + debit, − credit), `fees(legs, qty) -> float` (one side).
  - `value_at(legs, S, eval_date) -> float` (per share per unit), `pnl_at(legs, S, eval_date, cost) -> float` ($ per unit, excl. fees).
  - `analyze(legs, qty, spot, asof) -> dict` with keys: `entry_cost_per_share`, `credit_or_debit`, `qty`, `fills` (list of `{option, action, ratio, fill}`), `max_profit`, `max_loss`, `unbounded_profit`, `unbounded_loss`, `defined_risk`, `breakevens`, `prob_profit`, `net_greeks` (`delta_shares`, `gamma`, `theta_per_day`, `vega_per_point`), `fees_round_trip`, `eval_date`.
  - `ascii_payoff(legs, qty, spot, width=51, height=11) -> str`.

- [ ] **Step 1: Write the failing tests**

`tests/test_strategy.py`:
```python
import unittest

from tests.helpers import make_chain, make_contract, ASOF, EXPIRY
from optlib import chain as ch
from optlib import strategy as st


def legs(spec, spot=100.0, with_stock=False, **chain_kwargs):
    cs = ch.contracts(make_chain(spot=spot, **chain_kwargs)["data"])
    return st.legs_from_spec(spec, "TEST", ch.index_contracts(cs), spot=spot, with_stock=with_stock)


class TestSpecAndFills(unittest.TestCase):
    def test_parse_leg_spec(self):
        parsed = st.parse_leg_spec("SELL 1 P 95 2026-11-06; buy 1 p 90 2026-11-06")
        self.assertEqual(parsed[0], ("SELL", 1, "P", 95.0, EXPIRY))
        self.assertEqual(parsed[1][0:3], ("BUY", 1, "P"))

    def test_bad_spec_raises(self):
        with self.assertRaises(ValueError):
            st.parse_leg_spec("SELL P 95")
        with self.assertRaises(ValueError):
            st.parse_leg_spec("HOLD 1 P 95 2026-11-06")

    def test_missing_strike_raises_keyerror(self):
        with self.assertRaises(KeyError):
            legs("SELL 1 P 97 2026-11-06")

    def test_fill_model(self):
        c = make_contract("TEST261106P00095000", 1.00, 1.20)
        self.assertAlmostEqual(st.fill_price(st.Leg("BUY", 1, c)), 1.15)
        self.assertAlmostEqual(st.fill_price(st.Leg("SELL", 1, c)), 1.05)

    def test_fees(self):
        L = legs("SELL 1 P 95 2026-11-06; BUY 1 P 90 2026-11-06")
        self.assertAlmostEqual(st.fees(L, 3), 2 * 3 * 0.65)


class TestAnalyze(unittest.TestCase):
    def test_credit_put_spread_exact_values(self):
        L = legs("SELL 1 P 95 2026-11-06; BUY 1 P 90 2026-11-06")
        a = st.analyze(L, 2, 100.0, ASOF)
        credit = -a["entry_cost_per_share"]
        self.assertGreater(credit, 0)
        self.assertEqual(a["credit_or_debit"], "credit")
        self.assertAlmostEqual(a["max_profit"], credit * 100 * 2, places=1)
        self.assertAlmostEqual(a["max_loss"], -(5 - credit) * 100 * 2, places=1)
        self.assertEqual(len(a["breakevens"]), 1)
        self.assertAlmostEqual(a["breakevens"][0], 95 - credit, places=2)
        self.assertTrue(a["defined_risk"])
        self.assertTrue(0.5 < a["prob_profit"] < 0.95, a["prob_profit"])
        self.assertGreater(a["net_greeks"]["theta_per_day"], 0)   # short premium earns theta
        self.assertGreater(a["net_greeks"]["delta_shares"], 0)    # bullish
        self.assertAlmostEqual(a["fees_round_trip"], 2 * 2 * 2 * 0.65)

    def test_iron_condor(self):
        L = legs("BUY 1 P 85 2026-11-06; SELL 1 P 90 2026-11-06; "
                 "SELL 1 C 110 2026-11-06; BUY 1 C 115 2026-11-06")
        a = st.analyze(L, 1, 100.0, ASOF)
        credit = -a["entry_cost_per_share"]
        self.assertAlmostEqual(a["max_loss"], -(5 - credit) * 100, places=1)
        self.assertEqual(len(a["breakevens"]), 2)
        self.assertAlmostEqual(a["breakevens"][0], 90 - credit, places=2)
        self.assertAlmostEqual(a["breakevens"][1], 110 + credit, places=2)

    def test_long_call_is_defined_risk_unbounded_profit(self):
        a = st.analyze(legs("BUY 1 C 100 2026-11-06"), 1, 100.0, ASOF)
        self.assertTrue(a["unbounded_profit"])
        self.assertTrue(a["defined_risk"])
        self.assertAlmostEqual(a["max_loss"], -a["entry_cost_per_share"] * 100, places=1)

    def test_naked_short_call_rejected(self):
        a = st.analyze(legs("SELL 1 C 110 2026-11-06"), 1, 100.0, ASOF)
        self.assertTrue(a["unbounded_loss"])
        self.assertFalse(a["defined_risk"])

    def test_calendar_is_defined_risk(self):
        L = legs("SELL 1 C 100 2026-11-06; BUY 1 C 100 2026-12-18",
                 expiries=(EXPIRY, __import__("datetime").date(2026, 12, 18)))
        a = st.analyze(L, 1, 100.0, ASOF)
        self.assertEqual(a["eval_date"], EXPIRY.isoformat())
        self.assertTrue(a["defined_risk"])
        self.assertEqual(a["credit_or_debit"], "debit")

    def test_covered_call_with_stock(self):
        L = legs("SELL 1 C 110 2026-11-06", with_stock=True)
        a = st.analyze(L, 1, 100.0, ASOF)
        self.assertTrue(a["defined_risk"])                 # short call covered by shares
        self.assertAlmostEqual(a["net_greeks"]["delta_shares"], 100 - 100 * L[0].contract.delta, places=0)


class TestAscii(unittest.TestCase):
    def test_shape(self):
        L = legs("SELL 1 P 95 2026-11-06; BUY 1 P 90 2026-11-06")
        art = st.ascii_payoff(L, 1, 100.0, width=41, height=9)
        lines = art.splitlines()
        self.assertEqual(len(lines), 9 + 2)
        self.assertIn("*", art)
        self.assertIn("|", art)


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run to verify failure**

Run: `cd /Users/hmadhani/finance-portfolio && python3 -m unittest tests.test_strategy -v`
Expected: ERROR — `ImportError: cannot import name 'strategy'`

- [ ] **Step 3: Implement**

`scripts/optlib/strategy.py`:
```python
"""Multi-leg option position math: fills, payoff, max P&L, breakevens,
probability of profit, net Greeks, ASCII payoff diagram.

Units: prices per share; one "unit" of a position = each leg's `ratio`
contracts; `qty` multiplies units. One contract = MULTIPLIER shares.
entry_cost > 0 means a debit paid, < 0 a credit received.
Payoff is evaluated at the earliest leg expiry; legs expiring later are
valued with Black-Scholes at their own IV (this handles calendars/diagonals).
"""
import math
from dataclasses import dataclass
from datetime import date

from .bs import bs_price, norm_cdf
from .chain import Contract, occ_symbol, stock_contract

MULTIPLIER = 100
FEE_PER_CONTRACT = 0.65
SLIPPAGE_FRACTION = 0.25
RISK_FREE = 0.04


@dataclass
class Leg:
    action: str  # "BUY" or "SELL"
    ratio: int
    contract: Contract

    @property
    def sign(self) -> int:
        return 1 if self.action == "BUY" else -1


def parse_leg_spec(spec: str) -> list:
    out = []
    for part in spec.split(";"):
        toks = part.split()
        if len(toks) != 5:
            raise ValueError(f"bad leg spec {part.strip()!r}: want 'ACTION RATIO C|P STRIKE YYYY-MM-DD'")
        action, ratio, kind, strike, exp = toks
        action, kind = action.upper(), kind.upper()
        if action not in ("BUY", "SELL") or kind not in ("C", "P"):
            raise ValueError(f"bad leg spec {part.strip()!r}: action BUY|SELL, kind C|P")
        out.append((action, int(ratio), kind, float(strike), date.fromisoformat(exp)))
    return out


def legs_from_spec(spec: str, root: str, cs_index: dict, spot: float = None,
                   with_stock: bool = False) -> list:
    legs = []
    for action, ratio, kind, strike, exp in parse_leg_spec(spec):
        sym = occ_symbol(root, exp, kind, strike)
        if sym not in cs_index:
            raise KeyError(f"no quote for {sym} ({action} {kind} {strike} {exp})")
        legs.append(Leg(action, ratio, cs_index[sym]))
    if with_stock:
        legs.append(Leg("BUY", 1, stock_contract(root, spot)))
    return legs


def fill_price(leg: Leg) -> float:
    c = leg.contract
    if c.kind == "S":
        return c.mid
    half = SLIPPAGE_FRACTION * (c.ask - c.bid)
    return round(c.mid + half if leg.action == "BUY" else c.mid - half, 4)


def entry_cost(legs: list) -> float:
    return round(sum(l.sign * l.ratio * fill_price(l) for l in legs), 4)


def fees(legs: list, qty: int) -> float:
    return round(sum(l.ratio for l in legs if l.contract.kind != "S") * qty * FEE_PER_CONTRACT, 2)


def _eval_date(legs: list) -> date:
    return min(l.contract.expiry for l in legs)


def value_at(legs: list, S: float, eval_date: date) -> float:
    total = 0.0
    for l in legs:
        c = l.contract
        if c.kind == "S":
            v = S
        else:
            T = max(0, (c.expiry - eval_date).days) / 365.0
            v = bs_price(S, c.strike, T, RISK_FREE, c.iv, c.kind)
        total += l.sign * l.ratio * v
    return total


def pnl_at(legs: list, S: float, eval_date: date, cost: float) -> float:
    return (value_at(legs, S, eval_date) - cost) * MULTIPLIER


def _grid(legs: list, spot: float, n: int = 2000) -> list:
    strikes = [l.contract.strike for l in legs if l.contract.kind != "S"]
    hi = max(strikes + [spot]) * 2.0
    return sorted(set([hi * i / n for i in range(1, n + 1)] + strikes))


def analyze(legs: list, qty: int, spot: float, asof: date) -> dict:
    ev = _eval_date(legs)
    cost = entry_cost(legs)
    grid = _grid(legs, spot)
    pnls = [pnl_at(legs, S, ev, cost) * qty for S in grid]
    slope_hi = pnls[-1] - pnls[-2]
    unbounded_profit = slope_hi > 1e-6
    unbounded_loss = slope_hi < -1e-6

    breakevens = []
    for i in range(1, len(grid)):
        a, b = pnls[i - 1], pnls[i]
        if a == 0 and (i == 1 or pnls[i - 2] != 0):
            breakevens.append(round(grid[i - 1], 2))
        elif a * b < 0:
            breakevens.append(round(grid[i - 1] + (grid[i] - grid[i - 1]) * (-a) / (b - a), 2))

    opt_legs = [l for l in legs if l.contract.kind != "S"]
    sig = sum(l.contract.iv for l in opt_legs) / len(opt_legs)
    T = max((ev - asof).days, 1) / 365.0
    mu = math.log(spot) + (RISK_FREE - 0.5 * sig * sig) * T
    sd = sig * math.sqrt(T)

    def cdf(x):
        return norm_cdf((math.log(x) - mu) / sd)

    pop = cdf(grid[0]) if pnls[0] > 0 else 0.0
    for i in range(1, len(grid)):
        mid = (grid[i - 1] + grid[i]) / 2
        if pnl_at(legs, mid, ev, cost) > 0:
            pop += cdf(grid[i]) - cdf(grid[i - 1])
    if pnls[-1] > 0:
        pop += 1 - cdf(grid[-1])

    g = {"delta_shares": 0.0, "gamma": 0.0, "theta_per_day": 0.0, "vega_per_point": 0.0}
    for l in legs:
        k = l.sign * l.ratio * qty * MULTIPLIER
        g["delta_shares"] += k * l.contract.delta
        g["gamma"] += k * l.contract.gamma
        g["theta_per_day"] += k * l.contract.theta
        g["vega_per_point"] += k * l.contract.vega

    return {
        "entry_cost_per_share": cost,
        "credit_or_debit": "credit" if cost < 0 else "debit",
        "qty": qty,
        "fills": [{"option": l.contract.option, "action": l.action, "ratio": l.ratio,
                   "fill": fill_price(l)} for l in legs],
        "max_profit": None if unbounded_profit else round(max(pnls), 2),
        "max_loss": None if unbounded_loss else round(min(pnls), 2),
        "unbounded_profit": unbounded_profit,
        "unbounded_loss": unbounded_loss,
        "defined_risk": not unbounded_loss,
        "breakevens": breakevens,
        "prob_profit": round(pop, 3),
        "net_greeks": {k: round(v, 2) for k, v in g.items()},
        "fees_round_trip": round(2 * fees(legs, qty), 2),
        "eval_date": ev.isoformat(),
    }


def ascii_payoff(legs: list, qty: int, spot: float, width: int = 51, height: int = 11) -> str:
    ev = _eval_date(legs)
    cost = entry_cost(legs)
    strikes = [l.contract.strike for l in legs if l.contract.kind != "S"]
    lo, hi = min(strikes + [spot]) * 0.9, max(strikes + [spot]) * 1.1
    xs = [lo + (hi - lo) * i / (width - 1) for i in range(width)]
    ys = [pnl_at(legs, x, ev, cost) * qty for x in xs]
    ymax, ymin = max(max(ys), 0.0), min(min(ys), 0.0)
    span = (ymax - ymin) or 1.0

    def row(y):
        return int(round((ymax - y) / span * (height - 1)))

    canvas = [[" "] * width for _ in range(height)]
    for c in range(width):
        canvas[row(0.0)][c] = "-"
    spot_col = int(round((spot - lo) / (hi - lo) * (width - 1)))
    for r in range(height):
        if canvas[r][spot_col] == " ":
            canvas[r][spot_col] = "|"
    for c, y in enumerate(ys):
        canvas[row(y)][c] = "*"
    lines = []
    for r in range(height):
        label = f"{ymax:>10.0f} " if r == 0 else (f"{ymin:>10.0f} " if r == height - 1 else " " * 11)
        lines.append(label + "".join(canvas[r]))
    half = width // 2
    lines.append(" " * 11 + f"{lo:<{half}.2f}{hi:>{width - half}.2f}")
    lines.append(" " * 11 + "P&L ($) at expiry vs. underlying price.  | = today's price  - = $0 line")
    return "\n".join(lines)
```

- [ ] **Step 4: Run to verify pass**

Run: `cd /Users/hmadhani/finance-portfolio && python3 -m unittest tests.test_strategy -v`
Expected: all OK. If `test_calendar_is_defined_risk` fails on `defined_risk`, inspect `slope_hi` — at 2× the max strike the long back-month call and short front call should have near-equal slopes (value difference tends to a constant); do not loosen the `1e-6` threshold without understanding why.

- [ ] **Step 5: Commit**

```bash
cd /Users/hmadhani/finance-portfolio
git add scripts/optlib/strategy.py tests/test_strategy.py
git commit -m "optlib: multi-leg fills, payoff, breakevens, PoP, Greeks, ASCII payoff

AI-assisted change.

Signed-off-by: hmadhani2024@gmail.com"
```

---

### Task 5: Mark positions and management triggers

**Files:**
- Create: `scripts/optlib/marks.py`
- Create: `tests/test_marks.py`

**Interfaces:**
- Consumes: `Leg`, `MULTIPLIER` (Task 4); `Contract`, `stock_contract` (Task 2); `bs_price` not needed.
- Produces (in `optlib.marks`):
  - `positions.json` schema (the routine writes this):
    ```json
    {"positions": [{"id": "2026-09-28-SPY-PCS-1", "symbol": "SPY", "strategy": "credit_put_spread",
                    "opened": "2026-09-28", "qty": 2, "entry_cost": -1.25,
                    "profit_target_pct": 50,
                    "legs": [{"action": "SELL", "ratio": 1, "option": "SPY261106P00620000"},
                             {"action": "BUY",  "ratio": 1, "option": "SPY261106P00610000"}]}]}
    ```
    `entry_cost` = per-share net fill (+debit / −credit) exactly as `analyze()["entry_cost_per_share"]`. A shares leg uses `"option": "STOCK"`.
  - `mark_position(position: dict, cs_index: dict, spot: float, asof: date) -> dict` with keys `id`, `symbol`, `strategy`, `spot`, `value_per_share`, `pnl`, `pct_of_basis`, `dte`, `triggers` (list drawn from `"profit_target"`, `"stop_loss"`, `"21_dte"`, `"expiration"`, `"assignment"`), `legs` (per-leg `{option, mid, itm}`), `errors`.

Rules implemented:
- value per share = Σ sign·ratio·mid (expired legs → intrinsic from `spot`).
- pnl = (value − entry_cost) × 100 × qty.
- Credit (`entry_cost < 0`): basis = max profit = −entry_cost×100×qty. `profit_target` if pnl ≥ target% × basis; `stop_loss` if pnl ≤ −2 × basis.
- Debit: basis = entry_cost×100×qty. `profit_target` if pnl ≥ target% × basis; `stop_loss` if pnl ≤ −0.5 × basis.
- `21_dte` if min option-leg DTE ≤ 21. `expiration` if ≤ 0. `assignment` if DTE ≤ 0 and any SELL leg is in the money.

- [ ] **Step 1: Write the failing tests**

`tests/test_marks.py`:
```python
import unittest
from datetime import date

from tests.helpers import make_contract
from optlib import marks

ASOF = date(2026, 9, 28)


def pcs_position(entry_cost=-1.00, target=50):
    return {"id": "P1", "symbol": "TEST", "strategy": "credit_put_spread", "opened": "2026-09-01",
            "qty": 2, "entry_cost": entry_cost, "profit_target_pct": target,
            "legs": [{"action": "SELL", "ratio": 1, "option": "TEST261106P00095000"},
                     {"action": "BUY", "ratio": 1, "option": "TEST261106P00090000"}]}


def idx(short_bid, short_ask, long_bid, long_ask, exp="261106"):
    s = make_contract(f"TEST{exp}P00095000", short_bid, short_ask)
    l = make_contract(f"TEST{exp}P00090000", long_bid, long_ask)
    return {s.option: s, l.option: l}


class TestMarks(unittest.TestCase):
    def test_credit_profit_target(self):
        m = marks.mark_position(pcs_position(), idx(0.55, 0.65, 0.15, 0.25), 100.0, ASOF)
        # value = -0.60 + 0.20 = -0.40 ; pnl = (-0.40 - -1.00) * 100 * 2 = 120 ; basis 200 -> 60%
        self.assertAlmostEqual(m["pnl"], 120.0)
        self.assertAlmostEqual(m["pct_of_basis"], 60.0)
        self.assertIn("profit_target", m["triggers"])
        self.assertNotIn("21_dte", m["triggers"])
        self.assertEqual(m["dte"], 39)

    def test_credit_stop_loss(self):
        m = marks.mark_position(pcs_position(), idx(3.95, 4.05, 0.95, 1.05), 100.0, ASOF)
        # value = -4.00 + 1.00 = -3.00 ; pnl = -2.00*200 = -400 ; basis 200 -> stop at -400
        self.assertAlmostEqual(m["pnl"], -400.0)
        self.assertIn("stop_loss", m["triggers"])

    def test_21_dte(self):
        m = marks.mark_position(pcs_position(), idx(0.9, 1.0, 0.2, 0.3), 100.0, date(2026, 10, 17))
        self.assertEqual(m["dte"], 20)
        self.assertIn("21_dte", m["triggers"])

    def test_debit_stop(self):
        pos = {"id": "D1", "symbol": "TEST", "strategy": "long_call", "opened": "2026-09-01",
               "qty": 1, "entry_cost": 2.00, "profit_target_pct": 100,
               "legs": [{"action": "BUY", "ratio": 1, "option": "TEST261106C00100000"}]}
        c = make_contract("TEST261106C00100000", 0.95, 1.05)
        m = marks.mark_position(pos, {c.option: c}, 100.0, ASOF)
        self.assertAlmostEqual(m["pnl"], -100.0)
        self.assertIn("stop_loss", m["triggers"])

    def test_expired_leg_uses_intrinsic_and_flags_assignment(self):
        m = marks.mark_position(pcs_position(), {}, 93.0, date(2026, 11, 6))
        # short 95P intrinsic 2, long 90P 0 -> value -2 ; pnl = (-2+1)*200 = -200
        self.assertAlmostEqual(m["pnl"], -200.0)
        self.assertIn("expiration", m["triggers"])
        self.assertIn("assignment", m["triggers"])
        self.assertEqual(m["errors"], [])

    def test_missing_unexpired_quote_is_error(self):
        m = marks.mark_position(pcs_position(), {}, 100.0, ASOF)
        self.assertTrue(m["errors"])
        self.assertIsNone(m["pnl"])

    def test_stock_leg(self):
        pos = {"id": "S1", "symbol": "KO", "strategy": "assigned_shares", "opened": "2026-11-06",
               "qty": 1, "entry_cost": 85.0, "profit_target_pct": 100,
               "legs": [{"action": "BUY", "ratio": 1, "option": "STOCK"}]}
        m = marks.mark_position(pos, {}, 87.0, ASOF)
        self.assertAlmostEqual(m["pnl"], 200.0)
        self.assertIsNone(m["dte"])


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run to verify failure**

Run: `cd /Users/hmadhani/finance-portfolio && python3 -m unittest tests.test_marks -v`
Expected: ERROR — `ImportError: cannot import name 'marks'`

- [ ] **Step 3: Implement**

`scripts/optlib/marks.py`:
```python
"""Mark open positions (from options/data/positions.json) to mid and flag
management-rule triggers defined in options/investor-profile.md."""
from datetime import date

from .chain import parse_occ
from .strategy import MULTIPLIER


def _intrinsic(kind: str, strike: float, spot: float) -> float:
    return max(0.0, spot - strike) if kind == "C" else max(0.0, strike - spot)


def mark_position(position: dict, cs_index: dict, spot: float, asof: date) -> dict:
    qty = position["qty"]
    cost = position["entry_cost"]
    value, errors, leg_rows, dtes, assignment = 0.0, [], [], [], False
    for leg in position["legs"]:
        sign = 1 if leg["action"] == "BUY" else -1
        if leg["option"] == "STOCK":
            mid, itm = spot, None
        else:
            _, expiry, kind, strike = parse_occ(leg["option"])
            dte = (expiry - asof).days
            dtes.append(dte)
            itm = _intrinsic(kind, strike, spot) > 0
            if dte <= 0:
                mid = _intrinsic(kind, strike, spot)
                if sign < 0 and itm:
                    assignment = True
            elif leg["option"] in cs_index:
                mid = cs_index[leg["option"]].mid
            else:
                errors.append(f"no quote for {leg['option']}")
                mid = None
        leg_rows.append({"option": leg["option"], "mid": mid, "itm": itm})
        if mid is not None:
            value += sign * leg["ratio"] * mid

    out = {"id": position["id"], "symbol": position["symbol"], "strategy": position["strategy"],
           "spot": spot, "legs": leg_rows, "errors": errors,
           "dte": min(dtes) if dtes else None, "triggers": []}
    if errors:
        out.update(value_per_share=None, pnl=None, pct_of_basis=None)
        return out

    pnl = round((value - cost) * MULTIPLIER * qty, 2)
    basis = abs(cost) * MULTIPLIER * qty
    pct = round(pnl / basis * 100.0, 1) if basis else None
    target = position.get("profit_target_pct", 50)
    triggers = []
    if pct is not None and pct >= target:
        triggers.append("profit_target")
    stop_mult = 2.0 if cost < 0 else 0.5
    if basis and pnl <= -stop_mult * basis:
        triggers.append("stop_loss")
    if dtes and min(dtes) <= 21:
        triggers.append("21_dte")
    if dtes and min(dtes) <= 0:
        triggers.append("expiration")
    if assignment:
        triggers.append("assignment")
    out.update(value_per_share=round(value, 4), pnl=pnl, pct_of_basis=pct, triggers=triggers)
    return out
```

Note on `test_stock_leg`: shares are an "asset" position, basis 8500, pnl 200 → 2.4%, no triggers except none; `dte` is `None` because there are no option legs. Rules for assigned shares are applied by the routine (sell covered calls), not by marks.

- [ ] **Step 4: Run to verify pass**

Run: `cd /Users/hmadhani/finance-portfolio && python3 -m unittest tests.test_marks -v`
Expected: 7 tests OK

- [ ] **Step 5: Commit**

```bash
cd /Users/hmadhani/finance-portfolio
git add scripts/optlib/marks.py tests/test_marks.py
git commit -m "optlib: mark positions to mid with management-rule triggers

AI-assisted change.

Signed-off-by: hmadhani2024@gmail.com"
```

---

### Task 6: CLI `scripts/options_data.py`

**Files:**
- Create: `scripts/options_data.py`
- Create: `tests/test_cli.py`

**Interfaces:**
- Consumes: everything from Tasks 2-5.
- Produces: CLI contract used by the routine and the learner. All subcommands print one JSON document to stdout; exit code 0 on success, 2 on usage error. Global flag `--asof YYYY-MM-DD` (default: today).
  - `regime` → `{"asof", "vix", "vix3m", "term_structure": "contango"|"backwardation", "stress": bool, "vix_percentile_1y", "bxm", "put"}`
  - `scan [--symbols A,B] [--dte 30-60] [--max-expiries 2] [--iv-history PATH]` → `{"asof", "results": [{"symbol", "price", "iv30_pct", "expected_move_30d", "iv_rank": {...}, "is_etf", "expiries": [...], "candidates": [Contract.row...]}| {"symbol", "error"}]}`. Default symbols = `UNIVERSE`. Candidates are delta buckets `[0.05, 0.10, 0.16, 0.20, 0.25, 0.30, 0.40, 0.50]` per kind per selected expiry.
  - `price-spread --symbol SYM --legs "SPEC" --qty N [--with-stock]` → `analyze()` dict + `"payoff_ascii"` + `"spot"` + `"position_template"` (the dict to append to positions.json, `id` left as `"<fill-in>"`).
  - `mark [--positions PATH]` → `{"asof", "marks": [...]}`.
  - `record-iv [--symbols A,B] [--iv-history PATH]` → `{"asof", "appended": N, "errors": [...]}`.
- Defaults: `--iv-history options/data/iv-history.csv`, `--positions options/data/positions.json` (relative to repo root, resolved from the script's location).

- [ ] **Step 1: Write the failing tests**

`tests/test_cli.py`:
```python
import json
import os
import subprocess
import sys
import tempfile
import unittest

from tests.helpers import make_chain, write_fixture_dir

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
CLI = os.path.join(REPO, "scripts", "options_data.py")


class TestCli(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.fx = os.path.join(self.tmp.name, "fx")
        write_fixture_dir(self.fx, {"TEST": make_chain(strikes=range(70, 131, 1), width=0.04),
                                    "ETF1": make_chain(symbol="ETF1", spot=50.0, strikes=range(40, 61, 1))})
        self.env = dict(os.environ, OPTIONS_FIXTURE_DIR=self.fx)

    def tearDown(self):
        self.tmp.cleanup()

    def run_cli(self, *args, expect=0):
        p = subprocess.run([sys.executable, CLI, "--asof", "2026-09-28", *args],
                           capture_output=True, text=True, env=self.env)
        self.assertEqual(p.returncode, expect, p.stderr)
        return json.loads(p.stdout) if expect == 0 else p

    def test_regime(self):
        r = self.run_cli("regime")
        self.assertEqual(r["vix"], 15.0)
        self.assertEqual(r["term_structure"], "contango")
        self.assertFalse(r["stress"])
        self.assertIn("vix_percentile_1y", r)
        self.assertEqual(r["bxm"], 2560.6)

    def test_scan(self):
        ivp = os.path.join(self.tmp.name, "iv.csv")
        r = self.run_cli("scan", "--symbols", "TEST,MISSING", "--iv-history", ivp)
        ok, bad = r["results"]
        self.assertEqual(ok["symbol"], "TEST")
        self.assertAlmostEqual(ok["iv30_pct"], 20.0)
        self.assertIsNone(ok["iv_rank"]["iv_rank"])
        self.assertTrue(ok["candidates"])
        self.assertIn("error", bad)

    def test_price_spread(self):
        r = self.run_cli("price-spread", "--symbol", "TEST", "--qty", "2",
                         "--legs", "SELL 1 P 95 2026-11-06; BUY 1 P 90 2026-11-06")
        self.assertEqual(r["credit_or_debit"], "credit")
        self.assertIn("*", r["payoff_ascii"])
        tpl = r["position_template"]
        self.assertEqual(tpl["qty"], 2)
        self.assertEqual(tpl["entry_cost"], r["entry_cost_per_share"])
        self.assertEqual(tpl["legs"][0]["option"], "TEST261106P00095000")

    def test_price_spread_bad_strike_is_usage_error(self):
        p = self.run_cli("price-spread", "--symbol", "TEST", "--qty", "1",
                         "--legs", "SELL 1 P 95.5 2026-11-06", expect=2)
        self.assertIn("no quote", p.stderr)

    def test_record_iv_then_mark(self):
        ivp = os.path.join(self.tmp.name, "iv.csv")
        r = self.run_cli("record-iv", "--symbols", "TEST,ETF1", "--iv-history", ivp)
        self.assertEqual(r["appended"], 2)
        self.assertEqual(self.run_cli("record-iv", "--symbols", "TEST", "--iv-history", ivp)["appended"], 0)

        pos_path = os.path.join(self.tmp.name, "positions.json")
        tpl = self.run_cli("price-spread", "--symbol", "TEST", "--qty", "1",
                           "--legs", "SELL 1 P 95 2026-11-06; BUY 1 P 90 2026-11-06")["position_template"]
        tpl["id"] = "T1"
        with open(pos_path, "w") as f:
            json.dump({"positions": [tpl]}, f)
        m = self.run_cli("mark", "--positions", pos_path)["marks"][0]
        self.assertEqual(m["id"], "T1")
        self.assertLess(m["pnl"], 0)          # just paid slippage: marked at mid, below fill
        self.assertEqual(m["dte"], 39)

    def test_mark_empty(self):
        pos_path = os.path.join(self.tmp.name, "positions.json")
        with open(pos_path, "w") as f:
            json.dump({"positions": []}, f)
        self.assertEqual(self.run_cli("mark", "--positions", pos_path)["marks"], [])


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run to verify failure**

Run: `cd /Users/hmadhani/finance-portfolio && python3 -m unittest tests.test_cli -v`
Expected: FAIL — non-zero return code, `can't open file ... options_data.py`

- [ ] **Step 3: Implement**

`scripts/options_data.py`:
```python
#!/usr/bin/env python3
"""
options_data.py — data + deterministic math for the $50K options paper portfolio
(finance-portfolio repo, options/). Stdlib only. Data: Cboe delayed quotes
(15-min delayed, free, no key). Every number in options/learning-ledger.md
must be reproducible with one of these commands.

  regime                          VIX, VIX3M, term structure, VIX 1-yr percentile, BXM/PUT levels
  scan [--symbols A,B] [--dte 30-60]
                                  per symbol: price, iv30, expected move, IV rank, candidate strikes
  price-spread --symbol S --legs "SELL 1 P 95 2026-11-06; BUY 1 P 90 2026-11-06" --qty N [--with-stock]
                                  fills, max P/L, breakevens, prob. of profit, net Greeks, payoff diagram
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


def liquid_kwargs(symbol: str) -> dict:
    return {"abs_spread_ok": 0.05} if symbol in ETFS else {}


def cmd_regime(a):
    vix = ch.load_quote("_VIX")["current_price"]
    vix3m = ch.load_quote("_VIX3M")["current_price"]
    return {"asof": a.asof.isoformat(), "vix": vix, "vix3m": vix3m,
            "term_structure": "backwardation" if vix > vix3m else "contango",
            "stress": vix > vix3m,
            "vix_percentile_1y": ivhist.vix_percentile(ch.load_vix_history(), vix),
            "bxm": ch.load_quote("_BXM")["current_price"],
            "put": ch.load_quote("_PUT")["current_price"]}


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
        raise UsageError(str(e).strip('"'))
    out = st.analyze(legs, a.qty, spot, a.asof)
    out["spot"] = spot
    out["payoff_ascii"] = st.ascii_payoff(legs, a.qty, spot)
    out["position_template"] = {
        "id": "<fill-in>", "symbol": a.symbol.upper(), "strategy": "<fill-in>",
        "opened": a.asof.isoformat(), "qty": a.qty, "entry_cost": out["entry_cost_per_share"],
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
            raw = ch.load_chain(sym)
            chains[sym] = (ch.index_contracts(ch.contracts(raw)), raw["current_price"])
        idx, spot = chains[sym]
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
    ps.add_argument("--qty", type=int, required=True)
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
    json.dump(result, sys.stdout, indent=2, default=str)
    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 4: Run the full suite**

Run: `cd /Users/hmadhani/finance-portfolio && python3 -m unittest discover -s tests -v`
Expected: all tests OK (bs, chain, ivhist, strategy, marks, cli)

- [ ] **Step 5: Live smoke test against Cboe (network)**

Run:
```bash
cd /Users/hmadhani/finance-portfolio
python3 scripts/options_data.py regime
python3 scripts/options_data.py scan --symbols SPY,KO --iv-history /tmp/ivtest.csv | head -40
```
Expected: real VIX/VIX3M/BXM/PUT numbers; SPY and KO results with candidates and `iv_rank.iv_rank: null` (no history yet). Then pick two real SPY put strikes from the scan output and run `price-spread` with them; confirm `defined_risk: true` and a sensible `max_loss`. Delete `/tmp/ivtest.csv` afterwards.

- [ ] **Step 6: Commit**

```bash
cd /Users/hmadhani/finance-portfolio
chmod +x scripts/options_data.py
git add scripts/options_data.py tests/test_cli.py
git commit -m "options_data CLI: regime, scan, price-spread, mark, record-iv

AI-assisted change.

Signed-off-by: hmadhani2024@gmail.com"
```

---

### Task 7: Portfolio content files (profile, portfolio, ledger, state, backlog, README)

**Files:**
- Create: `options/investor-profile.md`, `options/options-portfolio.md`, `options/learning-ledger.md`, `options/DECISION.md`, `options/data/positions.json`, `options/data/iv-history.csv`
- Modify: `README.md` (append a section)

**Interfaces:**
- Produces: the section headings the routine prompt (Task 9) edits by name — in `options-portfolio.md`: `## Header`, `## Open Positions`, `## Closed Positions`, `## NAV History`, `## Daily Decision Log`; in `learning-ledger.md`: `## Primer`, `## Concept Index`, `## Entries`.

- [ ] **Step 1: Write `options/investor-profile.md`**

```markdown
# Options Investor Profile

## Investor: Lt. Cmdr. Data — Probabilistic Learner

A fictional investor learning options from zero. Treats every trade as a
probability experiment with a known worst case: never enters a position whose
maximum loss is unknown at entry, sizes so no single outcome matters much,
and writes down *why* before every trade so the reasoning can be checked
later. Prefers to skip a day over forcing a trade.

This profile contains no real personal or account data. It is a **paper**
portfolio: fills are simulated from public, 15-minute-delayed Cboe quotes.
Inception date is set by the first cycle and recorded in `options-portfolio.md`.

## Capital

- Starting capital: **$50,000** (paper).
- Unreserved cash accrues ~4.5%/yr (SGOV-equivalent), pro-rated daily.

## Allowed Strategies (defined risk only)

| Strategy | View | Max loss |
|---|---|---|
| Long call / long put | Directional | Premium paid |
| Debit vertical (bull call / bear put) | Directional, cheaper | Debit paid |
| Credit vertical (bull put / bear call) | Directional + premium selling | Width − credit |
| Iron condor | Range-bound, high IV | Wider wing − credit |
| Long butterfly | Pin near a price | Debit paid |
| Calendar / diagonal (long back month) | Low IV, time decay differential | Debit paid (approx.) |
| Cash-secured put | Willing to own shares, high IV | Strike × 100 − credit |
| Covered call | Only on shares acquired via put assignment | Share downside − credit |

**Never:** naked short calls or puts, short straddles/strangles, ratio spreads
with an uncovered leg — any position where `price-spread` reports
`defined_risk: false`.

## Position Sizing

- Max loss per position ≤ **3% NAV** (~$1,500 at inception).
- Sum of max losses across all open positions ≤ **25% NAV**.
- ≤ **2** open positions per underlying.
- ≤ **5** new positions per calendar week (Mon-Fri).
- Cash-secured put collateral (strike × 100) ≤ **20% NAV** per position — in
  practice only underlyings priced ≤ ~$100.
- Stress regime (VIX above VIX3M): halve the max loss per new position and open
  no new short-premium trades on single stocks.

## Entry Rules

- Days to expiration at entry: **30-60** (calendars: front 20-40, back 50-90).
- Short strikes: **0.16-0.30** absolute delta.
- Liquidity on every leg: open interest ≥ **500**; bid-ask width ≤ **10% of mid**
  (ETFs: or ≤ **$0.05**).
- Earnings: no short premium held through an earnings date, except a deliberate
  "IV-crush lesson" trade with max loss ≤ **1% NAV**, labeled as such. Check the
  next earnings date by WebSearch before any single-stock entry.
- Universe: SPY QQQ IWM DIA XLF XLE XLK XLV GLD TLT + AAPL MSFT NVDA AMZN GOOGL
  META TSLA AMD AVGO JPM BAC XOM KO PFE INTC F T WFC DIS NFLX.

## Regime → Strategy Guidance (judgment, not mechanical)

| Signal | Lean toward |
|---|---|
| IV rank ≥ 50 (or VIX percentile ≥ 60 while IV history < 20 days) | Selling premium: credit spreads, iron condors, CSPs |
| IV rank ≤ 25 (or VIX percentile ≤ 30) | Buying premium: debit spreads, calendars, long options |
| In between | Directional verticals in the direction of the trend |
| VIX > VIX3M (backwardation) | Stress: smaller size, defined-risk ETF trades only |

## Management Rules

- Credit trades: close at **50%** of max profit; close if loss reaches **2× the credit**.
- Debit trades: close at the profit target stated at entry (default **100%** gain);
  close if loss reaches **50%** of the debit.
- Close or roll anything at **21 DTE** (gamma risk grows near expiry).
- Short option in the money at expiration → simulate assignment: CSP becomes
  100 shares per contract at the strike (then covered calls are allowed);
  spreads are closed at intrinsic value.

## Execution Model

- Buy at mid + 25% of the bid-ask width; sell at mid − 25% of the width.
- Commission $0.65 per contract per side. Marks use mid.

## Benchmarks

- Cboe **BXM** (S&P 500 BuyWrite Index) and Cboe **PUT** (S&P 500 PutWrite
  Index) — the standard public benchmarks for systematic option selling — plus cash.
```

- [ ] **Step 2: Write `options/options-portfolio.md`**

```markdown
# Options Paper Portfolio — $50K (Lt. Cmdr. Data)

IMPORTANT: This is a paper/model options portfolio for learning and evaluation
only, tracked with public, delayed market data (no personal financial context).
It does not constitute investment advice or a recommendation to buy or sell any
security or option. Options involve significant risk and are not suitable for
all investors; see the OCC's "Characteristics and Risks of Standardized Options".

Rules: `options/investor-profile.md` · Teaching: `options/learning-ledger.md` ·
Machine state: `options/data/positions.json`

## Header

| Field | Value |
|---|---|
| Inception | (set on first cycle) |
| Cycle # | 0 |
| NAV | $50,000.00 |
| Cash | $50,000.00 |
| Collateral / max loss reserved | $0.00 |
| Capital at risk (sum of max losses) | $0.00 (0.0% NAV) |
| Net delta (share-equivalents) | 0 |
| Net theta ($/day) | 0.00 |
| Net vega ($/IV point) | 0.00 |
| Return since inception | 0.00% |
| BXM since inception | — |
| PUT since inception | — |
| Regime | — |

## Open Positions

| ID | Symbol | Strategy | Opened | Expiry | Qty | Entry $/sh | Mark $/sh | P&L $ | % of basis | Max loss $ | DTE | Triggers |
|---|---|---|---|---|---|---|---|---|---|---|---|---|

## Closed Positions

| ID | Symbol | Strategy | Opened | Closed | Realized P&L $ | Exit reason | Ledger entry |
|---|---|---|---|---|---|---|---|

## NAV History

Append-only. One row per cycle.

| Date | Cycle # | NAV | BXM | PUT | VIX |
|---|---|---|---|---|---|

## Daily Decision Log

Reverse-chronological. One heading per cycle: `### YYYY-MM-DD — Cycle #N: <summary>`.
```

- [ ] **Step 3: Write `options/learning-ledger.md`**

The Primer paraphrases official OCC/OIC definitions and cites them; it must not copy their text.

```markdown
# Options Learning Ledger

Every decision this portfolio makes — opening, adjusting, closing, or choosing
*not* to trade — is explained here for a beginner. Each entry shows the market
context, why this strategy beat the alternatives, the exact trade, what can go
wrong, and one or two new concepts. Every number can be reproduced with the
`Reproduce:` command in the entry. Sources for the concepts: `RESOURCES.md`.

Entries on closed trades end with **Your reflection** — left empty for you.

## Primer

Read once before the first entry. Definitions paraphrase the Options Industry
Council (optionseducation.org) and the OCC's *Characteristics and Risks of
Standardized Options* (theocc.com) — see RESOURCES.md.

- **Option** — a contract giving the buyer the *right*, not the obligation, to
  buy or sell an underlying asset at a set price before or on a set date. The
  seller takes on the matching *obligation*.
- **Call / Put** — a call is the right to *buy*; a put is the right to *sell*.
- **Strike** — the price at which the option lets you buy (call) or sell (put).
- **Expiration** — the last day the option exists. **DTE** = days to expiration.
- **Premium** — the price of the option, quoted per share. One US equity option
  contract covers **100 shares**, so a $1.50 premium costs $150 per contract.
- **Bid / Ask / Mid** — the highest price buyers are paying, the lowest sellers
  are asking, and the midpoint. The gap is a cost you pay when trading.
- **In / at / out of the money** — whether exercising right now would be worth
  something (ITM), be break-even (ATM), or be worthless (OTM).
- **Intrinsic vs. extrinsic value** — intrinsic is what the option is worth if
  exercised now; extrinsic ("time value") is everything above that, and it
  decays to zero by expiration.
- **Long vs. short** — buying an option (long) risks the premium paid; selling
  one (short) collects premium but takes on the obligation. This portfolio only
  sells options when a bought option caps the risk.

## Concept Index

| Concept | First explained in |
|---|---|

## Entries

Newest first. Format:

    ### YYYY-MM-DD — <OPEN|ADJUST|CLOSE|PASS> <symbol> <strategy> (Cycle #N)
    **Decision:** …
    **Market context:** …
    **Why this strategy:** …
    **The trade:** legs table, max profit, max loss, breakeven(s), probability of profit, payoff diagram
    **Greeks in dollars:** …
    **Concept spotlight:** …
    **What would prove this wrong:** …
    **Reproduce:** `python3 scripts/options_data.py … --asof YYYY-MM-DD`
    (CLOSE entries add) **Outcome:** · **What drove the P&L:** · **Lesson:** · **Your reflection:** (blank)
```

- [ ] **Step 4: Write `options/DECISION.md`, state files, README**

`options/DECISION.md`:
```markdown
# Decision Backlog — options portfolio

Dated 2026-09-27. Known simplifications, deliberately not built yet.

1. **No backtest.** Rules are industry heuristics (30-60 DTE, 16-30 delta,
   50% profit take, 21 DTE exit), not fitted to this portfolio's history.
2. **IV rank starts empty.** Per-underlying IV history accumulates from
   inception; for the first 20 trading days the VIX percentile is the proxy.
3. **European-style valuation.** Payoffs and probabilities use Black-Scholes
   without dividends; early assignment is modeled only at expiration.
4. **Delayed, end-of-day-ish data.** Quotes are 15-minute delayed and managed
   once a day — real positions can move a lot intraday.
5. **Free data only.** A paid API (Tradier, Polygon, MarketData.app) would give
   real historical IV; swap in behind `scripts/optlib/chain.py` if needed.
6. **No tax or margin modeling.** Portfolio margin, Reg-T margin, and tax
   treatment of options are out of scope.
```

`options/data/positions.json`:
```json
{"positions": []}
```

`options/data/iv-history.csv`:
```
date,symbol,iv30,price
```

Append to `README.md`:
```markdown

## Options paper portfolio (`options/`)

A separate $50K paper portfolio that trades **defined-risk options only**, run by
its own daily cloud routine, with a beginner-level learning ledger explaining every
decision. Rules: `options/investor-profile.md`. State: `options/options-portfolio.md`.
Teaching: `options/learning-ledger.md`. Reading list: `options/RESOURCES.md`.
Math and data: `scripts/options_data.py` (stdlib only; Cboe delayed quotes).
Tests: `python3 -m unittest discover -s tests -v`.
```

- [ ] **Step 5: Verify**

Run: `cd /Users/hmadhani/finance-portfolio && python3 -c "import json;json.load(open('options/data/positions.json'))" && python3 scripts/options_data.py mark && python3 -m unittest discover -s tests`
Expected: `{"asof": ..., "marks": []}` and all tests OK.

- [ ] **Step 6: Commit**

```bash
cd /Users/hmadhani/finance-portfolio
git add options/ README.md
git commit -m "options: investor profile, portfolio, learning ledger, state files

AI-assisted change.

Signed-off-by: hmadhani2024@gmail.com"
```

---

### Task 8: `options/RESOURCES.md` — verified, sourced reading list

**Files:**
- Create: `options/RESOURCES.md`

Rules for this task (non-negotiable — the user asked that every item be verifiable):
- Fetch every URL (WebFetch or `ctx_fetch_and_index`). Keep an item only if the page loads and shows the claimed title/authors. Record `verified 2026-MM-DD` on each.
- The one-line "why read it" must come from the fetched abstract/page, not memory. If the abstract is paywalled and the landing page shows only title/authors, write "Landing page verified; summary from abstract not available" rather than inventing a finding.
- Books: citation (author, title, edition, publisher, year, ISBN) verified against the publisher's page or a library catalog (e.g. worldcat.org, publisher site). Summary is a short original description — never copied text.
- Anything that cannot be verified is **omitted** and listed in a final "Not included (could not verify)" line.

- [ ] **Step 1: Verify candidate sources**

Candidates (DOI links resolve to the publisher's canonical page):

| # | Item | URL to verify |
|---|---|---|
| 1 | Black & Scholes (1973), "The Pricing of Options and Corporate Liabilities", *J. Political Economy* 81(3) | https://doi.org/10.1086/260062 |
| 2 | Merton (1973), "Theory of Rational Option Pricing", *Bell J. Econ.* 4(1) | https://doi.org/10.2307/3003143 |
| 3 | Cox, Ross & Rubinstein (1979), "Option Pricing: A Simplified Approach", *J. Financial Economics* 7(3) | https://doi.org/10.1016/0304-405X(79)90015-1 |
| 4 | Heston (1993), "A Closed-Form Solution for Options with Stochastic Volatility…", *Rev. Financial Studies* 6(2) | https://doi.org/10.1093/rfs/6.2.327 |
| 5 | Coval & Shumway (2001), "Expected Option Returns", *J. Finance* 56(3) | https://doi.org/10.1111/0022-1082.00352 |
| 6 | Bakshi & Kapadia (2003), "Delta-Hedged Gains and the Negative Market Volatility Risk Premium", *RFS* 16(2) | https://doi.org/10.1093/rfs/hhg002 |
| 7 | Carr & Wu (2009), "Variance Risk Premiums", *RFS* 22(3) | https://doi.org/10.1093/rfs/hhn038 |
| 8 | Goyal & Saretto (2009), "Cross-Section of Option Returns and Volatility", *JFE* 94(2) | https://doi.org/10.1016/j.jfineco.2009.01.001 |
| 9 | Whaley (2002), "Return and Risk of CBOE Buy Write Monthly Index", *J. Derivatives* 10(2) | https://doi.org/10.3905/jod.2002.319194 |
| 10 | Israelov & Nielsen (2015), "Covered Calls Uncovered", *Financial Analysts Journal* 71(6) | https://doi.org/10.2469/faj.v71.n6.4 |
| 11 | OCC — Characteristics and Risks of Standardized Options (ODD) | https://www.theocc.com/company-information/documents-and-archives/options-disclosure-document |
| 12 | Options Industry Council — education | https://www.optionseducation.org |
| 13 | Cboe Options Institute | https://www.cboe.com/optionsinstitute/ |
| 14 | Cboe BXM / PUT benchmark index pages | https://www.cboe.com/us/indices/benchmark_indices/ |
| 15 | SEC Investor.gov — Options | https://www.investor.gov/introduction-investing/investing-basics/investment-products/options |
| 16 | FINRA — Options | https://www.finra.org/investors/investing/investment-products/options |
| 17 | CME Group — Introduction to Options | https://www.cmegroup.com/education/courses/introduction-to-options.html |
| 18 | Cboe delayed quotes (this portfolio's data source) | https://www.cboe.com/delayed_quotes/ |
| B1 | Natenberg, *Option Volatility and Pricing*, 2nd ed., McGraw-Hill, 2015 | publisher / catalog |
| B2 | Hull, *Options, Futures, and Other Derivatives*, 11th ed., Pearson | publisher / catalog |
| B3 | Sinclair, *Volatility Trading*, 2nd ed., Wiley, 2013 | publisher / catalog |
| B4 | McMillan, *Options as a Strategic Investment*, 5th ed., Prentice Hall Press, 2012 | publisher / catalog |

For each: fetch, confirm title/authors/year, extract the abstract's main finding (papers) or what the site covers (sites). Correct any detail above that the fetched page contradicts (the page wins). If a DOI in this table fails, search for the paper by exact title and use the publisher's DOI you find — never guess.

- [ ] **Step 2: Write `options/RESOURCES.md`**

Structure:
```markdown
# Options Resources

Every item was opened and checked on the date shown. Papers link to the
publisher's DOI page; summaries come from each paper's own abstract. Books are
cited (not linked) with a short original description.

## Start here (beginner, free, official)
- **<title>** — <publisher>. <what it covers>. <url> · verified YYYY-MM-DD

## How options are priced (foundational papers)
- **<Authors> (<year>). "<Title>." *<Journal>* <vol>(<issue>).** <one-line finding from abstract>. <doi url> · verified YYYY-MM-DD
  - *Where it shows up in this portfolio:* <e.g. the Black-Scholes math in scripts/optlib/bs.py>

## What the evidence says about option returns and selling premium
(same format; "Where it shows up": volatility risk premium → why the profile sells premium when IV rank is high; BXM/PUT → benchmarks)

## Benchmarks and data used by this portfolio
(Cboe BXM/PUT pages, Cboe delayed quotes)

## Books
- **<Author>, *<Title>*, <ed.>, <Publisher>, <year>. ISBN <isbn>.** <2-sentence original description>. Verified via <catalog/publisher url> · YYYY-MM-DD

## Not included (could not verify)
- <item> — <reason>   (or "None")
```

- [ ] **Step 3: Self-check**

Run: `grep -c "verified 20" options/RESOURCES.md` — expect one per kept item. Confirm no item lacks a URL or ISBN, and no summary contains quoted text longer than a short phrase.

- [ ] **Step 4: Commit**

```bash
cd /Users/hmadhani/finance-portfolio
git add options/RESOURCES.md
git commit -m "options: verified, sourced RESOURCES reading list

AI-assisted change.

Signed-off-by: hmadhani2024@gmail.com"
```

---

### Task 9: Routine prompt + `hm-options-portfolio` skill

**Files:**
- Create: `options/routine-prompt.md` (repo)
- Create: `~/.claude/skills/hm-options-portfolio/SKILL.md` (skills repo at `~/.claude/skills`, separate git repo — commit only this file there)

**Interfaces:**
- Consumes: CLI contract (Task 6), file headings (Task 7), profile rules (Task 7).

- [ ] **Step 1: Write `options/routine-prompt.md`**

The file body is exactly the prompt the cloud routine receives:

```markdown
It is ~12pm ET on the day this routine fired. Run today's cycle for the $50K defined-risk OPTIONS paper portfolio in the `finance-portfolio` repo (directory `options/`). You are also the teacher: every decision gets a beginner-level learning-ledger entry.

HARD RULES: Paper trading only. Never read or reference anything outside this repo, never any personal financial data, never the Skill tool. Only public market data (the Cboe feed via scripts/options_data.py, plus WebSearch/WebFetch for news and earnings dates). Never fabricate a number: every price, Greek, probability, max loss, and breakeven you write must come from a `scripts/options_data.py` command you ran this cycle, and the ledger entry must show that command. Never open a position that `price-spread` reports as `defined_risk: false`.

STEP 0 — Setup and trading-day check.
0a. `cd` into the repo (find it with `pwd`/`ls`). `git pull --rebase origin main`. Run `date`.
0b. NYSE holidays — 2026: Jan 1, Jan 19, Feb 16, Apr 3, May 25, Jun 19, Jul 3, Sep 7, Nov 26, Dec 25. 2027: Jan 1, Jan 18, Feb 15, Mar 26, May 31, Jun 18, Jul 5, Sep 6, Nov 25, Dec 24. Beyond these, derive from the standard NYSE calendar (weekend-observed shifts). Weekend or holiday → PushNotification "Options: market closed today (<reason>) — no cycle." and stop. Write nothing.
0c. Same-day guard: if `options/options-portfolio.md` NAV History already has a row dated today, stop silently (no writes, no notification).
0d. Data check: `python3 scripts/options_data.py regime`. If it fails (network/HTTP error), enter DEGRADED MODE: use WebSearch only to check news on open positions; close a position only if a hard risk event is clear; open NOTHING; append a NAV History row marked "(degraded — no marks)" with the prior NAV; log why; commit; PushNotification "Options: Cboe data unreachable — degraded cycle, no new trades." Then stop.

STEP 1 — Read state: `cat options/investor-profile.md options/options-portfolio.md options/data/positions.json` and the `## Concept Index` of `options/learning-ledger.md` (so you never re-explain a concept already taught — link to it instead). If the Header's Inception is "(set on first cycle)", this is cycle 1: set Inception to today and record today's BXM/PUT/VIX as the base levels.

STEP 2 — Market regime: from `regime` output, note VIX, VIX3M, contango/backwardation (stress if backwardation), VIX 1-yr percentile. Then `python3 scripts/options_data.py scan` (full universe). For each symbol note price, iv30, expected 30-day move, IV rank (or the "insufficient history" note → use VIX percentile as proxy per the profile).

STEP 3 — Manage open positions FIRST: `python3 scripts/options_data.py mark`. For each position, act on triggers per the profile's Management Rules:
- profit_target / stop_loss / 21_dte → close (or roll to 30-60 DTE if the original thesis still holds and the roll itself passes every entry rule — price the roll with `price-spread`).
- expiration / assignment → settle: expired OTM legs worthless; ITM short put of a CSP → convert to shares (positions.json leg `{"action":"BUY","ratio":1,"option":"STOCK"}`, entry_cost = strike − credit received per share, qty = contracts); spreads → close at intrinsic.
- No trigger → hold; one-line note in the Daily Decision Log (no ledger entry needed for a plain hold unless something teachable happened, e.g. a big IV move).
Closing fills: price the closing legs with `price-spread` using the opposite actions (closing a short = BUY) and use its fills; realized P&L = (closing proceeds − entry cost) × 100 × qty − round-trip fees.

STEP 4 — New entries (skip entirely in stress regime for single stocks; halve max loss everywhere in stress):
- Capacity checks from the profile: ≤ 5 new positions this calendar week (count "OPEN" ledger headings dated Mon-today), sum of max losses ≤ 25% NAV after the trade, ≤ 2 positions per underlying, CSP collateral ≤ 20% NAV.
- Pick at most 2 candidates today. For each: state the regime → strategy reasoning, choose strikes from the scan candidates (short strikes 0.16-0.30 |delta|, 30-60 DTE, liquid), WebSearch the next earnings date for single stocks (no short premium through earnings unless it is the labeled ≤1% NAV IV-crush lesson).
- Size: `qty` = floor(allowed max loss ÷ per-unit max loss from `price-spread --qty 1`), minimum 1, else skip. Re-run `price-spread` with the final qty; that output is the trade.
- Append the `position_template` to `options/data/positions.json` with a real `id` (`YYYY-MM-DD-SYMBOL-STRATEGYABBREV-N`) and `strategy` name. Cash += −entry_cost × 100 × qty − entry fees.
- If nothing qualifies, that is a valid outcome: write a PASS ledger entry explaining what was checked and why nothing met the rules.

STEP 5 — Record IV: `python3 scripts/options_data.py record-iv`.

STEP 6 — Write `options/options-portfolio.md`:
- NAV = cash + Σ (mark value_per_share × 100 × qty) over open positions. Accrue interest on cash not reserved as collateral/max loss at 4.5%/yr pro-rated since the last NAV row.
- Update Header (all fields incl. net delta/theta/vega summed from marks/analyze, capital at risk, return vs BXM and PUT since inception), Open Positions table, Closed Positions (for anything closed today), append one NAV History row (Date, Cycle #, NAV, BXM, PUT, VIX), and add today's Daily Decision Log heading `### YYYY-MM-DD — Cycle #N: <summary>` with one line per position and per new trade.
- Increment Cycle #.

STEP 7 — Write `options/learning-ledger.md` entries (newest first, under `## Entries`), one per OPEN, CLOSE, ADJUST/ROLL, assignment, and PASS, in the documented format, pitched at a beginner:
- Market context in plain words first, then the numbers.
- "Why this strategy" must name 1-2 rejected alternatives and why they lost.
- The trade: legs table (action, contracts, call/put, strike, expiry, fill), max profit, max loss, breakeven(s), probability of profit, and the `payoff_ascii` diagram in a code block.
- Greeks in dollars for THIS position (e.g. "theta +$4.10/day means that if nothing else changes, the position gains about $4 per day from time decay").
- Concept spotlight: introduce at most 2 concepts not already in the Concept Index, explain from zero with a concrete example from this trade, and add each to the Concept Index table with a link to this entry. Suggested teaching order as trades allow: premium & breakeven → delta → theta → implied volatility → vega → IV rank → expected move → probability of profit → vertical spreads → credit vs debit → the volatility risk premium → gamma & why 21 DTE → skew → assignment → rolling → term structure/calendars → iron condors → butterflies.
- What would prove this wrong.
- Reproduce: the exact `python3 scripts/options_data.py ... --asof YYYY-MM-DD` command(s).
- CLOSE entries add Outcome, What drove the P&L (price move vs time decay vs volatility change, estimated from the entry Greeks), Lesson, and `**Your reflection:**` left EMPTY — never fill it.

STEP 8 — Quarterly note (first cycle after a quarter ends, if `options/quarterly-reports/<YYYY-Qn>.md` does not exist and inception precedes the quarter end): write it with period return vs BXM and PUT, trades opened/closed, win rate, average P&L per trade, largest loss, and a "concepts learned this quarter" list from the Concept Index. The first quarter is partial — label it with its date range.

STEP 9 — Verify then commit: `python3 -c "import json;json.load(open('options/data/positions.json'))"` must succeed. `git add options/`, commit with message "Options cycle #N: <summary>" and body ending with a blank line then `Signed-off-by: hmadhani2024@gmail.com` (no Co-Authored-By). `git pull --rebase origin main` then `git push origin main`. If the push is rejected, pull --rebase again and retry once. No PRs, no gh CLI.

STEP 10 — PushNotification: "Options #N: NAV $X (±Y% vs BXM ±A%, PUT ±B%). Opened: … Closed: … New concepts: …".

If anything is ambiguous or data is missing, do NOT guess numbers — write what you know, mark the gap in the Daily Decision Log, and say so in the notification.
```

- [ ] **Step 2: Write `~/.claude/skills/hm-options-portfolio/SKILL.md`**

```markdown
---
name: hm-options-portfolio
description: |
  NOTE: the daily cloud routine (options-portfolio-daily) embeds its own copy of
  options/routine-prompt.md from the finance-portfolio repo — this skill is for
  manual/interactive runs and learning sessions.

  $50K defined-risk OPTIONS paper portfolio with a beginner learning ledger,
  tracked in the isolated finance-portfolio repo (git@github.com:hmadhani/finance-portfolio.git,
  directory options/). Paper only, public Cboe delayed data only, no personal financial
  data. Use when asked to "run the options portfolio", "options cycle", "explain today's
  options trade", "what did the options portfolio learn", "walk me through the learning
  ledger", or to price/analyze a hypothetical spread with the portfolio's tools.
---

# HM Options Portfolio (paper, defined-risk, learning-first)

## Where things are (finance-portfolio repo)

| File | What |
|---|---|
| `options/investor-profile.md` | All rules (single source of truth) |
| `options/options-portfolio.md` | Portfolio state, NAV history, decision log |
| `options/learning-ledger.md` | Primer, Concept Index, one entry per decision |
| `options/RESOURCES.md` | Verified reading list |
| `options/routine-prompt.md` | Canonical daily cycle (the cloud routine embeds a copy) |
| `options/data/positions.json` | Open positions (machine state) |
| `scripts/options_data.py` | Data + math CLI (stdlib only) |

## Data — how the numbers are pulled

1. **Cboe delayed quotes (primary, free, no key, 15-min delay):**
   `https://cdn.cboe.com/api/global/delayed_quotes/options/<SYM>.json` returns the
   full chain with bid/ask, IV, delta, gamma, theta, vega, open interest; quotes
   `_VIX`, `_VIX3M`, `_BXM`, `_PUT` via `.../quotes/<SYM>.json`; VIX history CSV.
   Always go through `scripts/options_data.py` — never read raw chains into
   context (SPY alone is ~13,000 contracts).
2. **WebSearch/WebFetch:** earnings dates and news only — never prices or Greeks.
3. **IV history:** built by this portfolio in `options/data/iv-history.csv`;
   IV rank is null until 20 observations (VIX percentile is the proxy).
4. **Upgrade path:** a paid API (Tradier, Polygon, MarketData.app) can replace
   `scripts/optlib/chain.py`'s loaders without touching the rest.

## Manual run

Follow `options/routine-prompt.md` exactly.

## Learning session (interactive)

When asked to walk through the ledger: read the newest entries, re-run their
`Reproduce:` commands to show the numbers are real, explain each concept with
the user's questions, and never write into a `**Your reflection:**` section on
their behalf.

## Tools cheat sheet

    python3 scripts/options_data.py regime
    python3 scripts/options_data.py scan --symbols SPY,KO
    python3 scripts/options_data.py price-spread --symbol SPY --qty 1 \
        --legs "SELL 1 P 700 2026-11-06; BUY 1 P 690 2026-11-06"
    python3 scripts/options_data.py mark
    python3 -m unittest discover -s tests -v
```

- [ ] **Step 3: Commit both**

```bash
cd /Users/hmadhani/finance-portfolio
git add options/routine-prompt.md
git commit -m "options: canonical daily routine prompt

AI-assisted change.

Signed-off-by: hmadhani2024@gmail.com"
git pull --rebase origin main && git push origin main

cd /Users/hmadhani/.claude/skills
git add hm-options-portfolio/SKILL.md
git commit -m "hm-options-portfolio: skill for the options paper portfolio

AI-assisted change.

Signed-off-by: hmadhani2024@gmail.com"
git push
```
(Commit ONLY that file in the skills repo — it has unrelated uncommitted changes.)

---

### Task 10: Cloud routine — create disabled, trial run, enable

**Files:** none (remote configuration). Uses `RemoteTrigger` (load via `ToolSearch select:RemoteTrigger`).

- [ ] **Step 1: Push everything**

Run: `cd /Users/hmadhani/finance-portfolio && git status --short && git log origin/main..main --oneline`
Expected: clean tree, nothing unpushed (the cloud clones from GitHub).

- [ ] **Step 2: Create the routine DISABLED**

`RemoteTrigger` `create` with body:
- `name`: `options-portfolio-daily`
- `cron_expression`: `0 16 * * 1-5` (9am PT / 12pm ET — one hour after the stock routine's `0 15 * * 1-5`)
- `enabled`: `false`
- `job_config.ccr.environment_id`: `env_01PpiDxGhno1SJ5Z6wSbopoi`
- `session_context.sources`: `[{"git_repository": {"url": "https://github.com/hmadhani/finance-portfolio"}}]`
- `session_context.allowed_tools`: `["Bash","Read","Write","Edit","Glob","Grep","WebSearch","WebFetch","PushNotification"]`
- `events[0].data`: fresh lowercase v4 `uuid`, `session_id: ""`, `type: "user"`, `parent_tool_use_id: null`, `message: {"role": "user", "content": <full text of options/routine-prompt.md>}`
- No `mcp_connections` (not needed).

Record the returned `trig_…` id.

- [ ] **Step 3: Trial run**

Only on a trading day, during/after market hours (so marks are meaningful). `RemoteTrigger` `run` with the id. Then `list_runs` → `get_run_log` on the run.

Check in the log:
1. `regime` succeeded (Cboe reachable from the sandbox). If it failed with a network error → the degraded path ran; report to the user; decide on a paid API (DECISION.md item 5) before enabling.
2. `unittest` was not required, but `positions.json` validation passed.
3. Commit pushed: `cd /Users/hmadhani/finance-portfolio && git pull --rebase origin main && git log -1 --stat` shows `options/` changes.
4. Read the new `options/learning-ledger.md` entries: every number has a `Reproduce:` command; re-run one locally with the same `--asof` (numbers differ slightly only because quotes moved — the structure must match); `**Your reflection:**` sections are empty.

- [ ] **Step 4: Enable**

Only after Step 3 passes: `RemoteTrigger` `update` with `{"enabled": true}`. Report `next_run_at` and the routine link `https://claude.ai/code/routines/<id>` to the user.

- [ ] **Step 5: Record memory**

Add a project memory file `project_options_portfolio.md` (auto-memory dir) with: routine id, cron, files, data source, "paper only, defined-risk", start date; and one index line in `MEMORY.md`.

---

## Self-review (done while writing)

- Spec coverage: data source (T2, T6), files (T7-T9), profile rules (T7), CLI interface incl. regime/scan/price-spread/mark/record-iv (T6), BS helper + Greek sanity (T1), daily cycle (T9), ledger format + blank reflection (T7, T9), RESOURCES with verification (T8), testing incl. trial cloud run (T1-T6, T10), out-of-scope backlog (T7 DECISION.md). Benchmarks BXM/PUT (T6 regime, T7 header, T9).
- Types consistent: `entry_cost` per share signed (+debit/−credit) in `analyze`, `position_template`, `positions.json`, `mark_position`. `iv30` percent everywhere; contract `iv` decimal.
- Known judgment points left to the routine by design: strategy choice, roll decisions, earnings lookups, teaching text.
