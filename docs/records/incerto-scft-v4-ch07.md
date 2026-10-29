# SCoFT v4 chapter 7 checkpoint

2026-10-28 (America/New_York). Branch `scft/v4-ch07-viz-p2`, base
`b863314` from `origin/main`, including PR #37. Xiang selected
**gpt-6-astra xhigh** for writing and code; **gpt-6-astra max** will review
mathematics in a separate run. No delegation, staging, commit, push,
publication or file deletion.

Chosen guide title: **Chapter 7 — Averages and limit laws**.
No title or scope decision is required from Xiang.

## Contract and source review

Implemented `scft-v4-ch07`, including attached appendices C/D: teaching
first, bounded Python second, optional Lean last. Read root/track guidance,
shared rules, notation canon/lock, program contracts/state/review, chapter
4–6 records, P1/code-visibility records and touched sources. Used concept-page,
proof-writing, reading-guide, prose-review/unslop, git-conventions and
hub-publish guidance. No package/dependency mapping, lockfile, notation canon
or legacy URL-map change.

Read the supplied read-only `/workspace/scoft-toc/2001.10488v4.pdf` and
`v4-toc.txt`. Extractions remain in `/tmp`. No book text, source figures,
tables or close paraphrases are added. The local bibliography key
`taleb2025scoftv4` pins the 2025 third edition, arXiv:2001.10488v4.
Printed pages below correspond to PDF pages 14 higher.

| Section | Printed pages | Treatment |
| --- | --- | --- |
| §7.1 | 137–139 | Weak/strong convergence; integrable weak-law proof; cited SLLN; nonnegative infinite-mean divergence |
| §§7.2.1–7.2.2 | 139–141 | Symmetric stable sum identity and moment boundary; exact Cauchy average law |
| §§7.3.1–7.3.4 | 141–145 | Uniform/exponential cumulants and Berry–Esseen bounds; Pareto moment/normalization distinctions |
| §7.4 | 145–147 | Standardized cumulant scaling; zero fourth cumulant does not identify a Gaussian |
| §7.5 | 147–148 | Explicit iid attraction assumptions; array variants retained as cited context |
| §§7.6–7.6.1 | 148–150 | Higher absolute-moment LLN; links to existing moment-estimator and max/sum results |
| §7.7 | 151–152 | Original symmetric stable mean-absolute-deviation integral proof; Gaussian endpoint checked |
| §§C.1–C.2 | 183–186 | Exact exponential-rate/Pareto-outcome transform and finite mixtures; no certification of historical pandemic fits |
| Appendix D | 187–188 | Original optimized Bernoulli Chernoff proof; no exact-probability or general-LDP inference from a bound |

Checked the author-hosted January 11, 2019 manuscript of
[Durrett, Probability: Theory and Examples](https://sites.math.duke.edu/~rtd/PTE/PTE5_011119.pdf),
using its own printed pagination: Theorems 2.3.1/2.3.7, pp. 68/70;
2.4.1, p. 76; Example 3.3.16, p. 131; Example 3.3.23, pp. 138–139;
Theorem 3.4.17, p. 157; Theorems 3.8.2/3.8.8, pp. 186/191, and
Eq. 3.8.11, p. 189; Theorem 6.2.1, p. 335. These are cited inputs,
not claims that this branch proves general stable attraction or Birkhoff.

The guide identifies qualifications rather than inheriting source shortcuts:
existence of a normalized iid limit requires attraction assumptions; exact
Pareto exponent two has infinite variance; cumulants need the correct
standardization; a stable MAD coefficient requires an explicit CF convention;
a right-tail specification cannot determine a complete two-sided density;
Chernoff factorization requires independence. General skew-stable MAD,
historical fits, and unrestricted array-limit proofs are outside the selected
bounded teaching scope.

## Pages and wiring

New pages:

- [Chapter 7 guide](../../content/incerto-scoft-ch7.md).
- [Cauchy running statistics](../../content/incerto-cauchy-running.md).
- [Time averages and ensemble averages](../../content/incerto-ergodicity.md).

Extended canonical pages: [LLN](../../content/incerto-lln-failure.md),
[generalized CLT](../../content/incerto-generalized-central-limit-theorem.md),
[max/sum](../../content/incerto-max-to-sum-ratio.md),
[mixture uncertainty](../../content/incerto-mixture-uncertainty.md), and
[Cramér condition](../../content/incerto-cramer-condition.md). Existing
Pareto boundary and resampling arguments are linked and preserved.
The [P2 record](incerto-viz-p2.md) lists the additional visualization pages
and requested mobile repairs.

Wired the guide and new concepts into `myst.incerto.yml`, SCoFT overview,
Incerto hub, theorem/example indexes, API reference and generated graph/list.
The graph has **39 nodes, 65 dependency edges and 74 reference edges**.
Routes remain under `/math/incerto/`; the shared notation URL remains
`/math/notation/`. The program has **34 implemented concept bodies**;
its frozen M0.5 denominator remains 24. Graph nodes and program bodies are
different inventories (the graph includes later migrated notes).

## Python and figures

[limits.py](../../src/math/incerto/limits.py) adds five documented helpers:
`pareto_capped_mean`, `symmetric_stable_mean_abs`, `repeated_centered_sums`,
`pareto_plugin_nonfinite_probability`, and `bernoulli_chernoff_log_bound`.
The API fixes the stable CF scale, distinguishes capped from indicator-truncated
moments, specifies centering, and prints mathematical infinities explicitly.
Inputs and failure policies are tested against independent integrals,
Gaussian endpoints, Poisson/Gamma duality, exact binomial tails and finite
sampling identities. Sampling is capped at 50 million draws per experiment;
nonfinite observations/results raise instead of being discarded.

[limit_distributions.py](../../demos/incerto/limit_distributions.py) exports:

| Figure in `assets/figures/incerto/` | Canonical page | Fixed experiment |
| --- | --- | --- |
| `cauchy-running.svg` | `incerto-cauchy-running.md` | Three 10,000-prefix paths, seed 20261071; 600 independent samples at 10/30/100/1000/10000, seed 20261072; means and medians, no tail clipping |
| `lln-failure-paths.svg` | `incerto-lln-failure.md` | Pareto 0.8/1/1.3, cutoff 1; 10,000-prefix paths, seeds 20261080–82; 600 samples at 30/100/300/1000/3000, seeds 20261180–82 |
| `lln-capped-means.svg` | `incerto-lln-failure.md` | Exact population cap formula, 301 logarithmic caps from 1 to 10^7; cap never applied to the simulated observations |
| `generalized-clt.svg` | `incerto-generalized-central-limit-theorem.md` | Pareto 1.5, cutoff 1, center 3; 800 samples at 30/100/300/1000/3000, seed 20261074; same sums divided by n^(2/3) and sqrt(n) |
| `ergodicity-growth.svg` | `incerto-ergodicity.md` | 800 paths, 200 equally likely 1.5/0.6 multipliers, seed 20261073; log wealth and two analytical targets |

All random streams in the producers use PCG64. Bands are pointwise
10th/90th sampling quantiles with medians, not confidence bands. Arrays
are batched; source support is not truncated. Stable-scale IQRs in the
full Pareto experiment are **3.045, 3.340, 3.348, 3.521, 3.681**.
Analytic MAD at alpha 1.5 is **1.705** for n=1, **0.3674** for n=100,
and **0.07916** for n=10000. Code on pages has API anchors and executed
Output blocks; long blocks use the existing dropdown convention.

## hard_math_claims_for_max_review

Line numbers below identify this implementation; anchors survive later edits.
Tests and illustrations do not substitute for the requested independent review.

| ID | Location | Claim and assumptions |
| --- | --- | --- |
| CH07-C01 | `content/incerto-lln-failure.md:16`, `:91`, `:224` | Clipping proof of the iid integrable weak law; countable-truncation proof of nonnegative infinite-mean divergence; LLN for absolute powers and the separate estimator-variance gate. |
| CH07-C02 | `content/incerto-generalized-central-limit-theorem.md:18`, `:82` | Cited stable classification/tail balance, alpha-one truncated centering, exact Pareto full-versus-truncated centering shift; exponent-two Gaussian-domain qualification. |
| CH07-C03 | `content/incerto-cauchy-running.md:29` | Exact law of every Cauchy average, failure to converge to a finite constant, sample-median consistency and distinction from ergodicity. |
| CH07-C04 | `content/incerto-generalized-central-limit-theorem.md:199`, `:229` | Symmetric stable CF convention, exact sum/average scale, Tonelli integral for MAD, alpha-one boundary and Gaussian variance 2 sigma^2. |
| CH07-C05 | `content/incerto-generalized-central-limit-theorem.md:278` | Cumulant scaling n^(1-r/2); uniform/exponential examples; zero-excess counterexample; cited Berry–Esseen constant and Pareto moment gates. |
| CH07-C06 | `content/incerto-ergodicity.md:11`, `:33` | Stationarity/ergodicity and integrability; nonergodic constant process; independent multiplicative expectation, almost-sure log growth and strict Jensen comparison. |
| CH07-C07 | `content/incerto-ergodicity.md:108`; `content/incerto-mixture-uncertainty.md:269` | Fixed-horizon exponential-rate transform, moment condition pT < lambda; finite rate-mixture exponent determined by the smallest positive-weight rate. |
| CH07-C08 | `content/incerto-cramer-condition.md:134` | Optimized Bernoulli Chernoff inequality, q endpoints and noninteger thresholds; inequality versus exact probability and a general LDP. |
| CH07-C09 | `content/incerto-max-to-sum-ratio.md:64`; `content/incerto-plug-in-tail-estimation.md:192` | Preserve zero-prefix and Pareto dominance/resampling assumptions; known-cutoff Gamma probability of an infinite plug-in mean, including the alpha-one limit 1/2. |

Also review P2's exact event geometry, tie conventions and normalization
interpretations at the locations listed in [its record](incerto-viz-p2.md#hard_math_claims_for_max_review).

## M0.5 dispositions and state

- **002:** confirmed the already-resolved zero-prefix convention and eventual
  positivity. The numerical helper still exposes NaN at a zero total.
- **006:** added verified stable/LLN/ergodic/Berry–Esseen locators and local
  special-case proofs. Darling original-text access remains a recorded
  limitation; the prior secondary cross-check is preserved. Chapter-9
  theorem-source work remains open. No blanket closure of this shared issue.
- **007:** pinned and checked chapter 7 and C/D context. Later assignments
  remain open. Citation syntax cleanup elsewhere is not a new source audit.
- **009/010:** preserved the already-resolved growing-sample/fixed-size/moment
  distinctions and model-based reference simulation/subsampling caveats.
  This run does not newly resolve them or validate an ordinary bootstrap.

State records chapter 7/C/D done at the requested implementation scope and
advances `next_chunk` to `scft-v4-ch08`. Six concepts finish their scheduled
implementation scopes; mixture uncertainty remains in progress for chapter 20.
Separate max review is explicitly pending. **Lean: skipped-for-now** because
no toolchain is available; no declaration is represented as checked.

## Verification and remaining limits

- `UV_NO_SYNC=1 UV_CACHE_DIR=/tmp/ch07-uv MPLCONFIGDIR=/tmp/ch07-mpl OPENBLAS_NUM_THREADS=1 uv run pytest -q`:
  **887 passed, 43 subtests passed in 145.45s**. This includes the exact
  snippet suite and fresh-process byte comparisons for P1/P2/Rayleigh exports.
  The 71 helper cases also pass after the final input-validation cleanup.
- `scripts/regenerate_incerto_outputs.py` executed **122 snippets and one
  full-demo output**. The first full test attempt collected old Output blocks
  during regeneration and failed 16 comparisons; the final sequential run
  above passes. An earlier environment probe imported an old checkout;
  its path was removed before final regeneration/testing.
- Locked sync could not complete: the default uv cache lock is read-only;
  a writable offline cache lacks locked SciPy artifacts, and online access
  fails DNS. The local test environment uses Python 3.13.5, NumPy **2.5.4**
  (lock 2.4.6), SciPy **1.18.1**, Matplotlib **3.11.2**, PyYAML **6.0.3**,
  NetworkX **3.7**, pytest **9.0.2**. Other local differences include
  fonttools 4.65.0, packaging 26.3 and python-dateutil 3.0.0. Locks unchanged;
  this is not a locked-environment pass.
- All 15 actual new/changed SVGs were rendered to **390/900 px PNGs** with
  system librsvg/Cairo and visually inspected (30 previews under
  `/tmp/ch07-previews`). Captions, labels, signs, legends and support views
  agree. Playwright with `/usr/bin/google-chrome` failed at sandbox
  `setsockopt: Operation not permitted`; no full-browser pass is claimed.
- `npm ci` fails offline with ENOTCACHED and online with DNS EAI_AGAIN.
  `npm run build` was attempted in `/tmp/ch07-site-check` to preserve all
  repository files; it cannot find MyST. `npm run check:html` consequently
  reports missing fresh pages/assets. No fresh site artifact or publication.
- Inline DOI links were replaced with **63 existing local bibliography
  citations** across Incerto pages; new Durrett metadata lives only in
  `content/bibliography.bib`. Source scan finds **zero inline doi.org links**.
  The blocked build made zero DOI fetches, but a successful-build network
  audit still needs the external rerun.
- State/human-view validation, file/fragment/citation checks, source TOC
  membership, graph and whitespace are recorded in the final audit below.
  Wheel/package-layout checks were not run because mapping did not change.

Remaining actions for Xiang: the already-planned max review, a locked-environment
rerun and full site/browser checks where dependencies and Chrome can run,
then reader review after any authorized publication. No new mathematical
scope decision is required.

## Final source and artifact audit

- Executed the updated canonical state/human-view validator: **1,142**
  local plan links passed. Stable IDs, chapter order, source attachments,
  chronological reuse, optional Lean reasons and the frozen M0.5 inventory
  agree. The validator now recognizes the already-merged Rayleigh page as
  post-review material, valid directory links and MyST named figure anchors.
- Reviewed the tracked diff and complete new sources/records, plus all new
  SVGs through the rendered previews. The wider audit covers **74 files**,
  including **21 new files**, **1,227 relative links**, **129 citation uses**
  and **32 figure embeds**. New files pass separate whitespace/control-character
  checks; `git diff --check` passes.
- The explicit Incerto TOC matches all **59** public track pages, with no
  duplicates. Source layout reports **83 pages overall and 79 flat redirects**.
  These are source counts, not generated-HTML verification.
- The refactored chapter-5 runner was executed into scratch output by
  redirecting its exporter. All four original SVGs remain byte-identical;
  extracting the convolution panel did not alter the existing figures.
- Final Git state remains `scft/v4-ch07-viz-p2` at **b863314**, with no
  staged changes, commits or deleted files. The working tree contains the
  implementation for review.

## Max review

2026-10-28. Xiang selected **gpt-6-astra, max reasoning**. Reviewed the
incoming tracked diff and all new files: **74 files, including 21 new files
and 15 SVGs**. The audit includes the unchanged mathematics surrounding
the edits, API examples, docstrings, test expectations, captions and recorded
numbers. No delegation, staging, commits, publication or file deletion.

Found **two mathematical/numerical errors and one quantitative docstring
error**, all corrected minimally. No known incorrect mathematical claim
remains. General theorems still have their stated hypotheses and citation
status; finite computations are not proofs of asymptotic assertions.

Locations below refer to the working tree after these fixes. Each row groups
the claims, derivation and worked values at the named section or function;
later rows cover its code and figures. **Wrong (fixed)** records the incoming
verdict, followed by the corrected result. **Correct-with-caveat** identifies
an essential qualification, usually already present in the text.
**Unverifiable** is restricted to the specific source or empirical assertion
named in that row.

The **127 verdict groups** comprise **78 correct, 44 correct-with-caveat,
three wrong (fixed), and two unverifiable**. Shortened filenames in a
multi-file row share the first file's directory.

### Fixes applied

1. `content/incerto-generalized-central-limit-theorem.md:85`: the exact
   full-versus-truncated centering difference requires
   $a_n=x_m n^{1/\alpha}$. In general it is
   $\alpha nP(X>a_n)/(\alpha-1)$, which only converges to
   $\alpha/(\alpha-1)$ under the earlier tail-quantile normalization.
   For example, $a_n=x_m n^{1/\alpha}(1+1/n)$ satisfies that normalization
   but gives $2.1466252584$, rather than $3$, at $\alpha=1.5,n=4$.
   Added the exact-scale hypothesis and the separate asymptotic statement;
   specified the downward location shift under full-mean centering.
2. `src/math/incerto/limits.py:147`: the four-term Bernoulli relative-entropy
   calculation loses the small divergence near $q=p$. For
   $p=0.35,q=0.350000001,n=2^{53}$ it returned log bound $-1$, or
   $0.3678794412$. Berry–Esseen with constant 3 gives a lower bound
   $0.4211400915$ on the actual tail, so this was an invalid upper bound,
   not merely a loose approximation. An 80-digit Decimal calculation on the
   exact binary inputs gives log bound $-0.0197960433874721$.
   A local `log1p` expression now returns $-0.0197960417717695$.
   Added three independent high-precision and probability-bound regression
   cases at `tests/test_incerto_limits.py:80`. This is ordinary floating-point
   evaluation, not interval-certified arithmetic.
3. `src/math/incerto/limits.py:97`: corrected the experiment budget from
   “one million draws per size” to one million observations **per sample**.
   The total remains 50 million. Replaced the literal temporary-memory
   bound by $O(\mathtt{batch}\max(\mathtt{sizes}))$: the draw array and
   centered temporary can coexist, besides the returned array.

Only those three files and this appended review changed during the audit.
Regeneration changed no Output blocks or figures.

### Verdict table: chapter 7 and P2 claims

All paths in this table are under `content/`.

| Location | Verdict | Claim and evidence |
| --- | --- | --- |
| `incerto-lln-failure.md:16` | correct | Weak and almost-sure convergence have the stated quantifiers. Integrability suffices for the iid SLLN; finite variance is not required. |
| `incerto-lln-failure.md:30` | correct | The clipped weak-law proof fixes the cap first, uses variance at most the squared cap, and controls the remaining average by Markov and its vanishing absolute expectation. Taking sample size, then cap, gives the claimed limit. |
| `incerto-lln-failure.md:46` | correct-with-caveat | Independent indicators with probabilities $1/n$ distinguish convergence in probability from almost-sure convergence; they are an example of random variables, not an iid sample-mean counterexample. The separate dependent weak law follows from $\operatorname{Var}(S_n)=o(n^2)$. |
| `incerto-lln-failure.md:54`, `:91` | correct | For nonnegative iid infinite-mean observations, intersect the probability-one SLLN events for integer caps. Monotone convergence makes their means unbounded, forcing the original averages to infinity almost surely. Nonnegativity is essential to this proof. |
| `incerto-lln-failure.md:134` | correct-with-caveat | The running-average update is exact; downward steps do not contradict eventual divergence. The plotted finite paths and sampling quantiles are illustrations, not an almost-sure proof. |
| `incerto-lln-failure.md:165` | correct | Integrating survival gives the capped mean, including the mass above the cap. Independent quadrature reproduces all nine table entries; at cap $10^7$ the three values are $121.5943216,17.11809565,4.306855726$. The finite limit at $\alpha=1.3$ is $13/3$. |
| `incerto-lln-failure.md:224`, `:241` | correct | Apply the SLLN or nonnegative divergence theorem to $\lvert X\rvert^p$. Finite $p$th moment and finite variance of its estimator are different gates; the latter requires the $2p$th moment. Signed undefined means and dependent data retain their caveats. |
| `incerto-generalized-central-limit-theorem.md:18` | correct-with-caveat | Classification concerns a nondegenerate limit along all sample sizes of centered/scaled iid sums. It does not assert existence for every parent. The two-sided regular-variation and tail-balance conditions supply a sufficient attraction hypothesis for $0<\alpha<2$. |
| `incerto-generalized-central-limit-theorem.md:47`, `:61` | correct-with-caveat | Tail-quantile scaling includes a slowly varying factor. Zero centering below one, truncated centering at one, and full-mean centering above one are valid in the stated cases, but can select different stable locations. No general software skew/location convention is asserted. |
| `incerto-generalized-central-limit-theorem.md:85` | wrong (fixed) | The centering difference was stated as an exact constant for a merely asymptotically normalized scale. The exact-scale hypothesis and limit distinction above repair it. |
| `incerto-generalized-central-limit-theorem.md:95`, `:108` | correct-with-caveat | The Pareto maximum CDF is $(1-1/(ny^\alpha))^n$ on its support and tends to $e^{-y^{-\alpha}}$. Its scale explains the comparison with $\sqrt n$ but does not prove a sum limit. For general Pareto-type tails the earlier slowly varying qualification remains necessary. |
| `incerto-generalized-central-limit-theorem.md:132` | correct | Exact Pareto 1.5 has mean 3 at cutoff one. Dividing the same centered sums by $n^{2/3}$ and $\sqrt n$ multiplies every quantile difference, including the IQR, by $n^{1/6}$. Displayed tables and plots use the same sums. |
| `incerto-generalized-central-limit-theorem.md:201` | correct | Multiplication of the specified symmetric characteristic functions gives the exact sum and average identities. At index two the variance is $2\sigma^2$; at one averages retain their Cauchy law; below one the scale grows. These are identities for stable parents. |
| `incerto-generalized-central-limit-theorem.md:231` | correct | The nonnegative Fourier integral permits Tonelli. The Laplace representation gives the factor $2/\pi$; substitution and integration by parts give $2\sigma\Gamma(1-1/\alpha)/\pi$. Boundary terms vanish exactly in the claimed finite-mean range. |
| `incerto-generalized-central-limit-theorem.md:252` | correct | The near-zero integrand diverges for $\alpha\le1$. Independent characteristic-function quadrature gives MAD $1.7054652402$ at index 1.5 and $2/\sqrt\pi=1.1283791671$ at index two, agreeing with the helper and displayed values. |
| `incerto-generalized-central-limit-theorem.md:280` | correct | With the stated finite absolute moment, a continuous local logarithm of the characteristic function defines cumulants. Additivity and scaling give $n^{1-r/2}\kappa_r(X)/\sigma^r$. |
| `incerto-generalized-central-limit-theorem.md:292` | correct | Uniform excess is $-6/5$, exponential skewness/excess are $2,6$, and the three-point example has variance one and fourth moment three. Independent integration gives Berry–Esseen factors $1.2990381057$ and $2.4145532941$. These are not a universal convergence-speed ranking. |
| `incerto-generalized-central-limit-theorem.md:300`, `:309` | correct | Berry–Esseen constant 3 matches the cited theorem. Exact Pareto gates are strictly above 2, 3 and 4 for variance, third absolute moment and kurtosis respectively. At exponent two, truncated second moments grow logarithmically, giving a Gaussian domain with scale of order $\sqrt{n\log n}$. |
| `incerto-generalized-central-limit-theorem.md:320` | correct-with-caveat | Gaussian attraction can include infinite variance. At exponent one, moment existence depends on $\int L(x)/x\,dx$; the example's tail integral is one, not its entire mean. Finite mean alone does not make the full-versus-truncated location shift negligible. |
| `incerto-cauchy-running.md:11`, `:29` | correct | The density and characteristic function agree. Both signed first-moment parts diverge. The characteristic function of every average remains $\exp(i\mu t-\sigma\lvert t\rvert)$; its fixed positive deviation probability rules out convergence to any finite constant. |
| `incerto-cauchy-running.md:49` | correct | Cauchy quantiles give IQR $2\sigma$. Indicator SLLNs on either side of the unique median establish sample-median consistency, including the usual even-sample convention. |
| `incerto-cauchy-running.md:67` | correct-with-caveat | Seeds, sample sizes and plotted Cauchy quantiles agree with the producer. A finite empirical band can differ from the constant population mean band; no population moments are inferred from finite draws. |
| `incerto-cauchy-running.md:111` | correct | Absolute moments exist exactly for positive orders below one. The iid shift is ergodic, but the identity observable is not integrable, so its average is outside the stated ergodic theorem. |
| `incerto-ergodicity.md:11` | correct | Stationarity concerns joint laws under time shifts; ergodicity concerns invariant events. Birkhoff's integrability hypothesis is explicit. The constant Bernoulli process is stationary and nonergodic, with path average equal to its initial draw. |
| `incerto-ergodicity.md:33` | correct | Independence gives $E W_n=W_0(EA)^n$; the log SLLN gives path growth $E\log A$. Strict Jensen applies for a nonconstant positive multiplier with the stated integrability. |
| `incerto-ergodicity.md:55`, `:63`, `:103` | correct | The 1.8/0.6 example has log growth $0.0384805206$. For 1.5/0.6, $\log EA=0.0487901642$ but $E\log A=-0.0526802578$. Positive zero-multiplier probability causes eventual absorption under iid trials. |
| `incerto-ergodicity.md:108` | correct-with-caveat | For exponential rate $R$ and fixed positive horizon, $x_m e^{TR}$ is exact Pareto with exponent $\lambda/T$ and moment gate $pT<\lambda$. A right-tail specification alone cannot determine a two-sided rate density or establish an empirical pandemic model. |
| `incerto-mixture-uncertainty.md:34`, `:64` | correct | Conditional Gaussian moments transfer through powers of the variance. The two-state fourth moment $4.08$ and rare-variance mixture kurtosis $77.25$ follow by weighted sums; a finite hierarchy does not create an infinite moment. |
| `incerto-mixture-uncertainty.md:117` | correct | Gamma mixing of variance, lognormal mixing of variance, and Gamma mixing of precision give different moment/MGF behavior. The precision construction yields Student tails with moment threshold $p<\nu$ and variance $\nu/(\nu-2)$ where finite. |
| `incerto-mixture-uncertainty.md:209` | correct | Completing the square gives the stated Bessel-$K$ density and constants. Its exponential tails and origin limits follow from the Bessel integral and small/large-argument asymptotics; the singular value at the origin is not an atom. |
| `incerto-mixture-uncertainty.md:269` | correct-with-caveat | A finite mixture of positive rates is dominated by the smallest positive-weight rate. Equal minimal rates add their weights. The displayed coefficient uses the basis $(x_m/x)^{\lambda_{\min}/T}$; in a bare power of $x$ it also includes $x_m^{\lambda_{\min}/T}$. The strict moment gate and example mean 1.6 at $T=1/2$, infinite at $T=1$, are correct. |
| `incerto-cramer-condition.md:15`, `:65`, `:102` | correct | One-sided and neighborhood exponential-moment conditions are distinguished. Markov gives the stated bounds; normal/exponential MGFs and Pareto's divergent positive MGF have the correct domains. A growing truncated exponential integral is a finite check, not the proof by itself. |
| `incerto-cramer-condition.md:134` | correct | Optimizing the Bernoulli MGF gives the stated tilt and binary relative entropy. $q\le p$ gives the trivial upper bound; $q=1$ gives $p^n$; noninteger thresholds mean an integer ceiling. |
| `incerto-cramer-condition.md:170`, `:192` | correct-with-caveat | Independent finite binomial sums reproduce the table: for $n=1000,p=1/2,q=3/4$, the tail is $6.7381282530\times10^{-59}$ and the bound $1.5454488091\times10^{-57}$. A Chernoff inequality alone establishes neither exact probability nor a full LDP. The helper's separate numerical error is fixed. |
| `incerto-plug-in-tail-estimation.md:46`, `:133` | correct | Known-cutoff log excesses are exponential. The MLE and mean functional, including the all-cutoff limiting convention, follow. The delta-method variance coefficient is $x_m^2\alpha^2/(\alpha-1)^4$, equal to 36 at cutoff one and exponent 1.5. |
| `incerto-plug-in-tail-estimation.md:105`, `:177` | correct-with-caveat | Root-$n$ log-fit concentration under the exact model differs from the $n^{-1/3}$ sample-mean scale at exponent 1.5. The finite-fit event tends to one when the true mean is finite; this does not remove the finite-sample singularity or justify model misspecification. |
| `incerto-plug-in-tail-estimation.md:192` | correct | The fit is infinite exactly when the Gamma log-excess sum is at least $n$. Integer-shape Poisson sums independently reproduce every analytic probability; at exponent one the sequence tends to $1/2$ by the CLT. At exponent 1.5 and $n=100$ the probability is $5.9245403355\times10^{-6}$. |
| `incerto-plug-in-tail-estimation.md:246`, `:303` | correct | Body-plus-tail decomposition gives example mean 3.4. The derivative has negative sign. Positive log-fit density immediately below its pole makes even the conditional finite-fit first and second moments infinite; weak concentration does not imply moment convergence. |
| `incerto-subexponentiality.md:15`, `:64`, `:120` | correct | For nonnegative iid variables, the strict maximum event is contained in the strict sum event. The maximum tail is $2\bar F-\bar F^2$ universally; subexponentiality additionally makes the residual negligible. Fixed-$n$ tail equivalence is stated with its distributional hypotheses. |
| `incerto-subexponentiality.md:66` | correct-with-caveat | The first-quadrant partition is exact: maximum above $u$, or sum above $u$ with both coordinates at most $u$. The diagonal sum boundary is excluded. Colored area is not probability, and the caption supplies the boundary convention that filled polygons alone cannot encode. |
| `incerto-subexponentiality.md:95`, `:175`, `:283` | correct | The two strips plus the event that both observations exceed $h$ cover the residual. Choosing $h=x_m(x/x_m)^\gamma$ with $1/2<\gamma<1$ gives both required limits. Independent residual bounds are $0.3434278964,0.0303804248,0.00300375538$; prose rounds upward. |
| `incerto-subexponentiality.md:315`, `:328` | correct-with-caveat | Direct convolution integration reproduces all displayed ratios. At $u=10^4$, Pareto 1.5 gives $1.0004499437$, Weibull 0.5 gives $1.0103196875$, and exponential gives $5000.5=(1+u)/2$. The finite curves illustrate independently established limits. |
| `incerto-counting-exceedances.md:6`, `:69`, `:116` | correct | Strict survival is the complement of the right-continuous empirical CDF. For [1,2,2,4], values at threshold 2 are $1/4$ and $3/4$; non-strict exceedance is $3/4$. Open points mark left limits and filled points actual values. |
| `incerto-counting-exceedances.md:96` | correct-with-caveat | At a fixed threshold, iid indicators give a binomial count, unbiased fraction and variance $q(1-q)/n$. That assertion does not supply calibration for thresholds selected from the same data. |
| `incerto-max-to-sum-ratio.md:14`, `:61` | correct | Positive totals give $1/n\le M_n/S_n\le1$; zero prefixes are undefined. A nonzero nonnegative iid law eventually has positive total. Integrability plus Borel–Cantelli gives $M_n/n\to0$, then the SLLN gives a vanishing ratio. |
| `incerto-max-to-sum-ratio.md:29`, `:239` | correct-with-caveat | Exact Pareto exponent one has ratio tending to zero in probability, while below one the limit is nondegenerate, not identically one. The almost-sure converse is a cited result, not proved by the finite-mean argument; original-text access is separately qualified below. |
| `incerto-max-to-sum-ratio.md:117`, `:141` | correct | The running-list ratios and sums are exact; exponent 1.3 has typical maximum-to-sum order $n^{-3/13}$. Growing-sample paths and fixed-size repeated reference distributions answer different questions. |
| `incerto-max-to-sum-ratio.md:183` | correct-with-caveat | The subsampling conditions, nondegenerate limiting statistic and rescaling are necessary qualifications. For a continuous sample with a unique maximum, ordinary bootstrap includes it with probability $1-(1-1/n)^n\to1-e^{-1}$, creating the stated atom. Estimated scaling exponents need the specified rate condition. |
| `incerto-tail-threshold-selection.md:18`, `:61` | correct-with-caveat | Strict excesses, Hill's order-statistic convention and ties are distinguished. Exact GPD mean/variance gates are $\xi<1$ and $\xi<1/2$; regular-variation boundary moments need the slowly varying factor. Return quantiles have no singularity specifically at those two gates. |
| `incerto-tail-threshold-selection.md:83`, `:137` | correct | The 0.82-uniform/0.18-Pareto mixture survival integrates correctly. Expected counts are $17700,5400,1662.044958,511.554341$; $e(2)=1.9600484262$. Above the join, $\xi=10/17$, $\beta(u)=10u/17$, and modified scale is zero. The shared-grid figures preserve these targets. |
| `incerto-rayleigh-speed.md:31` | correct | Radial integration of independent Gaussian velocity components gives the normalized chi density, moment domain $r>-d$, dimensions 1/2/3, and the stated mean/variance/mode table. Independent quadrature confirms unit mass and second moment $d\sigma^2$ for dimensions 1,2,3,7. |
| `incerto-rayleigh-speed.md:109`, `:156` | correct | Speed has a generalized-Gamma kernel with squared argument, unlike GIG. Squared speed and kinetic energy have the stated Gamma scales; reciprocation gives inverse Gamma. Tail and near-origin comparisons are correct on the stated parameter domains. |
| `incerto-rayleigh-speed.md:193` | correct-with-caveat | Flux weighting multiplies the chamber speed density by speed and renormalizes, giving chi dimension $d+1$ under isotropy and the small-hole equilibrium model. A 2D effusive sample therefore has the 3D Maxwell speed form. |
| `incerto-rayleigh-speed.md:232`, `:285` | correct-with-caveat | With fixed total energy and no imposed total-momentum constraint, the energy fraction is Beta$(d/2,d(N-1)/2)$. Independent integration verifies normalization and second moment. Flux shifts the first Beta shape by $1/2$; the quasistatic cooling calculation gives $T\propto N^{1/d}$. These assumptions are not a certification of an animation's dynamics. |
| `incerto-rayleigh-speed.md:316` | correct-with-caveat | All recorded seeded diagnostics reproduce. Independent component draws give Rayleigh scale $0.9967140161$ and AIC $93781.3091$. Parameter-fitted KS p-values are explicitly uncalibrated; model ranking is a result for this sample. |
| `incerto-rayleigh-speed.md:390` | correct | The split equation preserves the factor $1/2$ and derivative sign. Solving the Gamma likelihood equation independently gives shape $3.1513414895$, scale $0.3964398066$, inward score $-0.0400805846$. Concavity and the two zero tangential scores justify the boundary optimum. |
| `incerto-rayleigh-speed.md:413`, `:420` | correct-with-caveat | The GIG AIC uses its declared nominal three-parameter count, so it is Gamma's AIC plus two; regular-model boundary validity is not claimed. QQ axes are theoretical horizontal/empirical vertical, all 199 probabilities are retained, and the fixed exponential squared-speed KS gives $D=0.00579135123,p=0.0696173878$. |
| `incerto-scoft-ch7.md:19`, `:34`, `:49`, `:73` | correct-with-caveat | Source locators and site normalization order agree with the supplied v4. The guide's moment/scaling summaries and worked MAD/cap values agree with the audited notes. It explicitly declines the source's unproved skew-MAD constants, unconditional attraction reading and empirical pandemic inference. |

### Verdict table: other changed mathematical pages

These pages mostly have citation-syntax changes, but their surrounding claims
were also reviewed. Paths remain relative to `content/`.

| Location | Verdict | Claim and evidence |
| --- | --- | --- |
| `incerto-pareto.md:28`, `:157`, `:208`, `:293` | correct | Density/CDF/survival, quantiles, hazard, moments, exceedance sizes and the known-cutoff likelihood follow by direct integration or differentiation. The finite-mean formula is used only above exponent one; an all-cutoff sample is handled as a limiting likelihood case. |
| `incerto-pareto.md:311`, `:350`, `:378` | correct | The sum-regime table distinguishes growing sample size from a fixed-size large threshold. The exponent-one truncation proof gives $S_n/(n\log n)\to x_m$ in probability and hence a vanishing maximum share. The subexponential fixed-$n$ claim has different quantifiers. |
| `incerto-pareto.md:400`, `:492` | correct | Union bounds give the minimum tail exponent for fixed positive sums without independence, but not full regular variation. Independent products follow from sums of exponential logs, including the equal-exponent logarithmic factor. The rare Pareto mixture has mean 0.55, survival 0.0025 at 4 and the stated moment boundary. |
| `incerto-pareto-moment-existence.md:15`, `:47`, `:88`, `:126` | correct | Direct integration gives the strict $p<\alpha$ gate, logarithmic equality case and truncated powers. Tonelli justifies independent-product moment factorization including divergent positive moments. Worked values agree with these integrals. |
| `incerto-regular-variation.md:25`, `:82`, `:123`, `:150` | correct-with-caveat | The tail-ratio characterization, representation-based bound and positive-power exponent $\alpha/r$ are correct. The representation theorem's necessity is cited rather than inferred from its elementary sufficiency proof. Slow variation need not approach a constant. |
| `incerto-karamata.md:14`, `:104`, `:173`, `:199` | correct | Integral asymptotics have the correct exponent domains and constants. Applying them to survival gives truncated and conditional moments. At the boundary the integral of $L(t)/t$ decides finiteness; the logarithmic example yields $(1+\alpha)e^\alpha$ for its boundary moment. |
| `incerto-double-pareto.md:15`, `:121`, `:186` | correct | The shifted symmetric convention is normalized, distinct from unshifted signed Pareto. Its tails, CDF, quantiles and absolute moments follow from the signed magnitude transformation and beta integral. |
| `incerto-double-pareto.md:218` | correct | Student tail matching and variance matching require different scales. At exponent three, the variance-matched tail ratio is $4/(3\pi)=0.4244131816$; the tail-matched Student variance is $1.7706827540$. |
| `incerto-extreme-value-index.md:15`, `:90`, `:184`, `:209` | correct-with-caveat | The EVI sign regimes and Pareto relation $\xi=1/\alpha$ are correct. Exact Pareto maxima use $c_n=x_m n^{1/\alpha}$, with GEV location $c_n$ and scale $c_n/\alpha$. Hill interpretations assume a positive regularly varying tail. |
| `incerto-frechet.md:17`, `:72`, `:108`, `:127` | correct | Density, support, moments and GEV conversion are consistent. The finite-block CDF and expansion have the correct negative $t^2/(2n)$ log correction. At normalized threshold one, $n=10,100,250,600$ give $0.3486784401,0.3660323413,0.3671424536,0.3675726619$. |
| `incerto-generalized-extreme-value.md:15`, `:60`, `:108`, `:132` | correct-with-caveat | CDF/density, support endpoints and the Gumbel limit are correct with SciPy shape $c=-\xi$. A density value assigned at a single endpoint need not equal its interior limit. The shorter figure title preserves all support information in the caption. |
| `incerto-generalized-pareto.md:15`, `:52`, `:110`, `:146` | correct | CDF/density, finite endpoint and its three density regimes, exponential limit, moment gates and threshold stability are correct. Exact Pareto excesses have shape $1/\alpha$ and scale $u/\alpha$. |
| `incerto-pickands-balkema-de-haan.md:17`, `:85`, `:120` | correct-with-caveat | The cited conditional-excess approximation is a uniform CDF statement on the available support with an appropriate scale. The local Pareto calculation is exact. Neither establishes a finite-data threshold rule or relative accuracy arbitrarily deep in the tail. |
| `incerto-hill-estimator.md:31`, `:67`, `:85`, `:129` | correct-with-caveat | The baseline is the next order statistic; for [1,2,4,8], the estimates are $\log2,1.5\log2,2\log2$. Consistency requires an intermediate sequence; normal error calibration needs further tail conditions. Ties and threshold selection retain their qualifications. |
| `incerto-mean-excess-function.md:15`, `:59`, `:109`, `:157` | correct | Tail integration and threshold conditioning give Pareto $u/(\alpha-1)$ and GPD $(\beta+\xi u)/(1-\xi)$ on their domains. Infinite means and zero-count estimates are not replaced by finite curves. Exponential/uniform population examples and strict counts are correct. |
| `incerto-iso-density-tail-geometry.md:21`, `:38`, `:82` | correct | Independent Gaussian contours favor balance; independent Cauchy density along a fixed positive sum has the stated stationary points and transition at sum two. The derivative factorization and tabulated comparisons check directly. |
| `incerto-iso-density-tail-geometry.md:127`, `:159` | correct | The spherical bivariate Cauchy density is normalized but is not the product of its marginals; the displayed sector probability is $1/(6\sqrt{10})=0.0527046277$. Switching correlations gives covariance identity but a nonradial characteristic function, so uncorrelated does not imply elliptical. |
| `incerto-survival-tail-ratio.md:18`, `:41`, `:79`, `:108` | correct-with-caveat | The squared-survival diagnostic is different from a convolution ratio. Pareto, exponential, Gaussian, Gamma and stretched-Weibull calculations have the stated limits. A zero or borderline ratio does not uniquely identify a tail class. |
| `incerto-tail-class-catalog.md:16`, `:70`, `:106`, `:127` | correct | The class examples, slowly varying factors and moment contrasts are consistent. Lognormal has all positive power moments and no finite positive exponential moment; completing the square and comparing quadratic/linear exponent growth prove those claims. |
| `incerto-tail-class-catalog.md:161`, `:210`, `:270` | correct | Ratios and finite comparison tables use their declared normalizations. Gamma convolution has asymptotic ratio $\Gamma(k)(\lambda x)^k/(2\Gamma(2k))$; exponential is the exact $(1+\lambda x)/2$ case. |
| `incerto-tail-class-catalog.md:325` | correct | Exponentiating Pareto gives a slowly varying survival with no finite positive power moment. Squeezing the sum tail between maximum and rescaled-maximum tails proves its subexponentiality. |
| `incerto-tail-class-catalog.md:370`, `:402` | correct | Location-mixture kurtosis 1.72 follows from second/fourth moments. Absorption requires repeated conditional chances; the finite-state example and summable-hazard counterexample, including survival at least one half, are valid. |
| `incerto-tail-class-catalog.md:474` | correct | Splitting the iid convolution at half the threshold and adding the both-large term gives the displayed identity, including nonnegative support and log-space evaluation. The numerical quadrature is not used as a proof of a limit. |
| `incerto-scoft-intro.md:1`, `incerto-empirical-example-concepts.md:1`, `incerto-theorem-concepts.md:1`, `incerto/index.md:1` | correct-with-caveat | New guide, Cauchy and ergodicity summaries agree with the canonical notes. These are navigation/classification statements; “theorem” placement does not upgrade numerical illustrations to proofs. |

### Verdict table: API, code and test expectations

API locations are in `content/incerto-api-reference.md`. Existing small
arithmetic examples were recalculated; executable Output blocks were also
regenerated and compared by the full snippet suite.

| Location | Verdict | Claim and evidence |
| --- | --- | --- |
| API `:86` | correct-with-caveat | Log/negative-log returns, counts and frequency lookup examples follow their finite input arithmetic. Dataset descriptions concern repository provenance; this audit does not independently certify the external observations. |
| API `:288`, `:334` | correct | Distribution conventions agree with the notes. The displayed default `hypsecant2` characteristic function is real because the law is centered and symmetric; removing `+0j` loses no information in this example. |
| API `:354`, `:379`, `:410` | correct-with-caveat | GPD/GEV signs, domains, endpoint conventions and Fréchet conversion are consistent. The documented tiny-argument Fréchet `nan` is a numerical limitation, not the mathematical density at zero. |
| API `:441` | correct | Hill/reciprocal-Hill, plug-in mean, running mean, maximum share and mean-excess examples match direct log sums and counts. [1,2,2,4] has strict excess counts [3,1,0] at [1,2,4]. GPD numerical success is explicitly weaker than model validity or a global optimum. |
| API `:650`, `:788` | correct | The two absolute-deviation functions are Gaussian-calibrated; the stable MAD helper is raw MAD. For [1,2,3], the values are $\sqrt{\pi/2}\,2/3$ and $1/\Phi^{-1}(3/4)$. Dispersion ratios use population-divisor standard deviation, with undefined constant-sample ratios and infinite zero-MedianAD ratios preserved. |
| API `:691`, `:710`, `:729`, `:748` | correct | Scale-curvature and variance-curvature boundaries are different. Their normal roots are $\sqrt{(5\pm\sqrt{17})/2}$ and $\sqrt{3\pm\sqrt6}$; Student roots and lognormal moment-to-parameter conversion have the stated scales. |
| API `:811`, `:894`, `:942` | correct | Survival ratios, direct convolution ratios, seeded exceedance fractions, spike moments and Pareto tail quantities agree with their definitions. Spike probability 0.01 gives radius 10, variance one and kurtosis 100; normalized maximum CDF values follow the exact finite-$n$ formula. |
| API `:1001` | correct | Repeated-event probability is $1-(1-p)^n$ for independent trials. Conditional-hazard products, finite-payoff expectation, absorbing paths and independent block means/variances/probabilities reproduce all displayed values. The split-damage example keeps its common-shock model. |
| API `:1139` | correct | Finite Gaussian-mixture densities, absolute survival and moments use the declared weights/variances. Pareto moment-estimator variance needs the doubled-order gate; the $\alpha=6,q=2,n=200$ value is $0.00375$. Absolute power means have the displayed sample-size normalization. |
| API `:1262` | correct | Student entropy uses scatter and nats; mutual information subtracts joint entropy from marginal entropies. Shared Gamma precision gives the declared bivariate Student law. Pearson versus uncentered cosine, eigenvalues, regression $R^2=1/4$ and mixture kurtosis 1.72 agree with the stated inputs. |
| API `:1422` | correct | Independent-product tails, indicator-truncated moments, Student matching and normalized q-exponential examples agree with their formulas. The log-constraint entropy example has common log moment $1/2$ and nonnegative KL equal to the entropy gap. |
| API `:1549` | correct-with-caveat | Chi speed, component-stream order, seven-family parameter counts, boundary fitting, QQ orientation and fixed-null squared-speed testing agree with the code. The numerical interior GIG branch does not certify a global optimum. |
| API `:1684` | correct-with-caveat | All five limit-helper contracts match their mathematical definitions after the Bernoulli fix. The cutoff cancels in the Gamma probability; positive infinite moments are distinct from numerical overflow. Sampling limits describe observations, not distribution truncation. |
| API `:1834`, `:1927` | correct | Figure counts, support markers, zero-survival masking, five-inch layout and strict exceedance examples match the implementation. The card viewport is explicitly finite and does not redefine the law's support. |
| `src/math/incerto/limits.py:31` | correct | `pareto_capped_mean` evaluates the survival integral, handles caps below cutoff and the logarithmic boundary, and preserves scale. Independent log-coordinate integration and the extreme-scale case $(c,x_m,\alpha)=(10^{300},10^{-300},1/2)$ give the expected value 2. |
| `src/math/incerto/limits.py:72` | correct | `symmetric_stable_mean_abs` implements the derived gamma expression in log space, with mathematical infinity at indices at most one and Gaussian variance $2\sigma^2$. Independent CF integration checks indices 1.1,1.5,2. |
| `src/math/incerto/limits.py:90` | correct-with-caveat | `repeated_centered_sums` sums centered observations, performs no scaling or mean estimation, and rejects invalid draws. Independent direct normal draws reproduce its stream and sums. Independence relies on the supplied sampler honoring its frozen-law contract. |
| `src/math/incerto/limits.py:97` | wrong (fixed) | The incoming per-size draw and literal memory claims were inaccurate. The corrected per-sample bound and asymptotic sampling-memory statement agree with the loop and allocation behavior. |
| `src/math/incerto/limits.py:123` | correct-with-caveat | `gammaincc(n,alpha*n)` is the correct Gamma survival. Independent finite Poisson sums agree at all figure inputs; tiny probabilities can underflow and machine output is not arbitrary-precision exactness. |
| `src/math/incerto/limits.py:135` | wrong (fixed) | The analytic Bernoulli formula and endpoint rules were correct; cancellation could violate the upper-bound property at allowed large sample sizes. The `log1p` branch and three Decimal/Berry–Esseen regressions address the demonstrated error. |
| `tests/test_incerto_limits.py:18`, `:37`, `:57`, `:64`, `:80`, `:97`, `:115`, `:124` | correct | Survival/CF integrals, Gaussian MAD, Poisson duality, optimized tilts, high-precision relative entropy, constant and shifted sums, budget checks and invalid-domain expectations are mathematically appropriate. Infinity and `nan` expectations distinguish absent moments from invalid estimates. |
| `src/math/incerto/gas_speeds.py:48`, `:61`, `:112`, `:134`, `:197`, `:220`, `:235` | correct-with-caveat | Chi sampling/scaling, Gamma and inverse-Gamma boundary scores, parameter counts and QQ grids match the note. The inverse-Gaussian physical-to-SciPy mapping is consistent. Boundary scores certify the stated cases; interior optimization retains its numerical caveat. |
| `tests/test_incerto_gas_speeds.py:22`, `:35`, `:90`, `:131`, `:148`, `:164` | correct | Normalization, energy-transform and flux identities, scale-equivariant sampling, AIC/KS values, boundary/inverse-boundary/interior cases, linear empirical quantiles and two-panel layout expectations all pass. The ranking and raw fitted KS p-values are expectations for the seeded sample only. |
| `src/math/incerto/figures.py:1`, `demos/incerto/distribution_cards.py:1`, `demos/incerto/rayleigh_speed.py:1` | correct | Edits change labels or export grouping. Distribution parameters, support, density normalizations, sample and quantile grid are preserved; regenerated assets match byte-for-byte. |
| `demos/incerto/power_laws.py:42` | correct | The extracted convolution plotter preserves laws, 81 thresholds, ratio normalization and failure checks. Independent integration checks both heavy-tail curves, while the exponential curve has a closed-form reference. |
| `demos/incerto/tail_estimation.py:1`, `:28`, `:37`, `:105`, `:143` | correct-with-caveat | The declared mixture, seeds, strict counts, known targets, shared grid and count masking agree. Four fits are below the count threshold; all eligible fits succeed numerically. At most 40 fits includes the separate PP examples. Success supplies no threshold/model guarantee. |
| `demos/incerto/limit_distributions.py:1`, `:32`, `:39` | correct-with-caveat | Cauchy, capped and uncapped Pareto, normalized-sum and growth experiments use the documented centers, sizes and seeds. Bands are pointwise sampling quantiles. PCG draws and finite paths do not prove infinite-sample properties. |
| `demos/incerto/visualization_p2.py:30` | correct | Event polygons, strict step endpoints, functional domain $\alpha>1$, and Gamma probability curves agree with the notes. Independent inverse-transform sampling reproduces every finite/infinite-fit count in the P2 record. |
| `tests/test_incerto_viz_p1.py:22`, `:49`, `:68`, `:100`, `:121`, `:166`, `:195`, `:244`, `:284` | correct-with-caveat | All distribution/support/normalization, zero-prefix, fit-domain, count-mask and reproducibility expectations check. GEV's assigned endpoint density is deliberately distinguished from its diverging interior limit. Parameter-recovery tolerances are numerical checks, not statistical coverage assertions. |
| `tests/test_incerto_viz_p2.py:22`, `:31`, `:41`, `:49` | correct | Tied-CDF complements, the exact $n^{1/6}$ empirical IQR ratio, exponential convolution and fresh-process SVG byte comparisons test the intended identities. Byte identity itself is not evidence for an asymptotic theorem. |

### Verdict table: generated assets, sources and records

SVG locations use line 1 because labels and paths together encode each figure.
Their generating calculations are reviewed above.

| Location | Verdict | Claim and evidence |
| --- | --- | --- |
| `assets/figures/incerto/subexponential-geometry.svg:1`, `subexponential-convolution.svg:1` | correct-with-caveat | Regions, strict boundary caption and convolution ratio match the proofs. The finite viewport and colored area do not encode a probability measure. |
| `assets/figures/incerto/lln-failure-paths.svg:1`, `lln-capped-means.svg:1` | correct | Complete running paths and repeated-sample bands are separate from population capped means; the mean line is drawn only for exponent 1.3. |
| `assets/figures/incerto/generalized-clt.svg:1`, `cauchy-running.svg:1` | correct | Sum normalizations, Cauchy reference quantiles and mean/median labels agree with the declared laws and sample sizes. |
| `assets/figures/incerto/ergodicity-growth.svg:1` | correct | The distinct curves are log expected wealth and expected log wealth. Their slopes have the independently checked signs and magnitudes. |
| `assets/figures/incerto/plugin-mean-singularity.svg:1`, `exceedances-ties.svg:1` | correct | Infinite-mean domain, all-fit proportions, analytic probability lines and open/filled tie markers match the exact formulas and counts. |
| `assets/figures/incerto/threshold-diagnostics.svg:1`, `threshold-gpd.svg:1`, `gev-card.svg:1` | correct-with-caveat | Split figures retain the same sample/grid and masks. Target shape, mean excess, modified scale, counts and GEV endpoints are correct; optimizer success is labeled as an outcome. |
| `assets/figures/incerto/rayleigh-speed-fits.svg:1`, `rayleigh-speed-qq.svg:1`, `rayleigh-speed-qq-tail.svg:1` | correct | Density and QQ labels, Gamma/GIG overlap, inverse-family tails and fixed exponential comparison agree with the seeded calculation. All 199 quantiles per fit remain displayed. |
| `content/bibliography.bib:336` | correct | Added Durrett metadata identifies the author-hosted 2019 manuscript and its own pagination. The chapter's cited Cauchy, stable-existence, attraction, Berry–Esseen and Birkhoff locators agree with that source. |
| `content/incerto-max-to-sum-ratio.md:257`, `docs/records/incerto-scft-v4-ch07.md:136` | unverifiable | Exact original-text verification of the Darling/O'Brien source statements was not completed. The max/sum claims agree with the independent finite-mean proof and accessible research-paper restatements; this does not close the original-source access gate. |
| `content/incerto-rayleigh-speed.md:5`, `content/incerto-scoft-ch7.md:29` | unverifiable | The physical implementation of the linked animation and the source's historical pandemic fits were not independently established. The notes correctly refrain from treating their calculations as such evidence. |
| `docs/records/incerto-scft-v4-ch07.md:22`, `content/incerto-scoft-ch7.md:12` | correct-with-caveat | Compared new exposition with the supplied v4 chapter 7 and appendices C/D. No copied passages were identified. A full-book exact 12-word scan of affected Markdown/Python prose found zero matches; that scan alone cannot rule out every close paraphrase. No book figures or tables were imported. |
| `docs/records/incerto-viz-p2.md:17`, `:36`, `:59`, `:76` | correct | Eleven new plus four changed SVGs; seven P2 figures, two chapter-7 figures and two new split exports. Seeds, sizes, fit counts, 390-pixel heights and mathematical captions agree with code and fresh previews. |
| `docs/records/incerto-scft-v4-ch07.md:154`, `docs/records/incerto-viz-p2.md:120` | correct-with-caveat | The incoming 887-test result is a historical implementation checkpoint. This review adds three cases, so the current result is 890 tests and 43 subtests. Prior build/browser and locked-environment limitations are not converted into passes. |
| `docs/plan/incerto-program/state.yaml:1`, `README.md:74`, `concepts.md:344`, `m0.5-review.md:199`, `validation.md:26`, `verification.md:1`, `visualization-review.md:12` | correct-with-caveat | The executable state/human-view validator passes all inventory totals, chapter assignments and 1,142 local links. There are 34 existing program concept pages; the M0.5 denominator remains 24. “Max review pending” is historical implementation state and is superseded by this section; it was left unchanged under the audit-only scope. |
| `assets/data/concept-graph.json:1810`, `assets/graphs/concept-list.html:1`, `myst.incerto.yml:1` | correct | Graph counts, dependency order, new page descriptions and TOC membership agree with the source inventory and tests. Graph links describe reading relationships, not additional mathematical implications. |

### Evidence and independent calculations

Analytic checks were performed before comparing with repository helpers.
Scratch calculations in `/tmp/incerto-max-numerics.py` and its JSON output
use SciPy quadrature, finite binomial/Poisson sums, direct component and
inverse-transform sampling, and an independent Gamma-likelihood root solve.
Decimal at 80 digits supplies the Bernoulli regression reference; mpmath is
not installed. The values needed to assess the findings are preserved above,
so the verdicts do not depend on retaining scratch files.

The cited probability inputs were checked against
[Durrett's author manuscript](https://sites.math.duke.edu/~rtd/PTE/PTE5_011119.pdf),
including Theorems 2.4.1, 3.4.17, 3.8.2/3.8.8 and 6.2.1 and
Examples 3.3.16/3.3.23. The symmetric scale convention also agrees with
[SciPy's characteristic-function specification](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.levy_stable.html).
The non-Gaussian subexponential examples agree with Theorems 3.29/3.30 of
[Foss–Korshunov–Zachary, second edition](https://www.math.u-szeged.hu/~kevei/tanitas/irodalom/Foss%20Korshunov%20Zachary%20An%20intro%20to%20heavy%20tailed%20and%20subexp%20dist.pdf).
The beta and Bessel identities used in the notes agree with
[DLMF 5.12.1](https://dlmf.nist.gov/5.12.E1),
[10.32.10](https://dlmf.nist.gov/10.32.E10) and
[10.40.2](https://dlmf.nist.gov/10.40.E2).

For max/sum source qualifications, the nondegenerate heavy-tail limit is
restated in [Kevei–Mason (2014), p. 632](https://alea.impa.br/articles/v11/11-30.pdf).
The almost-sure versus probability distinction is restated on p. 2 of the
[Arizona research report](https://www.cs.arizona.edu/sites/default/files/TR94-18.pdf).
The [O'Brien publisher abstract](https://www.cambridge.org/core/journals/journal-of-applied-probability/article/abs/limit-theorem-for-sample-maxima-and-heavy-branches-in-galtonwatson-trees/5988AEA451D95250FA1B1F2C8F5C96D1)
confirms its probability-limit subject and bibliographic identity, but does
not expose the full almost-sure argument. The general subsampling discussion
agrees with the conditions in
[Bickel–Götze–van Zwet, Theorem 1](https://www3.stat.sinica.edu.tw/statistica/oldpdf/a7n11.pdf).

### Open decisions for Xiang

- Decide whether publication requires obtaining the original Darling/O'Brien
  texts before closing the remaining max/sum source gate. No mathematical
  contradiction was found; the original-text verification is incomplete.
- Reconcile the plan and P2 record's pending-review wording when updating
  implementation status. This section completes the requested max audit;
  the other files retain their historical checkpoint text.
- Keep the current bounded scope unless a later task expands it: the
  parameterization-independent skew attraction statement, symmetric-only
  MAD proof, numerical GIG interior fit and unverified empirical source
  examples already disclose their limits. None requires a mathematical edit
  for this chapter's stated claims.

### Verification performed and limits

- Ran `scripts/regenerate_incerto_outputs.py` with the available environment:
  **122 snippets and one full-demo output executed; zero pages changed**.
- After regeneration completed, ran
  `UV_NO_SYNC=1 UV_CACHE_DIR=/tmp/incerto-max-uv MPLCONFIGDIR=/tmp/incerto-max-mpl OPENBLAS_NUM_THREADS=1 uv run pytest -q`:
  **890 passed, 43 subtests passed in 139.14 seconds**. This includes the
  affected limit, gas-speed, P1/P2 and snippet tests and fresh SVG exports.
- Ran the independent numerical audit and the canonical state/human-view
  validator; both passed. The latter checked **1,142** local plan links.
- Checked **1,227** local links and **129** citation uses across affected
  Markdown: no missing targets, fragments or bibliography keys. Direct
  inventory checks confirm **59** Incerto pages, **83** total source pages,
  **79** flat redirects and graph counts of **39** nodes, **65** dependency
  edges and **74** reference edges.
- Rendered all **15 SVGs at 390 and 900 pixels** using librsvg/Cairo into
  `/tmp/incerto-max-previews`; visually inspected all 15 mobile-width previews.
  Math labels, supports, scales, event/tie geometry and QQ orientation agree.
- Used the available Python 3.13.5 environment with NumPy 2.5.4 and SciPy
  1.18.1. This is **not** a locked-dependency pass. No new site build,
  browser/navigation pass, package build, Lean check or publication was run.
  The previously recorded installation/browser blockers remain external
  follow-ups; the audit does not claim to have rerun those blocked actions.
- `git diff --check` and separate whitespace/control-character checks on
  all **21** untracked files pass. Compared every affected file against the
  incoming snapshot: only the four audit files listed above differ, and
  this record's original text is intact. Git remains on
  `scft/v4-ch07-viz-p2` at **b863314**, with no staged changes or deletions.

## Mobile equation fit pass

2026-10-28. Reformatted **77 display blocks across the 13 requested pages**
for approximately 330 CSS pixels of equation space at a 390-pixel viewport.
Stacked paired formulas, split equality chains and long products or sums,
and placed side conditions on separate rows. The centering cases' two prose
qualifications now follow their display. Mathematical meaning, equation labels,
references, citation passages, and executable examples are preserved.

Verification: `UV_NO_SYNC=1 UV_CACHE_DIR=/tmp/incerto-mobile-uv uv run pytest -q
tests/test_incerto_page_snippets.py` passed **257 tests**; the same invocation
with `tests/test_concept_graph.py tests/test_migration_manifest.py` passed
**11 tests**. Compared against the incoming files, checked display delimiter,
brace and environment balance, and preserved the label/link/citation/code
inventories. `git diff --check` and separate whitespace checks on the touched
untracked files passed. Widths were estimated conservatively from the TeX;
no site build or browser measurement was run in the sandbox. Work remains
uncommitted on the same branch, with no staging or file deletion.
