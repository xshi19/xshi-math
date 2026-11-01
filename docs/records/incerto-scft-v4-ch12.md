# SCoFT v4 chapter 12 checkpoint

2026-11-01 (America/New_York). Branch `scft/v4-ch12`, base `316f98c`
from `origin/main`. Xiang selected **gpt-6-astra xhigh** for writing/code
and a separate **gpt-6-astra max** run for subsequent mathematical review.
No delegation, staging, commit, push, publication, or repository file deletion.

Chosen title: **Chapter 12 — Point forecasts and tail risk**.
Teaching, scoped source reconciliation and Python implementation are done.
Separate max review, fresh HTML/browser checks and post-publication reader
review remain distinct gates. The next writing chunk is `scft-v4-ch13`.

## Contract, sources and boundaries

Read the root and Incerto guidance, all shared rules, notation canon and
program lock, relevant concept/proof/reading-guide/prose/Git skills, program
contracts, state, M0.5 and visualization reviews, chapter-8/9 records,
visualization P2 and code-visibility patterns, snippet tests and output
regenerator. Applied hub-publish checks only to a scratch local build.

Read the supplied read-only `/workspace/scoft-toc/2001.10488v4.pdf`
and `v4-toc.txt`. Chapter 12 occupies printed **241–246**, PDF **255–260**.
The guide maps §12.1 p. 241, §12.2 pp. 241–243, §12.3 pp. 243–245,
and §12.4 pp. 245–246. Source extracts remain under `/tmp`.
No source text, closely paraphrased prose, table, figure or PDF is included.
A case-normalized 12-word overlap scan against the chapter found zero matches
in the concept page and guide; prose was also compared for close paraphrase.

The existing `taleb2025scoftv4` bibliography entry supplies chapter context.
Two versioned primary sources were added to `content/bibliography.bib`:

- Taleb, Bar-Yam and Cirillo, arXiv:2007.16096v1: attached
  `paper-point-forecast` mathematical scope, pp. 1–5 and the conditional
  information/action discussion on p. 7. Broader clinical and policy
  coverage remains excluded under the existing paper contract.
- Cirillo and Taleb, arXiv:2004.08658v1, §§II–IV pp. 2–6: background
  historical epidemic study; the bounded dual transform is in §II p. 4.
  Its data compilation is identified in the concept page's data-source
  note. No table was acquired, redistributed or refitted. This supporting
  citation creates no new program paper or empirical-study obligation.

The stable-attraction statement retains the existing verified Durrett
Theorem 3.8.2, p. 186 reference through the canonical limit-law page.
It is cited, not proved by the new simulations. Exact stable closure and
the elementary loss/transform calculations have original arguments.
All numerical cases are synthetic. No medical effectiveness, outbreak
forecast, historical tail fit or causal country comparison is inferred.

## Teaching and integration

- New [chapter guide](../../content/incerto-scoft-ch12.md): section/page
  map, exact scale equation and runnable example, source qualifications,
  figure and prerequisite links.
- Extended [point-forecast page](../../content/incerto-point-forecast.md):
  estimation versus prediction, exact stable scaling and cited Pareto
  attraction, positive infinite-mean boundaries, score moments and paired
  comparisons, quantile targets, survival-integral severity, finite caps,
  two distinct logarithms, bounded dual transforms, synthetic growth and
  an explicit precaution decision model.
- Extended [API reference](../../content/incerto-api-reference.md): five
  helpers, argument domains, executable finite/NaN/infinite/overflow and
  endpoint examples with generated output.
- Wired the MyST TOC, method and empirical-example indexes, Incerto hub,
  SCoFT overview, generated concept graph and program human views.
  Graph: **48 nodes, 89 dependency edges, 116 reference edges**.

`state.yaml` marks chapter 12, its attached selected mathematical paper
scope and `c-point-forecast` done at their recorded implementation scope.
The checkpoint separately records pending max review and site/live gates.
Calibration retains its chapter-13 scope. Current program bodies remain
**39**, total concepts **103**, active concepts **75**, and the frozen
M0.5 review inventory **24**. Existing M0.5 issue counts are unchanged;
006/007 remain open/deferred at their wider source-audit scope.

The canonical page already owns the pandemic-related forecast questions,
so no separate pandemic concept page was added. The zero-lower-endpoint
transform supplies bounded-variable context here; chapter-17 shadow-mean
fitting and chapter-18 historical estimation remain future work. Lean is
**skipped-for-now** as requested: the optional imported prototype supplies
no checked probability/scoring development for these claims.

## hard_math_claims_for_max_review

Line references identify the final public statements in this working tree.
Review their assumptions, proofs, source qualifications and numerical domains.

| Claim | File:line | Claim and support |
| --- | --- | --- |
| CH12-C01 | `content/incerto-point-forecast.md:268` | Mean estimation differs from predicting an independent future observation: Slutsky limit for integrable laws and variance sigma²(1+1/n) versus sigma²/n. Exact variance algebra; standard convergence argument. |
| CH12-C02 | `content/incerto-point-forecast.md:287`; `src/math/incerto/forecasting.py:29` | Symmetric stable average scale sigma n^(1/alpha−1), location versus mean, and quantile-width consequences for alpha below/at/above one. Original characteristic-function proof; finite arithmetic domain separately tested. |
| CH12-C03 | `content/incerto-point-forecast.md:342` | Exact positive Pareto stable-attraction scaling, zero centering below one, almost-sure divergence at alpha≤1, logarithmic alpha=1 boundary and alpha=2 normalization caveat. General attraction cited; bounded-truncation proof and existing boundary derivation linked; no uniform finite-sample rate. |
| CH12-C04 | `content/incerto-point-forecast.md:394` | Absolute/squared score mean and variance thresholds, strong-law divergence of infinite-mean nonnegative scores, and insufficient second moment of the amount for a squared-score CLT. Moment comparison and local truncation argument. |
| CH12-C05 | `content/incerto-point-forecast.md:416` | Paired absolute differences are bounded; paired squared differences are affine in X and may be integrable when both risks are infinite. Original cancellation; iid scope and degenerate variance stated. |
| CH12-C06 | `content/incerto-point-forecast.md:496`; `src/math/incerto/forecasting.py:51` | Quantile-loss integral identity, quantile minimizers for finite risk, bounded paired differences without a first moment, and exact Pareto quantiles. Original slope integration; density-quadrature checks including alpha<1. |
| CH12-C07 | `content/incerto-point-forecast.md:553` | Survival integral identifies expected excess; a fixed empirical survival fraction has MSE p(1−p)/n and relative RMSE sqrt((1−p)/(np)), not universal o(1/n) error. Tonelli/binomial arguments and canonical links. |
| CH12-C08 | `content/incerto-point-forecast.md:570`; `src/math/incerto/forecasting.py:73` | Fixed cap yields finite positive moments; capped Pareto mean and endpoint atom; dual/log transformations, inverse, local expansion, quantile transport and finite physical mean under an infinite-mean dual law. Original integration/inversion; high-precision and endpoint tests. |
| CH12-C09 | `content/incerto-point-forecast.md:695` | Exponential uncertainty in a growth rate yields a Pareto amount of exponent lambda/t; normal rate yields lognormal; Jensen requires the specified integrability/order and saturation changes convexity. Original change of variables and scoped convexity argument. |
| CH12-C10 | `content/incerto-point-forecast.md:717` | Capped excess is a difference of caps; action is preferred precisely when c<r E[J] under specified cost/effectiveness, with a sufficient worst-model condition. Conditional intervention forecasts require a separate causal comparison. Exact loss subtraction, synthetic examples; no empirical effectiveness claim. |

### Source qualifications

- **§12.1 p. 241 and §12.2 pp. 241–243:** point summaries are legitimate
  under a specified target/loss; one point does not identify the predictive
  distribution or tail payoff. Expected-loss integrability and paired
  comparisons prevent a blanket impossibility theorem.
- **§12.2 p. 242; §12.3 p. 243:** an empirical exponent below one is
  not an infinite physical mean under a fixed population cap. Exact Pareto
  boundary claims need their exact-law assumption; slowly varying factors
  can change regular-variation boundary moments. No universal threshold at
  alpha=2.5 or universal practical sample size is asserted.
- **§12.3 pp. 243–244:** distinguish LLN consistency, stable distributional
  scaling, mean absolute error and a future outcome's dispersion. Fixed
  threshold indicators have MSE of order 1/n and RMSE of order 1/sqrt(n),
  with rare-event relative error; one probability does not determine severity.
- **§12.3 pp. 244–245:** multiplication, nonlinearity and chaotic dynamics
  are different properties. A power law needs assumptions; information or
  interventions can change the tail model. Variance alone does not order
  expected convex harm over arbitrary distributions.
- **§§12.3–12.4 pp. 245–246:** an action regime belongs in the forecast.
  An observed intervention outcome neither directly evaluates an untreated
  forecast nor proves causation. The abstract precaution example states
  costs, units, effectiveness, cap and threshold; no source policy verdict
  or clinical claim is reproduced.

## Helpers and figures

[forecasting.py](../../src/math/incerto/forecasting.py) adds five public helpers.
All reader-visible names have API links, all displayed outputs are executed,
and long blocks use MyST dropdowns.

| Helper | Page and role |
| --- | --- |
| `stable_average_scale` | Point-forecast scaling, chapter guide and API: exact stable CF scale, finite arithmetic domain |
| `quantile_loss` | Point-forecast quantiles and API: asymmetric finite-input loss and overflow |
| `bounded_to_dual`, `dual_to_bounded` | Point-forecast bounds and API: endpoint map/inverse, NaN rejection and rounding limits |
| `pareto_forecast_scores` | Point-forecast evaluation and API: repeated same-draw mean/absolute/squared/sMAPE summaries |

The simulation reuses `calibration.point_forecast_loss`; its budget is at
most one million observations per replication and 50 million total draws,
in batches of 32 rows. Nonfinite observations or scores raise; none are
filtered. Existing stable absolute-error/kappa, Pareto distribution,
cap-expectation and payoff helpers supply the other calculations. No new
runtime dependency was added.

[demos/incerto/point_forecasts.py](../../demos/incerto/point_forecasts.py)
uses `src/math/incerto/figures.py` for style, vertical panels and deterministic
SVG export. All three figures appear on the point-forecast page and are
linked from the guide.

| SVG under `assets/figures/incerto/` | Exact versus numerical content |
| --- | --- |
| `point-forecast-scaling.svg` | Exact symmetric stable scales; simulated Pareto alpha=1.5 mean errors, 2,000 replications at n=30/100/300/1000/3000, PCG64 seeds 1200–1204 |
| `point-forecast-evaluation.svg` | Same sample-size grid, 2,000 replications, seeds 1210+n; estimated score quantiles, exact absolute-risk reference |
| `point-forecast-bounds.svg` | Exact endpoint map and capped excess curves, same median 2, alpha=.6/.8/1.2, threshold 10, caps 20–100000; no fitted data |

The producer uses **17,720,000** Pareto draws. Quantile bands describe
sampling variation, not confidence intervals or tests of attraction.
All six PNG previews at **390/900 px** were inspected under
`/tmp/ch12-previews`. Replaced an unavailable fraction glyph with mathtext;
regenerated and inspected the corrected labels at both sizes. Vertical
panels, log-axis labels, reference curves and legends are legible.

## Verification

- `UV_NO_SYNC=1 uv run pytest`: **1,645 passed, 1 skipped in 447.24 s**.
  The skip is the existing local-data layoffs example. This includes all
  exact page-output/API-link tests, the 58 new numerical cases, the new
  two-process SVG comparison, graph and package-import checks. The focused
  helper run also passed all 58 cases before the full suite.
- Regenerated **132 executed snippet outputs** with
  `scripts/regenerate_incerto_outputs.py --pages incerto-point-forecast
  incerto-scoft-ch12 incerto-api-reference`. The script and snippet-test
  contract are unchanged. Existing API outputs did not drift.
- Regenerated the graph with `uv run python scripts/build_concept_graph.py`.
  The executable state/human-view validator and **1,195** plan file/fragment
  links pass. Only the intended chapter, attached paper and concept records
  changed semantically; older checkpoints and M0.5 dispositions remain intact.
- Checked **530** local links across changed public pages and this record,
  bibliography keys, TOC membership, whitespace in tracked and new files,
  control characters, and `git diff --check`. Reviewed full new files,
  generated images and the final diff; no deleted or staged paths.
- All **25** display blocks on the affected concept/guide/API pages parse
  with cached KaTeX **0.19.1**. A virtual-tree font-metric estimate at 17 px
  gives a maximum of **248.81 px**. This is a layout screen, not actual
  browser-width certification. All three SVGs have inspected 390/900 px PNGs.
- Offline `npm ci` **passed** in `/tmp/ch12-site-verified` after copying
  the cached MyST 1.10.1 archive from the read-only system cache to a
  writable scratch cache. The earlier empty-cache attempt failed.
  `npm run build` then **failed** in MyST's npm version preflight
  (`npm: Package Not Found`), despite the working outer npm command.
  `npm run check:html` **failed** because fresh HTML/config/redirect
  artifacts do not exist. No fresh site build or HTML pass is claimed.
- Chromium/Playwright launch **failed** with sandbox socket setup
  `Operation not permitted`. Actual page equation widths, desktop/mobile
  navigation and live reader checks remain unverified.

Available test environment: Python **3.13.5**, NumPy **2.5.4**, SciPy
**1.18.1**, Matplotlib **3.11.2**, pytest **9.2.0**, NetworkX **3.7** and
PyYAML **6.0.3**. `uv sync --locked --offline` failed on an uncached SciPy
wheel; the lock selects different NumPy/pytest versions. Tests used an
ignored local environment with available system packages and an editable
install of this workspace. `UV_NO_SYNC=1`, writable `/tmp` UV/Matplotlib
caches and one OpenBLAS thread preserved that environment for the test run.
This is an available-dependency pass, not a locked installation result.

Packaging, Lean, publication, hub transfer and live reader review were not
run. There is no new checked Lean claim. No commit or file deletion occurred.
No additional owner decision is needed to finish this chunk. The separate
max run should review CH12-C01–C10 and helper numerical boundaries; an
operator environment must complete fresh site/browser checks before any
publication and then record the live reader review.

## Max review

2026-11-01 (America/New_York). Xiang's requested **gpt-6-astra, max
reasoning** review of the existing dirty `scft/v4-ch12` tree. This section
completes the mathematical review gate left pending above. The site/browser
and publication gates are separate. Read `git status`, the chapter diff,
this checkpoint, both complete public pages, the helpers, producer and tests.

**Verdict:** eight of CH12-C01–C10 are **correct**, two are
**correct-with-caveat**; no public equation required a mathematical correction.
Two arithmetic defects affected three helper functions and were fixed below.
The caveats concern scope and normalization, not counterexamples to the
page's scoped results. Numerical evidence supplements the arguments; it
does not prove almost-sure divergence, attraction or moment nonexistence.

### Claim verdicts and evidence

Page line numbers are unchanged by this review.

| Claim | File:line | Verdict | Evidence and scope |
| --- | --- | --- | --- |
| CH12-C01 | `content/incerto-point-forecast.md:268` | correct | The iid strong law and Slutsky give the future-error limit. Independence gives variances $\sigma^2/n$ and $\sigma^2(1+1/n)$. Fresh Normal sampling at $n=25$, $\sigma=2$ gave 0.159953 and 4.149002 versus exact 0.16 and 4.16 (100,000 replications). The future observation has the same parent law as the training observations. |
| CH12-C02 | `content/incerto-point-forecast.md:287` | correct | Multiplying the stated characteristic functions gives $s_n=\sigma n^{1/\alpha-1}$ exactly. Positive scale transport gives every fixed interquantile width. Fresh SciPy stable samples at $\alpha=.8,1,1.5,2$, $n=17$, $\sigma=1.7$ gave empirical/exact 10th–90th width ratios 1.00435, 1.01022, 0.99440, 0.99367 (30,000 replications each). At two, the parent variance is $2\sigma^2$. |
| CH12-C03 | `content/incerto-point-forecast.md:342` | correct-with-caveat | For exact Pareto, $a_n=x_m n^{1/\alpha}$ has $nP(X>a_n)=1$. Full-mean centering for $1<\alpha<2$ and zero centering below one give the claimed limits. $Z_\alpha^+$ is the limit under this tail normalization, not a unit-CF-scale stable variable. General two-sided regular variation also needs the tail-balance assumption in the linked theorem. The bounded-truncation argument proves almost-sure infinite-mean divergence; the linked $\alpha=1$ proof gives the separate $\log n$ normalization. At $\alpha=2$, $(S_n-2nx_m)/(x_m\sqrt{n\log n})\Rightarrow N(0,1)$. Independent finite-$n$ transforms and simulations agree; details below. |
| CH12-C04 | `content/incerto-point-forecast.md:394` | correct | A fixed shift leaves the large-$X$ power unchanged. The relevant moments are orders 1 and 2 for absolute-score mean/variance, and orders 2 and 4 for squared-score mean/variance. Integration of $|x-2|^k\alpha x^{-\alpha-1}$, for $k=1,2,4$ and $\alpha=k-.4,k,k+.4$, confirms power growth, logarithmic boundary growth and convergence respectively. For cutoffs $10^4$ and $10^8$, boundary increments divided by $k\log(10^4)$ were 0.999978, 0.999957, 0.999913. Bounded sMAPE and the iid truncation/strong-law arguments have the stated scope. |
| CH12-C05 | `content/incerto-point-forecast.md:416` | correct-with-caveat | The absolute paired difference is bounded by $|d_1-d_2|$; the squared difference is affine in $X$. For $d_1=2,d_2=7,x_m=1$, density quadrature gives an absolute-pair expectation of −1.729252 at $\alpha=.8$ despite infinite individual risks, and a squared-pair expectation of −15 at $\alpha=1.5$ despite infinite individual MSEs. Consistency of a **strict** ranking requires a nonzero expected difference; at a tie the strong law supplies no strict ordering. The page says such rankings are possible, so no correction is needed. |
| CH12-C06 | `content/incerto-point-forecast.md:496` | correct | Integrating bounded slopes gives the CDF integral, including atoms and nonunique quantiles. Its paired form needs no first moment; the sharper bound is $\max(\tau,1-\tau)|d_2-d_1|$, so the displayed bound is valid. At $\alpha=.8$, $d_1=2,d_2=7$, $\tau=.8$, independent density/CDF quadratures both give −0.635374033, within $2\times10^{-15}$. Discrete-law checks cover an atom minimizer and an interval of minimizers. The Pareto quantile follows by direct inversion. The helper's tiny-input error is separate and fixed below. |
| CH12-C07 | `content/incerto-point-forecast.md:553` | correct | Tonelli applies to the nonnegative excess even when its expectation is infinite. For Pareto $\alpha=1.7,x_m=1,u=3$, independent payoff-density and survival quadratures give 0.662090081103, differing by $2.1\times10^{-13}$. At a fixed threshold under iid sampling the fraction is unbiased, hence MSE equals $p(1-p)/n$. Fresh binomial simulation with $p=.01,n=500$ gave MSE 0.00001990454 versus exact 0.0000198; relative RMSE 0.446145 versus 0.444972 (200,000 replications). The stated orders exclude $p=0,1$. |
| CH12-C08 | `content/incerto-point-forecast.md:570` | correct | $0\le X\le H<\infty$ bounds every positive moment. Density integration plus the cap atom reproduces the capped mean, including $\alpha=1$ and $1\pm10^{-9}$, within $1.34\times10^{-15}$ relative error on the checked grid. Inversion, Taylor expansion and continuous monotone quantile transport hold; an endpoint atom maps to infinity. For dual Pareto $\alpha=.8,x_m=1,H=100$, quadrature gives physical mean 7.535005312479 although the dual mean is infinite. The endpoint helpers had a subnormal-ratio defect, fixed below. |
| CH12-C09 | `content/incerto-point-forecast.md:695` | correct | Inverting $x_0e^{tR}$ gives the Pareto survival with exponent $\lambda/t$ for exponential $R$; normal $R$ gives a lognormal law. Fresh exponential-rate draws with $\lambda=2,t=1.5,x_0=3$ match survival at $x/x_0=2,10,100$ within 1.50 binomial standard errors (300,000 draws). Jensen and convex-order qualifications are correct. Equal-mean discrete counterexamples below verify why variance alone and a saturation cap do not suffice. |
| CH12-C10 | `content/incerto-point-forecast.md:717` | correct | The difference-of-caps identity holds pointwise. Loss subtraction gives strict preference exactly when $c<r\mathbb E J$; equality is indifference. Direct survival integration gives harms 70.668069360025, 20.565365275347, 2.713616216875 at $\alpha=.6,.8,1.2$, with the stated common median/cap/threshold. Benefits at $r=.5$ reproduce the three decisions for $c=5$. The infimum criterion is sufficient, as stated. An intervention-conditioned predictive distribution does not identify the missing counterfactual; the page makes no causal-effect claim. |

The guide's equation at `content/incerto-scoft-ch12.md:38` and the
qualifications at `content/incerto-scoft-ch12.md:82` are **correct**.
The tenfold-sample ratios are $10^{1/\alpha-1}$; all four displayed
values agree with independent high-precision arithmetic and regeneration.

### Independent calculations and source checks

Fresh checks used Python 3.13.5, NumPy 2.5.4, SciPy 1.18.1 and mpmath
1.4.1 at **100 decimal digits**. Reference calculations used density
quadrature, inverse-uniform Pareto samples and SciPy's stable generator;
they did not call repository loss/scaling helpers to manufacture their
expected values. Integer seeds were PCG64 61201, 61202, 61203, 61205,
61207, 61209 and 61210. Scratch code and results are retained at
`/tmp/ch12-max-review/independent_checks.py`, `results.json` and `checks.log`.
No dependency or lockfile was changed.

- Stable-scale arithmetic: 105 combinations of seven indices, five sample
  sizes through $2^{53}$ and scales $10^{-200},1,10^{200}$; 97 finite
  answers agreed with mpmath within $8.24\times10^{-14}$ relative error,
  and all eight range failures were justified.
- Pareto boundaries: for $x_m=1$, integrate the density to get
  $\mathbb E e^{-qX}=\alpha q^\alpha\Gamma(-\alpha,q)$, using complex
  $q$ for characteristic functions. The tail-normalized limit at
  $1<\alpha<2$ has characteristic function
  $\exp\{-\Gamma(1-\alpha)(-it)^\alpha\}$; below one its Laplace
  transform is $\exp\{-\Gamma(1-\alpha)s^\alpha\}$.
  At transform argument 0.4 and $n=100,10^4,10^6$, exact finite-$n$
  errors decreased from 0.026184 to 0.000519 at $\alpha=.7$, from
  0.101269 to 0.005076 at $\alpha=1.5$, and from 0.049979 to
  0.020672 under the $\sqrt{n\log n}$ Gaussian normalization at two.
  Fresh inverse-uniform simulations used 3,000 replications at each of
  $n=100,10^4$ for $\alpha=.7,1,1.5,2$. At one, the median of
  $\bar X_n/\log n$ moved from 1.387527 to 1.192006; the probability
  of an error exceeding 0.5 fell from 0.427333 to 0.268333. These
  finite-sample results also show why an asymptotic rate is not a coverage
  guarantee.
- Convexity: take $R_A=5$ with probability .01 and $-5/99$ otherwise;
  take $R_B=\pm1$ with equal probabilities. Both have mean zero,
  but variance increases from 0.252525 to 1 while $\mathbb E e^R$
  decreases from 2.425373 to 1.543081. For the cap
  $g(r)=\min(e^r,e)$, the mean-preserving spread from $R=1$ to
  equally likely 0/2 lowers $\mathbb E g(R)$ from 2.718282 to 1.859141.
- Source reconciliation: read supplied PDF pages 255–260 (printed
  241–246) and compared them with both notes. Rechecked the tail-balance
  condition and truncated centering in
  [Durrett, Theorem 3.8.2, printed p. 186](https://sites.math.duke.edu/~rtd/PTE/PTE5_011119.pdf).
  The linked limit-law note already accounts for the full-mean centering
  shift $\alpha/(\alpha-1)$. Rechecked the
  [SciPy stable CF convention](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.levy_stable.html),
  the zero-lower-endpoint specialization of
  [Cirillo–Taleb equation (1), p. 4](https://arxiv.org/pdf/2004.08658v1),
  and the attached paper's [conditional-action discussion](https://arxiv.org/pdf/2007.16096v1).
- Copy review: manual comparison found original exposition and derivations,
  with attribution and explicit qualifications to the source. Unicode/case
  normalization and PDF line-break dehyphenation found **zero matching
  8-, 10- or 12-word sequences**, both against chapter 12 and against the
  **full v4 book**, in the concept page, guide, forecasting helper and
  figure producer. No copied book prose or figures was found. Extracts and
  overlap results remain under `/tmp/ch12-max-review`; the PDF was read-only.

### Helper verdicts and minimal fixes

| Helper, current File:line | Verdict | Evidence / correction |
| --- | --- | --- |
| `src/math/incerto/forecasting.py:29`, `stable_average_scale` | correct | Matches the page's CF scale; the 105 high-precision cases include finite values, overflow and exact $n=1$/$\alpha=1$ preservation. |
| `src/math/incerto/forecasting.py:51`, `quantile_loss` | wrong at a representable subnormal loss; corrected | Let $\varepsilon$ be the smallest positive binary64 number. At actual $\varepsilon$, forecast $-\varepsilon$, $\tau=.5$, the exact representable loss is $\varepsilon$; pre-scaling both inputs returned zero. Lines 66–68 now subtract first when the residual is finite, retaining the scaled-input fallback for overflowing residuals. Large finite losses and overflow behavior still pass. |
| `src/math/incerto/forecasting.py:74`, `bounded_to_dual` | wrong for nonzero subnormal ratios; corrected | With $H=10^{308}$, $x=4\times10^{-16}$, it returned $4.9406564584124655\times10^{-16}$, a **23.5164%** relative error. The 100-digit result rounds to $4\times10^{-16}$. Line 93 now uses the leading term for every subnormal ratio, not only a ratio rounded to zero. The correction to that leading term is below binary64 resolution. |
| `src/math/incerto/forecasting.py:101`, `dual_to_bounded` | wrong for nonzero subnormal ratios; corrected | The same input coordinate and cap produced the same 23.5164% error. Line 115 applies the same subnormal-ratio criterion. Both endpoints and the documented loss of inverse information near $H$ retain their stated behavior. |
| `src/math/incerto/forecasting.py:119`, `pareto_forecast_scores` | correct | Uses one fixed forecast and the same draws per score within each iid replication. New seed 61210, $\alpha=6,n=120,d=2$, 2,500 replications: all four Monte Carlo averages are within 1.46 standard errors of independent density quadrature. Existing tests check shape, scale transport, budget and overflow rejection. |

Added regressions at `tests/test_incerto_forecasting.py:72` and
`tests/test_incerto_forecasting.py:123`: one pinball case in both directions
and two parameterized transform cases, each covering four nonzero
subnormal ratios. These directly reproduce the defects; no mathematical
prose, guide equation or model choice was rewritten.

### Decisions for Xiang

No decision blocks the corrections or the scoped mathematical verdict.
Two optional exposition changes are left to Xiang:

1. Spell out the characteristic function of $Z_\alpha^+$ beside the
   Pareto limit. Its tail normalization is already fixed by the denominator
   and linked theorem, but an explicit convention would prevent confusing
   it with the preceding unit-scale symmetric law.
2. Add a sentence that a consistent strict paired ranking needs a nonzero
   expected loss difference. The present claim that such rankings are
   possible is correct; the tie qualification would be additional teaching.

### Verification for this review

- `UV_NO_SYNC=1 uv run pytest tests/test_incerto_forecasting.py -q`:
  **61 passed in 1.34 s**, including the three new regression cases.
- All independent SciPy/mpmath/Monte Carlo checks described above passed.
- Regenerated the three requested pages with
  `scripts/regenerate_incerto_outputs.py --pages incerto-point-forecast incerto-scoft-ch12 incerto-api-reference`:
  **132 executed outputs, zero changed pages**.
- Regenerated all three SVGs with `demos/incerto/point_forecasts.py`;
  all three are byte-identical to the pre-review files.
- `UV_NO_SYNC=1 uv run pytest tests/test_incerto_forecasting_figures.py tests/test_incerto_page_snippets.py -k 'forecasting or incerto-point-forecast or incerto-scoft-ch12 or incerto-api-reference' -q`:
  **265 passed, 216 deselected in 174.41 s**. This checks fresh-process
  SVG byte reproducibility, all 132 affected page outputs and their API
  links. Across the two pytest runs, **326 affected cases passed**, with
  no skipped cases.
- `git diff --check`, separate whitespace checks on every untracked file,
  and all **49 local links/fragments** in the two reviewed notes and this
  record passed. Reviewed the complete modified files and the review-only diff.
- Used `UV_NO_SYNC=1`, a writable `/tmp/ch12-max-uv` cache, a scratch
  Matplotlib cache and one OpenBLAS/OMP thread. As in the writing run, this
  is an available-dependency check, not a locked-installation result.
- Full-suite, fresh site/HTML/browser, packaging, Lean, hub transfer,
  publication and live reader checks were not rerun for this narrow review.
  Earlier HTML/browser limitations remain unresolved.
- A before/after SHA-256 inventory confirms that this review changed only
  `src/math/incerto/forecasting.py`, `tests/test_incerto_forecasting.py`
  and this record. Existing chapter work was preserved. No repository
  files were added or deleted during the review, no paths are staged,
  and no commit was made. Writes stayed within this clone and `/tmp`.

## Optional review items

2026-11-01. Xiang approved both exposition clarifications. The point-forecast
note now names Durrett's scale $a_n$ and truncated centering $b_n$, relates
them to full-mean centering for $1<\alpha<2$ and zero centering below one,
and gives the logarithmic centering at one. Locator: `durrett2019probability`,
fifth edition, **Theorem 3.8.2, printed p. 186**, using the existing local
bibliography and previously checked normalization in the linked limit-law
note. Both paired-ranking passages now require a nonzero expected loss
difference for a strict preference; zero is a tie in expectation regardless
of sample averages. The chapter guide, code, and outputs are unchanged;
output regeneration was unnecessary. No network fetches or commit.

Verification with existing dependencies, offline:

- `UV_NO_SYNC=1 uv run pytest tests/test_incerto_page_snippets.py tests/test_incerto_forecasting.py -q`:
  **540 passed, 1 skipped in 141.03 s**; the local layoffs CSV is absent.
- `git diff --check`, local bibliography keys and link targets passed;
  all 14 code/output blocks in the concept page are unchanged.
- Cached KaTeX parsed all 26 concept/guide displays. The largest estimated
  width, including its font multiplier, is **317.29 px**, within the 358 px
  reading width at 390 px. Actual browser verification remains blocked by
  Chromium's socket permission error. Full site/HTML checks were not rerun.
