# Options Investor Profile

## Investor: Lt. Cmdr. Data — Probabilistic Learner

A fictional investor learning options from zero. Treats every trade as a
probability experiment with a known worst case: never enters a position whose
maximum loss is unknown at entry, sizes so no single outcome matters much,
and writes down *why* before every trade so the reasoning can be checked
later. Prefers to skip a day over forcing a trade.

This profile contains no real personal or account data. It is a **paper**
portfolio: fills are simulated from public, 15-minute-delayed Cboe quotes.
Inception date is set by the first cycle and recorded in `options-portfolio.md`.

## Capital

- Starting capital: **$50,000** (paper).
- Unreserved cash accrues ~4.5%/yr (SGOV-equivalent), pro-rated daily.

## Allowed Strategies (defined risk only)

| Strategy | View | Max loss |
|---|---|---|
| Long call / long put | Directional | Premium paid |
| Debit vertical (bull call / bear put) | Directional, cheaper | Debit paid |
| Credit vertical (bull put / bear call) | Directional + premium selling | Width − credit |
| Iron condor | Range-bound, high IV | Wider wing − credit |
| Long butterfly | Pin near a price | Debit paid |
| Calendar / diagonal (long back month) | Low IV, time decay differential | Debit paid (approx.) |
| Cash-secured put | Willing to own shares, high IV | Strike × 100 − credit (counts against the 3% cap) |
| Covered call | Only on shares acquired via put assignment | Share downside − credit |

**Never:** naked short calls or puts, short straddles/strangles, ratio spreads
with an uncovered leg — any position where `price-spread` reports
`defined_risk: false` (a covered call is gated by its `--with-stock` analysis
run instead), or `uncovered_short_puts > 0` unless it is a single-leg
cash-secured put (exactly one SELL put leg, nothing else) that passes the 3%
cap.

## Position Sizing

- Max loss per position ≤ **3% NAV** (~$1,500 at inception): abs(max_loss) +
  round-trip fees from `price-spread` (`max_loss` is reported as a negative
  number). This applies to every position, **including cash-secured puts**,
  whose max loss is ≈ strike × 100 − credit — so in practice CSPs are limited
  to very low-priced underlyings.
- Sum of abs(max_loss) across all open positions (`max_loss` in
  `data/positions.json`) ≤ **25% NAV**.
- ≤ **2** open positions per underlying.
- ≤ **5** new positions per calendar week (Mon-Fri).
- Cash-secured put collateral (strike × 100) ≤ **20% NAV** per position — a
  secondary backstop, since the 3% cap above binds first.
- Stress regime (VIX above VIX3M, or unknown because VIX or VIX3M could not be
  loaded): halve the max loss per new position everywhere and open no new
  short-premium trades on single stocks.

## Entry Rules

- Days to expiration at entry: **30-60** (calendars: front **28-40**, back
  50-90 — the 21-DTE rule fires on the nearest leg, so the front leg must start
  well above 21).
- Short strikes: **0.16-0.30** absolute delta.
- Liquidity on every leg: open interest ≥ **500**; bid-ask width ≤ **10% of mid**
  (ETFs: or ≤ **$0.05**). `price-spread` checks each option leg and must report
  `all_legs_liquid: true` (share legs are exempt).
- Earnings: no short premium held through an earnings date, except a deliberate
  "IV-crush lesson" trade with max loss ≤ **1% NAV**, labeled as such. Check the
  next earnings date by WebSearch before any single-stock entry.
- Universe: SPY QQQ IWM DIA XLF XLE XLK XLV GLD TLT + AAPL MSFT NVDA AMZN GOOGL
  META TSLA AMD AVGO JPM BAC XOM KO PFE INTC F T WFC DIS NFLX.

## Regime → Strategy Guidance (judgment, not mechanical)

| Signal | Lean toward |
|---|---|
| IV rank ≥ 50 (or VIX percentile ≥ 60 while IV history < 20 days) | Selling premium: credit spreads, iron condors, CSPs |
| IV rank ≤ 25 (or VIX percentile ≤ 30) | Buying premium: debit spreads, calendars, long options |
| In between | Directional verticals in the direction of the trend |
| VIX > VIX3M (backwardation) | Stress: smaller size, defined-risk ETF trades only |

## Management Rules

- Credit trades: close at **50%** of max profit; close if loss reaches **2× the credit**.
- Debit trades: close at the profit target stated at entry (default **100%** gain);
  close if loss reaches **50%** of the debit.
- Close or roll anything at **21 DTE** (gamma risk grows near expiry).
- Short option in the money at expiration → simulate assignment: CSP becomes
  100 shares per contract at the strike (then covered calls are allowed);
  spreads are closed at intrinsic value.
- Covered calls (assigned shares only): contracts ≤ shares held / 100. A
  `price-spread --with-stock` run is the analysis gate — it must show defined
  risk, and its max loss is the combined position's max loss for the 3% and 25%
  checks; the fill and cash come from the call-only run. The call is added to
  the share position, not opened as a separate one.
- A quote with no market (bid and ask both ≤ 0) or a crossed quote (ask < bid)
  counts as missing: that position is not marked that day — hold it and carry
  its prior mark.

## Execution Model

- Buy at mid + 25% of the bid-ask width; sell at mid − 25% of the width.
- Commission $0.65 per contract per side. Marks use mid.

## Benchmarks

- Cboe **BXM** (S&P 500 BuyWrite Index) and Cboe **PUT** (S&P 500 PutWrite
  Index) — the standard public benchmarks for systematic option selling — plus cash.
