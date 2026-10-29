# SCoFT v4 chapter 10 checkpoint

2026-10-29 (America/New_York). Branch `scft/v4-ch10`, base `bd119c8`
from `origin/main`. Xiang selected **gpt-6-astra xhigh** for writing/code
and a separate **gpt-6-astra max** run for subsequent mathematical review.
No delegation, staging, commit, push, publication, or repository file deletion.

Chosen guide title: **Chapter 10 — Diagnosing returns**.
Teaching and bounded Python implementation are complete. The observed S&P
study is **not complete**: the fresh clone contains no authorized cache,
and the documented FRED downloader failed DNS resolution. A separate web
attempt could read the series notes but could not retrieve CSV content.
No simulated series is presented as empirical S&P evidence.

## Contract and sources

Read root/Incerto guidance, shared rules, notation canon/program lock,
program contracts and state, chapter 8/9 and visualization/code-visibility
patterns, the page-snippet tests, and output regeneration script. Used
concept-page, proof-writing, reading-guide, prose-review/unslop,
Git conventions and hub-publish guidance. Lean is **skipped-for-now** at
Xiang's request; no declaration or checked proof is added.

Read the external, read-only `/workspace/scoft-toc/2001.10488v4.pdf`
and its TOC. Also inspected rasterized source pages 200 and 216 to check
the conditional-ratio and angle formulas independently of PDF text extraction.
Consulted chapter 10, printed pp. 193–205; Appendix F,
pp. 207–212; and Appendix G, pp. 213–216. These are source units
`scft-v4-ch10`, `scft-v4-appf`, and `scft-v4-appg`. The guide maps every
§10.2 diagnostic, §10.3, F.1/F.2, and G.0.1 to the concept pages.
No book text, figures, tables, PDF, or TOC was copied into the repository.
The existing local `taleb2025scoftv4` and `fred2026sp500` bibliography
entries suffice; no inline DOI links or new bibliography entries were added.

The new `incerto-sp500.md` is the broader diagnostics home for `c-sp500`.
`incerto-sp500-tail.md` remains the cache-access/Hill/mean-excess home;
its data-source note is preserved. `incerto-ml-econometrics.md` is the
canonical `c-ml-econometrics` page at F/G scope. Appendix I remains
chapter-22 work. Both concepts stay **in-progress** because the observed
pipeline evaluation is uncomputed; the latter also has its later scope.
Chapter/appendix source-unit records likewise remain in-progress. The
chunk is marked done specifically at teaching/Python implementation scope,
and `next_chunk` is `scft-v4-ch11`, as requested. This does not claim that
all empirical, max-review, or publication gates have closed.

## Mathematical scope and hard_math_claims_for_max_review

Line references are to the final public files in this working tree.
The separate max run should review these claims and the numerical domains.

| Claim | File:line | Claim and support |
| --- | --- | --- |
| CH10-C01 | `content/incerto-sp500.md:78` | Iid finite-fourth-moment aggregation gives population excess kurtosis divided by horizon. Original expansion proof; no corresponding assertion about dependent samples. |
| CH10-C02 | `content/incerto-sp500.md:166` | Running-peak fractional drawdown equals the largest decline over ordered peak/trough pairs. Original finite identity; distinct from signed log drawdown. |
| CH10-C03 | `content/incerto-sp500.md:182` | Conditional mean/positive threshold is `1+e(u)/u`, exceeding one; exact Pareto ratio is `alpha/(alpha-1)` for alpha>1 and exponential ratio tends to one. Algebra plus linked exact Pareto calculation. |
| CH10-C04 | `content/incerto-sp500.md:240` | Raw absolute-power MS share tends to zero under iid sampling and a finite positive pth absolute moment. Explicit reduction to the existing finite-mean max-to-sum proof; no converse or finite-sample inference. |
| CH10-C05 | `content/incerto-sp500.md:252` | `x^-1 (1+sin(log x)/4)` is a valid decreasing survival with infinite mean but no regular variation. Original derivative, tail-integral, and multiplier-ratio argument. |
| CH10-C06 | `content/incerto-sp500.md:294` | Strict iid-continuous record counts have mean H_n and variance sum(1/j)(1-1/j). Original insertion-rank proof; ties and dependence excluded from the benchmark. |
| CH10-C07 | `content/incerto-ml-econometrics.md:32` | Raw second-moment averages remain strongly consistent with a finite second moment; their sampling variance is infinite if the fourth moment is infinite. SLLN cited through existing note; variance identity and nonnegative lower bound proved. |
| CH10-C08 | `content/incerto-ml-econometrics.md:77` | A fixed-small-CDF-distance contamination can change the mean without bound. Original bounded-parent mixture calculation; no blanket impossibility claim for bounded estimands. |
| CH10-C09 | `content/incerto-ml-econometrics.md:162` | Finite bounded-basis sums are bounded; every continuous piecewise-linear function with finitely many knots has an affine-plus-hinges representation with slope-jump coefficients. Original bound and telescoping proof. |
| CH10-C10 | `content/incerto-ml-econometrics.md:203` | Slopes are tangents of angles with axis-unit correction; hinge weights are slope differences. Softplus smoothing has uniform error at most log(2)/a, extending to a weighted-sum bound. Original geometric/algebraic arguments. |

Source qualifications: no equivalence between missing moments and regular
variation; no claim that sample fourth-moment instability proves nonexistence;
no conclusion that record-count nonrejection proves independence or MDA;
no unconditional rejection of covariance methods, econometrics or ML.
The conditional-ratio sign/normalization and angle/coefficient statements
are explicitly corrected at their v4 locators. Synthetic figures illustrate
known models; they do not verify any S&P tail exponent.

## Helpers, experiments, and figures

`src/math/incerto/diagnostics.py` adds ten public functions, all linked from
reader-visible calls to stable API anchors:

- `aggregate_returns`, `sample_excess_kurtosis`, `maximum_drawdown`;
- `moment_share_path`, `record_counts`, `conditional_tail_ratio`;
- `aggregation_diagnostics`, `chronological_tail_check`, `sp500_diagnostics`;
- `hinge_payoff`.

The pipeline reuses the existing price loader and log-return method,
`kappa_from_mads`, Hill exponent estimator and mean-excess helper. Powered
MS shares use log accumulation; tests compare ordinary inputs with the
existing max-to-sum path. Aggregation preserves chronological order and
zeros, reports discarded suffixes, and compares disjoint with overlapping
blocks. The full sample and its two chronological halves are reported.
Gain/loss tails have fixed retained-fraction and quantile rules, with
counts and NaNs for insufficient exceedances. The holdout cutoffs use only
training data; no refitting, shuffled split, or iid confidence interval is
silently added. Drawdown is computed on full price paths, not selected loss
days. The code validates positive prices and increasing dates and reports
calendar gaps. At least 44 closes are required for execution, not inference.

`demos/incerto/sp500_diagnostics.py` produces these five original SVGs via
`src/math/incerto/figures.py` and prints the complete report when a local
cache is present. Otherwise it prints an explicit unavailable-data message.

| Figure file (`assets/figures/incerto/`) | Page | Inputs |
| --- | --- | --- |
| `diagnostics-aggregation.svg` | `content/incerto-sp500.md` | PCG64 seed 1010, 128 paths of 4,096 observations for each of normal/t(3), horizons 1/4/16/64; sample medians and 10–90% ranges |
| `diagnostics-moments-records.svg` | `content/incerto-sp500.md` | PCG64 seed 1011, one path of 3,000 observations per law; fourth-power shares and Student record counts |
| `diagnostics-drawdown-ratio.svg` | `content/incerto-sp500.md` | Two orderings of six invented prices; exact Pareto/exponential conditional ratios |
| `pipeline-contamination.svg` | `content/incerto-ml-econometrics.md` | PCG64 seed 1012, 255 fixed normal observations and one replacement loss on a 120-point grid from 2 to 40 |
| `hinge-calibration.svg` | `content/incerto-ml-econometrics.md` | Exact knots 0/2, slopes .5/1.5/-.5, softplus parameters 1/4 |

M05-ISSUE-003 was already resolved; the corrected S&P plotting-position
wording remains. M05-ISSUE-014 is now resolved at source/figure scope:
we retain `1-i/(n+1)`, label it as rank plotting positions, explain ties
and the nonzero maximum, and preserve all data transformations and fits.

| Existing producer | Changed SVGs (`assets/incerto/figures/`) | Page |
| --- | --- | --- |
| `demos/incerto/amazon_bookrank.py` | `amazon-bookrank-1.svg` | `content/incerto-amazon-bookrank.md` |
| `demos/incerto/nyc_dog_name_tail.py` | `nyc-dog-name-tail-{1,2,3}.svg` | `content/incerto-nyc-dog-name-tail.md` |

The Amazon panels now stack. NYC's Hill, GPD shape and counts have separate
stacked panels; no second vertical count axis. All use the existing shared
style/export functions. `INCERTO_FIGURE_DIR` allows test exports outside the
repository. All four legacy outputs receive independent-process byte checks.
CC0 Amazon and NYC Open Data notices and snapshot bytes are unchanged.
No S&P prices, returns, or empirical figures were redistributed.

## Verification

The final available-environment checks passed; blocked installation/site gates remain separate.

- First helper run: **57 passed in 0.55 s**. Includes all 120 rank permutations
  of length five, independent SciPy kurtosis comparisons, brute-force ordered
  drawdown pairs, MS/log-range tests, strict threshold ties, zero/constant
  samples, overflow, exact hinge values/slopes, time-block conventions, both
  tail pipeline branches and no test-set leakage.
- Output regeneration: `scripts/regenerate_incerto_outputs.py --pages ...`
  executed **120 snippets** across the affected teaching/API/example pages,
  plus the NYC full demo. Four pages' Output blocks changed. The first
  combined attempt was interrupted; the two successful separate runs supply
  the final captured outputs. No number was hand-transcribed.
- Full `UV_NO_SYNC=1 UV_CACHE_DIR=/tmp/ch10-uv MPLCONFIGDIR=/tmp/ch10-final-mpl
  OPENBLAS_NUM_THREADS=1 uv run pytest`: **1,396 passed, 1 skipped in
  216.10 s**. The skip is the existing absent-local-CSV layoffs example; its
  synthetic input and recorded-summary checks pass. This includes all **411**
  page-snippet cases (410 passed, one skip), exact stdout/API/dropdown checks,
  and both new S&P cache branches. No test tolerance or expected value was
  weakened. An earlier complete run had 1,395 passes and one font-path test
  failure caused by the shared Matplotlib symlink; the local-copy environment
  correction resolved it in this full rerun.
- Ran the complete demo/report with a synthetic 301-close cache in
  `/tmp/ch10-synthetic-pipeline`. All full/half-window, aggregation, tail,
  record/MS and frozen-holdout fields execute; this verifies code, not an
  empirical financial result.
- Figures: all nine new/changed SVGs rendered through librsvg/Cairo to PNG at
  **390 and 900 px** under `/tmp/ch10-previews`. Inspected every size; repaired
  crowded NYC count ticks and new-figure legend/annotation overlap. Final
  independent-process export selection: **3 passed in 14.58 s**, comparing
  all nine SVGs with two fresh runs and committed asset bytes. The final
  full suite repeats these comparisons successfully.
- Equations: **19 display blocks** across the affected teaching/empirical
  pages parse with KaTeX 0.16.25. Conservative glyph/layout estimates at the
  site's 17 px base size have maximum width **265.8 px**. This is source and
  metric evidence, not a browser measurement of a 390 px page.
- Concept graph regenerated: **46 nodes, 85 dependency edges, 101 reference
  edges**; explicit TOC, indexes, SCoFT overview, API and plan views updated.
- State/human-view validation and **1,181** local file/fragment links passed. Updated
  the validator's scope/counts and its post-M0.5 list, including the existing
  layoffs page omitted by the previous checkpoint. The frozen M0.5 denominator
  remains 24; two new canonical bodies raise current program bodies to 37.
- Reviewed the diff and full contents of all 13 new files. `git diff --check`,
  separate new-file whitespace checks, **1,140** changed/new-file link
  destinations, bibliography keys, API anchors and figure paths passed.
  All dataset snapshots are byte-identical to the starting revision.
  No staged changes or deleted repository files; head remains `bd119c8`.

Environment: Python **3.13.5**, NumPy **2.4.6**, SciPy **1.18.1**,
Matplotlib **3.11.2**, pytest **9.0.3**, NetworkX **3.7**, PyYAML **6.0.3**.
`uv sync --locked --offline` failed on an uncached SciPy wheel. The new
local environment uses available chapter-9 dependency files, with a local
Matplotlib copy to preserve the bundled-font path contract, and a fresh
editable install pointing at **this checkout**. Other dependency directories
are read-only symlinks. The original Matplotlib symlink was renamed and
preserved, not deleted.
Tests use `UV_NO_SYNC=1`, writable `/tmp/ch10-uv` and Matplotlib caches
(`/tmp/ch10-final-mpl` for the final suite), and one BLAS thread. These are available-environment results,
not a fresh locked-install pass. Package mapping was unchanged.

Site checks: `npm ci --offline` failed because MyST 1.10.1 was not cached.
A scratch tree at `/tmp/ch10-site-check` reused the available MyST install;
`npm run build` failed its npm-version preflight before HTML generation.
`npm run check:html` consequently failed for missing output. Node was
24.22.1. Chrome failed at launch with `setsockopt: Operation not permitted`.
No completed site build, browser equation/navigation check, or live reader
review is claimed. No packaging build, Lean, hub transfer or publication ran.

## Decisions and next actions for Xiang

1. Run the separately requested **gpt-6-astra max** review of CH10-C01–C10
   and helper domains; no max review is claimed by this writing run.
2. Supply the authorized S&P cache or run the documented fetch where network
   access and source terms permit. Record provider, dates, retrieval/checksum,
   and cleaning before running the observed report. FRED's ten-year price-index
   window cannot recreate the book's 1987-containing sample. No new source is
   required to use the implemented pipeline.
3. Re-run locked dependency installation, site/HTML/browser checks, and the
   live reader review after publication. The chunk state advances the writing
   queue to chapter 11 while keeping these empirical/review gates visible.

No title, notation, or page-placement decision requires approval to review
this patch. The working tree is intentionally uncommitted.

## Max review

2026-10-29. Separate mathematical review requested by Xiang, using
**gpt-6-astra, max reasoning**. Inspected `git status` and `git diff` on
`scft/v4-ch10`, together with the untracked chapter files. The starting
worktree had 40 changed/untracked files and HEAD `bd119c8`. A byte snapshot
under `/tmp/ch10-max-review/before` distinguishes the review's changes from
the existing chapter work. No delegation, staging, commit, deletion, data
acquisition, or publication was performed.

**Verdict:** CH10-C01–C10 are **correct under their stated assumptions**.
Two numerical helper failures were **wrong** on valid inputs and are fixed
below. The helper review after those fixes is **correct-with-caveat**:
the checked finite-precision domains are not a uniform error guarantee.
No mathematical assertion in either concept page needed revision.

### Claim verdicts and independent evidence

Line numbers below refer to the reviewed working tree; neither concept
page changed during this review. Numerical experiments supplement the
arguments, and do not prove almost-sure convergence or infinite moments.

| Claim and file:line | Verdict | Argument and independent check |
| --- | --- | --- |
| CH10-C01 — `content/incerto-sp500.md:78` | **correct** | Independence and centering leave `h` fourth-moment terms and `6 binom(h,2)` variance-product terms. Dividing by the squared variance gives excess kurtosis divided by `h`. Direct 80-digit Gamma-density quadrature for sums of unit exponentials at `h=1,2,5,10` agrees with `6/h` to within `2.2e-81`. Exact rational Binomial sums at success probability `0.3` also verify negative excess kurtosis. Fresh Monte Carlo checks at `h=1,4,16` agree within two estimated standard errors. No assertion about dependent returns follows. |
| CH10-C02 — `content/incerto-sp500.md:166` | **correct** | For each positive trough price, `1-P_j/P_i` increases with the earlier peak price; maximizing over `i<=j` yields the running-peak expression. Including `i=j` gives zero as an available decline. Exhausted all **5,040** permutations of prices `[8,3,12,5,9,20,15]`, comparing the helper with exact rational ordered-pair maxima; maximum absolute error `1.12e-16`. |
| CH10-C03 — `content/incerto-sp500.md:182` | **correct** | With positive threshold, a nonempty conditioning event, and finite conditional mean, subtraction of the threshold gives `phi=1+e/u>1`. Direct density integrals for Pareto exponents `1.5,2.5,4` at thresholds `1,2,7,100`, plus four unit-exponential thresholds, agree with the stated ratios to within `2.1e-41`. Independent Pareto(3) and exponential sampling also agrees. The loss-tail conditioning event is correctly applied to `-r`; these examples do not characterize all tail classes. |
| CH10-C04 — `content/incerto-sp500.md:240` | **correct** | Apply the linked max-to-sum proof to the nonnegative variables `Y_i=abs(X_i)^p`: the SLLN gives a positive limiting average, and integrability plus Borel–Cantelli gives `max(Y_i)/n -> 0` almost surely. The stated positive finite moment excludes an identically zero denominator. Direct-power simulations with 32 paths per law illustrate the result: median fourth-power shares at `n=1,000/100,000` were `0.042773/0.001270` for normals and `0.053446/0.009339` for Pareto(6). No finite-path diagnostic or monotonicity theorem is implied. |
| CH10-C05 — `content/incerto-sp500.md:252` | **correct** | Complete the survival by setting it to one below 1. Its density on `[1,infinity)` is `[1+(sin(log x)-cos(log x))/4]/x^2`, with numerator at least `1-sqrt(2)/4>0`; quadrature gives total mass one. The survival integral from 1 to `exp(T)` is `T+(1-cos(T))/4`, so the mean diverges. At multiplier `exp(pi)`, the subsequences `log x=2*pi*n+pi/2` and `2*pi*n+3*pi/2` give distinct ratios `0.6*exp(-pi)=0.025928351` and `(5/3)*exp(-pi)=0.072023197`. This directly disproves regular variation. |
| CH10-C06 — `content/incerto-sp500.md:294` | **correct** | The insertion ranks form a bijection with the equally likely permutations, hence independent uniforms; each side's record indicators are independent Bernoulli variables with parameters `1/j`. Enumerated all **40,320** orders at `n=8`: exact mean `761/280`, variance `839971/705600`. Upper/lower covariance is `-372149/705600`, confirming that the two counts are not independent at this length. Fresh normal and Student(3) simulations at `n=64` give means `4.743000` and `4.743167`, versus `H_64=4.743891` (standard errors about `0.0051`). Ties and dependence remain excluded. |
| CH10-C07 — `content/incerto-ml-econometrics.md:32` | **correct** | Apply the SLLN to `X_i^2`; a fourth moment is unnecessary for consistency. With finite second but infinite fourth moment, `A_n^2 >= X_1^4/n^2` forces an infinite second moment of `A_n`, while its mean stays finite, so its variance is infinite. Independent Student(3) quadrature gives second moment 3 and truncated fourth moments `43.070884, 634.991572, 6588.986441` at cutoffs `10,100,1000`. For normal samples of size 16, Monte Carlo gives sampling variance `0.125021` (SE `0.000464`), versus exact `2/16`. This remains a raw-second-moment claim. |
| CH10-C08 — `content/incerto-ml-econometrics.md:77` | **correct** | The mixture-CDF difference is at most epsilon; in fact it equals epsilon between the bounded parent support and the added atom. Linearity gives mean shift `epsilon*(B-E_P[X])`. Independent survival integration with uniform `[0,1]` parent and epsilon `0.001` gives shifts `0.0015, 0.9995, 999.9995` at `B=2,1000,1000000`, with CDF distance fixed at `0.001`. In 200,000 independent size-100 experiments, the no-contamination frequency is `0.904905`, versus `(1-epsilon)^100=0.904792`. |
| CH10-C09 — `content/incerto-ml-econometrics.md:162` | **correct** | The triangle inequality bounds a finite bounded-basis sum. For the continuous piecewise-linear representation, slope jumps telescope on each interval and the anchor fixes the additive constant; the zero-knot case is affine. Independent SciPy quadrature of stepwise derivatives checks **800** evaluations across 40 randomly specified functions, with maximum absolute error `3.56e-15`. A separate sigmoid grid satisfies the sum-of-absolute-weights bound. Neither statement grants arbitrary nonlinear exact representation or global approximation of an unbounded target by a fixed bounded sum. |
| CH10-C10 — `content/incerto-ml-econometrics.md:203` | **correct** | Display slope is `(a_y/a_x)*s`, hence the data slope is `(a_x/a_y)*tan(vartheta)`; weights are successive data-slope differences. The softplus-minus-hinge difference equals `log(1+exp(-a*abs(z)))/a`, which lies between zero and `log(2)/a`, attaining the upper bound at zero. The weighted bound follows by the triangle inequality. An 80-digit grid checks **804** softplus values at `a=0.125,1,4,100`, including zero, and separate scaled-angle and weighted-sum checks pass. |

Reproducibility: numerical work used Python 3.13.5, NumPy 2.4.6,
SciPy 1.18.1, and mpmath 1.4.1 at 80 decimal digits. Fresh PCG64 streams
use `SeedSequence([20261029, claim_number])`; helper grids use number 11.
The exponential aggregation experiment has 400,000 samples per horizon;
the conditional-ratio experiment starts with 600,000 observations per law;
the record experiment has 120,000 paths per law. The normal second-moment
experiment has 200,000 samples of length 16. High-moment Monte Carlo errors
are reported as sampling evidence, not exact error bounds.

The executable audit and its complete results are retained locally as
`/tmp/ch10-max-review/independent_checks.py`, `numerical-results.json`, and
`numerical-results.txt`. The script SHA256 is
`02acb809655d6219f0a66199871a16463cb7ac424d00314b4f57faddabae73fe`.
These scratch files are not repository artifacts. The table preserves the
claim-level evidence and experiment settings in this record.

### Helper failures and minimal fixes

1. **Powered MS shares:** before the fix,
   `moment_share_path([2,2,2], 1e18)` returned `[1,1,1]`, although equal
   nonzero magnitudes require `[1,1/2,1/3]` for every positive power.
   Adding logarithms at a huge common offset erased the log-count term.
   `src/math/incerto/diagnostics.py:80` now keeps the sum divided by the
   running maximum power, rescaling on new maxima. Log ratios use `log1p`
   for close magnitudes. The same calculation preserves leading tiny
   observations, zeros, and tied maxima. The API description at
   `content/incerto-api-reference.md:3007` matches that calculation and its
   overflow contract.
2. **Hinge cancellation:** before the fix,
   `hinge_payoff(1e16, [0,1], [0,1,0])` returned zero, although the capped
   payoff is exactly one for every input at least one. Subtracting large
   hinge terms lost the constant right tail.
   `src/math/incerto/diagnostics.py:255` now evaluates the active linear
   segment from its knot value and slope. It preserves the existing
   anchoring, shape, extrapolation, and validation conventions.

Regression cases are in `tests/test_incerto_diagnostics.py:73` and `:161`.
All five newly selected cases failed against the starting implementation;
the complete helper file then passed **62 tests** after the fixes. No
existing tolerance or expected output was weakened.

All ten public helpers were checked against definitions independently:
direct block sums and SciPy sample kurtosis; exact ordered-pair drawdowns;
128 mpmath powered-share cases; prefix records; strict conditional means;
direct MAD/kappa formulas; sorted empirical quantiles and mpmath Gaussian
quantiles for the frozen holdout; a separate 77-close synthetic pipeline
with dated halves, zero returns, gain/loss Hill ranks and thresholds; and
derivative quadrature plus high-precision hinge values. Across 50 random
helper trials, maximum absolute discrepancies were `3.56e-15` for block
sums and conditional ratios, `2.67e-15` for sample kurtosis, `3.00e-15` for
the mpmath powered-share grid, and `4.45e-16` for holdout cutoffs. The
[SciPy kurtosis contract](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.kurtosis.html)
also confirms the Fisher, divisor-`n`, no-bias-correction convention used here.

Finite arithmetic still has rounding, underflow and explicit overflow
limits; the API already states that it has no uniform floating-point
error guarantee. The pipeline's disjoint/overlapping blocks, daily MAD
baseline, strict exceedances, positive-side tail quantiles, and shared
boundary close between chronological halves match the page definitions.
No return belongs to both holdout periods. Nothing in these checks
establishes empirical S&P calibration.

### Source comparison

Read the local v4 PDF, printed pp. 193–205 and 207–216; rasterized and
visually checked printed pp. 200 and 216. The source's conditional-ratio
sign, normalization and loss-tail event errors, and its angle/coefficient
error, are present in the PDF. The notes' corrections are mathematically
justified. The [versioned arXiv record](https://arxiv.org/abs/2001.10488v4)
confirms the third revised edition and version used.

**No copied book prose was found** in the two concept pages, chapter guide,
or the new diagnostics API section. Manual comparison was supplemented by
a case-normalized eight-word-sequence search against the full extracted
PDF: **zero matches**, including page captions and code. Standard formulas
and source locators are distinguished from prose copying. The figures
remain the original synthetic/model constructions, and no book text,
image, table, or PDF was added to the repository. Extraction and source
rasters stayed in `/tmp`. The read-only PDF SHA256 was unchanged:
`758e18b7337840104db93296144d67cf5514bf2de128fe557dc84bc32a0ad567`.

### Regeneration and remaining decisions

Ran the chapter demo successfully: all five synthetic/model figures were
regenerated and are **byte-identical** to the starting assets. The demo
again reported the absent local S&P cache. Ran
`scripts/regenerate_incerto_outputs.py --pages incerto-sp500 incerto-ml-econometrics incerto-scoft-ch10 incerto-api-reference`:
**116 snippets executed, zero Output-block changes**.

Final affected-test command, using `UV_NO_SYNC=1`, writable
`UV_CACHE_DIR=/tmp/ch10-max-uv`, `MPLCONFIGDIR=/tmp/ch10-max-mpl`, and
`OPENBLAS_NUM_THREADS=1`:

```sh
uv run pytest -q tests/test_incerto_diagnostics.py tests/test_incerto_diagnostic_figures.py tests/test_incerto_page_snippets.py -k 'diagnostic or incerto-sp500 or incerto-ml-econometrics or incerto-scoft-ch10 or incerto-api-reference or chapter10 or output_blocks or long_code_blocks'
```

**303 passed, 173 deselected in 89.57 s.** This covers the helper tests,
affected page/API examples and output contracts, the synthetic-cache
financial branch, and independent-process figure-byte comparisons. These
are available-environment results; the full repository suite and fresh
locked installation were not rerun. The independent audit script also
completed with every assertion passing.

No unresolved judgment call affects CH10-C01–C10. Xiang still owns the
observed-data source/window and the choice of a prespecified empirical
experiment, including aggregation horizons, tail fractions and holdout
probability. The review validates the documented choices' implementation,
not their statistical optimality. The observed S&P results remain
**unverifiable here** because no authorized cache is present. The prior
locked-install, site/HTML/browser and publication gates remain separate;
none was rerun or declared complete in this mathematical review.
This closes the separate max-review action above, while leaving those
empirical and publication actions open.

The review changed only `src/math/incerto/diagnostics.py`,
`tests/test_incerto_diagnostics.py`, `content/incerto-api-reference.md`, and
this record. All other pre-existing changes, including generated assets,
were preserved byte-for-byte. Final diff, separate untracked-file
whitespace, and local-link checks passed. HEAD remains `bd119c8` on
`scft/v4-ch10`, with no staged changes, commits, or deleted files.
