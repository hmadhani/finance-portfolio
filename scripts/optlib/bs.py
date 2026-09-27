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
    if T <= 0 or sigma <= 0:
        if kind == "C":
            delta = 1.0 if S > K else 0.0
        else:
            delta = -1.0 if S < K else 0.0
        return {"delta": delta, "gamma": 0.0, "theta": 0.0, "vega": 0.0}
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
