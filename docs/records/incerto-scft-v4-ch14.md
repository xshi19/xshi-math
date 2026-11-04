# SCoFT v4 chapter 14 checkpoint

2026-11-03 (America/New_York). Branch `scft/v4-ch14`, base `1351d17`
from `origin/main`; bibliography submodule at `e396cbd`. Xiang selected
**gpt-6-astra xhigh** for writing/code and a separate **gpt-6-astra max**
run for mathematical review afterwards. No delegation, staging, commit,
push, publication, or repository file deletion.

Chosen title: **Chapter 14 — Forecasts through time**.
Teaching and Python implementation are complete; final verification is
recorded below. Separate max review, fresh site/browser verification and
post-publication reader review remain distinct gates. Next writing chunk:
`scft-v4-ch15`. Lean is skipped-for-now, as requested.

## Contract and source review

Reviewed root and Incerto guidance, shared rules, notation canon and program
notation lock, concept/proof/reading-guide/prose/unslop/Git skills, program
contracts and state, M0.5/visualization review, chapters 12/13 checkpoints,
visualization P2 and code-visibility patterns, snippet tests and regenerator.
The hub-publish skill was used only for scratch local build checks.
No agent-guidance or dependency-manifest change.

Read the supplied read-only v4 PDF and TOC. The requested chapter scope is
printed **261–273**, PDF **275–287**. Verified §14.0.1 pp. 263–264;
§14.0.2 pp. 264–266; §14.0.3 p. 266; §14.1 pp. 266–267;
§14.2 pp. 268–269; §14.3 pp. 269–271; §14.4 p. 271 and the scoped
addendum pp. 271–273. The guide maps every section to the canonical note.

The existing `taleb2025scoftv4` entry in `bib/bibliography.bib` supplies
all chapter context. **No bibliography entry was added or modified.**
The requested initialization command could not update the submodule's
read-only Git configuration, but its checkout was already populated at
`e396cbd` and is clean. No submodule-pointer change or new DOI is needed.
No standalone-paper metadata is asserted without front-matter evidence.

All prose, derivations, code and figures are original. A normalized full-book
comparison found zero matching 8-, 10- or 12-word sequences in the new
concept page, guide, helper and producer. Source extracts and audit files
remain under `/tmp/ch14-review`; no book text, PDF, table or source figure
was imported. All experiments are synthetic, with no election observations
or commentary about individual forecasters.

### Source qualifications retained

- One event, one probability law and nested information sets imply the
  martingale property by the tower law. Market pricing under a different
  law does not identify the forecaster's physical or subjective law.
  Complementary claims summing to one do not force risk neutrality under
  that law. Positive expected gain is weaker than arbitrage.
- The unbounded Gaussian approximation tends to one half at fixed signal
  as remaining standard deviation increases. Its level sensitivity and
  instantaneous forecast volatility are distinct; the latter need not fall.
- The exactly bounded probit martingale has a different limit: its binary
  value tends to the current share at fixed interior threshold as integrated
  latent variance increases. No universal one-half theorem is asserted.
- Proposition 14.1's midpoint qualification does not establish a
  martingale. A symmetric start gives a constant unconditional mean in a
  driftless sigmoid example, but its conditional expectation changes.
  The page supplies the counterexample and the necessary drift correction.
- Thresholds are transformed with their coordinate: majority share one
  half maps to latent zero. Our probit coordinate is sqrt(2) times the
  source's erf coordinate. We derive the correct survival orientation and
  retain the time derivative in the backward equation. No source delta
  approximation is used as an exact share-volatility calibration.
- The revision budget is conditional expected squared variation, not a
  pathwise ceiling. A separate telescoping trading identity supplies a
  sufficient pathwise arbitrage condition with bounded downside. Constant
  nonzero Brownian volatility cannot simultaneously keep an unstopped
  process bounded. The multiple-candidate heuristic is not promoted to
  a theorem.

## Teaching and integration

- New [concept page](../../content/incerto-forecast-martingale.md):
  tower-law proof and converse, fair predictable bets, conditional Brier
  optimality, Gaussian binary valuation, exact probit martingale,
  logistic drift condition, corrected midpoint example, revision budget,
  trading identity, and synthetic diagnostic limits.
- New [chapter guide](../../content/incerto-scoft-ch14.md): section map,
  notation correspondence, source qualifications, display equation and
  runnable comparison of the two uncertainty limits.
- Existing [calibration/payoff](../../content/incerto-calibration-payoff.md)
  and [probability-conflation](../../content/incerto-probability-conflation.md)
  pages receive links only; their teaching is reused without duplication.
- API reference, MyST TOC, three relevant indexes, Incerto hub, SCoFT
  overview, graph/list and program views are updated. The graph has
  **51 nodes, 93 dependency edges and 124 reference edges**.

Program concept bodies rise from 41 to **42**. Stable IDs remain 103,
active concepts 75, and the frozen M0.5 review inventory 24. M05-ISSUE-006
and 007 keep their wider open dispositions. There is no new observed-data
study or Lean evidence. State closure means this chapter's teaching/Python
scope, with max and external site/live gates explicitly separate.

## hard_math_claims_for_max_review

These claims await the separately selected max run. Line references name
the current statements and their surrounding proofs; tests are numerical
evidence, not formal proof checks.

| Claim | File:line | Scope and support |
| --- | --- | --- |
| CH14-C01 | `content/incerto-forecast-martingale.md:26` | Conditional event probabilities form a bounded martingale under one law and nested filtration, also under the report filtration; terminal-indicator converse. Tower-property proof. |
| CH14-C02 | `content/incerto-forecast-martingale.md:69` | Bounded predictable finite-grid gains have zero expectation; conditional Brier regret is the squared probability error. Pricing law Q need not equal P; positive expected gain is not arbitrage. Conditional-expectation and square-expansion proofs. |
| CH14-C03 | `content/incerto-forecast-martingale.md:128`; `src/math/incerto/martingales.py:42` | Gaussian binary value, strict deterministic tie, horizon/scale derivatives, one-half limit, backward drift cancellation, and forecast diffusion coefficient. The underlying normal approximation is unbounded. |
| CH14-C04 | `content/incerto-forecast-martingale.md:202` | Exact anti-mean-reverting Gaussian coordinate, transition law, and bounded probit martingale. Independent-normal convolution proves the conditional mean exactly; Itô's formula supplies the equivalent SDE. |
| CH14-C05 | `content/incerto-forecast-martingale.md:261` | General sigmoid drift cancellation assumes a nonexplosive solution; bounded local martingale becomes a true martingale. Logistic specialization and centered driftless-probit counterexample distinguish unconditional mean from conditional coherence. |
| CH14-C06 | `content/incerto-forecast-martingale.md:295`; `src/math/incerto/martingales.py:80` | Transformed-threshold digital value and its martingale property; large latent-variance limit equals current share, with monotonicity stated only at majority threshold. Exact Gaussian tail calculation. |
| CH14-C07 | `content/incerto-forecast-martingale.md:366` | Conditional expected sum of squared revisions equals initial Bernoulli variance at resolution; truncated-grid inequality and Brier-improvement identity. Finite-grid proof; continuous quadratic variation explicitly uses a cited prerequisite rather than a local proof. |
| CH14-C08 | `content/incerto-forecast-martingale.md:406` | Exact trading gain V minus squared terminal displacement; sufficient almost-sure arbitrage threshold and bounded interim downside. Pathwise algebra, distinct from the expected budget. |
| CH14-C09 | `content/incerto-forecast-martingale.md:436`; `src/math/incerto/martingales.py:122`; `:180` | Exact-transition simulation and necessary revision/level moments; independent-row standard errors and one-row NaN. Neither moments nor one realized path certify coherence. Review near-equal probit differences and latent-coordinate numerical bounds. |

## Helpers and figures

New module [martingales.py](../../src/math/incerto/martingales.py) uses the
existing package mapping and SciPy dependency. It reuses the calibration
Brier evaluator; no existing helper implementation changed.

| Helper | Page use | Domain and numerical behavior |
| --- | --- | --- |
| `gaussian_binary_probability` | Concept, guide, API | Finite mean/threshold, nonnegative finite scale/horizon; long-double intermediates protect the standardized margin; strict deterministic tie and retained CDF saturation. |
| `probit_binary_probability` | Concept, guide, API | Share in [0,1], interior threshold, nonnegative finite latent scale/horizon; absorbed endpoints, stable expm1 variance, strict degenerate event and preserved near-equal quantile differences. |
| `simulate_probit_forecasts` | Concept, API, figures | Interior initial share, positive horizon; zero scale or integrated latent variance in [1e-12,50], with endpoint rounding tolerance documented below; at most 2,000,000 grid cells and 10,000 steps; PCG64; exact transitions and retained latent states. |
| `forecast_revision_summary` | Concept, API, figures | Finite probability matrices with a binary final column; all rows retained; means, Brier curve, predictable level moments and independent-row SEs; one row returns NaN SEs. |

All four functions have individual API anchors and executed examples.
Long examples are collapsible. Input-error, endpoint, deterministic,
NaN/infinity rejection, CDF rounding and one-row behavior are shown as
runnable code with captured plain-number output.

An adjacent-input regression found that inverse-normal rounding could map
two distinct shares to the same coordinate, causing a zero-volatility
path to change from one to zero. The deterministic simulation now retains
the original comparison. The probability evaluator uses an inverse-CDF
midpoint derivative for coordinate gaps below 1e-8, avoiding cancellation;
its local error order and limitations are documented in code. Tests cover
adjacent shares from 1e-300 through 0.8 and a nontrivial scaled-noise case.

The [figure producer](../../demos/incerto/forecast_martingales.py) uses
`src/math/incerto/figures.py` for fonts, vertical panels and deterministic
SVG export. All figures belong to the new concept page and are linked
from the guide.

| Figure under `assets/figures/incerto/` | Inputs and evidence |
| --- | --- |
| `forecast-uncertainty.svg` | Exact Gaussian/probit values at current levels .46/.54, majority threshold, 220-point scale grids; distinct scale units and limiting references. |
| `forecast-dual-paths.svg` | Four exact-transition paths, initial share .54, latent scale .8, horizon one, majority threshold, 100 steps; PCG64 seed 1402. |
| `forecast-revision-budget.svg` | 10,000 independent paths with 40 transitions, same model, seed 1403; coherent probabilities versus alternating ±.12 perturbations clipped to [0,1], preserving initial/terminal values. |

The producer consumes **400,400 normal draws**. Coherent revision-budget
gap is **−0.0010** with SE **0.0021**; the deliberately altered gap is
**1.7639** with SE **0.0055**. **3,587/10,000** coherent realized paths
exceed their expected budget. These are numerical estimates, not a
pathwise contradiction or observed election study. The page's shorter
experiment uses 4,000 paths, 40 steps and seed 1401 (160,000 draws).

All six **390/900 px** PNGs were visually inspected. The latent-path
legend was moved clear of a curve, regenerated and reinspected at both
sizes. Previews remain under `/tmp/ch14-previews`. The figure test checks
two fresh producer processes against all three repository SVG byte strings.

## Verification and limits

The first helper/figure run passed **68 tests in 4.47 s**. After the
adjacent-share correction, **74 passed in 4.45 s**, including unchanged
SVG bytes. The initial full suite passed **1,847 tests, 5 skipped in
250.59 s**; its collection preceded the added boundary regressions.
Final `UV_NO_SYNC=1 uv run pytest`: **1,855 passed, 5 skipped in
254.66 s**. The skips concern three observed-data snippets and two
observed-S&P figure cases whose local CSV inputs are absent. All new
chapter-14 tests and exact-output snippet checks pass. The regenerator
executed **142 teaching/API snippet outputs** across the affected pages.

Canonical graph regeneration produced **51 nodes, 93 dependency edges
and 124 reference edges**. State/human-view validation checks **1,210
plan links**; the changed-Markdown audit checks **1,561 local links**.
Bibliography keys, TOC membership and preservation of earlier chunk/source
records pass. Whitespace/control checks cover **30 changed or new files**,
including all ten untracked files; `git diff --check` passes and full new
files were reviewed.

All three byte-reproducible SVGs were rasterized and inspected at **390
and 900 px**; the path legend was adjusted and both sizes rechecked.
KaTeX 0.19.1 parsed all **18 display equations** on the new pages. The
largest font-metric width estimate is **223.34 px at 17 px**; this is a
layout screen, not a rendered-browser measurement.

The available environment is Python 3.13.5, NumPy 2.4.6, SciPy 1.18.1,
Matplotlib 3.11.2, pytest 9.0.3 and PyYAML 6.0.3. Tests use the pre-existing
editable installation of this clone with `UV_NO_SYNC=1`, a writable
`UV_CACHE_DIR=/tmp/ch14-uv`, `MPLCONFIGDIR=/tmp/ch14-mpl`, and one
OpenBLAS/OMP thread. Scratch locked offline sync failed on an uncached
SciPy wheel. No dependency or lockfile change; this is not a locked-install
pass.

Scratch `npm ci --offline --ignore-scripts` passed after recovering the
cached MyST 1.10.1 archive into a writable cache. `npm run build` in
`/tmp/ch14-site` failed MyST's npm version preflight (`Package Not Found`),
and `npm run check:html` consequently found missing fresh artifacts.
Chromium failed during sandbox socket setup with `Operation not permitted`.
No successful fresh HTML, browser navigation/equation measurement or live
reader review is claimed. KaTeX parsing and font-metric screening are
separate evidence, recorded above.

Packaging checks were not run: the package mapping is unchanged. Lean is
skipped-for-now because the owner requested it and the optional imported
prototype has no checked conditional-probability/stochastic-calculus
development for these claims. No new declaration, toolchain check,
publication or hub transfer.

## Decisions and resumption

No implementation choice needs an owner decision. The selected separate
**gpt-6-astra max** run should review CH14-C01–C09 and the numerical
domains, especially the bounded uncertainty limit, midpoint correction,
conditional versus pathwise revision claims, and adjacent-input behavior.
An operator environment must complete fresh site/browser checks before
publication and the standing live reader review afterwards. Chapter 15
is the next writing chunk; no chapter-15 implementation is included here.

## Max review

2026-11-04. Owner-selected **gpt-6-astra, max reasoning**. This completes
CH14-C01–C09's separate mathematical review and the requested notation audit.
Earlier statements that this review was pending describe the writing checkpoint;
the site/browser and post-publication reader gates remain open. No delegation,
commit, staging, file deletion, publication, or change to another work directory.

Read the incoming `git status` and `git diff`, all four chapter sources, their
tests, the notation canon, the supplied notation-economy rule, and the read-only
v4 PDF at printed pp. 261–273 (PDF pp. 275–287). The
[arXiv v4 record](https://arxiv.org/abs/2001.10488v4) confirms the version and
third-edition metadata. Before-edit copies and the incoming diff are under
`/tmp/ch14-max-review-20261104/before/` and `before.diff`; these distinguish
this review's changes from the pre-existing uncommitted chapter implementation.

### Verdicts and evidence

Verdicts describe the incoming claims; corrections below are already applied.
Locations refer to the final reviewed files. A wrong sentence within a claim
bundle does not invalidate its other, independently checked formulas.

| Claim | Verdict | Final location | Evidence and qualification |
| --- | --- | --- | --- |
| CH14-C01 | **correct** | `content/incerto-forecast-martingale.md:26` | Tower property, adaptation and integrability establish the martingale under the original and report filtrations. The converse uses the included terminal time and terminal indicator; no separate uniform-integrability assumption is needed. An exact nonuniform finite tree also checks report-filtration conditioning. |
| CH14-C02 | **correct** | `content/incerto-forecast-martingale.md:70` | Conditional expectation gives zero gains for bounded predictable finite-grid positions. Square expansion gives conditional Brier regret and an almost-surely unique optimum. The execution assumptions and distinction between forecasting law P and pricing law Q are necessary and already stated. Exact rational tree calculations check gains, regret and score improvement. |
| CH14-C03 | **wrong** in the unqualified level-sensitivity sentence; **fixed** | `content/incerto-forecast-martingale.md:130` | The Gaussian value, displayed derivatives, backward-equation cancellation, strict zero-variance tie and one-half limit are correct. Level sensitivity need not decrease for all remaining scales; the corrected sentence gives both monotonicity regions. Density quadrature agrees within 5.6e-17; 90-digit differentiation checks the formulas. |
| CH14-C04 | **correct** | `content/incerto-forecast-martingale.md:205` | Integrating the linear SDE gives mean exp(sigma² h/2) z and variance exp(sigma² h)−1. Independent-normal convolution proves the bounded share is a true martingale. The Brownian filtration is now explicit. Share-mean quadrature residual is at most 2.3e-16. |
| CH14-C05 | **correct** | `content/incerto-forecast-martingale.md:265` | Itô's formula yields −sigma² S''/(2S'); localization plus boundedness yields a true martingale on the assumed nonexplosive horizon. Logistic drift is bounded and globally Lipschitz. At z=.9, sigma=.8, h=.6 the driftless probit conditional mean is .777871060956286, versus current share .8159398746532405, despite unconditional mean one half. |
| CH14-C06 | **correct** | `content/incerto-forecast-martingale.md:298` | Standardizing the exact latent transition gives the displayed transformed-threshold upper tail. Its large integrated-variance limit is y for every fixed interior threshold. Majority-threshold monotonicity is correct; it need not hold elsewhere. Digital quadrature residual is at most 1.2e-16 and the event-tower residual at most 1.7e-16. |
| CH14-C07 | **correct-with-caveat**; continuous-time scope **fixed** | `content/incerto-forecast-martingale.md:372` | The conditional finite-grid budget and Brier-improvement identity are correct. For a grid beginning at a general t0, continuous variation is [p]T−[p]t0, not [p]T alone. Truncated-grid conditioning is now explicit. Exact rational calculations check both initial-information branches and every later branch, including the unspent conditional variance. |
| CH14-C08 | **correct** | `content/incerto-forecast-martingale.md:415` | Telescoping gives G=V−(pm−p0)². The stated almost-sure threshold is sufficient, with bounded interim downside and holdings under the stated trading assumptions. Exhaustive exact algebra checks 15,625 six-quote paths, including 11,854 satisfying the sufficient threshold. This is not a converse or a test based on one observed path. |
| CH14-C09 | **correct-with-caveat** | `content/incerto-forecast-martingale.md:445`; `src/math/incerto/martingales.py:67`, `:80`, `:122`, `:180` | Transition formulas, terminal resolution, retained latent state, diagnostics and one-row NaN behavior agree with the page. Standard errors now explicitly use the usual i.i.d.-row convention. Fresh independent simulation supports the null identities. Near-quantile accuracy and nominal domain endpoints remain numerical-policy decisions below. |

The [guide](../../content/incerto-scoft-ch14.md), including its tower equation
at line 32, is **correct**. Its source-coordinate correspondence is consistent:
our probit coordinate and latent diffusion scale are sqrt(2) times the source's
erf coordinate and scale. The source's share threshold must transform with the
coordinate. The guide's source qualifications, units, strict-event convention
and Gaussian/bounded limit comparison are retained.

### Minimal corrections

1. Gaussian level sensitivity is phi(d)/s. Its derivative with respect to s is
   phi(d)(d²−1)/s², so it increases for s < |x−u| and decreases for
   s > |x−u|. At x−u=.04 and s=.01,.02,.04,.08, the sensitivities are
   .0133830, 2.6995483, 6.0492681, 4.4008166. The asymptotic zero limit
   survives; the unqualified decreasing claim does not.
2. The continuous revision budget now uses the quadratic-variation increment
   over the actual grid interval. Conditional language is explicit for the
   truncated-grid inequality and its remaining-variance term.
3. The note, helper docstring and API reference now state the i.i.d.-row
   convention behind pooled Monte Carlo standard errors. Independence alone
   is insufficient with unequal row means: for independent coherent one-step
   rows starting at 0 and 1/2, squared revisions are deterministically 0 and
   1/4. Their average has true SE zero, while the pooled sample formula returns
   .125. This qualification does not change the existing identical-model
   simulations or the helper's calculations.

No helper algorithm, function name, signature, dictionary key, simulation seed,
figure producer or figure was changed. `mean`, `share`, `sigma`, `remaining`,
`threshold` and `horizon` still implement the page's current level, share,
model-specific scale, remaining time, share threshold and total horizon.
The helper's internal integrated variance is sigma² times remaining time;
its transformed threshold is the retained k. The producer's latent-noise axis
already displays sigma sqrt(tau), so removing the page's r alias needs no
figure-label change.

### Independent numerical checks

The fresh harness is `/tmp/ch14-max-review-20261104/verify.py`, with results
in `verification.json` and `verification.log`. It uses project NumPy 2.4.6
and SciPy 1.18.1, plus the already available system mpmath 1.4.1 loaded only
for this scratch audit; no dependency or lockfile was changed.

- A 16-leaf tree with exact rational weights 1,...,16 divided by 136 has
  nonconstant initial probabilities 25/36 and 41/100. It checks the tower
  identity, report filtration, conditional Brier regret, predictable gains,
  full and truncated revision budgets, and Brier improvement without any
  floating-point tolerance.
- Four fresh parameter choices each check Gaussian upper-tail density
  integration, bounded-model upper-tail integration, the share mean and the
  event tower by SciPy quadrature. Maximum absolute discrepancy across these
  checks is 2.23e-16. Independent 90-digit differentiation checks Gaussian
  sensitivities/PDE and both probit/logistic drift corrections, with maximum
  residual 4.91e-91.
- A 400-digit mpmath reference covers 233 probit evaluations, including strict
  zero-variance events, subnormal shares, adjacent floats, very large and very
  small scales/horizons, and the quantile-difference branch boundary. Largest
  absolute discrepancies in the ordinary-domain and adjacent-float groups are
  1.12e-16 and 4.92e-14 respectively. The cutoff case is reported separately
  below; these observed maxima are not global error bounds.
- A fresh **Philox seed 2026110401** experiment generates **60,000 paths,
  24 steps, 1,440,000 normal draws**. It independently simulates the Gaussian
  martingale exp(−sigma² t/2) Zt with Brownian clock 1−exp(−sigma² t), rather
  than calling the repository simulator. Inputs are initial share .37,
  threshold .61, sigma 1.1, horizon 1.3. The initial event probability is
  .3030500909429769; observed frequency is .3023666666666667 (−.3645 SE).
  The revision-budget gap is **.000393989945761128**, SE
  **.0008548266800988026** (**.4609 SE**). The maximum absolute standardized
  per-step revision, predictable-level and Brier-improvement residuals are
  **3.3444, 2.7578 and 1.8212**. Zero-variance terminal score residuals are
  checked as exact zeros, not divided by zero. A delete-one-path jackknife
  independently agrees with the reported budget-gap SE within 1e-14.
- The repository simulator is separately checked on **50,000 paths, 12 steps,
  PCG64 seed 2026110402**, initial share .63, threshold .57, sigma .9,
  horizon .8. Standardized innovation mean and variance errors are at most
  2.0142 and 1.1650 SE; the revision-budget gap is −.3856 SE. Initial-value
  error against mpmath is 1.12e-16. These are finite Monte Carlo checks,
  not proofs or simultaneous acceptance guarantees.
- For a non-majority example, share .9 and threshold .7 give probabilities
  .9944149, .8788698, .8993836, .9 at integrated variances .1, 1.8, 10, 100.
  This independently verifies why only the majority case claims monotonicity.
- Extreme Gaussian finite inputs preserve the expected limiting values.
  Representable extreme simulator grids (sigma 1e154, horizon 1e-308;
  sigma 2e-160, horizon 1e308) remain finite. A subnormal horizon that cannot
  represent two distinct steps is rejected explicitly; with zero scale and
  one step the same horizon is accepted.

### Source originality and verification

Manual comparison against all thirteen supplied chapter pages found no copied
or closely paraphrased source prose in the note or guide. A fresh normalized
comparison against the **full v4 book** finds **zero matching 8-, 10- or
12-word sequences** in either page, the helper, or the producer. The longest
prose run in the guide is the attributed seven-word chapter title; the note's
longest is a five-word historical name/section phrase. Such screens cannot
certify originality on their own; the manual comparison also checked sentence
structure and exposition. The proofs, synthetic examples and source corrections
are independently written. Source text and audit artifacts remain under `/tmp`.

`UV_NO_SYNC=1 uv run python scripts/regenerate_incerto_outputs.py --pages
incerto-forecast-martingale incerto-scoft-ch14 incerto-api-reference` executed
**142 snippet outputs**, with **zero output changes**. The guide, note and API
examples therefore still match the implementation after the notation pass.

Requested full suite: **`UV_NO_SYNC=1 uv run pytest` — 1,855 passed,
5 skipped in 273.00 s**. Skips are the existing absent-observed-data cases.
The suite includes exact teaching/API output checks and the chapter's two-fresh-
process figure comparisons; all three existing SVG byte strings are unchanged.
Tests used the pre-existing editable environment, with writable caches under
`/tmp/ch14-max-review-20261104/` and single-threaded BLAS/OMP; this is not a
fresh locked-install check. The complete log is `pytest.log` in that directory.

KaTeX 0.19.1 parses all **18 display equations**. The maximum font-metric
width estimate after inlining is **242.08 px at 17 px**; the transformed digital
formula estimates **191.83 px**. This is a parsing/layout screen, not a browser
measurement. A fresh standalone equation-preview attempt with Chromium failed
at `setsockopt: Operation not permitted`, exit 133; no screenshot was produced.
Full MyST/HTML checks were not rerun, and rendered-browser equation/navigation
review remains open. Packaging and Lean checks were not run; no packaging,
formalization or publication work is part of this review.

`git diff --check` passes. The final audit checks **1,562 local Markdown
links**, citation keys, TOC membership, and whitespace/control characters in
all **30 incoming changed/new files**, including the ten untracked files.
Before/after hashes confirm that this review changed exactly five files:
the concept note, chapter guide, API reference, helper docstring and this
record. The producer, figures, tests, graph, program views and every other
incoming file retain their original bytes. No new/deleted repository paths,
staged changes or branch change were introduced. The review-only diff is
`/tmp/ch14-max-review-20261104/review.diff`.

### Owner-approved resolutions

2026-11-04. Owner-selected **GPT-6-Astra xhigh**. The owner approved the
following resolutions after the max review and the merge of `origin/main`,
including notation B1. No Git commands or changes to `bib/` are part of this
follow-up.

- **Near-quantile accuracy contract.** Just above the existing 1e-8 latent-gap
  cutoff, direct subtraction of rounded inverse-normal values loses precision.
  At share `6.220961130021608e-16`, threshold `6.22096057427174e-16`, sigma
  `1.571428640309474e-8`, horizon 1, the helper returns
  `.758036354302486`; the 400-digit reference is `.7580363281495356`
  (absolute difference **2.6153e-8**). The owner accepted this measured
  accuracy with the algorithm unchanged. The function docstring and API
  reference now report errors up to about 2.6e-8 observed only for shares
  around 1e-16 just above the cutoff, alongside the measured ordinary-input
  maximum 1.12e-16 and adjacent-float maximum 4.92e-14. These are observed
  errors from the 233-evaluation, 400-digit audit, not global error bounds.
- **Nominal simulator endpoints.** With horizon 1, literal `sigma=1e-6`
  produces extended-precision integrated variance
  `9.999999999999999095e-13`, while `sigma=sqrt(50)` produces
  `50.000000000000003695`; the former strict interval check rejected both.
  The simulator now allows relative tolerance `8*np.finfo(float).eps`
  (about 1.8e-15) in integrated variance, with no absolute tolerance.
  Values on either side within that distance of an endpoint are treated as
  the endpoint by rescaling sigma in extended precision; out-of-range
  values beyond the tolerance still raise `ValueError`. The simulator
  docstring and API reference document the policy. New regressions cover
  both literal endpoints at horizon one, equivalent scales at horizons
  .25 and 4, identical paths for inward/outward rounding perturbations,
  and rejection beyond the tolerance at both boundaries.
- **Continuous-time sourcing.** The quadratic-variation extension remains
  explicitly a stochastic-calculus prerequisite, with a complete finite-grid
  proof only. The extension sentence now cites `[@karatzas1991brownian]`,
  Karatzas and Shreve, *Brownian Motion and Stochastic Calculus*, second
  edition (1991). The key is already present in `bib/bibliography.bib`;
  the submodule was read but not edited. No continuous-time proof was added.

The final prose pass follows [notation economy](../rules/notation-economy.md).
No mathematical symbols or aliases were introduced; the reviewed notation,
formulas, assumptions, strict-event conventions and proof scope are retained.

### Follow-up verification

`uv run pytest -q tests/test_incerto_martingales.py tests/test_incerto_martingale_figures.py`
passed **86 tests in 60.93 s**, including twelve new endpoint regressions and
the two-process SVG reproducibility check. The first run passed all 85
numerical tests but hit the figure subprocess's 60-second timeout while
Matplotlib built its font cache. A standalone figure run then completed;
all three generated SVGs matched the repository bytes. The requested test
command passed on retry without changing the figure test or its timeout.
Runs used writable UV/Matplotlib caches under
`/tmp/ch14-owner-resolutions-20261104/` and one OpenBLAS/OMP thread;
`UV_NO_SYNC` was not set.

Reviewed the follow-up diff against saved before-edit copies of the five
edited files: helper, numerical tests, API reference, concept note and this
record. AST comparison excluding docstrings confirms that both probability
algorithms are unchanged; the bibliography remains byte-identical. Checked
**358 local Markdown links**, **5 citation occurrences**, unchanged math
expressions in both edited content pages, and whitespace in all five files.
The before-edit copies and follow-up diff are under the same scratch directory.
No Git command, commit or bibliography edit was made.

The full suite, site/HTML/browser checks, packaging and Lean were not rerun.
The existing site/browser and post-publication reader gates remain open;
this follow-up closes the three owner-approved resolutions only.

## Notation audit

Applied `/workspace/notation-economy-rule.md` after settling the claims,
using the shared canon, sibling calibration/forecast notes, and the source's
coordinate conventions. This inventory belongs in the record, not on the
published pages. Variants in one row denote the same object at different times
or values; separate meanings of the same letter are listed separately.

### Removed auxiliary definitions

| Symbol | Page | One-line reason and replacement |
| --- | --- | --- |
| D = indicator of A | Note and guide | The explicit indicator keeps the fixed terminal event visible and remains short in the tower and Brier formulas. |
| a = sigma²/2 | Note | This is a determined coefficient, not an independent model parameter; write sigma²/2 in the SDE and exponents. |
| r = sigma sqrt(tau) | Note | The direct integrated variance sigma² tau exposes the parameter dependence without an extra uncertainty alias. |
| v = sqrt(1−exp(−r²)) | Note | This is only the valuation denominator; display it directly rather than require two levels of lookup. |

Removing the uncertainty alias r does **not** remove the unrelated bound
variable r in the filtration generator or stochastic integral. The scale-axis
quantity sigma sqrt(tau) and all its units remain in the figure caption and code.

### Retained symbols in the concept note

| Symbol | One-line reason |
| --- | --- |
| P | Primary probability law; the distinction from a pricing law is substantive. |
| E | Canonical expectation operator; conditioning carries the information set. |
| F_t | Primary filtration needed for every conditional claim and predictable strategy. |
| A | The fixed terminal event is the object being forecast throughout. |
| indicator of A | Displays the binary terminal payoff directly, including its idempotence in the budget proof. |
| p_t; p(t,x), p(t,y) | The forecast process and its two model-specific value functions are the subject of the page. |
| t, s (time indices), T | Times and the terminal horizon are necessary indices; the later scale s has a separately declared scope. |
| G_t | The report filtration is a distinct information set required for the smaller-filtration result. |
| sigma(·) (sigma-algebra operator) | Standard construction of the report filtration; distinct from diffusion scale sigma. |
| r (bound time variable) | A local dummy index in the report history and stochastic integral; it introduces no stored quantity. |
| t_i, t_0, t_m; i, m | The deterministic grid, endpoints and finite-sum indices are necessary for trading and revision formulas. |
| h_i | The chosen predictable position is an applied quantity reused in fair-gain and pathwise arguments. |
| Delta p_i | Standard forecast increment reused in gains, budgets, proofs and diagnostics. |
| G | Terminal trading gain connects the fair-betting proof to the pathwise strategy. |
| q_t | A distinct competing report is necessary to state proper-score regret and uniqueness. |
| Q | A genuinely different pricing law is required for the forecasting/pricing distinction. |
| X_t, x, x_0 | Primary Gaussian state, current value and initial value. |
| sigma (diffusion scale) | Primary model parameter with explicit, different units in the Gaussian and latent models. |
| W_t | Brownian driver needed to state the SDEs and their filtration. |
| u | Canonical threshold; preserving the strict event and transformed boundary is central. |
| tau = T−t | Remaining time has substantive horizon sensitivities, limits and API/figure uses. |
| s = sigma sqrt(tau) (normal SD) | Remaining Gaussian standard deviation is an applied uncertainty input with its own derivative and figure axis. |
| d = (x−u)/s | The standardized margin is meaningful and substantially shortens all sensitivities and the backward equation. |
| Phi | Canonical normal CDF links Gaussian valuation to the bounded probit transformation. |
| phi = Phi' | Standard normal density has substantive derivative, drift and volatility uses. |
| N(·,·) | Standard normal-distribution notation; its second parameter is explicitly the variance. |
| indicator of {x>u} | The explicit strict deterministic event preserves the zero-variance tie convention. |
| Y_t, y | Primary bounded share and current value; its local role is distinguished from Normix mixing notation. |
| Z_t, z, z_0 | Primary latent state, current coordinate and initial coordinate; separate from both share and event probability. |
| h (time increment) | Necessary transition horizon, with a separate scope from holdings and diagnostic instruments. |
| H | The independent auxiliary standard normal makes the CDF-convolution proof explicit. |
| N (random variable) | The other independent standard normal supplies the Gaussian convolution; scoped to that proof. |
| b (normal location) | Proof-local free location keeps the reusable normal identity readable and is immediately specialized. |
| c (normal scale) | Proof-local free scale makes the convolution variance transparent and supports the driftless counterexample too. |
| S | The general sigmoid is a mathematical object, not an alias for a particular probit/logistic formula. |
| b(z) (drift function) | The unknown drift is exactly what the general construction solves for; scoped separately from proof-local b. |
| k = Phi inverse of u | The transformed event boundary has substantive roles in valuation, coordinate consistency, limits and the helper. |
| p_i = p at t_i | Deferred to the grid section, this abbreviation substantially shortens repeated algebra without changing the forecast. |
| V | Realized total squared revisions is a distinct statistic reused in the budget and pathwise threshold. |
| [p]_t | Standard quadratic variation names the continuous-time object to which grid sums converge. |
| h (diagnostic function) | A general bounded predictable instrument is needed to distinguish moment checks from a full conditional identity. |

### Retained symbols in the guide

| Symbol | One-line reason |
| --- | --- |
| A and its indicator | Replaces D while preserving the same resolved event in the organizing identity. |
| F_t | Explicitly names the nested information sets before the tower equation. |
| E | Canonical conditional expectation states the organizing identity. |
| p_t, p_s | The actual binary reports at the compared times. |
| s, t | Necessary ordered time indices in the martingale identity. |
| Y | The bounded share is the same substantive object in the source and the note. |
| B | Retained only as the source's forecast notation in the correspondence, not as a second local forecast name. |
| u | The share threshold whose coordinate must be transformed. |
| k | Names the note/helper's latent threshold in the source correspondence. |
| Phi | Defines the transformation and inverse; now introduced with the canon link before its first use. |
| x | The source's erf coordinate, needed for the normalization comparison. |
| z | Our probit coordinate, with the required sqrt(2) conversion. |
| sigma | The note's latent diffusion scale, whose conversion and distinction from share volatility matter. |

No parallel notation canon, API alias or extra published inventory was added.
Claims, domains, strict inequalities, endpoint behavior, conditioning, units,
source attribution and figure meanings were compared before and after the pass.
