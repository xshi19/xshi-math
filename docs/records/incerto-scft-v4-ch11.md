# SCoFT v4 chapter 11 checkpoint

2026-10-30 (America/New_York). Branch `scft/v4-ch11`, base `ce67306`
from `origin/main`. Xiang selected **gpt-6-astra xhigh** for writing/code
and a separate **gpt-6-astra max** run for subsequent mathematical review.
No delegation, staging, commit, push, publication, or repository file deletion.

Chosen title: **Chapter 11 — Calibration and payoffs**.
The chapter's teaching and deterministic Python artifacts are implemented.
Separate max review, fresh site/browser checks, and a post-publication reader
review are distinct gates. The next writing chunk is `scft-v4-ch12`.

## Contract, sources and boundaries

Read the root and Incerto guidance, shared rules, notation canon and program
lock, relevant concept/proof/reading-guide/prose/Git skills, program contracts,
state, M0.5 review, visualization review, chapter-9/10 records, visualization
P2 and code-visibility patterns, snippet tests and output regenerator. Applied
the hub-publish skill to local build checks only. Consulted the Lean skill
for evidence boundaries; no formalization work was started.

Read the supplied, read-only `/workspace/scoft-toc/2001.10488v4.pdf` and
v4 TOC. Chapter 11 is printed pp. **219–240**, PDF pp. **233–254**.
Source extraction and the raster inspection of printed p. 240 stayed under
`/tmp`. The guide maps §§11.1–11.7, including both appendix subsections.
No source PDF, TOC, text, table, figure, or close paraphrase is included.
A case-normalized 12-word overlap scan against the chapter found zero
matches in the three new teaching pages; manual prose comparison also
preserves the original-writing boundary.

The existing `taleb2025scoftv4` bibliography entry supplies chapter context.
Two primary references were added only to `content/bibliography.bib`:
Hyndman–Koehler's forecast-accuracy paper (consulted author manuscript,
2 November 2005, §3, pp. 12–13), and Hyndman's 16 April 2014 discussion
of sMAPE denominator conventions. The paper supports the training-error
normalization; the latter distinguishes the bounded denominator used here
from other historical versions. The original M4 guide's university URL
returned 404; no unseen guide text is claimed verified. The point page
states its formula and zero convention directly. No inline DOI link was added.

All calculations are models or simulations. No data were acquired, and
no observed-data study, psychology experiment, financial-performance claim,
or competition ranking is inferred. Test/build checks use no network.
The existing third-party data notes and snapshots are unchanged.

## Teaching and integration

New pages:

- [Calibration and payoffs](../../content/incerto-calibration-payoff.md):
  event/payoff identification, Pareto and exponential comparisons,
  mean-matched lognormal example, specified parameter mixing, Brier
  calibration, tally law, fixed-forecast score law, two beta joint laws,
  and nonlinear exposure boundaries.
- [Point forecasts](../../content/incerto-point-forecast.md): finite-risk
  mean/median proofs, exact Pareto loss boundaries, absolute-risk example,
  loss-tail transformations, MASE and bounded sMAPE. Chapter 12 will extend
  this canonical page; its pandemic and wider forecasting scope is unstarted.
- [Chapter 11 guide](../../content/incerto-scoft-ch11.md): verified v4 map,
  notation mapping, source qualifications, display equations and a runnable
  exact finite-score example.

Reused rather than duplicated the asymmetric-payoff, Pareto-moment,
moment-estimation and chapter-10 ML/hinge/angle pages. The ML page adds a
short reciprocal link distinguishing geometric calibration from event
calibration. The MyST TOC, method/theorem indexes, Incerto hub, SCoFT intro,
API reference, concept graph/list and program human views are wired.
Graph: **48 nodes, 89 dependency edges, 110 reference edges**.

`state.yaml` records chapter 11 as done at this teaching/model/Python scope,
authorized chunks through 11, branch/scope, checkpoint, and next chapter 12.
Both concepts are **in-progress overall**, with explicit completed chapter-11
scopes: calibration also belongs to chapter 13, point forecasting to chapter
12. Later chunks' reuse lists include the newly existing pages; earlier
checkpoints are not backdated. Current program bodies rise from 37 to **39**;
103 concept IDs, 75 active concepts and the frozen 24-body M0.5 inventory
are unchanged. Chapter-10 empirical/review state is not rewritten.

## hard_math_claims_for_max_review

Line references identify the final public statements in this working tree;
review each surrounding proof, assumptions, cited inputs and helper domain.

| Claim | File:line | Claim and support |
| --- | --- | --- |
| CH11-C01 | `content/incerto-calibration-payoff.md:24` | Strict binary/vanilla/tail-level decomposition, survival integral and static nonreplication by cash plus one binary on unbounded support. Original pointwise and nonnegative-expectation arguments. |
| CH11-C02 | `content/incerto-calibration-payoff.md:85` | Exact Pareto/exponential excess means, fixed-event-probability severity nonidentification, moment boundary and payoff-equivalent quantity exceeding one. Local integration plus existing Pareto theorem; Weibull counterexample linked. |
| CH11-C03 | `content/incerto-calibration-payoff.md:154` | Fixed-mean lognormal at its mean: event probability decreases, tail/excess means increase and stay bounded by the mean; strict zero-scale discontinuity. Original normal-density square completion. |
| CH11-C04 | `content/incerto-calibration-payoff.md:204` | Convexity of the exact Pareto excess mean in a random exponent, Jensen comparison, infinite mixture despite exponents above one, and event-weighted conditional ratios. Original derivatives and mixture expectations. |
| CH11-C05 | `content/incerto-calibration-payoff.md:257` | Conditional Brier decomposition/strict propriety, calibrated expected score, all positive moments without independence, and common-outcome dependence counterexample. Original bounded algebra. |
| CH11-C06 | `content/incerto-calibration-payoff.md:332` | Exact iid binomial tally, cumulants, variance, standardized CLT versus uncentered point-mass limit. Generating-polynomial proof; general iid CLT cited through existing note. No universal n^-1 normal-approximation rate. |
| CH11-C07 | `content/incerto-calibration-payoff.md:366` | Fixed-q Brier pushforward, mean/variance, q=1/2 degeneracy, and bounded score with kurtosis exceeding 98. Original affine identity. |
| CH11-C08 | `content/incerto-calibration-payoff.md:407`; `src/math/incerto/calibration.py:149` | Independent versus calibrated beta/Bernoulli joint laws: one-score densities, CDFs and moments; iid convolution characteristic function, uniform special cases and variance of averages. Original change of variables and beta integrals. Simulated averages are numerical evidence only. |
| CH11-C09 | `content/incerto-point-forecast.md:28`; `:63` | Finite expected squared/absolute-loss minimizers are mean/medians; exact Pareto risk boundaries hold for every finite action; exact absolute risk at d>=xm. Original expansion, integral of slopes and moment comparison. |
| CH11-C10 | `content/incerto-point-forecast.md:150`; `content/incerto-calibration-payoff.md:535` | Absolute/squared errors have tail exponents alpha/alpha/2 for fixed forecasts; fixed-scale MASE preserves the former, sMAPE is bounded; conditional nonlinear payoff factorization and Jensen/interchange limits. Original event inversion and inequalities; definitions independently sourced. |

### Source qualifications for review

- **§11.1.2, pp. 224–225:** defined threshold events remain measurable under
  fat tails. Words alone omit threshold, horizon, units and severity.
  The nonreplication proof concerns cash plus one binary, not all dynamic
  strategies or a continuum of instruments.
- **§11.2, pp. 225–230:** threshold-times-probability differs from a tail
  amount by the excess mean. The Pareto factor uses `alpha-1`, and an
  amount expressed in threshold units need not be a probability. A limiting
  conditional-mean ratio is not a universal thin/fat classification.
  Mean-matched lognormal payoff means do not diverge with log scale.
- **§11.2.4, p. 230:** convexity is proved for the selected Pareto excess
  functional. No universal Jensen or kurtosis argument is imported. A
  mixture conditional ratio uses event-dependent weights.
- **§§11.3–11.4.1, pp. 230–235:** Brier calibration is meaningful for
  specified events; it does not identify severity. Bounded support ensures
  positive moments, not kurtosis below three, independence, or fast averages.
  The normal limit is centered/standardized; excess-kurtosis decay does
  not provide the asserted general normal-approximation rate.
- **§11.4, p. 233:** absolute-error metrics require the absolute numerator.
  sMAPE with the stated denominator is bounded; MASE uses training naive
  errors and a positive scale. No claim about the eventual M5 competition
  is inferred from the source's proposed metric.
- **§11.5, pp. 235–238:** conditional payoff expectation is an exact
  factorization. Replacing it by a function of a conditional mean requires
  assumptions; Jensen supplies an inequality only for suitable curvature.
  Finite hinge sums have the scope already proved in chapter 10. A genuine
  absorbing process retains every prior crossing; survival conditioning
  does not generally preserve a marginal payoff law.
- **§11.7, pp. 238–240:** the forecast/outcome joint law is explicit.
  A probability integral transform does not force reports to be beta.
  We derive score distributions from joint densities and iid convolution,
  avoiding reliance on the source's unwieldy variance/characteristic-function
  expressions. Raw fourth cumulants and standardized excess kurtosis have
  different averaging powers.

## Helpers and figures

`src/math/incerto/calibration.py` adds eleven public helpers. Every name
used on a reader page links its stable API anchor; long code/output blocks
use MyST dropdowns. Each Output block was generated by execution.

| Helpers | Purpose |
| --- | --- |
| `tail_bet_payoffs`, `pareto_tail_bet`, `lognormal_tail_bet` | Same-state payoffs and exact model means; strict equality, infinite moments, log evaluation and zero-scale boundary |
| `binary_tally_distribution`, `brier_score`, `brier_score_distribution` | Binomial fractions, observed scores and fixed-forecast finite law |
| `beta_brier_moments`, `beta_brier_cdf`, `simulate_brier_scores` | Explicit independent/calibrated joint models; exact moments/one-score CDF and bounded Monte Carlo of averages |
| `calibration_curve` | Bin counts, forecast means and frequencies; endpoint inclusion and empty-bin NaNs |
| `point_forecast_loss` | Absolute/squared/MASE/sMAPE values; zero convention, scale validation and arithmetic overflow |

The beta evaluator deliberately restricts shapes to `[0.001,10000]`.
Tally/average counts are at most 100,000. Simulation allows at most 20 million
pairs, at most one million replications, and batches of at most 100,000
pairs. Exact formulas do not imply uniform floating-point accuracy. No
replication is discarded, and mathematical infinity is distinguished from
representational overflow. API examples execute NaN, infinity, empty-bin,
degenerate-score, strict-tie and rejected-input cases.

All four original SVGs are generated by
`demos/incerto/calibration_payoffs.py` through the existing
`src/math/incerto/figures.py` style/layout/export functions. No style fork
or dependency was added.

| File (`assets/figures/incerto/`) | Page | Inputs |
| --- | --- | --- |
| `calibration-tail-payoffs.svg` | `incerto-calibration-payoff.md` | Exact payoff at u=4; exact Pareto excess at u=10, fixed p=.02 and 220 exponents in [1.05,4] |
| `calibration-curves.svg` | `incerto-calibration-payoff.md` | Uniform forecasts, conditional event probabilities Q and Q²; 4,000 pairs each, PCG64 seeds 1103/1104, ten fixed bins with counts and descriptive ±2 SE bars |
| `calibration-score-laws.svg` | `incerto-calibration-payoff.md` | Exact fixed-q law at n=20,p=.2; exact uniform one-score CDFs; 20,000 averages of 20 scores per joint model, PCG64 seed 1107 |
| `point-forecast-losses.svg` | `incerto-point-forecast.md` | Exact Pareto alpha=1.5,xm=1; common median forecast; exact absolute-risk curve d in [1,5] |

The random-forecast averages use 800,000 pairs in total. Mean estimates are
**0.3337 / 0.1669**, versus exact **1/3 / 1/6**, for independent/calibrated
models. Exact-model Monte Carlo SEs round to **0.0005 / 0.0003**.
Sampling 10/50/90% quantiles are **.249/.332/.421** and **.112/.164/.226**.
These are simulation estimates, not fitted observed performance.
The point-page example separately uses 20,000 Pareto draws, seed 1110;
its finite sample squared errors do not establish finite squared risk.

## M0.5 and optional Lean

No M0.5 issue is directly assigned to chapter 11. The scoped follow-up in
[m0.5-review.md](../plan/incerto-program/m0.5-review.md#chapter-11-follow-up-2026-10-30)
retains **006/007 open**: no deferred general theorem locator or global
legacy-citation audit is closed. Existing resolved moment and strict-event
conventions are preserved. Totals remain 13 resolved, two assigned, zero
owner decisions pending.

Lean is **skipped-for-now**. The optional imported prototype supplies no
checked probability/scoring development for these new claims; no toolchain,
cache or exact new declaration was selected. A small algebraic identity
would cover only a fraction of the probabilistic claim, so no unchecked
formalization stub is added. Python evidence is not Lean evidence.

## Verification

Checks below were executed against this working tree. Available-environment
tests and blocked fresh-install/site gates are recorded separately.

- New helper/figure selection: **79 passed in 6.01 s**. Direct density
  quadratures; all 32 binary sequences for each finite-law test setting;
  beta joint-density integrals and uniform closed forms; exact-moment Monte
  Carlo bounds; ties, empty bins, degeneracy, shape/count/input limits and
  representable tiny means.
- Output regeneration executed **128 snippets**, changing four pages:
  calibration, point forecast, chapter guide and API. No numeric output was
  hand-transcribed. The standard exact-output tests run without modification.
- Four SVGs rendered through librsvg/Cairo at **390 and 900 px** and all
  eight PNGs inspected. Repaired one legend crossing a vertical reference
  line and re-inspected both sizes. Previews: `/tmp/ch11-previews`.
- **24 display blocks** parse with KaTeX 0.16.25; conservative glyph/layout
  estimates at the site's 17 px base have maximum **287.3 px**. Two long
  fraction rows were split. These estimates do not certify browser widths.
- Full suite, `UV_NO_SYNC=1 uv run pytest`: **1,522 passed, 1 skipped in
  239.51 s**. The skip is the existing local-data layoffs example. Exact
  page outputs, graph/integration checks and both independent SVG exports
  pass. No code changed after this run.
- Executable state/human-view validation passed, including **1,187** plan
  file/fragment links; counts are 39 existing bodies, 103 total concepts,
  75 active concepts and zero new checked Lean claims.
- `npm ci --offline --ignore-scripts` in `/tmp/ch11-site-check` failed
  because the MyST 1.10.1 archive was not cached. The scratch copy then
  used available dependencies with an identical lockfile and a network
  guard. `npm run build` failed at MyST preflight: Node 24.22.1 detected,
  npm reported as `Package Not Found`. No fresh HTML export was produced.
- `npm run check:html` against that scratch copy failed on missing generated
  pages, assets, redirects and subsite configs. Four pre-existing unresolved
  legacy rows were skipped. This is not a passing HTML check.
- Headless Chrome with a writable temporary profile failed at sandbox
  socket setup (`setsockopt: Operation not permitted`). No browser equation,
  navigation, or live-reader pass is claimed.
- Packaging and Lean builds were not run: package mapping is unchanged,
  and Lean is explicitly skipped above. No CI workflow is present.
- Final changed-file audit passed **1,586** local file/fragment links and
  local bibliography keys. Reviewed the diff and the full new source files;
  SVGs were parsed and independently regenerated as well as visually checked.
  `git diff --check` and a separate whitespace scan including untracked
  files pass. No tracked file was deleted, and the index remains empty.

Environment: Python **3.13.5**, NumPy **2.4.6**, SciPy **1.18.1**,
Matplotlib **3.11.2**, pytest **9.0.3**. `uv sync --locked --offline`
failed because the SciPy wheel was absent from the available cache. A local
venv uses the available chapter-10 dependency files, a local Matplotlib
copy for bundled-font paths, and editable mapping to this checkout.
No manifest/lock or package mapping changed. Test commands use
`UV_NO_SYNC=1 UV_CACHE_DIR=/tmp/ch11-uv`, a writable Matplotlib cache and
one BLAS thread; results are not a fresh locked-install pass.

## Decisions and next actions for Xiang

1. Run the separate **gpt-6-astra max** review of CH11-C01–C10 and numerical
   domains. No max-review verdict is claimed by this xhigh writing run.
2. Complete fresh locked-install/site/browser checks where the required
   caches and process support are available, then live reader review after
   separately authorized publication.
3. Continue with chapter 12 on the existing point-forecast page. The chapter
   13 calibration extension and prior chapter-10 empirical gate remain open.

No title, notation, source-data or page-placement decision is needed for
this patch. The working tree remains intentionally uncommitted.

## Max review

2026-10-30. Xiang selected **gpt-6-astra, max reasoning** for this separate
review. Reviewed CH11-C01–C10, their surrounding assumptions and proofs, the
chapter guide and source qualifications, all eleven calibration helpers,
examples, tests and figure generation. This section completes the mathematical
review requested in item 1 above; it does not complete the separate publication
gates. No delegation, staging, commit, push, publication or repository deletion.

**Verdicts: five correct; five correct-with-caveat.** The latter identify
implementation defects or wording qualifications corrected below. The central
derivations survive review; none is unverifiable. Several pre-review helper
results were wrong within their advertised numerical domains, even though the
page formulas were correct. Numerical checks support the derivations and do not
replace the proofs or certify uniform floating-point accuracy.

### Claim verdicts

Locations below refer to the reviewed working tree. The earlier table's page
locations remain unchanged; `beta_brier_moments` now starts at line 153.

| Claim | Verdict | File:line and evidence |
| --- | --- | --- |
| CH11-C01 | **correct** | `content/incerto-calibration-payoff.md:24`, `:46`, `:63`; guide `content/incerto-scoft-ch11.md:36`. The pointwise identity and Tonelli apply to nonnegative losses, including infinite expectations; conditional excess requires positive event probability. Cash plus one binary is constant above the threshold, so the static nonreplication argument is valid on unbounded support. Independent atomic example, including a tie at `u=4`: `p=.6`, `T=4.8`, `C=2.4`; integrating its survival function gives the same excess. The helper's wider finite-real domain preserves the pointwise identity. |
| CH11-C02 | **correct** | `content/incerto-calibration-payoff.md:85`. For `u>=xm>0`, the finite formulas require `alpha>1`; valid Pareto laws with `0<alpha<=1` have both payoff means infinite. Forty direct density integrals agree with the helper to relative error below `2.5e-9`; a separate 48-case floating-range check preserves representable means and raises on the three true overflows. Exponential excess at `u=4,b=3` is `0.7907914143`; the Weibull example has excess `8` at `u=9`. Holding `p=.2` with `alpha=1.1` gives `p*=2.2`. The fixed-probability nonidentification and the limit-ratio qualification are valid. |
| CH11-C03 | **correct-with-caveat** | `content/incerto-calibration-payoff.md:154`; `src/math/incerto/calibration.py:87`. Completing the normal-density square proves all three formulas. Fifteen independent 80-digit normal-density integrals at positive scales `.03,.4,1,2.5,5`, mean `3`, agree within `8.9e-16` relative error. The fixed-mean limits are bounded, and the strict binary/tail-level discontinuities at zero scale are real. **Fixed:** a subnormal positive scale could erase a representable excess mean before multiplication by the mean; see the counterexample below. |
| CH11-C04 | **correct** | `content/incerto-calibration-payoff.md:204`. Differentiation gives the stated strictly positive `c''/c`; finite `EA` makes Jensen's right side defined, while the left side may be infinite. Nine high-precision derivative checks agree within `3.5e-77` absolute error. For equal exponents `1.2,2.8`, `u=4,xm=1`, the event-weighted ratio is `5.5638248622`, versus unweighted `3.7777777778` and mean-exponent `2`. The uniform `(1,2)` example diverges logarithmically, despite finite mean exponent. |
| CH11-C05 | **correct** | `content/incerto-calibration-payoff.md:257`. Conditional expansion proves strict propriety for a fixed event law; it is not a finite-sample reward guarantee. A three-forecast joint-law enumeration gives expected score `.214` by both sides of the decomposition. Calibration gives `E[Q(1-Q)]`; boundedness supplies every positive power and every real exponential moment without independence. With a common Bernoulli(`.3`) outcome and zero reports, the average's variance stays `.21` for every sample size. |
| CH11-C06 | **correct-with-caveat** | `content/incerto-calibration-payoff.md:332`; `content/incerto-scoft-ch11.md:72`. The iid law, first four cumulants, variance, point-mass limit and standardized CLT are correct. Rational enumeration of all 128 sequences in each of 25 settings verifies the cumulants and score laws. Normal-CDF errors at `p=.2`, `n=100,400,1600` are `.059462,.029873,.014954`, consistent with the lattice obstruction to a general `n^-1` bound. **Fixed:** the guide asserted independence was necessary for the law; it now states the assumption used in these derivations. A dependent counterexample is given below. |
| CH11-C07 | **correct-with-caveat** | `content/incerto-calibration-payoff.md:366`, `:381`. The affine pushforward, mean, variance and `q=.5` degeneracy are correct. Exact enumeration agrees with the helper's first four raw score moments within `4.5e-16` absolute error. Pearson kurtosis at `n=1,p=.01,q=0` is `98.0101010101`. **Fixed:** the kurtosis comparison now explicitly requires `0<p<1` as well as `q!=.5`; at event-probability endpoints the standardized quantity is undefined. |
| CH11-C08 | **correct-with-caveat** | `content/incerto-calibration-payoff.md:407`; `src/math/incerto/calibration.py:153`, `:185`. The two joint laws, transformed densities, beta moments, uniform special cases, iid variance and characteristic-function convolution are correct for positive shapes and the stated dependence. Direct joint-density quadrature over 36 models agrees within `4.7e-12` for moments and `1.8e-11` for CDFs; high-precision CDF differentiation confirms the densities. **Fixed:** raw-moment cancellation corrupted small variances, and square-root rounding corrupted CDFs near one. After correction, 384 variance settings agree with 80-digit references within `5.8e-16` relative error; 80 CDF settings, including endpoint singularities, agree within `2.3e-16` absolute error. Fresh Monte Carlo also checks averages and convolution below. |
| CH11-C09 | **correct** | `content/incerto-point-forecast.md:28`, `:63`, `:95`. The squared-risk proof requires a finite second moment; the absolute-risk proof requires a finite first absolute moment. The slope-integral argument covers atoms and nonunique medians. Bounds by multiples of powers of `X` establish necessity and sufficiency of both exact Pareto moment thresholds for every finite action, including equality at the divergent boundaries. Eighteen direct risk integrals confirm the formula; at `alpha=1.5,xm=1`, median/mean absolute risks are `1.7622031559` and `2.3094010768`. For masses `.5` at `0,2`, every point in `[0,2]` has absolute risk `1`. |
| CH11-C10 | **correct-with-caveat** | `content/incerto-point-forecast.md:150`; `content/incerto-calibration-payoff.md:535`; `src/math/incerto/calibration.py:253`. Inverting the loss events proves exponents `alpha` and `alpha/2` for fixed finite forecasts. A fixed positive MASE scale preserves the first exponent; a random denominator needs additional conditions. Twenty-five signed/extreme sMAPE cases agree with high-precision arithmetic and remain in `[0,2]`. Conditional factorization requires integrable payoff and positive event probability; Jensen additionally requires a defined conditional mean and suitable curvature, while infinite sums need an interchange argument. A discrete check gives conditional quadratic payoff `10` versus the square of the conditional mean `7.84`. **Fixed:** MASE now rejects nonscalar scales, as its documented domain requires. |

### Minimal fixes and their independent checks

- `src/math/incerto/calibration.py:101`: with
  `sigma=np.nextafter(0.,1.)`, `mean=1e308`, the old excess was zero;
  the 80-digit reference is `1.971036754199135e-16`. Scale before dividing
  in the subnormal branch. The omitted relative correction is of order
  `sigma**2/24`, below representable precision throughout this branch.
- `src/math/incerto/calibration.py:163`: at `a=.001,b=10000,p=1`, the old
  variance was `1.4551915228366852e-11`, versus
  `3.9987983407243435e-11` from 80-digit rising-factorial moments, an
  understatement of **63.6093%**. Condition on the outcome, compute the
  squared-beta component variances without subtraction, and apply total
  variance. For `Y~Beta(c,d)`, `t=c+d`, the positive formula used is
  `c(c+1)d[(4c+6)t+6(c+1)]/[t^2(t+1)^2(t+2)(t+3)]`.
  In the calibrated model, the component beta shapes are `(a,b+1)` and
  `(b,a+1)` with weights `b/(a+b)` and `a/(a+b)`. Rational raw-moment
  regression tests provide an independent oracle for this reformulation.
- `src/math/incerto/calibration.py:196`: at
  `z=np.nextafter(1.,0.)`, `a=b=.001`, independent outcomes, the old CDF
  was `0.5180343044854148`; the 80-digit value is
  `0.5183682618941981`. With `a=.001,b=10000,p=1`, the old value was
  `0.0265902026480265`, versus `0.02726468511977335`. Near one, evaluate
  the equivalent beta survival probability using
  `1-sqrt(z)=(1-z)/(1+sqrt(z))`; retain direct CDF evaluation near zero.
- `src/math/incerto/calibration.py:264`: one-element vector and matrix
  MASE scales previously changed the shape of a scalar loss. Both are now
  rejected; scalar training normalization and broadcasting of observations
  and forecasts keep their documented meanings.
- `content/incerto-calibration-payoff.md:381`: add the event-probability
  nondegeneracy condition to the kurtosis comparison.
- `content/incerto-scoft-ch11.md:72`: state independence as an assumption
  of these derivations. An exact counterexample to necessity assigns masses
  `(2,1,2,3,3,2,1,2)/16` to binary triples in lexicographic order. Each
  marginal is Bernoulli(`1/2`), their sum is Binomial(`3,1/2`), but
  `P(D1=D2=1)=3/16`, not `1/4`.
- `tests/test_incerto_calibration.py:71`, `:135`, `:151`, `:223`: add
  regression coverage for subnormal excess, endpoint CDFs, 12 exact-rational
  beta moment cases and the two invalid MASE scale shapes. No dependency,
  manifest, package mapping or API signature changed.

### Independent numerical evidence and source comparison

The scratch review scripts and JSON results are under
`/tmp/ch11-max-review-f5wiso2q/`: `independent_review.py`,
`before-results.json`, `after-results.json`, `domain_review.py`,
`domain-results.json`, `dependent-binomial.json` and `source-overlap.json`.
They use SciPy 1.18.1, mpmath 1.4.1 at 80 decimal digits, rational enumeration
and fresh NumPy Philox streams. mpmath was installed only into
`/tmp/ch11-max-review-deps`; the repository environment/lock was not changed.
The beta moment grid uses both shapes in
`{.001,.01,.1,1,10,100,1000,10000}` and
`p` in `{None,0,.01,.5,.99,1}`. The extra CDF check covers symmetric,
asymmetric and boundary shapes, including the largest float below one.
Floating-range checks allow ordinary rounding and subnormal quantization;
they are not an interval certificate for every accepted input.

Fresh Monte Carlo draws beta(`2.5,.7`) forecasts and Bernoulli outcomes
independently of the repository simulator, with 100,000 averages of 13
scores per model, **2.6 million pairs** total. Calibrated/independent
Philox seeds are **2026103001/2026103002**; the independent event
probability is `.3`. No replicate is discarded.

| Model | Simulated mean | Exact mean | Exact-model MC SE | Mean discrepancy in SE | Sample/exact average variance |
| --- | --- | --- | --- | --- | --- |
| Calibrated | 0.1302162612 | 0.1302083333 | 0.0001779433 | 0.0446 | 0.98285 |
| Independent | 0.4821166724 | 0.4822916667 | 0.0003106812 | -0.5633 | 1.00236 |

At characteristic-function argument `t=3`, direct joint-density integration
followed by the iid convolution gives sampling discrepancies
`0.0002437/0.0005361`, below the corresponding five-standard-error bounds
`0.0026495/0.0045626`. These checks support the finite simulation and its
moments; no empirical forecasting claim or normal-approximation rate follows.

Read all of chapter 11 in the supplied v4 PDF, printed pp. 219–240,
including the qualifications listed earlier. The PDF remained read-only;
layout and reading-order extractions stayed under `/tmp`. No copied book
prose or figure was found in the three pages. Case-normalized, Unicode-normalized,
line-hyphen-joined scans against both extractions found **zero 12-word and
zero 6-word contiguous matches**. Manual comparison also found original
exposition and derivations rather than close paraphrase. This is a scoped
source comparison, not a general provenance certificate.

Rechecked the primary [Hyndman–Koehler author manuscript](https://robjhyndman.com/papers/mase.pdf),
§3, pp. 12–13, for training naive-error normalization, and
[Hyndman's denominator discussion](https://robjhyndman.com/hyndsight/smape/)
for the stated sMAPE convention. The page supplies its own `(0,0)` policy.
The source's broad psychology, market-performance and competition conclusions
remain outside the established claims. The book's unwieldy characteristic
functions and variance expressions were not used as computational oracles.

### Verification and decisions

- Final affected-tests command:
  `UV_NO_SYNC=1 UV_CACHE_DIR=/tmp/ch11-uv MPLCONFIGDIR=/tmp/ch11-max-review-mpl OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 uv run pytest tests/test_incerto_calibration.py tests/test_incerto_calibration_figures.py tests/test_incerto_page_snippets.py`.
  **547 passed, 1 skipped in 143.14 s** after all helper and page fixes.
  The skip is the pre-existing local-data layoffs example. Sixteen new
  regression cases cover the four helper defects.
- `scripts/regenerate_incerto_outputs.py --pages incerto-calibration-payoff
  incerto-point-forecast incerto-scoft-ch11 incerto-api-reference` executed
  **128 snippets** after the final fixes; **zero recorded outputs changed**.
  Run with the same `UV_NO_SYNC=1` environment above. The figure test
  regenerated all four SVGs in two separate processes and confirmed that
  both exports equal the existing repository bytes.
- Independent review scripts, `git diff --check`, a separate whitespace scan
  of all 12 untracked files, 371 local file/fragment/figure links and three
  bibliography keys passed. The baseline-file audit found no missing files
  and an empty index. The review changed only the two
  qualified teaching passages, `src/math/incerto/calibration.py`,
  `tests/test_incerto_calibration.py`, and this appended record. Existing
  tracked chapter work was preserved; no file was staged or deleted.
- The full repository suite was not rerun. The earlier 1,522-test result
  remains historical. Fresh locked installation, HTML/site/browser,
  packaging, Lean and post-publication checks were not run in this review;
  the existing gates and limitations above remain open. No uniform numerical
  error guarantee or checked formalization is claimed.

No unresolved mathematical decision blocks these ten claims. Two optional
presentation choices remain for Xiang: make `p_u>0` explicit in the guide's
condensed display at `content/incerto-scoft-ch11.md:36` (it is already required
by the linked mean-excess definition), and give the ordinary finite-variance
CLT a precise theorem locator rather than the current general limit-law
cross-link. Neither was changed as part of the minimal mathematical fixes.
The separate site/browser and publication decisions remain with Xiang.
