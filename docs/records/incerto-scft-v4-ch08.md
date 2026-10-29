# SCoFT v4 chapter 8 checkpoint

2026-10-29 (America/New_York). Branch `scft/v4-ch08`, base `22483bb`
from `origin/main`, including chapter 7 and visualization P2. Xiang selected
**gpt-6-astra xhigh** for writing and code; a separate **gpt-6-astra max**
run reviews the mathematical claims afterwards. No delegation, staging,
commit, push, publication or file deletion.

Chosen guide title: **Chapter 8 — How much averaging helps**.
The implementation is complete at the authorized teaching/Python scope;
independent max review and external site verification remain separate gates.

## Contract and sources

Read root/Incerto guidance, all shared rules, notation canon and program
notation lock, the requested program documents/state, chapter 6/7 and
P2/code-visibility records, snippet tests and output regeneration script.
Used concept-page, proof-writing, reading-guide, prose-review/unslop,
git-conventions and hub-publish guidance. Teaching comes before numerical
examples; Lean is **skipped-for-now** as requested. No new declaration is
represented as checked. Dependency mappings, lockfiles, shared notation
and the legacy URL manifest are unchanged.

Read the supplied read-only `/workspace/scoft-toc/2001.10488v4.pdf` and
`v4-toc.txt`. Chapter 8 occupies printed pp. 153–169, PDF pp. 167–183.
Extraction and source-page previews remain in `/tmp`. No book text,
figures or tables are imported. The exposition, proofs and code are original;
source attribution uses chapter/section/page locators and local bibliography
entries. The attached primary paper, arXiv:1802.05495v3, was checked in its
HTML version at the corresponding mathematical scope, §§II–V and appendices
D–G. Its bibliography entry is `taleb2018kappa`; the book remains
`taleb2025scoftv4`. The paper's empirical portfolio assertions are not adopted.

| V4 locator | Printed pages | Treatment |
| --- | --- | --- |
| §§8.1–8.2 | 154–158 | Population MAD, two-index kappa, admissible domain, invariance, monotonic sum MAD and telescoping growth |
| §§8.3–8.3.2 | 158–160 | Exact stable benchmark, qualified attraction, equal-single-MAD Gaussian comparison and minimum integer size |
| §§8.4.1–8.4.2 | 161 | Distribution-body/asymmetry distinction; Student pair formula, cubic sums and anchored logarithmic rate |
| §8.4.3 | 161–162 | Lognormal fixed-law and fixed-size limits |
| §8.4.4 | 162 | Unimodal triangular counterexample and separated normal mixture |
| §§8.5.1–8.5.3 | 162–164 | Independent equal-weight exposures, common-component obstruction and limits of inference |
| §8.6.1 | 164–166 | Original cubic-Student Fourier/MAD derivation and corrected asymptotic constant |
| §8.6.2 | 166–168 | Lognormal third-moment mismatch, direct limit proofs and bounded conditional Monte Carlo |
| §8.6.3 | 168 | Gamma integration-by-parts identity and exponential limit |
| §8.6.4 | 169 | Absolute-normal integral and binomial mixture for every finite sum size |

The stable sum identity and classical CLT are cited structural inputs,
linked to the earlier limit-law page. Their kappa consequences and the
special-case formulas are proved here. General attraction is explicitly
conditional on uniform integrability and normalization growth. Pareto and
lognormal simulation points are numerical estimates, with Monte Carlo
uncertainty distinguished from uncertainty about the assumed model.
Pearson-family and moment-matched lognormal approximations are not treated
as exact sum distributions or certified bounds.

Three source discrepancies require particular attention in max review:

- The exact cubic-Student expression gives
  `log(n)*kappa(1,n) -> 2*log(pi/2)`, not the `pi^2/4` printed at p. 165.
  This follows both from the finite Poisson sum/Stirling calculation and
  the finite-variance absolute-moment limit. The printed page was inspected.
- Under equal single-observation MADs, a constant kappa gives exponent
  `(2-kappa)/(2*(1-kappa))` in the required-size power, rather than the
  source's `1/(1-kappa)`. Using the full cubic-Student curve at Gaussian
  reference size 30 gives the first crossing at 44, rather than 120;
  exponential summands cross at 36. The notes display the preceding integer
  as well, so minimality is inspectable.
- Negative kappa does not require bimodality: the unique-mode triangular
  density has MADs `2/3` and `14/15`, hence kappa about `-0.06004`.

The stable benchmark is **2-alpha**; **1/alpha** is the sum-growth exponent.
The task's suggested `2-1/alpha` is not used. Index one has no finite MAD.
The logarithmic anchored rate is not a normal-CDF or tail-quantile error bound.

## Pages and wiring

New: [kappa](../../content/incerto-kappa.md) and
[chapter 8 guide](../../content/incerto-scoft-ch8.md).
Extended: [moment estimation](../../content/incerto-moment-estimation.md),
including original sample-sufficiency and dependence arguments.
All named package functions on these pages have API links; runnable examples
print actual outputs, including `nan`, `-inf`, `inf`, exceptions and an
insufficient search cap. Long code follows the dropdown convention.

Updated `myst.incerto.yml`, the [API reference](../../content/incerto-api-reference.md),
SCoFT overview, Incerto hub, method/example indexes, local bibliography,
concept graph/list, program README/register/inventory/verification/validation,
visualization review and planning index. The graph has **40 nodes,
67 dependency edges and 79 reference edges**. Program concept bodies
increase from 34 to **35**; the M0.5 denominator remains the frozen 24.

The state marks chapter 8 and its attached paper scope done, advances
`next_chunk` to `scft-v4-ch09`, and retains chapter-8 max review as pending.
Kappa completes its scheduled scope. Moment estimation remains in progress
for chapter 28. The already-completed chapter-7 max review is reconciled
against its existing record; this run does not perform a new chapter-7 audit.
Chapter 9 and later work are not executed.

## Helpers and figures

[concentration.py](../../src/math/incerto/concentration.py) adds nine helpers:
`kappa_from_mads`, `stable_kappa`, `gaussian_sum_mad`, `gamma_sum_mad`,
`student_sum_mad`, `estimate_sum_mad`, `lognormal_sum_mad`,
`normal_location_mixture_sum_mad`, and `gaussian_equivalent_n`.
The API states the centering, scalar domains, count limits, error policies
and population-versus-estimate distinctions. Student has exact formulas
at sizes one/two for admitted degrees of freedom and at every size for
degree three. The general Monte Carlo helper uses a known mean, retains
all draws, and limits work to 50 million observations.

The lognormal estimator conditions on the last mean-one summand and
integrates a bounded lower-deviation payoff. The parent model has unbounded
support; no observation is truncated or discarded. Its reported standard
error describes numerical integration. The integer search requires a
deterministic population-MAD curve. An eight-machine-epsilon log-comparison
tolerance prevents rounded exact equalities from shifting the Gaussian
answer by one; nearer crossings are explicitly indistinguishable.

[concentration.py demo](../../demos/incerto/concentration.py) uses the shared
`src/math/incerto/figures.py` styling/export helpers and produces four SVGs.
All random streams use PCG64; the full demo uses about nine million draws.

| Figure in `assets/figures/incerto/` | Page | Calculation |
| --- | --- | --- |
| `kappa-aggregation.svg` | `incerto-kappa.md` | Exact Gaussian, cubic Student, exponential and stable-index-1.5 curves, sizes 2–1000 |
| `kappa-sample-size.svg` | `incerto-moment-estimation.md` | Minimum integer searches and stable power law, Gaussian reference sizes 2–1000 |
| `kappa-lognormal.svg` | `incerto-kappa.md` | Sizes 2/16, 11 log-scales from 0.2 to 3, 30,000 replications per point, seeds 20261100–20261121 |
| `kappa-shape.svg` | `incerto-kappa.md` | Pareto-3 estimates at sizes 2/8/32/128, 20,000 replications, seeds 20261090–20261093; exact Student/normal-mixture/triangular comparisons |
| `plugin-mean-singularity.svg` | `incerto-plug-in-tail-estimation.md` | Increased panel spacing in `demos/incerto/visualization_p2.py`; values and sample retained |
| `ergodicity-growth.svg` | `incerto-ergodicity.md` | Four-path linewidth 0.7→1.1 and alpha 0.6→0.95 in `demos/incerto/limit_distributions.py`; paths and targets retained |

Monte Carlo bars transform MAD plus/minus two estimated standard errors
through kappa, with the exact single-observation MAD held fixed. They are
diagnostics, not guaranteed coverage intervals. The Pareto/Student example
changes bodies as well as asymmetry and proves no universal skewness ordering.

## hard_math_claims_for_max_review

Line references below identify this implementation; named anchors remain
stable if prose moves. Numerical tests do not substitute for max review.

| ID | Location | Claim and assumptions |
| --- | --- | --- |
| CH08-C01 | `content/incerto-kappa.md:30`; `src/math/incerto/concentration.py:35` | Finite-first-moment domain, location/scale invariance, Jensen/triangle bounds, telescoping growth and the equal-MAD extended limit. |
| CH08-C02 | `content/incerto-kappa.md:117`; `src/math/incerto/concentration.py:71` | Exact stable kappa is 2-alpha for alpha>1, including skew laws; attraction needs uniform integrability and logarithmic normalization growth. |
| CH08-C03 | `content/incerto-kappa.md:157`; `src/math/incerto/concentration.py:109` | Student single and two-summand beta/gamma formulas for nu>1; CF integral and incomplete-gamma/finite-polynomial formulas for cubic sums. |
| CH08-C04 | `content/incerto-kappa.md:233`, `:249` | Cubic limit constant 2 log(pi/2); general finite-variance constant 4 log(sigma sqrt(2/pi)/M(1)), with no CDF convergence-rate inference. |
| CH08-C05 | `content/incerto-kappa.md:275`; `src/math/incerto/concentration.py:89` | Gamma centered absolute moment via integration by parts; exponential anchored constant and Stirling evaluation. |
| CH08-C06 | `content/incerto-kappa.md:350`; `src/math/incerto/concentration.py:162` | Lognormal single MAD; third-moment failure of exact lognormal sum closure; fixed-law n limit and fixed-n small/large log-scale limits. |
| CH08-C07 | `content/incerto-kappa.md:421`; `src/math/incerto/concentration.py:139`, `:162` | Conditional lower-deviation estimator, bounded payoff, known-mean requirement, Monte Carlo SE and numerical failure contracts. |
| CH08-C08 | `content/incerto-kappa.md:479`; `src/math/incerto/concentration.py:209` | Unimodal triangle MAD ratio 7/5 and negative kappa; binomial absolute-normal mixture and kappa tending to negative infinity with separation. |
| CH08-C09 | `content/incerto-moment-estimation.md:295`, `:335`, `:391`; `src/math/incerto/concentration.py:236` | Leave-one-out monotonicity, integrable L1 limit, minimum integer search, corrected constant-kappa exponent and sizes 44/36 at Gaussian size 30. |
| CH08-C10 | `content/incerto-moment-estimation.md:420`; `demos/incerto/concentration.py:1` | Independent equal-weight portfolio identity and common-component MAD limit; exact versus estimated figure curves, error-bar transformation and body/asymmetry caveats. |

Review the implementation's representability limits and deterministic-search
tolerance as well as the mathematical identities. API claims are collected
under the nine `api-` anchors in `content/incerto-api-reference.md`.

## Verification and limits

- `UV_NO_SYNC=1 UV_CACHE_DIR=/tmp/ch08-uv MPLCONFIGDIR=/tmp/ch08-mpl-local OPENBLAS_NUM_THREADS=1 uv run pytest -q`:
  **998 passed, 43 subtests passed in 157.64 seconds**. This includes all
  page snippets, the 77 new helper cases, fresh-process figure byte comparisons,
  existing P2/limit exports and graph/navigation-source tests.
- Helper tests use independent gamma tail integration, Student scale-mixture
  integration, cubic Fourier integration/finite sums, normal-mixture
  quadrature, lognormal conditional quadrature, exact triangular values,
  exhaustive search comparisons, boundary and overflow checks. A first
  normal-mixture quadrature missed a remote peak; integrating in centered
  normal coordinates corrected the test reference.
- `scripts/regenerate_incerto_outputs.py` executes **137 snippets and one
  full-demo output**. Final display rounding is regenerated rather than
  edited by hand. The four affected output pages are kappa, moment estimation,
  chapter 8 and the API reference; earlier output blocks remain unchanged.
  After the final rounding pass, the exact snippet suite passed again:
  **287 passed in 92.09 seconds**. No helper or figure code changed after
  the full-suite pass.
- The six actual new/changed SVGs were rendered with librsvg/Cairo at
  **390 and 900 px** and all twelve final previews inspected. The requested
  panel collision and low-contrast paths are resolved. Mobile heights are
  545/324/323/590 px for aggregation/sample-size/lognormal/shape, 575 px for
  plug-in and 339 px for growth. Previews remain under `/tmp/ch08-previews`.
- Display math in the two concept pages was split conservatively for about
  330 CSS pixels of equation space on a 390-pixel phone. A full browser
  measurement of rendered equations and navigation remains unavailable.
- The executable state/human-view validator passes, including **1,147**
  local plan links. The wider changed-file audit passes **1,282** relative
  links, seven citation uses and six figure embeds across **33** changed/new
  files, including **11** new files. All six changed SVGs parse as XML.
  Source inventories contain **61** Incerto pages, **85** total pages and
  **81** flat redirects. Graph counts agree with the generated artifacts.
- Checked all new source files and the diff; `git diff --check` and separate
  new-file whitespace/control-character checks pass. The two concept pages
  have 37 balanced display blocks. A 12-word overlap scan of the two new
  pages' prose against the chapter extraction found zero matches; this is
  a supplementary check, not a test for every possible close paraphrase.
  Git remains on `scft/v4-ch08` at `22483bb`, with no staged changes or
  deleted files.

The fresh clone had no installed project environment. `uv sync --locked
--offline` with a writable cache could not obtain the locked SciPy artifact.
The current checkout was installed editable without dependency resolution;
available dependencies from the prior local environment supplied the tests.
An initial full run had one Matplotlib font-path failure because the package
was symlinked into that environment. A local copy of the same Matplotlib
package and a fresh font cache resolved it; the final run above passed.
No dependency or lockfile changes were made. This is **not a locked-environment
verification pass**.
Actual versions: Python **3.13.5**, NumPy **2.4.6**, SciPy **1.18.1**,
Matplotlib **3.11.2**, NetworkX **3.7**, pytest **9.0.3**, PyYAML **6.0.3**,
fonttools **4.67.0**, packaging **26.2**, python-dateutil **2.9.0.post0**.

For the site attempt, a scratch copy under `/tmp/ch08-site-check` reused an
available MyST 1.10.1 dependency tree after confirming identical
`package-lock.json`. `npm run build` failed at MyST's “npm Package Not Found”
preflight. `npm run check:html` consequently reported absent fresh pages,
assets and configs. No fresh site build is claimed. Playwright with system
Chrome failed with `setsockopt: Operation not permitted` and SIGTRAP.
No browser, publication, wheel-packaging or Lean pass is claimed.

## Decisions and follow-up for Xiang

- Run the planned independent max review, concentrating on CH08-C01–C10
  and the three source discrepancies above before publication.
- Complete locked-dependency, site-build/HTML and browser checks in an
  unrestricted environment, then perform the usual live reader review after
  any separately authorized publication.
- No additional title or scope decision is needed. Chapter 9 is the next
  implementation chunk; it is not authorized by this checkpoint itself.

## Max review

2026-10-29. Xiang selected **gpt-6-astra, max reasoning**. Reviewed the
33 changed/new files on `scft/v4-ch08`, using `git status`, `git diff`,
the full new files, and the surrounding mathematical arguments. No delegation,
staging, commit, push, publication or deletion. The earlier checkpoint above
retains its historical verification scope; this section records the new review.

**Verdict:** the ten CH08 claim groups are mathematically correct at their
stated scopes, with the qualifications below. All three book corrections are
supported. One numerical defect was wrong and is fixed: Gaussian-equivalent
sample sizes could change when only the measurement units changed. No symbolic
formula, proof, displayed number or test reference value required correction.

### Claim ledger: kappa

Locations refer to the reviewed working files. “Correct-with-caveat” identifies
an interpretation or computational limitation, not an unproved replacement
formula. The rows separate claims within CH08-C01–C08; repeated claims in the
guide and API are covered below.

| Location | Claim | Verdict and evidence |
| --- | --- | --- |
| `content/incerto-kappa.md:33` | Integrability, population centering, sum/average MAD | **Correct.** Triangle inequality makes every centered sum integrable; division by n gives the average MAD. Median deviation and fitted-center deviation are different estimands. |
| `content/incerto-kappa.md:48` | Domain, two-size definition and inversion | **Correct.** Positive strictly increasing MADs make the logarithm positive; solving for the MAD ratio gives the displayed power. Both counts and both indices are necessary. |
| `content/incerto-kappa.md:59` | Adjacent-index source convention, natural logs, “metric” | **Correct.** Printed p. 158 defines the adjacent-size shorthand. Shared notation uses natural logs; no metric-space distance is asserted. |
| `content/incerto-kappa.md:65` | Affine invariance, monotone sum MAD, triangle bound, kappa at most one | **Correct.** Centering removes translations, absolute values supply the scale factor, conditional Jensen increases sum MAD, and M(n) ≤ n M(1). Substitution gives the claimed upper bound. |
| `content/incerto-kappa.md:73` | Telescoping growth | **Correct.** Each term is log(M(n_j)/M(n_{j-1})); intermediate terms cancel. Exact discrete convolution through n=20 also checked both MAD monotonicities and the chain 1,3,8,20, with zero numerical residual. |
| `content/incerto-kappa.md:90` | Boundary outputs, equal-positive extended limit, Cauchy exclusion | **Correct.** As the positive log ratio decreases to zero, kappa tends to negative infinity. Zero or divergent MADs do not define the population index. All displayed outputs reproduced. |
| `content/incerto-kappa.md:120` | Stable scaling, kappa = 2−alpha, Gaussian endpoint | **Correct.** Centering an integrable stable law gives strict n^(1/alpha) scaling. Independent characteristic-function quadrature at alpha=1.3 and 1.7, including nonzero asymmetry parameters, agrees within 9e-13 relative error. The asymmetry parameter is not a finite third standardized moment. |
| `content/incerto-kappa.md:140` | Qualified attraction | **Correct-with-caveat.** Uniform integrability plus weak convergence gives convergence of absolute expectations; log-normalizer growth gives the limit of kappa. This uses the usual nondegenerate stable-limit convention, so $\mathbb E\lvert Z\rvert>0$. A degenerate zero limit would invalidate the conclusion. No general finite-sample rate is claimed. |
| `content/incerto-kappa.md:152` | Same tail exponent can give different finite kappas | **Correct.** Tail asymptotics do not specify the central distribution. The Pareto/Student comparison changes the body and asymmetry together and does not isolate a causal effect of skewness. |
| `content/incerto-kappa.md:160` | Student domain, single MAD and beta-integral proof | **Correct.** Integrating x times the t density gives the gamma ratio for nu > 1. Independent density quadrature at nu=1.1,1.5,2,2.3,3,12,1000 agrees with the helper; the largest relative discrepancy was below 8e-13. |
| `content/incerto-kappa.md:174` | Independent Gamma/Beta decomposition and Student pair formula | **Correct.** The variance of the conditional normal is nu/[2 T B(1−B)]. Its half moment factors into the two stated expectations; gamma duplication gives the displayed ratio. Independent shifted-t absolute-moment quadrature agrees within 1.3e-12. At nu=3 the ratio is exactly 3/2. |
| `content/incerto-kappa.md:198` | Cubic Student characteristic function | **Correct.** Differentiating the Cauchy transform yields the normalized squared-denominator density transform. The local integrable bound justifies differentiation; the residue argument has the stated sign and scale. |
| `content/incerto-kappa.md:208` | Fourier integration, boundary terms, incomplete gamma and finite sum | **Correct.** Integration by parts gives n I_n; substituting t=n(1+u) gives the upper incomplete gamma. Its integer recurrence gives n! n^(−n) sum(j<n) n^j/j!. Exact rational arithmetic for n=1–100 agrees within 5.2e-14. The book's Eq. 8.11 is algebraically equivalent by the incomplete-gamma recurrence. |
| `content/incerto-kappa.md:232` | Poisson/Stirling limit and corrected cubic constant | **Correct.** The Poisson probability tends to 1/2, giving M(n)/M(1) asymptotic to sqrt(pi n/2). Hence log(n) kappa tends to 2 log(pi/2) = 0.9031654105789097, not pi²/4 = 2.467401100272340. Independent rescaled Fourier quadrature confirms the MAD asymptotic. |
| `content/incerto-kappa.md:243` | Anchored kappa is not a CDF or tail-quantile error bound | **Correct.** It is a ratio of two first absolute moments. Its logarithmic rate alone provides neither of those distributional error controls. |
| `content/incerto-kappa.md:252` | Finite-variance UI bound, absolute-moment CLT and general constant | **Correct.** $\mathbb E[\lvert Y_n\rvert\mathbf1_{\lvert Y_n\rvert>K}]\le\sigma^2/K$ supplies UI. Thus M(n)/sqrt(n) → sigma sqrt(2/pi); substituting the logarithmic expansion gives 4 log(c/M(1)). This constant may be negative or zero; the zero case supplies no nonzero leading rate. |
| `content/incerto-kappa.md:278` | Gamma shape/scale convention, convolution and MAD | **Correct.** Summing iid same-scale gammas adds shapes. The upper-deviation integral and incomplete-gamma recurrence give 2 theta a^a exp(−a)/Gamma(a). Independent 70-digit density quadrature includes shape 1e-6 and total shape 1e13. |
| `content/incerto-kappa.md:295` | Exponential asymptotic, positive finite kappa, tail classification | **Correct.** M(1)=2 theta/e and sigma=theta give 4−2 log(2 pi) = 0.3242458671813090. For integer n, the increment of log(M(n)/sqrt(n)) is (n+1/2) log(1+1/n)−1 > 0, proving positive finite kappa. The exponential has a positive-range MGF and convolution-tail ratio (1+lambda x)/2, which diverges rather than tending to one. |
| `content/incerto-kappa.md:315` | Gaussian/Student/exponential outputs and aggregation caption | **Correct.** All nine rounded kappas reproduced. The stable-1.5 curve has sum exponent 2/3 and kappa 1/2; scaling single MADs to one makes the upper curves relative average errors. |
| `content/incerto-kappa.md:353` | Lognormal parameters, mean and single MAD | **Correct.** Gaussian exponential tilting at Z=sigma/2 gives 2m[2 Phi(sigma/2)−1]. The parameters are log-location/log-scale, not the observable mean/SD. |
| `content/incerto-kappa.md:368` | Third-moment obstruction to lognormal sum closure | **Correct.** The mean-one third centered moment is v²(v+3); averaging divides it by n² and variance by n. The two displayed skewnesses differ for v>0, n>1. This rules out exact closure without claiming an approximation-error bound. |
| `content/incerto-kappa.md:385` | Fixed-law large-n and fixed-n small-scale limits | **Correct.** Finite variance supplies the first limit. The displayed L² error identity follows from E[Z V_sigma]=sigma; finite sums then have the Gaussian MAD ratio sqrt(n). |
| `content/incerto-kappa.md:405` | Fixed-n large-scale limit, order of limits, Gaussian attraction | **Correct.** V_sigma → 0 almost surely under the fixed-normal coupling. Bounded convergence applies to min(T_sigma,n), not to T_sigma itself. Its mean stays n, so the MAD ratio tends to n and kappa to one. All fixed lognormal laws still have finite power moments. |
| `content/incerto-kappa.md:423` | Lower-deviation identity and conditional payoff | **Correct.** Centered integrable deviations have equal positive and negative expectations. Completing the square gives h(a)=a Phi(d)−Phi(d−sigma); 0 ≤ h ≤ n supplies a bounded integration variable. The assumed population mean is essential. |
| `content/incerto-kappa.md:441` | Monte Carlo estimator and standard error | **Correct-with-caveat.** Averaging conditional payoffs is unbiased in exact arithmetic; the ordinary estimated SE is a finite-variance diagnostic. Boundedness does not ensure that a finite simulation sees rare payoff changes. The sigma=10 example below demonstrates the limitation. |
| `content/incerto-kappa.md:450` | Seeded lognormal numbers and transformed error bars | **Correct-with-caveat.** Outputs reproduce. Kappa is increasing in the larger MAD on its domain, so transforming endpoints is valid and generally asymmetric. The bars are explicitly not guaranteed coverage intervals; single-observation MADs are exact and held fixed. |
| `content/incerto-kappa.md:482` | Unique-mode triangle, Irwin–Hall CDF and negative kappa | **Correct.** Independent piecewise density quadrature gives 2/3 and 14/15. Their ratio is 7/5 and kappa is −0.060042717106145. The inclusion–exclusion CDF and integral on [0,2] have the correct coefficients and scaling. |
| `content/incerto-kappa.md:510` | Binomial normal mixture, absolute-normal formula and limit | **Correct.** Conditioning on signs gives mean a(2k−n) and variance n sigma². Independent normal-coordinate quadrature agrees within 4e-16 in the checked cases. For large a, M(1) is asymptotic to a and M(2)=a+sigma/sqrt(pi)+o(1), so the ratio approaches one from above and kappa tends to negative infinity. |
| `content/incerto-kappa.md:540` | Mixture outputs, Pareto caption, body/asymmetry caveat | **Correct-with-caveat.** Rounded mixture values reproduce. Pareto(3, minimum 1) has mean 3/2 and MAD 4/9, independently integrated. The four Pareto points are estimates with finite-variance SE diagnostics, not exact kappa values or a universal skewness/kurtosis ordering. |

### Claim ledger: moment estimation and guide

| Location | Claim | Verdict and evidence |
| --- | --- | --- |
| `content/incerto-moment-estimation.md:28` | Raw-moment definitions, Pareto moments, unbiasedness and variance gate | **Correct.** Integrating alpha x_m^alpha x^(q−alpha−1) gives the formula and the logarithmic boundary. Independence gives the finite variance; the nonnegative single-term lower bound proves divergence when q<alpha≤2q. The examples m2=3, m2=3/2, m4=3 and 3/(4n) are consistent. Formatting changes preserve the formulas. |
| `content/incerto-moment-estimation.md:79` | Truncation consistency and infinite-mean divergence | **Correct.** Bounded-variable Chebyshev plus uniform control of the nonnegative omitted expectation proves the probability limit. The separately linked infinite-mean theorem supplies the stronger almost-sure statement. |
| `content/incerto-moment-estimation.md:101` | RMS/sample-SD integrability and bias distinction | **Correct.** E R_n²=m2 and Cauchy–Schwarz yield finite variance for the root. Subtracting the squared empirical mean only reduces the empirical variance. A fixed Bessel correction preserves finiteness. |
| `content/incerto-moment-estimation.md:127` | Gaussian absolute-moment and RMS risks | **Correct.** Half-normal moments give the variance (pi/2−1)/n; a chi-square half moment gives b_n and MSE 2(1−b_n). Under a variance mixture, the calibrated absolute statistic targets E sqrt(Y), not sqrt(EY). |
| `content/incerto-moment-estimation.md:166` | Rare-mixture numerical moments and missing-state probability | **Correct.** EY=1, 3 E Y²=77.25, estimator variance 76.25/n; 0.99^50=0.6050060671. Conditional narrow-state second moment is 0.5. |
| `content/incerto-moment-estimation.md:217` | Conditional plug-in singularity and outputs | **Correct.** The log-excess average is Gamma(n, scale 1/(n alpha)); its positive density at one makes the reciprocal first and second moments diverge even conditional on a finite fit. The three printed outputs reproduce. |
| `content/incerto-moment-estimation.md:240` | Weighted power means, equality, limit, unnormalized geometry | **Correct.** Jensen gives increasing weighted power means and the stated equality condition; bounding by the largest observation gives the limit. Unnormalized quantities decrease with order. The example (1,2,2 sqrt(2),4) and areas (2,pi,4) are correct; the text already excludes orders below one from norm terminology. |
| `content/incerto-moment-estimation.md:278` | MAD bounds, equality, Gaussian calibration and two-point example | **Correct.** Triangle/Cauchy–Schwarz give the bounds, and equality in the latter requires constant absolute centered value. Gaussian calibration changes the bound; the calibrated two-point ratio is sqrt(2/pi). |
| `content/incerto-moment-estimation.md:298` | Relative error, equal-single-MAD convention, minimum integer | **Correct.** R(n)=M(n)/(n M(1)); the Gaussian target is 1/sqrt(n_g). This criterion compares one absolute expectation, not confidence coverage or variance. The minimization is over integer sample sizes as stated in the prose. |
| `content/incerto-moment-estimation.md:320` | Markov bound and finite-variance comparison | **Correct.** Apply Markov to the nonnegative absolute estimation error. Equal finite parent variances imply equal mean variances sigma²/n at equal n, independently of kappa. |
| `content/incerto-moment-estimation.md:335` | Leave-one-out monotonicity and L¹ convergence | **Correct.** Each observation occurs n times among the n+1 leave-one-out means, whose average is the full mean. Jensen gives monotonicity. Centered clipping leaves a remainder bounded in L¹ by twice the clipping error; take n then the clipping threshold to infinity. Thus every positive Gaussian target is eventually crossed. |
| `content/incerto-moment-estimation.md:361` | Student 44, exponential 36, preceding integers and insufficient cap | **Correct.** Exact rational Student sums and 70-digit gamma evaluation bracket the target independently; values are recorded below. Monotonicity establishes minimality. None at cap 10 means only that the search stopped too early. |
| `content/incerto-moment-estimation.md:391` | Constant-kappa exponent and stable specialization | **Correct.** R(n)=n^((kappa−1)/(2−kappa)); solving the inequality gives exponent (2−kappa)/(2(1−kappa)), then an integer ceiling. Substitution of kappa=2−alpha gives alpha/[2(alpha−1)], hence 3/2 at alpha=1.5. A small-size kappa is only a heuristic for a nonstable law. |
| `content/incerto-moment-estimation.md:420` | Independent equal-weight portfolio and common component | **Correct.** The first MAD is exactly M(n)/n. The iid residual average tends to zero in L¹, and the absolute-value map is 1-Lipschitz, giving residual MAD $\mathbb E\lvert C-\mathbb EC\rvert$. Independence from C is sufficient, though stronger than needed for this conclusion. No empirical or optimal-weight claim is made. |
| `content/incerto-moment-estimation.md:456` | Retained experiment outputs, seeds, counts and interpretation | **Correct-with-caveat.** All outputs reproduce; 600×5000 is three million observations and 100×200 describes the printed experiment. Empirical quantiles/SEs are numerical evidence and cannot establish a population moment boundary. |
| `content/incerto-scoft-ch8.md:12` | Edition, source map, notation and correction summary | **Correct.** Checked the supplied v4 chapter, printed pp. 153–169 (PDF 167–183), and the primary v3 paper. The map's section/page locators and distinctions between chapter derivations and lettered book appendices agree. |
| `content/incerto-scoft-ch8.md:45` | Six mathematical qualifications and worked comparison | **Correct.** These repeat the verified stable, triangle, cubic-limit, MAD-matching, lognormal and portfolio claims. Both worked outputs reproduce; the reference to 120 is restricted to the book's stated MAD criterion. |

### Claim ledger: implementation, tests and other changed files

| Location | Claim | Verdict and evidence |
| --- | --- | --- |
| `src/math/incerto/concentration.py:14` | Count/domain caps and positive-result failure policy | **Correct-with-caveat.** The validators enforce the stated ranges. `_exp` rejects zero/nonfinite rounded results; subnormal numbers still have limited relative precision. These are bounded floating-point implementations of exact formulas, not interval-certified evaluations. |
| `src/math/incerto/concentration.py:29` | Stirling remainder and omitted term | **Correct.** The next term is −1/(1680 a^7), whose magnitude at a=10000 is 5.953e-32, below the stated 6e-31. This is a truncation-error statement, not a bound on all floating-point rounding. |
| `src/math/incerto/concentration.py:35` | Kappa validation, extended outputs and stable helper | **Correct.** The formula, positive-finite monotonicity rejection, equal-MAD negative infinity, undefined-moment NaNs and 2−alpha benchmark match the stated convention. The helper does not certify that arbitrary supplied MADs arise from an iid law. |
| `src/math/incerto/concentration.py:83`; `src/math/incerto/concentration.py:260` | Gaussian formula and scale-independent minimum-size search | **Wrong before review; fixed.** Separate large logarithms lost the small ratio, and the Gaussian helper's log/exp round trip introduced additional relative error. Direct Gaussian scaling and division before taking the search logarithm restore the invariant result. Details below. |
| `src/math/incerto/concentration.py:95` | Gamma formula, switch and scale limits | **Correct-with-caveat.** Independent 70-digit quadrature agrees within 3.9e-12 over the checked grid, including both sides of the switch. At total shape 1e13 and scale 1e-200, the relative error was 3e-15. The pre-switch cancellation is larger than the Stirling truncation error but does not affect the reported crossings. |
| `src/math/incerto/concentration.py:115` | Student formulas, supported sizes, infinity convention | **Correct-with-caveat.** Single/pair formulas and cubic upper-gamma implementation agree with independent references. The inf at nu≤1 denotes divergent absolute moment about the symmetric location; it does not create a population mean or an admissible kappa. At nu=1000 the checked relative error is about 1e-12. |
| `src/math/incerto/concentration.py:145` | Known-mean Monte Carlo, SE, budgets and retention | **Correct-with-caveat.** It averages absolute centered sums and uses sample SD/sqrt(replications). Rescaling by the observed maximum avoids overflow without discarding draws. Infinite-variance absolute deviations do not support the conventional SE interpretation, as documented. |
| `src/math/incerto/concentration.py:168` | Conditional lognormal estimator, n=1 formula and range | **Correct-with-caveat.** The bounded payoff and multiplicative factors match the derivation; the returned SE has the same scale. PCG64 describes the documented integer-seeded runs; passing an existing NumPy Generator preserves that generator, including a different bit generator. The extreme-scale SE caveat below remains. |
| `src/math/incerto/concentration.py:215` | Normal-location-mixture normalization and finite sum | **Correct-with-caveat.** Normalizing both a and sigma before evaluating H avoids avoidable overflow. The point-mass branch applies only when their ratio underflows; contributions below floating-point resolution cannot be recovered. The mathematical formula is the verified binomial mixture. |
| `src/math/incerto/concentration.py:242`; `content/incerto-api-reference.md:2148` | Doubling/binary search, tolerance and cap meaning | **Correct-with-caveat after the fix.** Monotonicity justifies the search for the required deterministic population curve. The eight-epsilon tolerance does not certify an inaccurate callback or resolve arbitrarily close crossings. Since 1≤M(n)/M(1)≤n≤1e7, forming the dimensionless ratio cannot overflow for the stated mathematical inputs. |
| `content/incerto-api-reference.md:1930` | Nine API contracts and all added example outputs | **Correct-with-caveat.** Reproduced every block, including errors, inf, NaN, negative infinity and None. Domains, count limits and mathematical/Monte Carlo distinctions agree with implementation, subject to the Student-infinity and Generator qualifications above. |
| `tests/test_incerto_concentration.py:18` | Gamma, Student, Fourier, rational and asymptotic expectations | **Correct.** All reference integrals and constants were independently checked. The test at n=1e7 checks 4 log(M(n)/(sqrt(n)M(1))), which is 0.9028290121, not the finite-n value log(n) kappa=0.8782326234. Its comment correctly distinguishes the two. |
| `tests/test_incerto_concentration.py:70` | Stable/Gaussian benchmarks, scaling, triangle and mixture tests | **Correct.** Expectations follow from the verified exact identities. The normal quadrature is centered in the normal coordinate, avoiding missed remote peaks. |
| `tests/test_incerto_concentration.py:101` | Lognormal quadrature, seeded tolerances and scaling | **Correct-with-caveat.** An additional CDF-convolution reference, independent of the implemented put formula, agrees. A fixed-seed six-SE check is a regression diagnostic, not a universal probability guarantee. The sigma=10 test's broad proximity-to-16 expectation is valid but does not test SE calibration. |
| `tests/test_incerto_concentration.py:133` | Exhaustive search, failure contracts and Gaussian equalities | **Correct-with-caveat.** Exhaustive comparisons use the intended tolerance. The synthetic curve M(n)=n exercises cap handling; it is not an example of a nondegenerate integrable iid population law. Input failures and divergences match the contracts. |
| `tests/test_incerto_concentration.py:164` | New scale and overflow regressions | **Correct.** Independent curves c sqrt(n) and the Gaussian helper must return n_g for five scales from 1e-300 to 1e300 and sizes through 1e7, even when the cap equals the answer. A separate check preserves representable-large versus overflowing Gaussian MADs. |
| `demos/incerto/concentration.py:30` | Transformed intervals and all four figure calculations | **Correct-with-caveat.** Increasing kappa in the larger MAD preserves endpoint order. Seeds, counts, exact single MADs, stable exponent/ceiling and Pareto centering agree with captions. The total is 8,680,000 scalar draws, appropriately described as about nine million. All sampled interval endpoints stay inside the metric's domain. |
| `tests/test_incerto_concentration_figures.py:12` | Reproducibility/asset expectations | **Correct.** Both fresh processes reproduce the four assets byte for byte. These tests check reproducibility, not the mathematical validity of a population model. |
| `demos/incerto/limit_distributions.py:119`; `demos/incerto/visualization_p2.py:60` | Retained growth and plug-in calculations beneath styling edits | **Correct.** Growth targets are n log(1.05) and (n/2) log(0.9); the plug-in curve is alpha/(alpha−1) for alpha>1. No mathematical data changed in these two edits. Fresh-process P2/limit export tests pass. |
| `assets/figures/incerto/kappa-aggregation.svg:1`; `assets/figures/incerto/kappa-sample-size.svg:1`; `assets/figures/incerto/kappa-lognormal.svg:1`; `assets/figures/incerto/kappa-shape.svg:1` | Plotted numbers, scales and labels | **Correct-with-caveat.** Regenerated from the audited producers with identical bytes. Exact curves and Monte Carlo points remain distinguished. The existing captions retain the error-bar and model-scope limitations. |
| `assets/figures/incerto/ergodicity-growth.svg:1`; `assets/figures/incerto/plugin-mean-singularity.svg:1` | Styling-only figure changes | **Correct.** Source diff and reproducibility tests preserve the simulated paths, analytic targets and sample counts. |
| `assets/data/concept-graph.json:1`; `assets/graphs/concept-list.html:1` | Graph membership and numerical counts | **Correct.** The generated graph has 40 nodes, 67 dependency edges and 79 reference edges, plus separately typed related/application/proof/generalization edges. Graph tests agree with frontmatter. Layout coordinates carry no mathematical assertions. |
| `content/bibliography.bib:344`; `content/incerto-scoft-intro.md:5`; `content/incerto/index.md:143`; `content/incerto-method-concepts.md:9`; `content/incerto-empirical-example-concepts.md:17`; `myst.incerto.yml:48` | Attribution, source dates, reading route and model-calculation labels | **Correct at the mathematical scope.** The added navigation introduces no further theorem, formula or empirical-data claim. The primary paper is v3, 26 November 2018; the book is v4, 17 September 2025. |
| `docs/plan/incerto-program/README.md:77`; `docs/plan/incerto-program/concepts.md:1338`; `docs/plan/incerto-program/inventory.md:32`; `docs/plan/incerto-program/state.yaml:1663`; `docs/plan/incerto-program/validation.md:29`; `docs/plan/incerto-program/verification.md:3`; `docs/plan/incerto-program/visualization-review.md:19`; `docs/plan/index.md:30` | Repeated mathematical scope and inventory counts | **Correct.** The added text repeats the audited claims and keeps teaching, numerical evidence and optional Lean separate. Recounted 35 program concept bodies, 61 Incerto pages, 85 total pages and 81 flat redirects; the frozen denominator remains 24. Planning flags still describe the pre-review checkpoint. |
| `docs/records/incerto-scft-v4-ch08.md:24`; `docs/records/incerto-scft-v4-ch08.md:56`; `docs/records/incerto-scft-v4-ch08.md:99`; `docs/records/incerto-scft-v4-ch08.md:137` | Source locators, three discrepancies, helper/figure counts and CH08-C01–C10 summaries | **Correct-with-caveat.** These agree with this ledger. The original full-test and snippet totals match the retained final logs; they are historical runs, not the new 387-test result below. |

### Independent evidence and source corrections

Read the supplied PDF afresh with `pdftotext -f 167 -l 183 -layout` and
visually inspected printed pp. 160 and 165. The book's equal-single-MAD
criterion is explicit in Eq. 8.7; Eq. 8.8 and the following 120-observation
example do not solve it correctly. The book's subsequent variance/confidence
language is a different criterion. The guide fairly limits its correction to
absolute error. The pi²/4 limit is visibly printed on p. 165, and the
bimodality requirement appears on p. 162. The book's exact cubic MAD formula
itself is correct. Also checked the primary
[paper](https://arxiv.org/html/1802.05495v3) and
[v4 metadata](https://arxiv.org/abs/2001.10488v4).

Independent calculations used SciPy quadrature, exact `Fraction` arithmetic,
and mpmath **1.4.1 at 70 decimal digits**. For cubic sums, rescaling the Fourier
integral by sqrt(n) permits a reference at n=10^24, outside the package's count
limit: 4 log(M(n)/(sqrt(n)M(1))) = 0.903165410577846, consistent with the
proved constant. The actual log(n) kappa still converges more slowly; it is
0.895844869509261 at that n. Neither finite number is substituted for the limit.

| Independent quantity | Value |
| --- | --- |
| Gaussian target, 1/sqrt(30) | 0.1825741858350554 |
| Cubic Student R(43) | 0.1837314442454652, above target |
| Cubic Student R(44) | 0.1817113686546491, below target |
| Exponential R(35) | 0.1828674964423482, above target |
| Exponential R(36) | 0.1803217078129340, below target |
| Mean-one lognormal two-sum MAD, sigma=0.5 | 0.5761132990496239 |
| Mean-one lognormal two-sum MAD, sigma=1 | 1.191048900774249 |
| Mean-one lognormal two-sum MAD, sigma=2 | 2.399002445707364 |

The lognormal reference uses the independent convolution identity
E(c−X−Y)_+ = integral from 0 to c of F_X(x)F_Y(c−x) dx. At sigma=1e-4,
the integration must resolve the narrow region near x=1; an initial coarse
quadrature missed it and was replaced with explicit breakpoints. Likewise,
the tiny-scale Gamma reference was integrated at unit scale before multiplying
by the scale, avoiding the quadrature's absolute-tolerance floor. Neither
reference-calculation correction changed repository code or mathematics.

Fresh **Philox** raw-draw simulations used 400,000 independent replications
per case, seeds **729301–729308**, for Student sums at sizes 2/8, Gamma shape
0.7 at size 7, the triangle pair, Pareto-3 single MAD, and mean-one lognormal
sums at (n,sigma)=(2,0.5),(8,1),(8,2). Lognormal comparisons used separate
conditional streams, seeds **819278–819280**. All differences were within
2.12 combined estimated SEs. An independent Gaussian common-component example
with Var(C)=4 and residual variance 9 matched sqrt(4+9/n) sqrt(2/pi) at
n=1,10,1000; its limiting MAD is 1.595769121605731. This supports the
calculation but does not replace its L¹ proof.

No copied book prose or imported book figures were found. A fresh normalized
10-word and 12-word overlap scan across the added Markdown prose found zero
matches against the chapter; manual review also checked the mathematical
exposition and source attribution. Shared mathematical formulas and cited
source titles are expected. An overlap scan cannot prove the provenance of
every phrase, so this is evidence of independently written exposition, not a
general originality certification.

Scratch evidence: `/tmp/ch08-max-numerics.py`, its JSON/log, and
`/tmp/ch08-max-monte-carlo.py`, its JSON/log. The pre-review file snapshot is
`/tmp/ch08-max-baseline`; these scratch files are not repository deliverables.

### Minimal fix and verification

Before the fix,
`gaussian_equivalent_n(lambda n: 1e-200*np.sqrt(n), 2)` returned **3**.
The same valid Gaussian MAD curve at unit scale returned **2**. Separately,
using `gaussian_sum_mad(n, sigma=1e200)` returned **5** at reference size **4**.
The first failure was cancellation in subtracting logs of dimensional MADs;
the second also included the helper's unnecessary log/exp round trip.

- `src/math/incerto/concentration.py:83`: evaluate sigma sqrt(2n/pi)
  directly, preserving the finite-result overflow check.
- `src/math/incerto/concentration.py:260`: form M(n)/M(1) before its logarithm;
  this dimensionless ratio is between one and n under the input contract.
- `tests/test_incerto_concentration.py:164`: add five parameterized scale
  regressions and one overflow-contract test. This increases the helper
  suite from 77 to **83** cases.

`UV_NO_SYNC=1 UV_CACHE_DIR=/tmp/ch08-max-uv MPLCONFIGDIR=/tmp/ch08-mpl-local
OPENBLAS_NUM_THREADS=1 uv run python scripts/regenerate_incerto_outputs.py`
executed **137 snippets and one full-demo output; zero pages changed**.
The chapter-8 demo regenerated all four SVGs with identical bytes.

The following affected tests passed under the same environment variables:

```sh
uv run pytest -q tests/test_incerto_concentration.py \
  tests/test_incerto_concentration_figures.py \
  tests/test_incerto_page_snippets.py tests/test_incerto_viz_p2.py \
  tests/test_concept_graph.py
```

Result: **387 passed in 113.92 seconds**. This includes the 83 helper cases,
all page snippets, chapter-8 figure reproduction, the existing P2/limit figure
exports and graph checks. The separate initial helper run also passed all 83.
The command used `UV_NO_SYNC=1`; this is still an available-dependency run,
not a locked-environment pass. No full-suite, fresh HTML/browser, wheel or
Lean verification is claimed for this review.

`git diff --check` and separate whitespace/control-character checks on all
11 new files pass. Only the helper, its tests and this record differ from the
pre-review snapshot. No files are staged or deleted; all work remains uncommitted.

### Decisions and limits for Xiang

- **Extreme-lognormal SE presentation.** At n=2, sigma=10, mu=−50,
  100,000 replications and seed 613729, the estimator returns
  MAD 3.999998371657866 with estimated SE 5.50725e-9. Independent quadrature
  gives MAD 3.999996764165067 and true Monte Carlo SE 6.56725e-6 for that
  conditional estimator. The observed error is only 0.245 true SE but about
  292 reported SEs: the simulation missed rare payoff changes. The current
  diagnostic-only caveat is mathematically honest. Xiang can decide whether
  to add this explicit example, narrow the advertised numerical range, or
  request a different integration method; none was silently introduced.
- **Optional precision of wording.** The attraction paragraph could explicitly
  say “nondegenerate” for its stable limit, and the API could distinguish
  default PCG64 integer seeds from an already supplied Generator. The reviewed
  mathematics and all published seeded examples use the intended conventions.
- **Numerical certification.** Arbitrarily close search crossings, inaccurate
  user callbacks and subnormal relative precision remain outside the floating-
  point guarantee. Tests verify the repaired scale failure, not every possible
  finite input. No further demonstrated formula error remains.
- **Separate gates.** Fresh site rendering, locked dependencies and browser
  behavior remain **unverifiable in this review** and retain their existing
  follow-ups. Planning files still have their historical “max review pending”
  wording; only this requested record was appended. Reconcile those flags
  when accepting the review, without authorizing chapter 9 or publication.
