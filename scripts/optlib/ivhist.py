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
    new = []
    for r in rows:
        key = (day, r[0])
        if key not in existing:
            existing.add(key)
            new.append(r)
    write_header = not os.path.exists(path) or os.path.getsize(path) == 0
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    with open(path, "a", newline="") as f:
        w = csv.writer(f, lineterminator="\n")
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


def vix_percentile(csv_text: str, current: float, lookback: int = 252):
    """Percent of the last `lookback` VIX closes below `current`, or None when
    the text holds no closes (empty, header-only, an HTML error page, or no
    CLOSE column)."""
    closes = []
    for r in csv.DictReader(io.StringIO(csv_text)):
        try:
            closes.append(float(r["CLOSE"]))
        except (KeyError, TypeError, ValueError):
            continue
    closes = closes[-lookback:]
    if not closes:
        return None
    return round(sum(1 for c in closes if c < current) / len(closes) * 100.0, 1)
