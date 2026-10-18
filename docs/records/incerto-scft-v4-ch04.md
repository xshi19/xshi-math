# SCoFT v4 chapter 4 implementation

Date: 2026-10-18 (America/New_York). Branch: `scft/v4-ch04`.
Base: `51a5959` (`origin/main`). Owner-selected model: gpt-6-astra, xhigh.
No subagents, commit, push, or publication. The owner requested a separate
Astra max run for the hard mathematics; that review is completed below.

## Source and teaching scope

Read the supplied read-only `/workspace/scoft-toc/2001.10488v4.pdf`,
chapter 4, printed pp. 69–89 (PDF pages 83–103), and `v4-toc.txt`.
The extraction also included the following blank page. Source text stayed
under `/tmp`; no PDF, TOC, source passage, table or figure entered the tree.
The chapter guide keeps `/math/incerto/incerto-scoft-ch4/` and uses the title
**Chapter 4 — Finite-moment fat tails**. The title covers both the mixture
mechanism and the estimation question without reproducing the long source title.

Drafted the teaching before its helper, demo and tests:

- [Chapter guide](../../content/incerto-scoft-ch4.md): checked v4 reading map,
  short original examples, notation mappings and explicit source qualifications.
- [Variance mixtures](../../content/incerto-mixture-uncertainty.md): absolute
  moment transfer, kurtosis, finite mixtures, gamma/lognormal variance versus
  gamma precision, and the scalar variance–mean gamma calculation moved from
  the guide. The author-controlled adaptation and MIT notice are retained.
- [Body/shoulder note](../../content/incerto-body-shoulder-tail.md): retained
  the scoped normal Taylor argument, aligned positive mixing notation with
  `Y`, added the Student derivative proof, finite-mixture crossings and the
  sufficient interval conditions for Jensen applied to survival.
- [Moment estimation](../../content/incerto-moment-estimation.md): delivers
  the queued Moment-Estimation Failure scope. It distinguishes moment existence,
  estimator variance, consistency, root transformations, exact Gaussian risk,
  missed rare states, plug-in singularities and normalized power means.
- [Dispersion ratio](../../content/incerto-dispersion-ratio.md): documents
  the repaired zero-denominator behavior and links the new estimation note.

The source's scale boundaries are not silently identified with variance
boundaries. Zero mean does not identify an MGF with a characteristic function.
Missing moments do not establish a power law. Around §4.4.3, p. 83, distinguish
the variance of the empirical second moment from the variance of its square
root: the latter is finite whenever the population second moment is finite.
The source's general preference for absolute deviation is not adopted as a
universal estimator comparison. Known-center Gaussian risk calculations name
both the model and squared-error target.

All chapter-4 source context uses `taleb2025scoftv4`, with section/page locators.
The moved Bessel calculation cites checked [DLMF 10.32.10](https://dlmf.nist.gov/10.32#E10),
[10.40.2](https://dlmf.nist.gov/10.40#E2), and
[10.30.2–3](https://dlmf.nist.gov/10.30). These identities are cited inputs;
conditioning and substitutions are derived on the page. No attached paper or
appendix is assigned to this chunk. Cauchy paths and recursive mixing retain
their later chapter scopes.

The new concepts are in the Incerto TOC, distribution/method indexes, hub,
SCoFT overview, API index and regenerated concept graph. Source membership
is 51 Incerto pages, 75 pages overall and 71 flat redirects; these are source
counts, not a successful HTML build. No URL-map, dependency-lock, package
mapping, shared-notation canon or bibliography change was needed.

## Hard mathematics for the separate max review

Review the hypotheses and arguments independently of numerical tests.
The stable IDs below are also recorded in state.

| ID | Claim and scope | Teaching location |
| --- | --- | --- |
| CH04-C01 | Independent centered normal variance mixing transfers every positive absolute moment by Tonelli; finite second mixing moment gives kurtosis $3\mathbb EY^2/(\mathbb EY)^2$. Finite-state examples preserve variance and all exponential moments despite arbitrarily large kurtosis across the family. | [Moment transfer](../../content/incerto-mixture-uncertainty.md#mixture-moment-transfer), [finite states](../../content/incerto-mixture-uncertainty.md#mixture-finite-states) |
| CH04-C02 | Gamma variance has the stated MGF interval; lognormal variance has every power moment but no nonzero MGF argument; gamma precision yields the Student density, exponent and strict moment gate. The variance–mean gamma Bessel density, MGF interval, origin singularities and exponential decay use stated special-function inputs. | [Variance/precision](../../content/incerto-mixture-uncertainty.md#mixture-variance-precision), [gamma extension](../../content/incerto-mixture-uncertainty.md#mixture-variance-gamma) |
| CH04-C03 | Normal variance and scale density curvatures have different zeros; bounded centered perturbations justify a pointwise Taylor remainder; survival curvature and finite-interval Jensen conditions differ again. Finite-mixture crossings need not equal local zeros. | [Normal derivation](../../content/incerto-body-shoulder-tail.md#derivation-of-the-variance-curvature-boundaries), [finite comparison](../../content/incerto-body-shoulder-tail.md#body-shoulder-worked-figure) |
| CH04-C04 | For Student degrees of freedom $\nu>1$, the scale-curvature quadratic gives four boundaries; at $\nu=3$ they are $\pm\sqrt{4\pm\sqrt{13}}$ in scale units. The Gaussian root limit and the exclusion of $\nu=1$ are explicit. | [Student derivation](../../content/incerto-body-shoulder-tail.md#body-shoulder-student) |
| CH04-C05 | Exact iid Pareto $q$th sample moments are unbiased and weakly consistent if $q<\alpha$, but have finite variance iff $2q<\alpha$. The truncation proof needs no finite estimator variance. RMS and sample SD have finite second moments whenever the population second moment is finite. | [Estimator gates](../../content/incerto-moment-estimation.md#moment-estimation-gates), [root distinction](../../content/incerto-moment-estimation.md#moment-estimation-root) |
| CH04-C06 | For known-zero-center iid Gaussian observations, gamma integration gives the exact RMS bias factor and MSE; calibrated mean absolute deviation has the stated exact risk. Under variance mixing the same absolute-deviation calibration targets $\mathbb E\sqrt Y$, not $\sqrt{\mathbb EY}$. | [Gaussian comparison](../../content/incerto-moment-estimation.md#moment-estimation-normal-comparison) |
| CH04-C07 | The rare-variance mixture has second moment 1, fourth moment 77.25 and empirical-second-moment variance $76.25/n$. No wide-state selection has probability $0.99^n$ and leaves conditional expected sample second moment 0.5. | [Missed state](../../content/incerto-moment-estimation.md#moment-estimation-rare-state) |
| CH04-C08 | The known-cutoff Pareto plug-in has infinite conditional first/second moments even among finite fits, because the log-excess average's density is positive at the singular boundary. | [Plug-in comparison](../../content/incerto-moment-estimation.md#moment-estimation-plugin), with the existing full density derivation linked |
| CH04-C09 | Weighted absolute power means increase with order and tend to the maximum; unnormalized finite-dimensional norms decrease, so unit balls expand. Integrability and Cauchy–Schwarz give the unscaled mean-absolute-deviation bounds; Gaussian calibration does not preserve the universal bound. | [Power means](../../content/incerto-moment-estimation.md#moment-estimation-power-means), [different estimands](../../content/incerto-moment-estimation.md#mean-absolute-deviation-is-a-different-estimand) |

## Python and numerical evidence

Helper: [finite_moments.py](../../src/math/incerto/finite_moments.py).
Demo: [finite_moments.py](../../demos/incerto/finite_moments.py).
Tests: [test_incerto_finite_moments.py](../../tests/test_incerto_finite_moments.py).
The dispersion ratio function now belongs to
[stats.py](../../src/math/incerto/stats.py); the existing demo imports it.

The helper evaluates finite-mixture log densities, two-sided log survivals,
absolute moments, exact Pareto empirical-moment variance and normalized
power means. Domain checks reject invalid weights, variances, counts and
nonfinite inputs. Moment nonexistence is distinguished from arithmetic
overflow; counts are at most $2^{53}$. Power means and dispersion ratios
rescale before taking powers, avoiding unnecessary overflow. Zero-weight
mixture components are omitted mathematically, not sampled and discarded.

The chapter demo uses 801 density points, 241 survival thresholds, 801
geometric contour points and fixed curvature/crossing calculations. Its
repeated samples use NumPy PCG64 seed `20261018`, sizes 50/200/1000/5000,
600 replications per law/size, and four laws: unit normal, the specified
rare-state mixture, Pareto(3,1) and Pareto(6,1). No clipping, censoring,
external data or nonfinite removal. Largest sample matrix: 600×5000;
normal runtime is seconds. The bands are sampling-distribution quantiles,
not Monte Carlo confidence intervals or empirical model evidence.

Original SVGs in `assets/figures/incerto/`:
`finite-moment-mixtures.svg`, `finite-moment-curvature.svg`,
`finite-moment-estimation.svg`, and `finite-moment-norms.svg`.

Key outputs:

| Calculation | Result |
| --- | --- |
| Equal-weight variances 0.4/1.6 | Second moment 1; kurtosis 4.08 |
| Rare variances 0.5/50.5, weights 0.99/0.01 | Second moment 1; kurtosis 77.25 |
| Positive mixture crossings, $a=0.1$ | 0.740030686, 2.330737663 |
| Positive mixture crossings, $a=0.6$ | 0.658172404, 2.199288283 |
| No wide state, $n=50$ | 0.605006067 |
| Rare mixture relative second moment, $n=50$ | 10th/50th/90th percentiles 0.399634 / 0.556530 / 1.807717 |
| Same mixture, $n=5000$ | 0.837696 / 0.991985 / 1.144544 |
| Pareto(3,1), second-moment estimator | Target 3; infinite variance at every finite $n$ |
| Pareto(6,1), $n=100$ | Target 1.5; estimator variance 0.0075 |

The 47 new numerical tests compare with independent density integrals,
SciPy Pareto expectations, finite examples, numerical density derivatives,
exact moment boundaries, invalid domains and extreme rescalings. They include
constant, nonconstant/tied and ordinary dispersion cases. None tests an
asymptotic theorem by asserting that one random sample behaves as expected.

## Chapter-3 figure review fixes

The existing [figures.py](../../src/math/incerto/figures.py) is the single
style/export owner. Every Incerto figure generator already called its theme;
all now also use its SVG export helper. Removed per-script hash salts and
centralized stable metadata, timestamp suppression and whitespace handling.
The theme pins bundled DejaVu Serif, normal weight for ordinary text,
labels and titles, consistent `dejavuserif` mathtext, path output and a fixed
hash salt. Mathematical italics and the regular STIX accent/blackboard glyphs
selected by that math fontset remain deliberate symbol forms, not bold text.
No dependency version or host font installation changed.

**Root-cause evidence and its limit:** the reported “input”, “Step k” and
“Horizon N” paths in the baseline SVGs match the bundled regular DejaVu
Serif outlines exactly. The audit found no bold font paths. Thus neither
Charter fallback nor a within-label weight switch is demonstrated by these
files. Browser CSS cannot change their embedded outlines. The old serif
fallback list was host-dependent and is now removed, but calling it the
observed cause would overstate the evidence. The confirmed layout defect was
severe downscaling: a 761.52-point-wide export gave main text as small as
4.10–4.61 pixels at 390 CSS pixels. Rasterization at that size can make
regular serif strokes look uneven; reproducing the exact reader-device
appearance remains a post-publication check.

The lecture figures now use vertically stacked panels at 5-inch source
width. Their exports are 365.52 points wide; smallest main text is about
10.56 pixels at 390px, excluding intentionally smaller mathematical
superscripts. Titles and labels were shortened or wrapped where needed.
The scale/dependence figure has three panels: Pareto survival, any-loss
probability on a linear axis, and total-loss probability on a logarithmic
axis. A $10^{-70}$–1 shared scale had visually compressed probabilities
0.02 and 0.554 into the same upper strip. Separate axes and markers show
the difference; equality at one block is retained. Captions and alt text
name the vertical arrangement and explain the former apparent near-overlap.

Regenerated **all 17 Incerto demo SVGs**: 11 in `assets/figures/incerto/`
and six retained under `assets/incerto/figures/`. The latter reuse the
already committed Amazon/NYC snapshots and existing simulation seeds;
no new data were acquired. Their empirical methods were not revised, and
M0.5 011/014 remain assigned to their original chapter scopes.

Rendered each actual SVG at widths 390 and 900 with system librsvg/Cairo
through `ctypes`, then inspected all 17 in contact sheets and the seven
new/lecture layouts individually at 390px. This is SVG rendering, not a
separate Matplotlib raster export. The outline audit compares every embedded
font glyph with its bundled font's unhinted outline and rejects bold faces.
The baseline glyph comparison and fresh regular/italic checks passed.
Two persistent figure tests check reset of inherited bold/font settings and
byte-identical timestamp-free SVG export. Scratch scripts and previews are
under `/tmp/ch04-*`; they are not published assets.

## M0.5 dispositions and optional Lean

- **005:** chapter-4 guide, concept links and reader wording updated. The
  historical M0.5 live pass remains closed; these edits await a fresh live review.
- **007:** chapter-4 source context pinned with checked v4 locators. The
  shared issue remains assigned to later chapters; no blanket year replacement.
- **013:** resolved with `NaN` for both constant-sample ratios and infinity
  only for positive numerator over zero, with regression tests. The review
  ledger now has 11 resolved issues and four remaining chapter assignments.
- **Lean:** `skipped-for-now`: no installed toolchain and no sandbox network.
  No Lean files or declarations added, and the imported prototype was not built.

## Verification and resume

| Check | Actual result |
| --- | --- |
| Plain `uv run pytest` | Read-only default-cache lock failure. |
| `UV_CACHE_DIR=/tmp/m05-uv-cache UV_OFFLINE=1 uv sync --locked` | Passed; installed this checkout from the existing writable cache. |
| Same environment, `uv run pytest` | **326 passed in 3.88s**, including 47 chapter-4 numerical cases and two new style/export tests. |
| All eight Incerto SVG generators | Passed with local inputs; all 17 SVGs regenerated, repeat hashes and outline checks recorded below. |
| `npm ci --offline --cache /tmp/m05-npm-cache --no-audit --no-fund` | Failed `ENOTCACHED` for MyST 1.10.1. Reused `node_modules` from `/workspace/pub30-math-1792342244` after byte-comparing its package lock. |
| `npm run build` with writable offline uv cache | Blocked at MyST npm preflight; direct child-process probe reproduces `EPERM spawnSync /bin/sh`. No fresh HTML build. |
| `npm run check:html` | Failed on absent fresh HTML/config/assets after the build failure. Its legacy portion checks 64 compatibility pages for 65 mapped rows and skips four pre-existing unresolved rows. |
| State, source links, citations, TOC, source overlap and whitespace | Final source audit recorded below. |
| Full browser equations/navigation, live site review, publication | Not performed. Headless Chrome could not launch in this sandbox; librsvg previews do not establish a live browser pass. |
| Wheel build and Lean | Not run: package mapping unchanged; Lean explicitly skipped. |

Chapter-4 implementation is `done`; `next_chunk` is `scft-v4-ch05` as
requested. Body/shoulder coverage is complete at its contracted scope.
Mixture and moment-estimation concepts remain `in-progress` for their later
chapter extensions, with chapter-4 teaching/Python delivery recorded done.
The frozen M0.5 denominator stays 24; the implemented concept count is 30.
The separate Astra max review is completed below. A successful external site
build/check and post-publication Math Site Editor review remain follow-ups. No new decision from
Xiang is needed for the title, model scopes or figure layout chosen here.

## Final source and artifact audit

- The executable state validator passes, including unique keys, stable IDs,
  source mappings, deliverable statuses, human concept views and **1,011**
  local plan links. It now evaluates reused-page availability in chapter
  order: the newly written moment note is not retroactively counted as a
  chapter-3 prerequisite that existed then. Eleven later chunk reuse lists
  gain the now-available canonical pages; their work remains unstarted.
- The changed/new-file audit checks **55 files, including 10 new files**,
  **637** relative file/fragment links, all 54 content citation-key uses,
  all four chapter titles against the TOC/hub/overview, and all 17 SVG XML
  files. Source membership is 51 Incerto pages, 75 pages across four sites,
  and 71 flat redirects. These counts do not establish generated HTML.
- Manual source comparison and a normalized nine-word overlap scan found
  no matching nine-word passage between the supplied chapter and the four
  chapter-4 teaching bodies (license notices excluded). This supplements
  original drafting and manual review; it is not a copyright classifier.
- All **17 SVG hashes match on a complete second generation**. The outline
  audit verifies **702** embedded glyph paths against bundled regular or
  italic font outlines; no bold face occurs. DejaVu Serif supplies ordinary
  text and most mathematics; its mathtext configuration uses bundled STIX
  regular/italic outlines for a few accents, large symbols and blackboard
  glyphs. Those are mathematical fallback glyphs, not mixed text weights.
- Actual SVG previews at both widths were inspected; the final curvature
  figure was rechecked at 390px after moving the legend clear of the curves.
  Main lecture text scales to at least 10.56px at 390px CSS width.
- Reviewed the diff and full new teaching, helper, demo, tests and record.
  `git diff --check` and separate whitespace/final-newline checks for new
  files pass. Notation canon, URL map, bibliography and dependency locks
  match the base. No deleted or staged files; **45 modified and 10 untracked
  files**, with no commit, push or deployment.

The final prose pass explicitly states finite mean mixing variance in the
survival-Jensen comparison. It preserves the distinction between population
density geometry, numerical illustrations and sampling evidence.

## Max-reasoning math review

Reviewed 2026-10-18 by owner-selected gpt-6-astra at MAX reasoning on the
uncommitted `scft/v4-ch04` worktree. Read root/track guidance, the shared
notation canon, [program notation lock](../plan/incerto-program/architecture.md#urls-notation-and-publication-boundaries),
and proof-writing skill first. Followed the
[chapter-1](incerto-scft-v4-ch01.md#max-reasoning-math-review),
[chapter-2](incerto-scft-v4-ch02.md#max-reasoning-math-review), and
[chapter-3](incerto-scft-v4-ch03.md#max-reasoning-math-review) procedure:
reviewed all 45 tracked-file diffs and all 10 new files, independently derived
the claims, checked sources and numerical boundaries, and inspected all 17
SVGs and their captions. This closes mathematical review. HTML publication
and live reader review remain separate gates.

| Claim | Verdict | Method and scope |
| --- | --- | --- |
| CH04-C01 — Absolute moments, kurtosis and finite states | correct | Independence and Tonelli factor every positive absolute moment, including infinity; substitution in the normal integral gives the gamma constant. Cauchy–Schwarz supplies the first moment when the second is finite. Conditioning gives both transforms with their distinct exponent signs, kurtoses 4.08 and 77.25, and the wider-component density asymptotic. The general two-state family has second mixing moment 1 + (1−p)(1−c)²/p; each fixed p > 0 retains all real exponential moments. The a = 1 limiting atom is correctly excluded from the density formula. Checked density integrals, exact rational arithmetic and all mixture figure points. |
| CH04-C02a — Gamma/lognormal variance and gamma precision | correct | Gamma integration gives the stated power moments and strict MGF interval, with a divergent integral at both endpoints. Completing the square gives the lognormal moments; the positive exponential term eventually dominates the quadratic normal exponent for every nonzero MGF argument. Integrating gamma precision gives the unit-scale Student density, survival exponent ν, strict absolute-moment gate q < ν, and variance ν/(ν−2) when ν > 2. Student polynomial tails likewise exclude every nonzero MGF argument. Checked independent gamma/precision integrals, Gaussian quadrature for lognormal mixing and the Student tail constant. |
| CH04-C02b — Variance–mean gamma calculation | correct | Expanding the conditional Gaussian exponent leaves γx − x²/(2y) − A²y/2. Substitution gives the displayed Bessel coefficient. The MGF interval is exactly (−A−γ, A−γ); the endpoints diverge. Conditional mean/variance give the stated moments. At zero, the integral is finite exactly for λ > 1/2 and gives the displayed value. Below 1/2 the density behaves as a constant times the integrable power \|x\|^(2λ−1); equality gives a logarithmic singularity. The two density tails have factors \|x\|^(λ−1) and rates A∓γ. Checked quadrature across shapes/skews, MGF derivatives, small-argument behavior, signed tail decay and the Laplace reduction. |
| CH04-C02 inputs — Bessel identities | cited-ok | Read [DLMF 10.32.10](https://dlmf.nist.gov/10.32#E10), [10.40.2](https://dlmf.nist.gov/10.40#E2), and [10.30.2–3](https://dlmf.nist.gov/10.30). Their positive-real-argument hypotheses apply. The order symmetry [10.27.3](https://dlmf.nist.gov/10.27#E3) supplies the small-argument case with λ < 1/2. These are cited inputs, not proofs supplied by this page or by numerical quadrature. |
| CH04-C03 — Normal curvature, Taylor expansion and survival Jensen | correct | Independent differentiation gives the density polynomials y⁴−6y²+3 and z⁴−5z²+2, and survival curvature proportional to x²/v−3. Bounded H keeps the Taylor segment in a compact positive variance interval, so its third derivative bounds the pointwise O(τ³) remainder. Jensen requires the stated convex/concave mixing interval and finite mean. Recomputed the 0.2/1.8 density ratio, all four local boundaries, both finite-mixture crossing pairs, and symmetric/asymmetric bounded perturbations. No claim of uniform tail expansion or global Jensen follows. |
| CH04-C04 — Student scale curvature | correct | Logarithmic differentiation gives the stated rational quadratic; for ν > 1 its positive sum/product and discriminant give two positive roots in z². At ν = 3 they are 4 ± √13. Dividing by ν gives the Gaussian scale limit. At ν = 1 the remaining root is z² = 1/3 and the outer pair escapes, so the four-boundary formula cannot include that endpoint. Scale/standard-deviation distinctions are correct. High-precision derivatives and roots agree; the helper's numerical defects are corrected under PY02 below. |
| CH04-C05 — Pareto estimator gates, consistency and roots | correct | Linearity proves unbiasedness for q < α. Independence gives the finite variance formula for 2q < α; the nonnegative one-observation lower bound proves divergence at and above equality. Bounded truncation, Chebyshev, Markov and vanishing integrable remainders prove weak consistency without estimator variance. The linked infinite-mean argument correctly uses a countable sequence of bounded truncations. R_n² = sample second moment and s_n² ≤ sample second moment give finite second moments for both square-root statistics whenever the population second moment is finite. Checked exact Pareto examples, gates and gamma calculations for RMS. |
| CH04-C06 — Gaussian risk and calibration targets | correct | The sum of squared standardized normals is gamma(n/2, 2). Its square-root integral gives b_n; E R_n² = σ² then gives MSE/σ² = 2(1−b_n). Normal absolute moments give A_n's exact risk (π/2−1)/n. The known center and squared-error target are explicit. Under variance mixing, the calibration instead targets E√Y; strict concavity separates this from √EY for nonconstant integrable Y. Independent gamma-density integration and high-precision gamma ratios agree, including n = 1 and the three printed risks. |
| CH04-C07 — Rare-state probabilities and estimator variance | correct | Exact sums give EY = 1 and 3EY² = 77.25, hence variance 76.25/n. Independent selectors give the no-wide-state probability 0.99^n, including 0.605006067 at n = 50. Conditioning leaves iid N(0, 0.5) observations and expected empirical second moment 0.5. Reproduced the seeded quantiles. These quantiles illustrate sampling spread; they do not prove convergence rates or moment existence. |
| CH04-C08 — Conditional plug-in singularity | correct | The known-cutoff log-excess average has gamma shape n and rate nα. Its density is continuous and positive at 1, and P(ξ-hat < 1) is positive. A lower bound on a left neighborhood gives divergent first- and second-moment integrals; conditioning only divides by a finite positive probability. Checked the linked density derivation and logarithmic-coordinate integrals approaching the pole. Removing nonfinite fits does not regularize the conditional law. |
| CH04-C09 — Power means, norms and absolute deviations | correct | Strict Jensen gives increasing normalized absolute power means and the equality condition; the maximum/positive-weight sandwich gives their limit. Coordinate normalization proves decreasing unnormalized ℓ_p values, hence expanding unit balls. The diamond/circle/square areas are 2, π and 4. Integrability and Cauchy–Schwarz prove the unscaled absolute-deviation bounds; the symmetric two-point law disproves a universal Gaussian-calibrated lower ratio of 1. Checked finite vectors, all 801 contour points and exact two-point ratios. |
| CH04-Q01 — Guide, notation, source qualifications and routes | correct | Checked every reading-map locator against the supplied v4 pages. The guide correctly separates scale/variance, variance/precision, MGF/characteristic function, missing moments/power laws, and second-moment/RMS estimator variance. The broader source assertions are qualified rather than adopted. Shared Y, α, ξ, x_m and u retain their roles; A explicitly maps the legacy variance-gamma helper's alpha. TOC, indexes, concept graph and plan references agree. |
| CH04-PY01 — Dispersion helper and M05-ISSUE-013 | corrected | The requested constant/tied 0/0 fix was correct. Additional boundary review found large-offset centering error and possible arithmetic infinities with a positive median deviation. Translate by an observed middle value, rescale, and determine an exactly zero median deviation from a strict majority of equal observations. Constant ratios remain NaN; only a true zero median deviation gives infinity. Unrepresentable finite results raise FloatingPointError. Exact two-point cases, large outliers with small central spacings, ties and overflow cases now pass. |
| CH04-PY02 — Student curvature helper | corrected | The subtractive root lost the inner boundary immediately above ν = 1; the discriminant overflowed at very large finite ν. Rationalized the inner squared root to 4ν/(5ν+1+√((ν+1)(17ν+1))) and divided the coefficients by ν before evaluation. Checks at nextafter(1, 2), 1+10⁻¹² and 10³⁰⁸ agree with independent high-precision roots and the endpoint limits. |
| CH04-PY03 — Mixture density, Pareto gate and power-mean arithmetic | corrected | Halving a standardized normal value before squaring preserves representable log densities near −10³⁰⁸. Comparing 2q with α avoids rounding a subnormal α/2 onto q and falsely declaring infinite Pareto estimator variance. A positive power mean that underflows now raises instead of returning zero. Twelve total regression cases cover these changes and PY01/PY02. Ordinary worked values and all SVG bytes are unchanged. |
| CH04-F01 — Figure data, layout, fonts and captions | correct | Captured numerical line/collection data from HEAD and current generators: all 68 baseline objects match, with maximum normalized rounding difference below 2.4×10⁻¹⁶. The extra object repeats the common-shock line on the separated panel. At k = 40, any loss is 0.554299596 and total loss is 1.099511628×10⁻⁶⁸; the common-shock probability remains 0.02 and both events agree at k = 1. All 17 regenerated SVGs are byte-identical to the input worktree. Captions distinguish model curves, samples and observed data. |

Corrections and numerical evidence:

- In [stats.py](../../src/math/incerto/stats.py), two adjacent floats near
  10³⁰⁰ previously gave dispersion ratios about 1.12838 and 0.953873.
  Every distinct two-point sample instead requires √(2/π) ≈ 0.797885 and
  Φ⁻¹(0.75) ≈ 0.674490. Translation before scaling fixes the discrepancy.
  An observed middle anchor preserves small central spacings beside a large
  outlier; a strict-majority tie check prevents underflow from masquerading
  as a mathematically zero median deviation.
- The same file's Student helper returned inner roots zero at
  `df = nextafter(1, 2)` and nonfinite roots at `df = 1e308`. Stable root
  algebra gives the correct limits, 1/√3 and the Gaussian boundaries.
- In [finite_moments.py](../../src/math/incerto/finite_moments.py),
  `normal_mixture_log_density(1.5e154, [1], [1])` previously raised although
  its log density is representable, about −1.125×10³⁰⁸. For the smallest
  positive float d, α = 5d and q = 2d previously returned infinite estimator
  variance; with n = x_m = 1, the exact target is 5/3 and variance is 20/9.
  Positive power means below the representable range now raise explicitly.
- `UV_CACHE_DIR=/tmp/m05-uv-cache UV_OFFLINE=1 uv run pytest`:
  **338 passed in 3.99s**, including 59 chapter-4 numerical cases (47 original
  plus 12 regressions) and the shared style/export tests. Imports resolve to
  this worktree. No dependency or packaging change was made.
- `/tmp/ch04-max-review/numerical_review.py`: **7,123 assertions passed**,
  using NumPy 2.4.6, SciPy 1.18.1 and cached mpmath 1.4.1 at 80 digits.
  Independent density integrals, numerical derivatives, exact rational sums
  and high-precision evaluations supplement the proofs. Finite-distance
  asymptotic comparisons have their own tolerances; they do not establish
  divergent integrals or limiting theorems.
- `/tmp/ch04-max-review/figure_review.py` reran all eight generators using
  local inputs and unchanged seeds. It compared the 13 existing SVGs' plotted
  data with the committed generators and reproduced all four new figures.
  All 17 hashes match the input files. The data snapshots are unchanged.
- Rendered the actual SVGs with librsvg/Cairo at 390px and 900px and inspected
  all 17 in contact sheets. Rechecked all **702** embedded glyph outlines
  against the bundled regular/italic fonts; no bold outline occurs. The
  vertical lecture layout and separate probability axes are faithful. This
  verifies SVG artifacts, not browser CSS or the reader's device rendering.

Source and repository checks:

- Independently extracted and read the supplied read-only
  `/workspace/scoft-toc/2001.10488v4.pdf`, printed pp. 69–89 (PDF pages
  83–103). Checked section starts at 69, 71, 72, 74, 75, 76, 79, 80, 83,
  84, 87 and 88 against the guide's ranges. The qualifications about
  characteristic functions (p. 72), scale boundaries (pp. 77–78), and
  estimator variance (p. 83) accurately address the source.
- Manual comparison found no copied book prose or close paraphrase.
  Normalized five-/nine-word scans covered changed text additions and full
  new text files. No nine-word match occurred. The only five-word matches
  were the two overlapping fragments of “it is not a power law,” ordinary
  mathematical wording. No source figures, tables or extracts entered the
  repository; source text and scratch scripts remain under `/tmp`.
- State/human-view validation passed with **1,012** plan links. The changed-file
  audit passed **644** relative links, all 54 content citation-key uses, figure
  XML, source membership and whitespace checks. The source layout remains
  51 Incerto pages, 75 total pages and 71 flat redirects. Shared notation,
  bibliography, URL map, dependency locks and package mapping remain unchanged.
  These checks do not constitute a fresh HTML build.

No mathematical item needs Xiang's decision. The external site build/check
and post-publication Math Site Editor/device review remain open; they were
not rerun here. Wheel and Lean builds were not run because their mappings
and sources are unchanged. This review changes the two numerical helpers,
their regression tests, this record and the existing review-status entries.
Teaching formulas, captions and SVG bytes needed no correction. No files
were deleted, staged, committed, pushed or published.

Review-only changed files: `src/math/incerto/stats.py`,
`src/math/incerto/finite_moments.py`, `tests/test_incerto_finite_moments.py`,
this record, `docs/plan/index.md`, and the program's `README.md`,
`concepts.md`, `m0.5-review.md`, `state.yaml`, `validation.md` and
`verification.md`. The full worktree remains 45 modified and 10 untracked
files, with no staged changes.

## Operator rerun outside the sandbox (2026-10-18, America/New_York)

On this branch's working tree (base `51a5959`), clean `_build/`:

| Check | Result |
| --- | --- |
| `uv run pytest -q` | pass: 338 passed, 43 subtests passed |
| `npm ci` | pass |
| `npm run build` | pass; no doi.org lookups |
| `npm run check:html` | pass: 75 pages across four sites, 71 redirects, 60 pages with display math; 4 pre-existing unresolved legacy url-map rows skipped |

The Math Site Editor's live reader review of the new and changed pages and figures is due after publication.
