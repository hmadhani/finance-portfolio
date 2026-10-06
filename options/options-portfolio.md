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
| Inception | 2026-10-01 (BXM/PUT/VIX base levels set 2026-10-02: BXM 2564.68, PUT 3681.24, VIX 15.65) |
| Cycle # | 4 |
| NAV | $50,664.36 |
| Cash | $47,974.36 |
| Collateral / max loss reserved | $2,053.25 |
| Capital at risk (sum of max losses) | $2,053.25 (4.1% NAV) |
| Net delta (share-equivalents) | 64.35 |
| Net theta ($/day) | -9.46 |
| Net vega ($/IV point) | 19.25 |
| Return since inception | +1.33% |
| BXM since inception | +0.41% |
| PUT since inception | +0.41% |
| Regime | VIX 15.23 / VIX3M 17.79 contango, not stress; VIX 1y percentile 13.9 (low) → buy premium |

## Open Positions

| ID | Symbol | Strategy | Opened | Expiry | Qty | Entry $/sh | Mark $/sh | P&L $ | % of basis | Max loss $ | DTE | Triggers |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2026-10-02-SPY-BCDS-1 | SPY | bull_call_debit_spread | 2026-10-02 | 2026-11-06 | 1 | 9.70 | 13.82 | +411.50 | +42.4% | 970 | 31 | none |
| 2026-10-05-QQQ-BCDS-1 | QQQ | bull_call_debit_spread | 2026-10-05 | 2026-11-06 | 1 | 10.83 | 13.09 | +225.25 | +20.8% | 1083 | 31 | none |

## Closed Positions

| ID | Symbol | Strategy | Opened | Closed | Realized P&L $ | Exit reason | Ledger entry |
|---|---|---|---|---|---|---|---|

## NAV History

Append-only. One row per cycle.

| Date | Cycle # | NAV | BXM | PUT | VIX |
|---|---|---|---|---|---|
| 2026-10-01 | 1 (degraded — no marks; no positions open) | $50,000.00 | — | — | — |
| 2026-10-02 | 2 | $50,001.86 | 2564.68 | 3681.24 | 15.65 |
| 2026-10-05 | 3 | $50,139.45 | 2571.02 | 3690.31 | 15.57 |
| 2026-10-06 | 4 | $50,664.36 | 2575.32 | 3696.35 | 15.23 |

## Daily Decision Log

Reverse-chronological. One heading per cycle: `### YYYY-MM-DD — Cycle #N: <summary>`.

### 2026-10-06 — Cycle #4: both spreads up, no triggers; PASS on new trades

- Regime: VIX 15.23, VIX3M 17.79 (contango, no stress), VIX 1y percentile 13.9 → very cheap options, lean to buying premium. IV history still only 2 days, so the VIX percentile is the proxy.
- HOLD 2026-10-02-SPY-BCDS-1: mark 13.815 vs 9.70 entry, P&L +$411.50 (+42.4%), 31 DTE, no triggers (profit target +100%).
- HOLD 2026-10-05-QQQ-BCDS-1: mark 13.085 vs 10.8325 entry, P&L +$225.25 (+20.8%), 31 DTE, no triggers.
- PASS on new trades: both open positions are the same bullish Nov-06 index bet; a third would stack correlated delta right after a sharp rally. See ledger PASS entry.
- Interest accrued $5.91 (1 day at 4.5% on $47,968.45). NAV $50,664.36 (positions marked at mid). Net Greeks summed from `price-spread` runs of each position.

### 2026-10-05 — Cycle #3: SPY spread +12.5%, opened QQQ bull call debit spread

- Regime: VIX 15.57, VIX3M 18.06 (contango, no stress), VIX 1y percentile 18.3 → still cheap options, lean to buying premium. IV history only 1 day, so VIX percentile is the proxy.
- HOLD 2026-10-02-SPY-BCDS-1: mark 10.915 vs 9.70 entry, P&L +$121.50, 32 DTE, no triggers (profit target is +100%).
- NEW 2026-10-05-QQQ-BCDS-1: QQQ 760/790 Nov-06 call debit spread, 1 lot, debit $10.83, max loss $1,083 (+$2.60 fees) ≤ 3% NAV; total capital at risk 4.1% NAV. Second index-ETF bull spread is correlated with SPY; kept to 1 trade and small size. Both positions are on the same Nov-06 expiry and the same direction.
- Interest accrued $18.14 (3 days at 4.5% on $49,034.86). Entry fee $1.30. NAV $50,139.45 (QQQ marked at mid 10.795).
- Net Greeks summed from `price-spread` runs of each position at current quotes.

### 2026-10-02 — Cycle #2: Cboe back online; opened SPY bull call debit spread

- Regime: VIX 15.65, VIX3M 18.24 (contango, no stress), VIX 1y percentile 18.7 → cheap options, lean to buying premium. IV history has 0 days, so the VIX percentile is the proxy. BXM/PUT base levels recorded today.
- No open positions to manage (`mark` empty at start).
- NEW 2026-10-02-SPY-BCDS-1: SPY 773/800 Nov-06 call debit spread, 1 lot, debit $9.70, max loss $970 (+$2.60 fees), 1.9% of NAV. Only 1 trade today — one clean low-IV trade is enough.
- Interest accrued $6.16 (1 day at 4.5% on $50,000 cash). NAV $50,001.86 (spread marked at 9.67 mid).

### 2026-10-01 — Cycle #1 (degraded): Cboe unreachable, no trades

- `regime` failed entirely: every Cboe fetch (VIX, VIX3M, BXM, PUT) returned `Tunnel connection failed: 403 Forbidden` from the sandbox proxy. Degraded mode per routine rules: no new positions opened.
- `mark` ran (exit 0) but there are no open positions, so nothing to manage and no triggers.
- NAV carried at the starting $50,000.00 (all cash; no interest accrued since inception is today). BXM/PUT/VIX base levels could NOT be recorded — they are left blank rather than guessed; set them on the first cycle with working data.
