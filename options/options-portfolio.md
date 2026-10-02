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
| Inception | 2026-10-01 (BXM 2,555.60 / PUT 3,670.90 / VIX 16.39 base levels set 2026-10-02, the first cycle with working Cboe data) |
| Cycle # | 2 |
| NAV | $49,994.21 |
| Cash | $50,275.71 |
| Collateral / max loss reserved | $2,225.25 |
| Capital at risk (sum of max losses) | $2,225.25 (4.45% NAV) |
| Net delta (share-equivalents) | +64.5 |
| Net theta ($/day) | +5.12 |
| Net vega ($/IV point) | -25.66 |
| Return since inception | -0.01% |
| BXM since inception | 0.00% (base set today) |
| PUT since inception | 0.00% (base set today) |
| Regime | Normal: VIX 16.39 < VIX3M 18.58 (contango), VIX 1-yr percentile 34.1 — in-between, no stress |

## Open Positions

| ID | Symbol | Strategy | Opened | Expiry | Qty | Entry $/sh | Mark $/sh | P&L $ | % of basis | Max loss $ | DTE | Triggers |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2026-10-02-SPY-BPS-1 | SPY | bull_put_spread | 2026-10-02 | 2026-11-06 | 1 | -1.135 | -1.18 | -4.50 | -4.0% | 886.50 | 35 | none |
| 2026-10-02-TLT-BPS-1 | TLT | bull_put_spread | 2026-10-02 | 2026-11-06 | 3 | -0.5375 | -0.545 | -2.25 | -1.4% | 1338.75 | 35 | none |

## Closed Positions

| ID | Symbol | Strategy | Opened | Closed | Realized P&L $ | Exit reason | Ledger entry |
|---|---|---|---|---|---|---|---|

## NAV History

Append-only. One row per cycle.

| Date | Cycle # | NAV | BXM | PUT | VIX |
|---|---|---|---|---|---|
| 2026-10-01 | 1 (degraded — no marks; no positions open) | $50,000.00 | — | — | — |
| 2026-10-02 | 2 | $49,994.21 | 2,555.60 | 3,670.90 | 16.39 |

## Daily Decision Log

Reverse-chronological. One heading per cycle: `### YYYY-MM-DD — Cycle #N: <summary>`.

### 2026-10-02 — Cycle #2: first full cycle — opened SPY and TLT bull put spreads (overwrites degraded Cycle #2)

- The earlier degraded Cycle #2 (Cboe unreachable) was, on the user's instruction, re-run in full: its NAV row and Header are overwritten by this one (its log text is kept below for history); Cycle #1 (degraded) is retained. Inception remains 2026-10-01; BXM/PUT/VIX base levels (2,555.60 / 3,670.90 / 16.39) are recorded today.
- Regime: VIX 16.39, VIX3M 18.58 → contango, `stress: false`; VIX 1-yr percentile 34.1 → in-between, so directional/trend-following verticals. IV history is 0 days (record-iv appended 30 symbols today), so VIX percentile is the proxy.
- `mark`: no positions open before today's trades, no triggers.
- NEW 2026-10-02-SPY-BPS-1: SELL 735P / BUY 725P, 2026-11-06 (35 DTE), qty 1, credit $1.135/sh, max loss $886.50 (+$2.60 fees; cap 3% NAV = $1,500). All legs liquid. Fees $1.30 at entry.
- NEW 2026-10-02-TLT-BPS-1: SELL 75P / BUY 70P, 2026-11-06 (35 DTE), qty 3, credit $0.5375/sh, max loss $1,338.75 (+$7.80 fees). qty = floor(1500.18 / 448.85) = 3. All legs liquid. Fees $3.90 at entry.
- Both ETFs, so no earnings check needed. Capital at risk $2,225.25 (4.45% NAV) < 25%; 1 position per underlying; 2 new positions this week (≤5).
- NAV = cash $50,275.71 + marks (SPY −$118.00, TLT −$163.50) = $49,994.21. The −$6 vs. start is the bid/ask give-up on entry plus fees; no interest accrued beyond the $6.16 already carried in cash.

### 2026-10-02 — Cycle #2 (degraded) — SUPERSEDED by the full Cycle #2 above; kept for history: Cboe still unreachable, no trades

- `regime` exited 1 again: all Cboe fetches (VIX, VIX3M, BXM, PUT) returned `Tunnel connection failed: 403 Forbidden`. Degraded mode: no new positions, no scan, no record-iv.
- `mark` ran (exit 0): no open positions, no triggers.
- NAV = cash $50,000.00 + 1 day interest at 4.5%/yr ($6.16) = $50,006.16. BXM/PUT/VIX base levels still unrecorded (not guessed).
- No ledger entries: nothing opened, closed or assigned.

### 2026-10-01 — Cycle #1 (degraded): Cboe unreachable, no trades

- `regime` failed entirely: every Cboe fetch (VIX, VIX3M, BXM, PUT) returned `Tunnel connection failed: 403 Forbidden` from the sandbox proxy. Degraded mode per routine rules: no new positions opened.
- `mark` ran (exit 0) but there are no open positions, so nothing to manage and no triggers.
- NAV carried at the starting $50,000.00 (all cash; no interest accrued since inception is today). BXM/PUT/VIX base levels could NOT be recorded — they are left blank rather than guessed; set them on the first cycle with working data.
