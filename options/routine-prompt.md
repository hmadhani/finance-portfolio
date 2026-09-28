It is ~12pm ET on the day this routine fired. Run today's cycle for the $50K defined-risk OPTIONS paper portfolio in the `finance-portfolio` repo (directory `options/`). You are also the teacher: every decision gets a beginner-level learning-ledger entry.

HARD RULES: Paper trading only. Never read or reference anything outside this repo, never any personal financial data, never the Skill tool. Only public market data (the Cboe feed via scripts/options_data.py, plus WebSearch/WebFetch for news and earnings dates). Never fabricate a number: every price, Greek, probability, max loss, and breakeven you write must come from a `scripts/options_data.py` command you ran this cycle, and the ledger entry must show that command. Never open a position that `price-spread` reports as `defined_risk: false`.

STEP 0 — Setup and trading-day check.
0a. `cd` into the repo (find it with `pwd`/`ls`). `git pull --rebase origin main`. Run `date`.
0b. NYSE holidays — 2026: Jan 1, Jan 19, Feb 16, Apr 3, May 25, Jun 19, Jul 3, Sep 7, Nov 26, Dec 25. 2027: Jan 1, Jan 18, Feb 15, Mar 26, May 31, Jun 18, Jul 5, Sep 6, Nov 25, Dec 24. Beyond these, derive from the standard NYSE calendar (weekend-observed shifts). Weekend or holiday → PushNotification "Options: market closed today (<reason>) — no cycle." and stop. Write nothing.
0c. Same-day guard: if `options/options-portfolio.md` NAV History already has a row dated today, stop silently (no writes, no notification).
0d. Data check: `python3 scripts/options_data.py regime`. If it fails (network/HTTP error), enter DEGRADED MODE: use WebSearch only to check news on open positions; close a position only if a hard risk event is clear; open NOTHING; append a NAV History row marked "(degraded — no marks)" with the prior NAV; log why; commit; PushNotification "Options: Cboe data unreachable — degraded cycle, no new trades." Then stop.

STEP 1 — Read state: `cat options/investor-profile.md options/options-portfolio.md options/data/positions.json` and the `## Concept Index` of `options/learning-ledger.md` (so you never re-explain a concept already taught — link to it instead). If the Header's Inception is "(set on first cycle)", this is cycle 1: set Inception to today and record today's BXM/PUT/VIX as the base levels.

STEP 2 — Market regime: from `regime` output, note VIX, VIX3M, contango/backwardation (stress if backwardation), VIX 1-yr percentile. Then `python3 scripts/options_data.py scan` (full universe). For each symbol note price, iv30, expected 30-day move, IV rank (or the "insufficient history" note → use VIX percentile as proxy per the profile).

STEP 3 — Manage open positions FIRST: `python3 scripts/options_data.py mark`. For each position, act on triggers per the profile's Management Rules:
- profit_target / stop_loss / 21_dte → close (or roll to 30-60 DTE if the original thesis still holds and the roll itself passes every entry rule — price the roll with `price-spread`).
- expiration / assignment → settle: expired OTM legs worthless; ITM short put of a CSP → convert to shares (positions.json leg `{"action":"BUY","ratio":1,"option":"STOCK"}`, entry_cost = strike − credit received per share, qty = contracts); spreads → close at intrinsic.
- No trigger → hold; one-line note in the Daily Decision Log (no ledger entry needed for a plain hold unless something teachable happened, e.g. a big IV move).
Closing fills: price the closing legs with `price-spread` using the opposite actions (closing a short = BUY) and use its fills; realized P&L = (closing proceeds − entry cost) × 100 × qty − round-trip fees.

STEP 4 — New entries (skip entirely in stress regime for single stocks; halve max loss everywhere in stress):
- Capacity checks from the profile: ≤ 5 new positions this calendar week (count "OPEN" ledger headings dated Mon-today), sum of max losses ≤ 25% NAV after the trade, ≤ 2 positions per underlying, CSP collateral ≤ 20% NAV.
- Pick at most 2 candidates today. For each: state the regime → strategy reasoning, choose strikes from the scan candidates (short strikes 0.16-0.30 |delta|, 30-60 DTE, liquid), WebSearch the next earnings date for single stocks (no short premium through earnings unless it is the labeled ≤1% NAV IV-crush lesson).
- Size: `qty` = floor(allowed max loss ÷ per-unit max loss from `price-spread --qty 1`), minimum 1, else skip. Re-run `price-spread` with the final qty; that output is the trade.
- Append the `position_template` to `options/data/positions.json` with a real `id` (`YYYY-MM-DD-SYMBOL-STRATEGYABBREV-N`) and `strategy` name. Cash += −entry_cost × 100 × qty − entry fees.
- If nothing qualifies, that is a valid outcome: write a PASS ledger entry explaining what was checked and why nothing met the rules.

STEP 5 — Record IV: `python3 scripts/options_data.py record-iv`.

STEP 6 — Write `options/options-portfolio.md`:
- NAV = cash + Σ (mark value_per_share × 100 × qty) over open positions. Accrue interest on cash not reserved as collateral/max loss at 4.5%/yr pro-rated since the last NAV row.
- Update Header (all fields incl. net delta/theta/vega summed from marks/analyze, capital at risk, return vs BXM and PUT since inception), Open Positions table, Closed Positions (for anything closed today), append one NAV History row (Date, Cycle #, NAV, BXM, PUT, VIX), and add today's Daily Decision Log heading `### YYYY-MM-DD — Cycle #N: <summary>` with one line per position and per new trade.
- Increment Cycle #.

STEP 7 — Write `options/learning-ledger.md` entries (newest first, under `## Entries`), one per OPEN, CLOSE, ADJUST/ROLL, assignment, and PASS, in the documented format, pitched at a beginner:
- Market context in plain words first, then the numbers.
- "Why this strategy" must name 1-2 rejected alternatives and why they lost.
- The trade: legs table (action, contracts, call/put, strike, expiry, fill), max profit, max loss, breakeven(s), probability of profit, and the `payoff_ascii` diagram in a code block.
- Greeks in dollars for THIS position (e.g. "theta +$4.10/day means that if nothing else changes, the position gains about $4 per day from time decay").
- Concept spotlight: introduce at most 2 concepts not already in the Concept Index, explain from zero with a concrete example from this trade, and add each to the Concept Index table with a link to this entry. Suggested teaching order as trades allow: premium & breakeven → delta → theta → implied volatility → vega → IV rank → expected move → probability of profit → vertical spreads → credit vs debit → the volatility risk premium → gamma & why 21 DTE → skew → assignment → rolling → term structure/calendars → iron condors → butterflies.
- What would prove this wrong.
- Reproduce: the exact `python3 scripts/options_data.py --asof YYYY-MM-DD ...` command(s).
- CLOSE entries add Outcome, What drove the P&L (price move vs time decay vs volatility change, estimated from the entry Greeks), Lesson, and `**Your reflection:**` left EMPTY — never fill it.

STEP 8 — Quarterly note (first cycle after a quarter ends, if `options/quarterly-reports/<YYYY-Qn>.md` does not exist and inception precedes the quarter end): write it with period return vs BXM and PUT, trades opened/closed, win rate, average P&L per trade, largest loss, and a "concepts learned this quarter" list from the Concept Index. The first quarter is partial — label it with its date range.

STEP 9 — Verify then commit: `python3 -c "import json;json.load(open('options/data/positions.json'))"` must succeed. `git add options/`, commit with message "Options cycle #N: <summary>" and body ending with a blank line then `Signed-off-by: hmadhani2024@gmail.com` (no Co-Authored-By). `git pull --rebase origin main` then `git push origin main`. If the push is rejected, pull --rebase again and retry once. No PRs, no gh CLI.

STEP 10 — PushNotification: "Options #N: NAV $X (±Y% vs BXM ±A%, PUT ±B%). Opened: … Closed: … New concepts: …".

If anything is ambiguous or data is missing, do NOT guess numbers — write what you know, mark the gap in the Daily Decision Log, and say so in the notification.
