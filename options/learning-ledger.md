# Options Learning Ledger

Every decision this portfolio makes — opening, adjusting, closing, or choosing
*not* to trade — is explained here for a beginner. Each entry shows the market
context, why this strategy beat the alternatives, the exact trade, what can go
wrong, and one or two new concepts. Every number comes from the `Reproduce:`
command in the entry; re-running it re-prices against the quotes available
when re-run, which may differ from the cycle's quotes. Sources for the
concepts: `RESOURCES.md`.

Entries on closed trades end with **Your reflection** — left empty for you.

## Primer

Read once before the first entry. Definitions paraphrase the Options Industry
Council (optionseducation.org) and the OCC's *Characteristics and Risks of
Standardized Options* (theocc.com) — see RESOURCES.md.

- **Option** — a contract giving the buyer the *right*, not the obligation, to
  buy or sell an underlying asset at a set price before or on a set date. The
  seller takes on the matching *obligation*.
- **Call / Put** — a call is the right to *buy*; a put is the right to *sell*.
- **Strike** — the price at which the option lets you buy (call) or sell (put).
- **Expiration** — the last day the option exists. **DTE** = days to expiration.
- **Premium** — the price of the option, quoted per share. One US equity option
  contract covers **100 shares**, so a $1.50 premium costs $150 per contract.
- **Bid / Ask / Mid** — the highest price buyers are paying, the lowest sellers
  are asking, and the midpoint. The gap is a cost you pay when trading.
- **In / at / out of the money** — whether exercising right now would be worth
  something (ITM), be break-even (ATM), or be worthless (OTM).
- **Intrinsic vs. extrinsic value** — intrinsic is what the option is worth if
  exercised now; extrinsic ("time value") is everything above that, and it
  decays to zero by expiration.
- **Long vs. short** — buying an option (long) risks the premium paid; selling
  one (short) collects premium but takes on the obligation. This portfolio only
  sells options when a bought option caps the risk.

## Concept Index

| Concept | First explained in |
|---|---|
| Premium & breakeven | [2026-10-02 OPEN SPY](#2026-10-02--open-spy-bull-call-debit-spread-cycle-2) |
| Vertical spreads (debit) | [2026-10-02 OPEN SPY](#2026-10-02--open-spy-bull-call-debit-spread-cycle-2) |
| Delta | [2026-10-05 OPEN QQQ](#2026-10-05--open-qqq-bull-call-debit-spread-cycle-3) |
| Theta | [2026-10-05 OPEN QQQ](#2026-10-05--open-qqq-bull-call-debit-spread-cycle-3) |
| Implied volatility | [2026-10-06 PASS](#2026-10-06--pass-cycle-4) |
| Expected move | [2026-10-06 PASS](#2026-10-06--pass-cycle-4) |
| Vega | [2026-10-07 PASS](#2026-10-07--pass-cycle-5) |
| IV rank | [2026-10-08 PASS](#2026-10-08--pass-cycle-6) |
| Probability of profit | [2026-10-08 PASS](#2026-10-08--pass-cycle-6) |
| Credit vs debit | [2026-10-09 PASS](#2026-10-09--pass-cycle-7) |
| Volatility risk premium | [2026-10-09 PASS](#2026-10-09--pass-cycle-7) |
| Gamma & why 21 DTE | [2026-10-12 PASS](#2026-10-12--pass-cycle-8) |
| Skew | [2026-10-13 PASS](#2026-10-13--pass-cycle-9) |
| Stop-loss | [2026-10-14 CLOSE QQQ](#2026-10-14--close-qqq-bull-call-debit-spread-cycle-10) |
| Rolling | [2026-10-14 CLOSE QQQ](#2026-10-14--close-qqq-bull-call-debit-spread-cycle-10) |
| Term structure (contango/backwardation) | [2026-10-16 PASS](#2026-10-16--pass-cycle-12) |
| Credit vertical spread (bull put) | [2026-10-19 OPEN SPY](#2026-10-19--open-spy-bull-put-credit-spread-cycle-13) |
| Risk/reward ratio vs. win rate | [2026-10-19 OPEN SPY](#2026-10-19--open-spy-bull-put-credit-spread-cycle-13) |

## Entries

### 2026-10-19 — OPEN SPY bull put credit spread (Cycle #13)
**Decision:** Sell 2 SPY Nov-20 748/740 put credit spreads (id 2026-10-19-SPY-BPCS-1), collecting $1.1025 per share ($220.50) with a worst case of $1,379.50.
**Market context in plain words:** Calm market with fair-to-rich option prices. VIX is 17.55 with VIX3M at 19.16 (contango, no stress) and the VIX is higher than on 58.3% of days in the past year, so options are a bit pricier than usual. SPY is $769.89; the options market says a typical 30-day move is about ±$28.90 (iv30 13.10%). IV history is only 11 days, so IV rank is unavailable and the VIX percentile is the proxy. After a stretch of sitting in cash since the Oct-16 close, the 50-65 zone points toward modest premium selling rather than buying.
**Why this strategy:** A bull put credit spread gets paid if SPY stays above 748. Rejected: (1) another bull call debit spread — we just lost money on two of them, and buying premium is the opposite of what a 58th-percentile VIX favors; (2) an iron condor — it also bets SPY stays under a call-side strike, and we have no view that capping the upside earns enough extra credit here. The put spread wins because the short strike (0.25 delta, 21 points below spot, inside the 1-sigma expected move) sits well under today's price and the long 740 put makes the worst case a known number.
**The trade (from `price-spread`):**
| Action | Contracts | Type | Strike | Expiry | Fill |
|---|---|---|---|---|---|
| SELL | 2 | Put | 748 | 2026-11-20 | 5.6275 |
| BUY | 2 | Put | 740 | 2026-11-20 | 4.525 |

- Net credit: $1.1025/share = $220.50 for 2 contracts. Max profit $220.50, max loss $1,379.50 (width $8 × 100 × 2 = $1,600 − credit), breakeven 746.90, probability of profit 74.2%, fees round trip $5.20 (entry $2.60 recorded now). Max loss + fees = $1,384.70, under the 3% NAV cap ($1,474) and 2.8% of NAV as capital at risk (limit 25%).
- Profit target 50% of max profit (buy back near $0.55); stop loss if the loss reaches 2× the credit ($441); close or roll at 21 DTE (Oct 30 → Nov 20 expiry gives a 21-DTE date of 2026-10-30).
```
       220                        ****************************
           ---------------------------------------------------
                                        |                     
                                 *      |                     
                                        |                     
                                        |                     
                                        |                     
                                        |                     
                                *       |                     
                                        |                     
     -1380 *********************        |                     
           666.00                                       846.88
```
**Greeks in dollars (whole position):** delta +9.86 share-equivalents (if SPY rises $1, the position gains about $10); theta +$2.32/day (if nothing else changes, about $2 a day from time decay in our favor); vega −$16.88 per IV point (if implied volatility rises one point, the position loses about $17); gamma −0.30.
**Concept spotlight:**
- *Credit vertical spread (bull put spread):* You sell one put and buy a cheaper put further down, in the same expiry. The money comes in on day one — the credit — and you keep all of it if SPY finishes above the short strike (748). Here we sell the 748 put for 5.6275 and buy the 740 put for 4.525, net $1.1025. The 740 put is insurance: no matter how far SPY falls, the most we lose is the $8 strike gap minus the credit, $6.8975 per share. Compare with the debit spreads we held earlier ([Credit vs debit](#concept-index)): there we paid first and hoped; here we are paid first and hope nothing bad happens.
- *Risk/reward ratio vs. win rate:* This trade risks $1,379.50 to make $220.50 — about 6.3 dollars risked per dollar of potential profit. That only works if it wins often: break-even needs a win rate near 86%, and the model says 74.2%. In plain words, the rules let us take it, but it is not a bargain; selling premium pays on average only when the options are priced richer than the real moves, which is the [volatility risk premium](#concept-index). We are testing that, with a small stake, not assuming it.
**What would prove this wrong:** SPY closing below 746.90 at Nov-20, or a fast drop that pushes the spread's mark to about 3.31 (a $2.21 loss per share vs. the credit, the 2× stop) well before then. A volatility spike hurts us through vega even if SPY barely moves.
**Reproduce:**
```
python3 scripts/options_data.py --asof 2026-10-19 regime
python3 scripts/options_data.py --asof 2026-10-19 scan
python3 scripts/options_data.py --asof 2026-10-19 price-spread --symbol SPY --legs "SELL 1 P 748 2026-11-20;BUY 1 P 740 2026-11-20" --qty 2
```

### 2026-10-16 — PASS (Cycle #12)
**Decision:** Open nothing new; the portfolio is 100% cash after the SPY close.
**Market context:** Cboe throttled our VIX requests (HTTP 429), so today we do not know the VIX, VIX3M or whether the market is stressed. BXM 2579.50 and PUT 3703.48 did load. SPY is $768.93, expected 30-day move ±$27.97 (iv30 12.69%, from `scan`). Our rules say unknown stress counts as stress: no new single-stock premium selling and half the usual size limit (1.5% NAV).
**Why pass:** Rejected: (1) a fresh SPY bull call spread — it would repeat the bet we just closed with no regime read to justify it; (2) a bull put credit spread on SPY — selling premium blind to the VIX percentile means we cannot tell if we are paid enough for the risk. Flying with an instrument missing is the one time to wait.
**What I checked:** `regime` (exit 0, five null fields), `mark`, `scan` of 30 symbols (IV history only 10 days, so no IV rank), `record-iv` (30 appended).
**Concept spotlight:**
- *Term structure (contango/backwardation):* VIX measures expected volatility over 30 days; VIX3M over 3 months. Normally the longer one is higher (contango, e.g. 16.75 vs 18.65 yesterday) because the future is less certain. When the short-term number jumps above the long-term one (backwardation), traders are paying up for protection right now: a stress signal. That is why a missing VIX is treated cautiously: we cannot rule it out.
**What would prove this wrong:** A calm, rich-premium day we sat out. Missing it costs nothing.
**Reproduce:**
```
python3 scripts/options_data.py --asof 2026-10-16 regime
python3 scripts/options_data.py --asof 2026-10-16 scan
```

### 2026-10-16 — CLOSE SPY bull call debit spread (Cycle #12)
**Decision:** Close 2026-10-02-SPY-BCDS-1 (SPY 773/800 Nov-06 call spread, 1 lot) because it reached 21 days to expiry; do not roll.
**Market context in plain words:** We paid $9.70 per share for the right to profit if SPY rose above 773. SPY peaked near $779-ish earlier, but today it is $768.93, below our long strike. The spread is worth about $7.48 at mid (`mark`), -22.9%.
**Why close (not hold or roll):** Rejected: (1) hold to expiry — gamma risk grows near expiration (see [Gamma & why 21 DTE](#concept-index)) and SPY needs about +$13.8 (to $782.70 = 773 + 9.70 debit) just to break even; (2) roll to a later spread — it would be a new bullish bet with VIX data missing, so it must clear every entry rule fresh and cannot today.
**The trade (closing, from `price-spread`):**
| Action | Contracts | Type | Strike | Expiry | Fill |
|---|---|---|---|---|---|
| SELL (to close) | 1 | Call | 773 | 2026-11-06 | 8.0475 |
| BUY (to close) | 1 | Call | 800 | 2026-11-06 | 0.5875 |

Net credit $7.46/share = $746.00. Opened at a $9.70 debit. Fees: entry $1.30 + exit $1.30 = $2.60.
**Outcome:** Realized P&L = -(−7.46 + 9.70) × 100 − 2.60 = **-$226.60** (-23.4% of the debit).
**What drove the P&L (estimated from entry Greeks):** Price and time. Delta was about +40 share-equivalents (logged 2026-10-15), so the SPY decline hurt; theta of about -$10 to -$14/day over 14 days took roughly $150. The spread was +42% on Oct 6 and gave it all back — we had no profit-taking rule below +100%.
**Lesson:** A +42% gain unrealized is not a gain. A profit target that never triggers is only a wish; consider stating a partial-profit rule at entry.
**What would prove this wrong:** SPY rallying above $780 before Nov-06. We would have recovered; the 21-DTE rule exists because that is not predictable.
**Reproduce:**
```
python3 scripts/options_data.py --asof 2026-10-16 mark
python3 scripts/options_data.py --asof 2026-10-16 price-spread --symbol SPY --legs "SELL 1 C 773 2026-11-06;BUY 1 C 800 2026-11-06" --qty 1
```
**Your reflection:**

### 2026-10-15 — PASS (Cycle #11)
**Decision:** Open nothing new today; hold the SPY spread.
**Market context:** VIX 16.75 (44th percentile of the past year, contango, no stress). SPY $770.41 is slightly below where we bought. Options are neither cheap nor rich, so neither buying nor selling premium has an edge.
**Why pass:** Rejected: (1) another bull call spread — doubles a bet that is already -11.3%; (2) a bull put credit spread on SPY — a 44th-percentile VIX pays little for the risk. The SPY spread (delta +40 share-equivalents, theta -$14.03/day, vega +$40.41 per IV point, from `price-spread`) reaches 21 DTE tomorrow, when the rules say close or roll.
**What I checked:** `regime` (no errors), `mark` (SPY spread mark 8.605, no triggers), `scan` of 30 symbols (SPY iv30 13.0%, expected move ±$28.70), `record-iv`.
**What would prove this wrong:** A strong rally we sat out. Missing a move costs nothing.
**Reproduce:**
```
python3 scripts/options_data.py --asof 2026-10-15 regime
python3 scripts/options_data.py --asof 2026-10-15 scan
python3 scripts/options_data.py --asof 2026-10-15 price-spread --symbol SPY --legs "BUY 1 C 773 2026-11-06;SELL 1 C 800 2026-11-06" --qty 1
```

### 2026-10-14 — PASS (Cycle #10)
**Decision:** Open nothing new today.
**Market context:** VIX 16.19 (34th percentile of the past year, contango, no stress). SPY $770.72 and QQQ $732.55 fell again. Options are still on the cheap side, but we just got stopped out of one bullish bet and still hold another.
**Why pass:** Opening a fresh bullish spread right after a stop-out is chasing the loss back. Rejected: (1) a new QQQ call spread at lower strikes — same bet that just failed; (2) a bull put credit spread on SPY — VIX in the 34th percentile pays little for the risk. SPY's remaining spread has its own 21-DTE decision on 2026-10-16.
**What I checked:** `regime` (no stress, no errors), `mark`, `scan` of all 30 symbols (SPY iv30 12.8%, expected move ±$28.18; INTC 65.1% and AMD 57.2% richest, single-stock), `record-iv`.
**What would prove this wrong:** A sharp rebound that we sat out. Missing a move costs nothing; a forced trade costs real (paper) money.
**Reproduce:**
```
python3 scripts/options_data.py --asof 2026-10-14 regime
python3 scripts/options_data.py --asof 2026-10-14 scan
```

### 2026-10-14 — CLOSE QQQ bull call debit spread (Cycle #10)
**Decision:** Close 2026-10-05-QQQ-BCDS-1 (QQQ 760/790 Nov-06 call spread, 1 lot) because the stop-loss fired.
**Market context in plain words:** QQQ drifted down from $757-ish when we bought to $732.55. A call spread needs the price to rise; instead it fell, so the spread we paid $10.83 for is now worth about $3.56 at mid. That is -67.1% of what we paid, past our -50% limit.
**Why close (not hold or roll):** The rule was written before the trade, when we were calm. Rejected: (1) hold and hope — QQQ would need to rally above $763.54 (breakeven of the closing trade's mirror) to recover, and only ~23 days remain; (2) roll to a later expiry — a roll means paying more premium for the same failed thesis, and the thesis (QQQ rises) is not better today than on Oct 5.
**The trade (closing):**
| Action | Contracts | Type | Strike | Expiry | Fill |
|---|---|---|---|---|---|
| SELL (to close) | 1 | Call | 760 | 2026-11-06 | 4.00 |
| BUY (to close) | 1 | Call | 790 | 2026-11-06 | 0.455 |

Net credit received $3.545/share = $354.50. Opened at a $10.8325 debit. Fees: entry $1.30 + exit $1.30 = $2.60.
**Outcome:** Realized P&L = -(−3.545 + 10.8325) × 100 − 2.60 = **-$731.35** (-67.5% of the debit).
**What drove the P&L (estimated from entry Greeks):** Mostly price: delta was about +25 share-equivalents, and QQQ fell roughly $25 from entry, which accounts for most of the loss. Time decay (theta about -$16/day over 9 days, ≈ -$140) took a further bite. Implied volatility moved little (vega effect small).
**Position risk at the end:** the max loss was always capped at $1,083 (2.2% of NAV); the stop kept us from taking all of it.
**Concept spotlight:**
- *Stop-loss:* a pre-decided exit price. Example: we bought this spread for $10.83 and said we would sell if it fell to half, about $5.42. The market blew through it (it hit $3.56), so we exit at the next price, not the ideal one. A stop does not guarantee the exact loss; it prevents a bad trade from becoming a worse one.
- *Rolling:* closing a position and opening a similar one further out in time (or at different strikes) to give the idea more time. Example: sell this Nov-06 spread and buy a Dec spread. It is only sensible if you would open that new trade fresh today; otherwise it is just a way to avoid admitting a loss.
**What would prove this wrong:** QQQ rallying hard this week. We would have recovered some money by holding, but the rule exists because that outcome is not predictable.
**Reproduce:**
```
python3 scripts/options_data.py --asof 2026-10-14 mark
python3 scripts/options_data.py --asof 2026-10-14 price-spread --symbol QQQ --legs "SELL 1 C 760 2026-11-06;BUY 1 C 790 2026-11-06" --qty 1
```
**Your reflection:**

### 2026-10-13 — PASS (Cycle #9)
**Decision:** Open nothing new; hold both bull call spreads (no trigger fired).
**Market context:** SPY slipped to $776.82 and QQQ to $742.09. The VIX is 15.44 (19th percentile of the past year, contango, no stress): options are still cheap. SPY spread is +$200.50 (+20.7%); QQQ spread is -$503.75 (-46.5%). The QQQ stop is -50% of the debit, a spread value of about 5.42 versus 5.795 now, so only about $38 from being triggered. Both are at 24 DTE; the 21-DTE exit arrives 2026-10-16.
**Why pass:** Both holdings are one bet (US large caps up by Nov-06), and QQQ is nearly stopped out. Rejected: (1) a fresh QQQ spread at lower prices — that is averaging down into a position the rules say to cut at -50%; (2) a bull put credit spread on SPY — with VIX in the 19th percentile we are paid little for the risk. The stop, not hope, decides QQQ's fate.
**What I checked:** `regime` (no stress, no errors), `mark` (no triggers, no errors), `scan` of all 30 symbols (SPY iv30 12.2%, expected move ±$27.09; QQQ 18.3%, ±$38.98; INTC 63.7% and AMD 55.6% richest but single-stock), `record-iv`.
**Greeks for what we hold (from `price-spread`):** SPY spread: delta +43.56 share-equivalents, gamma 0.31, theta -$9.70/day, vega +$25.36 per IV point; PoP 39.3%, breakeven $784.74. QQQ spread: delta +25.43, gamma 0.65, theta -$15.99/day, vega +$41.39; PoP 24.3%, breakeven $765.87. Together theta is about -$25.69/day: if nothing else changes, time decay costs the pair roughly $26 a day.
**Concept spotlight:**
- *Skew:* options on the same stock and expiry do not all trade at the same implied volatility. Puts far below the price usually cost more IV than at-the-money options, because investors pay up for crash protection. Example from today's scan: SPY Nov-13 700 put has IV 22.96%, while the 780 call near the money has IV 12.18%. That gap is skew. It means a credit spread that sells a downside put collects richer premium than the at-the-money IV suggests, and a bought put costs extra.
**What would prove this wrong:** A sharp rebound in QQQ that makes us wish we had added; or QQQ falling to its stop (spread value near 5.42), which would lock in a loss near -$550 including fees. Either way the 21-DTE decision is on 2026-10-16.
**Reproduce:**
```
python3 scripts/options_data.py --asof 2026-10-13 regime
python3 scripts/options_data.py --asof 2026-10-13 mark
python3 scripts/options_data.py --asof 2026-10-13 scan
python3 scripts/options_data.py --asof 2026-10-13 price-spread --symbol SPY --legs "BUY 1 C 773 2026-11-06;SELL 1 C 800 2026-11-06" --qty 1
python3 scripts/options_data.py --asof 2026-10-13 price-spread --symbol QQQ --legs "BUY 1 C 760 2026-11-06;SELL 1 C 790 2026-11-06" --qty 1
```

### 2026-10-12 — PASS (Cycle #8)
**Decision:** Open nothing new; hold both bull call spreads (no trigger fired).
**Market context:** SPY rose to $778.87 and QQQ fell to $747.63, so the two indexes diverged again. The VIX is 15.14 (13th percentile of the past year, contango, no stress): options are still cheap. SPY spread is +$292.00 (+30.1%); QQQ spread is -$335.75 (-31.0%). The QQQ stop is -50% of the debit (spread value about 5.42 vs 7.475 now); both are at 25 DTE, so the 21-DTE exit is only 4 days away.
**Why pass:** Both holdings are one bet (US large caps up by Nov-06), and capital at risk is already 4.1% NAV. Rejected: (1) a new debit spread on a third index (IWM/DIA) — the same bet again, with QQQ already losing; (2) a credit spread on a rich-IV single stock (INTC iv30 61.1%, AMD 53.1%) — single-stock short premium with no clear thesis, and the IV is high for a reason. The rules allowed a trade; judgment said wait.
**What I checked:** `regime` (no stress, no errors), `mark` (no triggers, no errors), `scan` of all 30 symbols (SPY iv30 12.0%, expected move ±$26.81; QQQ 17.9%, ±$38.38; IV history 6 days so the VIX percentile is the proxy), `record-iv`.
**Greeks for what we hold (from `price-spread`):** SPY spread: delta +42.81 share-equivalents, gamma 0.14, theta -$7.38/day, vega +$18.02 per IV point; PoP 41.8%, breakeven $785.67. QQQ spread: delta +28.59, gamma 0.55, theta -$14.56/day, vega +$38.38; PoP 28.6%, breakeven $767.47. Together theta is about -$21.94/day: if nothing else changes, time decay costs the pair roughly $22 a day.
**Concept spotlight:**
- *Gamma & why 21 DTE:* delta says how much an option gains per $1 move in the stock; **gamma** says how fast delta itself changes. Our QQQ spread has gamma 0.55: for each $1 QQQ moves, the position's delta shifts by about 0.55 share-equivalents, so a $10 rally would lift delta from ~29 to ~34 and make the position behave more like owning shares. Gamma grows as expiration nears, so a few days can swing the position hard in either direction. That is why the profile closes or rolls anything at 21 DTE: after that, outcomes get jumpier and less predictable for the same dollars at risk.
**What would prove this wrong:** A sharp rally that makes us wish we had added, or QQQ sliding to its stop (spread value near 5.42). Also the 21-DTE exit arrives soon, so we must decide then whether to close or roll.
**Reproduce:**
```
python3 scripts/options_data.py --asof 2026-10-12 regime
python3 scripts/options_data.py --asof 2026-10-12 mark
python3 scripts/options_data.py --asof 2026-10-12 scan
python3 scripts/options_data.py --asof 2026-10-12 price-spread --symbol SPY --legs "BUY 1 C 773 2026-11-06;SELL 1 C 800 2026-11-06" --qty 1
python3 scripts/options_data.py --asof 2026-10-12 price-spread --symbol QQQ --legs "BUY 1 C 760 2026-11-06;SELL 1 C 790 2026-11-06" --qty 1
```

### 2026-10-09 — PASS (Cycle #7)
**Decision:** Open nothing new; hold both bull call spreads (no trigger fired).
**Market context:** The VIX is 14.88, only the 8th percentile of the past year (contango, no stress): options are about as cheap as they have been all year. SPY is $777.41 and our SPY spread is +$242.00 (+24.9%). QQQ is $750.17 and our QQQ spread is -$215.25 (-19.9%): the two indexes split today, even though we treated them as one bet. The QQQ stop is -50% of the debit (spread value about 5.42 vs 8.68 now); 28 DTE, so the 21-DTE rule is a week away.
**Why pass:** Cheap options favor buying, which we already did. A third bullish spread would be more of the same bet, and doubling down on the losing QQQ leg is not a plan. Rejected: (1) a bull put credit spread on SPY — at this volatility the market pays very little for the risk (see spotlight); (2) a single-stock iron condor on a rich-IV name (AMD iv30 53.9%, INTC 63.6%) — would be short premium on a single stock with no earnings check or clear thesis, and rich IV there usually exists for a reason. Capital at risk is 4.1% of NAV vs 25% cap and 2 of 5 weekly slots are used, so rules allowed a trade; judgment said wait.
**What I checked:** `regime` (no stress, no errors), `mark` (no triggers, no errors), `scan` of all 30 symbols (SPY iv30 11.97%, ±$26.68 expected move; QQQ 17.75%, ±$38.17; IWM 18.18%, ±$14.52; DIA 12.93%, ±$19.06 — nothing uncorrelated with a clear thesis; IV history 5 days so VIX percentile is the proxy), `record-iv`.
**Greeks for what we hold (from `price-spread`):** SPY spread: delta +40.7 share-equivalents, theta -$7.41/day, vega +$21.39 per IV point; PoP 41.4%, breakeven $785.12. QQQ spread: delta +29.18, theta -$12.53/day, vega +$35.19; PoP 31.0%, breakeven $768.71. Together theta is about -$19.94/day: if nothing else changes, time decay costs the pair roughly $20 a day.
**Concept spotlight:**
- *Credit vs debit:* a **debit** trade costs money up front (we pay, like both of our spreads); the most you can lose is what you paid, and time decay works against you. A **credit** trade pays you up front (you sell); the most you can lose is the spread width minus the credit, and time decay works for you, but you need the price to stay away from your short strike. Example: our SPY spread cost $9.70 per share to open; its mirror, a credit spread, would pay you instead and win when the stock stays put.
- *Volatility risk premium:* on average, implied volatility (what options charge) runs higher than the volatility that actually happens, so option sellers get paid a small edge for taking on risk. The edge is fattest when IV is high and thinnest when IV is low. With the VIX in its 8th percentile, selling premium is a poor deal today, which is why we pass on credit trades and have been buying instead.
**What would prove this wrong:** A rebound that makes us wish we had added, or QQQ sliding to its stop (spread value near 5.42).
**Reproduce:**
```
python3 scripts/options_data.py --asof 2026-10-09 regime
python3 scripts/options_data.py --asof 2026-10-09 mark
python3 scripts/options_data.py --asof 2026-10-09 scan
python3 scripts/options_data.py --asof 2026-10-09 price-spread --symbol SPY --legs "BUY 1 C 773 2026-11-06;SELL 1 C 800 2026-11-06" --qty 1
python3 scripts/options_data.py --asof 2026-10-09 price-spread --symbol QQQ --legs "BUY 1 C 760 2026-11-06;SELL 1 C 790 2026-11-06" --qty 1
```

### 2026-10-08 — PASS (Cycle #6)
**Decision:** Open nothing new; hold both bull call spreads (no trigger fired).
**Market context:** Stocks slipped again: SPY $774.46 (was $776.17), QQQ $753.36 (was $756.68). The VIX is 15.48 (19th percentile of the past year, contango, no stress), so options are still cheap. SPY spread +$151.00 (+15.6%), QQQ spread now -$56.25 (-5.2%). Stop is -50% of the debit, profit target +100%, 21-DTE rule is 8 days away from mattering (29 DTE).
**Why pass:** Both holdings are one bet (US large caps up by Nov-06). A dip does not make a third copy a different bet. Rejected: (1) averaging down with another QQQ spread — adds to the position that is losing and raises correlated risk; (2) a bull put credit spread — at VIX 15 we would be paid little for the risk. Capacity was not the problem (capital at risk 4.1% NAV vs 25% cap; 2 of 5 weekly slots used).
**What I checked:** `regime`, `mark` (no triggers, no errors), `scan` of all 30 symbols (SPY iv30 12.55%, ±$27.86 expected move; QQQ 18.3%, ±$39.56; AMD 54.4%, INTC 65.6% are the richest but single-stock and would need earnings checks and short premium — no clear thesis).
**Greeks for what we hold (from `price-spread`):** SPY spread: delta +38.4 share-equivalents, theta -$7.92/day, vega +$26.29 per IV point. QQQ spread: delta +29.4, theta -$10.69/day, vega +$28.62. Together theta is about -$18.61/day.
**Concept spotlight:**
- *IV rank:* where today's implied volatility sits between its lowest and highest level over the past year (0 = cheapest, 100 = most expensive). If SPY's IV ranged 10%-30% and is 12.55%, rank is about 13: cheap, favoring buying options. We only have 4 days of our own IV history (need 20), so we use the VIX percentile (19) as a stand-in.
- *Probability of profit (PoP):* the model's estimate of the chance a position finishes with a gain at expiration. Our SPY spread has PoP 38.8% (breakeven $784.26): it wins less than half the time but pays about 1.8 to 1 when it does (max profit $1,730 vs max loss $970). A low PoP is not bad on its own; compare it with the payout.
**What would prove this wrong:** A rebound that makes us wish we had added, or a slide to the stop (QQQ spread value near $5.42).
**Reproduce:**
```
python3 scripts/options_data.py --asof 2026-10-08 regime
python3 scripts/options_data.py --asof 2026-10-08 mark
python3 scripts/options_data.py --asof 2026-10-08 scan
python3 scripts/options_data.py --asof 2026-10-08 price-spread --symbol SPY --legs "BUY 1 C 773 2026-11-06;SELL 1 C 800 2026-11-06" --qty 1
python3 scripts/options_data.py --asof 2026-10-08 price-spread --symbol QQQ --legs "BUY 1 C 760 2026-11-06;SELL 1 C 790 2026-11-06" --qty 1
```

### 2026-10-07 — PASS (Cycle #5)
**Decision:** Open nothing new; hold both bull call spreads (no trigger fired).
**Market context:** The market dipped: SPY fell from $781.19 to $776.17 and QQQ from $762.16 to $756.68. The VIX is 15.35 (15.9th percentile of the past year, contango, no stress), so options are still cheap. Our spreads gave back some gains: SPY spread +$227.50 (+23.5%, was +42.4%), QQQ spread +$59.75 (+5.5%, was +20.8%). Profit target is +100%, stop is −50% of the debit, 21-DTE rule not near (30 DTE).
**Why pass:** Both holdings are the same bet (US large-cap stocks up by Nov-06). Adding a third would stack correlated risk; a dip does not change that. Rejected: (1) a third index bull call spread — more of the same exposure; (2) a bull put credit spread — premium is thin at VIX 15, so we would be paid little for the risk. Capital at risk is 4.1% of NAV, under the 25% cap, and 2 of 5 weekly slots are used, so the rules allowed a trade; judgment said wait.
**What I checked:** `regime` (no stress), `mark` (no triggers, no errors), `scan` of all 30 symbols (SPY iv30 12.5%, expected 30-day move ±$27.92; QQQ 18.5%, ±$40.03; IWM 19.1%, ±$15.16; XLE 25.4%, ±$4.60 — no uncorrelated setup with a clear thesis; IV history only 3 days so VIX percentile is the proxy).
**Greeks for what we hold (from `price-spread` at current quotes):** SPY spread: delta +37.6 share-equivalents, theta −$6.68/day, vega +$20.18 per IV point. QQQ spread: delta +29.2, theta −$9.10/day, vega +$22.67. Together theta is about −$15.78/day: if nothing else changes, time decay costs the pair roughly $16 a day.
**Concept spotlight:**
- *Vega:* how much a position's value changes when implied volatility moves one point. Our SPY spread has vega +$20.18, so if SPY's IV rose from 12.5% to 13.5%, the spread would gain about $20 (all else equal); if IV fell a point, it would lose about $20. We own options (we paid a debit), so we are "long vega": cheap options at VIX 15 are the reason we bought, and a rise in volatility would help us.
**What would prove this wrong:** A rebound that makes us wish we had added, or a deeper slide that tests the −50% stop (SPY: spread value at about $4.85, QQQ about $5.42). Either way each spread's thesis is in its OPEN entry.
**Reproduce:**
```
python3 scripts/options_data.py --asof 2026-10-07 regime
python3 scripts/options_data.py --asof 2026-10-07 mark
python3 scripts/options_data.py --asof 2026-10-07 scan
python3 scripts/options_data.py --asof 2026-10-07 price-spread --symbol SPY --legs "BUY 1 C 773 2026-11-06;SELL 1 C 800 2026-11-06" --qty 1
python3 scripts/options_data.py --asof 2026-10-07 price-spread --symbol QQQ --legs "BUY 1 C 760 2026-11-06;SELL 1 C 790 2026-11-06" --qty 1
```

### 2026-10-06 — PASS (Cycle #4)
**Decision:** Open nothing new today; hold both bull call spreads.
**Market context:** The VIX (the market's "fear gauge") is 15.23, only in the 13.9th percentile of the past year — options are cheap. SPY is $781.19 and QQQ $762.16; both rallied since we bought (SPY spread +$411.50, +42.4%; QQQ spread +$225.25, +20.8%). No management trigger fired (profit target is +100%, stop is −50% of the debit, 21 DTE).
**Why pass:** Cheap options say "buy premium", which we already did twice — but both trades are the same bet (US large-cap stocks go up, same Nov-06 expiry). A third would pile on correlated risk after a sharp rally. Rejected: (1) a third index bull spread — more of the same exposure; (2) selling a bull put credit spread — premium is thin when volatility is this low, so we'd be paid little for the risk. Capital at risk is 4.1% of NAV, well under the 25% cap, so the rule allowed a trade; judgment said wait. Skipping a day is a valid decision.
**What I checked:** `regime` (no stress), `mark` (no triggers), `scan` of all 30 symbols (e.g. SPY iv30 12.5%, expected 30-day move ±$28.02; QQQ 18.6%, ±$40.6; TLT 14.8%, ±$3.28 — no clear uncorrelated setup with a stated thesis), and capacity (1 new position this week of 5).
**Concept spotlight:**
- *Implied volatility (IV):* the annualized size of price swings the option prices are "implying". SPY's 30-day IV is 12.5%, meaning the market expects SPY to wobble roughly 12.5% a year. High IV = expensive options (good to sell); low IV = cheap (good to buy). It is derived from option prices, not from a forecast anyone made.
- *Expected move:* IV turned into dollars over a period. For SPY: $781.19 × 12.5% × √(30/365) ≈ $28, so the market is pricing roughly a ±$28 range by early November (about a one-standard-deviation range, ~68% likely). Our SPY spread breakeven is $782.70, so the stock needs to hold near here for us to stay in profit.
**What would prove this wrong:** A strong continued rally where we would have wished we had added; or a sharp reversal where passing saved us. Either way the thesis for each held spread stays the same — see their OPEN entries.
**Reproduce:**
```
python3 scripts/options_data.py --asof 2026-10-06 regime
python3 scripts/options_data.py --asof 2026-10-06 mark
python3 scripts/options_data.py --asof 2026-10-06 scan
```

### 2026-10-05 — OPEN QQQ bull call debit spread (Cycle #3)
**Decision:** Buy 1 QQQ Nov-06 760/790 call debit spread for a $10.83/share debit ($1,083).
**Market context:** The VIX is 15.57, still low (18.3rd percentile) with VIX3M at 18.06 — calm, no stress. Cheap options favor buying. QQQ is $753.80 and the market's expected 30-day move is about ±$40.51. Our SPY spread is already up $121.50 (+12.5%).
**Why this strategy:** Another capped-cost bullish bet. Rejected: (1) a bull put credit spread — selling premium pays little when volatility is low; (2) a second SPY spread — we would then hold two positions on one underlying; QQQ spreads the bet slightly, though it is highly correlated with SPY, so this is really more of the same view.
**The trade:**
| Action | Contracts | Type | Strike | Expiry | Fill |
|---|---|---|---|---|---|
| BUY | 1 | Call | 760 | 2026-11-06 | 15.145 |
| SELL | 1 | Call | 790 | 2026-11-06 | 4.3125 |

Max profit $1,916.75 · Max loss $1,083.25 · Breakeven 770.83 · Probability of profit 34.9% · fees_round_trip $2.60 (32 DTE).
```
      1917                     |        **********************
                               |                              
                               |       *                      
                               |      *                       
                               |     *                        
                               |    *                         
           ---------------------------------------------------
                               |   *                          
                               |  *                           
                               | *                            
     -1083 **********************                             
           678.42                                       869.00
```
**Greeks in dollars:** Delta +27.25 share-equivalents; theta −$8.89/day; vega +$24.10 per IV point.
**Concept spotlight:**
- *Delta:* how much an option's price moves when the stock moves $1. Our long 760 call has delta 0.48, the short 790 call 0.21; net 0.27 per share × 100 = +27 share-equivalents, so QQQ up $1 ≈ +$27 for the position (a small gain, not guaranteed).
- *Theta:* time decay. Net theta −$8.89/day means that if nothing else changes, the position loses about $9 a day as expiry nears, because we own more option time value than we sold. Debit spreads are a race: the stock must move up faster than time decay eats the premium.
**What would prove this wrong:** QQQ flat or falling — it needs to finish above 770.83 (+2.3%). Exit rule: loss reaches 50% of the debit, profit hits 100%, or 21 DTE.
**Reproduce:** `python3 scripts/options_data.py --asof 2026-10-05 price-spread --symbol QQQ --legs "BUY 1 C 760 2026-11-06; SELL 1 C 790 2026-11-06" --qty 1` (re-prices against the quotes available when re-run)

### 2026-10-02 — OPEN SPY bull call debit spread (Cycle #2)
**Decision:** Buy 1 SPY Nov-06 773/800 call debit spread for a $9.70/share debit ($970).
**Market context:** The VIX ("fear gauge") is 15.65, low for the past year (18.7th percentile), and VIX3M (18.24) is above it — a calm market with no stress. When option prices are cheap, buying is more attractive than selling. SPY is $768.99; the market's expected 30-day move is about ±$28.
**Why this strategy:** A debit spread is a bet SPY rises, with a capped cost. Rejected: (1) a plain long call — costs about $12 per share and loses more if nothing happens; (2) a bull put credit spread — selling premium pays little when volatility is this low.
**The trade:**
| Action | Contracts | Type | Strike | Expiry | Fill |
|---|---|---|---|---|---|
| BUY | 1 | Call | 773 | 2026-11-06 | 12.09 |
| SELL | 1 | Call | 800 | 2026-11-06 | 2.39 |

Max profit $1,730 · Max loss $970 · Breakeven 782.70 · Probability of profit 35.5% · fees_round_trip $2.60 (35 DTE).
```
      1730                     |        **********************
                               |       *
                               |      *
                               |
                               |     *
                               |    *
           ---------------------------------------------------
                               |   *
                               |  *
                               | *
      -970 **********************
           692.09                                       880.00
```
**Greeks in dollars:** Delta +33 share-equivalents: SPY up $1 ≈ +$33. Theta −$8.00/day: if nothing else changes, the position loses about $8 a day to time decay. Vega +$33.37 per IV point: if implied volatility rises 1 point, the position gains about $33.
**Concept spotlight:**
- *Premium & breakeven:* the premium is the price of an option. We pay $12.09 and receive $2.39, a net $9.70 debit. SPY must finish above 773 + 9.70 = 782.70 to profit.
- *Vertical (debit) spread:* buy one option and sell another of the same type and expiry at a different strike. The sold call (800) pays part of the cost but caps the gain at (800−773)−9.70 = $17.30/share.
**What would prove this wrong:** SPY flat or falling by Nov 6 (it needs ~+1.8% to break even). Exit rule: loss reaches 50% of the debit, profit hits 100%, or 21 DTE.
**Reproduce:** `python3 scripts/options_data.py --asof 2026-10-02 price-spread --symbol SPY --legs "BUY 1 C 773 2026-11-06; SELL 1 C 800 2026-11-06" --qty 1` (re-prices against the quotes available when re-run)

Newest first. Format:

    ### YYYY-MM-DD — <OPEN|ADJUST|ROLL|CLOSE|ASSIGNED|PASS> <symbol> <strategy> (Cycle #N)
    **Decision:** …
    **Market context:** …
    **Why this strategy:** …
    **The trade:** legs table, max profit, max loss, breakeven(s), probability of profit, payoff diagram
    **Greeks in dollars:** …
    **Concept spotlight:** …
    **What would prove this wrong:** …
    **Reproduce:** `python3 scripts/options_data.py --asof YYYY-MM-DD …` (re-prices against the quotes available when re-run)
    (Only OPEN headings count toward the 5-new-positions-per-week limit; a ROLL is not a new position.)
    (CLOSE entries add) **Outcome:** · **What drove the P&L:** · **Lesson:** · **Your reflection:** (blank)
