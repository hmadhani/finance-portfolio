# Finance Portfolio (Cloud, Isolated) — Model Portfolio Tracker

Market-data-only, no personal financial context. This is an isolated experiment;
it does not read or reference any personal financial data, account files, or
external personal tracking systems. See `investor-profile.md` for the sizing
rules, glide path, and theme-concentration limits governing this loop.

- **Inception date:** 2026-08-26
- **Starting balance:** $100,000
- **Benchmark:** SPY

---

```
IMPORTANT: This is a paper/model portfolio for evaluation purposes only, tracked with
public market data alone (no personal financial context). It does not constitute
investment advice or a recommendation to buy or sell any security. All investments involve
risk, including potential loss of principal. Always consult with qualified financial
professionals before making investment decisions.
```

## Header (as of 2026-09-15)

| Metric | Value |
|---|---|
| NAV | $98,903.82 |
| Total return | -1.10% (since inception) |
| Blended Benchmark (ref) | not yet tracked — see note below |
| SPY (ref) | $760.88 (-0.68% since inception) |
| Cash balance | $11,040.18 (11.16% of NAV) |
| Stock sleeve | $64,667.22 (65.38% of NAV) |
| Sector ETF sleeve | $15,242.42 (15.41% of NAV) |
| Bond sleeve | $7,954.00 (8.04% of NAV) |
| Cycle # | 7 |
| Glide-Path Phase | Accumulation |

`Cycle #` counts routine cycles that have written this file (one entry per
NAV History row below), independent of wall-clock cadence changes.

**Blended Benchmark note:** `investor-profile.md` defines the 70% ACWI / 13%
AGG / 7% GLD / 10% cash blended benchmark. This cycle made another dedicated
attempt to backfill the 2026-08-26 inception-date closes for ACWI/AGG/GLD
and got closer than any prior cycle but still not a confirmed exact-date
close: direct-fetch access to every major historical-data provider (Yahoo
Finance, stockanalysis.com, MarketWatch, Stooq, ishares.com,
spdrgoldshares.com, SEC EDGAR, Finviz, TipRanks, Wikipedia, etc.) remains
blocked by this session's network-egress policy. The best bracketing data
found this cycle: ACWI closed $161.09 on 2026-08-27 (one day after
inception, in a range-bound market week — S&P 500 closed +0.3% on
2026-08-26 itself); AGG traded ~$97.82 on 2026-08-19 (one week before
inception); spot gold closed/traded ~$4,593-4,621/oz on 2026-08-26 itself
per market-recap sourcing, which cross-checked against today's
spot-to-GLD ratio (~0.914) implies a derived (not sourced) GLD close near
$420-422 that day. None of these is an actual confirmed 2026-08-26 closing
print for the ETF itself, so NAV History continues to carry "—" for this
column until an exact print can be sourced (e.g. via a paid data API or a
manual brokerage historical-data pull) — the bracket data above is logged
for a future cycle to use if it decides an approximation is preferable to
continuing the gap. Today's current-day reference prices: ACWI $161.67
(2026-09-15), AGG $97.00 (2026-09-15), GLD ~$403 (2026-09-15, sources
ranged $396-407 intraday). SPY is tracked as the secondary reference per
the profile.

This is Cycle #7, a **LIGHT** cycle (Tuesday, the second trading day of
this calendar week — Cycle #6 already covered Monday's HEAVY slot). All 15
holdings got the lightweight reaffirm/exit-only check (major news + Exit
Criteria scan only, no full fundamentals/technicals/analyst-consensus
pass) — see Trade Log. No Exit Criteria were triggered on any position;
all 15 reaffirmed HOLD. No new positions were opened (LIGHT cycles never
open new positions per the routine's rules) and no trims were needed —
the Theme Exposure table was recomputed from today's prices and every
theme, position, and sector-ETF sleeve remained inside its cap (AI-Capex
came closest at 24.76% of NAV, still under the 25% cap). Cash accrued 1
day of SGOV-equivalent interest since the last cycle (2026-09-14).

---

## NAV History

Appended every cycle (heavy or light) — source of truth for the Quarterly/
Annual Report's Return Trend chart. `Blended Benchmark` is the 70/13/7/10
ACWI/AGG/GLD/cash mix defined in `investor-profile.md`; left as "—" for
cycles before that benchmark was tracked.

| Date | Cycle # | NAV | Blended Benchmark | SPY (ref) |
|---|---|---|---|---|
| 2026-08-26 | 1 | $100,000.00 | — | $766.08 |
| 2026-09-05 | 2 | $100,000.00 | — | $766.08 |
| 2026-09-05 | 3 | $100,031.19 | — | $770.19 |
| 2026-09-08 | 4 | $99,001.13 | — | $770.19 |
| 2026-09-11 | 5 | $98,412.97 | — | $757.54 |
| 2026-09-14 | 6 | $98,526.03 | — | $764.29 |
| 2026-09-15 | 7 | $98,903.82 | — | $760.88 |

---

## Holdings

| Ticker | Type | Theme | Shares | Entry Price | Cost Basis | Current Price | Mkt Value | % NAV | Unrealized G/L |
|---|---|---|---|---|---|---|---|---|---|
| AVGO | Stock | AI-Capex | 14 | $357.56 | $5,005.84 | $366.70 | $5,133.80 | 5.19% | +$127.96 (+2.56%) |
| ETN | Stock | Energy-Transition | 12 | $412.97 | $4,955.64 | $396.07 | $4,752.84 | 4.81% | -$202.80 (-4.09%) |
| COF | Stock | Financials | 35 | $217.40 | $7,609.08 | $219.60 | $7,686.00 | 7.77% | +$76.92 (+1.01%) |
| LLY | Stock | Healthcare-GLP1 | 6 | $1,182.09 | $7,092.52 | $1,154.25 | $6,925.50 | 7.00% | -$167.02 (-2.35%) |
| TJX | Stock | Consumer-Defensive | 35 | $139.48 | $4,881.80 | $126.22 | $4,417.70 | 4.47% | -$464.10 (-9.51%) |
| GOOGL | Stock | AI-Capex | 14 | $341.95 | $4,787.30 | $340.65 | $4,769.10 | 4.82% | -$18.20 (-0.38%) |
| BALL | Stock | Materials | 106 | $60.97 | $6,462.80 | $62.49 | $6,623.94 | 6.70% | +$161.14 (+2.49%) |
| PEP | Stock | Consumer-Defensive | 35 | $142.27 | $4,979.45 | $136.46 | $4,776.10 | 4.83% | -$203.35 (-4.08%) |
| NEE | Stock | AI-Capex | 59 | $84.29 | $4,973.11 | $82.13 | $4,845.67 | 4.90% | -$127.44 (-2.56%) |
| MU | Stock | AI-Capex | 5 | $930.25 | $4,651.25 | $960.00 | $4,800.00 | 4.85% | +$148.75 (+3.20%) |
| BHRB | Stock | Financials | 69 | $70.63 | $4,873.47 | $73.80 | $5,092.20 | 5.15% | +$218.73 (+4.49%) |
| IMAX | Stock | Communication-Services | 93 | $52.50 | $4,882.50 | $52.09 | $4,844.37 | 4.90% | -$38.13 (-0.78%) |
| XLK | Sector ETF | AI-Capex | 26 | $186.00 | $4,836.00 | $190.13 | $4,943.38 | 5.00% | +$107.38 (+2.22%) |
| XLI | Sector ETF | Energy-Transition | 59 | $185.96 | $10,971.64 | $174.56 | $10,299.04 | 10.41% | -$672.60 (-6.13%) |
| AGG | Bond | Diversified-Core | 82 | $97.90 | $8,027.80 | $97.00 | $7,954.00 | 8.04% | -$73.80 (-0.92%) |
| Cash | — | — | — | — | $11,040.18 | — | $11,040.18 | 11.16% | — |
| **TOTAL** | — | — | — | — | **$100,030.38** | — | **$98,903.82** | **100.00%** | **-$1,126.56 (-1.27% on positions)** |

---

## Theme Exposure

| Theme | Positions | Mkt Value | % NAV |
|---|---|---|---|
| AI-Capex | AVGO, GOOGL, NEE, MU, XLK | $24,491.95 | 24.76% |
| Financials | COF, BHRB | $12,778.20 | 12.92% |
| Healthcare-GLP1 | LLY | $6,925.50 | 7.00% |
| Consumer-Defensive | TJX, PEP | $9,193.80 | 9.30% |
| Energy-Transition | ETN, XLI | $15,051.88 | 15.22% |
| Materials | BALL | $6,623.94 | 6.70% |
| Communication-Services | IMAX | $4,844.37 | 4.90% |
| Diversified-Core | AGG | $7,954.00 | 8.04% |

(Cash is intentionally excluded from theme exposure — it carries no thematic risk.)

---

## Trade Log (reverse-chronological)

### 2026-09-15 — Cycle #7 (LIGHT): reaffirm pass, no trades

LIGHT cycle: lightweight reaffirm/exit-only check on all 15 holdings (major
news + Exit Criteria scan only, no full fundamentals/technicals pass). No
Exit Criteria triggered on any position. Theme Exposure and sleeve weights
recomputed from today's prices; everything remained inside its cap
(AI-Capex closest at 24.76% of NAV, under the 25% cap; XLI closest of the
sector ETFs at 10.41%, under its 15% cap; no stock above ~7.8% of NAV,
under the 10% cap). Cash at 11.16% of NAV, above the 10% floor. No new
positions opened (LIGHT cycles never open new positions).

**AVGO — Broadcom (HOLD, reaffirmed — no action).** Theme: AI-Capex. Shares
fell ~4.8% Monday (2026-09-14) on a sector-wide debate among tech
executives over the pace of AI development, plus continued digestion of
Broadcom's own fiscal Q3 print (beats on revenue/custom-AI-ASIC growth,
but margin mix pressured by the AI-ASIC/networking shift); shares partly
recovered today. Broader semiconductor sector (NVDA, MRVL, AMD, QCOM) sold
off in sympathy — not an AVGO-specific thesis break. No insider-selling or
exit-criteria flags found. Screened against AI-Capex, the portfolio's
current hottest theme by relative strength (manual DECISION.md item 3
stopgap) — already near its 25% cap, so no add considered today regardless.

**ETN — Eaton Corporation (HOLD, reaffirmed — no action).** Theme:
Energy-Transition. Stock pulled back from last week's levels alongside a
broader industrials/rate-sensitive-sector wobble, despite continued
positive analyst activity (UBS upgraded to Buy on 2026-09-07, Bernstein
reiterated Buy on 2026-09-02) and company news unrelated to the core
data-center-power thesis (a new Autodesk data-sharing tie-up, a $242M
Arkansas manufacturing expansion). No guidance cut, no backlog reversal —
the stated stop condition was not triggered.

**COF — Capital One Financial (HOLD, reaffirmed — no action).** Theme:
Financials. Discover integration remains on track (14 of 24 planned
months in, debit-network conversion complete, synergy run-rate capture
underway toward the $2.7B by-2027 target); no credit-quality deterioration
or integration setback reported this week. Thesis intact.

**LLY — Eli Lilly (HOLD, reaffirmed — no action).** Theme: Healthcare-GLP1.
GLP-1 franchise demand remains strong (Q2 revenue +48% YoY, FY2026
guidance raised to $85-87B); incretin pipeline (orforglipron, retatrutide)
and a new women's-health push (AtaiBeckley acquisition closed) reinforce
rather than break the thesis. Stock remains well off its highs on
sector-wide GLP-1 valuation reset, not a company-specific deterioration.

**TJX — The TJX Companies (HOLD, reaffirmed — no action).** Theme:
Consumer-Defensive. Remains near 52-week lows following the
mid-August guidance-related selloff (EPS beat, but cautious guidance
triggered a Jefferies downgrade on Marmaxx-segment concerns); no new
incremental deterioration this week beyond the already-priced-in move.
Down ~9.5% unrealized — watched, but the exit criteria (thesis broken, 2
consecutive quarters of fundamental deterioration) are not yet met on a
single guidance-driven pullback.

**GOOGL — Alphabet (HOLD, reaffirmed — no action).** Theme: AI-Capex.
Continued AI-infrastructure investment (a new $15B European data-center
commitment announced 2026-09-09) and Waymo's European robotaxi expansion
plan support the thesis; an ongoing FTC inquiry into YouTube consumer-
protection practices is a watch item, not yet a thesis-breaking event.

**BALL — Ball Corporation (HOLD, reaffirmed — no action).** Theme:
Materials. New India manufacturing investment (Uttar Pradesh facility,
operational 2029) and two new board appointments this month; a routine
$0.20/share dividend was declared and paid today. No deterioration
flagged; UBS remains Neutral (not a Sell) on valuation, not thesis.

**PEP — PepsiCo (HOLD, reaffirmed — no action).** Theme:
Consumer-Defensive. No new news this week beyond routine IR
scheduling (Q3 results set for 2026-10-08) and a media-account shift to
Publicis; international strength continues to offset North American
softness per the last earnings call. Thesis intact.

**NEE — NextEra Energy (HOLD, reaffirmed — no action).** Theme: AI-Capex.
Company reaffirmed 2026 EPS guidance ($3.92-$4.02, targeting the high end)
and the Dominion combination timeline (close expected 2H 2027) this week;
no regulatory setback reported. Stop condition not triggered.

**MU — Micron Technology (HOLD, reaffirmed — no action).** Theme:
AI-Capex. Shares softened intraday/after-hours on sector-wide
semiconductor-tariff uncertainty and pre-earnings positioning ahead of the
2026-09-30 fiscal Q4 report — not company-specific; Deutsche Bank
reiterated a Buy rating and raised its price target this week. HBM
demand/supply thesis unchanged. No exit criteria triggered.

**BHRB — Burke & Herbert Financial (HOLD, reaffirmed — no action).**
Theme: Financials. No new news since the July 2026 Q2 print (LINKBANCORP
merger integration, ~$11.0B combined assets); shares continue to trade
constructively. No red flags found.

**IMAX — IMAX Corporation (HOLD, reaffirmed — no action).** Theme:
Communication-Services. Record summer box office ($728M, +73% YoY) led by
"The Odyssey" (extended in IMAX through September 30); Q3 already past
$600M in IMAX box office receipts, full-year 2026 guided to $1.4B. Thesis
strengthening, no exit criteria triggered.

**XLK — Technology Select Sector SPDR (HOLD, reaffirmed — no action).**
Theme: AI-Capex, passive sleeve pick — not individually re-picked, only
rebalanced on drift from target/theme caps. No rebalance needed today.

**XLI — Industrial Select Sector SPDR (HOLD, reaffirmed — no action).**
Theme: Energy-Transition, passive sleeve pick. Pulled back with the
broader industrials complex this week; remains the largest single sleeve
at 10.41% of NAV, still under its 15% ETF cap. No rebalance needed today.

**AGG — iShares Core U.S. Aggregate Bond ETF (HOLD, reaffirmed — no
action).** Passive core bond sleeve, rebalanced only on drift from the 8%
target. Currently 8.04% of NAV — no rebalance needed today.

**Cash** accrued ~1 day of SGOV-equivalent interest (~$1.36) since the
last cycle (2026-09-14).

### 2026-09-14 — Cycle #6 (HEAVY): full research pass, 3 adds (COF, LLY, BALL), theme-cap trim

On-schedule HEAVY cycle (Monday, first trading day of the week — no
holiday shift this week). Full fundamentals/valuation/technicals/catalyst/
insider/analyst-consensus research pass run on all 15 held positions;
baseline screener + sector-rotation scan also run for new candidates since
the portfolio remained under its 15-20 stock target (12 stocks) with cash
well above the 10% floor (17.5% before this cycle's trades).

**AVGO — reaffirmed, HOLD.** FQ3 FY26 (reported early Sept) beat again
(revenue $29.59B, adjusted EPS $3.32 vs $3.24 est), AI-semiconductor
revenue +221% YoY to $16.7B with FY26 AI-revenue guidance raised to $58B
(from $56B) and a multi-year path to $115B (FY27) then $230B (FY28) —
thesis intact and strengthening. Stock is down ~20% from its June
all-time high on a "guide not aggressive enough for a priced-for-
perfection stock" reaction rather than a fundamental miss; technicals have
turned near-term bearish (RSI ~36, negative MACD) after the pullback.
Insider selling remains broad (CEO, chairman, and CLO all sold this
period) but each individual's sales are well under 10% of their remaining
stakes — not a red-flag breach. Short interest low (~1.1-1.2% of float).
Analyst consensus remains Strong Buy, targets clustering $500-533. Theme:
AI-Capex, at the 25% cap (see theme-cap check below) — no room to add
regardless of the dip; a "hot"-theme name transitioning from chased to
digesting.

**ETN — reaffirmed, HOLD.** Record Q2 results and raised FY26 guidance
(EPS $13.40-13.60, organic growth 11-13%) remain unchanged from last
cycle's read; UBS's 9/8 upgrade to Buy/$515 continues to look directionally
right, but short interest has kept climbing since (+13% per the 8/31 FINRA
settlement, then reportedly +18% in a single day around 9/10, now ~1.9% of
float and rising fast off a low base) even as multiple executives
(COO, SVP/Controller, another SVP) sold in the $440-452 range — above
today's ~$421 working price. Q3 earnings not until ~Nov 3, a >45-day gap
with no company-specific near-term catalyst. Theme: Energy-Transition,
still a "hot," flow-favored theme (see XLI note) — this argues against
chasing ETN higher here even though the fundamental case remains strong;
reassess as an ADD candidate on a further pullback rather than at the
current post-upgrade level.

**COF — ADD (12 sh @ $218.25, +$2,619.00; 23 -> 35 sh, new avg entry
$217.40, now 7.75% NAV).** Discover integration is running ahead of the
"~50% of originations" checkpoint flagged last cycle — Capital One has
started migrating Discover cards onto its own back-office systems and is
testing Capital One-branded cards on the Discover network, with the
combined entity now the largest U.S. credit-card issuer by purchase
volume (+26% YoY). Q2 adjusted EPS $5.81 beat $4.69 consensus; credit
quality continues improving. Valuation is in-line with the sector (~13x
vs ~13.4x) and well below COF's own 10-year average (~18.2x) despite the
operational momentum — not a stretched entry. Insider selling is small
and scheduled (10b5-1 plan), short interest unremarkable (~1.8% of
shares). Financials/XLF flows are moderate and recently resumed
(+$2.51B trailing month after an August wobble) rather than an extreme,
crowded chase, and the theme sits at only 12.70% NAV post-add versus the
25% cap — ample room without concentrating. Some RSI readings suggest a
short-term overbought condition, which argues for sizing this as a
meaningful but not maximal add (bringing COF to 7.75% NAV, still well
under the 10% single-stock cap) rather than a full top-up, leaving room
to average in further around the Oct 22 earnings print if warranted.

**LLY — ADD (2 sh @ $1,116.00, +$2,232.00; 4 -> 6 sh, new avg entry
$1,182.09, now 6.80% NAV).** The product story has materially strengthened
since last cycle: orforglipron (branded Foundayo) has since been
FDA-approved as a once-daily oral GLP-1 for obesity/overweight-with-
comorbidities, directly reversing the ATTAIN-1 trial disappointment that
had been the backdrop for the CEO Ricks insider purchase flagged in
earlier cycles — that purchase should now be understood as a ~13-month-old
data point (Aug 2025) rather than a fresh signal, and no new 2026 insider
buying was found, so this cycle retires that specific data point from the
thesis even as the approval it once anticipated has since come through.
Foundayo/Zepbound now have expanded U.S. government-backed coverage, and a
Phase 3 readout showed orforglipron can maintain weight loss after
transitioning off injectable therapy, opening a maintenance-use case. Q2
revenue grew 48% YoY with FY26 guidance raised again; Q3 earnings
(confirmed Oct 29) now falls inside the 90-day catalyst window. A Novo
Nordisk advertising lawsuit (filed 7/21) is a manageable legal overhang,
not a thesis break. Valuation is rich vs. pharma peers (~32-37x vs ~25.6x)
but growth-justified against a decelerating Novo Nordisk. Healthcare/XLV
flows are described as only now beginning to return (5.9% YTD inflow
share vs tech's 7.3%) — an early-stage, not-yet-crowded rotation, the
opposite of chasing an already-hot theme, and Healthcare-GLP1 sits at just
6.80% NAV post-add versus the 25% cap, plenty of room.

**TJX — HOLD (hard decision point, resolved this cycle).** Nothing new and
decision-relevant has surfaced since 9/11: no new guidance, no new comp
data, no confirmed Q3 date, no fresh analyst moves beyond the already-known
Jefferies/Citi target cuts and the Barclays/Morgan Stanley Buy
reaffirmations. The stock is now confirmed trading below both its 50- and
200-day moving averages at the current $125.49 (a technical picture the
cached aggregator data hadn't caught up to last cycle), but this is a
continuation of the already-flagged move, not a new fact pattern. Under
this portfolio's named exit criteria — thesis broken outright, insider
selling >10% of holdings, two consecutive quarters of *confirmed*
fundamental deterioration, or a demonstrably better opportunity with no
room elsewhere — none is met: both of the last two reported quarters beat
on revenue and EPS with guidance raised both times; insider selling is a
mild, sell-only pattern but nowhere near a 10%-of-holdings trigger; short
interest is low (~1.1% of float) and falling, not elevated. Valuation has
become more attractive on the drop (now the cheapest of the big three
off-price names on P/E despite the best fundamental print of the three).
This is a decisive HOLD, not a punt: the Q3 FY27 print (expected
mid-to-late November, date still unconfirmed) remains the real second data
point — a confirmed Marmaxx miss there would satisfy the two-consecutive-
quarter deterioration bar and should trigger a hard SELL/TRIM
re-evaluation, while a beat/stabilization would argue for treating the
current price as a legitimate ADD opportunity given Consumer-Defensive's
thin 9.31% NAV weight. Theme: Consumer-Defensive, not a hot/flow-driven
theme right now.

**GOOGL — reaffirmed, HOLD.** Q2 revenue $119.8B (+24% YoY) with Google
Cloud accelerating to +82% YoY and cloud operating income more than
tripling; FY26 capex guidance raised to $195-205B. A favorable U.S.
ad-tech/AdX antitrust ruling in early September removed a major overhang
and helped snap the stock's longest monthly losing streak in over a
decade. Trailing P/E (~17.5x) and forward P/E (~16.4-16.9x) remain the
cheapest of the mega-cap AI-capex names, a genuine discount to the tech
sector (~29-34x) despite ~60% gross margins. Insider selling (Pichai) is
routine 10b5-1, short interest negligible (~0.6% of shares). This screens
as the best risk-adjusted name in the AI-Capex sleeve — GOOGL underperformed
for stretches of 2026 before the antitrust-relief rally, more of a
value re-rating than a chased-momentum story — but the theme is at its 25%
cap (see below), so no capital can be committed here regardless of
conviction; first in line to be reconsidered for an ADD if room opens via a
trim elsewhere. Theme: AI-Capex.

**BALL — ADD (25 sh @ $59.90, +$1,497.50; 81 -> 106 sh, new avg entry
$60.97, now 6.44% NAV).** Cleanest quarter of the group again: comparable
diluted EPS +14.4% YoY, global can shipments +4.3% YoY, South America
segment operating earnings +64% on mid-teens volume growth, FY26 guidance
unchanged (not cut) at 10%+ comparable EPS growth and $900M+ FCF. Trades at
~16x trailing/forward P/E — cheaper than Amcor (~32x), roughly in line
with Crown Holdings (~17x) — a reasonable multiple given the growth.
Analyst base is heavily Buy-skewed (70% Buy, zero Sell among 23 analysts),
average target $75.00 implying ~25% upside. The one soft spot — short
interest rose sequentially (+1.12M shares per the 8/31 FINRA settlement)
— is worth watching but not alarming in absolute terms. Materials is a
broadly "hot" sector this year (rotation into metals/commodity strength),
but BALL's own re-rating this quarter reads as company-specific execution
(South America strength, volume acceleration) rather than a pure sector-flow
chase, and Materials sits at just 6.44% NAV post-add versus the 25% cap —
sized modestly to preserve room for further adds if the confirmed Nov 3
Q3 print extends the trend. Theme: Materials.

**PEP — reaffirmed, HOLD (watch item, unresolved).** The margin-recovery
thesis still has not shown up in the numbers — North America beverage
volume still down 4% YoY, PBNA margins still compressing, the salty-snack
price-cut strategy (up to 15% off Lay's/Tostitos/Doritos/Cheetos since
February) has not yet reversed the volume decline, and FY guidance remains
only reaffirmed, not raised. Short interest is up ~30% (16.40M to 21.33M
shares), confirming last cycle's flag, though still a modest ~1.56% of
float in absolute terms. New this cycle: Barclays cut its price target to
$144 on 9/13, explicitly warning North American food momentum may be
fading — a fresh, negative data point directionally consistent with, not
contradictory to, the existing thesis. None of this yet meets the
portfolio's exit bar (not two confirmed deterioration quarters, no
10%-of-holdings insider selling, no thesis break — the staples/dividend-
aristocrat characteristics with a 4.3%+ yield remain intact). Q3 earnings
confirmed for Oct 8, 2026 remains the resolving catalyst exactly as
flagged last cycle: a second straight quarter of NA-volume decline with
guidance only reaffirmed (not raised) would satisfy the two-quarter
deterioration bar and should trigger a serious TRIM/SELL discussion next
cycle; NA-volume stabilization or a guidance raise would argue for holding
or adding, given Consumer-Defensive's 9.31% NAV weight leaves room. Theme:
Consumer-Defensive, not a hot/flow-driven theme.

**NEE — reaffirmed, HOLD (watch item).** Fundamentals remain on-track — FY26
adjusted EPS guidance reaffirmed at the high end ($3.92-4.02), backlog grew
to 35.1 GW, long-term 8%+ EPS CAGR guidance reiterated through 2035. The
$66.8B NextEra-Dominion merger cleared shareholder votes on 9/3 (99.47%
approval) but still needs state/federal regulatory clearance, targeted to
close H2 2027 — the named "regulatory setback" stop criterion has not been
triggered, only the ongoing (already-flagged) political/regulatory
scrutiny. Technicals remain bearish (price below both 50- and 200-day
moving averages, a "death cross" configuration per one source), but per
the portfolio's own rules price weakness alone is not a sell trigger absent
a confirmed fundamental or thesis break. NEE is notably not a "hot"-momentum
name within the AI-Capex sleeve — it has lagged AVGO/MU/GOOGL's runs — which
makes it a useful diversifier within the theme even though the theme
overall is at cap. No room to add regardless. Theme: AI-Capex.

**MU — reaffirmed, HOLD (highest-scrutiny watch item).** This is the
textbook "chasing a hot theme" profile the portfolio's rules are designed
to catch: FQ3 FY26 revenue hit a record $41.46B (+346% YoY) on a historic
memory-pricing supercycle, HBM sold out through 2027-28, but the stock's
parabolic run has compressed the forward P/E to ~5.8x — the market
explicitly pricing in a sharp reversion once the cycle peaks — short
interest is "near the highest levels in years" (~3.3% of float) with a
public high-profile short (Michael Burry, disclosed 7/2), and fiscal Q4
earnings land Sept 30 (16 days out), the single nearest and highest-stakes
catalyst in the book. None of the codified exit triggers are actually met
today — the thesis is intact and strengthening (not broken), there is no
confirmed fundamental deterioration (quite the opposite), and insider
selling is plan-based (10b5-1) rather than opportunistic dumping with no
evidence of exceeding 10% of any individual's holdings — so per the
portfolio's rule that price appreciation and hot-sector dynamics alone are
not sufficient grounds for a sale, MU is held through the Sept 30 print
rather than trimmed pre-emptively. This is, however, the single name in
the book most likely to generate a legitimate TRIM signal on short notice
(a guidance miss or confirmed margin/pricing deterioration) and gets the
tightest watch of any holding heading into that earnings call. Theme:
AI-Capex, at cap.

**BHRB — reaffirmed, HOLD (correction to the thesis framing).** Important
update since the 9/11 purchase: the LINKBANCORP merger this position was
bought on is not a pending deal — it already closed on May 1, 2026 (all
regulatory approvals landed 4/13/26), creating the ~$11.0B-asset combined
bank. The live question going forward is therefore integration execution
and cost-synergy realization, not deal-completion risk, and the position's
internal framing is recalibrated accordingly. Q2 2026 (reported 7/23) came
in as a genuine, if modest, miss on both metrics — adjusted EPS $2.03 vs
$2.10 consensus, revenue -4% vs consensus — the first of the two
consecutive quarters that would trip the fundamental-deterioration exit
trigger; one more disappointing print (plausibly reporting mid-to-late
October, date still unconfirmed) would meet that bar. Against that,
valuation remains cheap versus peers (~8-9x forward P/E vs ~11.7-12x peer
average, ~11% discount to book), insider activity is balanced (a director
bought ~$315K in the largest insider purchase of the trailing year, roughly
offsetting other insiders' smaller sales), and short interest is small in
absolute terms (~0.79% of float) despite a fast percentage rise off a tiny
base. Given the position is only three days old and the merger-integration
read is still a single data point, the right move is to hold as-is and
watch the next print closely rather than add into unconfirmed execution.
A confirmed live price for today could not be sourced (best available
figure remains the $70.63 entry/9-1 print) — flagged as a data gap.
Theme: Financials.

**IMAX — reaffirmed, HOLD (do not chase).** Fundamentals remain excellent —
clean Q2 beat across every metric, a record summer box office ($728M
Memorial Day-Labor Day on "The Odyssey"), and a dense forward release slate
(Dune: Part Three, Spider-Man: Brand New Day, an IMAX-exclusive Netflix
theatrical release) into a confirmed 2028 EBITDA-margin target above 50%.
But the stock is up ~46% YTD and several analyst targets — the $44.50
average, a $35 median-of-19, even Goldman's freshly-raised-but-still-
Neutral $50 (9/4) — now sit at or below the current ~$52.66 price, a sign
the market may already be pricing in a good chunk of the good news. A VP's
9/10 sale of 22,500 shares reduced that individual's own position by ~11%
— a mild yellow flag worth noting explicitly since it brushes the
portfolio's >10%-of-holdings language, though it does not represent
company-wide insider selling anywhere near that threshold and is not
treated as a trigger. Communication-Services' 2026 "heat" is concentrated
in mega-cap AI beneficiaries (Alphabet, Meta), not niche cinema-tech names,
so IMAX is not really riding sector-level inflows — its re-rating is fully
company-specific, and with the position already up sharply and several
targets suggesting full valuation, this is a hold-through-the-catalyst-
stretch (Q3 earnings ~Oct 22, unconfirmed, plus the H2 release slate) call
rather than an add-into-strength one. Theme: Communication-Services.

**XLK — reaffirmed, HOLD; trimmed 1 share for the theme-cap rebalance
(see below).** Technicals remain constructive (price above both 50- and
200-day moving averages, RSI ~61, aggregate "Strong Buy" signal), valuation
in line with its own history (~33x). Fund-flow data is genuinely
inconsistent across sources this cycle (a reported -$1.39B one-month
outflow alongside an $8.3B single-week inflow spike in the same window) —
read as real hot-money rotation churn rather than a clean directional
trend, consistent with 2026's broader pattern of tech-sector whipsaws.
Worth flagging for the record: XLK's top holdings (NVDA, AAPL, MSFT, AVGO,
MU) directly overlap two other AI-Capex positions in this book (AVGO, MU),
so the portfolio's true look-through single-name AI/semiconductor
concentration is somewhat higher than the headline 24.88% theme figure
implies — a reason to hold XLK as-is rather than add even if room existed,
and a data point worth weighing the next time theme capacity opens up.
The imminent 9/15-16 FOMC meeting is the dominant near-term macro catalyst
for the sleeve. Theme: AI-Capex.

**XLI — reaffirmed, HOLD.** Continues to see supportive flow data (+$345M
net inflows over the trailing month as of early August) and YTD
outperformance vs SPY, trading above both its 50- and 200-day moving
averages; RSI has cooled to a neutral ~35 (a pause after the strong run
rather than an overbought extreme) with a mild negative MACD reading
consistent with a short-term cooldown. Q3 industrial earnings season is
the next real catalyst, with GE Aerospace reporting Oct 20 (FY26 guidance
already raised, Q2 orders +17% to $16.5B — a bullish read-through for
XLI's aerospace/defense sleeve) and RTX's own Q3 commentary worth a
targeted follow-up closer to its report date. Flagged explicitly: Energy-
Transition/Industrials remains a "hot," flow-favored, premium-valued theme
— this argues against adding into strength at current levels even though
there is meaningful room (15.62% NAV post-cycle) before the 25% cap;
revisit sizing after October industrial earnings clarify whether the
current re-rating extends or cools. Theme: Energy-Transition.

**AGG — passive core bond sleeve, no action.** Not re-picked; price update
only (~$97.00, ~4.0% trailing yield). Currently 8.07% NAV, below its ~13%
target but not a hard-capped sleeve — no rebalance rule triggers a top-up
buy absent a specific instruction to do so. Theme: Diversified-Core
(non-thematic by definition).

**Theme-cap check (mandatory every cycle):** Recomputed the Theme Exposure
table from today's market values before any trades. Pure price
appreciation pushed AI-Capex (AVGO, GOOGL, NEE, MU, XLK) to $24,703.30,
25.07% NAV, fractionally over the 25% cap, with no independent Step-3
thesis-level reason to exit any of the five names (all five reaffirmed
HOLD above). AVGO ($5,067.86) and XLK ($5,067.09) were within $0.77 of
each other as the theme's largest positions — effectively tied given this
cycle's data-quality caveats on exact pricing — so consistent with the
precedent set in the two prior theme-cap trims, XLK (the diversified
sector-ETF position) was trimmed rather than the single-name AVGO holding,
to preserve full single-stock conviction exposure. Trimmed XLK from 27 sh
to 26 sh: sold 1 sh @ $187.67 = $187.67 proceeds routed to cash. AI-Capex
now $24,515.63 (24.88% NAV), back under the cap. No other theme,
per-position, or per-ETF cap was breached this cycle (Financials 12.70%,
Healthcare-GLP1 6.80%, Consumer-Defensive 9.31%, Energy-Transition 15.62%,
Materials 6.44%, Communication-Services 4.97%, Diversified-Core 8.07% — all
well clear of the 25% cap; largest single stock post-adds is COF at 7.75%
NAV, largest ETF sleeve is XLI at 10.50% NAV — both clear of their 10%/15%
caps).

**New candidates screened (Step 4, baseline filter + sector-rotation scan)
— zero cleared the bar this cycle.** Screened themes with room
(Financials, Healthcare-GLP1, Consumer-Defensive, Consumer-Discretionary,
Materials, Communication-Services); avoided AI-Capex entirely (at cap).
Sector-rotation context: money is currently rotating out of mega-cap
Tech/AI into Industrials, Energy, Materials, Consumer Staples, and
Utilities — Materials and Consumer Staples are themselves "hot" right now,
which raised the bar for anything found there to be genuinely idiosyncratic
rather than a rotation chase. Six names were fully vetted and rejected:
**CSTM** (Constellium, Materials) — high leverage (D/E ~1.7-2.1x) and very
low insider ownership (1.2%), thin industrial margins; the "obvious"
Materials-rotation name and it fails on fundamentals, not just crowding.
**DDI** (DoubleDown Interactive, would-be Communication-Services) — looked
clean on paper (6+/8 filters) but is the target of an active
controlling-shareholder going-private squeeze-out (DoubleU Games proposing
$11.25/ADS, contested by an activist as undervaluing the company); the
stock already trades above the offer, making it a merger-arb bet on deal
outcome rather than a fundamentals position — disqualified. **BFH** (Bread
Financial, Financials) — sub-10% revenue growth, sub-5% insider ownership,
trading near 52-week highs with a fresh Wells Fargo downgrade to Hold
(9/12) — looks like buying the top. **PAY** (Paymentus, would-be
Financials) — RSI 80.3, an explicit overbought disqualifier, rich
valuation, net insider selling. **ARX** (Accelerant Holdings, would-be
Financials) — strong growth and insider ownership but already under a
pending Thoma Bravo take-private at $20.25/share, capping upside near the
deal price; William Blair already downgraded post-announcement — same
structural issue as DDI. **RM** (Regional Management, Financials) —
genuinely attractive valuation (6.4x forward P/E, 0.77x P/B) with real
insider buying (new CEO bought 10,000 shares in the open market in August)
but fails the $500M market-cap floor (~$320M), carries meaningfully higher
leverage than the guideline (4.4x, albeit structurally normal for an
installment lender), and is trading near its 52-week low — the opposite of
top-30%-of-sector relative strength; flagged as a watch-list name to
re-screen if the downtrend stabilizes and market cap grows post-Q3 (~Nov
3). NVO (Novo Nordisk) was briefly considered but deprioritized without a
full scorecard — it is the single most obvious, widely-covered GLP-1
mega-cap turnaround trade in the market, the opposite of the idiosyncratic
pick this screen looks for, and its size leaves little room to hold it
meaningfully below the 10% cap while staying diversifying.

Stock sleeve moved from 12 to 12 positions (no count change) but grew from
58.9% to 65.28% of NAV via the three adds — running further above its
~50% target, flagged again for the next quarterly report's sleeve-drift
table rather than itself a trigger for action under the stated rebalance
rules (only per-position/per-ETF/per-theme caps are hard-enforced; sleeve
targets are not). Cash declined from 17.47% to 11.20% of NAV via the three
adds, landing close to the ~10% target/floor by design (the sizing table
sets cash's target equal to its floor) but still comfortably above the
hard 10% minimum. Cash rose by $6.36 from ~3 days of SGOV-equivalent
accrual (4.5%/yr assumed midpoint of the stated 4-5%/yr range, pro-rated
since the 2026-09-11 prior cycle) plus $187.67 in theme-cap trim proceeds,
before the three adds ($2,619.00 COF + $2,232.00 LLY + $1,497.50 BALL =
$6,348.50 total) were funded from it. Glide-Path Phase remains
Accumulation (19 days elapsed since the 2026-08-26 inception, far inside
the 0-7-year window).

**Price-data and methodology caveats:** Current prices for all 15
holdings, SPY, and the blended-benchmark reference tickers were sourced
via WebSearch/WebFetch per this routine's public-market-data-only
constraint; this session's network-egress policy continues to block direct
fetches of most major finance data sites (Yahoo Finance, MarketWatch,
stockanalysis.com, Finviz, WSJ, Stooq, TipRanks, SEC EDGAR, ishares.com,
spdrgoldshares.com), so all figures are WebSearch-snippet aggregates.
ETN and XLI prices in particular carried real ambiguity this cycle (ETN
between a $409.19 prior-close and a $425.26 intraday read; XLI between a
$175.27 dated close and a $181.80 unconfirmed live read) — the more
conservative, specifically-dated figure was used in each case ($421.00 and
$175.27 respectively) and is flagged here as approximate. BHRB's live
price could not be confirmed at all this cycle; its 9/11 entry price was
carried forward unchanged. NEE's most-recent-dated figure available was
from 9/3, several days stale relative to the other holdings. As in prior
cycles, individual technical-indicator (moving-average/RSI/MACD) readings
frequently conflicted across sources/snapshot dates for the same ticker,
in several cases clearly reflecting stale pre-rally or pre-selloff data
carried forward by aggregator caches; the most specifically-dated,
most-recent, and context-corroborated figure was used in each case, with
outliers called out inline above rather than silently used.

### 2026-09-11 — Cycle #5 (HEAVY): full research pass, 2 new positions (BHRB, IMAX)

Heavy cycle run Friday 2026-09-11 rather than Monday — this week's Monday
(2026-09-07) was Labor Day, the routine's own catch-up rule looked at this
week's Trade Log headings (Monday 9/7 through today) and found only Cycle
#4 (2026-09-08), tagged LIGHT rather than HEAVY, so today's cycle picks up
the missed HEAVY slot. Full fundamentals/valuation/technicals/catalyst/
insider/analyst-consensus research pass run on all 13 held positions;
baseline screener + sector-rotation scan also run for new candidates since
the portfolio remained well under its 15-20 stock target (10 stocks) with
cash well above the 10% floor (27.4% before this cycle's trades).

**AVGO — reaffirmed, HOLD.** Q3 FY26 (reported 9/2-9/4) beat on revenue
($29.59B, +86% YoY) and adjusted EPS ($3.32 vs $3.24 est), AI-semiconductor
revenue +221% YoY to $16.7B; forward P/E (~19x) is below the semiconductor
industry median despite the AI-networking/custom-silicon growth story
intact (6 named hyperscale custom-silicon customers). Watch items: adjusted
gross margin compressing (~75%, guided toward ~73% next quarter) as custom
silicon mixes up, and a soft Q4 revenue guide ($34.8B vs $35.03B consensus)
drove a post-earnings pullback. Insider selling remains persistent (51 of
52 trailing-90-day Form 4s were sales) but reads as routine 10b5-1/tax
activity against very large remaining insider stakes, not a concentrated
>10%-of-holdings cluster — exit criteria not triggered. Analyst consensus
remains ~84% buy, target range $506-533. Theme: AI-Capex, still the
portfolio's hottest theme (now 24.99% NAV, effectively at the 25% cap) —
flagged explicitly per the DECISION.md #3 stopgap; no further AI-Capex
buys are appropriate until the theme has room.

**ETN — reaffirmed, HOLD.** Record Q2 2026 results (sales $8.5B, +21% YoY;
adjusted EPS $3.15) with FY2026 guidance raised again (EPS $13.40-$13.60,
organic growth 11-13%); data-center order momentum continues (+85% YoY) and
UBS upgraded to Buy on 9/8 (target raised $450->$515), directly confirming
the grid-to-chip thesis. Watch item: valuation is rich (~68% above its own
10-year average P/E) and short interest jumped ~20% over the past week
immediately after the UBS-driven rally, suggesting some skepticism about
chasing it here — not an exit signal, but worth monitoring. Theme:
Energy-Transition, a theme still seeing real fund-flow support (XLI
+9-20% YTD depending on methodology) — a "hot" theme by the DECISION.md #3
stopgap standard, sized within its per-position cap.

**COF — reaffirmed, HOLD.** Q2 2026 beat (adjusted EPS $5.81 vs $4.85 est,
revenue $15.85B +4% QoQ) with credit quality improving (provision for
credit losses -27%, net charge-off rate down 22bps) and Discover
integration on track (50% of originations migrated). Valuation comparisons
are noisy post-acquisition (GAAP P/E swung from 38x to ~12x on deal
accounting) but normalized profitability is recovering. No insider-selling
cluster or credit-quality red flag found. Theme: Financials — not
previously a "hot" theme by flow data, though this cycle's screen found
sector-level rotation-in support (XLF, curve steepening); COF itself is
an idiosyncratic integration story, not a chase of that flow.

**LLY — reaffirmed, HOLD.** Q2 2026 revenue $23.0B (+48% YoY) driven by
Mounjaro/Zepbound ($14.9B combined, +$6.3B YoY); FY2026 guidance raised
again (revenue $85-87B, EPS $35.50-$36.50). GLP-1 franchise thesis fully
intact; CEO Ricks made an open-market purchase this period (~$1M+), a
mildly positive insider signal, not a red flag. Watch items: valuation
premium to sector remains large (~58-80% above healthcare/peer averages)
and ex-US GLP-1 pricing realization is down 36% even as volume is up
113%, a pricing-power watch item rather than a thesis break. Q3 earnings
confirmed 2026-10-29. Theme: Healthcare-GLP1 — a narrow, idiosyncratic
theme (not a broad "hot sector" chase; broader healthcare/XLV strength
this cycle is driven by names outside this theme's definition).

**TJX — reaffirmed, HOLD (full research pass, decision point).** This
position was explicitly flagged last cycle for a full research pass to
decide HOLD/SELL/TRIM, since it had fallen to a 52-week low. Since then it
has fallen further, to a fresh 52-week low of $125.49 intraday today (down
from $132.35 on 9/8, ~26% off its 52-week high), and picked up a batch of
sell-side price-target cuts since the last cycle (Jefferies to Hold/$145,
Citi to Neutral/$154, Gordon Haskett to Accumulate/$155, Guggenheim and
Wells Fargo also cutting targets). Against that, the fundamentals do not
confirm the stated exit criteria: Q2 FY27 (reported 8/19) beat on both
revenue (+5% YoY) and EPS ($1.36 vs $1.10 LY), and full-year guidance was
raised for the second consecutive quarter — the only soft data point is a
Q3 FY27 guide (comps +2-3%, EPS $1.30-$1.32) that came in below Street
hopes, and management attributes the Marmaxx comp deceleration to a
self-described "self-inflicted," fixable merchandise-mix execution issue
rather than a demand problem. Barclays and Morgan Stanley both reiterated
Buy this week despite the new low. Per the routine's named exit criteria
(thesis broken outright, or 2 consecutive quarters of *confirmed*
fundamental deterioration — not yet met, since both of the last two
quarters actually beat and guidance was raised both times), this does not
yet meet the bar for a rules-based exit; selling purely on price-momentum
and sentiment without a confirmed fundamental or thesis break would be a
reactive, undisciplined decision inconsistent with this portfolio's stated
philosophy of disciplined compounding over short-term reaction. HELD, with
the position re-flagged as a hard decision point for the next HEAVY cycle:
the Q3 FY27 print (expected mid-to-late November) is the report that will
either confirm the claimed Marmaxx recovery or convert the "soft guidance"
data point into the second quarter of confirmed deterioration the exit
criteria call for. Theme: Consumer-Defensive, not a hot/flow-driven theme
right now — this is a name-specific, not thematic, risk.

**GOOGL — reaffirmed, HOLD.** Q2 2026 revenue $119.8B (+24% YoY) with
Google Cloud accelerating to +82% YoY ($24.8B) and cloud operating income
more than tripling YoY; capex guidance raised to $195-205B on continued
AI-infrastructure buildout. Trailing P/E (~17x) remains the cheapest of
mega-cap tech peers. New near-term catalyst: the next phase of the U.S.
ad-tech antitrust trial is set for 2026-09-22 (within the 90-day window),
and an appeals-court ruling has cleared youth-addiction litigation to
proceed against major platforms including Google — incremental legal
overhang, not a thesis break. No insider-selling cluster; short interest
low (~0.6% of shares out). Theme: AI-Capex, at the theme cap alongside
AVGO/NEE/MU/XLK (see AVGO note above) — no room to add here even though
the fundamentals remain strong.

**BALL — reaffirmed, HOLD.** Cleanest quarter of the four consumer/
materials names: Q2 2026 revenue $3.99-4.00B (+20% YoY, well above the
~$3.68B estimate), comparable diluted EPS +14.4% YoY, global can shipments
accelerating (+4.3% YoY); FY2026 guidance (>10% comparable EPS growth,
>$900M FCF) reaffirmed. No insider-selling cluster (only routine small
VP-level option exercises); two new independent directors joined the
board 9/9, governance-neutral. Analyst consensus solidly Buy, average
target ~$72.57 (~16% upside from $62.49). Theme: Materials — XLB is
seeing real rotation-in this cycle (+17% YTD, breaking out on
copper/gold-silver strength), making this a "hot" theme by the DECISION.md
#3 stopgap standard, though BALL itself was entered well before this
flow picked up.

**PEP — reaffirmed, HOLD (watch item).** Q2 2026 revenue $24.18B (+6.4%
reported, beat) and core EPS $2.20 (narrow beat), but the stated
margin-recovery thesis has not yet shown up in the numbers this quarter
(gross margin -50-80bps YoY, core operating margin -40bps YoY) and North
America beverage volume fell 4%; FY2026 guidance was only reaffirmed, not
raised, in contrast to every other held name's guidance this cycle. Short
interest rose ~30% in the latest reporting period, though still a modest
~1.6% of shares out. No insider-selling cluster (routine executive/
director activity only). Not yet a confirmed exit trigger (revenue and
EPS both still beat, and only one quarter without margin improvement, not
the two consecutive quarters of deterioration the criteria call for), but
this is now the second-most-flagged watch item in the book after TJX,
worth resolving at the 2026-10-08 Q3 print. Theme: Consumer-Defensive, not
a hot/flow-driven theme.

**NEE — reaffirmed, HOLD (watch item, escalated).** Fundamentals remain
strong — FY2026 guidance reaffirmed at the high end ($3.92-4.02 adjusted
EPS), renewables/storage backlog grew to 35.1 GW, and FPL's large-load
data-center demand pipeline grew from 6 GW to 8 GW contracted with 12 GW
in advanced discussions, direct evidence for the AI-power thesis. However,
the named "stop" watch item has genuinely escalated since the last cycle:
Virginia's governor has now formally intervened as a party in the SCC's
Dominion Energy merger review, Arlington County's board also voted to
intervene, and the SCC took the unusual step of ordering three in-person
public hearings (Nov 5, 9, 10) — this is a broadening of political/
regulatory opposition, not yet the "regulatory setback" that is this
position's actual named stop criterion (a final SCC decision isn't
expected until January 2027, outside this cycle's 90-day catalyst window).
Technicals have also turned soft (price below both its 50- and 200-day
moving averages, with one source flagging a death cross). Per the named
exit criteria, this remains a HOLD — the stop is "a regulatory setback,"
not "regulatory scrutiny" — but it is now flagged as the most elevated
watch item in the book, to be reassessed immediately if the SCC process
produces an adverse procedural or preliminary ruling before the next
cycle. Theme: AI-Capex, at the theme cap (see AVGO note).

**MU — reaffirmed, HOLD (watch item).** HBM thesis remains intact: full
calendar-2026 HBM supply (including HBM4) is sold under signed contracts,
HBM4E targeted for CY2027 volume production, and forward valuation
(~10-11x, some estimates as low as ~6x FY2027 consensus) screens cheap
relative to AI-semiconductor peers. The single biggest near-term catalyst
in the entire book is MU's fiscal Q4 2026 earnings on 2026-09-30 — flagged
across coverage as potentially the most important 2026 catalyst for AI
memory stocks, and it falls right before the next scheduled cycle. Watch
items unchanged in direction but with new data this cycle: short interest
is "near the highest levels seen in years" (~3.3% of float) even as the
stock trades well below its June all-time high, and CXMT's global DRAM
share has now confirmed at 10% (up from <1% in 2023, now the #4 global
DRAM supplier), though one forecast expects CXMT's growth-momentum to
decelerate in 2027. No hyperscaler capex deceleration evidence found yet.
Not a thesis break. Theme: AI-Capex, at the theme cap (see AVGO note).

**XLK — reaffirmed, HOLD.** Technicals remain constructive (price above
both 50- and 200-day moving averages, RSI ~61, aggregated screens read
Strong Buy) and the broad AI-capex thesis is unchanged, but flow data is a
new watch item: technology-sector ETFs pulled in a record $19B in July
2026 then *lost* $6.1B in August even as the sector gained ~6% that month —
an early sign of profit-taking/rotation out of mega-cap tech, consistent
with 2026 flow data increasingly favoring industrials/healthcare/
financials. The 2026-09-15/16 FOMC meeting is the dominant near-term macro
catalyst for high-multiple tech names in this fund. Price data for this
ETF could not be refreshed past a 2026-09-04 snapshot this cycle (same
figure as last cycle) — flagged as a data-staleness caveat below. Theme:
AI-Capex, at the theme cap (see AVGO note).

**XLI — reaffirmed, HOLD.** Continues to be one of 2026's strongest-flow
sectors on a relative basis (YTD outperformance vs. SPY cited across
multiple sources, though exact magnitude varied by methodology), with the
fund's own narrative shifting toward being "the physical layer of the AI
buildout" (power, cooling, grid equipment) alongside its original
reshoring/defense angle — both directly consistent with the stated thesis.
Technical indicators (50/200-day moving averages, RSI) could not be
reliably pinned down this cycle; one figure found (200-DMA ~$156.68) is
inconsistent with the fund's current ~$174-176 price and strong YTD
performance and is flagged as likely stale rather than used. Q3 2026
industrial earnings (October) are the next catalyst, with GE Aerospace/RTX
order-book commentary as a tone-setter. Theme: Energy-Transition, a "hot"
theme by flow data this cycle (see ETN note).

**AGG — passive core bond sleeve, no action.** Not re-picked; rebalanced
only on drift from its ~13% target (currently 8.0% NAV, below target but
not a hard-capped sleeve — no rebalance rule triggers a top-up buy absent
a specific instruction to do so). Price update only. ~4.1% trailing yield.
Theme: Diversified-Core (non-thematic by definition).

**Theme-cap check (mandatory every cycle):** Recomputed the Theme Exposure
table from today's market values. AI-Capex (AVGO, GOOGL, NEE, MU, XLK) sits
at $24,594.22, 24.99% NAV — essentially at, but not over, the 25% cap; no
rebalance trigger this cycle, but no further AI-Capex buys are appropriate
until price movement or a trim creates room. No other theme, per-position,
or per-ETF cap was breached.

**New positions opened (Step 4, baseline screener + sector-rotation scan):**
Screened for candidates outside the AI-Capex theme (at cap) across the
themes with room (Financials, Healthcare-GLP1, Consumer-Defensive,
Energy-Transition, Materials, Consumer-Discretionary, Communication-
Services). Two names cleared the bar (>=6/8 baseline filters, a catalyst
within 90 days, RSI<70, no major insider-selling red flag); several others
(Palomar Holdings, Sociedad Química y Minera, Hims & Hers) were screened
and rejected on insider-ownership, leverage, or overbought-RSI grounds.

**BHRB — Burke & Herbert Financial Services Corp. (BUY, 69 sh @ $70.63,
$4,873.47, 4.95% NAV)**
A regional-bank M&A story: completed a $354M all-stock merger with
LINKBANCORP (May 2026), creating an ~$11.0B-asset bank. Passes 4 of 8
baseline filters cleanly (market cap ~$1.1-1.4B, trailing P/E ~8.8-11.4x,
insider ownership 10.9% with 34 insider buys and 0 sales trailing 12
months, trading near the top of its 52-week range) with 3 filters not
applicable to a depository bank's balance sheet (gross margin, D/E, FCF
yield have no clean equivalent for a bank) rather than failed. RSI ~43,
having cooled from a prior overbought reading rather than currently
extended. Catalyst: Q3 2026 earnings (likely mid-to-late October) should
show the first full quarter of LINKBANCORP integration synergies, with a
sector-wide NIM tailwind from yield-curve steepening (2s10s from -108bp to
+52bp). Analyst consensus Moderate Buy/Buy, targets $75-81. Theme:
Financials. Hot-theme note (DECISION.md #3 stopgap): this is a
sector-rotation-aligned pick — Financials/XLF is seeing genuine inflow
support this cycle from the curve-steepening tailwind — but the specific
name is a small, under-the-radar M&A story rather than a crowded mega-cap
bank trade, so it adds rotation exposure without chasing an already-hot
single name. Drawdown-survivability check: a small-cap regional bank
carries idiosyncratic/liquidity risk beyond a mega-cap bank; sized at
~5% NAV (well under the 10% cap) specifically to keep any single-name
shock absorbable without forced selling elsewhere in the book.

**IMAX — IMAX Corporation (BUY, 93 sh @ $52.50, $4,882.50, 4.96% NAV)**
Premium-cinema technology/licensing name, tied to box-office and system
installs rather than AI-infrastructure spend. Passes all 8 baseline
filters (market cap ~$2.8B; forward P/E ~22.4x; revenue +14.8% YoY TTM;
gross margin ~57.8% TTM; debt/equity ~0.6-0.9x; FCF yield ~3-4%
(borderline estimate, source figures for FCF varied); insider ownership
23.2%; 52-week relative strength +45%, a clear sector outperformer).
Technicals: price above both 50- and 200-day moving averages, RSI ~44
(cooled from an overbought ~70 reading in early August), trading ~5.5%
below its 52-week high rather than freshly extended. Catalyst: tracking
toward a record ~$1.4B global 2026 box office and 160-175 new system
installations for the year, with Q3 earnings (early November) as the next
confirming data point and Q4 seasonally the heaviest quarter for the
business. Analyst consensus Moderate Buy, consensus target ~$54.45
(Rosenblatt at $65). Theme: Communication-Services — a new theme for this
book (0% NAV before this buy). Hot-theme note (DECISION.md #3 stopgap):
explicitly a *company-specific* momentum name (+45% over 52 weeks) sitting
inside a *cold* sector at the ETF level (XLC saw net outflows, -$1.76B
trailing 3 months, -$2.81B trailing year) — this is the opposite of
chasing a hot sector rotation, and was selected specifically because it
diversifies the book into an unused theme rather than adding to an
already-crowded trade. Drawdown-survivability check: single-thesis
consumer/entertainment exposure tied to box-office cyclicality; sized at
~5% NAV, comfortably under the 10% cap.

No positions sold or trimmed this cycle. Stock sleeve moved from 10 to 12
positions (49.1% -> 58.9% of NAV, running above its ~50% target — flagged
for the next quarterly report's sleeve-drift table, not itself a trigger
for action under the routine's stated rebalance rules); cash declined from
27.4% to 17.5% of NAV, still well above the 10% floor. Cash rose by $9.96
from ~3 days of SGOV-equivalent accrual (4.5%/yr assumed midpoint of the
stated 4-5%/yr range, pro-rated since the 2026-09-08 prior cycle) before
the two new-position buys were funded from it. Glide-Path Phase remains
Accumulation (16 days elapsed since the 2026-08-26 inception, far inside
the 0-7-year window).

**Price-data and methodology caveats:** Current prices for all 15
holdings (13 prior + 2 new), SPY, and the blended-benchmark reference
tickers were sourced via WebSearch/WebFetch per this routine's
public-market-data-only constraint. This cycle's research agents reported
that direct WebFetch access to most major finance data sites (Yahoo
Finance, MarketWatch, stockanalysis.com, Finviz, WSJ, Stooq, ishares.com,
spdrgoldshares.com) was blocked by this environment's network-egress
policy, so all figures are WebSearch-snippet aggregates of those same
underlying sources rather than direct page reads — a new, session-level
data-access constraint worth flagging for future cycles. Individual price
and technical-indicator (moving-average/RSI/MACD) readings frequently
conflicted across sources/snapshot dates for the same ticker; the most
specifically-dated, most-recent, and context-corroborated figure was used
in each case, and outlier/stale-looking figures (e.g. XLI's 200-DMA, a
stale SPY figure carried in the last two NAV History rows that today's
research flagged as inconsistent with current index levels, XLK's
2026-09-04 price snapshot) are called out inline above rather than
silently used. NAV History is append-only per the routine's own rules, so
no prior row was altered; today's SPY reference reflects the best
currently-available figure rather than an attempt to reconcile the prior
rows.

### 2026-09-08 — Cycle #4 (LIGHT): reaffirm pass + theme-cap rebalance

Light cycle for the 2026-09-07 (Labor Day) slot, run 2026-09-08 — market-holiday
shift (this is the "Friday LIGHT" slot in the Mon-HEAVY/Wed-LIGHT/Fri-LIGHT
rotation, following Cycle #3). Lightweight reaffirm/exit-only check on all 13
holdings — no full fundamentals/technicals/analyst-consensus research pass
(heavy-cycle only), no new positions screened or opened.

**AVGO — reaffirmed, no action.** Price essentially flat (~$357.89). No news
surfaced since the last cycle that changes the AI-networking/custom-silicon
thesis; no exit criteria triggered.

**ETN — reaffirmed, no action.** Price flat (~$410.85). Data-center
power/cooling demand thesis unchanged; no exit criteria triggered.

**COF — reaffirmed, no action.** Price flat (~$219.60). No new
credit-quality or Discover-integration signal since the last cycle.

**LLY — reaffirmed, no action.** Down ~5.4% to $1,149.36 on broad market
softness (Dow/S&P/Nasdaq all lower today amid US-Canada trade-tension and
oil-price headlines) rather than any GLP-1-specific news; no guidance cut or
competitive-share-loss signal found. Thesis intact.

**TJX — reaffirmed, no action (watch item, escalated).** Continues to slide —
now around $132.35, a 52-week low near $131, down roughly 23% from its
52-week high. Drivers confirmed via search: soft Q3 guidance overshadowing
the Q2 beat, the previously-noted Jefferies downgrade on Marmaxx softness,
and analyst commentary that the stock's premium valuation (30-32x forward
earnings) leaves little margin of safety. This is real, not a data artifact —
multiple independent sources corroborate the 52-week-low level. Still,
Wall Street consensus remains Strong Buy (23 analysts, mean target $171.18),
Q2 itself beat on both revenue and EPS, and the named exit criteria (thesis
broken outright, or 2 consecutive quarters of confirmed fundamental
deterioration — only one quarter of soft *guidance* exists so far, not yet
realized deterioration) are not yet met. Held, flagged for a full research
pass at the next HEAVY cycle rather than an exit today.

**GOOGL — reaffirmed, no action.** Down ~2.1% to $331.35, in line with
today's broad mega-cap tech pullback (search-reported decliners include
Apple -2.55%, Alphabet -2.10%); no cloud-growth deceleration or ad-market
softness signal specific to Alphabet found.

**BALL — reaffirmed, no action.** Price flat (~$62.49). No new signal.

**PEP — reaffirmed, no action.** Price flat (~$137.63). No new signal;
earnings not due until Oct 8.

**NEE — reaffirmed, no action (watch item).** Roughly flat (~$83.00).
Dominion Energy merger review remains a named watch item (regulatory
scrutiny noted last cycle); no new setback confirmed this cycle.

**MU — reaffirmed, no action (watch item).** Up modestly to ~$1,014.91 on
continued semiconductor-sector strength; DRAM/China-competition and
Nvidia-order-visibility watch items unchanged, not yet a thesis break.

**Rebalance — theme cap (not a thesis exit):** Recomputed the Theme Exposure
table from current market values per Step 5 (mandatory every cycle, heavy or
light). Pure price movement since the last cycle pushed AI-Capex (AVGO,
GOOGL, NEE, MU, XLK) to ~25.12% NAV, fractionally over the 25% cap, with no
independent thesis-level reason to exit any of the five names. Trimmed XLK —
the largest position in the theme — from 28 sh to 27 sh: sold 1 sh @ $187.28
= $187.28 proceeds routed to cash. AI-Capex now $24,677.47 (24.93% NAV), back
under the cap. No other theme, per-position, or per-ETF cap was breached this
cycle.

No new positions opened (LIGHT cycle — Step 4 candidate screening is
heavy-cycle only). Cash rose from $26,742.13 to $26,939.30: $9.89 from ~3
days of SGOV-equivalent accrual (4.5%/yr assumed midpoint of the stated
4-5%/yr range, pro-rated since the 2026-09-05 prior cycle) plus $187.28 in
theme-cap trim proceeds. Glide-Path Phase remains Accumulation (13 days
elapsed since the 2026-08-26 inception, far inside the 0-7-year window).

**Price-data caveat:** current prices for all 13 holdings, SPY, and the
blended-benchmark reference tickers were sourced via WebSearch per this
routine's public-market-data-only constraint; several individual searches
returned inconsistent or stale-looking figures across repeated queries for
the same ticker (a known limitation of this data source noted by prior
cycles). Where results conflicted, the most specifically-dated and
context-corroborated figure was used (e.g. TJX and GOOGL prices were
cross-checked against dedicated news-search results before being accepted).

### 2026-09-05 — Cycle #3 (LIGHT): reaffirm pass + theme-cap rebalance

Off-schedule manual run on a Saturday (routine is scheduled Mon/Wed/Fri; an
off-schedule day defaults to a LIGHT cycle per the routine's own rules).
Lightweight reaffirm/exit-only check on all 13 holdings — no full
fundamentals/technicals/analyst-consensus research pass (heavy-cycle only),
no new positions screened or opened.

**AVGO — reaffirmed, no action.** Stock down modestly (~$357.90) after a
guidance-driven pullback; insiders continued routine selling but no signal
that it crosses the >10%-of-holdings exit threshold. AI-Capex thesis
(custom-silicon/networking demand) intact.

**ETN — reaffirmed, no action.** Data-center sales momentum continues
(+65% last quarter cited); no exit criteria triggered.

**COF — reaffirmed, no action.** Q2 beat already reflected; dividend
declared, analyst price target raised (Wolfe Research to $275). No
credit-quality deterioration signal.

**LLY — reaffirmed, no action.** Multiple positive Phase 3 readouts
(orforglipron, retatrutide) reinforce the GLP-1 thesis; no guidance cut or
competitive-share-loss signal.

**TJX — reaffirmed, no action.** Marmaxx softness / Jefferies downgrade
noted as a watch item, but comp-sales deceleration (the stated exit
criterion) not yet confirmed; Morgan Stanley maintains Overweight.

**GOOGL — reaffirmed, no action.** AI/cloud momentum positive (Gemini 3.8
release, bullish analyst commentary); no cloud-growth deceleration or
ad-market softness signal.

**BALL — reaffirmed, no action.** Mixed analyst sentiment but price targets
being raised (BofA to $73, JPMorgan upgrade to Overweight); no
volume-trend reversal signal.

**PEP — reaffirmed, no action.** Routine dividend declared; earnings not
due until Oct 8; no further volume deterioration signal beyond what was
already priced in.

**NEE — reaffirmed, no action (watch item).** Virginia Gov. Spanberger
said she will intervene in the Dominion Energy merger review — this is
regulatory scrutiny, not yet the "Dominion merger regulatory setback" named
as this position's stop criterion; watching closely on future cycles.

**MU — reaffirmed, no action (watch item).** Strong day on broad
semiconductor sentiment; DRAM share loss to China's CXMT and Nvidia
order-visibility limited to 2030 both noted as watch items, not yet a
thesis break (HBM 2026 supply still sold out).

**Rebalance — theme cap (not a thesis exit):** Recomputed the Theme
Exposure table from current market values per Step 5 (mandatory every
cycle, heavy or light). Pure price appreciation since the last cycle pushed
AI-Capex (AVGO, GOOGL, NEE, MU, XLK) to 25.35% NAV, over the 25% cap, with
no independent Step-3 thesis-level reason to exit any of the five names.
Trimmed XLK — the largest position in the theme — from 30 sh to 28 sh: sold
2 sh @ $185.93 = $371.86 proceeds routed to cash. AI-Capex now $24,981.64
(24.97% NAV), back under the cap. No other theme or per-position/per-ETF
cap was breached this cycle.

No new positions opened (LIGHT cycle — Step 4 candidate screening is
heavy-cycle only). Cash rose from $26,370.27 to $26,742.13 via the trim
proceeds; no SGOV-equivalent accrual booked, since the prior cycle (Cycle
#2) was dated the same calendar day (2026-09-05), leaving zero elapsed
time to accrue over. Glide-Path Phase remains Accumulation (10 days
elapsed since the 2026-08-26 inception, far inside the 0-7-year window).

### 2026-09-05 — Rules-change rebalance: theme-concentration cap introduced

**Rebalance — rules change (not a thesis exit):** Introduced the Investor
Profile's 25% theme-concentration cap (see `investor-profile.md`). Tagged
every holding with a Theme; AI-Capex (AVGO, GOOGL, NEE, MU, XLK) measured at
30.39% NAV, exceeding the new cap. Trimmed XLK from 59 sh ($10,974.00, 10.97%
NAV) to 30 sh ($5,580.00, 5.58% NAV) — sold 29 sh @ $186.00 = $5,394.00
proceeds routed to cash — bringing AI-Capex to $24,997.50 (25.00% NAV, at the
cap). No fundamental AI-Capex thesis changed for any of these five positions;
this is a concentration-rule trim only. Also added this cycle: `Cycle #` and
`Glide-Path Phase` header fields (Accumulation, per `investor-profile.md`'s
wall-clock-derived glide path) and the Theme Exposure table above.

### 2026-08-26 — Fill-out pass (same-day continuation of the Monday cycle)

Held positions: no thesis-relevant news since the morning entries; all 6 reaffirmed,
no action. Ran W2 Baseline Screener across the sectors not yet represented (healthcare,
consumer discretionary, communication services, materials, consumer staples, utilities,
a second semiconductor name) to move the stock sleeve toward its 60% target. Seven
positions opened, each sized under the 5% NAV cap:

**LLY — Eli Lilly (BUY, 4 sh @ $1,215.13, $4,860.52, 4.86% NAV)**
Fundamentals: Q2 2026 revenue $22.97B (+47.7% YoY), EPS $8.38 vs. $6.40 est. Raised FY2026
guidance to $85-87B revenue / ~$36 non-GAAP EPS. Catalyst: GLP-1 franchise demand. Entered
on a down day (-1.5%) rather than chasing strength. Stop: guidance cut or GLP-1 competitive
share loss. Target: reassess at next earnings given raised guidance.

**TJX — TJX Companies (BUY, 35 sh @ $139.48, $4,881.80, 4.88% NAV)**
Fundamentals: off-price model delivering 5% comps in FY2026, steady grower with an 8-week
price high but not an all-time high (all-time high $167.88 vs. entry $139.48). Catalyst:
continued market-share gains from full-price retail. Diversification into defensive-leaning
consumer discretionary. Stop: comp-sales deceleration. Target: prior high $167.88 zone.

**GOOGL — Alphabet (BUY, 14 sh @ $341.95, $4,787.30, 4.79% NAV)**
Fundamentals: accelerating Google Cloud AI adoption; BNP Paribas Outperform, $420 target
(~23% above entry). Catalyst: AI-driven ad + cloud growth. Entered on a down day (-1.44%,
market weighing AI capex vs. cloud growth) rather than chasing strength. Diversification
into communication services. Stop: cloud growth deceleration or ad-market softness. Target:
analyst consensus $420.

**BALL — Ball Corporation (BUY, 81 sh @ $61.30, $4,965.30, 4.97% NAV)**
Fundamentals: analysts raised fair-value estimate to $63.26 (updated Street targets $65-78
range) on volume-trend and cost improvements. Catalyst: aluminum-packaging demand recovery.
Diversification into materials. Stop: volume-trend reversal. Target: Street range $65-78.

**PEP — PepsiCo (BUY, 35 sh @ $142.27, $4,979.45, 4.98% NAV)**
Fundamentals: organic volume growth accelerating to +1% (fastest since 2022) as
streamlining efforts pay off; stock down ~10% over 6 months, trading below its 12-month
average target ($155, ~9% upside). Catalyst: margin recovery from restructuring.
Diversification into consumer staples (defensive ballast). Stop: further volume
deterioration. Target: analyst consensus $155.

**NEE — NextEra Energy (BUY, 59 sh @ $84.29, $4,973.11, 4.97% NAV)**
Fundamentals: $100B data-center campus JV with Brookfield in Paducah, KY; 21GW of
large-load pipeline interest, 12GW in advanced discussions. Trading well below its
2026 all-time high ($98.75) despite the AI-power buildout thesis; 20-analyst Buy
consensus, $98.39 target (~17% above entry). Diversification into utilities — direct AI
power-demand exposure, uncorrelated to the XLI/ETN industrial-power thesis. Stop:
Dominion merger regulatory setback. Target: analyst consensus $98.39.

**MU — Micron Technology (BUY, 5 sh @ $930.25, $4,651.25, 4.65% NAV)**
Fundamentals: fiscal Q2 2026 revenue +196% YoY, non-GAAP EPS +682% YoY; HBM supply for
2026 already sold out, 2027 capacity under long-term agreements. Morgan Stanley's top 2026
semiconductor pick. Catalyst: AI memory/HBM demand, second AI-infrastructure name alongside
AVGO but a different sub-sector (memory vs. networking silicon) — watched for RSI/momentum
risk given the sharp run. Stop: HBM pricing or hyperscaler capex deceleration. Target:
reassess at next earnings.

**No positions sold or trimmed this pass.** Stock sleeve moved from 3 to 10 positions
(15.0% → 49.1% of NAV); cash declined from 55.1% to 21.0%, still above the 10% floor.

### 2026-08-26 — Seed the portfolio (inception)

Ran the W2 Baseline Screener and W4 Sector Rotation Detector on public market data.
No held positions to review (first cycle). Six positions opened:

**XLK — Technology Select Sector SPDR (BUY, 59 sh @ $186.00, $10,974.00, 10.97% NAV)**
W4 sector-rotation scan: Tech is receiving the dominant share of 2026 sector inflows
(~78% of $17B June sector inflows per State Street data), driven by continued AI capex.
Top accumulation-signal sector alongside Industrials. Sized near the 15% ETF sleeve cap
minus room for a second sleeve pick.

**XLI — Industrial Select Sector SPDR (BUY, 59 sh @ $185.96, $10,971.64, 10.97% NAV)**
W4 scan: Industrials is the single best-performing S&P sector YTD 2026 (+19.5%) and led
sector inflows in June ($2.2B), driven by AI-data-center power/cooling capex (Eaton,
Vertiv-adjacent names) and reshoring/logistics demand. Second accumulation-signal sleeve
pick.

**AVGO — Broadcom (BUY, 14 sh @ $357.56, $5,005.84, 5.01% NAV)**
Fundamentals: record $22.1B quarterly revenue, 25.2% YoY revenue growth, 54.7% EBITDA
margin. Valuation: P/E ~59.7x — rich, but growth-adjusted and consistent with AI-networking
peers; 26-analyst Buy consensus, price target $501.58 (~40% above entry). Catalyst: continued
AI custom-silicon/networking demand tailwind, consistent with the XLK sector thesis at the
single-name level. Entry zone: current price. Stop: thesis breaks if AI-infra capex growth
decelerates materially (watch hyperscaler capex guidance in upcoming earnings). Target:
analyst consensus $501.58.

**ETN — Eaton Corporation (BUY, 12 sh @ $412.97, $4,955.64, 4.96% NAV)**
Fundamentals: Q2 2026 adjusted EPS $3.15 (beat $3.07), revenue $8.5B (beat $8.16B, +21%
YoY), record 23.1% adjusted operating margin, backlog up 43% YoY. Company raised full-year
organic growth guidance to 11-13% (from 9-11%) and adjusted EPS outlook to $13.40-$13.60.
Catalyst: data-center power/cooling ("grid-to-chip") demand — directly confirms the XLI
sector-rotation thesis at the single-name level; Boyd (liquid cooling) revenue forecast
raised to $1.8B FY. Entry zone: current price. Stop: guidance cut or backlog growth reversal.
Target: reassess at next earnings given raised guidance already priced partially in.

**COF — Capital One Financial (BUY, 23 sh @ $216.96, $4,990.08, 4.99% NAV)**
Fundamentals: Q2 2026 revenue $15.85B (+26% YoY), adjusted EPS $5.81, P/E compressed to
~12.2x (from ~38.5x in Q1) — screens as undervalued relative to growth. Catalyst: Discover
acquisition integration driving card/network growth; multiple recent analyst upgrades on
litigation clarity. 16-analyst Buy consensus, price target $258.27 (~19% above entry).
Diversification pick outside the AI-infrastructure theme (financials sleeve). Entry zone:
current price. Stop: credit-quality deterioration or Discover integration setback. Target:
analyst consensus $258.27.

**AGG — iShares Core U.S. Aggregate Bond ETF (BUY, 82 sh @ $97.90, $8,027.80, 8.03% NAV)**
Passive core bond sleeve per fixed sizing rules — not re-picked weekly, only rebalanced on
drift from the 8% target. ~4.06% dividend yield.

**No positions sold or trimmed this cycle (inception).**

Cash reserve ($55,075.00, 55.08% of NAV) held above the ~10% floor pending additional
stock candidates clearing the Watchlist Entry Criteria over coming Monday cycles, and
accrues at ~4-5%/yr SGOV-equivalent starting this date.
