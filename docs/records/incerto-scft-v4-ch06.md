# SCoFT v4 chapter 6 checkpoint

Date: 2026-10-18 (America/New_York). Branch `scft/v4-ch06`, base `8c50598`
from `origin/main`. Owner-selected model: **gpt-6-astra xhigh** for writing
and code. The separate owner-requested **gpt-6-astra max** review is
recorded [below](#max-review). The implementation checkpoint retains its
original checks and pending-review wording. No delegation, commit, staging,
push or publication.

Chosen guide title: **Chapter 6 — Thick tails in higher dimensions**.
It matches the source topic and the chapter-1–5 navigation pattern.
No title or mathematical scope decision is required from Xiang.

## Contract and sources

Executed `scft-v4-ch06`, including attached source unit `scft-v4-appa`:
teaching first, bounded Python second, optional Lean last. Read root/track
guidance, all shared rules, notation canon and program notation lock,
program contracts/state/review, prior chapter records and touched pages.
Used concept-page, proof-writing, reading-guide, prose-review/unslop,
git-conventions and hub-publish workflows. The URL map, shared notation,
bibliography, package mapping and dependency locks are unchanged.

Read the supplied read-only `/workspace/scoft-toc/2001.10488v4.pdf` and
`v4-toc.txt`. Source text extraction and previews stay in `/tmp`; no PDF,
TOC extract, copied book text, table or figure is added to the repository.
All chapter context uses `taleb2025scoftv4`, third edition (2025),
arXiv:2001.10488v4. Page numbers below are printed; PDF pages are offset
by 14. Chapter opening is p. 107, transition p. 120, appendix opening p. 121.

| Source section | Printed pages | PDF pages | Teaching scope |
| --- | --- | --- | --- |
| §6.1 | 108 | 122 | Shared Gaussian variance mixing; covariance and central density |
| §6.2 | 109–112 | 123–126 | Elliptical characteristic functions, linear maps and switching correlation |
| §6.3 / §6.3.1 | 113–114 | 127–128 | Normalized Student density; dependent versus independent Cauchy coordinates |
| §6.4 | 114–115 | 128–129 | Entropy and mutual information with explicit integrability |
| §6.5 | 115–116 | 129–130 | Specified Wigner ensemble, finite-variance limit, finite spectral identities |
| §6.6 | 116–117 | 130–131 | Centered and uncentered sample coefficients; undefined population moments |
| §6.7 | 117–119 | 131–133 | Independent-error regression population target and consistency |
| §A.1 | 122–124 | 136–138 | Symmetric location mixture, kurtosis, rare Pareto regime contrast |
| §A.2 | 124–125 | 138–139 | Homogeneous absorbing chain and nonpersistent-hazard counterexample |

Additional checked inputs: [DLMF 5.12.1](https://dlmf.nist.gov/5.12#E1)
for the beta integral; [Tao, 254A Notes 4](https://terrytao.wordpress.com/2010/02/02/254a-notes-4-the-semi-circular-law/),
Theorem 1 and §1's truncation reduction, for the empirical semicircle law.
The latter is cited, not proved; the note states nested minors of one infinite
real symmetric iid-entry matrix, mean zero, variance one, and square-root
normalization. Finite spectral identities are proved separately.

The source's historical regressions, portfolio prescriptions, general
upward-bias claim, and finite-sample rate are not adopted as established
results. The Student entropy is derived from normalization and the beta
integral instead of importing the source's special-function expression.
Independent Cauchy coordinates explicitly disprove a general stable-to-
elliptical implication. Scatter, covariance, and centered/uncentered sample
coefficients have separate definitions. Appendix A is treated through stated
special cases, not a blanket claim about every irreversible process.

## Teaching and hard claims for max review

| ID | Claim and assumptions | Location |
| --- | --- | --- |
| CH06-C01 | Shared positive variance mixing gives elliptical characteristic functions; linear-map closure, covariance under finite mixing mean, and central-density increase for the bounded two-state mixture. | [Shared scale](../../content/incerto-multivariate-tails.md#multivariate-elliptical) |
| CH06-C02 | Gamma precision integrates to the normalized multivariate Student; projections share degrees of freedom and covariance exists only above two. | [Student derivation](../../content/incerto-multivariate-tails.md#multivariate-student) |
| CH06-C03 | Conditional precision gives a scale depending on the first coordinate, hence dependence at diagonal scatter; bounded joint absolute-exceedance excess is strictly positive. | [Zero correlation](../../content/incerto-multivariate-tails.md#multivariate-zero-correlation) |
| CH06-C04 | Beta radial transform and differentiable normalization give finite Student entropy for all positive degrees of freedom; entropy subtraction gives mutual information, including the exact Cauchy constant. | [Information](../../content/incerto-multivariate-tails.md#multivariate-information) |
| CH06-C05 | Independent versus spherical Cauchy constrained density geometry; exact sector mass; switching-normal nonellipticality; independent stable Cauchy counterexample. | [Geometry](../../content/incerto-iso-density-tail-geometry.md#tail-geometry-elliptical), [switching](../../content/incerto-iso-density-tail-geometry.md#tail-geometry-switching) |
| CH06-C06 | Centered and uncentered coefficients are bounded when defined; one paired fixed-sample contamination drives both to its sign without any iid sampling claim. | [Sample coefficients](../../content/incerto-multivariate-tails.md#multivariate-sample-correlation) |
| CH06-C07 | Cited empirical semicircle scope versus extreme-eigenvalue/covariance questions; proved trace-square identity and largest-entry spectral-radius bound. | [Spectra](../../content/incerto-multivariate-tails.md#multivariate-spectra) |
| CH06-C08 | Independent centered finite-variance error gives the stated population squared correlation; SLLN and OLS normal equations give consistency; bounded convergence gives convergence of expectations, with no universal bias sign or rate. | [Regression](../../content/incerto-multivariate-tails.md#multivariate-regression) |
| CH06-C09 | Location-mixture moments/kurtosis/MGF and central valley; absorbing-chain power and decreasing-hazard counterexample; positive Pareto regime weight preserves moment gates and exponent. | [Regimes](../../content/incerto-tail-class-catalog.md#tail-catalog-regimes), [absorption](../../content/incerto-tail-class-catalog.md#tail-catalog-absorbing), [Pareto mixture](../../content/incerto-pareto.md#pareto-regime-mixture) |

Also review the numerical boundary policies in the new helper, including
restricted Student degrees of freedom, undefined coefficient handling,
scale-before-centering arithmetic and finite versus nonrepresentable values.
Tests and figures are supporting computation, not proofs of cited limits.

New guide and multivariate note are wired into the explicit Incerto TOC,
track hub, SCoFT overview, distribution index, API reference and generated
concept graph. Geometry, catalog and Pareto pages are extended at their
canonical homes; prior chapter arguments are linked. Graph generation reports
**36 nodes, 62 dependency edges and 69 reference edges**. Routes retain
`/math/incerto/`; no legacy URL-map rows are invented.

## Python, worked values and figures

New [helper](../../src/math/incerto/multivariate.py),
[runner](../../demos/incerto/multivariate_tails.py), and
[tests](../../tests/test_incerto_multivariate.py). Installed imports remain
`xmath.incerto`. No new dependency, dataset, package mapping or formalization.

The helper computes Student entropy/information, shared-scale bivariate
Student samples, centered or uncentered sample coefficients, symmetric
spectra, finite-variance regression targets and location-mixture kurtosis.
Student routines deliberately restrict degrees of freedom to **[0.5, 1000]**;
this is a numerical API scope, not the mathematical existence domain.
Constant centered columns and zero uncentered vectors return NaN; infinite
population error variance is rejected instead of assigning correlation zero.
Nonfinite sampler output and spectral overflow raise without removing data.
Coefficient normalization uses powers of two and reference subtraction to
preserve represented differences at large offsets. A final coefficient clamp
only bounds floating roundoff to the exact interval [-1, 1].

| Figure | Reproducible bounds |
| --- | --- |
| `multivariate-geometry.svg` | 241×241 grid on [-4,4]²; independent/spherical Cauchy and equally weighted normal correlations ±0.8; four fractions of origin density |
| `multivariate-information.svg` | 121 degree values from 0.75 to 30, scatter parameters 0/0.6; 61 thresholds from 0.2 to 8 at degree 3; gamma-precision quadrature |
| `multivariate-spectra.svg` | 12 symmetric 80×80 matrices per law: normal, variance-standardized Student 3, unit-scale Student 1.5; full eigenvalue CDFs and explicit normalization |
| `multivariate-sampling.svg` | 400 replications at n=30/100/300/1000; shared-scale Students 1.5/5 at scatter 0.6; independent Student-3 error in V=X+error |
| `multivariate-regimes.svg` | 481 density points on [-6,6]; 241 separation values [0,5]; 100 conditional-hazard steps |

All five use `set_theme(scale=1.1)` and `savefig` from the shared
`src/math/incerto/figures.py`, bundled regular serif fonts, single-column
layouts and external legends. PCG64 seed **20261018** is fixed; the largest
Student sampling array has 400,000 pairs. No clipped observations, omitted
eigenvalues, external data, censoring or fitted parameters. Bands are
10th/50th/90th sampling quantiles, not confidence intervals. Quadrature is
one-dimensional, limit 200, absolute/relative tolerance 1e-9; errors above
2e-8 stop the run. The maximum joint-tail error estimate was **9.97e-10**.

Representative outputs:

- Cauchy sector, radius >3 and angle width pi/3: **0.0527046276695**.
- Zero-scatter-correlation Student information: nu=1 **0.224171427529**,
  nu=3 **0.0424114106506**, nu=5 **0.0171282784194** nats.
- Complete eigenvalue ranges: normal **[-2.05153038, 2.10446003]**;
  Student 3 **[-6.42697972, 6.72234465]**; Student 1.5
  **[-90.0787534, 89.8717092]**, under the declared finite normalization.
- At n=1000, 10/50/90 sample-correlation quantiles are approximately
  **0.2571/0.6375/0.8803** for nu=1.5 and **0.5622/0.6052/0.6439**
  for nu=5. Only the latter has population Pearson correlation 0.6.
- Regression target **0.25**; n=1000 fitted R² quantiles
  **0.2085/0.2605/0.3108**.
- Location mixture m=2, sigma=1: kurtosis **1.72**. Survival at step 100:
  constant hazard **0.00592052922033**, decreasing hazard **0.577576190173**.
- Rare Pareto regime: survival at four **0.0025**, mean **0.55**,
  infinite second moment.

## Task B: chapter-5 reader fixes

Regenerated through [power_laws.py](../../demos/incerto/power_laws.py), using
the shared export. All four chapter-5 SVGs were regenerated because the
runner exports the whole set; entropy's curves are unchanged and its legends
also move outside axes.

1. **Matching:** all legends are below the axes. The double-Pareto central
   spike is fully exposed. Updated the double-Pareto page caption/alt text.
2. **Diagnostics:** explicit signed ticks on the broad symlog panel and a
   separate linear panel for exponential/logistic. Exponential is exactly
   zero; logistic approaches zero from below. The convolution panel remains
   separate. Updated the survival-ratio page caption/alt text.
3. **Integrals:** positive truncated moments use log-log axes, omitting only
   the mathematically zero endpoint b=1 (240 plotted points remain). There is
   no symlog linear/log switch. Updated the moment-page caption, alt text and
   grid description. No distribution or data truncation was introduced.

Rendered the **actual nine SVGs** through system librsvg/Cairo at **390px
and 900px** and visually inspected all 18 previews. An initial crowded
minor-tick axis in the new information plot was replaced with explicit
threshold ticks; all four sampling sizes are also labeled. Final labels,
legends and central spike are legible and unclipped. Scratch previews live
under `/tmp/ch06-previews`; they are not generated-site browser evidence.

## M0.5, verification and resume

**M05-ISSUE-007:** chapter-6 density geometry and new chapter/appendix
context now use the pinned v4 key and checked locators. Recorded this scoped
resolution in M0.5; other chapter assignments and global issue totals remain
unchanged. **Lean: skipped-for-now**, as requested, because no toolchain
or sandbox network is available. No checked declaration is added.

| Check | Actual result |
| --- | --- |
| `UV_CACHE_DIR=/tmp/m05-uv-cache UV_OFFLINE=1 uv sync --locked` | Passed using the existing writable offline cache. |
| `uv run pytest` with that cache, writable Matplotlib cache and one BLAS thread | **443 passed**, including **51 chapter-6 cases**. Tests include independent density/entropy integrals, two joint-tail conditioning routes, exact Cauchy information, OLS identity, spectral invariants, sampling indicators, domains and extreme scales/offsets. |
| Chapter-6 and chapter-5 demos | Passed finite/error checks and exported five new/four regenerated SVGs. Repeat-generation hash audit recorded below. |
| `npm ci --offline --cache /tmp/m05-npm-cache --no-audit --no-fund` | Failed ENOTCACHED for MyST 1.10.1. Copied local pub32 node_modules only after byte-identical package-lock comparison. |
| `npm run build` | Failed at MyST npm preflight; direct Node child-process probe reproduces `EPERM spawnSync /bin/sh`. No fresh HTML build. |
| `npm run check:html` | Failed on missing fresh HTML/config/assets after blocked build. |
| State validator, source links/citations/TOC, graph, whitespace | Final audit below; source membership is not an HTML pass. |
| Separate Astra max review | Pending; claims CH06-C01 through C09 above. |
| Browser equations/navigation and post-publication live review | Not performed; require external build and authorized publication. |
| Wheel / Lean | Not run: mapping unchanged; Lean explicitly skipped. |

State marks chapter 6 and appendix A done at the implemented teaching/Python
scope and advances `next_chunk` to `scft-v4-ch07`, as requested. Three concepts
finish their scheduled implementation scopes; multivariate tails remains
in progress for chapter 29. All retain honest pending max-review evidence.
There are **32 implemented concept bodies**, while M0.5 remains **24**.
Chapter 7 is a resume pointer, not work executed or authorized here.

No decision is required from Xiang before the separate max review. The
remaining actions are that review, external site checks and a fresh reader
review after publication. No commit, file deletion or hub transfer was made.

## Final source and artifact audit

- **443 tests passed in 4.48s**. All nine SVG hashes are identical after
  rerunning both demos with the declared cache and thread settings. All 18
  actual-SVG PNG previews were inspected; final information/sampling tick
  fixes were re-rendered and checked at both widths.
- The executable state/human-view validator passes, including **1,035** local
  plan file/fragment links, stable IDs, exact chapter order, source mappings,
  deliverable flags and the frozen M0.5 review inventory. Only later reuse
  lists gain the new multivariate page; later work remains unstarted.
- Source audit passes for **36 changed/new files**, including **11 new files**,
  **723** relative file/fragment links and **82** content citation references.
  All six chapter titles agree across navigation. Source membership is
  **55 Incerto pages, 79 pages overall and 75 flat redirects**. These are
  source counts, not generated HTML evidence.
- Reviewed mathematical prose, the full new helper/runner/tests/guide/note/
  record, tracked diffs and graph output. The final proof pass makes the
  regression expectation's bounded extension on degenerate samples explicit;
  the actual coefficient remains undefined and the helper returns NaN.
  Preserved the geometry page's old `statement` anchor.
- A normalized nine-word overlap scan finds no matching passage between
  changed teaching (excluding retained license notices) and the supplied
  chapter/appendix. This supplements original drafting and manual comparison;
  it is not a copyright classifier. The supplied PDF retains SHA-256
  `758e18b7337840104db93296144d67cf5514bf2de128fe557dc84bc32a0ad567`.
- `git diff --check`, separate new-file whitespace/final-newline checks and
  SVG XML checks pass. No deleted or staged files: **25 modified, 11 new**.
  Shared notation, URL map, bibliography, package mapping and locks retain
  their input bytes. No commit or publication occurred.
- No successful HTML build, rendered-equation/browser review or live reader
  pass is claimed. A direct optional KaTeX syntax probe was also unavailable
  because this dependency tree exposes no standalone `katex` module.

## Max review

2026-10-18, owner-selected **gpt-6-astra max**, on the uncommitted
`scft/v4-ch06` worktree. **Verdict: the priority mathematical claims are
correct.** Fixed a numerical input-domain error and an incomplete figure
caption. No population formula or plotted value needed correction.
This section supersedes the earlier pending-max-review statements.

Read the required guidance, all shared rules, validation/verification
contracts, the incoming diff and complete new source files. Checked the
supplied PDF read-only; its SHA-256 remains
`758e18b7337840104db93296144d67cf5514bf2de128fe557dc84bc32a0ad567`.
Source extracts and figure previews remain in `/tmp/ch06-max-review` or
other `/tmp` files. No book text or source figure was added to the repository.

### Claim verdicts

| Claim | Verdict | Review finding |
| --- | --- | --- |
| CH06-C01 — elliptical scale mixtures, linear maps, covariance | **Correct** | Conditioning gives the displayed characteristic function. Finite mixing mean gives finite second moments and covariance `E[Y] Sigma`; arbitrary deterministic linear maps allow singular images. Strict convexity proves the two-state central-density increase. A finite Gaussian mixture still has finite directional MGFs. |
| CH06-C02 — normalized Student, projections, moment gates | **Correct** | Gamma shape/rate and all normalizing factors agree. A nonzero projection has scale `sqrt(b^T Sigma b)` and the same degrees of freedom. Positive absolute moments have order below `nu`; the covariance multiplier `nu/(nu-2)` applies only for `nu>2`. |
| CH06-C03 — diagonal scatter and joint exceedances | **Correct** | The posterior gamma rate is `(nu+x^2)/2`; the conditional Student scale depends on `x`. Pearson correlation is zero only when `nu>2`. The joint absolute-exceedance excess is the strictly positive variance of a bounded, strictly monotone function of the shared scale. |
| CH06-C04 — entropy, mutual information, Cauchy value | **Correct** | The beta radial transform and differentiated beta integral give the stated entropy. Endpoint logarithms are integrable for every `nu>0`, so entropy subtraction is valid. At `nu=1`, `h1=log(4*pi)`, `h2=log(2*pi)+3`, and the excess information is `log(8*pi)-3 = 0.224171427529...` nats. |
| CH06-C05 — sector mass and nonelliptical examples | **Correct** | The spherical Cauchy radial tail is `1/sqrt(1+u^2)` and angle is independent uniform. The sector value is `1/(6*sqrt(10))`. Switching correlations preserve covariance `I2` but violate radial characteristic-function symmetry. Independent Cauchy coordinates are stable with an L1 characteristic exponent, which cannot be an elliptical quadratic-form profile. The constrained-density arguments do not claim a tail-probability limit. |
| CH06-C06 — sample bounds and contamination | **Correct** | Cauchy–Schwarz supplies both bounds when denominators are positive. The centered leading vectors use `H e_n` with squared norm `1-1/n`; both coefficients tend to `sign(c)` for fixed `n>=2`. This is explicitly a deterministic replacement argument. |
| CH06-C07 — semicircle scope and finite spectra | **Correct** | The stated iid finite-variance real symmetric ensemble is a special case of the cited theorem. Nested minors and square-root normalization are explicit; a fourth moment is unnecessary for the empirical-measure limit. The trace-square identity and largest-entry lower bound are separately proved. Neither is asserted to prove an extreme-eigenvalue limit or a covariance-matrix law. |
| CH06-C08 — regression target and consistency | **Correct** | Independence gives covariance `a` and response variance `a^2+tau^2`. The five strong-law averages are integrable; OLS with an intercept gives `R_n^2=r_n^2`. The zero extension on constant-column samples is bounded and eventually irrelevant almost surely, so expectations converge. NaN remains the numerical answer on a degenerate sample. There is no claimed universal bias sign or rate. |
| CH06-C09 — location-mixture moments and central valley | **Correct** | Expansion gives the stated second/fourth moments and Pearson kurtosis; at `m=2,sigma=1`, `K=43/25`. The MGF is finite for every real argument and the origin is a strict density minimum when `m>sigma`. |
| CH06-C09 — absorbing-state conditions | **Correct** | The transition-matrix power includes `p=0` and `p=1`. Starting intact, eventual failure is certain exactly for `p>0` in this homogeneous model. For `p_j=2^(-j-1)`, the product lower bound is at least `1/2`; no independence of unconditional failure events is assumed. |
| CH06-C09 — rare Pareto regime | **Correct** | Every positive mixture weight retains the Pareto survival exponent and the exact positive-order moment gate. The bounded regime cannot cancel a divergent nonnegative moment. The survival `0.0025`, mean `0.55`, and infinite second moment are correct. |

The normalized Student, conditional-law, entropy, geometry, sample-statistic,
regression and appendix calculations have adequate local derivations or
explicit links to their prerequisites. The semicircle limit and retained
tail-class/max-to-sum theorems remain cited, not claimed proved by simulation.

### Fixes and numerical checks

- **Fixed:** NumPy complex scalars and arrays could pass through the real
  parameter conversions with only `ComplexWarning`, discarding their
  imaginary parts. The helper now rejects complex degrees of freedom,
  scatter parameters, log determinants, regression parameters and
  location-mixture parameters before conversion. Nine regression cases
  failed on the incoming helper and pass after the fix.
- **Fixed:** the information-figure caption now specifies `rho=0` in its
  lower panel. Its alt text describes the two plotted joint probabilities;
  the plot does not display their difference as a separate curve.
- The helper formulas, gamma sampler, centered/uncentered coefficients,
  spectrum normalization, regression target and scaled kurtosis agree with
  the notes. The deliberate Student API interval `[0.5,1000]` remains
  separate from the mathematical domain `nu>0`.
- `uv run pytest` with the writable offline uv/Matplotlib caches and one
  BLAS thread: **452 passed in 4.20s**, including **60 chapter-6 cases**.
  The independent entropy integrals, two joint-tail conditioning routes,
  OLS identity, spectral invariants and extreme-scale checks pass.
- Both demos ran successfully through the shared figure style/export.
  The chapter-6 demo was rerun after the helper fix; its printed outputs
  and all nine SVG hashes match the review baseline exactly. The maximum
  joint-tail quadrature error estimate is `9.97e-10`.
- PCG64 seed `20261018`, 400 replications at sizes through 1000, and twelve
  80-by-80 matrices per law are fixed and bounded. The same generator is
  advanced across experiments in a fixed order. No draw or eigenvalue is
  discarded; sampling bands are percentiles, not confidence intervals.

### Figure and caption verdicts

Freshly rendered all nine actual SVGs with librsvg/Cairo at 390px and 900px.
Inspected every 390px preview and the three requested chapter-5 figures
also at 900px. These are artifact checks, not generated-site browser checks.

| Figure | Verdict and checked correspondence |
| --- | --- |
| `multivariate-geometry.svg` | **Correct:** independent/spherical Cauchy and the equal normal mixture with correlations `+/-0.8`; levels are fractions of origin density, not enclosed mass. |
| `multivariate-information.svg` | **Fixed caption; curves correct:** entropy at scatter parameters 0/0.6; lower-panel joint probabilities use `nu=3,rho=0`. |
| `multivariate-spectra.svg` | **Correct:** full eigenvalue ranges, distinct horizontal scales, variance-standardized Student 3, unit-scale Student 1.5, and semicircle overlays only in finite-variance panels. |
| `multivariate-sampling.svg` | **Correct:** centered correlation, fitted intercept-regression R-squared, 10/50/90 sampling percentiles, and population lines only where defined. |
| `multivariate-regimes.svg` | **Correct:** normal location-mixture densities, Pearson kurtosis and the two specified conditional-hazard survival products. |
| `power-law-matching.svg` | **Correct:** central double-Pareto peak visible; distinct Student tail/variance matching; survival-ratio limits 1 and `4/(3*pi)`; multiplier limit `1/8`. Legends agree with their panel's curves. |
| `power-law-diagnostics.svg` | **Correct:** top panel has Pareto, Weibull and normal log-ratios on a signed symlog axis; the linear panel has exponential zero and negative logistic values. The bottom convolution ratios are a separate calculation. |
| `power-law-integrals.svg` | **Correct:** independent Pareto products, exact truncated moments at orders 1/1.5/2, and the Karamata ratio. The moment panel has 240 positive points on log-log axes; only the zero endpoint is omitted. |
| `power-law-entropy.svg` | **Correct:** the unchanged log-coordinate densities and q-survivals match the retained maximum-entropy caption; the compact-support curve reaches zero at 2. |

### Citations, decisions and limits

The chapter-6/appendix-A locator table above matches the supplied PDF,
including the 14-page offset. Rechecked the retained chapter-5 and earlier
Taleb section/page locators on the touched concept pages. The references
identify source context separately from this repository's original proofs.

The theorem-level checks agree with
[Tao, Theorem 1 and §1, Exercise 5](https://terrytao.wordpress.com/2010/02/02/254a-notes-4-the-semi-circular-law/),
[DLMF 5.12.1](https://dlmf.nist.gov/5.12#E1), and the retained Gaussian-tail
input [DLMF 7.12.1](https://dlmf.nist.gov/7.12#E1).
Foss–Korshunov–Zachary (2013, second edition), §3.5, Theorem 3.29 and
following paragraph on p. 57, and Theorem 3.30 and examples on p. 58
support the catalog's cited positive classifications. The second-edition
text was checked through the
[university-hosted PDF](https://www.math.u-szeged.hu/~kevei/tanitas/irodalom/Foss%20Korshunov%20Zachary%20An%20intro%20to%20heavy%20tailed%20and%20subexp%20dist.pdf).
[Kevei–Mason, p. 632, Theorem 1.1 and the iid discussion](https://alea.impa.br/articles/v11/11-30.pdf#page=2)
supports the retained Pareto sum/maximum limit and the reciprocal used here.

**Open source-access limitation:** the unchanged Darling (1952),
Theorem 5.1 pointer was not checked against the original article in this
run: the AMS/DOI endpoints failed and JSTOR did not expose the text.
The accessible Kevei–Mason discussion corroborates the iid result, as in
the previous chapter's review. This is not an open chapter-6 mathematical
claim. **Optional Xiang decision:** retain the existing Darling citation
alongside that accessible account (recommended), or require the original
1952 text before treating its exact theorem number as directly rechecked.
No other mathematical decision is needed.

This review changed `src/math/incerto/multivariate.py`,
`tests/test_incerto_multivariate.py`, the information caption in
`content/incerto-multivariate-tails.md`, and this record. Current review
status is synchronized in `docs/plan/incerto-program/{README.md,concepts.md,
state.yaml,validation.md,verification.md,m0.5-review.md}` and
`docs/plan/index.md`; later-chapter authorization and statuses are unchanged.

No fresh HTML build/check, browser equation/navigation review, live reader
review, wheel build or Lean check was run in this math-review pass.
The recorded MyST sandbox failure and external publication checks remain
separate follow-ups. No files were deleted or staged; no commit or
publication was made.

Final source checks passed: the executable state/human-view validator
(1,035 plan file/fragment links), source audit (724 relative file/fragment
links and 82 content citation-key uses), TOC/title agreement, SVG XML,
`git diff --check`, and separate new-file whitespace/final-newline checks.
The citation-key count checks bibliography membership; factual locator
verification and its Darling limitation are described above. The complete
worktree still has 25 modified tracked files and 11 untracked files, with
no staged changes. This review changed 11 of those existing working files.

## Operator rerun outside the sandbox

On 2026-10-18 the operator reran the checks outside the Codex sandbox after
deleting `_build/`: `uv run pytest` (452 passed, 43 subtests), `npm ci`,
`npm run build` (exit 0, no `doi.org` fetches) and `npm run check:html`
(exit 0; 79 pages across four sites, 64 legacy compatibility pages). This
resolves the sandbox `EPERM` blocker above. The operator also rendered the
three revised chapter-5 figures and the five new chapter-6 figures to PNG at
390 px and 900 px widths and inspected them: legends no longer cover curves,
the diagnostics panel has readable ticks with exponential and logistic in a
separate linear panel, and the integrals panel uses log–log axes without
switch kinks. Post-publication live reader review remains pending until Xiang
approves merge and publish.
