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
