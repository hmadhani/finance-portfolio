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
