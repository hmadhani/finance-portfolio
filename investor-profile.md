# Investor Profile

## Investor: Mr. Spock — Logical Investor

A hypothetical growth-oriented investor, still in the accumulation phase, who
will begin a gradual de-risking phase roughly 7 (fictional) years into this
portfolio's life, followed by a multi-year bridge into a more conservative
posture. Prioritizes disciplined compounding over short-term reaction; before
any position, applies a drawdown-survivability check (can this position or the
portfolio absorb a 20-30% single-day shock without forced selling?). Core
belief: diversify broadly, size concentration deliberately (both per-position
and per-theme), hold a small hedge sleeve as ballast, and never let one idea
dominate the book.

This profile contains no real names, ages, dates of birth, account data, or
calendar-year dates tied to any real person. All dates below are internal to
this portfolio's own fictional timeline, anchored to its published inception
date (2026-08-26), which was always public and is not sensitive.

## Position Sizing

| Sleeve | Target | Cap |
|---|---|---|
| Individual stocks | ~50% | 10% NAV per name |
| Sector ETFs | ~20% | 15% NAV per ETF |
| Hedge (GLD/IAU) | ~7% | 10% NAV |
| Bonds (AGG) | ~13% | — |
| Cash | ~10% | floor 10% NAV |

- Target stock position count: 15-20 concurrent positions (the 10% cap is a
  ceiling, not a target size).
- Rebalance a position when appreciation pushes it past its cap's trim band
  (see Trading Discipline rule 3); log as "rebalance," never as a thesis exit.
- Cash yield: ~4-5%/yr, SGOV-equivalent, accrued on idle cash.

## Theme Taxonomy and Concentration Cap

Every holding gets exactly one `Theme` tag from this list (extend only if a
new holding genuinely fits none of these):

- `AI-Capex` — semiconductors, hyperscale/cloud infrastructure, data-center
  power and cooling.
- `Financials` — banks, card networks, insurers, asset managers.
- `Healthcare-GLP1` — GLP-1 franchise and adjacent metabolic-health names.
- `Energy-Transition` — renewables, grid buildout, materials tied to the
  energy transition.
- `Consumer-Defensive` — staples, off-price/value retail.
- `Consumer-Discretionary` — non-defensive retail, travel, discretionary goods.
- `Materials` — packaging, industrial materials, chemicals.
- `Communication-Services` — media, ad-tech, telecom, search/cloud platforms
  when the primary thesis is communication-services-driven rather than AI-Capex.
- `Diversified-Core` — broad sector ETFs and the bond sleeve (AGG), which are
  themselves diversifying rather than thematic.

**Rule:** no single theme (summed across all positions carrying that tag,
individual stocks and sector ETFs alike) may exceed **25% of NAV**. Checked
before every new buy and every rebalance, independent of the per-position and
per-ETF caps above — a portfolio can be fully compliant on position-level caps
and still breach the theme cap.

## Trading Discipline (anti-churn, effective 2026-09-28)

The loop runs a full research pass every trading day, so these rules keep daily
re-evaluation from turning into daily trading. They apply on every cycle. When
one blocks a trade the research pass would otherwise make, log the position as
"reaffirmed — no action (blocked by Trading Discipline rule N)" so the log shows
why.

1. **Minimum hold** — no discretionary SELL, TRIM, or ADD on a position within
   20 trading days of its most recent BUY or ADD (count trading days from the
   trade-log dates). Exempt: hard exits (thesis broken; insider selling >10% of
   a single insider's holdings) and cap rebalances under rule 3.
2. **Buy-back cooldown** — do not buy a ticker within 30 calendar days of a
   full SELL of it.
3. **Trim bands** — caps are enforced with hysteresis, not at the line:
   - Theme: trim only when a theme exceeds **27% NAV**, back down to **24%**.
   - Individual stock: trim only above **11% NAV**, back down to **9%**.
   - Sector ETF: trim only above **16.5% NAV**, back down to **13.5%**.
   - Hedge: trim only above **11% NAV**, back down to **9%**.
   The 25% / 10% / 15% / 10% caps still apply at full strength to **new buys
   and adds** — never buy into a theme or position that would sit above its
   cap. The bands only govern when drift from price appreciation forces a
   trim.
4. **Minimum trade size** — skip any trade under **0.5% of NAV** (~$500 at
   inception). Hard exits (full SELL) are exempt.
5. **Something must have changed** — an ADD or TRIM on a held position needs
   new information since that position's last verdict: an earnings report or
   guidance change, an analyst rating change (a price-target tweak alone does
   not count), a ±10% price move since the last verdict, or a material
   corporate event (M&A, regulatory/FDA decision, litigation ruling,
   management change). Otherwise the verdict is "reaffirmed — no action".
   Name the change in the rationale.
6. **Trading costs** — every trade pays **5 bps slippage**: buys execute at
   quote × 1.0005, sells at quote × 0.9995. Record the execution price (not
   the quote) in the trade log, so costs flow through NAV.
7. **Weekly limit & turnover** — at most **2 new positions opened per calendar
   week** (Mon-Fri, counted from the trade log). Quarterly/annual reports
   include a turnover figure: (total buys + total sells, $) ÷ 2 ÷ average NAV
   over the period.

## Glide Path

Mr. Spock has his own fictional 10-year investment horizon starting at this
portfolio's inception (2026-08-26), fully decoupled from any real person's
retirement date.

- **Accumulation** (years 0-7 since inception, i.e. before 2033-08-26): full
  Position Sizing table above, unchanged.
- **De-risking** (years 7-10 since inception, i.e. 2033-08-26 through
  2036-08-26): linear glide — equity sleeve (stocks + sector ETFs) glides down
  from ~70% combined toward ~40% combined by the end of this window; bonds and
  cash glide up correspondingly; hedge sleeve stays flat at ~7%. Interpolate
  linearly by elapsed days within the window.
- **Bridge** (10+ years since inception, i.e. on/after 2036-08-26): target mix
  — stocks ~20%, sector ETFs ~15%, hedge ~7%, bonds ~33%, cash ~25%.

`Glide-Path Phase` is derived from **elapsed wall-clock time since the
published inception date**, not from the run-cycle count (the cycle count can
drift from wall-clock on a missed run or a future cadence change, so it is
tracked separately as an audit counter only — see `portfolio.md`'s `Cycle #`
field).

## Blended Benchmark

Primary: **70% ACWI + 13% AGG + 7% GLD + 10% cash (SGOV-equivalent)** — mirrors
this profile's actual target allocation and removes home-bias (ACWI, not
SPY-only, satisfies the "not home-biased" principle). SPY is retained as a
secondary reference line only, for the widely-recognized comparison point.

## Drawdown-Survivability Principle (qualitative only — see DECISION.md)

Before any buy, ask: "can this position or the portfolio absorb a 20-30%
single-day shock without forced selling?" This is currently a qualitative
judgment call made in each trade's written rationale, not a mechanical test —
see `DECISION.md` item 1 for the deferred mechanical version.

## Quarterly / Annual Report Template (Markdown)

Each `quarterly-reports/YYYY-Qn.md` (or `YYYY-annual.md`) contains, in order:

1. Header: period label, NAV, period return %, since-inception return %. A
   partial period (the inception quarter/year — inception was 2026-08-26,
   mid-Q3) is labeled partial with its actual date range.
2. Benchmark comparison table: this portfolio vs. blended benchmark vs. SPY.
3. Sleeve-drift table: target % vs. current % per sleeve.
4. Theme Exposure table (same shape as portfolio.md's).
5. Glide-Path Phase and Cycle # as of period end.
6. Trade-log summary for the period (count of buys/sells/rebalances/reaffirms,
   plus turnover % per Trading Discipline rule 7 and total slippage paid).
7. "Known Simplifications" section, verbatim list of DECISION.md's 3 open items.
8. The standard disclaimer paragraph.
9. A link/reference to the matching `.xlsx` in the same directory.
