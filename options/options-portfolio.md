# Options Paper Portfolio — $50K (Lt. Cmdr. Data)

IMPORTANT: This is a paper/model options portfolio for learning and evaluation
only, tracked with public, delayed market data (no personal financial context).
It does not constitute investment advice or a recommendation to buy or sell any
security or option. Options involve significant risk and are not suitable for
all investors; see the OCC's "Characteristics and Risks of Standardized Options".

Rules: `options/investor-profile.md` · Teaching: `options/learning-ledger.md` ·
Machine state: `options/data/positions.json`

## Header

| Field | Value |
|---|---|
| Inception | 2026-10-01 (BXM/PUT base levels unavailable — Cboe unreachable on cycle 1; to be set on first successful cycle) |
| Cycle # | 1 |
| NAV | $50,000.00 |
| Cash | $50,000.00 |
| Collateral / max loss reserved | $0.00 |
| Capital at risk (sum of max losses) | $0.00 (0.0% NAV) |
| Net delta (share-equivalents) | 0 |
| Net theta ($/day) | 0.00 |
| Net vega ($/IV point) | 0.00 |
| Return since inception | 0.00% |
| BXM since inception | — |
| PUT since inception | — |
| Regime | Unknown (Cboe data unreachable, degraded cycle) |

## Open Positions

| ID | Symbol | Strategy | Opened | Expiry | Qty | Entry $/sh | Mark $/sh | P&L $ | % of basis | Max loss $ | DTE | Triggers |
|---|---|---|---|---|---|---|---|---|---|---|---|---|

## Closed Positions

| ID | Symbol | Strategy | Opened | Closed | Realized P&L $ | Exit reason | Ledger entry |
|---|---|---|---|---|---|---|---|

## NAV History

Append-only. One row per cycle.

| Date | Cycle # | NAV | BXM | PUT | VIX |
|---|---|---|---|---|---|
| 2026-10-01 | 1 (degraded — no marks; no positions open) | $50,000.00 | — | — | — |

## Daily Decision Log

Reverse-chronological. One heading per cycle: `### YYYY-MM-DD — Cycle #N: <summary>`.

### 2026-10-01 — Cycle #1 (degraded): Cboe unreachable, no trades

- `regime` failed entirely: every Cboe fetch (VIX, VIX3M, BXM, PUT) returned `Tunnel connection failed: 403 Forbidden` from the sandbox proxy. Degraded mode per routine rules: no new positions opened.
- `mark` ran (exit 0) but there are no open positions, so nothing to manage and no triggers.
- NAV carried at the starting $50,000.00 (all cash; no interest accrued since inception is today). BXM/PUT/VIX base levels could NOT be recorded — they are left blank rather than guessed; set them on the first cycle with working data.
