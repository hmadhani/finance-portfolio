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

## Entries

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
