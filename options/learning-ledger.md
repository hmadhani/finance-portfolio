# Options Learning Ledger

Every decision this portfolio makes — opening, adjusting, closing, or choosing
*not* to trade — is explained here for a beginner. Each entry shows the market
context, why this strategy beat the alternatives, the exact trade, what can go
wrong, and one or two new concepts. Every number can be reproduced with the
`Reproduce:` command in the entry. Sources for the concepts: `RESOURCES.md`.

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

## Entries

Newest first. Format:

    ### YYYY-MM-DD — <OPEN|ADJUST|CLOSE|PASS> <symbol> <strategy> (Cycle #N)
    **Decision:** …
    **Market context:** …
    **Why this strategy:** …
    **The trade:** legs table, max profit, max loss, breakeven(s), probability of profit, payoff diagram
    **Greeks in dollars:** …
    **Concept spotlight:** …
    **What would prove this wrong:** …
    **Reproduce:** `python3 scripts/options_data.py … --asof YYYY-MM-DD`
    (CLOSE entries add) **Outcome:** · **What drove the P&L:** · **Lesson:** · **Your reflection:** (blank)
