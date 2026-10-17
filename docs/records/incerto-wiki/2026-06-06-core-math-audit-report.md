> Historical record from `incerto-wiki` at `9717c9cf83aee18b47f423a14bce2f0d14bb8bcb`.
> Source: `docs/reports/deep-math/2026-06-06-core-math-audit-report.md`. Statements and commands below describe that repository
> at the recorded date, not current xshi-math verification. MIT; copyright (c) 2023 xshi19.

# Report

## Executive Summary

Most core formulas and proof sketches are correct under their intended iid/right-tail/asymptotic assumptions. Main fixes:

- Double Pareto mean is misstated for `alpha <= 1`; code also reports `0`.
- Pareto survival-ratio identity needs an "eventually"/support condition for `t < 1`.
- S&P 500 loss definition includes zeros, while Hill code requires positive losses.
- Hill, mean-excess, and PBdH pages should make several load-bearing assumptions more explicit.
- Citation precision is thin: theorem/section/page references are missing for several durable EVT claims.

## Problem Restatement

Audit the listed Incerto Wiki concept pages and relevant Python helpers for mathematical correctness, assumptions, boundary cases, notation consistency, code/prose alignment, empirical overclaiming, and citation/proof gaps, using only supplied repository context.

## Assumptions and Notation

- Shared notation in `content/notation/index.md` is mostly followed: `alpha` for Pareto tail exponent, `xi=1/alpha`, `k` upper order statistics, `u` threshold, `S_n`, `M_n`, `R_n`.
- Add or localize repeated notation not yet shared: GPD scale `beta`, right endpoint `x_F`.
- Critical assumptions that should remain visible: iid sampling, nonnegativity for LLN/max-to-sum, positivity for Hill, `P(X>u)>0` for mean excess, regular variation for Pareto-type asymptotics, and intermediate sequence `k_n -> infinity`, `k_n/n -> 0`.

## Source and Context Inventory

Audited repository files:

- Concept pages under `content/concepts/...` listed in the request.
- Reading guides: `content/reading-guides/taleb-scoft/ch3.md`, `ch4.md`, and `content/reading-guides/external/embrechts-modelling-extremal-events.md`.
- Code: `incerto/distributions.py`, `incerto/estimators.py`.
- Tests: `tests/test_distributions.py`, `tests/test_estimators.py`.
- Bibliography: `content/bibliography.bib`.

No PDFs or web sources were supplied or used.

## Main Analysis

- Pareto, Pareto moments, Karamata, LLN failure, and max-to-sum pages are largely correct.
- Double Pareto page/code has a real boundary error: symmetry does not make the expectation exist when positive and negative parts are both infinite.
- Hill estimator code matches the displayed order-statistic formula.
- PBdH statement is broadly correct, but endpoint/support and citation precision should be improved.
- Mean excess formulas are correct with missing support/exceedance assumptions.
- Empirical pages are mostly cautious. S&P 500 title/formula should better match "diagnostics on positive losses," not a proven tail fit.

## Proofs or Derivations

- Double Pareto: for `X=B(Y-1)`, `E[X^+]=E[X^-]=0.5 E[Y-1]`. Since Pareto `E[Y]=infinity` for `alpha <= 1`, both parts are infinite, so `E[X]` is undefined, not `0`.
- Pareto ratio: if `t<1` and `x_m <= x < x_m/t`, then `tx < x_m`, so `bar F(tx)=1`, not `(x_m/(tx))^alpha`. The identity is exact only when both `x` and `tx` are in the Pareto tail, or asymptotically.
- Max-to-sum proof is correct: integrability implies `x P(X>x)->0`, so the union-bound term vanishes.
- Mean excess GPD formula `e(u)=(beta+xi u)/(1-xi)` is correct only for thresholds in support with `beta+xi u>0` and `xi<1`.

## Computations or Checks

Static code check only; tests were inspected but not run.

- `pareto_type1` implements the stated Type I formulas and scale behavior.
- `double_pareto` implements density/CDF/SF correctly, but `_stats` returns mean `0.0` for all `alpha`; this conflicts with expectation existence.
- `hill_estimator`, `hill_alpha_estimator`, and `hill_stability` implement the stated Hill formula.
- `max_to_sum_ratio`, `running_mean`, and `mean_excess` align with prose.
- Missing tests: Double Pareto mean boundary, Pareto scaled formulas, SP500 positive-loss precondition if dataset helpers are tested elsewhere.

## Caveats and Failure Modes

- Empirical Hill/mean-excess plots are diagnostics, not model proof.
- Threshold choice dominates finite samples.
- Dependence and volatility clustering remain major caveats for S&P 500 losses.
- Boundary cases near `alpha=1`, `alpha=2`, `xi=1`, and `xi=1/2` should be stated wherever moments are interpreted.

## Suggested Incerto Wiki Changes

### P0

1. **Path:** `content/concepts/distributions/double-pareto.md`; `incerto/distributions.py`; `tests/test_distributions.py`
   **Location:** Statement/Derivation; `double_pareto_gen._stats`
   **Issue:** Claims/code report mean `0` for all `alpha`, but the mean is undefined for `alpha <= 1`.
   **Correction:** State `E[X]=0` only for `alpha>1`; for `alpha<=1`, only symmetry center/principal-value intuition is zero. Return `nan` for undefined mean, or explicitly document a non-expectation location convention.
   **Verification:** Add tests for `alpha=0.8`, `1.5`, `3.0`; verify positive/negative-part integrals.

2. **Path:** `content/concepts/distributions/pareto.md`
   **Location:** Intuition/Properties survival-ratio identity
   **Issue:** Exact ratio for all `x>=x_m`, `t>0` is false when `t<1` and `tx<x_m`.
   **Correction:** Say exact for `x >= max(x_m, x_m/t)`, or asymptotically as `x -> infinity`.
   **Verification:** Check counterexample `t=1/2`, `x=x_m`.

### P1

3. **Path:** `content/concepts/examples/sp500-tail.md`
   **Location:** Statement formula and Python cell
   **Issue:** `L_t=-log(P_t/P_{t-1}) 1_{P_t<P_{t-1}}` includes zeros; Hill requires strictly positive observations.
   **Correction:** Define the analyzed sample as positive losses on down days, or define `max(-log return,0)` and explicitly filter `L_t>0` before Hill.
   **Verification:** Confirm `losses` from `negative_log_returns()` are finite and strictly positive.

4. **Path:** `content/concepts/methods/hill-estimator.md`
   **Location:** Consistency paragraph
   **Issue:** "usual iid tail assumptions" is too implicit.
   **Correction:** State iid positive sample, right tail regularly varying with `xi>0`, and intermediate `k_n`.
   **Verification:** Local proof sketch/citation to Hill or EVT theorem.

5. **Path:** `content/concepts/theorems/mean-excess-function.md`
   **Location:** Statement
   **Issue:** Missing `P(X>u)>0` and GPD support conditions.
   **Correction:** Add `P(X>u)>0`; for GPD require threshold in support and `beta+xi u>0`; mean finite only for `xi<1`.
   **Verification:** Derive from GPD threshold stability.

6. **Path:** `content/concepts/theorems/pickands-balkema-de-haan.md`
   **Location:** Statement
   **Issue:** Right endpoint `x_F` and support compatibility are not formally defined.
   **Correction:** Define `x_F=sup{x:F(x)<1}` and clarify the sup is over valid excess support.
   **Verification:** Compare with cited PBdH theorem statement.

### P2

7. **Path:** theorem/method pages using standard results
   **Location:** References sections
   **Issue:** Citation gap: no theorem/page/section pointers for regular variation representation, Karamata, Hill consistency, PBdH, GPD moments.
   **Correction:** Add precise references from bibliography sources. Mark uncertain until checked against source texts.
   **Verification:** Source lookup.

8. **Path:** `content/concepts/methods/hill-estimator.md`; `content/concepts/theorems/pickands-balkema-de-haan.md`; Embrechts guide
   **Location:** links to `extreme-value-index.md`
   **Issue:** Linked dependency not supplied in manifest; possible broken/missing concept page.
   **Correction:** Verify file exists; if absent, add page or remove dependency.
   **Verification:** Site link check.

9. **Path:** `content/notation/index.md`
   **Location:** Tail behavior / EVT notation
   **Issue:** `beta` and `x_F` recur but are not shared notation.
   **Correction:** Add entries for GPD scale `beta` and right endpoint `x_F`.
   **Verification:** Cross-page notation scan.

10. **Path:** `content/concepts/examples/amazon-bookrank.md`; `content/concepts/examples/sp500-tail.md`
    **Location:** Titles
    **Issue:** "Pareto in the Wild" and "Tail Fit" can sound stronger than diagnostics.
    **Correction:** Consider "Amazon Book Rank Tail Diagnostics" and "S&P 500 Tail Diagnostics."
    **Verification:** Editorial review.

11. **Path:** `tests/test_distributions.py`
    **Location:** distribution boundary tests
    **Issue:** Missing tests for moment-existence boundaries and scale formulas.
    **Correction:** Add Pareto scale checks and Double Pareto `alpha<=1` mean behavior.
    **Verification:** Run `pytest tests/test_distributions.py`.

### P3

12. **Path:** `content/concepts/theorems/mean-excess-function.md`
    **Location:** page type/path
    **Issue:** Mean excess is more diagnostic/method than theorem.
    **Correction:** Optionally move under methods or keep with explicit rationale.
    **Verification:** Link/build check.

13. **Path:** `content/concepts/methods/max-to-sum-ratio.md`
    **Location:** frontmatter `depends_on`
    **Issue:** Method depends on an example page.
    **Correction:** Make example a backlink rather than dependency.
    **Verification:** Concept graph check.

## References

Repository bibliography keys used as available context: `@bingham1987regular`, `@feller1971introduction`, `@resnick2007heavy`, `@embrechts1997modelling`, `@hill1975simple`, `@balkema1974residual`, `@pickands1975statistical`, `@davison1990models`, `@coles2001introduction`, `@taleb2020scoft`, `@zhu2021amazonbookrank`, `@fred2026sp500`.
