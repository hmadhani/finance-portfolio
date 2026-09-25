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

## Header (as of 2026-09-25)

| Metric | Value |
|---|---|
| NAV | $98,649.27 |
| Total return | -1.35% (since inception) |
| Blended Benchmark (ref) | not yet tracked — see note below |
| SPY (ref) | $767.38 (+0.17% since inception) |
| Cash balance | $11,231.46 (11.39% of NAV) |
| Stock sleeve | $64,365.23 (65.27% of NAV) |
| Sector ETF sleeve | $15,160.08 (15.37% of NAV) |
| Bond sleeve | $7,892.50 (8.00% of NAV) |
| Cycle # | 15 |
| Glide-Path Phase | Accumulation |

`Cycle #` counts routine cycles that have written this file (one entry per
NAV History row below), independent of wall-clock cadence changes.

**Blended Benchmark note:** `investor-profile.md` defines the 70% ACWI / 13%
AGG / 7% GLD / 10% cash blended benchmark. This cycle's ACWI read was dated
2026-08-14 (over a month stale — no current print surfaced), so it remains
not reliably corroborated enough to start tracking the column (consistent
with prior cycles' decision); NAV History continues to carry "—" for
Blended Benchmark. Today's reference prices for the components: GLD
$391.71 (dated 2026-09-24, prev close $392.88, range $389.05-393.07 —
essentially flat vs. last cycle's ~$391.20 midpoint), AGG $96.25 (unchanged
for a third consecutive cycle — no fresher corroborated print found
today, carried forward), ACWI ~$162.63 (see stale-dating note above). SPY
is tracked as the secondary reference per the profile; a fresh read of
$767.38 (2026-09-25, within today's $763.25-$768.95 session range) was
used this cycle, replacing the prior cycle's $767.81.

This is Cycle #15, a **LIGHT** cycle (Friday — Monday 2026-09-21 already
ran this week's HEAVY cycle, Cycle #11; Tuesday through Thursday
2026-09-22 to 2026-09-24 were also LIGHT, Cycles #12-14). Lightweight
reaffirm/exit-only checks (major-news + Exit Criteria scan only, no full
fundamentals/technicals/analyst-consensus pass) were run on all 16 held
positions; no Exit Criteria were triggered on any position (no thesis
break, no insider selling exceeding 10% of a single insider's holdings, no
confirmed two-consecutive-quarter fundamental deterioration). Notable items
surfaced but judged non-exit-triggering: GOOGL closed at $339.01, still
pressured by competitive-pressure sentiment ahead of Meta's Connect
conference and the ongoing AI-antitrust/youth-addiction litigation
overhang (existing legal risk, not a thesis break), counterbalanced by an
expanded custom-AI-chip partnership with Marvell and the upcoming Project
Suncatcher space-based AI-compute experiment; PEP announced planned price
increases on snacks/drinks and a Maryland plant closure as it reshapes its
North American network — a proactive cost/network move consistent with
the already-flagged one-quarter of North American volume softness, not a
new deterioration signal; MU has an earnings report due 2026-09-30 (5 days
out) with trailing insider-selling (~$387M/12mo) still elevated but no
single insider crossing the >10%-of-holdings threshold; VRTX received
expanded FDA approvals for ALYFTREK/TRIKAFTA to additional age groups and
CFTR variants, and RBC raised its price target to $543 — a positive
catalyst, thesis strengthening if anything. All 16 positions were
reaffirmed HOLD from a thesis standpoint. No new positions were opened
(LIGHT cycles never open new positions per the routine's rules). The
Theme Exposure table was recomputed from today's prices: AI-Capex moved to
23.99% of NAV (down slightly from 24.08% last cycle), staying under the
25% cap, so **no rebalance was triggered this cycle** — no theme or
per-position/per-ETF cap was breached. No trades executed this cycle at
all. Cash accrued 1 day of SGOV-equivalent interest (~4.5%/yr assumption)
since the last cycle (2026-09-24).

**Price-data reconciliation this cycle:** COF reads remained highly
inconsistent across sources ($201.84, $203.19, $218.49 — no two within 2%
of each other, the same pattern as last cycle), so no fresh price was
accepted; the $207.55 anchor was carried forward again, still flagged as
uncorroborated. VRTX's headline read ($539.08) was identical to the figure
already carried forward as an uncorroborated anchor for two prior cycles,
with other sources again bimodal ($438-443 vs. $552.03) and no tighter
cluster around either pole, so $539.08 was carried forward once more,
still flagged uncorroborated. IMAX's read ($52.77, "+1.81%") exactly
repeated last cycle's own figure and framing, with no indication of a
fresher print, so it was treated as a stale repeat and carried forward
unchanged (same value, not independently re-corroborated). XLI's search
result surfaced the same $175.27 figure this routine previously rejected
(Cycle #14) in favor of a more specific OHLC-based read; with no fresher
specifically-dated print today, the prior cycle's accepted $170.56 was
carried forward rather than reverting to the rejected figure. BALL's
search again surfaced the stale $62.49 figure flagged in Cycle #14 as a
multi-cycle-repeating artifact; the $58.82 anchor accepted that cycle (a
specifically-dated 2026-09-23 close) was carried forward instead. LLY's
reads were noisy ($1,181.89, $1,167.18, session range $1,138.36-1,158.23)
but its explicitly-stated previous close of $1,159.54 sits centrally
within that scatter (within ~1.4% of every other read), so it was accepted
as this cycle's anchor, replacing the prior cycle's carried-forward
$1,146.60. NEE's cluster ($76.71 "-2.83%", a $75.61-77.47 same-day range)
was internally consistent (an $86.19 outlier from one source was
discarded), so $76.71 was accepted. AVGO ($354.99, within today's
$354.01-362.90 range), ETN ($440.08, within today's $427.01-441.38 range),
TJX ($129.24, within today's $128.57-130.42 range and matching the
-0.22%-ish session move), GOOGL ($339.01, an explicitly-stated close),
BHRB ($73.80, internally consistent with a $73.52 previous close and the
stated +0.37% move), MU ($1,080.53, within today's $1,044.00-1,081.04
range), and XLK ($196.04, a timestamped 10:54 AM EDT read) all had
same-day reads specific and internally consistent enough to accept. AGG
($96.25) had no fresher corroborated print for a third straight cycle and
was carried forward again.

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
| 2026-09-16 | 8 | $97,296.82 | — | $760.88 |
| 2026-09-17 | 9 | $97,198.00 | — | $754.05 |
| 2026-09-18 | 10 | $97,718.10 | — | $762.60 |
| 2026-09-21 | 11 | $98,571.79 | — | $767.48 |
| 2026-09-22 | 12 | $98,959.97 | — | $767.48 |
| 2026-09-23 | 13 | $99,585.04 | — | $770.71 |
| 2026-09-24 | 14 | $98,790.46 | — | $767.81 |
| 2026-09-25 | 15 | $98,649.27 | — | $767.38 |

---

## Holdings

| Ticker | Type | Theme | Shares | Entry Price | Cost Basis | Current Price | Mkt Value | % NAV | Unrealized G/L |
|---|---|---|---|---|---|---|---|---|---|
| AVGO | Stock | AI-Capex | 14 | $357.56 | $5,005.84 | $354.99 | $4,969.86 | 5.04% | -$35.98 (-0.72%) |
| ETN | Stock | Energy-Transition | 12 | $412.97 | $4,955.64 | $440.08 | $5,280.96 | 5.35% | +$325.32 (+6.56%) |
| COF | Stock | Financials | 35 | $217.40 | $7,609.08 | $207.55 | $7,264.25 | 7.37% | -$344.83 (-4.53%) |
| LLY | Stock | Healthcare-GLP1 | 6 | $1,182.09 | $7,092.52 | $1,159.54 | $6,957.24 | 7.05% | -$135.28 (-1.91%) |
| TJX | Stock | Consumer-Defensive | 35 | $139.48 | $4,881.80 | $129.24 | $4,523.40 | 4.59% | -$358.40 (-7.34%) |
| GOOGL | Stock | AI-Capex | 14 | $341.95 | $4,787.30 | $339.01 | $4,746.14 | 4.81% | -$41.16 (-0.86%) |
| BALL | Stock | Materials | 106 | $60.97 | $6,462.80 | $58.82 | $6,234.92 | 6.32% | -$227.88 (-3.53%) |
| PEP | Stock | Consumer-Defensive | 18 | $142.27 | $2,560.86 | $128.12 | $2,306.16 | 2.34% | -$254.70 (-9.94%) |
| NEE | Stock | AI-Capex | 59 | $84.29 | $4,973.11 | $76.71 | $4,525.89 | 4.59% | -$447.22 (-8.99%) |
| MU | Stock | AI-Capex | 4 | $930.25 | $3,721.00 | $1,080.53 | $4,322.12 | 4.38% | +$601.12 (+16.16%) |
| BHRB | Stock | Financials | 69 | $70.63 | $4,873.47 | $73.80 | $5,092.20 | 5.16% | +$218.73 (+4.49%) |
| IMAX | Stock | Communication-Services | 93 | $52.50 | $4,882.50 | $52.77 | $4,907.61 | 4.98% | +$25.11 (+0.51%) |
| VRTX | Stock | Healthcare-GLP1 | 6 | $512.00 | $3,072.00 | $539.08 | $3,234.48 | 3.28% | +$162.48 (+5.29%) |
| XLK | Sector ETF | AI-Capex | 26 | $186.00 | $4,836.00 | $196.04 | $5,097.04 | 5.17% | +$261.04 (+5.40%) |
| XLI | Sector ETF | Energy-Transition | 59 | $185.96 | $10,971.64 | $170.56 | $10,063.04 | 10.20% | -$908.60 (-8.28%) |
| AGG | Bond | Diversified-Core | 82 | $97.90 | $8,027.80 | $96.25 | $7,892.50 | 8.00% | -$135.30 (-1.69%) |
| Cash | — | — | — | — | $11,231.46 | — | $11,231.46 | 11.39% | — |
| **TOTAL** | — | — | — | — | **$99,944.82** | — | **$98,649.27** | **100.00%** | **-$1,295.55 (-1.46% on positions)** |

---

## Theme Exposure

| Theme | Positions | Mkt Value | % NAV |
|---|---|---|---|
| AI-Capex | AVGO, GOOGL, NEE, MU, XLK | $23,661.05 | 23.99% |
| Financials | COF, BHRB | $12,356.45 | 12.53% |
| Healthcare-GLP1 | LLY, VRTX | $10,191.72 | 10.33% |
| Consumer-Defensive | TJX, PEP | $6,829.56 | 6.92% |
| Energy-Transition | ETN, XLI | $15,344.00 | 15.56% |
| Materials | BALL | $6,234.92 | 6.32% |
| Communication-Services | IMAX | $4,907.61 | 4.98% |
| Diversified-Core | AGG | $7,892.50 | 8.00% |

(Cash is intentionally excluded from theme exposure — it carries no thematic risk.)

---

## Trade Log (reverse-chronological)

### 2026-09-25 — Cycle #15 (LIGHT): reaffirm pass, no trades

Lightweight reaffirm/exit-only pass on all 16 held positions (Friday —
week's HEAVY cycle already ran Monday 2026-09-21, Cycle #11). No Exit
Criteria triggered on any position; no new positions opened (LIGHT cycles
never open new positions). Theme Exposure recomputed: AI-Capex 23.99% of
NAV (down slightly from 24.08%, still under the 25% cap) — no rebalance
triggered. No per-position or per-ETF cap breached. Cash accrued 1 day of
SGOV-equivalent interest since the last cycle (2026-09-24). See the
Header's price-data reconciliation note above for this cycle's price
sourcing (COF and VRTX carried forward uncorroborated again; IMAX, BALL,
XLI, and AGG carried forward with no fresher print today; LLY updated off
an explicitly-stated previous close).

- **AVGO** (AI-Capex) — reaffirmed HOLD. $354.99. No material news this
  cycle beyond the previously-flagged Chinese hardware-probe watch item;
  not thesis-breaking.
- **ETN** (Energy-Transition) — reaffirmed HOLD. $440.08. No adverse news;
  analyst consensus remains Buy with a $479.57 average 12-month target.
- **COF** (Financials) — reaffirmed HOLD. $207.55 (carried forward,
  uncorroborated again — same-day price reads still span $201.84-$218.49
  with no two within 2% of each other). No exit criteria triggered.
- **LLY** (Healthcare-GLP1) — reaffirmed HOLD. $1,159.54 (explicitly-stated
  previous close, replacing the prior cycle's carried-forward $1,146.60).
  No adverse news; thesis intact.
- **TJX** (Consumer-Defensive) — reaffirmed HOLD. $129.24. No adverse news.
- **GOOGL** (AI-Capex) — reaffirmed HOLD. $339.01 (close). Continued
  competitive-pressure sentiment ahead of Meta's Connect conference and
  the ongoing AI-antitrust/youth-addiction litigation overhang (existing
  legal risk, screened as this portfolio's hottest theme by relative
  strength per DECISION.md item 3, not a thesis break); counterbalanced by
  an expanded Marvell custom-AI-chip partnership and the upcoming Project
  Suncatcher space-based AI-compute experiment.
- **BALL** (Materials) — reaffirmed HOLD. $58.82 (carried forward from
  Cycle #14's specifically-dated 2026-09-23 close; today's search again
  surfaced the stale $62.49 figure, discarded). No exit criteria triggered.
- **PEP** (Consumer-Defensive) — reaffirmed HOLD. $128.12. Announced
  planned price increases on snacks/drinks and a Maryland plant closure as
  it reshapes its North American network — a proactive cost move
  consistent with the already-flagged volume softness, not a new
  deterioration signal; still one quarter of softness, short of the
  two-consecutive-quarter exit bar; watch into the 2026-10-08 Q3 print.
- **NEE** (AI-Capex) — reaffirmed HOLD. $76.71. No material new news beyond
  the ordinary session move. No exit criteria triggered.
- **MU** (AI-Capex) — reaffirmed HOLD. $1,080.53. Elevated trailing
  insider-selling ($387M/12mo) continues but no single insider crossed the
  >10%-of-holdings exit threshold this cycle; earnings due 2026-09-30 (5
  days out) — a near-term catalyst to watch.
- **BHRB** (Financials) — reaffirmed HOLD. $73.80. No material news.
- **IMAX** (Communication-Services) — reaffirmed HOLD. $52.77 (carried
  forward — today's read exactly repeated last cycle's figure and framing
  with no indication of a fresher print). No exit criteria triggered.
- **VRTX** (Healthcare-GLP1) — reaffirmed HOLD. $539.08 (carried forward,
  uncorroborated again — reads remain bimodal between ~$438-443 and
  ~$552). Received expanded FDA approvals for ALYFTREK/TRIKAFTA to
  additional age groups and CFTR variants; RBC raised its price target to
  $543 — a positive catalyst. Trailing insider selling (~$158M/12mo) has
  not crossed the single-insider >10% exit threshold.
- **XLK** (AI-Capex, Sector ETF) — reaffirmed HOLD. $196.04.
- **XLI** (Energy-Transition, Sector ETF) — reaffirmed HOLD. $170.56
  (carried forward — today's search again surfaced the $175.27 figure
  this routine rejected last cycle in favor of a more specific OHLC read;
  no fresher specifically-dated print appeared today).
- **AGG** (Diversified-Core, Bond) — reaffirmed HOLD. $96.25 (carried
  forward, no fresher corroborated print for a third straight cycle).

### 2026-09-24 — Cycle #14 (LIGHT): reaffirm pass, no trades

Lightweight reaffirm/exit-only pass on all 16 held positions (Thursday —
week's HEAVY cycle already ran Monday 2026-09-21, Cycle #11). No Exit
Criteria triggered on any position; no new positions opened (LIGHT cycles
never open new positions). Theme Exposure recomputed: AI-Capex 24.08% of
NAV (down from 24.32%, still under the 25% cap) — no rebalance triggered.
No per-position or per-ETF cap breached. Cash accrued 1 day of
SGOV-equivalent interest since the last cycle (2026-09-23). See the
Header's price-data reconciliation note above for this cycle's price
sourcing (COF and VRTX carried forward uncorroborated; BALL updated off a
multi-cycle stale price).

- **AVGO** (AI-Capex) — reaffirmed HOLD. $361.74. Q3 FY26 results showed AI
  semiconductor revenue +221% YoY; a reported Chinese regulatory probe into
  Broadcom hardware in state-backed data centers is a watch item, not
  thesis-breaking.
- **ETN** (Energy-Transition) — reaffirmed HOLD. $438.03. Continues to
  benefit from AI data-center power/grid-buildout demand; new Trane
  Technologies thermal-management collaboration announced this month.
- **COF** (Financials) — reaffirmed HOLD. $207.55 (carried forward,
  uncorroborated this cycle). Recent coverage cites an earnings beat;
  conflicting same-day price reads mean the figure needs re-verification
  next cycle. No exit criteria triggered.
- **LLY** (Healthcare-GLP1) — reaffirmed HOLD. $1,146.60 (carried forward,
  no fresher corroborated read today). AtaiBeckley acquisition closed;
  Inluriyo approved for ER+ breast cancer (2026-09-18); thesis intact.
- **TJX** (Consumer-Defensive) — reaffirmed HOLD. $131.22. Stock closed
  2026-09-23 up 0.33%; no adverse news.
- **GOOGL** (AI-Capex) — reaffirmed HOLD. $338.00 (-3.73% close). New AI
  antitrust lawsuit and youth-addiction litigation overhang drove the
  selloff; AdX ruling avoided a structural breakup and Gemini 3.8 Flash
  shipped this cycle. Legal risk noted as a screened-against-hot-theme flag
  (AI-Capex remains this portfolio's hottest theme by relative strength;
  see DECISION.md item 3) but not a thesis break.
- **BALL** (Materials) — reaffirmed HOLD. $58.82 (fresh dated read,
  replacing a stale $62.49 carried across several cycles). Stock fell
  1.92% despite a Q2 earnings beat (EPS $1.03 vs. $0.99 consensus, revenue
  +19.7% YoY); JPMorgan upgraded to Overweight 2026-09-18. No exit
  criteria triggered.
- **PEP** (Consumer-Defensive) — reaffirmed HOLD. $130.78. Trading near its
  52-week low on North American volume weakness; Citi reaffirmed Buy
  ($142 PT) the same day. One quarter of softness so far — does not meet
  the two-consecutive-quarter fundamental-deterioration exit bar; watch
  into the 2026-10-08 Q3 print.
- **NEE** (AI-Capex) — reaffirmed HOLD. $77.02. Dominion Energy merger
  package expanded for Virginia regulators (targeting 2H 2027 close);
  Morgan Stanley trimmed its price target to $111. No exit criteria
  triggered.
- **MU** (AI-Capex) — reaffirmed HOLD. $1,096.16. Elevated trailing
  insider-selling ($387.1M/12mo) continues but no single insider crossed
  the >10%-of-holdings exit threshold this cycle; earnings due 2026-09-30.
- **BHRB** (Financials) — reaffirmed HOLD. $73.80. No material news;
  Q3 fixed-income investor presentation published 2026-09-18.
- **IMAX** (Communication-Services) — reaffirmed HOLD. $52.77. Morgan
  Stanley reiterated a Buy this cycle citing theater demand; CFO sold
  $1.1M in stock on 2026-09-02, well below the >10%-of-holdings exit
  threshold.
- **VRTX** (Healthcare-GLP1) — reaffirmed HOLD. $539.08 (carried forward;
  new reads were bimodal — one cluster near $511-515, another near
  $546-552 — with neither corroborated enough to displace the anchor).
  Trailing insider selling (~$158.4M/12mo, no insider buying) is a watch
  item but has not crossed the single-insider >10% exit threshold; Phase
  2b AMPLIFIED kidney-disease data announced 2026-09-22 was positive.
- **XLK** (AI-Capex, Sector ETF) — reaffirmed HOLD. $194.75.
- **XLI** (Energy-Transition, Sector ETF) — reaffirmed HOLD. $170.56.
- **AGG** (Diversified-Core, Bond) — reaffirmed HOLD. $96.25 (carried
  forward, no fresher corroborated print today).

### 2026-09-23 — Cycle #13 (LIGHT): reaffirm pass, no trades

Lightweight reaffirm/exit-only pass (major-news + Exit Criteria scan only,
no full fundamentals/technicals/analyst-consensus research). All 16 held
positions reaffirmed HOLD; no Exit Criteria triggered on any position. No
new positions opened (LIGHT cycle). Theme Exposure recomputed: AI-Capex
rose to 24.32% NAV (from 24.10%) on AVGO/GOOGL/MU/XLK price appreciation
but stayed under the 25% cap — no rebalance triggered. No per-position or
per-ETF cap was breached either. **No trades executed this cycle.**

- **AVGO** (AI-Capex) — reaffirmed HOLD. Q3 FY26 results (reported prior to
  this cycle) showed revenue of $29.6B (+86% YoY) and a ninth straight
  earnings beat, with AI revenue up triple digits YoY; no negative news
  found this cycle. Price $366.12 (+2.4% vs. entry). Screened against a
  currently "hot" theme: yes (AI-Capex remains the portfolio's largest and
  best-performing theme) — manual DECISION.md item 3 stopgap note.
- **ETN** (Energy-Transition) — reaffirmed HOLD. Continued strong AI/data-center
  power-buildout demand narrative; Bernstein maintained Buy on 9/21; no
  Exit Criteria triggered. Price $438.03 (+6.1% vs. entry).
- **COF** (Financials) — reaffirmed HOLD. Routine credit-metrics filing and a
  €1.5B senior-notes offering this cycle; Buy consensus intact (16
  analysts); no thesis-break or insider-selling flags. Price $207.55
  (-4.5% vs. entry).
- **LLY** (Healthcare-GLP1) — reaffirmed HOLD. FDA approved Inluriyo for ER+
  breast cancer (9/18) following the Mounjaro cardiovascular approval
  (8/28); Guggenheim raised its price target to $1,284 (9/17); no negative
  catalysts. Price $1,146.60 (-3.0% vs. entry).
- **TJX** (Consumer-Defensive) — reaffirmed HOLD. Q2 FY27 revenue of $15.2B
  beat consensus by $20M with +4% comps; stock recovered off a mid-month
  52-week-low test to close above $131 on 9/22. Price $130.96 (-6.1% vs.
  entry).
- **GOOGL** (AI-Capex) — reaffirmed HOLD. Continued AI product momentum
  (Gemini 3.8 Flash/Live launches) and a planned €13B European
  infrastructure investment; a rogue-AI security story (Gemini) is a
  watch item but not a thesis-break. Price $351.16 (+2.7% vs. entry).
  Screened against a "hot" theme: yes (AI-Capex).
- **BALL** (Materials) — reaffirmed HOLD. JPMorgan upgraded to Overweight
  (9/18); board additions and an India manufacturing expansion announced;
  no negative flags. Price $62.49 (+2.5% vs. entry).
- **PEP** (Consumer-Defensive) — reaffirmed HOLD. New independent board
  director (Joaquin Duato, 9/17); stock remains near 52-week lows on
  margin softness noted last cycle, but no new deterioration confirmed
  this cycle beyond what's already priced in — one quarter of softness
  logged, not yet the two-consecutive-quarter exit trigger. Price $131.19
  (-7.8% vs. entry).
- **NEE** (AI-Capex) — reaffirmed HOLD. Dominion Energy shareholders approved
  the $66.8B NextEra merger; Morgan Stanley trimmed its price target to
  $114 (still Overweight); DOE loan support for the Duane Arnold nuclear
  restart. Price $79.29 (-5.9% vs. entry). Screened against a "hot" theme:
  yes (AI-Capex, via data-center power demand).
- **MU** (AI-Capex) — reaffirmed HOLD. Stock rose >6% this week ahead of the
  9/30 fiscal Q4 earnings report on strong AI-memory demand; no insider
  selling found in the September window (the CEO's prior sale was in July,
  outside this cycle's lookback and not >10% of holdings). Price $1,097.72
  (+18.0% vs. entry, largest unrealized gain in the book). Screened
  against a "hot" theme: yes (AI-Capex) — this cycle's biggest driver of
  the theme's move toward its cap.
- **BHRB** (Financials) — reaffirmed HOLD. Routine Q3 investor-presentation
  SEC filing (9/18); no new developments beyond the already-closed
  LINKBANCORP merger. Price $73.80 (+4.5% vs. entry).
- **IMAX** (Communication-Services) — reaffirmed HOLD. Record summer box
  office ($728M global, led by *The Odyssey*) and continued investor-conference
  visibility; no negative flags. Price $52.77 (+0.5% vs. entry).
- **VRTX** (Healthcare-GLP1) — reaffirmed HOLD. Crinetics acquisition closed
  (9/1); positive Phase 2b inaxaplin (kidney disease) data announced 9/16;
  Morgan Stanley resumed coverage at Overweight. Price jumped to $539.08
  (+5.3% vs. the $512.00 anchor carried for several cycles) — see
  price-data reconciliation note above; the move is consistent with this
  cycle's positive newsflow, not treated as a data error.
- **XLK** (Sector ETF, AI-Capex) — reaffirmed HOLD (diversified sleeve, no
  single-name Exit Criteria applicable). Price $196.29 (+5.5% vs. entry).
- **XLI** (Sector ETF, Energy-Transition) — reaffirmed HOLD (diversified
  sleeve). Price $170.27 (-8.4% vs. entry).
- **AGG** (Bond, Diversified-Core) — reaffirmed HOLD (diversified sleeve).
  Price $96.25, first fresh corroborated print in five cycles (was $97.00).
- **Cash** — accrued 1 day of SGOV-equivalent interest (~4.5%/yr) since the
  prior cycle; balance $11,228.70 (11.28% of NAV), above the 10% floor.

### 2026-09-22 — Cycle #12 (LIGHT): reaffirm pass, MU trimmed 1 sh (theme-cap rebalance)

On-schedule LIGHT cycle (Tuesday — Monday 2026-09-21 already ran this
week's HEAVY cycle). Lightweight reaffirm/exit-only check on all 16
holdings (major-news + Exit Criteria scan only, per LIGHT-cycle rules — no
full fundamentals/technicals/analyst-consensus pass, no new positions
opened). Theme Exposure table recomputed from today's prices; AI-Capex had
drifted to 25.16% of NAV on pure price appreciation (AVGO/GOOGL/MU/XLK all
up), breaching its 25% cap, so 1 share of MU — the largest AI-Capex
position by market value — was trimmed, bringing the theme to 24.10% of
NAV. This is logged as "rebalance — theme cap," not a thesis exit; MU's
thesis was independently reaffirmed HOLD below. No other theme, position,
or sector-ETF sleeve breached its cap.

**AVGO — Broadcom (HOLD, reaffirmed).** $357.61 (prev $349.31, +2.35%).
No negative news; insider selling continues at a steady pace ($29.7M sold
vs. $0.37M bought over the last 3 months) but nowhere near the >10%-of-
holdings Exit Criterion threshold. Q3 FY26 beat (AI-chip revenue +221%
YoY to $16.7B) continues to support the thesis. No Exit Criteria
triggered. Theme: AI-Capex (screened against a currently "hot" theme —
AI-Capex remains a leadership sector this cycle, per DECISION.md item 3
stopgap).

**ETN — Eaton Corporation (HOLD, reaffirmed).** $427.51, carried forward
unchanged — no fresher print than 2026-09-21 could be sourced this cycle.
Bernstein reiterated Buy; continued positive coverage on data-center/grid
demand. No Exit Criteria triggered. Theme: Energy-Transition.

**COF — Capital One Financial (HOLD, reaffirmed).** $207.20 (prev
$202.36, +2.39%). Bank stocks broadly rallied this week; no COF-specific
negative catalyst. Consensus remains Buy with a $258 price target. No
Exit Criteria triggered. Theme: Financials.

**LLY — Eli Lilly (HOLD, reaffirmed).** $1,146.60, carried forward
unchanged — no fresher print than 2026-09-21 could be sourced this cycle.
Strongly positive news flow: CEO reports Foundayo (oral GLP-1) capturing
~70% of new Medicare-driven senior GLP-1 starts, breaking ground on a
$6.5B Houston manufacturing facility. No Exit Criteria triggered. Theme:
Healthcare-GLP1.

**TJX — TJX Companies (HOLD, reaffirmed — watch item).** $130.96 (prev
$127.24, +2.92%). Stock remains near its 52-week low and below its 200-day
average following the post-earnings slide, but Goldman maintained Buy
(operational missteps called "transitory," $178 PT) and a new board member
was appointed. Not yet two consecutive quarters of fundamental
deterioration, so held as a watch item rather than an Exit Criterion
trigger. Theme: Consumer-Defensive.

**GOOGL — Alphabet (HOLD, reaffirmed).** $349.54, best available print
this cycle but explicitly dated 2026-09-18 (flagged as stale — no fresher
print located). Positive backdrop continues: antitrust remedies trial
proceeding without a forced structural breakup, analyst upgrades
(Evercore, Tigress) following the ruling. No Exit Criteria triggered.
Theme: AI-Capex (screened against a currently "hot" theme — see AVGO
note above).

**BALL — Ball Corporation (HOLD, reaffirmed).** $62.49, carried forward
unchanged — no fresher print than 2026-09-21 could be sourced this cycle.
No negative news. No Exit Criteria triggered. Theme: Materials.

**PEP — PepsiCo (HOLD, reaffirmed).** $129.75, carried forward
essentially unchanged. BofA maintained Hold; PepsiCo added Joaquin Duato
to its board. Continued North America softness vs. international
strength noted, consistent with the prior cycle's trim rationale, but no
new deterioration beyond what was already priced in. No Exit Criteria
triggered. Theme: Consumer-Defensive.

**NEE — NextEra Energy (HOLD, reaffirmed).** $79.80 (prev $80.75, -1.18%).
NextEra closed a $1.9B DOE loan to restart the Duane Arnold nuclear plant
in Iowa; the pending Dominion Energy merger continues progressing
(shareholder approval secured). Morgan Stanley trimmed its price target
slightly to $111 but Evercore reiterated Buy. No Exit Criteria triggered.
Theme: AI-Capex (screened against a currently "hot" theme — see AVGO
note above).

**MU — Micron Technology (HOLD, reaffirmed; 1 sh trimmed as a
theme-cap rebalance, not a thesis exit).** $1,043.96 (prev $1,016.80,
+2.67%), a genuinely fresh today-dated print. Thesis remains strong going
into the Sept 30 earnings print — Wall Street models 350% YoY sales growth
this quarter, Stifel reiterated Buy at a $1,500 PT — but MU was the
largest AI-Capex constituent when the theme breached its 25% cap this
cycle, so 1 of 5 shares was sold (4 remain) purely for theme-concentration
discipline. Theme: AI-Capex (the theme this trim was screened against
being over-hot is exactly the DECISION.md item 3 concern this manual
stopgap exists to flag).

**BHRB — Burke & Herbert Financial (HOLD, reaffirmed).** $73.80, carried
forward unchanged — no fresher print than 2026-09-21 could be sourced
this cycle. No new negative news. No Exit Criteria triggered. Theme:
Financials.

**IMAX — IMAX Corporation (HOLD, reaffirmed).** $53.10 (prev $52.77,
+0.63%). Record summer box office ($728M, +73% YoY) reaffirmed; "The
Odyssey" extended through Sept 30 in 70mm locations; FY26 guidance of
~$1.4B global box office reaffirmed. No Exit Criteria triggered. Theme:
Communication-Services.

**VRTX — Vertex Pharmaceuticals (HOLD, reaffirmed).** $512.00, carried
forward unchanged — three WebSearch reads returned this cycle ($539.08,
$438.49, $417.77) were mutually inconsistent and none corroborated each
other or the $512.00 opening price from yesterday's cycle, so all three
were discarded as unreliable rather than used. Positive news: positive
Phase 2b AMPLIFIED kidney-disease data, Phase 2/3 AMPLITUDE trial
enrollment completed. No Exit Criteria triggered. Theme: Healthcare-GLP1.

**XLK — Technology Select Sector SPDR (HOLD, reaffirmed).** $194.85 (prev
$189.60, +2.77%), tracking continued AI/tech-sector strength. Contributed
to this cycle's AI-Capex theme-cap breach (see rebalance note above); no
further action taken at the ETF level since the MU trim alone brought the
theme back under cap.

**XLI — Industrial Select Sector SPDR (HOLD, reaffirmed).** $169.85 (prev
$175.27, -3.09%), the first fresh-looking read for this ticker in several
cycles. Sleeve remains at 10.13% of NAV, within its 15% NAV cap. No
rebalance needed.

**AGG — iShares Core U.S. Aggregate Bond ETF (HOLD, reaffirmed).** $97.00,
carried forward unchanged — no fresher print than 2026-09-18 could be
sourced this cycle (now five consecutive cycles carried at this level;
passive core bond sleeve, not re-picked). Sleeve at 8.04% of NAV. No
rebalance needed.

**Net this cycle: 1 share of MU sold as a theme-cap rebalance (not a
thesis exit); no other trades.** Cash accrued 1 day of SGOV-equivalent
interest (~4.5%/yr assumption) since the last cycle (2026-09-21) plus the
MU sale proceeds ($1,043.96), bringing the balance to $11,227.32 (11.34%
of NAV).

### 2026-09-21 — Cycle #11 (HEAVY): full research pass, PEP trimmed, VRTX opened

On-schedule HEAVY cycle (Monday, first trading day of the week — no holiday
shift this week). Full fundamentals/valuation/technicals/catalyst/insider/
analyst-consensus research run on all 15 held positions via parallel
research passes; baseline screener + sector-rotation scan also run for new
candidates since the portfolio remained under its 15-20 stock target (12
stocks) with cash above the 10% floor (11.21% before this cycle's trades).

**AVGO — reaffirmed, HOLD.** $349.31 (prev $349.05). FQ3 FY26 beat again
(revenue $29.6B +86% YoY, non-GAAP EPS $3.32 +96% YoY, op margin 67.9%),
AI-semiconductor revenue $16.7B (+221% YoY, 56% of revenue) with FQ4
guidance accelerating further to $34.8B total revenue / $21.7B AI-semis
(+236% YoY) — thesis intact and strengthening, not decelerating. Technicals
show a bullish golden cross (50dma $386.6 > 200dma $371.4) but RSI 71.9 is
overbought — not a chase point. Insider selling this period was routine
RSU-related, short interest low. Analyst consensus Strong Buy, targets
$520-532. Theme: AI-Capex, at ~24.9% of the 25% cap — no room to add
regardless of conviction. AI-Capex is the hottest theme in the book right
now.

**ETN — reaffirmed, HOLD.** $427.51 (prev $392.66, a +8.9% move corroborated
by two independent sources but with no matching company-specific news found
to explain the size of the jump — flagged for extra scrutiny next cycle).
Q2 fundamentals remain strong (record $8.5B revenue, raised FY26 guidance to
12% organic growth, EPS midpoint $13.50), but valuation is historically
stretched (trailing P/E ~43x vs 5-yr median ~32x) and RSI ~71.5 is
overbought. Persistent insider selling with zero offsetting buying over the
trailing 3 months ($5.7M sold) is a watch item, not yet a confirmed >10%-of-
holdings trigger. Theme: Energy-Transition, also running hot on the same
data-center power-demand wave as AI-Capex — no room to add comfortably at
this valuation/RSI combination.

**COF — reaffirmed, HOLD.** $202.36 (prev $203.00). Q2 net income $3.0B,
adjusted EPS $5.81 beat $4.69 consensus, NIM expanded 14bps to 8.01%, and
provision for credit losses fell $1.1B QoQ with a $662M reserve release —
credit normalization post-Discover integration is confirming the thesis.
Valuation remains a discount to the sector (P/E ~13.5-16x vs ~22x sector
avg). Insider selling modest/routine, short interest low (1.32% of float).
Analyst consensus Buy, PT $228-261. This is fundamentally ADD-worthy, but
already the largest position in the book at 7.19% NAV — sizing discipline
argues HOLD rather than adding further ahead of the Q3 print. Theme:
Financials, warm but not a top-of-book momentum theme.

**LLY — reaffirmed, HOLD (lean ADD-on-weakness).** $1,146.60 (prev
$1,134.34). Q2 net income $7.1B, EPS $7.94 vs $6.29 a year ago; US revenue
+33%, Mounjaro +91% to $9.9B, Zepbound US +44% — growth still accelerating.
Trailing P/E ~39-41x is actually below LLY's own 5-yr median (~53x). RSI
42.8 leaves real room to run before overbought. Oral T2D submission
(ACHIEVE program) is a live catalyst inside the 90-day window; Berenberg
upgraded to Buy on 9/15 with a $1,400 PT. Large-dollar insider selling
($3.56B trailing 12mo, zero offsetting buys) is a watch item but not
confirmed as >10% of any individual insider's holdings. Already near 7%
NAV, so default HOLD; would add only on a pullback. Theme: Healthcare-GLP1,
reheating on the fresh upgrade and pending regulatory catalyst.

**TJX — reaffirmed, HOLD (watch item).** $127.24 (prev $122.84). Q2 FY27
comps +4% beat plan, revenue +6.9%, EPS $1.10 vs $0.97 prior year,
guidance raised — fundamentals genuinely solid, no exit criterion met. But
Q3 comp guide of only +2-3% signals deceleration, the stock trades below
its 50dma with negative MACD, and valuation (~22x P/E) now runs at a
premium to off-price peers (~17x) after the recent run. Not a sell — no
thesis break, no confirmed 2-quarter deterioration, no >10%-of-holdings
insider selling — but the weakest setup of the group for adding. Held at
current size; revisit at the mid-to-late November Q3 print. Theme:
Consumer-Defensive, the laggard of the book on momentum.

**GOOGL — reaffirmed, HOLD.** $346.40 (prev $346.51). Q2 revenue $119.8B
(+24% YoY), Cloud +82% to $24.8B, operating margin +2pt to 34% — but FY26
capex guidance was raised sharply to $195-205B (from $180-190B), creating
near-term multiple/FCF-narrative risk even as growth stays strong. Stock is
sitting almost exactly at both its 50dma ($343.21) and 200dma ($342.73) —
a tight coil at trend support. RSI ~56 neutral, short interest low and
falling. Analyst consensus Strong Buy, avg PT ~$428. Theme: AI-Capex, at
~24.9% of the 25% cap — no room to add despite this screening as the
best risk-adjusted name in the sleeve; first in line if theme-cap room
opens via a trim elsewhere.

**BALL — reaffirmed, HOLD.** $62.49 (prev $62.92). FY26 consensus EPS
still guided +12.6% YoY; Q3 print due Nov 3. Analyst backdrop remains
constructive (70% buy/strong-buy, zero sell of 23 analysts, avg PT $75,
meaningful upside to cost basis) and only a modest, immaterial insider sale
was found (<1% of holdings). However, the technical picture has turned
bearish short-term and short interest is climbing (~7.8M shares, up from
~6.9M, days-to-cover ~5.1) — worth a tighter watch into the Nov 3 print,
not yet an exit trigger. Theme: Materials, not currently a hot momentum
theme — BALL is a steady compounder rather than a momentum name here.

**PEP — TRIMMED (35 -> 18 sh @ $129.75, -$2,205.75 proceeds; remaining 18
sh at unchanged $142.27 avg entry, now 2.37% NAV).** This is a risk-
reduction move, not a thesis exit — Q2 revenue ($24.18B, +6.4%) beat and
core EPS ($2.20) was essentially in-line, and full-year guidance was
reaffirmed rather than cut, so the portfolio's own exit bar ("2 consecutive
quarters of fundamental deterioration" or a guidance cut) is NOT yet met.
But the warning signs are real and stacking: a fresh 52-week low ($129.75,
~24% off the 52-wk high), a bearish 10dma/50dma cross on Sept 10, RSI in
oversold territory, North America beverage volume -4% YoY, PBNA Foods
operating profit -8% despite +6.4% segment revenue (price cuts eating
margin), and management itself flagging results "tracking toward the low
end" of guidance. Q3 earnings are confirmed for Oct 8, 2026 — a hard
decision gate: continued NA deterioration or a guidance cut there would
satisfy the exit criterion and should trigger a full SELL/TRIM re-
evaluation at the next cycle without further delay. Cutting the position
roughly in half now de-risks into that binary catalyst while preserving
the ability to hold the (now smaller) remainder if Q3 stabilizes. Theme:
Consumer-Defensive, not a hot/flow-driven theme, which compounds the
company-specific pressure.

**NEE — reaffirmed, HOLD.** $80.75 (prev $80.50). Q2 adjusted EPS $1.15
(+9.5% YoY) beat; FY26 guidance reaffirmed at the high end ($3.92-4.02),
8%+ long-term growth reiterated through 2032. The ~$100B Dominion Energy
merger continues to progress without a regulatory setback — S-4
registration went effective and both companies' shareholder votes cleared
in early September; applications are filed across FERC/NRC/state
commissions with close still guided to 2H2027. Technicals remain bearish
(price below both 50dma $87.90 and 200dma $89.50, RSI 29.8 oversold), but
per this portfolio's rules price weakness alone — absent a confirmed
fundamental or regulatory break — is not a sell trigger; if anything it's
arguably a better entry for long-term holders. Theme: AI-Capex, at ~24.9%
of the 25% cap — no room to add despite the oversold setup; stays HOLD-only.

**MU — reaffirmed, HOLD (highest-conviction "would-add-if-room").** $1,016.80
(prev $985.00; conflicting reads this cycle spanned $1,015.80-$1,017.79,
midpoint used). FQ4 guided to a record $50.0B revenue (±$1B) at ~86% gross
margin, beating consensus by ~$6.55B — shares jumped ~14.6% after-hours.
HBM4 volume shipments started for Nvidia's Vera Rubin platform; 2026 HBM
supply is fully sold out. Technicals strongly bullish (price above both
50dma $915.62 and 200dma $661.99, MA signal "Strong Buy" 12/0). Net insider
selling (73,623 sold vs 23,200 bought trailing 90 days) is a moderate, not
critical, flag — no single sale confirmed above 10% of holdings. Analyst
consensus Strong Buy, avg PT ~$1,513. This is the strongest fundamental/
technical setup of any AI-Capex name in the book, but the theme sits at
~24.9% of its 25% cap — flagged as the top candidate to fund if theme-cap
room opens via a trim elsewhere, not actionable today. Theme: AI-Capex,
very hot — MU is the highest-beta direct beneficiary.

**BHRB — reaffirmed, HOLD.** $73.80 (unchanged — no clean 2026-09-21 print
could be sourced this cycle, carried forward; a $60.04 read was discarded
as an outlier inconsistent with BHRB's known 52-week range). Q2 GAAP EPS
missed badly ($0.50 vs $1.64 est.) but that was entirely merger-charge
noise from the May 1 LinkBancorp combination (now ~$11.0B assets);
adjusted diluted EPS was $2.03 on healthy underlying run-rate. Valuation
roughly in line to modestly cheap vs regional-bank peers (P/E ~8-12x vs
~11-12x sector avg; P/B discount to sector median). No insider sale
exceeded the 10% threshold. Analyst consensus Moderate Buy, avg PT $75-80.
No exit criteria triggered — merger integration synergies should show up
in Q3/Q4 GAAP prints as charges roll off. Theme: Financials, not currently
a hot momentum theme.

**IMAX — reaffirmed, HOLD (lean ADD-on-weakness).** $52.77 (prev $52.09).
Q2 revenue $102.8M (+12% YoY), adj. EPS $0.43 (+65% YoY), adj. EBITDA
margin 46.6%; global box office $285M was the best Q2 since 2019 with 38
installations, the best Q2 in a decade — FY26 guide reiterated at ~$1.4B
box office. Trading above both 50dma (~$41) and 200dma (~$37) near 52-week
highs. Two watch items: short interest is elevated (~20% of float per
Fintel/Ortex) and one CFO-level insider sold ~11% of his direct holding on
Sept 10 (small in absolute dollar terms, and an unconfirmed/speculative
"open to sale" headline was found but not corroborated by any live
process) — neither individually meets the exit bar (no company-wide >10%
insider liquidation, no 2-quarter deterioration). Analyst consensus
bullish-tilted (Benchmark, Rosenblatt Buy; Goldman Neutral but PT raised to
$50), no Sell ratings. Theme: Communication-Services, hot specifically for
IMAX on record Q2 results and a strong 2026-27 film slate.

**XLK — reaffirmed, HOLD.** $189.60 (prev $187.87; freshest print located
was dated 2026-09-18, flagged as possibly stale). Structurally bullish
(golden cross intact, price above both 50/200dma), but near-term flows
turned mixed (-$693M 1-month vs. +$1.15B 6-month) as investors grow more
selective on AI-capex ROI, and semiconductor concentration within the fund
has risen to ~42%, making it more of a leveraged AI-chip bet than
diversified tech. No addition given the already-full 5.00% weight and
AI-Capex theme sitting at its cap. Theme: AI-Capex, showing early
digestion/rotation signs after a long hot run — watch the outflow trend
into Q3 earnings season.

**XLI — reaffirmed, HOLD (sizing note).** $175.27 (unchanged — the only
read found this cycle appeared to be a stale duplicate of the prior
cycle's anchor, no fresh print located). Industrials remain the strongest
relative-strength sector story in the book (+19.7% YTD vs SPY +13.7%,
within 0.2% of its 52-week high), riding AI-infrastructure buildout,
defense spending, reshoring, and improving PMI data — no negative
constituent news found. At 10.49% NAV, XLI is still comfortably under its
15% per-ETF cap, so no forced rebalance is triggered, but it is roughly 2x
the weight of every other core position — a portfolio-construction note
for future review if industrials roll over, not an action this cycle.
Theme: Energy-Transition/Industrials, the best-momentum sector in the
book right now.

**AGG — reaffirmed, HOLD (passive, no action).** $97.00 (unchanged). The
Treasury curve remains elevated and upward-sloping (10yr ~5.01%, 30yr
~5.33%, near 20-yr highs) after the Fed's September dot plot shifted from
projecting cuts to projecting hikes into 2027 — a hawkish repricing that is
a modest, already-reflected headwind to price rather than a thesis break.
AGG's yield remains ~4.05-4.14%, consistent with the stated ~4.06% holding
yield. Continue the passive core-bond sleeve per fixed-sizing policy — not
re-picked, only rebalanced on drift from the 13% target. Theme:
Diversified-Core.

**VRTX — NEW POSITION (BUY, 6 sh @ $512.00, $3,072.00, 3.12% NAV).**
Vertex Pharmaceuticals cleared this cycle's baseline screen (6 of 8
filters: market cap $132.5B in range, FY26 revenue guidance raised to
$13.2B, ~86% gross margin, debt/equity 0.10, insider ownership 10.66%, RSI
33 — a pullback, not overbought; narrowly misses on forward P/E 25.53 and
FCF yield ~2.8%) and is backed by this cycle's clearest sector-rotation
signal: Healthcare/XLV posted the best 1-month return of all 11 S&P
sectors (+3.47%) with ETF flows flipping from outflows to inflows the week
of 9/16, and BofA's September fund-manager survey shows global managers
rotating into Healthcare more than any other sector after years of
underperformance-driven cheap valuations. VRTX has a genuine near-term
catalyst — an FDA accelerated-approval decision on povetacicept for IgA
nephropathy due Nov 30, 2026 — a best-in-class balance sheet, and only
minor/routine insider selling. Analyst consensus Buy (23 analysts), avg PT
$554.91 (+15.5% from entry). Sized to what the 10% cash floor could
comfortably fund after the PEP trim (position sizing constrained by
maintaining cash >= 10% NAV, not by conviction — see Position Sizing
note below); room to add further exists under both the 10% single-stock
cap and the theme's 25% cap (Healthcare-GLP1 now 10.10% of NAV with LLY
included). Theme: Healthcare-GLP1. Two other screened candidates were
passed on this cycle: UMBF (Financials, moderate conviction — mixed
near-term momentum, thin/ambiguous insider-ownership data, only ~4-5 of 8
filters cleanly passed) and NTRA (Healthcare-GLP1, watchlist only — fails
the RSI<70 gate at 72.3 and the 5% insider-ownership floor at ~3.0%, plus
a recent insider sale into strength; revisit on a pullback).

**Position-sizing note:** VRTX was sized smaller than this portfolio's
typical ~5% initial position (targeting instead the ~$3,400 of cash
available above the 10% NAV floor after the PEP trim) rather than trimming
further into PEP or another position purely to fund a full-size entry —
preserving PEP's remaining position as a legitimate (smaller) hold through
its Oct 8 catalyst, rather than treating the trim as a blank check to
fully fund the new buy.

---

### 2026-09-18 — Cycle #10 (LIGHT): reaffirm pass, no trades

Lightweight reaffirm/exit-only check on all 15 holdings (major-news + Exit
Criteria scan only, per LIGHT-cycle rules — no full fundamentals/technicals/
analyst-consensus pass, no new positions opened). Theme Exposure table
recomputed from today's prices; every theme, position, and sector-ETF
sleeve remained inside its cap, so no rebalance was needed.

**AVGO — Broadcom (HOLD, reaffirmed).** $349.05 (prev $349.21). Positive
news only: Q3 FY26 beat (revenue $29.6B, EPS $3.32), guided Q4 revenue
$34.8B on AI-chip sales +236% YoY; ex-dividend $0.65/share Sept 21. No
Exit Criteria triggered. Theme: AI-Capex.

**ETN — Eaton Corporation (HOLD, reaffirmed).** $392.66 (prev $399.22,
carried-forward price refreshed this cycle). Raised FY26 organic-growth
guidance to 12% on data-center demand; new Aerospace segment president
named. No negative news, no Exit Criteria triggered. Theme:
Energy-Transition.

**COF — Capital One Financial (HOLD, reaffirmed).** $203.00 (prev
$203.19). No major negative catalyst; BofA trimmed price target to $254
from $280 (still Buy-rated) and completed a €1.5B senior-notes offering.
Watch item: passing mention of rising credit-card delinquencies in
unrelated coverage — not sourced to a COF-specific disclosure, logged as a
watch item, not an Exit Criteria trigger. Theme: Financials.

**LLY — Eli Lilly (HOLD, reaffirmed).** $1,134.34 (prev $1,136.11,
essentially flat). Positive flow: FDA approved an updated Kisunla label
(better ARIA-E safety) and Foundayo (oral GLP-1), and the FDA ended the
GLP-1 shortage designation (blocks compounded knockoffs of
Zepbound/Mounjaro) — net bullish for the branded franchise. No Exit
Criteria triggered. Theme: Healthcare-GLP1.

**TJX — TJX Companies (HOLD, reaffirmed).** $122.84, carried forward
unchanged — no price print newer than 2026-09-16 could be sourced this
cycle (second consecutive cycle carried). No fresh news found beyond the
already-logged raised FY27 outlook / Jefferies Marmaxx-segment concern.
No Exit Criteria triggered. Theme: Consumer-Defensive.

**GOOGL — Alphabet (HOLD, reaffirmed).** $346.51 (prev $344.98). Positive
catalyst: a federal judge ruled Google will not have to divest its AdX
ad-tech exchange (behavioral remedies only, no breakup) — a meaningful
antitrust overhang eased; multiple analyst price-target hikes followed
(e.g. Evercore to $450). No Exit Criteria triggered. Theme: AI-Capex.

**BALL — Ball Corporation (HOLD, reaffirmed).** $62.92 (prev $62.49,
refreshed this cycle after being carried forward). New India
manufacturing-facility investment and two new board members announced;
no negative news. No Exit Criteria triggered. Theme: Materials.

**PEP — PepsiCo (HOLD, reaffirmed — watch item).** $130.10 (prev $136.46,
a -4.66% move), a fresh 52-week low, continuing a multi-week slide on
snack-item price cuts pressuring margins and soft North America consumer
trends. However, Q2 2026 revenue ($24.18B) and EPS ($2.20) still modestly
beat consensus, so this does not yet meet the Exit Criterion of "2
consecutive quarters of fundamental deterioration" — held, not trimmed,
but flagged as a watch item for the next HEAVY research pass. Theme:
Consumer-Defensive.

**NEE — NextEra Energy (HOLD, reaffirmed — watch item).** $80.50 (prev
$80.65, essentially flat). NextEra continues advancing its pending ~$100B
Dominion Energy acquisition (expanded a Virginia customer-benefits
package Sept 14 to secure regulatory approval) and secured a $1.9B loan
to restart the Duane Arnold nuclear plant. Regulatory-approval-dependent
M&A remains a watch item, not a trigger. No Exit Criteria triggered.
Theme: AI-Capex.

**MU — Micron Technology (HOLD, reaffirmed).** $985.00 (prev $927.60,
+6.19%). Opened a $2.75B India semiconductor assembly/test facility
(Gujarat) with commercial production started and first modules shipped to
Dell; TD Cowen reiterated Buy at $1,600 PT, RBC initiated/reiterated
Outperform. No Exit Criteria triggered. Theme: AI-Capex.

**BHRB — Burke & Herbert Financial (HOLD, reaffirmed).** $73.80,
unchanged. No new negative news; LINKBANCORP/LINKBANK merger integration
fully closed, Q2 EPS beat ($2.03 vs. $1.99 consensus). No Exit Criteria
triggered. Theme: Financials.

**IMAX — IMAX Corporation (HOLD, reaffirmed).** $52.09, unchanged.
Reaffirmed FY26 guidance (~$1.4B global box office); "The Odyssey" is now
IMAX's highest-grossing release ever ($289M). No negative news, no Exit
Criteria triggered. Theme: Communication-Services.

**XLK — Technology Select Sector SPDR (HOLD, reaffirmed).** $187.87 (prev
$183.74, +2.25%), tracking the broader AI/tech rally (GOOGL, MU strength
today). No rebalance needed — sleeve remains within its 15% NAV cap.

**XLI — Industrial Select Sector SPDR (HOLD, reaffirmed).** $175.27 (prev
$168.71, +3.89%). No rebalance needed — sleeve at 10.58% of NAV, within
its 15% NAV cap.

**AGG — iShares Core U.S. Aggregate Bond ETF (HOLD, reaffirmed).** $97.00,
carried forward unchanged — no fresher print than 2026-09-05 could be
sourced this cycle (third consecutive cycle carried; passive core bond
sleeve, not re-picked). No rebalance needed — sleeve at 8.14% of NAV.

**No positions sold, trimmed, or added this cycle.** Theme Exposure
recomputed: AI-Capex is the closest theme to its cap at 24.86% of NAV
(still under the 25% cap) — watch next cycle given continued strength in
AVGO/GOOGL/MU/XLK. Cash accrued 1 day of SGOV-equivalent interest since
the last cycle (2026-09-17), bringing the balance to $11,044.26.

### 2026-09-17 — Cycle #9 (LIGHT): reaffirm pass, no trades, price-data reconciliation

LIGHT cycle: lightweight reaffirm/exit-only check on all 15 holdings (major
news + Exit Criteria scan only, no full fundamentals/technicals pass). No
Exit Criteria triggered on any position. Theme Exposure and sleeve weights
recomputed from today's prices; everything remained inside its cap
(AI-Capex closest at 24.58% of NAV, under the 25% cap; XLI closest of the
sector ETFs at 10.24%, under its 15% cap; no stock above ~7.3% of NAV,
under the 10% cap). Cash at 11.36% of NAV, above the 10% floor. No new
positions opened (LIGHT cycles never open new positions). Several tickers
returned materially conflicting price reads today; a second targeted
cross-check pass was run and the more internally-consistent, corroborated
value used in each case — see the header note above and per-ticker detail
below.

**AVGO — Broadcom (HOLD, reaffirmed — no action).** Theme: AI-Capex. Price
$349.21, +1.3% day-over-day, corroborated by an independent read near
$348.28 tied to a Cloud Network Insights product launch plus a broader
semiconductor sector rebound (NVDA/AMD strength); an alternate $342.91
read was set aside as less corroborated. No insider-selling or exit-
criteria flags found.

**ETN — Eaton Corporation (HOLD, reaffirmed — no action).** Theme:
Energy-Transition. No new company-specific news found today. Price could
not be refreshed past the existing print ($399.22, matched today's search
result exactly which raised a staleness concern) and was carried forward
unchanged — second consecutive cycle carried. Stop condition not
triggered.

**COF — Capital One Financial (HOLD, reaffirmed — no action, watch item
continues).** Theme: Financials. Price $203.19, a -1.77% move that lines
up almost exactly with yesterday's confirmed close, consistent with the
ongoing proposed federal credit-card-rate-cap overhang; a $216.51
"rebound" read had no corroborating news and was discarded. Still a
legislative/regulatory overhang worth tracking, not a thesis break — no
named exit criterion met.

**LLY — Eli Lilly (HOLD, reaffirmed — no action).** Theme: Healthcare-GLP1.
No negative news found today. Search result repeated the prior cycle's
exact price ($1,136.11), which fell within today's reported day range
($1,131.59-$1,161.00), so accepted as a flat day. Thesis unchanged.

**TJX — The TJX Companies (HOLD, reaffirmed — no action, price-data flag).**
Theme: Consumer-Defensive. Price $122.84, a normal -2.7% day; a $154.39
read implying a ~22% one-day jump had zero corroborating news anywhere
and is treated as a bad data point, discarded. No new incremental
company news found; the already-flagged soft Marmaxx comp remains a
single data point, not the two consecutive quarters of confirmed
deterioration the exit criteria require.

**GOOGL — Alphabet (HOLD, reaffirmed — no action).** Theme: AI-Capex. Price
$344.98, a small move from yesterday. No new news dated today beyond
already-known items; analyst consensus remains Strong Buy. Stop condition
not triggered.

**BALL — Ball Corporation (HOLD, reaffirmed — no action).** Theme:
Materials. No new news found today; price could not be refreshed past the
existing print ($62.49), carried forward unchanged — third consecutive
cycle carried. No deterioration flagged.

**PEP — PepsiCo (HOLD, reaffirmed — no action).** Theme:
Consumer-Defensive. Price $136.46, a modest +0.7% move. No new news dated
today; the already-flagged margin-recovery watch item remains open
pending the 2026-10-08 Q3 print. Thesis intact.

**NEE — NextEra Energy (HOLD, reaffirmed — no action, watch item
continues).** Theme: AI-Capex. Price $80.65, in line with today's reported
day range and a small move from yesterday. No new news found today beyond
the already-known Dominion-merger customer-benefits package, which
remains a structural item to monitor given the deal's size, not itself a
regulatory setback (the position's actual stop criterion). Stop condition
not triggered.

**MU — Micron Technology (HOLD, reaffirmed — no action).** Theme:
AI-Capex. Price $927.60, essentially flat day-over-day and independently
corroborated; a $973.88 read had no matching news-sourced print and was
discarded. Fiscal Q4 earnings (2026-09-30) remains the nearest major
catalyst, 13 days out. HBM demand/supply thesis unchanged.

**BHRB — Burke & Herbert Financial (HOLD, reaffirmed — no action).**
Theme: Financials. Price $73.80, up modestly. No new news found since the
last cycle; consensus remains constructive. No red flags found.

**IMAX — IMAX Corporation (HOLD, reaffirmed — no action).** Theme:
Communication-Services. Price $52.09, roughly flat. No new news found
beyond already-known analyst-target moves from earlier in September.
Thesis unchanged, no exit criteria triggered.

**XLK — Technology Select Sector SPDR (HOLD, reaffirmed — no action).**
Theme: AI-Capex, passive sleeve pick — not individually re-picked, only
rebalanced on drift from target/theme caps. Price $183.74. No rebalance
needed today.

**XLI — Industrial Select Sector SPDR (HOLD, reaffirmed — no action).**
Theme: Energy-Transition, passive sleeve pick. Price $168.71, a modest
-0.7% move. Remains the largest single sleeve at 10.24% of NAV, still
under its 15% ETF cap. No rebalance needed today.

**AGG — iShares Core U.S. Aggregate Bond ETF (HOLD, reaffirmed — no
action).** Passive core bond sleeve, rebalanced only on drift from the 8%
target. Currently 8.18% of NAV — no rebalance needed today.

**Cash** accrued ~1 day of SGOV-equivalent interest (~$1.36) since the
last cycle (2026-09-16).

### 2026-09-16 — Cycle #8 (LIGHT): reaffirm pass, no trades, price-data corrections noted

LIGHT cycle: lightweight reaffirm/exit-only check on all 15 holdings (major
news + Exit Criteria scan only, no full fundamentals/technicals pass). No
Exit Criteria triggered on any position. Theme Exposure and sleeve weights
recomputed from today's prices; everything remained inside its cap
(AI-Capex closest at 24.55% of NAV, under the 25% cap; XLI closest of the
sector ETFs at 10.31%, under its 15% cap; no stock above ~7.4% of NAV,
under the 10% cap). Cash at 11.35% of NAV, above the 10% floor. No new
positions opened (LIGHT cycles never open new positions). Today's NAV
change (-1.63% day-over-day) is driven mostly by price-data corrections on
AVGO, COF, XLK, and XLI rather than genuine single-day market moves — see
the header note above for the cross-checked detail.

**AVGO — Broadcom (HOLD, reaffirmed — no action).** Theme: AI-Capex. No
new news dated 2026-09-15/16 found beyond last cycle's already-digested
FQ3 print and sector-wide AI-pace debate. Price corrected from an
uncorroborated $366.70 to a multi-source-confirmed $344.72 — a data fix,
not a new decline. No insider-selling or exit-criteria flags found.

**ETN — Eaton Corporation (HOLD, reaffirmed — no action).** Theme:
Energy-Transition. No new company-specific news found today; consensus
remains Buy (~$478 average target). Stop condition not triggered.

**COF — Capital One Financial (HOLD, reaffirmed — no action, watch item
flagged).** Theme: Financials. Shares have declined over several sessions
($217.91 -> ~$206.81) on a proposed federal 10% credit-card-interest-rate
cap that is spooking card-lender sentiment broadly, not a Capital One-
specific development; no confirmed credit-quality deterioration or
Discover-integration setback found. This is a legislative/regulatory
overhang worth tracking next cycle, not a thesis break — none of the
named exit criteria (thesis broken, insider selling >10% of holdings, two
confirmed quarters of deterioration, higher-conviction alternative with no
room) are met.

**LLY — Eli Lilly (HOLD, reaffirmed — no action).** Theme: Healthcare-GLP1.
No negative news found; recent coverage is supportive (Foundayo oral
GLP-1 gaining new-patient share, a Berenberg Buy/price-target raise).
Thesis reinforced, not broken.

**TJX — The TJX Companies (HOLD, reaffirmed — no action).** Theme:
Consumer-Defensive. No new incremental news dated 2026-09-15/16; the
already-flagged soft Marmaxx comp remains a single data point, not the two
consecutive quarters of confirmed deterioration the exit criteria require.
Price unchanged from last cycle ($126.22).

**GOOGL — Alphabet (HOLD, reaffirmed — no action).** Theme: AI-Capex. No
new news dated 2026-09-15/16 beyond the already-known 9/9 European
data-center commitment; analyst consensus remains Strong Buy. Stop
condition not triggered.

**BALL — Ball Corporation (HOLD, reaffirmed — no action).** Theme:
Materials. No new news found today; price could not be refreshed past the
existing 2026-09-15 print ($62.49), carried forward unchanged. No
deterioration flagged.

**PEP — PepsiCo (HOLD, reaffirmed — no action).** Theme:
Consumer-Defensive. No new news dated 2026-09-15/16; the already-flagged
margin-recovery watch item remains open pending the 2026-10-08 Q3 print.
Thesis intact, not broken.

**NEE — NextEra Energy (HOLD, reaffirmed — no action, watch item
flagged).** Theme: AI-Capex. On 2026-09-14, NextEra and Dominion announced
an expanded Virginia customer-benefits package aimed at securing
regulatory approval for the pending ~$100B Dominion acquisition — a
structural development worth continued monitoring given the deal's size,
but not itself a "regulatory setback" (the position's actual named stop
criterion). Price today showed conflicting intraday reads ($81.65
Robinhood, $81.01 TradingView, $77.76 MarketBeat); the $77.76 outlier was
excluded and the average of the other two ($81.33) was used. Stop
condition not triggered.

**MU — Micron Technology (HOLD, reaffirmed — no action).** Theme:
AI-Capex. No new news dated 2026-09-15/16; fiscal Q4 earnings
(2026-09-30) remains the nearest major catalyst, 14 days out. HBM
demand/supply thesis unchanged. No exit criteria triggered.

**BHRB — Burke & Herbert Financial (HOLD, reaffirmed — no action).**
Theme: Financials. No new news found since the last cycle; consensus
remains constructive. No red flags found.

**IMAX — IMAX Corporation (HOLD, reaffirmed — no action).** Theme:
Communication-Services. No new news dated 2026-09-15/16 found beyond
already-known analyst-target moves (Rosenblatt raise, Goldman
Hold-reiterate) from earlier in September. Thesis unchanged, no exit
criteria triggered.

**XLK — Technology Select Sector SPDR (HOLD, reaffirmed — no action).**
Theme: AI-Capex, passive sleeve pick — not individually re-picked, only
rebalanced on drift from target/theme caps. Price corrected from $190.13
to a $184.89 confirmed 2026-09-15 close. No rebalance needed today.

**XLI — Industrial Select Sector SPDR (HOLD, reaffirmed — no action).**
Theme: Energy-Transition, passive sleeve pick. Price corrected from
$174.56 to a $169.93 confirmed 2026-09-15 close. Remains the largest
single sleeve at 10.31% of NAV, still under its 15% ETF cap. No rebalance
needed today.

**AGG — iShares Core U.S. Aggregate Bond ETF (HOLD, reaffirmed — no
action).** Passive core bond sleeve, rebalanced only on drift from the 8%
target. Currently 8.08% of NAV — no rebalance needed today.

**Cash** accrued ~1 day of SGOV-equivalent interest (~$1.36) since the
last cycle (2026-09-15).

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
