# Options Paper Portfolio — Design Spec

Date: 2026-09-27 · Status: approved in brainstorming session

## Goal

A $50,000 **paper** options portfolio, run daily by a cloud routine, that doubles
as a learning tool for a beginner. Every decision (open, adjust, close, pass) is
explained in a learning ledger at beginner depth, with numbers that can be
reproduced from a script. Fully separate from the $100K stock paper portfolio
(own files, own routine, own benchmark), same repo.

## Decisions made (brainstorming answers)

| Question | Answer |
|---|---|
| Paper or real money | Paper only |
| Strategy universe | Defined-risk only — no naked short options |
| Cadence | Daily cloud routine, every trading day |
| Underlyings | Liquid ETFs + ~20 high-volume mega-caps, independent of the stock portfolio |
| Learner level | Beginner — explain every term on first use |
| Data approach | Option A: script-backed (Cboe delayed-quotes JSON + deterministic Python math); model does judgment and teaching |

## Data source (verified 2026-09-27 from local machine)

- `https://cdn.cboe.com/api/global/delayed_quotes/options/<SYM>.json` — full
  chain, per contract: bid/ask/sizes, iv, delta, gamma, vega, theta, rho, theo,
  open_interest, volume, last price. SPY returned 12,940 contracts. 15-min delayed.
- `https://cdn.cboe.com/api/global/delayed_quotes/quotes/_VIX.json` — VIX quote
  (same pattern for `_VIX3M`).
- VIX daily history CSV (Cboe) — for VIX percentile until per-underlying IV
  history accumulates. URL to be verified during implementation.
- Yahoo `query2.finance.yahoo.com/v7/finance/options` — **rejected** (HTTP 401).
- Index symbols in the Cboe feed use a leading underscore (`_VIX`, `_SPX`).
- **Open risk:** cloud sandbox reachability of `cdn.cboe.com` is unverified.
  Mitigated by a one-off manual cloud trial run before enabling the schedule;
  fallback is WebSearch-only degraded mode (manage/close existing positions,
  open nothing new, say so in the push notification).
- Upgrade path (not built now): paid API (Tradier / Polygon / MarketData.app)
  behind the same script interface if Cboe proves limiting.

## Files

| Path | Purpose |
|---|---|
| `options/investor-profile.md` | Fictional persona "Lt. Cmdr. Data — Probabilistic Learner" + every rule below. Single source of truth for rules. |
| `options/options-portfolio.md` | Header (NAV, cash, collateral reserved, capital at risk, net Greeks, cycle #), Open Positions, Closed Positions (realized P&L), NAV History (append-only), Daily Decision Log (reverse-chronological). |
| `options/learning-ledger.md` | Concept Index at top (term → first-explained entry) + one entry per decision. |
| `options/RESOURCES.md` | Papers, official education, books — every item sourced and link-verified with date. |
| `options/data/iv-history.csv` | `date,symbol,atm_iv_30d,underlying_price` — appended daily; drives IV rank. |
| `options/DECISION.md` | Deferred known simplifications for this portfolio. |
| `scripts/options_data.py` | Fetch, filter, compute, mark-to-market (CLI, JSON out). |
| `tests/test_options_data.py` + `tests/fixtures/` | Unit tests against a saved Cboe fixture. |
| `~/.claude/skills/hm-options-portfolio/SKILL.md` | Skill for manual runs; mirrors routine prompt. |
| Cloud routine `options-portfolio-daily` | `0 16 * * 1-5` UTC (9am PT / 12pm ET). |

## Investor profile rules

**Capital:** $50,000 inception, cash earns SGOV-equivalent ~4-5%/yr on
unreserved cash.

**Allowed strategies:** long call/put, debit vertical, credit vertical, iron
condor, long butterfly, calendar/diagonal (long back month), cash-secured put,
covered call (only on shares acquired via put assignment). Never: naked short
calls or puts, ratio spreads with a naked leg, undefined-risk strangles/straddles
short.

**Sizing:**
- Max loss per position ≤ 3% NAV (~$1,500 at inception).
- Sum of max losses across open positions ≤ 25% NAV.
- ≤ 2 open positions per underlying; ≤ 5 new positions per calendar week.
- Cash-secured put collateral (strike × 100) ≤ 20% NAV per position → only
  underlyings priced ≤ ~$100.
- Earnings: no short premium held through an earnings date, except a deliberate
  "IV-crush lesson" trade sized ≤ 1% NAV max loss, labeled as such.

**Entry filters:**
- 30-60 DTE at entry (calendars: front 20-40, back 50-90).
- Short strikes ~0.16-0.30 |delta|.
- Liquidity: open interest ≥ 500 on every leg; bid-ask ≤ 10% of mid
  (ETFs: or ≤ $0.05 absolute).

**Regime → strategy mapping (guidance, not mechanical):**
- IV rank high (≥ 50) → premium selling (credit spreads, iron condors, CSPs).
- IV rank low (≤ 25) → premium buying (debit spreads, calendars, long options).
- Between → directional debit/credit verticals per trend.
- VIX > VIX3M (backwardation) → stress regime: halve new-position size, no new
  short-premium on single names.

**Management rules:**
- Credit trades: take profit at 50% of max profit; stop at loss = 2× credit received.
- Debit / long-premium trades: take profit at 50-100% gain (state target at
  entry); stop at 50% loss of debit.
- Close or roll anything at 21 DTE.
- Short leg ITM at expiration → simulate assignment (CSP → shares, then covered
  calls allowed; spreads → close at intrinsic).

**Fill model:** buy at mid + 25% of (ask − bid); sell at mid − 25% of (ask − bid);
$0.65 per contract commission. Marks use mid.

**Benchmarks:** Cboe BXM (S&P 500 BuyWrite) and Cboe PUT (S&P 500 PutWrite)
index levels, plus cash. Reported in portfolio header and quarterly.

## `scripts/options_data.py` interface

Subcommands, all emit JSON to stdout (so the routine and the learner can both run them):

- `regime` → VIX, VIX3M, term-structure flag, VIX 1-yr percentile.
- `scan --symbols SPY,QQQ,... --dte 30-60` → per symbol: price, ATM 30-day IV,
  IV rank (from iv-history.csv; `null` + note if < 20 observations), expected
  move (price × IV × √(DTE/365)), filtered liquid contracts near target deltas.
- `price-spread --legs '<json>'` → fill-model entry price, max profit, max loss,
  breakevens, approximate probability of profit (from short-leg delta / BS),
  net Greeks, ASCII payoff diagram.
- `mark --positions options/options-portfolio.md` (or JSON) → per position mid
  mark, P&L, DTE, % of max profit, rule triggers (50% profit, 2× stop, 21 DTE,
  ITM at expiry).
- `record-iv --symbols ...` → appends today's ATM 30-day IV rows to iv-history.csv
  (idempotent per date/symbol).

Black-Scholes helper implemented in-script for payoff/PoP and a sanity check
against Cboe's published Greeks (tolerance test only; Cboe values are the ones used).

## Daily cycle (routine prompt outline)

0. Locate repo, `date`, NYSE holiday/weekend check (same list as stock routine),
   same-day guard (NAV History row for today → exit silently).
1. Read `options/investor-profile.md`, `options/options-portfolio.md`,
   `options/learning-ledger.md` Concept Index.
2. `python3 scripts/options_data.py regime` and `record-iv`.
3. `mark` open positions → apply management rules first (closes/rolls/assignment).
4. `scan` universe → regime read → candidate trades → `price-spread` each →
   enforce sizing/liquidity/earnings rules → open or pass.
5. Write portfolio file (header, tables, NAV row, decision log) and one ledger
   entry per decision (including "pass — no trade" with reason).
6. `git pull --rebase`, commit (`Signed-off-by: hmadhani2024@gmail.com`, no
   Co-Authored-By), push to main.
7. PushNotification: NAV, return vs BXM/PUT, trades opened/closed, new concepts
   introduced today.

If the Cboe feed is unreachable → degraded mode (see Data source).

## Learning ledger entry format

```
### YYYY-MM-DD — <OPEN|ADJUST|CLOSE|PASS> <symbol> <strategy> (Cycle #N)
**Decision:** one sentence.
**Market context:** plain-language regime read + numbers (IV rank, expected move, trend).
**Why this strategy:** chosen vs. 1-2 rejected alternatives and why.
**The trade:** legs table (action, qty, type, strike, expiry, fill), max profit,
  max loss, breakeven(s), probability of profit, ASCII payoff diagram.
**Greeks in dollars:** what delta/theta/vega mean for THIS position today.
**Concept spotlight:** 1-2 new terms explained from zero (first use only; add
  to Concept Index).
**What would prove this wrong:** invalidation conditions.
**Reproduce:** exact `options_data.py` command.
```

CLOSE entries add: outcome, P&L attribution (price move / time decay / vol
change), lesson, and an empty `**Your reflection:**` section — never filled by
the model.

## RESOURCES.md

Sections: foundational pricing papers (Black-Scholes 1973, Merton 1973,
Cox-Ross-Rubinstein 1979, Heston 1993); evidence on option returns and the
volatility risk premium (Coval & Shumway 2001, Bakshi & Kapadia 2003,
Carr & Wu 2009, Goyal & Saretto 2009); option-writing index research
(Whaley 2002 on BXM, Cboe PUT/BXM studies, Israelov & Nielsen / AQR on covered
calls); official education (OCC "Characteristics and Risks of Standardized
Options", Options Industry Council, Cboe Options Institute, CME Group);
books (Natenberg, Hull, Sinclair) as citation + short original summary only —
no copied text. Every link fetched and marked `verified YYYY-MM-DD`; anything
unverifiable is omitted, not guessed.

## Testing

- Unit tests (pytest) on a saved Cboe SPY fixture: chain filtering, fill model,
  vertical/condor/butterfly max P&L + breakevens, expected move, IV rank math,
  idempotent record-iv, mark rule triggers.
- BS Greeks within tolerance of Cboe values on fixture contracts.
- One-off manual cloud run before enabling the schedule (confirms Cboe
  reachability from the sandbox and end-to-end write/commit/push).

## Out of scope (→ options/DECISION.md)

Historical backtesting; real IV history before inception; intraday management;
early-assignment modeling beyond expiry-ITM; paid data APIs; portfolio-margin
simulation; tax treatment.
