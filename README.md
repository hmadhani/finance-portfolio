# finance-portfolio

Isolated repo for a cloud-automated, market-data-only paper trading experiment
(synthetic $100K portfolio). Deliberately contains **no personal financial data**
(no account balances, tax lots, concentration flags) — the Monday cloud routine
that writes to this repo only ever sees public market data (yfinance prices,
WebSearch research) and its own prior state in this repo.

This is separate from and does not replace the personally-gated model portfolio
tracked in the a separate personal tracking system
(`finance/financial_research/model_portfolio_2026-08-25.md`), which continues to
route every trade through `hm-sc-stock-research-loop`'s full financial-context
verdict discipline.

`portfolio.md` (created by the first Monday run) is the single artifact of record
for this repo's experiment.
