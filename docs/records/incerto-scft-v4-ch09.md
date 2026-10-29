# SCoFT v4 chapter 9 checkpoint

2026-10-29. Chunk `scft-v4-ch09`, branch `scft/v4-ch09`, base `0306b19`.
Xiang selected **gpt-6-astra, xhigh reasoning** for writing and code, with a
separate **gpt-6-astra max** mathematical review afterwards. This record
closes the requested teaching and Python implementation, not that later review
or publication. No staging, commit, push, publication or file deletion.

Chosen guide title: **Chapter 9 — Maxima and hidden tails**.
Source units: `scft-v4-ch09` and `scft-v4-appe`; no attached paper units.
The next implementation pointer is `#/chunks/scft-v4-ch10`. Lean is
**skipped-for-now**, as requested; no checked declaration is added.

## Source scope and mathematical distinctions

Read the supplied read-only `2001.10488v4.pdf` and v4 TOC outside the
repository. Chapter 9 occupies printed pp. **171–181** (PDF pp. 185–195);
Appendix E occupies printed pp. **189–191** (PDF pp. 203–205).
The guide maps §9.1, its three subsections, §9.2/9.2.1, §9.3, and E/E.1.
E.1 itself is on **p. 191**, not the appendix's opening p. 189.
The prose, proofs, numerical code and figures are original. Neither source
text nor source images were imported. A 12-word overlap scan of added content
against the inspected source sections found no matches; prose and attribution
were also reviewed manually.

The notes use these qualifications rather than reproducing ambiguous or
incorrect source formulas:

- **§9.1, pp. 171–177:** domain of attraction means a nondegenerate normalized
  maximum limit, not just approaching an endpoint. Regular variation does
  not require its slowly varying factor to approach a constant. A fixed
  block's far-tail exponent and the growing-block Fréchet limit are distinct.
  The maxima Gumbel CDF is `exp(-exp(-z))`. PBDH requires an attraction
  hypothesis; uniform CDF approximation alone does not imply moment convergence.
- **§9.2, pp. 177–179:** the upper-tail Pareto moment of order p is finite
  exactly for p < alpha. A finite integral below a cutoff does not make
  the complementary upper-tail integral finite. Missing probability beyond
  the observed maximum has the exact Beta(1,n) law; multiplying it by n
  gives the rate-one exponential limit. Substituting a limiting Fréchet
  maximum into a finite-sample calculation is an approximation.
- **§9.2.1, pp. 179–180:** the normal calculation integrates over every
  possible maximum, including negative values. A positive upper-tail
  mean contribution is expressed in standard-deviation units, never as
  a fraction of the zero centered-normal mean.
- **§9.3, pp. 180–181:** the empirical measure is a valid probability
  measure. At a fixed threshold its strict exceedance count is binomial;
  the pointwise Bernoulli CLT is distinct from a functional empirical-process
  theorem. The probability integral transform uses F(X), not a fixed F(x).
  A continuous population is not absolutely continuous with respect to a
  finite atomic empirical measure. Small uniform CDF error alone cannot
  control an unbounded payoff.
- **Appendix E/E.1, pp. 189–191:** the exact inverse-gamma sampling law
  requires an exact Pareto model and a specified fixed cutoff or fixed
  retained count. Multiplying the estimate by (m−1)/m retains inverse-gamma
  shape m and changes its scale to (m−1)alpha. Conditioning above 1+epsilon
  and clipping at that boundary are different experiments; clipping creates
  an atom. Neither makes an ordinary sample-mean bias claim valid.

Opened Gasull, Jolis and Utzet's primary preprint **arXiv:1308.5541v1**,
§2, pp. 3–4, Eqs. (7)–(9), for the quantile/Mills normalizing constants;
the local bibliography records that version alongside the published article.
Also checked Durrett's January 2019 manuscript, **Theorem 3.4.1, p. 144**,
for the iid finite-variance CLT. The new model calculations have local proofs.
Attempts to retrieve the general PBDH/GEV/Hill-consistency sources were blocked
by publisher access, bot challenges or network restrictions. Their precise
full-theorem locators, the Fréchet converse and the earlier Darling original
remain **unverified**, under M05-ISSUE-006. No guessed theorem numbers were added.

## Teaching and integration

New pages:

- [Chapter 9 guide](../../content/incerto-scoft-ch9.md), including an exact
  finite-sample comparison and the v4 section/page map.
- [Tail beyond the sample maximum](../../content/incerto-hidden-tail.md),
  containing the missing-mass proof, hidden moments, normal comparison and
  empirical-CDF counterexample.

All nine required canonical pages were extended:

| Program concept | Page and chapter-9 addition |
| --- | --- |
| `c-gev` | [GEV](../../content/incerto-generalized-extreme-value.md#gev-gaussian-maxima): exact normal maxima, two normalizations, convergence proof and error curves |
| `c-frechet` | [Fréchet](../../content/incerto-frechet.md#frechet-regular-variation): sufficient regular-variation argument and fixed-block tail |
| `c-pbdh` | [PBDH](../../content/incerto-pickands-balkema-de-haan.md#pbdh-chapter-nine): assumptions, normal excess limit and exact bounded example |
| `c-gpd` | [GPD](../../content/incerto-generalized-pareto.md#gpd-moment-integrals): survival integrals and moment boundaries |
| `c-evi` | [EVI](../../content/incerto-extreme-value-index.md#evi-chapter-nine): Pareto, normal and uniform shape conventions |
| `c-hill` | [Hill](../../content/incerto-hill-estimator.md#hill-sampling-law): exact sampling density, bias, moments and stable arithmetic; additions only |
| `c-mean-excess` | [Mean excess](../../content/incerto-mean-excess-function.md#mean-excess-hidden-tail): conditional overshoot versus unconditional hidden contribution |
| `c-threshold` | [Threshold choice](../../content/incerto-tail-threshold-selection.md#threshold-chapter-nine): fixed k, fixed threshold, selection and ties |
| `c-plugin` | [Plug-in estimation](../../content/incerto-plug-in-tail-estimation.md#plugin-hidden-tail): missing contribution, debiasing, conditioning and clipping |

The hidden-tail page is a supplementary treatment for existing program
concepts, with a graph node `hidden-tail`; it does not introduce a new
program ID or enlarge the frozen M0.5 inventory. Program totals stay at
**103 IDs**, **75 active**, **35 registered existing concept bodies**.
The regenerated graph has **43 nodes, 74 dependency edges, 91 reference
edges**, with other relationship types counted separately.

Updated the explicit MyST TOC, Incerto hub, theorem/method indexes, SCoFT
overview, API reference, local bibliography, generated graph/list, planning
index and program human views/state. Earlier mathematical material is linked.
The two protected power-law pages and their demos/figures are unchanged.

## Helpers and figures

[extremes.py](../../src/math/incerto/extremes.py) adds seven public helpers:

| Helper | Calculation and limits |
| --- | --- |
| `pareto_hidden_moment` | Exact tail integral, including infinite moments; representational overflow raises |
| `expected_pareto_hidden_fraction` | Exact beta-function expectation; undefined fraction is NaN |
| `maximum_missing_mass` | Frozen Beta(1,n) law for iid continuous parents |
| `pareto_exponent_sampling` | Frozen inverse-gamma law, with optional scale-only bias correction |
| `gaussian_maximum_norming` | Quantile/Mills or explicit asymptotic constants; n≥3 |
| `gaussian_maximum_cdf` | Exact normal maximum CDF in logs, including infinite endpoints |
| `expected_gaussian_hidden_mean` | Numerical quadrature of an exact integral after an exponential-variable transform; estimated error returned |

Counts are bounded by 10^9. Floating-point evaluation is not interval
certification. API examples expose invalid inputs, NaN/infinite results and
numerical overflow with real output. Every reader-facing package import has
an API anchor; long examples use dropdowns.

[estimators.py](../../src/math/incerto/estimators.py) now computes Hill values
from nonnegative weighted adjacent log spacings. It uses `log1p` for nearby
values and log differences for widely separated values. This removes the
cancellation that produced negative/positive noise for constant samples,
without clamping away positive spacing in near ties.

All four SVGs come from [extreme_values.py](../../demos/incerto/extreme_values.py)
through the shared `src/math/incerto/figures.py` theme/export functions:

| File under `assets/figures/incerto/` | Reader page | Evidence |
| --- | --- | --- |
| `gaussian-maxima.svg` | GEV | Exact CDF/density versus Gumbel; n=10,100,10000, error panels n=100, z in [−3,5] |
| `hidden-tail-pareto.svg` | Hidden tail | Exact expected fractions and 10th/median/90th quantiles; n=10 to 10^6 |
| `hidden-tail-normal.svg` | Hidden tail | Quadrature for n=10 to 10^5, plus the conditional new-record mean |
| `hill-sampling-law.svg` | Hill | Exact densities/quantiles plus 4,000 fixed-k fits for each k=5,30, sample size 200 |

Only the Hill comparison is simulated: **1,600,000 scalar draws**, PCG64
seeds **2026102905** and **2026102930**, true alpha=1.5. All 8,000 fits
are retained and finite. The reported medians are 1.611 and 1.515; these
are numerical checks, not proof. The largest reported normal-integral
absolute error on the figure grid is **9.2e-11**, an estimate, not a bound.

## hard_math_claims_for_max_review

Line numbers below refer to this checkpoint's working files. Read the full
statement and assumptions, not just the line indicated.

| ID | File:line | Claim and evidence status |
| --- | --- | --- |
| CH09-C01 | `content/incerto-frechet.md:179` | Regular variation plus an admissible normalization gives Fréchet attraction; fixed-n maximum retains the tail exponent. Original sufficient-direction proof; converse remains cited. |
| CH09-C02 | `content/incerto-generalized-extreme-value.md:158` | Mills-ratio and explicit log-log normalizations give the same maxima Gumbel limit. Original proof using normal-tail bounds; exact CDF/density numerically compared. |
| CH09-C03 | `content/incerto-pickands-balkema-de-haan.md:142`; `content/incerto-extreme-value-index.md:237` | Normal excess scaling and bounded-uniform GPD/GEV examples. Exact/special-case proofs; general PBDH and GEV classification remain cited, with source-locator limits above. |
| CH09-C04 | `content/incerto-generalized-pareto.md:168`; `content/incerto-mean-excess-function.md:199` | GPD mean/second moment boundaries and the survival-times-threshold-plus-overshoot identity. Original integrations and decomposition. |
| CH09-C05 | `content/incerto-hidden-tail.md:23` | Exact Beta missing-mass law, next-record probability and exponential scaling limit for continuous iid samples. Original probability-transform proof. |
| CH09-C06 | `content/incerto-hidden-tail.md:73` | Pareto hidden moment, power-of-Beta fraction, gamma-ratio expectation and decay; requires p<alpha. Original derivation; not a sample-mean bias correction. |
| CH09-C07 | `content/incerto-hidden-tail.md:170`; `src/math/incerto/extremes.py:148` | Exact normal hidden-mean integral and exponential transform, plus conditional new-record interpretation. Proof of identities; quadrature is numerical. |
| CH09-C08 | `content/incerto-hidden-tail.md:230`; `content/incerto-scoft-ch9.md:68` | Fixed-threshold Bernoulli CLT versus random-maximum behavior; CDF/moment counterexample and absolute-continuity limitation. Elementary proof plus cited CLT. |
| CH09-C09 | `content/incerto-hill-estimator.md:196`; `src/math/incerto/estimators.py:72` | Fixed-cutoff and fixed-k gamma pivot, inverse-gamma moments/debiasing, delta limit, weighted-spacing identity and arithmetic. Original proof; simulation and high-precision numerical regressions. |
| CH09-C10 | `content/incerto-plug-in-tail-estimation.md:319`; `content/incerto-tail-threshold-selection.md:227` | Adding known hidden contribution biases an unbiased sample mean upward; conditioning versus clipping; fixed-count calibration does not survive arbitrary selection. Original identities and stated limits. |

## M0.5 issues

The [review](../plan/incerto-program/m0.5-review.md) and state record all nine
assigned issues. **011 is now fixed** by the spacing implementation and
constant/near-tie/scale tests. **001, 003, 005, 008 and 010** retain their
earlier resolutions with chapter-9 qualifications: known-cutoff assumptions,
rank versus strict survival, reader-facing prose, nonmonotone finite-endpoint
mean excess, and bootstrap limits. **006** remains open for unchecked general
theorem locators; **007** now has verified chapter-9/E locators but retains
the wider legacy-reference audit; **014** retains the Amazon/NYC rank-label
work assigned to chapter 10. No empirical label fix or new financial study
is claimed. Totals are **12 fixed, 3 assigned, 0 awaiting a Xiang decision**.

## Verification and limits

- `UV_NO_SYNC=1 UV_CACHE_DIR=/tmp/ch09-uv MPLCONFIGDIR=/tmp/ch09-mpl uv run pytest`:
  **1,239 passed in 189.82 seconds**. This includes **63 new cases**, all
  exact page-output checks, existing estimator regressions, graph checks,
  and two fresh-process exports matching all four SVGs byte for byte.
- `scripts/regenerate_incerto_outputs.py`: **172 snippet outputs and one
  full NYC-demo output** regenerated on the final run, with no further changes.
  The first run regenerated 171 snippets and changed seven pages. Protected
  power-law pages remained byte-identical to the branch baseline.
- `uv run python scripts/build_concept_graph.py`: regenerated the graph and
  concept list. No new concept IDs were invented in program state.
- All four figures rendered to PNG at **390 and 900 px** and all eight PNGs
  inspected. Labels, legends, bands, axis units and panels are legible.
- **100 display blocks** across changed/new content pages parse with
  KaTeX **0.16.25**. Long rows were split with short alignment columns.
  These source/parser checks do not certify actual page widths.
- State/human-view validation passed, including **1,171** local links. The
  changed/new-file audit checked **1,596** links and package API anchors,
  bibliography keys, figure paths, additive Hill scope and new-file whitespace.
  `git diff --check` passed. Full new files and the diff were reviewed.

`uv sync --locked` failed fetching python-dateutil because DNS/network access
was unavailable. Tests used an editable install of this checkout with available
dependencies; no dependency manifest or lockfile changed. Actual versions:
Python **3.13.5**, NumPy **2.5.4**, SciPy **1.18.1**, Matplotlib **3.11.2**,
pytest **9.0.3**, PyYAML **6.0.3**. This is not a locked-environment pass.

In `/tmp/ch09-site-check`, `npm ci --offline --ignore-scripts` failed because
the pinned MyST archive was absent from npm's cache. Reusing an available
MyST **1.10.1** tree with identical `package-lock.json`, the site builder
failed its **npm Package Not Found** preflight. `npm run check:html` failed
because fresh pages/assets/configs were not built. System Chrome under
Playwright failed with **setsockopt: Operation not permitted** and SIGTRAP.
No fresh HTML, browser-navigation, rendered-page equation, wheel-packaging,
Lean or live-publication verification is claimed.

## Decisions and next action for Xiang

- Run the planned independent max review over CH09-C01–C10 before publication.
- Finish the remaining general-theorem source locators when primary full
  text is accessible. Keep M05-ISSUE-006 open until then.
- Run locked-environment, fresh site/HTML and mobile/desktop browser checks
  in an environment that supports them, followed by reader review after any
  separately authorized publication.
- No title, notation or scope decision is outstanding. Chapter 10 is next;
  its financial analysis and the retained rank-label issue were not executed.

## Max review

2026-10-29. Independent mathematical review using Xiang's selected
**gpt-6-astra, max reasoning**. Reviewed `git status`, the full working diff,
all ten new files, the complete mathematical notes named above, the API
contracts and examples, the changed Hill arithmetic, and every expectation in
`tests/test_incerto_extremes.py`. The starting tree contained 28 modified and
10 untracked files. The verdicts below distinguish mathematical claims from
source-access and numerical-accuracy claims. Repeated formulas are grouped
with their equivalent occurrences; locations refer to the reviewed files.

**Verdict:** the ten CH09-C01–C10 claim families are correct or
correct-with-caveat after the minimal fixes below. Three prose statements
needed correction. The hidden-moment formula was correct, but its floating-point
implementation mishandled cancellation and extreme log powers. The Hill tie
implementation needed no correction. General-theorem source locators remain
unverifiable from the primary full texts available in this review; this is
not a verdict that those theorems are false. No copied book prose or figures
were found.

### Corrections applied

| Location | Original verdict and evidence | Minimal correction |
| --- | --- | --- |
| `content/incerto-hidden-tail.md:240` | **wrong** as written: the antecedent of “Its expectation” was the binomial numerator. A count has mean `n*q` and variance `n*q*(1-q)`. | Assign `q` and `q*(1-q)/n` explicitly to the empirical survival **fraction**. The CLT formula was already correct. |
| `content/incerto-mean-excess-function.md:214` | **wrong** without an exceedance: a nonempty sample entirely at or below the threshold has no empirical mean excess. | Require a nonempty finite **exceedance** sample. |
| `content/incerto-hill-estimator.md:224` | **wrong** if read as a universal prohibition: some data-selected counts preserve calibration. For an exact Pareto sample, the minimum log observation is independent of the upper exponential spacings; choosing `k=1` or `2` using only that minimum preserves the conditional fixed-count law. | Change “does not retain” to “need not retain.” Ordinary selection using the fitted upper-tail curve still requires calibration. |
| `src/math/incerto/extremes.py:61` | **wrong** numerical evaluation: at `x_m=2`, `t=4`, `p=alpha/2`, the answer is exactly 2. The former expression returned `1.6487212707001282` for `alpha=1e16` and 1 for `alpha=1e308`. Adding the small log prefactor before cancelling large powers lost it. | Combine the power terms first, then add `log1p(p/(alpha-p))`. When both products overflow before cancelling, factor out `alpha` for that calculation. |
| `src/math/incerto/extremes.py:63` | **wrong** overflow/underflow handling: `p=0, alpha=1e308, t=10, x_m=1` raised although its probability rounds to zero. Conversely an already positive infinite log power could pass through `exp(inf)` without raising for a finite but unrepresentable moment. | Permit a negative infinite log power to yield zero; explicitly reject a positive infinite log power. Mathematical moment divergence still returns `inf`. |
| `tests/test_incerto_extremes.py:137` | **correct**, new regression expectations. At `p=alpha/2` and `t=x_m**2`, the powers cancel and the prefactor is 2. The probability `10**(-1e308)` underflows; the huge cutoff moment overflows. | Add five cases: four cancellation combinations and one underflow/overflow test. No existing expected result was relaxed. |

### Claim ledger: notes and proofs

All file names in this table are under `content/`. “Correct-with-caveat”
identifies the precise scope or limitation; it does not substitute numerical
agreement for a proof.

| Claim / location | Verdict | Evidence and scope |
| --- | --- | --- |
| C01a — `incerto-frechet.md:17,32,40` — CDF, density, GEV conversion | **correct** | Differentiation gives the displayed density; `xi=1/alpha, mu=1, sigma=xi` makes the GEV support factor equal to `y`. |
| C01b — `incerto-frechet.md:85,125,135` — exact Pareto maximum, table and expansion | **correct** | Independence gives `(1-y**(-alpha)/n)**n` on the stated support. Values for `n=10,100,600` round to `0.348678,0.366032,0.367573`; the logarithmic correction is `-t**2/(2*n)`. |
| C01c — `incerto-frechet.md:103,149` — Fréchet survival and finite-block boundaries | **correct** | `1-exp(-s) ~ s`; the normalized Pareto lower endpoint is `n**(-1/alpha)`. These are population curves, not fitted laws. |
| C01d — `incerto-frechet.md:184` — regular variation implies attraction | **correct-with-caveat** | For the stated admissible `a_n`, `n*barF(a_n*y) -> y**(-alpha)` and `n*log(1-barF(a_n*y)) -> -y**(-alpha)`. Values at nonpositive `y` follow by monotonicity. Existence for arbitrary generalized tail quantiles and the converse are not proved on this page. |
| C01e — `incerto-frechet.md:204` — fixed-block tail equivalence | **correct** | For each fixed positive integer `n`, the binomial expansion gives `1-(1-q)**n ~ n*q`. It preserves the regular-variation exponent and is distinct from growing-block convergence. |
| C02a — `incerto-generalized-extreme-value.md:17,29,33,66` — GEV support and signs | **correct** | Endpoints, the zero-shape limit, the `±0.3` exponents, and `H(0)=exp(-1)` agree algebraically. SciPy's `c=-xi` convention is applied consistently. |
| C02b — `incerto-generalized-extreme-value.md:45,50` — classification and Gumbel parents | **correct-with-caveat** | Normal and lognormal are Gumbel-domain examples. The classification requires an existing nondegenerate normalized iid maximum limit; no such limit is claimed for every parent. Full theorem locator remains unverified. |
| C02c — `incerto-generalized-extreme-value.md:109,139` — Pareto calibration | **correct** | `alpha=9/5` gives `xi=5/9`, scale `x_m*250**(5/9)`, and `(249/250)**250=0.3671424535662421`. The stated normalized GEV location and scale are correct. |
| C02d — `incerto-generalized-extreme-value.md:163,173` — normal maximum and Mills constants | **correct** | `Phi**n` differentiates to `n*phi*Phi**(n-1)`. `b=isf(1/n)` and `a=sf(b)/phi(b)` match Gasull–Jolis–Utzet v1, §2, Eqs. (7)–(9). |
| C02e — `incerto-generalized-extreme-value.md:184` — Gaussian limit proof | **correct** | Integration by parts gives `t*phi(t)/(1+t*t) <= barPhi(t) <= phi(t)/t`. Thus `a*b -> 1`, `a -> 0`, the tail ratio tends to `exp(-z)`, and the maximum CDF tends to the maxima Gumbel CDF. Fixed negative `z` causes no support problem for sufficiently large `n`. |
| C02f — `incerto-generalized-extreme-value.md:205` — explicit constants | **correct** | Expanding the normal-tail logarithm gives the displayed equation for `b_n**2` and error `O((log log n)**2/s_n**3)`. Consequently the scale ratio tends to 1 and the centering difference divided by `a_n` tends to zero. |
| C02g — `incerto-generalized-extreme-value.md:239,248,257` — output, density Jacobian and units | **correct-with-caveat** | Executed outputs agree. The normalized density includes `a_n`; general normal constants are `(sigma*a_n, mu+sigma*b_n)`. The finite grid comparisons provide neither a global supremum nor relative rare-tail guarantees. |
| C03a — `incerto-pickands-balkema-de-haan.md:19,31,43,67` — excess definition and theorem | **correct-with-caveat** | The conditional CDF, positive scaling, absolute supremum difference and endpoint extension agree with the usual PBDH statement. The full MDA assumption is explicit. This page proves special cases, not the full equivalence; original-source locators remain unverified. |
| C03b — `incerto-pickands-balkema-de-haan.md:102,127` — exact Pareto excess and table | **correct** | The survival ratio is `(1+y/u)**(-alpha)`, with `xi=1/alpha` and `beta=u/alpha`. For `alpha=1.7`, the scaled survival at 1 is `2**(-1.7)` for every admissible threshold. |
| C03c — `incerto-pickands-balkema-de-haan.md:152` — normal excess limit | **correct** | Mills bounds give `barPhi(u+y/u)/barPhi(u) -> exp(-y)` for fixed nonnegative `y`. At `y=1`, fresh values for `u=2,4,8` are `0.272950739,0.337483634,0.359560559`. |
| C03d — `incerto-pickands-balkema-de-haan.md:164,177` — Pareto/normal/uniform comparison | **correct** | Normal scale is asymptotically `1/u`; Pareto scale is exactly `u/alpha`; uniform excesses have `xi=-1, beta=b-u`. The printed GPD survivals `exp(-1),1/4,0` use the correct endpoints. |
| C03e — `incerto-pickands-balkema-de-haan.md:195` — CDF versus moment convergence | **correct-with-caveat** | Bare uniform CDF proximity gives no control of unbounded moments. The contamination example proves this metric limitation. It is not a counterexample within the excesses of one fixed MDA parent. Full MDA hypotheses with `xi<1` can supply the needed tail bounds; see the decision below. |
| C03f — `incerto-extreme-value-index.md:17,64,94,111` — EVI definition and exact Pareto normalization | **correct** | EVI is defined through the nondegenerate maximum limit, with `xi=1/alpha` in the regularly varying case. `b_n=c_n, a_n=c_n/alpha` yields the standard GEV. Endpoint approach `F(r)**n -> 0` alone is insufficient. |
| C03g — `incerto-extreme-value-index.md:173,188,218` — moments, Hill and model examples | **correct-with-caveat** | The Hill formula, GPD support examples and `1/1.6=0.625` are correct. At regular-variation moment boundaries the slowly varying factor matters; the GPD's exact boundaries are not asserted universally. |
| C03h — `incerto-extreme-value-index.md:242` — uniform maximum limit | **correct** | The endpoint gap has survival `(1-t/n)**n`. Centering at `b-b/n` and scaling by `b/n` gives `H_-1(z)=exp(z-1)` for `z<=1`, with CDF one above. |
| C04a — `incerto-generalized-pareto.md:17,29,36,66` — GPD law and examples | **correct** | The support, exponential limit, finite negative-shape endpoint and the `xi=±0.4` survival powers agree with direct substitution. |
| C04b — `incerto-generalized-pareto.md:113,128` — threshold stability | **correct** | Dividing survivals gives the same shape and scale `beta+xi*u`; the Pareto special case gives `u/alpha`. All thresholds obey the support restriction. |
| C04c — `incerto-generalized-pareto.md:154,171` — moment integrals | **correct** | Tonelli gives the first two survival integrals. The antiderivative and endpoint evaluation yield mean `beta/(1-xi)` and second moment `2*beta**2/((1-xi)*(1-2*xi))` in their domains. For `xi=.4,beta=2`, mean `10/3` and variance `500/9` are correct. |
| C04d — `incerto-generalized-pareto.md:185,196,212` — existence boundaries | **correct** | Mean diverges at `xi=1`; second moment diverges at `xi=1/2`. For `xi>=1` ordinary variance about a finite mean is undefined, as the page states. Negative shape has bounded support. |
| C04e — `incerto-mean-excess-function.md:17,32,74,114` — mean excess formulas | **correct** | Survival integration yields `u/(alpha-1)`; GPD stability gives `(beta+xi*u)/(1-xi)`. The exponential and uniform table rows, and the strict-count example `(1,2,2,4)`, are correct. |
| C04f — `incerto-mean-excess-function.md:138,149` — bounded endpoint | **correct** | `0 <= e(u) <= x_F-u` proves the endpoint limit. The two-atom example gives `e(.9)=1.1` and `e(1.1)=1.9`, so monotonicity does not follow. |
| C04g — `incerto-mean-excess-function.md:202,212,216` — unconditional contribution | **correct after fix** | Conditioning gives `barF(u)*(u+e(u))`. Exact Pareto first moments diverge when `alpha<=1`; empirical mean excess requires at least one strict exceedance and is undefined at the sample maximum. |
| C05a — `incerto-hidden-tail.md:26,39` — missing mass and record probability | **correct** | For continuous iid parents, the maximum of uniform probability transforms has CDF `v**n`. Therefore `U_n` has survival `(1-u)**n`, Beta(1,n) law and mean `1/(n+1)`. An independent next-record event has that same probability. Strictly increasing `F` is not needed. |
| C05b — `incerto-hidden-tail.md:45,67` — exponential scaling and numeric quantiles | **correct** | `(1-t/n)**n -> exp(-t)` for fixed `t>=0`. The finite law is bounded; the exponential limit is for `n*U_n`. All displayed means and 95th quantiles reproduce. |
| C06a — `incerto-hidden-tail.md:76,84,94` — hidden Pareto moment | **correct** | Direct density integration gives `alpha*x_m**p/(alpha-p)*(x_m/t)**(alpha-p)` exactly for `0<=p<alpha`. At and above the boundary the upper integral diverges for every finite threshold. |
| C06b — `incerto-hidden-tail.md:97,103,105` — random hidden fraction | **correct** | With an independent population draw, division by the finite population moment leaves `R=U**r`, `r=1-p/alpha`. Its CDF is `1-(1-h**(1/r))**n` on `[0,1]`. |
| C06c — `incerto-hidden-tail.md:111,122` — expected fraction and asymptotic rate | **correct** | Integrating `u**r*n*(1-u)**(n-1)` yields the beta/gamma ratio. Stirling's formula gives `Gamma(1+r)*n**(-r)` for fixed `r>0`. The mean case needs `alpha>1`; its exponent tends to zero as `alpha` decreases to one. |
| C06d — `incerto-hidden-tail.md:134,154` — reported values and sampling band | **correct-with-caveat** | The numbers reproduce; the band transforms Beta quantiles monotonically and is sample-to-sample variation, not a parameter-confidence band. Numerical beta evaluation has ordinary rounding error. |
| C06e — `incerto-hidden-tail.md:162` — sample mean unbiasedness | **correct** | For `alpha>1`, linearity gives `E[bar X_n]=E[X]`. The independent-draw tail contribution is a different random quantity. |
| C07a — `incerto-hidden-tail.md:173,180` — Gaussian tail integral | **correct** | Integrating `x*phi(x)=-phi'(x)` gives `T_1(t)=phi(t)` for every real `t`. Multiplying by the exact maximum density and integrating over the whole real line gives the displayed expectation. |
| C07b — `incerto-hidden-tail.md:189,194` — units and exponential transform | **correct** | Centered-normal scaling multiplies the contribution by `sigma`. For `V=Phi(M_n)`, `P(-n*log(V)>w)=exp(-w)`; the inverse map is exact. This quantity is not a fraction of the zero normal mean. |
| C07c — `incerto-hidden-tail.md:213,221` — quadrature and record interpretation | **correct-with-caveat** | The ratio equals the conditional mean of the independent next draw given a new record, and also equals the expected maximum of `n+1` normal draws by exchangeability. It differs from the unweighted average of conditional tail means at realized maxima. The reported integration error is an estimate. |
| C08a — `incerto-hidden-tail.md:233,240` — empirical measure and binomial moments | **correct after fix** | The atomic empirical measure has mass one. Its strict exceedance count is Binomial(n,q); division by `n` gives the stated fraction moments. |
| C08b — `incerto-hidden-tail.md:242,251` — CLT, probability transform and random threshold | **correct** | The iid Bernoulli CLT has variance `q*(1-q)` after square-root-n scaling. It is pointwise. `F(X)` is uniform for continuous `F`, whereas `F(x)` is a constant; strict empirical survival at `M_n` is zero. |
| C08c — `incerto-hidden-tail.md:258` — contamination counterexample | **correct** | The maximum CDF distance is exactly `epsilon`, while the added first moment is `epsilon*epsilon**(-2)=1/epsilon`. No uniform mean-error bound can depend on CDF distance alone. |
| C08d — `incerto-scoft-ch9.md:67` — absolute continuity | **correct** | The complement of the finite sample set has empirical mass zero and continuous-population mass one. Thus population absolute continuity with respect to the empirical measure fails. |
| C08e — `incerto-hidden-tail.md:276` — ranks, ties and empirical bootstrap | **correct-with-caveat** | For ascending rank `i=n`, the plotting survival is `1/(n+1)>0`; strict survival is zero. Resampling the empirical support cannot exceed its maximum. Fitted-parent extrapolation requires the model to permit larger outcomes. |
| C09a — `incerto-hill-estimator.md:33,63,93,135` — Hill coordinate, ties and examples | **correct** | The formula estimates `xi`, its reciprocal estimates `alpha`, and zero log spacing has no finite reciprocal. Pareto log-excesses are Exp(rate alpha). The four-observation table telescopes to the stated multiples of `log(2)`. |
| C09b — `incerto-hill-estimator.md:114` — general consistency | **correct-with-caveat** | Positive iid regularly varying tails and an intermediate deterministic sequence are the standard consistency hypotheses; second-order conditions are not needed for this consistency claim. The precise cited theorem locator remains unverified. |
| C09c — `incerto-hill-estimator.md:203` — known-cutoff Gamma law | **correct** | Independent exponential Laplace transforms multiply to `(alpha/(alpha+s))**m`; hence `T` has Gamma shape `m`, rate `alpha`, and the estimates are `T/m` and `m/T`. |
| C09d — `incerto-hill-estimator.md:215` — fixed-k conditional argument | **correct** | Conditional upper observations, before sorting, have the product truncated-parent law; exponential memorylessness removes the random log threshold. Ordered log-excesses are not falsely called independent. Their symmetric sum has the same Gamma law. |
| C09e — `incerto-hill-estimator.md:226,237` — inverse-gamma density and moments | **correct** | The Jacobian for `T=m/a` is `m/a**2`; integrating powers gives `(m*alpha)**q*Gamma(m-q)/Gamma(m)` for `q<m`, with divergence for positive `q>=m`. |
| C09f — `incerto-hill-estimator.md:247,258` — bias, variance and debiasing | **correct-with-caveat** | The stated means and variances follow from the moment formula. Multiplication by `(m-1)/m` changes scale, not shape. `xi_hat` has mean `1/alpha` and variance `1/(m*alpha**2)`. SciPy prints `inf` for variance at `m=1`; ordinary centered variance is undefined there because the mean is infinite. |
| C09g — `incerto-hill-estimator.md:263,303` — normal limit and pivot | **correct** | The exponential CLT and derivative of the reciprocal give asymptotic variance `alpha**2`. The pivot `alpha*T` is Gamma(m, rate 1). These do not automatically calibrate selected-threshold intervals. |
| C09h — `incerto-hill-estimator.md:312,329` — spacing identity and constant sample | **correct** | Each adjacent gap occurs `j` times in the original top-k sum. All gaps are nonnegative; exact ties give zero. For twenty tens the displayed Hill values and strict-count NaN are correct. |
| C09i — `incerto-hill-estimator.md:224` — data-selected count | **correct after fix** | The general fixed-count guarantee need not survive selection; the minimum-based counterexample above explains why the former categorical wording was too strong. |
| C10a — `incerto-plug-in-tail-estimation.md:48,149` — known-cutoff likelihood | **correct** | The log likelihood is strictly concave in the exponent with optimizer `n/sum(log(X/x_m))` almost surely. The all-cutoff limiting convention and finite-mean boundary are distinguished. |
| C10b — `incerto-plug-in-tail-estimation.md:114,165,192` — plug-in asymptotics | **correct-with-caveat** | Delta variance is `x_m**2*alpha**2/(alpha-1)**4`; at `alpha=1.5,x_m=1` this is 36. Conditioning on finite fits has probability tending to one. The exact-Pareto sample-mean stable scale for `1<alpha<2` is slower. This is not finite-sample MSE dominance. |
| C10c — `incerto-plug-in-tail-estimation.md:219,230,403` — infinite fits and singular moments | **correct** | Nonfinite fits occur exactly when the Gamma log-sum is at least `n`; at true exponent one their probability tends to 1/2. The positive density at `xi_hat=1` makes both conditional first and second plug-in moments diverge. |
| C10d — `incerto-plug-in-tail-estimation.md:260,281,301` — body/tail decomposition | **correct** | The tail contributes its mass times `u*alpha/(alpha-1)` and the empirical body uses divisor `n`. The `.8/.2` mixture has mean `3.4`; the conditional tail mean 9 is not the whole mean. |
| C10e — `incerto-plug-in-tail-estimation.md:322,337` — adding hidden contribution | **correct** | For the stated positive exact Pareto model, the added contribution is integrable, strictly positive, and has expectation `mu*n*B(2-1/alpha,n)`. Adding it to an already unbiased sample mean creates that positive bias. |
| C10f — `incerto-plug-in-tail-estimation.md:344,350,355` — conditioning and clipping | **correct** | Conditioning divides the density above `h` by its survival. Clipping leaves that density intact and places mass `P(A<=h)` at `h`. The decreasing functional `x_m*a/(a-1)` is bounded by `x_m*h/(h-1)` on this domain. Neither operation preserves the exponent's unbiasedness. |
| C10g — `incerto-plug-in-tail-estimation.md:369,391` — selection numbers and sensitivity | **correct** | Retained probabilities `.7495,.5929,.3088` reproduce. The mean derivative is `-x_m/(alpha-1)**2`; an exponent interval reaching one cannot give a finite upper mean bound. |
| C10h — `incerto-tail-threshold-selection.md:230,243` — fixed threshold/count and ties | **correct** | Conditional on a fixed threshold's positive count, exact Pareto log-excesses have the Gamma sum law. For `(1,2,2,4), k=2`, the threshold is 2, one strict exceedance remains, and one Hill log-excess is zero. |
| C10i — `incerto-tail-threshold-selection.md:86,101,118,133` — existing mixture numbers | **correct** | The piecewise survival integrates the uniform body and Pareto tail. Expected counts at `u=3,6,12` are `5400,1662.044958,511.554341`; the `u=2` mean excess is `1.960048426`. Modified GPD scale is constant under threshold changes. |
| C10j — `incerto-tail-threshold-selection.md:74,146,179` — diagnostics and limitations | **correct-with-caveat** | GPD moment boundaries differ from return-level sensitivity; population limits and numerical fit success do not validate a threshold. Plotting positions, strict counts, the fifty-exceedance mask and fitted-data comparison are identified correctly. |
| Guide — `incerto-scoft-ch9.md:34,40,52,58,83` | **correct** | The shared-symbol mapping, gamma ratio, `n^-1` versus `n^-r` rates, moment domain and printed values agree with C01–C10. Chapter/appendix page locators were checked against the supplied v4 PDF. |

### Claim ledger: implementation, tests and generated material

| Location / claims | Verdict | Evidence |
| --- | --- | --- |
| `src/math/incerto/extremes.py:3,16,28,34` — count and parameter domains | **correct** | Integer counts are bounded by `10**9`, booleans are rejected as counts, scalar positive parameters and nonnegative finite orders are checked. The lower norming bound is an API restriction, not a theorem that normal maxima require `n>=3`. |
| `src/math/incerto/extremes.py:40` and `content/incerto-api-reference.md:2518` — hidden-moment contract | **correct after fix**, with numerical caveat | Direct quadrature checks the integral and scaling; the new edge cases check prefactor cancellation and the distinction between mathematical divergence and representational overflow. Logarithmic evaluation is floating-point arithmetic, not arbitrary-precision certification. |
| `src/math/incerto/extremes.py:76` — expected fraction | **correct-with-caveat** | `n*B(n,2-p/alpha)` equals the proved expectation; cutoff cancellation, `p=0` and undefined-fraction NaN are correct. The largest relative error against 60-digit gamma ratios on the review grid was `1.02e-9` at `n=10**6`; this is smaller than the page's printed precision. |
| `src/math/incerto/extremes.py:92` — frozen missing-mass law | **correct-with-caveat** | Beta(1,n) agrees with the exact continuous iid proof. Outside those hypotheses the helper provides no calibration guarantee; special dependence structures would need separate analysis. |
| `src/math/incerto/extremes.py:101` — exponent sampling | **correct-with-caveat** | Shape, scales, debiasing count restriction and overflow rejection agree with the Gamma pivot. The caller must supply the fixed-cutoff or fixed-k sampling interpretation; the helper cannot infer it. |
| `src/math/incerto/extremes.py:122,142` — normal constants and maximum CDF | **correct** | Independent normal-tail calculations check the constants and CDF. Scalar/array shape, infinite endpoints, rejected NaNs, log evaluation and underflow convention agree with the API. |
| `src/math/incerto/extremes.py:157` — Gaussian quadrature | **correct-with-caveat** | The stable map `isf(-expm1(-w/n))` is algebraically the exact inverse map. Independent original-density quadrature at 60 digits agrees, including `n=10**9`. QUADPACK's error and convergence checks are not rigorous enclosures. |
| `src/math/incerto/estimators.py:40,73,188,229` — Hill docstrings and changed arithmetic | **correct** | The adjacent-gap identity matches the direct order-statistic definition. `log1p` preserves small positive gaps; distant values use log differences without forming an overflowing ratio. Exact ties return zero; reciprocal infinity is intentional. Fresh high-precision checks had maximum relative error `1.81e-16`. |
| `src/math/incerto/estimators.py:111,245,281,321,345,406` — retained estimator contracts | **correct-with-caveat** | Known-cutoff plug-in formulas and singular moments, cumulative means, max/sum conventions, strict excesses, GPD modified scale and support checks are consistent. Numerical optimizer success and empirical diagnostics are explicitly not statistical validity guarantees. |
| `tests/test_incerto_extremes.py:24` — density quadrature and `3**p` scaling | **correct** | Scaling both threshold and cutoff by three multiplies the unnormalized pth moment by `3**p`. All four cases are strictly inside the finite-moment domain. |
| `tests/test_incerto_extremes.py:32` — maximum-quantile integral | **correct** | If `V` is uniform then `F(M_n)=V**(1/n)`; `-expm1(log(V)/n)` is the missing mass. All sixteen expectations agree with independent gamma-ratio evaluation. |
| `tests/test_incerto_extremes.py:42` — Beta law and scaled limit | **correct-with-caveat** | Means, survival `.75**n`, inverse-CDF checks and the `exp(-2)` comparison are correct. Underflow and default absolute tolerances mean this does not certify relative accuracy for arbitrarily tiny probabilities. |
| `tests/test_incerto_extremes.py:51` — Gamma pivot, correction and variance | **correct** | `P(m/T<=a)=P(T>=m/a)`; scaling the estimator changes CDF arguments as tested. The variance formula is tested only for `m>2`. |
| `tests/test_incerto_extremes.py:65` — fixed-k Monte Carlo tolerance | **correct-with-caveat** | Each indicator at an exact quantile is Bernoulli with the stated probability across independent replications. Six estimated-reference standard errors are an implementation check, not proof or a simultaneous confidence band. |
| `tests/test_incerto_extremes.py:76,88` — ties and full float range | **correct** | Direct summation gives the four factors `1,1.5,1.75,1.4` times `log(2)`. Decimal calculations use exact represented floats, and distinct near ties are not clamped to zero. |
| `tests/test_incerto_extremes.py:102` — Gaussian normalization expectations | **correct-with-caveat** | At the quantile, both `sf(b)` and `a*pdf(b)` are `1/n`; maximum CDF is `(1-1/n)**n`, and at zero it is `2**(-n)`. Tolerances and underflow are numerical, not theorem-strength bounds. |
| `tests/test_incerto_extremes.py:115` — Gaussian hidden integral | **correct** | It integrates the original maximum density, independently of the helper's transform. For `n=1`, the value is `1/(2*sqrt(pi))`; the high-precision review also verified the same value at `n=2` by symmetry. |
| `tests/test_incerto_extremes.py:126,137,151,161,170` — boundaries and validation | **correct after implementation fix** | Infinite Pareto moments, undefined moment fractions, SciPy infinite-moment conventions, invalid count/parameter cases, and overflow behavior are intentional. The added regression expectations follow exact algebra, not snapshots of the implementation. |
| `tests/test_incerto_extremes.py:183` — deterministic figure expectations | **correct-with-caveat** | Two fresh processes reproduced all four SVG files byte for byte and omitted timestamps. This verifies reproducibility, not the mathematical meaning of their curves; the latter was checked separately. |
| `demos/incerto/extreme_values.py:25` / `gaussian-maxima.svg` | **correct** | Exact raw CDF, normalizing constants and normalized density Jacobian match the proof. CDF and density errors have the stated sign, grid and block sizes. The SVG's axes and legend agree. |
| `demos/incerto/extreme_values.py:49` / `hidden-tail-pareto.svg` | **correct** | Expected fractions use the exact beta formula; for `alpha=1.5`, hidden-mean quantiles are Beta quantiles to the power `1/3`. The logarithmic sample range, exponents and sampling band match the caption. |
| `demos/incerto/extreme_values.py:71` / `hidden-tail-normal.svg` | **correct-with-caveat** | Multiplication by `n+1` gives the conditional next-record mean. The maximum reported error estimate is `9.161223168963062e-11`, correctly rounded to `9.2e-11`. The axes use standard-deviation units. |
| `demos/incerto/extreme_values.py:86,92` / `hill-sampling-law.svg` | **correct** | Two groups of `4000*200` draws total 1,600,000; seeds and true exponent match. All 8,000 estimates are finite, with medians `1.6107202691909874` and `1.51539200476733`. Density/quantile panels use the correct inverse-gamma laws, and the ECDF includes every estimate. |
| `content/incerto-api-reference.md:2510` — seven added contracts and all outputs | **correct-with-caveat** | Parameter restrictions, returned laws, NaN/infinity meanings, sign conventions and exact-versus-quadrature descriptions agree with the code after correction. All new and retained executable API outputs reproduce; outputs alone are not proof of older algorithms' statistical calibration. |
| `content/incerto-method-concepts.md:24`, `content/incerto-theorem-concepts.md:21`, `content/incerto/index.md:168,188`, `content/incerto-scoft-intro.md:8,32`, `myst.incerto.yml:39,90` | **correct** | These additions route to the relevant notes/guide and preserve their mathematical descriptions. The chapter-9 and appendix page ranges match v4. No independent new theorem is asserted by a navigation link. |
| `assets/data/concept-graph.json:1`, `assets/graphs/concept-list.html:1` | **correct-with-caveat** | Regenerated graph semantics match note metadata: 43 nodes, 74 dependency edges, 91 reference edges, plus 2 application, 1 generalization, 1 proof-dependency and 25 related edges. These edge types are not interchangeable mathematical implications. Graph tests pass. |
| `docs/plan/incerto-program/state.yaml:1`, `README.md:80`, `concepts.md:23`, `inventory.md:3`, `validation.md:26`, `m0.5-review.md:3`, `verification.md:3`, `visualization-review.md:3`; `docs/plan/index.md:3` | **correct-with-caveat** | Executed state/human-view validation confirms 103 IDs, 75 active, 35 registered existing bodies, nine chapter concepts, 12 fixed issues and 3 assigned issues. The added hidden-tail page does not change that inventory. Historical test/build claims remain historical; the “max pending” flags describe the implementation checkpoint and are superseded for this review by this appended section. |

### Independent numerical evidence

The fresh audit used SciPy 1.18.1 and mpmath 1.4.1, not values copied from
the existing tests. Scratch programs and full numeric results are under
`/tmp/ch09-max-review/`; the reproducible formulas, sample sizes and seeds
are recorded here so the conclusions do not depend on those temporary files.

- **Regular variation:** used survival `x**(-1.7)*(1+log(x))` for `x>=1`,
  solving `n*barF(a_n)=1` independently. At `y=.5,1,2,4`, maximum absolute
  CDF errors decrease from `0.0554672` at `n=10` to `0.0105383` at `n=10**9`.
  This supplies a nonconstant slowly varying example. For fixed block size
  seven, the far-tail ratio to `7*barF(x)` is `0.822650,0.993330,0.999995`
  at `x=10,100,10000`.
- **Normal maxima:** a fresh 4,001-point grid on `[-3,5]` gives Mills CDF
  errors `0.0521629,0.0271898,0.0136811,0.00601748` at
  `n=10,100,10000,10**9`. Explicit-constant errors are
  `0.0643758,0.0589154,0.0404583,0.0241956`. These are grid maxima only.
- **GPD moments:** independent survival quadrature at scale 2.3 and shapes
  `-2,-1,-.4,0,.2,.4,.75`, for the finite first/second moments, differs from
  the formulas by at most `1.62e-11` relatively. Divergence boundaries follow
  from the tail powers; they are not inferred from a finite cutoff integral.
- **Pareto fractions:** 60-digit gamma ratios cover counts
  `1,2,10,1000,10**6,10**9` and `(alpha,p)` equal to
  `(1.00001,1),(1.1,1),(1.5,1),(3,2),(1.2,0)`. The largest relative
  difference is `1.02e-9`. Separate 400-digit calculations confirm the
  exact cancellation cases used to repair the hidden-moment helper.
- **Gaussian hidden mean:** original-density integration at 60 digits, over
  the whole real line, covers `n=1,2,10,100,1000,10000,10**9`. The largest
  absolute discrepancy is `1.59e-14`. At `n=10**9`, the independent value is
  `6.08768457851858e-9`, versus helper value `6.08768459076890e-9`, an absolute
  discrepancy `1.23e-17`. This does not certify the quadrature error estimate.
- **Missing mass:** PCG64 seed `2026102941`, 100,000 fresh samples per parent,
  sample size 23, using normal, uniform and inverse-transform Pareto draws.
  The missing-mass KS distances from Beta(1,23) are `0.00298848,0.00203578,
  0.00255305`. The Pareto hidden-fraction sample mean is `0.31094277`, versus
  `0.31101850` exactly, a difference of `-0.217` Monte Carlo standard errors.
  Independent normal next draws give record probability `0.04139` versus
  `1/24`, and conditional mean `1.93470` versus `1.94767` from quadrature.
- **Hill:** PCG64 seed `2026102942`, 60,000 fresh Pareto samples of size 80,
  exponent 1.7, evaluated directly by top log-ratios for
  `k=1,2,5,12,30,79`. All eighteen 10th/50th/90th CDF checks are within
  2.84 binomial standard errors of their exact probabilities. The first 300
  samples at each count agree with the implementation within `4.45e-16`
  absolutely. Exact-float high-precision tie/range checks have relative
  error at most `1.81e-16`.
- **Conditioning/clipping:** PCG64 seed `2026102943`, 200,000 independent
  samples of twenty Exp(rate 1.2) log-excesses, with `A=19/sum(Y)` and
  `h=1.1`. Direct inverse-gamma density integration gives retained probability
  `0.59293203`, conditional plug-in mean `4.81085870`, and clipped plug-in
  mean `7.33025990` for cutoff one. Fresh Monte Carlo gives `0.5935`,
  `4.81750`, and `7.33068`; the common upper bound is 11.

### Sources and originality

- **correct:** rechecked the supplied v4 PDF at printed pp. 171–181 and
  189–191, including E.1 on p. 191. The notes correct, rather than adopt,
  the source's finite-sample exponential missing-mass claim, its hidden-moment
  domain/complement confusion, and its debiased inverse-gamma shape. The
  Gaussian integral includes negative maxima; the empirical probability
  transform and measure-theoretic qualifications are sound.
- **correct:** the normal constants' locator is independently verified in
  [Gasull–Jolis–Utzet v1](https://arxiv.org/pdf/1308.5541v1), §2, p. 3,
  Eqs. (7)–(9); the explicit alternative appears in §5, p. 16. The local
  bibliography explicitly distinguishes preprint locators from publication
  metadata. The January 2019 version of
  [Durrett](https://sites.math.duke.edu/~rtd/PTE/PTE5_011119.pdf), Theorem
  3.4.1, printed p. 144, states the iid finite-variance CLT used here.
- **unverifiable in this run:** the precise original full-theorem locators
  for general PBDH, GEV classification, Fréchet converse and general Hill
  consistency. Project Euclid returned a bot-challenge iframe for both the
  Pickands and Balkema–de Haan papers; the Stanford technical-report copy
  was also inaccessible. The source-locator part of M05-ISSUE-006 stays open.
  The 2015 journal metadata in `content/bibliography.bib:390` was not
  independently retrieved from the publisher; the 2013 primary preprint
  and the formula locators were inspected directly.
- **correct-with-caveat:** no copied book prose was found by manual comparison
  and an independent normalized 12-word overlap scan across 32 changed/new
  textual files against chapter 9 and Appendix E: zero matches. This is a
  bounded originality check, not proof of provenance for every historical
  sentence in the repository. All four SVGs are generated by repository code,
  with different calculations/presentation from the book figures; no source
  image was imported.

### Decisions for Xiang

1. **PBDH moment wording:** decide whether to add the stronger mean-excess
   corollary. For a fixed parent in `MDA(H_xi)` with `xi<1`, the usual
   normalization and tail-quantile bounds yield
   `e(u)/beta(u) -> 1/(1-xi)`. Tail-integrability control is part of that
   proof and can follow from the attraction assumptions; it need not be an
   independent extra hypothesis. The present warning is correct about bare
   CDF proximity and fitted finite-threshold means, but “additional
   tail-integrability conditions” at `incerto-pickands-balkema-de-haan.md:199`
   can be read more broadly. No new general corollary was inserted during
   this minimal-fix review.
2. **Source completion:** retain M05-ISSUE-006 until precise primary
   full-theorem locators can be checked. The local special-case proofs and
   independent calculations do not close that citation task.
3. **Numerical precision policy:** the four-significant-digit demonstrations
   are supported. Decide separately whether the API should promise tighter
   accuracy across every finite floating-point parameter, especially extreme
   cancelling moment powers and large-count beta evaluations. This review
   fixes demonstrated arithmetic failures without adding arbitrary precision
   or claiming uniform numerical error bounds.
4. **Publication/status:** fresh locked-environment/site/browser checks and
   the later live reader review remain outstanding. Program-state pending
   flags were not edited in this mathematical-only pass; reconcile them from
   this record when updating workflow status. No chapter-10 work was performed.

### Verification and final working state

- `UV_NO_SYNC=1 UV_CACHE_DIR=/tmp/ch09-max-uv uv run pytest
  tests/test_incerto_extremes.py tests/test_incerto_estimators.py
  tests/test_incerto_numerical_reliability.py tests/test_incerto_tail_diagnostics.py`:
  **114 passed in 8.93 seconds**, including all 68 extremes cases and the
  two fresh-process SVG reproduction checks.
- `UV_NO_SYNC=1 UV_CACHE_DIR=/tmp/ch09-max-uv MPLCONFIGDIR=/tmp/ch09-max-mpl
  OPENBLAS_NUM_THREADS=1 uv run pytest tests/test_incerto_page_snippets.py
  tests/test_concept_graph.py`: **368 passed in 119.89 seconds**.
  Total for these disjoint affected test selections: **482 passed**.
- Executed `scripts/regenerate_incerto_outputs.py` through `runpy`, with an
  audit hook prohibiting writes to the two protected pages: **172 snippet
  outputs and one full-demo output regenerated; zero page-output changes**.
  The final numerical changes affect no displayed output. All final outputs
  also passed the exact-output tests above.
- Executed the state/human-view validation in
  `docs/plan/incerto-program/validation.md`: passed, including **1,171**
  local file/fragment links and all inventory counts. Inspected all four
  existing 900-pixel PNG previews against their regenerated SVGs and formulas.
- Reviewed the review-only diff and full new files. `git diff --check` and
  separate new-file whitespace checks passed. Both protected power-law pages
  remain byte-identical to the starting review snapshot. No files deleted;
  no staging or commits.
- Changed by this review: `content/incerto-hidden-tail.md`,
  `content/incerto-mean-excess-function.md`, `content/incerto-hill-estimator.md`,
  `src/math/incerto/extremes.py`, `tests/test_incerto_extremes.py`, and this
  record. Existing chapter-9 work remains uncommitted on `scft/v4-ch09`.
- Not rerun: the full repository pytest suite, dependency synchronization,
  fresh site/HTML/browser checks, wheel packaging, Lean or publication.
  The available-dependency tests are not a locked-environment verification.
