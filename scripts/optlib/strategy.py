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
from .chain import Contract, has_valid_quote, occ_symbol, stock_contract

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
        ratio = int(ratio)
        if ratio <= 0:
            raise ValueError(f"bad leg spec {part.strip()!r}: ratio must be > 0")
        out.append((action, ratio, kind, float(strike), date.fromisoformat(exp)))
    return out


def legs_from_spec(spec: str, root: str, cs_index: dict, spot: float = None,
                   with_stock: bool = False) -> list:
    legs = []
    for action, ratio, kind, strike, exp in parse_leg_spec(spec):
        sym = occ_symbol(root, exp, kind, strike)
        if sym not in cs_index:
            raise KeyError(f"no quote for {sym} ({action} {kind} {strike} {exp})")
        if not has_valid_quote(cs_index[sym]):
            c = cs_index[sym]
            raise KeyError(f"no valid quote for {sym} (bid {c.bid}, ask {c.ask}): "
                           "no market or crossed quote")
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

    # Unboundedness is a structural property of net upside exposure, not a
    # finite-difference slope: puts can never make loss unbounded (S >= 0),
    # and a long back-month call in a calendar may not have converged to its
    # linear asymptote by 2x the highest strike at high IV/long DTE, which
    # would make the slope test wrongly flag an in-rule calendar as unbounded.
    upside_exposure = sum(l.sign * l.ratio for l in legs if l.contract.kind in ("C", "S"))
    unbounded_profit = upside_exposure > 0
    unbounded_loss = upside_exposure < 0
    # Short puts not covered by a long put. Puts have bounded loss (S >= 0), so
    # defined_risk alone cannot catch a 1x2 put ratio spread or a CSP; the
    # routine only allows uncovered_short_puts > 0 for a single-leg CSP.
    uncovered_short_puts = max(0, -sum(l.sign * l.ratio for l in legs if l.contract.kind == "P"))

    # For bounded structures whose per-leg BS value hasn't fully converged at
    # the grid's 2x-strike boundary (e.g. a high-IV calendar), sample a much
    # further point to get max_profit/max_loss closer to the true extremum.
    # The original grid resolution is kept for breakevens and the ASCII plot.
    far = max([l.contract.strike for l in legs if l.contract.kind != "S"] + [spot]) * 10.0
    tail_pnls = pnls + [pnl_at(legs, far, ev, cost) * qty]

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
        "max_profit": None if unbounded_profit else round(max(tail_pnls), 2),
        "max_loss": None if unbounded_loss else round(min(tail_pnls), 2),
        "unbounded_profit": unbounded_profit,
        "unbounded_loss": unbounded_loss,
        "defined_risk": not unbounded_loss,
        "uncovered_short_puts": uncovered_short_puts,
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
