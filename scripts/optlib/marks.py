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
