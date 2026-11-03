# SCoFT v4 chapter 13 checkpoint

2026-11-02 (America/New_York). Branch `scft/v4-ch13`, base `d002ee7`
from `origin/main`. Xiang selected **gpt-6-astra xhigh** for writing/code
and a separate **gpt-6-astra max** run for mathematical review afterwards.
No delegation, staging, commit, push, publication or repository file deletion.

Chosen title: **Chapter 13 — Probability and payoff risk**.
The teaching and Python scope is implemented. Separate max review, fresh
site/browser verification and post-publication reader review remain distinct
gates. The next writing chunk is `scft-v4-ch14`; it is not started here.

## Contract, sources and boundaries

Read the root and applicable Incerto guidance, rules, notation canon and lock,
program contracts, state, M0.5/visualization review, chapter-11/12 checkpoints,
visualization P2 and code-visibility record, snippet harness and regenerator.
Applied concept, proof, reading-guide, prose, unslop, Git and local site-check
skills. No agent-guidance files or dependency manifests were changed.

Read the supplied v4 PDF and TOC without modifying them. Chapter 13 occupies
printed pp. **253–260**, PDF pp. **267–274**: §13.1 p. 253; §13.2
pp. 253–256; §13.3 pp. 257–258; §13.4 pp. 258–259; §13.5 p. 259;
§13.6 pp. 259–260. The existing `taleb2025scoftv4` bibliography entry
supplies chapter context. The attached `paper-probability-conflation` was
read at [arXiv:2301.10985v1](https://arxiv.org/pdf/2301.10985v1): §§I–II,
pp. 1–3 for the model mathematics and §§III–IV, pp. 3–4 for the scoped
evaluation discussion. Its new entry is only in `content/bibliography.bib`.

All proofs, prose, code and figures are original. Source material is cited
by chapter/section/page; no book text, extract, table or figure is imported.
A Unicode/case-normalized, line-break-dehyphenated scan found zero matching
8-, 10- or 12-word sequences against the full v4 book in the three new
pages, calibration extension, helper and producer. Manual source comparison
also found original explanations. Extraction and comparison files remain
under `/tmp/ch13-review`.
All examples use synthetic finite laws or exact Pareto/beta models. No
observed data, forecasting competition, individual performance comparison
or financial risk guarantee is inferred.

### Source qualifications

- **§13.2, pp. 253–256:** bounded event scores do not identify conditional
  severity. Fixed event probabilities and complete survival curves are
  different information; accurate curves still need uniform tail control
  to bound a mean error. A binary forecast can inform a bounded decision.
- **§13.3, pp. 257–258; §13.6, pp. 259–260:** the chapter's beta model
  randomizes a probability report at fixed Pareto exponent. Its inverse
  survival map is convex. Our random-exponent extension is separately
  defined and proved; it is not attributed to that beta calculation.
- The beta-transformed quantile has moment order `r` exactly below `a*alpha`.
  The mean/variance boundaries and the distinction between an infinite raw
  second moment and a defined variance are explicit. No additional
  `a+b` restriction is needed after the integrability condition.
- A probability integral transform concerns a continuous realized CDF
  value; it does not make every fixed event probability uniform. General
  heavy tails need not be exact Pareto laws. Unnormalized upper-tail
  expectations differ from ES, with quantile atoms requiring fractional mass.
- **§§13.4–13.5, pp. 258–259:** evaluation requires a specified target,
  payoff and joint sampling law. The number of records alone establishes
  neither independence nor an effective sample size of one. No narrative
  judgment or named-person commentary is reproduced.
- **§13.6, pp. 259–260:** the linked finite-sample power-mean statement
  concerns rooted powers and the sample maximum; unrooted population
  moments do not converge to the expected maximum of a random sample.

## Teaching and integration

- New [probability-conflation page](../../content/incerto-probability-conflation.md):
  equal binary score laws with arbitrarily different excess means, uniform
  CDF error without mean control, beta-report propagation and neutral
  evaluation claims. Proofs and numerical illustrations are identified.
- Extended [calibration/payoff page](../../content/incerto-calibration-payoff.md#calibration-payoff-error):
  probability/severity error decomposition, a bounded-severity Brier-regret
  bound, exact Pareto exponent error and a useful binary decision example.
- New [risk-measures page](../../content/incerto-risk-measures.md): VaR/ES,
  quantile atoms, the variational ES formula and subadditivity, Pareto moment
  boundaries, exponent convexity, Jensen/Taylor scope, predictive mixtures
  and retained infinite ES fits in a repeated Hill experiment.
- New [chapter guide](../../content/incerto-scoft-ch13.md): all six source
  sections mapped to canonical pages, notation differences, source
  qualifications, a display equation and a runnable moment-boundary example.

Reused the existing Pareto-moment, asymmetric-payoff, moment-estimation,
calibration/payoff and point-forecast homes. Reader code uses installed
`xmath.incerto` functions with individual API anchors, collapsible long
examples and regenerated outputs. The API reference, MyST TOC, method,
theorem and empirical-example indexes, Incerto hub, SCoFT intro, concept
graph/list and program views are updated. The graph has **50 nodes,
92 dependency edges and 123 reference edges**. No new concept ID is introduced.

State records this chunk's teaching/Python as done and Lean as skipped.
Probability-conflation and calibration/payoff have completed their mapped
teaching scopes. Risk measures remain in progress for chapters 28/29 and
Dynamic Hedging module E. Future reuse lists include the new pages;
earlier checkpoints are preserved. Program concept bodies rise from 39 to
**41**; the 103-ID register, 75 active concepts and 24-body M0.5 review
denominator are unchanged. M05-ISSUE-006/007 remain open at their wider scope.

## hard_math_claims_for_max_review

Review the assumptions, proof and numerical domain around each final anchor.
These are pending independent max review; Python tests are not proof checks.

| Claim | File:line | Claim and support |
| --- | --- | --- |
| CH13-C01 | `content/incerto-probability-conflation.md:26` | Brier regret and exact iid score-law equality do not bound excess-payoff mean error over Pareto laws with fixed event probability; divergence as alpha decreases to one. Local algebra and Pareto integration. |
| CH13-C02 | `content/incerto-probability-conflation.md:117` | Uniform CDF errors and all-threshold Brier regret can vanish while means diverge; the truncated-integral bound requires finite means and uniform tail control. Explicit finite-law counterexample and integral inequality. |
| CH13-C03 | `content/incerto-probability-conflation.md:187`; `src/math/incerto/risk_measures.py:142` | Inverse Pareto survival is convex in probability; beta-report transformed moments exist exactly for r<a*alpha, with density-tail exponent a*alpha and scoped variance boundary. Change of variables and beta integral. |
| CH13-C04 | `content/incerto-calibration-payoff.md:571` | Probability/severity error decomposition, bounded known severity times square-root Brier regret, and fixed-event Pareto excess-error formula. Algebra, with bounded binary decisions retained. |
| CH13-C05 | `content/incerto-risk-measures.md:23`; `:116` | ES quantile-integral and atom formula; variational minimization and subadditivity for integrable losses; finite mutually exclusive-loss counterexample to VaR subadditivity. Original quantile/positive-part proofs. |
| CH13-C06 | `content/incerto-risk-measures.md:172`; `src/math/incerto/risk_measures.py:55` | Exact Pareto VaR/ES and ES infinity at alpha<=1, with the upper-tail probability convention. Local tail integration. |
| CH13-C07 | `content/incerto-risk-measures.md:215` | Strict convexity of Pareto VaR on alpha>0 and ES on alpha>1, Jensen at the mean exponent, and a bounded-perturbation second-order expansion. No arbitrary-estimator bias or variance-only ordering claim. |
| CH13-C08 | `content/incerto-risk-measures.md:273`; `src/math/incerto/risk_measures.py:101` | Common-cutoff random-exponent mixtures dominate the mean-exponent Pareto tail; mixture quantiles remain finite but mixture ES or average quantiles can be infinite. Mixture quantiles differ from averaged model quantiles. Jensen, dominated convergence, Tonelli and explicit counterexamples. |
| CH13-C09 | `content/incerto-risk-measures.md:352`; `demos/incerto/probability_conflation.py` | Repeated iid Pareto/Hill plug-in risk experiment is finite-sample numerical evidence; alpha<=1 fits produce infinite ES and remain in all denominators. No confidence coverage, general Hill theorem or automatic Jensen bias claim. |

## Helpers and figures

New module [risk_measures.py](../../src/math/incerto/risk_measures.py):

| Function | Teaching use | Numerical contract |
| --- | --- | --- |
| `pareto_risk` | Risk page and guide | Exact Pareto VaR/ES; alpha,xm positive, 0<p<1; mathematical infinite ES returned, unrepresentable finite positive results raise. |
| `discrete_risk` | Risk page | Nonnegative finite law; normalized weights within 1e-12 of one; ES fills exactly the upper p mass, including part of a quantile atom. |
| `pareto_mixture_risk` | Risk page | Finite common-cutoff mixture, component alpha in [0.001,1000]; log-survival root and exact component tail integrals; zero-weight components ignored. |
| `beta_pareto_quantile_moment` | Probability page and guide | Nonnegative order, shapes in [0.001,10000], positive alpha,xm; moment boundary checked before beta ratios; order zero is one. |

[Numerical tests](../../tests/test_incerto_risk_measures.py) compare against
independent density integrals, exact rational beta moments, atom examples,
mixture survival and tail integrals. They cover tiny probabilities, zero
weights, moment boundaries, invalid inputs and overflow/underflow contracts.
The public API examples execute `nan`, `inf`, boundary and exception cases.
An additional near-one tail-probability regression reproduces and fixes a
mixture-root bracket failure: `expm1`/`log1p` preserve the small CDF before
ordinary log-survival evaluation takes over.
Existing calibration, Hill, Pareto-moment, finite-payoff and quantile-loss
helpers are reused without changes to their implementations.

All four figures come from
[probability_conflation.py](../../demos/incerto/probability_conflation.py),
using `src/math/incerto/figures.py` for theme, panels and deterministic export.

| Figure under `assets/figures/incerto/` | Page | Inputs and evidence |
| --- | --- | --- |
| `conflation-payoff-gap.svg` | Probability conflation | Exact 20-report Brier distribution at q=p=0.1; u=5 with cutoff adjusted across alpha; exact excess means. |
| `conflation-probability-error.svg` | Probability conflation | Exact inverse quantiles and transformed survival for Beta(2,3), alpha=0.5,1,2 and xm=1. |
| `risk-exponent-uncertainty.svg` | Risk measures | Equal-weight alpha=2±d, d from 0 to 0.95, p=0.01 and xm=1; model averages, mixture and mean-exponent baseline. |
| `risk-estimation.svg` | Risk measures | PCG64 seed 1308, 2,000 iid Pareto(1.2,1) samples of 500; k=20,50,100,200,400 on the same samples; 1,000,000 total draws. |

The Hill figure reports 382, 177, 57, 9 and 0 infinite ES fits respectively,
out of 2,000 at each k. Bands are 10/50/90% sampling quantiles, not intervals
with asserted coverage. The page's shorter experiment uses seed 1307,
400 samples of 250 and k=25/100 (100,000 draws), keeping all fits. The
probability page uses fixed finite inputs and exact model evaluations;
its nonidentification proof is exact.

All four SVGs were rendered to PNG at **390 and 900 px** and visually
inspected. A legend crossing a curve was moved, regenerated and rechecked.
Previews remain under `/tmp/ch13-previews`. The figure test compares two
independent producer processes with the checked-in bytes.

## Verification and limits

The initial focused helper/figure run passed **72 tests in 9.84 s**.
After the endpoint regression and fix, the focused run passed **73 tests
in 9.90 s**, including both fresh-process SVG exports against repository
bytes. The initial full suite passed **1,756 tests, 5 skipped in 470.06 s**;
its collection preceded the additional regression. Final verification below
includes that case in a fresh full-suite collection.


- Final `UV_NO_SYNC=1 uv run pytest`: **1,757 passed, 5 skipped in
  480.37 s**. This includes the unchanged page-snippet harness, exact
  displayed-output comparisons and API-link checks. Skips are one layoffs
  snippet, two S&P snippets and two observed-S&P SVG cases: their local
  CSVs are absent. No chapter-13 case is skipped.
- `scripts/regenerate_incerto_outputs.py --pages incerto-probability-conflation
  incerto-risk-measures incerto-calibration-payoff incerto-scoft-ch13
  incerto-api-reference`: **151 executed outputs**, with no summary-derived
  or full-demo output. The final API prose clarification is retained.
- `uv run python scripts/build_concept_graph.py`: **50 nodes, 92 dependency
  edges, 123 reference edges**; graph tests pass in the full suite.
- Executed the updated `validation.md` validator: state, counts, dependency
  and human-view checks pass, including **1,204 plan file/fragment links**.
  A separate check covers **1,271 local links/fragments in all 19 changed
  Markdown files**, plus local bibliography keys.
- `git diff --check` and separate whitespace checks on all **12 untracked
  files** pass. Reviewed tracked changes and the full new pages, helper,
  producer, tests and checkpoint, as well as all new figures. All changes
  remain unstaged; no files were deleted and no commit was made.

The required `UV_NO_SYNC=1` run uses available dependencies: Python 3.13.5,
NumPy 2.5.4, SciPy 1.18.1, Matplotlib 3.11.2, pytest 9.2.0, PyYAML 6.0.3
and NetworkX 3.7. Locked offline sync could not obtain the uncached SciPy
wheel. An ignored local environment points at available distributions;
editable installation uses this clone's package mapping. No lockfile or
dependency requirement changed. This is not a successful locked install.

`npm ci --offline --ignore-scripts` succeeded from a scratch cache.
`npm run build` in `/tmp/ch13-site` failed at MyST 1.10.1's npm preflight
with `PackageNotFound`; `npm run check:html` consequently reported absent
fresh pages/assets as well as existing unresolved legacy routes. Chrome
could not launch because sandbox socket setup returned `Operation not
permitted`. No successful fresh HTML, browser equations/navigation or live
reader review is claimed. KaTeX parsed **41 displays** across the changed
teaching/API pages; the largest 17px-font width estimate was **303.66 px**,
inside a 358px reading column. This is a font-metric estimate, not a browser
measurement. Logs and equation details remain under `/tmp/ch13-review`.

Packaging checks were not run because import mappings are unchanged.
Lean is **skipped-for-now**, as requested: the optional imported prototype
has no checked development for these probability/risk claims, and no new
declaration or toolchain check is claimed. No publication or hub transfer.

## Decisions and resumption

No unresolved choice blocks the requested implementation. Xiang's selected
separate **gpt-6-astra max** run should review CH13-C01–C09 and the helper
numerical boundaries. Fresh site/browser checks need an environment where
MyST and Chrome can run; any later publication needs the standing live
reader review. Chapter 14 is the next writing chunk. The broader risk-measure
and M0.5 source-audit scopes remain open as recorded in state.

## Max review

2026-11-02. Xiang requested **gpt-6-astra, max reasoning** for this separate
mathematical review. Reviewed the existing unstaged chapter-13 work on
`scft/v4-ch13`, including `git status`, the tracked diff, and the complete
new teaching pages, helper, producer and tests. No delegation, staging,
commit, deletion, publication, or writes to another work directory.

The nine mathematical arguments hold under their stated assumptions.
CH13-C07 and CH13-C09 have the interpretation caveats below. One helper
boundary calculation was **wrong** and is fixed; no public-page equation
needed changing. Locations below refer to the reviewed files after the fix.

### Claim verdicts

| Claim | Verdict | File:line | Independent evidence and scope |
| --- | --- | --- | --- |
| CH13-C01 | **correct** | `content/incerto-probability-conflation.md:26` | Fixed `p,u` give identical Bernoulli observations and therefore identical iid score laws for every constant report. Independent density integration at `u=5,p=0.1`, with adjusted minima, gives excess means `0.25,1,10,100` for exponents `3,1.5,1.05,1.005`. Enumerated all 256 eight-event outcomes at three reports and checked the entire score distributions. The divergence follows algebraically from `up/(alpha-1)`, not from simulation. |
| CH13-C02 | **correct** | `content/incerto-probability-conflation.md:117` | Direct finite-law CDF calculations give distances `0.1,0.01,0.001` and means `10,100,1000`. Splitting the survival integral proves the stated `H` bound. Checked it on 100 independently generated pairs of finite laws. Uniform tail control is a sufficient class assumption; individual finite means or bounded individual supports supply no uniform bound. |
| CH13-C03 | **correct**; helper boundary **wrong → fixed** | `content/incerto-probability-conflation.md:187`; `src/math/incerto/risk_measures.py:162` | Differentiating the inverse survival gives positive curvature. The beta integral is finite exactly for `r<a*alpha`, including divergence at equality; the density and survival powers differ by one as stated. Independent 90-digit transformed-density quadrature gives `4`, `64/35`, and `4` for the displayed finite moments. A million fresh beta draws give mean `1.8299359` against `64/35`, 1.68 theoretical standard errors away. The helper formerly rounded a positive integrability gap to zero; see the exact counterexample below. |
| CH13-C04 | **correct** | `content/incerto-calibration-payoff.md:571` | Adding and subtracting `p*mhat` proves the decomposition. The Brier bound requires the correctly known conditional severity as stated. Checked 10,000 finite input tuples and independently integrated the Pareto payoffs: absolute errors `2.5,5,45` for the displayed fitted exponents. The relative-error denominator is correctly the fitted exponent minus one. |
| CH13-C05 | **correct** | `content/incerto-risk-measures.md:23`; `:116` | Quantile integration and the excess identity include the fractional quantile atom. Independent linear optimization of upper-tail mass gives VaR/ES `5/12.5` in the atom example. On 100 signed finite joint laws, this calculation agrees with the variational minimum and satisfies subadditivity. The mutually exclusive example gives marginal VaR `0,0`, sum VaR `10`, and ES `8,8,10`. The proof covers integrable real losses; the helper intentionally accepts nonnegative finite laws. |
| CH13-C06 | **correct** | `content/incerto-risk-measures.md:172`; `src/math/incerto/risk_measures.py:56` | SciPy's independent Pareto quantile and density integral agree at three exponents and three tail masses, with a cutoff of two. For example, exponent `1.2`, tail mass `0.01` gives VaR `92.83177667`, ES `556.99066003`. The integrand for the first tail moment is proportional to `x^(-alpha)`, proving infinity at and below one. The page correctly limits the boundary assertion to exact Pareto laws. |
| CH13-C07 | **correct-with-caveat** | `content/incerto-risk-measures.md:215` | Independent 90-digit differentiation confirms both curvature formulas. Jensen gives a non-strict inequality for a constant exponent and a strict one for a nonconstant exponent; the ES sentence at line 248 uses “exceeds” after the preceding quantile paragraph states this distinction. The bounded, centered Taylor expansion is valid. For `Z=-1,2` with probabilities `2/3,1/3`, the remainder divided by `epsilon^3` stays bounded as epsilon halves from `0.02` to `0.0025`. No variance-only ordering or arbitrary-estimator bias conclusion follows. Making the ES equality case explicit is an editorial decision below. |
| CH13-C08 | **correct** | `content/incerto-risk-measures.md:273`; `src/math/incerto/risk_measures.py:102` | Jensen gives the common-cutoff survival dominance; dominated convergence proves finite interior mixture quantiles. Independent survival-root solving and density integration give mixture VaR/ES `26.16699356/156.37846976`, versus averaged model values `25.79768151/143.27614531`. A uniform exponent on `(1,2)` has finite mixture quantile `28.74077355` at tail mass `0.01` but infinite mean/ES. Uniform `(0,1)` has a finite mixture quantile while the average model quantile diverges. |
| CH13-C09 | **correct-with-caveat** | `content/incerto-risk-measures.md:352`; `demos/incerto/probability_conflation.py:89` | Independently reconstructed the producer's `382,177,57,9,0` infinite-fit counts using direct upper log excesses. All denominators remain 2,000. A fresh experiment with 12,000 samples of 500, generated as exponentials on the log scale, gives `2122,1014,325,27,1` infinite fits. Counts agree with the exact Gamma tail probabilities within 2.56 binomial standard deviations. The plotted zero at `k=400` is an observed count, not zero population probability; no coverage or general bias assertion is supported by these bands. |

An independent counterexample also checks C07's variance warning. At
`p=0.01,xm=1`, exponents `1.01,2.11` with weights `0.1,0.9` have mean
two, variance `0.1089`, and average model VaR/ES `17.536246/980.155327`.
Equally likely exponents `1.5,2.5` have the same mean and larger variance
`0.25`, but smaller average VaR/ES `13.926960/37.574498`.

The guide's equation at `content/incerto-scoft-ch13.md:38` is **correct**:
the pointwise identity `X*1{X>u}=u*1{X>u}+max(X-u,0)`, followed by Tonelli,
also covers atoms and infinite expectations. An independent atom check
with masses `0.85,0.1,0.05` at `0,5,20` and `u=5` gives both sides equal
to one. Its beta example at line 57 correctly has mean four and infinite
second moment. The producer's four calculations match the page definitions;
the transformed survival uses the beta CDF because the transformation is
decreasing. Apart from the repaired beta boundary, the helper definitions
match the pages, including upper-tail mass rather than confidence as input.

### Minimal fix

At `src/math/incerto/risk_measures.py:162`, replaced the cancellation-prone
extended-precision subtraction with the exact rational gap for the supplied
float inputs, then converted the positive gap for the existing log-beta
evaluation. The moment-boundary decision now precedes this conversion.
There is no new dependency.

Let `e=2**-52`, `a=alpha=1+e`, `order=1+2*e`, `b=1`, `xm=1`.
All these inputs are exactly representable, and
`a*alpha-order=e**2>0` in exact arithmetic. The moment therefore equals
`(2**52+1)**2`, approximately `2.028240960365168e31`. The original helper
returned `inf`; the corrected helper returns the finite value to about
`6e-15` relative error. This is a false mathematical infinity, not a finite
overflow or an ambiguity about rounding decimal input.

Added two deterministic regression cases at
`tests/test_incerto_risk_measures.py:152`, for beta shape `b=1` and `b=3`.
Their independent 100-digit Decimal reference uses the finite-product
identity for integer beta shapes, and checks both the adjacent divergent
order and exact equality at the boundary. An additional 1,000-case
90-digit probe across exponent scales from `1e-200` to `1e200` classified
498 finite and 502 divergent cases correctly; the largest finite relative
error was `2.61e-11`. This probe does not assert uniform floating-point
accuracy throughout the documented domain.

### Source comparison

Read the supplied PDF without modifying it: printed pp. 253–260, PDF
pp. 267–274. Also checked the primary
[2023 article](https://arxiv.org/pdf/2301.10985v1), especially its beta model
on pp. 2–3. The notes correctly qualify the source's inverse-survival
curvature, probability-integral-transform interpretation, moment domain,
and unnormalized tail expectation. No copied book prose was found in
manual comparison or in a fresh full-book scan: zero matching normalized
8-, 10-, or 12-word sequences across the three new pages, calibration
extension, helper and producer. Normalization includes Unicode, case and
line-break dehyphenation. This scan is supporting evidence, not a proof of
authorship. The figures are independently generated from the documented
synthetic models.

Locator correction to the earlier “Source qualifications” section: the
unrooted-moment/expected-maximum assertion is in Remark 13.1's footnote on
printed p. 254. Section 13.6, pp. 259–260, proves the tail-level identity;
it does not discuss the power-mean limit. The guide's mathematical
qualification remains correct.

### Decisions left to Xiang

- At `content/incerto-risk-measures.md:248`, optionally replace “exceeds”
  with “is at least” and explicitly repeat the nonconstant-exponent
  condition for strictness. The preceding paragraph already gives the
  Jensen equality distinction; no theorem or formula needs changing.
- Optionally state next to the Hill figure that zero observed infinite fits
  need not mean zero probability. Here
  `P(alpha_hat<=1)=P(Gamma(k,1)>=1.2*k)`; at `k=400` it is
  `0.0000793353174434`. Thus every finite `k` in this exact model has a
  positive chance of infinite plug-in ES, and its unconditional expected
  plug-in ES is infinite. This additional teaching point is not needed to
  validate the figure's current sampling interpretation.

### Review verification

Independent checks use SciPy 1.18.1 and mpmath 1.4.1, the latter at 90
decimal digits, plus fresh Philox seed `2026110213`: one million beta
reports and six million Pareto observations. Density integrals, finite-law optimization,
derivatives, and simulations are separate evidence from the local proofs.
The script, numerical results, PDF extraction, before-review snapshots and
overlap scan are in `/tmp/ch13-max-review-jdleo0ug/`. No extraction was
added to the repository.

- `UV_NO_SYNC=1 uv run pytest tests/test_incerto_risk_measures.py tests/test_incerto_risk_figures.py -q`:
  **75 passed in 11.49 s**, including both new boundary cases and two
  fresh producer runs matching all four existing SVGs byte for byte.
- `UV_NO_SYNC=1 uv run pytest tests/test_incerto_calibration.py tests/test_incerto_estimators.py -q`:
  **121 passed in 1.82 s**.
- `UV_NO_SYNC=1 uv run pytest tests/test_incerto_page_snippets.py -q -k
  'incerto-probability-conflation or incerto-risk-measures or
  incerto-calibration-payoff or incerto-scoft-ch13 or incerto-api-reference
  or output_blocks'`: **304 passed, 216 deselected in 187.43 s**.
  This includes executed-output comparisons, API anchors and output-block
  checks. Across the three focused runs: **500 passed; none skipped**.
- `scripts/regenerate_incerto_outputs.py --pages incerto-probability-conflation
  incerto-risk-measures incerto-calibration-payoff incerto-scoft-ch13
  incerto-api-reference`: **151 executed outputs; zero changed pages**.
- Verified **416 local links**, including **366 fragments**, across the
  five reviewed teaching/API pages and this record, plus all cited local
  bibliography keys. `git diff --check` and separate whitespace checks
  on all **12 untracked files** pass.
- Compared content hashes with the start-of-review snapshot: only
  `src/math/incerto/risk_measures.py`, `tests/test_incerto_risk_measures.py`
  and this record changed during review. No original file is missing;
  the source PDF hash is unchanged. The index remains empty and all
  original chapter work remains unstaged.

The initial `uv` invocation could not write its default cache. Subsequent
commands set `UV_CACHE_DIR=/tmp/ch13-max-uv-cache` as well as
`UV_NO_SYNC=1`; available dependencies were used without synchronization
or lockfile changes. The earlier locked-install limitation still applies.

The full test suite, fresh HTML/browser checks, packaging and Lean were
not rerun in this focused review. The earlier site/browser limitations
remain open; no deployment or formal proof check is claimed.
