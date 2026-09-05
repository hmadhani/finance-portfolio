# finance-portfolio

Isolated repo for a cloud-automated, market-data-only paper trading experiment
(synthetic $100K portfolio). Deliberately contains **no personal financial data**
(no account balances, tax lots, concentration flags) — the Monday cloud routine
that writes to this repo only ever sees public market data (yfinance prices,
WebSearch research) and its own prior state in this repo.

This is separate from, and does not replace, a personally-gated model-portfolio
track that runs elsewhere with full financial-context verdict discipline (real
account data, tax lots, concentration limits) — that track is intentionally
kept out of this repo entirely.

`portfolio.md` (created by the first Monday run) is the single artifact of record
for this repo's experiment.
