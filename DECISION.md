# Decision Backlog — finance-portfolio

Dated 2026-09-05. Deferred blind-spot fixes identified during the investor-profile
design pass, not yet built. No personal data in this file.

## 1. Drawdown-proxy rejection test

Currently the "20-30% single-day drawdown survivability" check in
`investor-profile.md` is a qualitative judgment call written into each trade's
rationale — not mechanically enforced. Build: reject any candidate whose
trailing 1-year max single-day drop exceeds a defined threshold, or reject a
trade if it pushes portfolio-implied beta above a cap.

## 2. Dynamic hedge sizing

The hedge sleeve (GLD/IAU) is a static ~7% target. A real risk-parity-style
hedge scales up in high-volatility regimes rather than staying flat. Build: a
vol-regime signal (e.g. VIX level/trend) that widens the hedge sleeve's target
band in high-vol periods and narrows it in calm periods.

## 3. Momentum-screen counterweight

The W2 baseline screener (revenue growth >10%, top-30%-of-sector relative
strength) is a momentum/quality screen that will systematically re-buy
whatever sector is currently hot, quietly reinforcing theme concentration
over many cycles even though each individual buy passes the 25% theme cap at
the time. Build: a periodic value/turnaround counterweight screen (e.g.
bottom-30% relative strength within a sector but improving fundamentals) to
run alongside W2 rather than exclusively.

## Status

All three are qualitative/manual for now — the loop's written rationale for
each new buy should note whether it was screened against a "hot" theme, as a
manual stopgap until item 3 is built. Revisit after a few quarters of
Quarterly Report data exist to see whether these gaps are actually biting.
