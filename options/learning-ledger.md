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
| Premium & breakeven | [SPY bull put spread](#2026-10-02--open-spy-bull-put-spread-cycle-2) |
| Credit vs. debit & vertical spreads | [SPY bull put spread](#2026-10-02--open-spy-bull-put-spread-cycle-2) |
| Delta | [TLT bull put spread](#2026-10-02--open-tlt-bull-put-spread-cycle-2) |
| Probability of profit | [TLT bull put spread](#2026-10-02--open-tlt-bull-put-spread-cycle-2) |

## Entries

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

### 2026-10-02 — OPEN SPY bull put spread (Cycle #2)
**Decision:** Sell a SPY put credit spread: SELL 735 put / BUY 725 put, 2026-11-06, 1 contract.
**Market context:** The S&P 500 ETF (SPY) trades at 763.99. The market's "fear gauge" (VIX) is 16.39 and is *below* its 3-month version (18.58) — a calm, normal market, not a stressed one. VIX is at the 34th percentile of its past year: middle-to-low. With no IV history yet, the profile says to use that as the guide: neither rich enough to lean hard into selling premium nor cheap enough to buy it, so a modest, defined-risk bet that SPY does not fall much is reasonable. SPY's implied 30-day volatility is 13.4%, and the market expects roughly a ±$29.43 move over 30 days.
**Why this strategy:** A bull put spread earns money if SPY stays above 735 at expiry (about 4% below today's price) and caps the loss at the 10-point width minus the credit. Rejected: (1) a *naked* short 735 put would collect more but has a huge worst case and is forbidden; (2) a *debit* call spread (bet on a rally) needs SPY to rise a lot to win, whereas the put spread wins if SPY merely does not fall; (3) a wider 725/700 spread would have a max loss of roughly $2,300, above the 3% NAV cap of $1,500.
**The trade:**

| Action | Contracts | Type | Strike | Expiry | Fill |
|---|---|---|---|---|---|
| SELL | 1 | Put | 735 | 2026-11-06 | 4.8725 |
| BUY | 1 | Put | 725 | 2026-11-06 | 3.7375 |

Net credit $1.135/share = $113.50. Max profit $113.50. Max loss $886.50 (10-point width × 100 − credit). Breakeven 733.87. Probability of profit 77.6%. Fees round trip $2.60 (entry $1.30). Sizing: $886.50 + $2.60 = $889.10 ≤ 3% of NAV ($1,500.18), so 1 contract.
```
       114                       *****************************
           ---------------------------------------------------
                                         |                    
                                         |                    
                                *        |                    
                                         |                    
                                         |                    
                               *         |                    
                                         |                    
                                         |                    
      -886 ********************          |                    
           652.50                                       840.39
           P&L ($) at expiry vs. underlying price.  | = today's price  - = $0 line
```
**Greeks in dollars:** delta +4.9 share-equivalents: if SPY rises $1, the position gains about $4.90. Theta +$1.70/day: if nothing else changes, the position gains about $1.70 per day from time decay. Vega −$10.45 per IV point: if implied volatility rises one point, the position loses about $10. Gamma −0.15.
**Concept spotlight:**
- **Premium & breakeven.** Premium is the price of an option. Here we *receive* $1.135 per share ($113.50) for the spread. Breakeven is the stock price where the trade neither makes nor loses money at expiry: the short strike 735 minus the credit 1.135 gives 733.87. Below that we lose; above it we profit.
- **Credit vs. debit & vertical spreads.** A vertical spread is two options of the same type and expiry at different strikes. When you receive money to open it, it is a *credit* spread (you want the options to expire worthless and keep the cash); when you pay to open it, it is a *debit* spread. The bought 725 put is insurance that turns an open-ended loss into a capped one.
**What would prove this wrong:** SPY closing below 735 before expiry — a sell-off of more than ~4%. Management per the profile: close at 50% of max profit ($56.75), at a loss of 2× the credit ($227), or at 21 DTE.
**Reproduce:** `python3 scripts/options_data.py --asof 2026-10-02 regime` · `python3 scripts/options_data.py --asof 2026-10-02 scan` · `python3 scripts/options_data.py --asof 2026-10-02 price-spread --symbol SPY --legs "SELL 1 P 735 2026-11-06; BUY 1 P 725 2026-11-06" --qty 1`

### 2026-10-02 — OPEN TLT bull put spread (Cycle #2)
**Decision:** Sell a TLT (20+ year Treasury bond ETF) put credit spread: SELL 75 put / BUY 70 put, 2026-11-06, 3 contracts.
**Market context:** TLT trades at 77.70 with 30-day implied volatility of 16.3% and an expected 30-day move of about ±$3.63. Same calm regime as above (VIX 16.39, contango, VIX percentile 34). A bond ETF adds a position that is not simply another bet on stocks.
**Why this strategy:** We win if TLT stays above 75 (about 3.5% below today). Rejected: (1) an iron condor would also sell calls above, but that adds a second side to manage and risk for little extra credit; (2) a long put or debit put spread bets on a fall — the opposite of the neutral-to-mildly-bullish stance here — and pays for time decay instead of collecting it.
**The trade:**

| Action | Contracts | Type | Strike | Expiry | Fill |
|---|---|---|---|---|---|
| SELL | 3 | Put | 75 | 2026-11-06 | 0.655 |
| BUY | 3 | Put | 70 | 2026-11-06 | 0.1175 |

Net credit $0.5375/share = $161.25 total. Max profit $161.25. Max loss $1,338.75. Breakeven 74.46. Probability of profit 77.3%. Fees round trip $7.80 (entry $3.90). Sizing: 1 contract has max loss $446.25 + $2.60 fees = $448.85; floor($1,500.18 / $448.85) = 3 contracts.
```
        54                            ************************
           --------------------------*------------------------
                                   **       |                 
                                  *         |                 
                                 *          |                 
                                *           |                 
                               *            |                 
                              *             |                 
                             *              |                 
                            *               |                 
      -446 *****************                |                 
           63.00                                         85.47
           P&L ($) at expiry vs. underlying price.  | = today's price  - = $0 line
```
(Diagram is for 1 contract; the position is 3×.)
**Greeks in dollars:** delta +59.64 share-equivalents: if TLT rises $1, the position gains about $60. Theta +$3.42/day: if nothing else changes, the position gains about $3.42 per day from time decay. Vega −$15.21 per IV point. Gamma −15.9 (delta changes quickly if TLT drops toward 75).
**Concept spotlight:**
- **Delta.** Delta says how much an option's price moves per $1 move in the stock, and doubles as a rough probability the option finishes in the money. The 75 put has delta −0.2526: it gains about $0.25 if TLT falls $1 and has roughly a 25% chance of expiring in the money. We *sell* it, so we want that to stay small. Short strikes are kept at 0.16–0.30 delta.
- **Probability of profit.** The chance a position ends with any profit at expiry, derived from option prices. Here 77.3%: about 3 in 4 times this makes money — but the losing ~23% lose far more than a winner earns ($1,339 vs $161), which is why we size small and take profit at 50%.
**What would prove this wrong:** TLT falling below 75 (a bond sell-off / rate spike). Management: close at 50% of max profit ($80.63), at a loss of 2× the credit ($322.50), or at 21 DTE.
**Reproduce:** `python3 scripts/options_data.py --asof 2026-10-02 scan` · `python3 scripts/options_data.py --asof 2026-10-02 price-spread --symbol TLT --legs "SELL 1 P 75 2026-11-06; BUY 1 P 70 2026-11-06" --qty 3`
