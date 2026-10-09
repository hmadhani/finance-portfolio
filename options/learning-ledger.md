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

## Entries

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
