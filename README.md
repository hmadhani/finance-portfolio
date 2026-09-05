# finance-portfolio

Isolated repo for a cloud-automated, market-data-only paper trading experiment
(synthetic $100K portfolio). Deliberately contains **no personal financial data**
(no account balances, tax lots, concentration flags) — the Mon/Wed/Fri cloud
routine that writes to this repo only ever sees public market data (WebSearch/
WebFetch prices and research) and its own prior state in this repo, including
`investor-profile.md` (a fictional risk-posture profile, "Mr. Spock — Logical
Investor," containing zero real personal data) and `DECISION.md` (a design
backlog).

This is separate from, and does not replace, a personally-gated model-portfolio
track that runs elsewhere with full financial-context verdict discipline (real
account data, tax lots, concentration limits) — that track is intentionally
kept out of this repo entirely.

`portfolio.md` is the single artifact of record for current state.
`quarterly-reports/` holds generated Markdown + XLS performance reports on a
quarterly and annual cadence.
