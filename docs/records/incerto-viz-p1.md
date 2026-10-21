# Incerto visualization P1

2026-10-20. Implemented on `viz/p1`, stacked directly on
`origin/site/code-visibility` at `3e8504d5f8f838c4b976e6ed610716b717dfb591`
(PR #35). Xiang selected Codex GPT-6-Astra xhigh for code and figures;
independent Astra max mathematical review is recorded below. No commit, staging,
push, file deletion, publication, chapter-7 work, or program-state change.

Scope is exactly the ten enumerated P1 items from the read-only
`/workspace/visualization-review-pr34.md`. That review was read in place and
was not copied into this branch. Other legacy layout repairs, P2 and P3 are
outside this change. Existing proofs are preserved; the Max review adds
limit clarifications and sources.

## Items and figures

All assets below live in `assets/figures/incerto/`. The first eleven are new.
The last reuses the existing slow-variation asset with larger text and a
vertical-layout width; its population law and exponent remain unchanged.
Every figure has a caption and descriptive alt text on its concept page.

| Item | Figure | Page | Producer |
| --- | --- | --- | --- |
| 1 | [pareto-card.svg](../../assets/figures/incerto/pareto-card.svg) | [Pareto](../../content/incerto-pareto.md#pareto-distribution-card) | `demos/incerto/distribution_cards.py` |
| 2 | [gpd-card.svg](../../assets/figures/incerto/gpd-card.svg) | [Generalized Pareto](../../content/incerto-generalized-pareto.md#gpd-distribution-card) | `distribution_cards.py` |
| 3 | [gev-card.svg](../../assets/figures/incerto/gev-card.svg) | [GEV](../../content/incerto-generalized-extreme-value.md#gev-distribution-card) | `distribution_cards.py` |
| 4 | [frechet-card.svg](../../assets/figures/incerto/frechet-card.svg) | [Fréchet](../../content/incerto-frechet.md#frechet-distribution-card) | `distribution_cards.py` |
| 4 | [frechet-maxima.svg](../../assets/figures/incerto/frechet-maxima.svg) | [Fréchet maxima](../../content/incerto-frechet.md#frechet-maxima-comparison) | `distribution_cards.py` |
| 5 | [double-pareto-card.svg](../../assets/figures/incerto/double-pareto-card.svg) | [Double Pareto](../../content/incerto-double-pareto.md#double-pareto-distribution-card), before the existing matching figure | `distribution_cards.py` |
| 6 | [hill-stability.svg](../../assets/figures/incerto/hill-stability.svg) | [Hill estimator](../../content/incerto-hill-estimator.md#hill-synthetic-stability) | `demos/incerto/tail_estimation.py` |
| 7 | [mean-excess.svg](../../assets/figures/incerto/mean-excess.svg) | [Mean excess](../../content/incerto-mean-excess-function.md#mean-excess-synthetic) | `tail_estimation.py` |
| 8 | [threshold-diagnostics.svg](../../assets/figures/incerto/threshold-diagnostics.svg) | [Threshold selection](../../content/incerto-tail-threshold-selection.md#threshold-synthetic-figures) | `tail_estimation.py` |
| 8 | [threshold-pp.svg](../../assets/figures/incerto/threshold-pp.svg) | [Threshold selection](../../content/incerto-tail-threshold-selection.md#threshold-synthetic-figures) | `tail_estimation.py` |
| 9 | [max-to-sum.svg](../../assets/figures/incerto/max-to-sum.svg) | [Max-to-sum](../../content/incerto-max-to-sum-ratio.md#max-to-sum-paths) | `demos/incerto/max_to_sum.py` |
| 10 | [glossary-slow-variation.svg](../../assets/figures/incerto/glossary-slow-variation.svg) | [Regular variation](../../content/incerto-regular-variation.md#regular-variation-slow-ratio); existing chapter-2 embed retained | `demos/incerto/glossary_worked_cases.py` |

The five cards share one density/CDF/log-log survival layout in
[figures.py](../../src/math/incerto/figures.py). They use fixed parameters:
Pareto minimum one and exponents 0.8/1.5/3; GPD scale one and shapes
−0.4/0/0.4; GEV location zero, scale one and shapes −0.3/0/0.3; Fréchet
unit scale and double Pareto's shifted symmetric unit-scale convention,
both with exponents 0.8/1.5/3. Finite endpoints are marked. Negative
coordinates are shown only in the linear density/CDF panels. Exact zero
survival is masked on log axes, whose lower visible probability is 1e-8.
No moment matching or probability floor is applied.

The Fréchet comparison calls the existing `pareto_normalized_maximum_cdf`
for n=1/4/16/64 and alpha=1.5. Its second panel displays the CDF difference
without shifting overlapping curves. Slow variation retains the valid law
u^-2 (1+log u) above one. Its caption explicitly distinguishes that exponent
and slowly varying factor from the page's earlier alpha=1.5/log(u) example.
The other glossary asset remains byte-identical to the base revision.

## Helpers and API

Every public addition has an explicit `api-*` anchor and runnable example in
[the API reference](../../content/incerto-api-reference.md).

| Source | New helper | Contract and checks |
| --- | --- | --- |
| [distributions.py](../../src/math/incerto/distributions.py) | `generalized_pareto(xi, beta=1)` | Frozen zero-location GPD with pdf/cdf/sf/logsf/ppf/rvs/support; finite scalar parameters and positive scale. Tests cover formulas, support, endpoints, normalization, zero-shape limit and small tails. |
| Same | `generalized_extreme_value(xi, mu=0, sigma=1)` | Frozen GEV translated to SciPy `c=-xi`, preserving the page's positive-heavy-tail convention. Independent formula, location/scale, endpoint, normalization and Gumbel-limit tests. |
| Same | `frechet(alpha, scale=1)` | Frozen `invweibull`, positive alpha/scale, zero density/CDF and unit survival at/below zero. Formula, GEV-reparameterization, normalization and tiny-survival tests. |
| [estimators.py](../../src/math/incerto/estimators.py) | `max_to_sum_path(x)` | One ratio per nonnegative prefix; zero totals return NaN. Log accumulation avoids overflowing sums and scaling early values by a future record. Tests cover exact prefixes, scale invariance, zeros, invalid data, overflow and the final-ratio identity. |
| Same | `gpd_threshold_fit(x, threshold, min_exceedances=30)` | Strict excesses, fixed zero location, iteration/evaluation caps, convergence and support checks; count/status retained when parameters are unavailable. Tests cover fitted deterministic GPD quantiles, ties, minimum counts, constant excesses, invalid inputs/support and optimizer failure. |
| [figures.py](../../src/math/incerto/figures.py) | `vertical_figure` | Shared five-inch single-column layout with validated panel count/height. |
| Same | `distribution_card` | Shared three-panel exporter input; validates grids/evaluations, marks supports and masks log-axis zeros. Layout/support/masking tests plus complete export reproducibility tests. |

The five numerical helpers are also exported through `xmath.incerto`.
No dependency, lockfile or package mapping changed. The adapters use the
published [GPD](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.genpareto.html),
[GEV](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.genextreme.html)
and [Fréchet/inverse-Weibull](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.invweibull.html)
interfaces. The installed SciPy version is 1.18.1; the GEV translation is
also checked against the page formula rather than only against SciPy output.

## Experiment contract

- Hill: n=30,000; exact Pareto alpha=1.7/minimum=1, PCG64 seed 20261020.
  The independent mixture uses seed 20261021, uniform [1,3] with probability
  0.82 and Pareto alpha=1.7/minimum=3 otherwise. Its realized tail count is
  5,344. The third panel maps retained counts to observed thresholds; strict
  counts are checked against k for these untied continuous samples.
- Mean excess: reuses the exact-Pareto sample; independent exponential-mean-1
  and uniform-[0,5] samples use seeds 20261022/20261023, also n=30,000.
  Population and empirical curves have separate line styles. Estimates with
  fewer than 50 exceedances are masked; all counts remain visible. Infinite
  population mean excesses are labelled, not drawn. The figure's Pareto
  exponent 1.7 is explicitly distinguished from the earlier table's 1.6.
- Threshold selection: reuses exactly the Hill mixture sample. All six
  panels use one observed-threshold grid and strict counts. A separate PP
  figure uses fixed thresholds 2/3/12, with 17,596/5,344/501 excesses.
  There are 35 coordinated fits plus three PP fits, each capped at 2,000
  Nelder-Mead iterations / 4,000 objective evaluations. Four coordinated
  fits are masked for counts below 50; zero eligible fits failed numerically.
  No optimal threshold or confidence band is reported. PP ordinates use
  i/(m+1), explicitly distinguished from strict empirical survival.
- Max-to-sum: alpha=0.8/1/1.3, minimum one, 30,000 prefixes. Three displayed
  paths per law use independent PCG64 streams 20261030–32; 400 replication
  paths per law use independent streams 20261040–42. Each full path is
  computed, then sampling quantiles are stored at 100 requested log-spaced
  integer checkpoints, with duplicates removed. One replication at a time
  bounds memory. Bands are pointwise 10th/90th percentiles, with the median;
  they are neither confidence nor simultaneous path bands.

## hard_math_claims_for_max_review

These are the precise new display/interpretation locations for the separate
max run. They mostly illustrate existing page results; numerical tests and
figures do not replace mathematical review. Line numbers refer to this
uncommitted implementation.

| Location | Claim or convention to review |
| --- | --- |
| `content/incerto-pareto.md:110` | Log-log survival slope is −alpha; the density exponent is −(alpha+1), with lower cutoff one. |
| `src/math/incerto/distributions.py:27` | GPD support and zero-shape limit; endpoint CDF/survival and possible density divergence for xi < −1. |
| `src/math/incerto/distributions.py:39`; `content/incerto-generalized-extreme-value.md:78` | GEV shape translation c=−xi and the direction of the shape-dependent support boundary. |
| `src/math/incerto/distributions.py:53`; `content/incerto-frechet.md:154` | Fréchet parameterization; normalized exact Pareto maxima and finite-block support n^(−1/alpha). |
| `content/incerto-double-pareto.md:109` | Signed shifted construction, whole-real support, and right-tail probability half the absolute-tail probability. |
| `content/incerto-hill-estimator.md:158` | Exact-Pareto and mixture tail target xi=1/1.7; mapping k to the actual threshold without treating a plateau as a unique selector. |
| `content/incerto-mean-excess-function.md:162` | Increasing/flat/decreasing population mean excess; conditioning below the uniform endpoint; infinite Pareto mean excess for alpha ≤ 1. |
| `content/incerto-tail-threshold-selection.md:142`; `src/math/incerto/estimators.py:330` | Shared thresholds/counts, Pareto references only above the join, and GPD modified scale beta(u)−xi*u. Numerical fit success has no global-optimum or model-validation guarantee. |
| `content/incerto-tail-threshold-selection.md:163` | In-sample PP plotting positions and their limited interpretation after parameter fitting. |
| `src/math/incerto/estimators.py:306`; `content/incerto-max-to-sum-ratio.md:134` | Running-ratio arithmetic/zero prefixes; pointwise ensemble quantiles and interpretation below/at/above the mean boundary. No limit-of-one claim below alpha=1. |
| `content/incerto-regular-variation.md:196` | Valid normalized log-corrected survival and doubling ratio tending to one quarter; explicit distinction from the earlier exponent-1.5 example. |

## Verification and limits

- `UV_CACHE_DIR=/tmp/m05-uv-cache uv sync --locked --offline` passed using the
  existing cache. An initial online resolution failed at DNS; no dependency
  versions were changed to work around it.
- All four producers executed. The focused tests run each producer twice in
  fresh interpreters and compare bytes both between runs and against the
  repository SVGs. All twelve new/changed assets pass, with fixed hash salt,
  bundled fonts and no timestamp. The other glossary asset was regenerated
  only in scratch space and verified byte-identical to its repository copy.
- `MPLCONFIGDIR=/tmp/incerto-p1-mpl UV_CACHE_DIR=/tmp/m05-uv-cache uv run python scripts/regenerate_incerto_outputs.py`
  executed all **105 snippets** and the existing NYC full-demo output.
  Fifteen new snippets were added; outputs on nine changed pages were
  regenerated from execution. Plain-number, API-link, visible-code and
  dropdown conventions pass the existing snippet suite.
- `MPLCONFIGDIR=/tmp/incerto-p1-mpl UV_CACHE_DIR=/tmp/m05-uv-cache uv run pytest`:
  **715 passed in 96.00 seconds**, including **40 P1 tests**. No warnings in
  the final full run.
- All twelve SVGs were rasterized with system librsvg/Cairo at **390 px and
  900 px**, producing 24 PNGs in `/tmp/incerto-viz-p1-render/`, and visually
  inspected. The scratch renderer is `/tmp/render-incerto-p1.py`. Inspection
  caught crowded log ticks on the threshold figure and undersized text on
  the reused ratio figure; both were repaired, regenerated and reinspected.
  No overlapping legends, cropped labels or missing curves remain in the
  reviewed PNGs. ImageMagick's first conversion was visibly defective and
  was superseded by librsvg; it was not used as verification evidence.
- `git diff --check`, separate whitespace checks for new files, relative-link
  and figure-target checks passed. New sources, tests and complete record
  were reviewed, alongside the tracked diff and rendered SVGs.
- Full MyST site build, assembled-HTML checks, browser navigation and live
  publication were **not run**. The standard multi-site builder deletes
  intermediate directories, so it was not used under the no-deletions
  instruction. PNG inspection does not establish full page/browser behavior.
- No new external mathematical consultation or Lean verification was run.
  The following Max review supersedes the initially pending mathematical gate.

## Max review

2026-10-20. Xiang selected GPT-6-Astra at MAX for this review. Reviewed the
router, both rule bodies, track guidance, record, tracked diff, all new Python
files, and all twelve P1 SVGs. Initial work was copied to
`/tmp/incerto-max-review-initial/` for comparison; the existing uncommitted
P1 work was preserved. No staging, commit, deletion, or publication.

Verdict: the P1 mathematical claims and displayed computations pass after
the small corrections below. The Fréchet adapter has an inherited SciPy
limitation outside the displayed grids; that remains a decision for Xiang,
not a claim of numerical correctness over all finite inputs.

### Helpers

| Item | Verdict | Evidence and qualifications |
| --- | --- | --- |
| `generalized_pareto` | Pass | Checked PDF/CDF/SF against the closed forms at scale 2, below support, at zero, in the interior, at/beyond the negative-shape endpoint, and just inside it. Support is `[0, inf)` for nonnegative shape and `[0, -beta/xi]` otherwise. Shapes −2/−1/−0.5 distinguish infinite/constant/zero endpoint density. The zero-shape exponential formulas and two-sided `xi=±1e-10` limits pass for all three methods. |
| `generalized_extreme_value` | Pass; endpoint documentation corrected | The transformation is `c=-xi`. Positive shape has a left endpoint; negative shape has a right endpoint. Checked location 2/scale 3 against the page formula, normalization, both CDF/SF extensions, and the Gumbel PDF/CDF/SF limit. Additional scale-4 checks at shapes −2/−1/−0.5 distinguish the one-sided density limit from SciPy's assigned value at the endpoint: for `xi<-1` the former is infinite but the latter is zero. This is a permissible single-point density convention, not missing probability mass. |
| `frechet` | Qualified pass | `invweibull(alpha, scale=s)` has CDF `exp(-(y/s)^(-alpha))`, positive interior support, and GEV coordinates `(xi, mu, sigma)=(1/alpha, s, s/alpha)`. PDF/CDF/SF, support, scale, normalization, boundary values and small right tails pass for the card exponents. Extremely small positive arguments can produce a spurious NaN density in SciPy 1.18.1; see the decision below. |
| `max_to_sum_path` | Pass | Each output is the prefix maximum divided by that prefix's sum. Direct arithmetic, zero prefixes, all-zero input, scale invariance, final-ratio identity, invalid inputs, overflowing raw sums and tiny early values before a huge later record are covered. Log accumulation preserves the intended ratios without using future data. |
| `gpd_threshold_fit` | Corrected; pass | Strict excesses and `floc=0` agree with the page convention; deterministic quantile fits recover negative/zero/positive shapes. Modified scale is `beta(u)-xi*u`, which may be negative. Count masking, constant excesses, invalid support/scale/location/parameters and capped-optimizer failure are covered. Overflow while subtracting a finite threshold previously escaped as `FloatingPointError`; it now returns failure status, NaN parameters and the strict count. Success still means a usable numerical fit, not a global MLE or tail-model validation. |

The shared scalar validator now translates conversion failures (including
`None` and integers too large for float) into the documented `ValueError`.
No distribution parameterization or ordinary fitted value changed.

### Pages, figures and captions

| P1 item | Verdict | Claim-by-claim check |
| --- | --- | --- |
| 1. Pareto | Pass after caption correction | Log-log survival slope is `-alpha` and density exponent is `-(alpha+1)` for thresholds at least the cutoff. The displayed survival is flat at one below the cutoff, now explicit in the caption. Replaced the stated upper viewport limit of 1 with the lower visible probability: the axes actually allow 1.1 for padding. |
| 2. Generalized Pareto | Pass | Scale 1 and shapes −0.4/0/0.4 give the plotted support, exponential boundary and upper endpoint 2.5. At and above that endpoint CDF/SF are 1/0. Zero survival is masked, with no probability floor. |
| 3. GEV | Pass | At location 0/scale 1, shape 0.3 has lower endpoint −10/3; shape −0.3 has upper endpoint 10/3. Every CDF passes through `exp(-1)` at zero. The log panel contains only positive thresholds. |
| 4. Fréchet and Pareto maxima | Pass | Unit-scale Fréchet survival is asymptotic to a power, not an exact power throughout its support. For normalization `a_n=x_m*n^(1/alpha)`, the finite-block CDF is zero below `n^(-1/alpha)` and `(1-y^(-alpha)/n)^n` above it. Its limit is `exp(-y^(-alpha))`. The second panel correctly plots limit minus finite CDF; the correction is nonnegative. Checked n=1/4/16/64, including points below the finite-block boundary. |
| 5. Shifted double Pareto | Pass | The signed construction is `B*(Y-1)` with an independent equiprobable sign and Pareto minimum 1. Support is all real numbers; the density peaks at zero. For nonnegative x, right survival is `0.5*(1+x)^(-alpha)` and absolute survival is twice that value. The shift explains curvature on the log-log panel. |
| 6. Hill | Pass | Both specified tails have target `xi=1/1.7=10/17`. The plotted k counts the top order statistics; the baseline is `x_(n-k:n)`. Recomputed strict counts and direct log-excess averages at all 157 distinct k values from 170 requests. The realized mixture tail count is 5,344, versus expectation 5,400. A visual plateau selects no unique threshold. |
| 7. Mean excess | Pass | Population curves are `u/0.7` for Pareto 1.7 above 1, 1 for the mean-one exponential above zero, and `(5-u)/2` for uniform `[0,5]` at `0<=u<5`. Independent survival integrals agree. Conditioning at the uniform endpoint is undefined, so it is omitted. Pareto `alpha<=1` gives infinite population excess expectation, while a finite observed sample can still have a finite estimate. Counts and masking agree with the caption. |
| 8. Threshold diagnostics and PP | Pass after axis clarification | One seeded mixture supplies all diagnostics. There are 35 observed thresholds, four with counts below 50, and no eligible numerical fit failures. Pareto references begin at the join; threshold stability gives `beta(u')=beta(u)+xi*(u'-u)`, hence constant modified scale (zero for this exact Pareto tail). PP counts are 17,596/5,344/501 at u=2/3/12. Horizontal values are fitted CDFs and vertical values are `i/(m+1)`; the caption now says so explicitly. These positions and fits give an in-sample check, with no calibrated band or unique-threshold guarantee. |
| 9. Max-to-sum | Pass; limit attribution strengthened | The 400-path bands are pointwise empirical 10th/90th percentiles and medians at 86 distinct integer checkpoints from 100 requests. They are not confidence or simultaneous bands. Finite positive mean implies almost-sure convergence to zero; O'Brien's converse supplies the iff for nontrivial iid nonnegative observations. Exact Pareto alpha=1 converges to zero only in probability, whereas `0<alpha<1` has a nondegenerate weak limit (Darling). No convergence-to-one claim is made. The finite-mean proof itself is unchanged. |
| 10. Regular variation | Pass | `u^(-2)*(1+log(u))` equals one at u=1 and has derivative `-u^(-3)*(1+2*log(u))<0` for u>=1; extension by one below 1 is a valid survival law. Its doubling ratio is `0.25*(1+log(2)/(1+log(u)))`, tending to 1/4. All 161 plotted ratios agree with this expression; endpoints are 0.4233 and 0.2670. The exponent-2/factor-`1+log(u)` distinction from the earlier exponent-1.5 example is explicit. |

The API entries match the helper signatures, exports, methods, support and
failure behavior after the documentation corrections above. The module
summary now says distribution objects: the existing generator objects are
not themselves frozen laws. Every newly added callable has its API anchor
and runnable example. The shared card and vertical layout helpers passed
their grid, support-marker, log-zero and reproducibility checks.

### Limit and source audit

The finite-mean implication follows from the page's Borel–Cantelli and strong
law argument. At exact Pareto alpha=1, put `Z=X/x_m` and truncate at
`b_n=n*log(n)`. Then `E[Z*1(Z<=b_n)]=log(b_n)`, its second moment is
`b_n-1`, and `P(max Z_i>b_n)<=1/log(n)`. Chebyshev's inequality gives
`S_n/(x_m*n*log(n)) -> 1` in probability. The exact maximum CDF gives
`M_n/(x_m*n)` bounded in probability, hence `R_n -> 0` in probability.
O'Brien's converse excludes almost-sure convergence to zero. The finite
simulation is only an illustration of these distinct limits.

Source checks on 2026-10-20:

- The official SciPy [GPD](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.genpareto.html),
  [GEV](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.genextreme.html)
  and [inverse-Weibull](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.invweibull.html)
  documentation confirms the conventions. Installed SciPy 1.18.1 source
  and numerical evaluations establish the endpoint and overflow behavior.
- [O'Brien's publisher entry](https://doi.org/10.2307/3213043) confirms the
  1980 paper, volume 17, pages 539–545, and the probability-limit criterion.
  Its almost-sure iff is explicitly reproduced in the authors' research report
  [Downey–Wright, §1.2](https://www.cs.arizona.edu/sites/default/files/TR94-18.pdf#page=3).
- [Darling's publisher record](https://www.jstor.org/stable/1990824) confirms
  1952, volume 73, pages 95–107. The nondegenerate limit attribution is
  cross-checked in [Fukker–Györfi–Kevei, Remark 5](https://real.mtak.hu/167448/1/1308.0521.pdf#page=25),
  which identifies Darling's Theorem 5.1. The original Darling and O'Brien
  full texts were not accessible through the available web tool; their full
  proofs were not rechecked. The page now gives direct primary citations
  without claiming to prove the converse or the infinite-mean weak limit.

### Fixes and decision for Xiang

Review edits are confined to `src/math/incerto/distributions.py`,
`src/math/incerto/estimators.py`, `tests/test_incerto_viz_p1.py`, the API
reference, Pareto, max-to-sum and threshold-selection pages, and this record.
The existing P1 figure producers and their numerical results are unchanged.

**Decision: retain thin SciPy adapters or add a hardened Fréchet backend.**
In the installed SciPy, `frechet(3).pdf(1e-100)` is NaN with an overflow
warning, although its positive mathematical density is below float range
and should round to zero. Its CDF/SF still evaluate to 0/1. The helper
docstring and API now disclose this inherited limitation. Retaining the
adapter is sufficient for the checked P1 grids; promising reliable density
evaluation throughout the floating-point domain would require additional
implementation and tests. No custom backend or probability clipping was
introduced in this review. The GEV single-point density convention needs
no mathematical correction.

### Verification

- Added 15 regression cases: singular/constant/vanishing endpoint density
  regimes, invalid scalar conversions, excess-subtraction overflow, and
  invalid fitted results. Strengthened existing support and zero-shape
  PDF/CDF/SF checks. The focused numerical run passed **51 tests** with
  the four full-export cases reserved for the full suite.
- Independent numerical checks also covered Pareto slopes, the double-Pareto
  factor, finite-block support and CDF order, GPD threshold stability,
  population mean-excess integrals, Hill baselines/counts, PP fits/positions
  and the normalized log-corrected survival ratio.
- Regenerated the distribution cards/maxima and all threshold/Hill/mean-excess
  SVGs through their demos. All twelve P1 assets still parse and are
  byte-identical to their pre-review versions. Re-rendered all twelve at
  390 and 900 pixels with librsvg/Cairo; inspected all twelve 390-pixel
  images against captions, formulas and producer data. No figure correction
  was needed.
- `MPLCONFIGDIR=/tmp/incerto-max-review-mpl UV_CACHE_DIR=/tmp/m05-uv-cache uv run pytest`:
  **730 passed in 95.26 seconds**, including **55 P1 cases**, with no warnings.
  The four export tests each run their producer twice in fresh interpreters
  and compare all twelve SVGs with both the other run and repository copies.
- `MPLCONFIGDIR=/tmp/incerto-max-review-mpl UV_CACHE_DIR=/tmp/m05-uv-cache uv run python scripts/regenerate_incerto_outputs.py`:
  **105 snippet outputs and one full-demo output regenerated; zero pages
  changed**. Plain-number checks passed. An initial attempt exited with
  signal 15 before any page writes; the complete repeat above succeeded.
- `git diff --check`, separate whitespace checks on all sixteen untracked
  files, changed/new Markdown relative links, figure targets and API anchors
  passed. The index is unchanged and unstaged; the branch remains `viz/p1`.
- No full MyST build, assembled-HTML check, browser-navigation check, wheel
  build, external consultant or Lean verification. No package mapping or
  dependency changed; the standard site builder deletes intermediate
  directories and was not run under the no-deletion instruction.
