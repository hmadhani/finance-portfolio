# Options Portfolio — Open Issues List

Known gaps and deferred review findings from the build (2026-09-27, plan
`docs/superpowers/plans/2026-09-27-options-portfolio.md`). Nothing here blocks
the trial run. Items fixed in the final-review wave are listed at the bottom
for traceability.

## Decide before relying on it

- [ ] **Covered-call lifecycle is unspecified.** Once the routine writes a call
  on assigned shares, nothing defines: closing/rolling *only the call leg* at
  21 DTE, removing an expired OTM call leg from the share position, or the
  shares being called away (ITM call at expiry). Only reachable after a CSP is
  assigned *and* a call is written — weeks out at the earliest.

## Behavior gaps (routine / risk logic)

- [ ] An unpriceable leg (0/0 or crossed quote) makes the closing `price-spread`
  exit 2, so the position is held and retried — it can stay open past 21 DTE
  until expiry. Logged each cycle, but not yet documented in
  `investor-profile.md`.
- [ ] Selling assigned shares outright can't be priced by `price-spread` (no
  stock-only close path).
- [ ] The 25% NAV aggregate check double-counts the share position when a
  covered call is the candidate (conservative, blocks rather than over-allows).
- [ ] Covered-call analysis `max_loss` bases the shares at spot, not at the
  assignment cost basis.
- [ ] Stock-only positions (`entry_cost > 0`) get debit-style
  `profit_target`/`stop_loss` triggers from `mark`, though share management was
  meant to belong to the routine.
- [ ] `stock_contract` always keys `"STOCK"` — user ruled keep plan code
  (stock contracts are per-position and never enter the per-symbol chain
  index); re-check if that ever changes.

## Code correctness (minor)

- [ ] `bs_price` / `prob_itm` zero-vol fallback (T>0, sigma=0) ignores discounting.
- [ ] `Contract` kind other than `"C"` is silently treated as a put.
- [ ] `Leg.sign` treats any action other than `"BUY"` as SELL (no validation).
- [ ] `parse_leg_spec` still accepts strike ≤ 0; a trailing `;` gives a confusing error.
- [ ] `legs_from_spec(with_stock=True, spot=None)` → TypeError; all-stock legs →
  ZeroDivisionError in the IV average.
- [ ] `credit_or_debit` labels zero cost "debit"; breakeven uses an exact `== 0` float check.
- [ ] PoP uses a plain average IV across legs (undocumented approximation).
- [ ] `iv_rank` = 0 vs `iv_percentile` can contradict on flat history (hi == lo).
- [ ] `lookback=0` slices the whole list in `history()` / `vix_percentile()`.
- [ ] No ISO-date validation in `ivhist`.
- [ ] `profit_target` compares a 1-dp rounded percent — can fire ~0.04pp early.
- [ ] At `dte <= 0`, intrinsic uses current spot, not the settlement price.
- [ ] `regime` message wording is cosmetic/inconsistent.

## Test gaps

- [ ] `bs_greeks` boundary and put-theta tests; `test_bs.py:38` comment says
  theta ≈ −0.16/day, actual −0.211.
- [ ] `Contract.row()`, `fetch_text` fixture/network branches, `load_*`, and
  `is_liquid` boundary values untested.
- [ ] `MIN_OBS` boundary, flat history, empty VIX (ivhist).
- [ ] `value_at` / `pnl_at` / payoff ASCII with a stock leg; dedicated regression
  tests for the unbounded-profit mirror fix and the far-point `max_loss`.
- [ ] Negative-trigger and debit profit-target tests (marks).
- [ ] CLI: ETF `abs_spread_ok` override path (fixture ETF1 is not in `ETFS`);
  stress/backwardation branch.

## Docs

- [ ] `RESOURCES.md`: McMillan ISBN sourced from a retailer (publisher catalog
  page exists); Whaley / OCC / CME links verified via Wayback only.

## Fixed in the final-review wave (for reference)

- [x] `ivhist.record` CRLF line endings → `lineterminator="\n"`.
- [x] `vix_percentile` crash on empty/header-only/HTML → returns None; `regime` reports partial `errors`.
- [x] `parse_leg_spec` ratio ≤ 0 → rejected.
- [x] CLI KeyError message `.strip('"')` no-op → `e.args[0]`.
- [x] Routine STEP 3 had no branch for `mark` chain-failure `error` entries → hold + carry prior mark.
