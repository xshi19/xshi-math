# Power-law fitting and goodness-of-fit checkpoint

2026-10-29. Branch `csn/power-law-theory`, base `22483bb` from `origin/main`.
Xiang selected **gpt-6-astra xhigh** for this implementation and a separate
**gpt-6-astra max** run for mathematical review. No delegation, staging,
commit, push, publication, or repository file deletion. The entire
`docs/plan/incerto-program/` tree, including `state.yaml` and `next_chunk`,
is unchanged; this task does not advance the chapter queue.

## Delivered scope

- New theory pages: [fitting](../../content/incerto-power-law-fitting.md) and
  [goodness of fit](../../content/incerto-power-law-goodness-of-fit.md), with
  original derivations, explicit assumptions, synthetic examples, and the
  requested brief future-example admonitions.
- Added [powerlaw.py](../../src/math/incerto/powerlaw.py): continuous/discrete
  MLEs, tie-aware KS, threshold selection, Fisher SE, continuous/exact-zeta
  sampling, empirical joint-SE bootstrap, semiparametric GOF bootstrap,
  conditional alternative fits, and non-nested/nested LR statistics.
  All ten public functions are re-exported and have
  [API entries](../../content/incerto-api-reference.md#api-powerlaw-mle-continuous).
- Reused Pareto sampling, RNG/input helpers, empirical survival, and shared
  figure styling. No dependency or package mapping change. Added
  [72 tests](../../tests/test_incerto_powerlaw.py) and explicit registration
  coverage in the existing exact-output snippet suite.
- Added both pages to the TOC, method index, track reading path, and Hill/
  threshold “See also” lists. Regenerated the graph/list: **41 nodes,
  69 dependency edges, 79 reference edges**. The glossary remains a short
  glossary of three interpretive terms, not a second notation canon.

## Sources and mathematical scope

Read the requested repository guidance/contracts, code-visibility and latest
chapter-7 records, notation canon/lock, source modules, and local mathematical
reference material. Only mathematical context was used from the supplied
external workspace; all experiments here use independent synthetic inputs.
No source passages, figures, tables, or empirical measurements were imported.

CSN's [author preprint, arXiv:0706.1062v2](https://arxiv.org/abs/0706.1062v2)
was consulted at §§3.1–3.4, §4.1, §5, and appendices B/C. The local bibliography
records the 2009 SIAM Review article. The
[Vuong publication record](https://authors.library.caltech.edu/records/0gmss-rn517)
confirms the 1989 Econometrica metadata; its full-PDF download failed, so a
fresh line-by-line audit of the original theorem remains for max review.
The [Self–Liang paper](https://pages.stat.wisc.edu/~larget/Stat998/Fall2015/Self-Liang-1987.pdf)
is the additional cited source for the regular boundary-mixture result,
§3, Case 5. Hill's existing local bibliography entry was reused.
New citations resolve locally; no inline DOI URLs or DOI-fetch syntax was added.

The notes retain **alpha = survival exponent**, with local **a = alpha+1**
for CSN's density/mass convention. Discrete PL fitting and both bootstraps
are implemented; alternative fitters currently supply continuous conditional
densities and reject discrete mode. LR score arrays can represent either
measure, but must share the same observations and measure. Nested cutoff
comparisons return an uncalibrated statistic by default; the caller must
justify any chi-square or boundary-mixture calibration. Numerical fits report
artificial search boundaries and do not claim global optimality.

## Figures and reproducibility

[powerlaw_fitting.py](../../demos/incerto/powerlaw_fitting.py) generates
`powerlaw-fitted-tail.svg` and `powerlaw-ks-threshold.svg` through the shared
figure helpers. PCG64 seed **982**, **6000** observations: uniform body on
[1,4] with probability 0.7, otherwise Pareto minimum 4 and survival exponent
1.8. There are **21** threshold candidates (1 to 6 by 0.25), minimum tail
count 200. Result: **xmin 4.00, alpha 1.725, retained 1815, KS 0.021**.
The empirical survival is strict; the fitted line starts with inclusive
retained mass. No zero survival is replaced by a positive plotting floor.

Both SVGs match two fresh-process exports byte-for-byte. Rendered and visually
inspected all four PNG previews at **390/900 px**, using librsvg/Cairo:
`/tmp/csn-previews`. Mobile dimensions are 390×329 and 390×483. Labels,
legends, dotted population join, KS minimum, and count panel are legible.
Page demonstrations use PCG64 seeds 310, 321/328, 330/331, 340/341, 350,
360, and 370; bootstrap examples use only 24 or 39 replicates. Their stated
precision is illustrative. API bootstrap examples use eight replicates.

## hard_math_claims_for_max_review

| Location | Claim and review scope |
| --- | --- |
| `content/incerto-power-law-fitting.md:35`, `:61` | Survival/density exponent mapping; exact continuous MLE; finite-MLE exception; inclusive count versus Hill's k strict upper observations. |
| `content/incerto-power-law-fitting.md:134`; `src/math/incerto/powerlaw.py:92` | Zeta likelihood, score/concavity, finite root, half-integer approximation and its limits; numerical optimization and integer sampling. |
| `content/incerto-power-law-fitting.md:218`; `src/math/incerto/powerlaw.py:127` | KS supremum at both sides of empirical jumps, integer gaps, grid selection, and retained counts. |
| `content/incerto-power-law-fitting.md:308`; `src/math/incerto/powerlaw.py:190`, `:279` | Continuous and discrete Fisher errors; numerical curvature; full-sample joint bootstrap covariance versus unproved interval coverage. |
| `content/incerto-power-law-goodness-of-fit.md:33`; `src/math/incerto/powerlaw.py:250` | Empirical-body/fitted-tail null mixture, random tail counts, replicate threshold refitting, inclusive bootstrap p, and B≥1/(4 epsilon²) as an MC-SE bound. |
| `content/incerto-power-law-goodness-of-fit.md:139`; `src/math/incerto/powerlaw.py:317`, `:337` | Conditional normalizers; lognormal fit, profiled Weibull scale, unrestricted interior cutoff exponent, and exact Pareto boundary. |
| `content/incerto-power-law-goodness-of-fit.md:245`; `src/math/incerto/powerlaw.py:446` | Vuong normalization, two-sided p, finite positive contrast variance, fitted-model/selected-threshold caveats, and Pareto-versus-exponential moment gates. |
| `content/incerto-power-law-goodness-of-fit.md:375` | Nested LR orientation and factor two; regular half-point-mass/chi-square boundary reference; cutoff score's infinite-information failure for survival alpha≤2. |

## Verification and limits

- `UV_NO_SYNC=1 UV_CACHE_DIR=/tmp/csn-uv MPLCONFIGDIR=/tmp/csn-mpl OPENBLAS_NUM_THREADS=1 uv run pytest`:
  **999 passed in 161.68 seconds**, including all 72 new numerical/figure cases.
  Independent checks include SciPy generators, discrete CDF inversion, finite
  series Fisher information, conditional SciPy log densities, direct cutoff
  quadrature, known-generator LR signs, and invalid-input/failure contracts.
- `scripts/regenerate_incerto_outputs.py` executed **140 snippets and one
  full-demo output**. The first pass changed only the two new pages and API;
  a second pass changed only the new GOF page to print tiny p-values in
  scientific notation. All eight new theory-page snippets and ten API examples
  have executed Output blocks. The final exact-output/registration suite,
  `UV_NO_SYNC=1 uv run pytest -q tests/test_incerto_page_snippets.py`, passed
  **294 tests in 92.32 seconds** with the same cache/thread environment above.
- KaTeX **0.16.25** parses all **25** new display blocks with errors enabled.
  Displays use short rows/aligned breaks with conservative mobile width
  estimates. Full browser measurement remains unverified: Chrome failed with
  `setsockopt: Operation not permitted`.
- Locked `uv sync --locked` failed on package-download DNS. A local available
  dependency copy plus an offline editable installation imports this checkout.
  Python 3.13.5, NumPy 2.4.6, SciPy 1.18.1, Matplotlib 3.11.2, pytest 9.0.3
  were used. Some ancillary packages differ from the lock; this is not a
  locked-install verification. No lockfile was changed.
- Full MyST build was attempted in `/tmp/csn-site-check` using available
  MyST 1.10.1/theme files; preflight reports npm “Package Not Found” despite
  the npm command running. HTML checking consequently reports missing fresh
  artifacts. No HTML, navigation, live-reader, or publication pass is claimed.
- Local links, fragments, citation keys, API anchors, figure targets, TOC
  coverage, Python syntax, graph regeneration, and whitespace were checked.
  `git diff --check` passes; new files were checked separately and reviewed
  in full. No package/wheel build or Lean formalization was run; mapping is
  unchanged and this statistical/numerical scope has no Lean deliverable.

## Math-review corrections (2026-10-29)

The verification above records the original implementation checkpoint. This
follow-up fixes the four reported numerical findings in
[powerlaw.py](../../src/math/incerto/powerlaw.py) and adds regression coverage in
[test_incerto_powerlaw.py](../../tests/test_incerto_powerlaw.py).

- Cutoff fitting chooses initial rate bounds from the sample scale and expands
  artificial bounds over at most eight search rounds. A pure-law maximum is
  certified only when its inward score is negative beyond the roundoff
  tolerance. An infinite or unresolved score cannot certify the boundary;
  failed optimization and an inferior pure-law fallback remain unsuccessful.
  Tests cover failed optimizers, including failures after a bound expansion.
- Cutoff quadrature recenters and rescales the mode, splits the integration
  range around it, and places additional breakpoints on long intervals.
  Evaluating the exponential decay in log coordinates also preserves mass
  beyond the ordinary exponential's overflow point. Independent checks use
  the [incomplete-gamma identity](https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.gammaincc.html),
  direct integration in scaled data coordinates, and the exponential integral.
- Discrete Fisher information uses scaled log moments with an
  [Euler–Maclaurin tail](https://dlmf.nist.gov/25.11.iii). Doubling the finite
  sum checks convergence; roundoff and underflow checks reject unresolved
  variance. Tests compare finite-series information at moderate and steep
  exponents, cover large thresholds, and verify rejection when resolution fails.
- Exponential fitting accepts constant samples strictly above the threshold;
  positive mean excess gives the finite rate estimate. All-threshold samples
  still raise.

The reported wide-range sample now gives an interior fit with density exponent
**0.991142**, rate **1.117994e-9**, and nested LR statistic **575.082212**
(the review's feasible-point lower bound was **214.12386**). For density
exponent **-9** and dimensionless rate **exp(-10)**, the log normalizer is
**112.801873**. The discrete SE at survival exponent **40**, sample size
**100**, and threshold **1** is **213938.731869**. The exponential fit to
`[2, 2]` at threshold **1** has rate **1** and log likelihood **-2**.

Updated the two affected [API entries](../../content/incerto-api-reference.md)
to describe the numerical methods and failure contracts. The regeneration
script executed **140 snippets and one full-demo output**; **zero recorded
outputs changed**. No figure, dependency, package mapping, or public signature
changed.

- `UV_NO_SYNC=1 UV_CACHE_DIR=/tmp/csn-uv MPLCONFIGDIR=/tmp/csn-mpl OPENBLAS_NUM_THREADS=1 uv run pytest`:
  **1028 passed in 149.60 seconds**, including **101 power-law cases**
  (**29 added in this follow-up**) and all page-output comparisons.
- Reviewed the implementation/test changes and updated record in full.
  `git diff --check`, separate whitespace checks for the untracked files,
  Python syntax, and the record's local links pass.
- The SHA-256 of `docs/plan/incerto-program/state.yaml` matches the value at
  the start of this follow-up. Existing worktree changes are retained;
  nothing was staged, committed, or deleted.
- HTML/browser, locked-install, packaging, and Lean checks were not rerun.
  The environment and publication limitations in the original checkpoint
  still apply.

## Open questions and handoff

No owner scope decision is needed. The four supplied math-review findings are
addressed above; the broader claim-review checklist is retained for reference.
Discrete alternative fitting and a dedicated nested-LR
simulation helper are outside this implementation's documented API scope.
A locked-environment rerun, full HTML/mobile browser check, and a reader review
after any later authorized publication remain external verification work.
