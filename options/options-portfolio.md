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
| Cycle # | 11 |
| NAV | $49,241.36 |
| Cash | $48,380.86 |
| Collateral / max loss reserved | $970.00 |
| Capital at risk (sum of max losses) | $970.00 (2.0% NAV) |
| Net delta (share-equivalents) | 40.09 |
| Net theta ($/day) | -14.03 |
| Net vega ($/IV point) | 40.41 |
| Return since inception | -1.52% |
| BXM since inception | +0.58% |
| PUT since inception | +0.59% |
| Regime | VIX 16.75 / VIX3M 18.65 contango, not stress; VIX 1y percentile 44.0 (in between) → no new trade |

## Open Positions

| ID | Symbol | Strategy | Opened | Expiry | Qty | Entry $/sh | Mark $/sh | P&L $ | % of basis | Max loss $ | DTE | Triggers |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2026-10-02-SPY-BCDS-1 | SPY | bull_call_debit_spread | 2026-10-02 | 2026-11-06 | 1 | 9.70 | 8.605 | -109.50 | -11.3% | 970 | 22 | none |

## Closed Positions

| ID | Symbol | Strategy | Opened | Closed | Realized P&L $ | Exit reason | Ledger entry |
|---|---|---|---|---|---|---|---|
| 2026-10-05-QQQ-BCDS-1 | QQQ | bull_call_debit_spread | 2026-10-05 | 2026-10-14 | -731.35 | stop_loss (-67.1%) | [2026-10-14 CLOSE](learning-ledger.md#2026-10-14--close-qqq-bull-call-debit-spread-cycle-10) |

## NAV History

Append-only. One row per cycle.

| Date | Cycle # | NAV | BXM | PUT | VIX |
|---|---|---|---|---|---|
| 2026-10-01 | 1 (degraded — no marks; no positions open) | $50,000.00 | — | — | — |
| 2026-10-02 | 2 | $50,001.86 | 2564.68 | 3681.24 | 15.65 |
| 2026-10-05 | 3 | $50,139.45 | 2571.02 | 3690.31 | 15.57 |
| 2026-10-06 | 4 | $50,664.36 | 2575.32 | 3696.35 | 15.23 |
| 2026-10-07 | 5 | $50,320.77 | 2574.62 | 3695.47 | 15.35 |
| 2026-10-08 | 6 | $50,134.19 | 2574.71 | 3695.88 | 15.48 |
| 2026-10-09 | 7 | $50,072.11 | 2578.12 | 3699.27 | 14.88 |
| 2026-10-12 | 8 | $50,019.36 | 2578.99 | 3701.72 | 15.14 |
| 2026-10-13 | 9 | $49,765.78 | 2579.27 | 3702.09 | 15.44 |
| 2026-10-14 | 10 | $49,269.90 | 2578.09 | 3701.46 | 16.19 |
| 2026-10-15 | 11 | $49,241.36 | 2579.69 | 3703.08 | 16.75 |

## Daily Decision Log

Reverse-chronological. One heading per cycle: `### YYYY-MM-DD — Cycle #N: <summary>`.

### 2026-10-15 — Cycle #11: SPY spread -11.3%, no trigger (21 DTE tomorrow); PASS

- Regime: VIX 16.75, VIX3M 18.65 (contango, no stress), VIX 1y percentile 44.0 (in between). IV history 9 days, so VIX percentile is the proxy. `regime` errors: none.
- HOLD 2026-10-02-SPY-BCDS-1: mark 8.605 vs 9.70 entry, P&L -$109.50 (-11.3%), 22 DTE, no triggers. 21 DTE arrives 2026-10-16: close or roll then.
- PASS on new trades: in-between regime gives no edge, and the only holding is a bullish SPY bet already slightly red. See ledger PASS.
- Interest accrued $5.96 (1 day at 4.5% on $48,374.90). NAV $49,241.36 (cash $48,380.86 + SPY spread $860.50 at mid). Net Greeks from `price-spread`. IV recorded (30 symbols).

### 2026-10-14 — Cycle #10: QQQ spread stopped out (-$731.35); SPY spread -7.7%, no trigger; PASS

- Regime: VIX 16.19, VIX3M 18.42 (contango, no stress), VIX 1y percentile 33.7. IV history 8 days, so VIX percentile is the proxy. `regime` errors: none.
- CLOSE 2026-10-05-QQQ-BCDS-1: `stop_loss` fired (mark 3.56 vs 10.8325 entry, -67.1%). Closed via `price-spread` at fills 4.00 / 0.455 (credit 3.545/sh). Realized -$731.35 after $2.60 fees. See ledger CLOSE.
- HOLD 2026-10-02-SPY-BCDS-1: mark 8.95 vs 9.70 entry, P&L -$75.00 (-7.7%), 23 DTE, no triggers. 21 DTE arrives 2026-10-16: close or roll then.
- PASS on new trades: just stopped out of a bullish bet; no revenge trade, and VIX percentile does not favor selling premium. See ledger PASS.
- Interest accrued $5.92 (1 day at 4.5% on $48,015.78). Close cash +$353.20 (credit $354.50 - $1.30 exit fee). NAV $49,269.90 (cash $48,374.90 + SPY spread $895.00 at mid). Net Greeks from `price-spread`. IV recorded (30 symbols).

### 2026-10-13 — Cycle #9: QQQ spread -46.5% (stop is -50%), SPY spread +20.7%, no triggers; PASS

- Regime: VIX 15.44, VIX3M 18.03 (contango, no stress), VIX 1y percentile 18.7 → cheap options. IV history only 7 days, so the VIX percentile is the proxy. `regime` errors: none.
- HOLD 2026-10-02-SPY-BCDS-1: mark 11.705 vs 9.70 entry, P&L +$200.50 (+20.7%), 24 DTE, no triggers.
- HOLD 2026-10-05-QQQ-BCDS-1: mark 5.795 vs 10.8325 entry, P&L -$503.75 (-46.5%), 24 DTE, no triggers. The -50% stop sits at a mark of about 5.416, so it is within about 0.38/sh ($38). Both hit 21 DTE on 2026-10-16: close or roll then; a stop hit before that closes QQQ.
- PASS on new trades: same correlated bullish bet; QQQ is nearly stopped out, and adding more would be averaging down. See ledger PASS entry.
- Interest accrued $5.92 (1 day at 4.5% on $48,009.86). NAV $49,765.78 (cash $48,015.78 + positions $1,750.00 at mid). Net Greeks summed from `price-spread` runs. IV recorded (30 symbols).

### 2026-10-12 — Cycle #8: SPY spread +30.1%, QQQ spread -31.0%, no triggers; PASS

- Regime: VIX 15.14, VIX3M 17.87 (contango, no stress), VIX 1y percentile 13.1 → cheap options. IV history only 6 days, so the VIX percentile is the proxy. `regime` errors: none.
- HOLD 2026-10-02-SPY-BCDS-1: mark 12.62 vs 9.70 entry, P&L +$292.00 (+30.1%), 25 DTE, no triggers.
- HOLD 2026-10-05-QQQ-BCDS-1: mark 7.475 vs 10.8325 entry, P&L -$335.75 (-31.0%), 25 DTE, no triggers (stop is -50% of debit, i.e. mark ~5.42). Both hit 21 DTE on 2026-10-16: close or roll then.
- PASS on new trades: same correlated bullish bet already held. See ledger PASS entry.
- Interest accrued $17.75 (3 days at 4.5% on $47,992.11). NAV $50,019.36 (cash $48,009.86 + positions $2,009.50 at mid). Net Greeks summed from `price-spread` runs. IV recorded (30 symbols).

### 2026-10-09 — Cycle #7: SPY spread +24.9%, QQQ spread -19.9% (index split), no triggers; PASS

- Regime: VIX 14.88, VIX3M 17.88 (contango, no stress), VIX 1y percentile 8.3 → very cheap options. IV history only 5 days, so the VIX percentile is the proxy. `regime` errors: none.
- HOLD 2026-10-02-SPY-BCDS-1: mark 12.12 vs 9.70 entry, P&L +$242.00 (+24.9%), 28 DTE, no triggers.
- HOLD 2026-10-05-QQQ-BCDS-1: mark 8.68 vs 10.8325 entry, P&L -$215.25 (-19.9%), 28 DTE, no triggers (stop is -50% of debit, i.e. mark ~5.42).
- PASS on new trades: still one correlated bullish bet, now split (SPY up, QQQ down). See ledger PASS entry.
- Interest accrued $5.92 (1 day at 4.5% on $47,986.19). NAV $50,072.11 (cash $47,992.11 + positions $2,080.00 at mid). Net Greeks summed from `price-spread` runs. IV recorded (30 symbols).

### 2026-10-08 — Cycle #6: market slipped again, SPY spread +15.6%, QQQ spread -5.2%, no triggers; PASS

- Regime: VIX 15.48, VIX3M 18.05 (contango, no stress), VIX 1y percentile 19.0 → cheap options. IV history only 4 days, so the VIX percentile is the proxy. `regime` errors: none.
- HOLD 2026-10-02-SPY-BCDS-1: mark 11.21 vs 9.70 entry, P&L +$151.00 (+15.6%), 29 DTE, no triggers.
- HOLD 2026-10-05-QQQ-BCDS-1: mark 10.27 vs 10.8325 entry, P&L -$56.25 (-5.2%), 29 DTE, no triggers (stop is -50% of debit).
- PASS on new trades: still the same correlated bullish bet; QQQ is now slightly red. See ledger PASS entry.
- Interest accrued $5.92 (1 day at 4.5% on $47,980.27). NAV $50,134.19 (cash $47,986.19 + positions $2,148.00 at mid). Net Greeks summed from `price-spread` runs. IV recorded.

### 2026-10-07 — Cycle #5: market dipped, both spreads still green, no triggers; PASS

- Regime: VIX 15.35, VIX3M 17.87 (contango, no stress), VIX 1y percentile 15.9 → cheap options; IV history only 3 days so the VIX percentile is the proxy. `regime` errors: none.
- HOLD 2026-10-02-SPY-BCDS-1: mark 11.975 vs 9.70 entry, P&L +$227.50 (+23.5%), 30 DTE, no triggers.
- HOLD 2026-10-05-QQQ-BCDS-1: mark 11.43 vs 10.8325 entry, P&L +$59.75 (+5.5%), 30 DTE, no triggers.
- PASS on new trades: both holdings are the same bullish Nov-06 index bet; a third adds correlated risk. See ledger PASS entry.
- Interest accrued $5.91 (1 day at 4.5% on $47,974.36). NAV $50,320.77 (positions marked at mid; cash $47,980.27 + $2,340.50). Net Greeks summed from `price-spread` runs. IV recorded (30 symbols).

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
