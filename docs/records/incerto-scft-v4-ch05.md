# SCoFT v4 chapter 5 checkpoint

Date: 2026-10-18. Branch: `scft/v4-ch05`, from `origin/main` at `f222fd5`.
Owner-selected model: gpt-6-astra, xhigh, for writing and code. A separate
owner-selected gpt-6-astra max run will review the hard mathematics; it has
not occurred in this checkpoint. No delegation, commit, push or publication.

The implementation-stage results below are retained as history. The subsequent
[Max review](#max-review), completed on 2026-10-18, supersedes their pending
review status and test count.

The chosen guide title is **Chapter 5 — Subexponentials and power laws**.
It retains the source's mathematical topic while omitting its level label.
The original source-unit title remains unchanged in state and the inventory.
No decision from Xiang is needed for the title or the bounded model scopes.

## Contract and source review

Executed `scft-v4-ch05`: chapter 5 plus attached appendix B, teaching first,
bounded Python cases second, optional Lean last. The nine contracted concepts
reuse eight canonical bodies and add one maximum-entropy body. The survival
ratio page already existed and was extended. The new chapter guide links
prior proofs rather than duplicating them.

Read the supplied read-only `/workspace/scoft-toc/2001.10488v4.pdf` and
`/workspace/scoft-toc/v4-toc.txt`. The edition is Taleb (2025), third edition,
arXiv:2001.10488v4, bibliography key `taleb2025scoftv4`. Extracts and scratch
calculations stay under `/tmp`; no source prose, tables or figures entered
the repository. Explanations, proofs, worked inputs and figures are original.

| Source locator | Printed pages | PDF pages | Scoped teaching |
| --- | --- | --- | --- |
| §5.0.1 | 91–93 | 105–107 | Fixed-size iid sums and subexponentiality |
| §§5.0.2–5.0.3 | 93–95 | 107–109 | Event ratios, conditional size, logistic boundary example |
| §5.1.1 | 95–97 | 109–111 | Regular variation, representation and integral distinctions |
| §5.1.2 | 97–98 | 111–112 | Model comparison; no empirical fit inferred |
| §§5.2.1–5.2.2 | 98–100 | 112–114 | Positive sums; independent Pareto products |
| §5.2.3 | 100 | 114 | Positive powers and exponent transformation |
| §5.3 | 101 | 115 | Normalized double Pareto versus Student |
| §5.4 | 102 | 116 | Inference limitation; jobless-claims data not reproduced or validated |
| §5.5 | 102–103 | 116–117 | Log-Pareto, index-zero survival and moment divergence |
| §5.6 | 103–105 | 117–119 | Squared Student exponent and moment gates; links chapter-4 estimator distinction |
| Appendix B opening / §B.1 | 127–129 | 141–143 | Fixed measure/support; Shannon maxima |
| §B.2 | 129–133 | 143–147 | Tsallis composition, escort stationarity and normalized q family |

The §5.6 special-function expression and mean-deviation table are not needed
for the contracted teaching and are not claimed verified. No empirical or
historical data study is included. The appendix's nonlinear escort constraint
is treated through necessary stationarity and explicit family properties;
a general global escort-constrained maximum is not asserted.

Theorem-level source checks, performed against actual text:

- Bingham, Goldie and Teugels, *Regular Variation*: Theorem 1.3.1, p. 12,
  for representation; Theorem 1.5.11, p. 28, for the direct Karamata theorem;
  Propositions 1.5.8 and 1.5.10, pp. 26–27, for power-times-slow-factor
  integrals. Inspected the [publisher preview](https://api.pageplace.de/preview/DT0400.9781107107939_A23693114/preview-9781107107939_A23693114.pdf),
  PDF pages 34 and 48–50. The existence theorem is cited; its elementary
  consequences and the moment calculations are proved locally.
- Foss, Korshunov and Zachary, *An Introduction to Heavy-Tailed and
  Subexponential Distributions*, second edition (2013): §3.3, Corollary 3.20
  and Theorem 3.21, p. 52, for fixed-size convolution equivalence; §3.5,
  Theorem 3.29 and following paragraph, p. 57, for regular variation;
  Theorem 3.30 and examples, p. 58, for lognormal and stretched Weibull.
  Inspected the [authors' book text on a university host](https://www.math.u-szeged.hu/~kevei/tanitas/irodalom/Foss%20Korshunov%20Zachary%20An%20intro%20to%20heavy%20tailed%20and%20subexp%20dist.pdf),
  PDF pages 64 and 69–70. These classifications are cited inputs, not
  conclusions from the finite plots.

## Claims and teaching artifacts

| Claim ID | Page / scope | Evidence and limits |
| --- | --- | --- |
| CH05-C01 | [Regular variation](../../content/incerto-regular-variation.md#regular-variation-representation) | Cited measurable representation; proved sufficiency, log-tail exponent and positive-power transformation. A log ratio does not imply convergence of a derivative. |
| CH05-C02 | [Karamata](../../content/incerto-karamata.md#karamata-conditional-mean), [Pareto moments](../../content/incerto-pareto-moment-existence.md) | Cited integral theorem with local boundedness; derived conditional-size limit and a complete finite boundary-moment example. Exact Pareto's equality boundary remains divergent; general regular variation can differ. |
| CH05-C03 | [Pareto sums/products](../../content/incerto-pareto.md#pareto-sums-products) | Positive finite sums preserve a logarithmic exponent under arbitrary dependence; no full regular-variation claim from these bounds. Exact independent product formulas include the equal-exponent logarithm. Signed cancellation, dependent squares and reciprocals show the hypotheses matter. Existing growing-sample regimes are retained. |
| CH05-C04 | [Double Pareto and Student](../../content/incerto-double-pareto.md#double-pareto-student-matching) | Density bounds give Student tail constant and moment threshold. Tail and variance matching give different scales and moments. Normalization and undefined-mean reporting convention are preserved. |
| CH05-C05 | [Survival ratio](../../content/incerto-survival-tail-ratio.md#tail-ratio-borderline) | Logistic light-tail/MGF comparison, Laplace ratio, exponential prefactor under translation and exact Weibull formula. The event ratio is distinguished from convolution. |
| CH05-C06 | [Subexponentiality](../../content/incerto-subexponentiality.md), [log-Pareto](../../content/incerto-tail-class-catalog.md#tail-catalog-log-pareto) | General fixed-size and class results cited; direct maximum-bound squeeze proves the log-Pareto index-zero case. Every positive power moment diverges. No growing-sample maximum/sum limit is inferred. |
| CH05-C07 | [Shannon certificate](../../content/incerto-maximum-entropy.md#maximum-entropy-shannon) | KL inequality proves the global uniform, Gaussian and log-constrained Pareto optima with equality conditions. Measure, support, integrability and coordinate change are explicit. |
| CH05-C08 | [Tsallis and escorts](../../content/incerto-maximum-entropy.md#maximum-entropy-tsallis) | Joint-density composition and necessary variational equation are derived. No entropy identity for a sum or global conclusion from nonlinear-constraint stationarity. |
| CH05-C09 | [q family](../../content/incerto-maximum-entropy.md#maximum-entropy-q-family) | Normalization, compact/infinite support, survival exponent, ordinary-moment threshold and escort mean derived. A log-gamma competitor independently checks the Shannon entropy gap. |

The [guide](../../content/incerto-scoft-ch5.md) also derives the exponent
of a squared Student variable and routes its mean/variance gates to the
existing moment notes. It supplies the stretched-Weibull conditional-mean
counterexample to a thin-tail inference. These guide claims belong in the
separate max review along with CH05-C01 through CH05-C09.

The guide, track hub, overview, Methods index and API reference are linked
through `myst.incerto.yml`. The regenerated concept graph has **35 nodes,
60 dependency edges and 65 reference edges**. Flat source paths and
`/math/incerto/` routes are preserved. Cross-track references use canonical
`/math/ig/` and `/math/notation/` URLs. No URL-map row or notation symbol
was added or renamed.

## Python, worked values and figures

New helper: [power_laws.py](../../src/math/incerto/power_laws.py).
New runner: [power_laws.py](../../demos/incerto/power_laws.py).
New tests: [test_incerto_power_laws.py](../../tests/test_incerto_power_laws.py).
Imports use the installed `xmath.incerto` mapping. Dependencies and packaging
are unchanged. No external data, RNG, fitting, censoring or sampling intervals.

The five helper entry points calculate Pareto product log survival,
indicator-truncated Pareto moments, Student matching scales, q-exponential
log survival and one entropy/KL worked comparison. Input validation rejects
invalid domains. Arithmetic overflow raises rather than posing as a
mathematical infinite moment. Log-tail calculations retain underflowed
ordinary probabilities. Truncated moments may underflow to zero. Compact
q survival is mathematically zero beyond its endpoint; no observations are
removed. Entropy quadrature documents its limiting/underflow integrands.

Near-equal product exponents use `expm1`; thresholds near the minimum use
a second-order CDF series. Truncated-moment evaluation uses logarithms and
the continuous equality case. Tests compare independent conditioning and
density integrals, gamma/GPD parameterizations, analytic moments, endpoint
limits and explicit invalid/overflow cases. The shared convolution helper
is also checked against separate quadrature and the exact exponential sum.

| Figure | Fixed scope |
| --- | --- |
| [Diagnostics](../../assets/figures/incerto/power-law-diagnostics.svg) | Two vertical panels. 241 event-ratio thresholds in [1,16]; 81 convolution thresholds in [3,10000] for each of Pareto(1.5), Weibull(0.5), exponential(1). Convolution rtol=1e-9, maxlevel=12; every success flag checked. |
| [Integrals](../../assets/figures/incerto/power-law-integrals.svg) | Three vertical panels. 241 product/truncation thresholds in [1,10000]; log-integral comparison starts at 1.01. Product exponents (1,2) and (1,1), Pareto moment exponent 1.5 and orders 1/1.5/2, logarithmic integrals with powers 0/1. |
| [Matching](../../assets/figures/incerto/power-law-matching.svg) | Three vertical panels. Exponent 3; 501 density points in [-4,4] and 241 thresholds in [1,10000]. Tail-matched and variance-matched Students compared to unit shifted double Pareto. |
| [Entropy](../../assets/figures/incerto/power-law-entropy.svg) | Two vertical panels. 301 log-size points in [0,3]; 301 q-family thresholds in [0,6], beta=2 and q=0.75/1/1.25/1.6. Entropy/constraint/KL integrals run to infinity, limit=160, epsabs=epsrel=1e-10, estimated error budget 2e-9. |

All four figures call shared `set_theme(scale=1.1)` and `savefig` from
`src/math/incerto/figures.py`; each uses one column, regular bundled serif
fonts and different line styles. Finite plotted values and quadrature flags
are checked. Original SVGs are the repository artifacts;
390px and 900px previews are scratch verification files outside the repo.

Representative runner output:

- Two-sum ratios at thresholds 3 and 10000: Pareto **1.76907593** and
  **1.00044994**; Weibull **1.04038344** and **1.01031969**; exponential
  **2** and **5000.5**. Maximum quadrature evaluations were 259, 131 and 131.
- Student constant at exponent 3: **1.1026577908435844**; tail-matching
  scale **0.7682627055029694**; variance-matching scale **0.5773502691896257**;
  tail-matched variance **1.770682754000227**. Variance-matched survival
  ratio tends to **4/(3 pi) = 0.424413...**, not one.
- Pareto/log-gamma masses are 1 within floating precision; both log moments
  are **0.5**. Entropies **0.8068528194400547** and **0.6909213037816425**;
  independently integrated KL **0.11593151565841223**.
- The finite regular-variation boundary example gives **3e² = 22.167168297**.
  Log-Pareto survival at log thresholds 2, 4 and 8 is **1/4, 1/16, 1/64**.

These values check finite calculations. They neither prove asymptotic
classification nor establish empirical adequacy.

## M0.5 dispositions and optional Lean

- **006:** chapter-5 theorem locators checked and attached to the cited
  statements. Other assigned chapters remain open; no global closure.
- **007:** chapter 5 and appendix B use the pinned v4 key and checked
  locators. Other assigned chapters retain their work.
- **009:** confirmed reviewed Pareto growing-sample regimes unchanged;
  fixed-size rare events, sum bounds and products are explicitly separated.
- **012:** confirmed density factor 1/2, mean/variance distinction and
  `NaN`/`+inf` reporting convention; the full suite retains those tests.
- **015:** confirmed integral-theorem cross-reference; representation now
  has a separate cited section, with no conflation of the two theorems.

The global M0.5 issue counts are unchanged. No new owner decision is needed.
Lean is **skipped-for-now**: no installed toolchain and no sandbox network,
as instructed. No checked declaration or formalization coverage is added.

## Verification and remaining gates

| Check | Actual result |
| --- | --- |
| Environment | Default uv cache was read-only. `UV_CACHE_DIR=/tmp/m05-uv-cache UV_OFFLINE=1 uv sync --locked` succeeded with cached dependencies. |
| `UV_CACHE_DIR=/tmp/m05-uv-cache UV_OFFLINE=1 uv run pytest -q` | **386 passed, 43 subtests passed in 4.35s**, including 48 new chapter-5 cases. |
| Chapter-5 demo | Passed; four SVGs exported; deterministic regeneration and preview audit recorded below. |
| `npm ci --offline --cache /tmp/m05-npm-cache --no-audit --no-fund` | Failed `ENOTCACHED` for MyST 1.10.1. Reused `node_modules` from `/workspace/pub31-math-1792350000` after byte-identical package-lock comparison. |
| `npm run build` with writable offline uv cache | Blocked at MyST npm preflight. Direct Node child-process probe reproduces `EPERM spawnSync /bin/sh`. No fresh HTML build. |
| `npm run check:html` | Failed on absent fresh HTML/config/assets following the blocked build. No passing HTML claim. |
| State, links, citations, TOC, source overlap, whitespace | Final source audit recorded below. |
| Separate Astra max review | Pending, assigned to the later owner-selected run. |
| Rendered browser equations/navigation and live reader review | Not performed; require a successful external build and authorized publication. SVG previews are narrower evidence. |
| Wheel build | Not run: package mapping and dependencies unchanged. |
| Lean | Explicitly skipped for toolchain/network limits. |

State marks `scft-v4-ch05` and its two source units done at the recorded
teaching scope and moves `next_chunk` to `scft-v4-ch06`. Concepts with later
extensions (Pareto, catalog, maximum entropy) remain in progress; other
chapter-5 concepts close their implementation scopes. Each carries the
pending separate max review honestly. There are **31 implemented concept
bodies**, while the frozen M0.5 review denominator stays **24**.
Chapter 6 is a next pointer, not authorization to execute it in this run.

Changed artifacts: nine concept bodies; new chapter guide; Methods index,
track hub, overview and API reference; MyST TOC and generated graph;
Python helper, demo and tests; four SVGs; this record; program state,
concept register, README, validation, verification and M0.5 issue follow-ups;
and the planning index. Existing notation, URL map, bibliography, dependency
locks, package mapping and all prior figures remain unchanged.

## Final source and artifact audit

The implementation checks and remaining gates above are distinct from the
separate max review. The final audit below records source-level consistency
and SVG reproducibility; it does not establish generated HTML or live review.

- The executable state/human-view validator passes, including unique keys,
  no YAML aliases, stable IDs, exact chapter order, source/concept mappings,
  deliverable status, frozen review counts and **1,028** local plan links.
  Later chunk reuse lists recognize the new maximum-entropy page without
  backdating it into the chapter-5 reused-page list. Later work stays todo.
- Source audit: **32 changed/new files, 10 new files**, **745** relative
  file/fragment links, **75** content citation-key uses, all five guide titles
  against TOC/hub/overview, and SVG XML. Source membership is **53 Incerto
  pages, 77 pages across four sites, 73 flat redirects**. These are source
  counts, not a generated HTML pass.
- Manual source comparison and a normalized nine-word overlap scan found
  no matching passage between the changed teaching bodies (license notices
  excluded) and the supplied chapter 5 / appendix B. This supplements original
  drafting and manual review; it is not a copyright classifier.
- All **four SVG hashes match** after regeneration. Rendered actual SVGs
  with system librsvg/Cairo at **390px and 900px**, inspected all four at
  both widths, and rechecked the integral plot after removing unused negative
  axis space. Single-column labels and legends remain readable.
- Audited **182 embedded glyph outlines** against the bundled font files;
  all four figures use DejaVu Serif regular outlines, with no bold glyphs.
  This verifies the exported SVGs, not a browser's page CSS or a live device.
- Final numerical boundary review added a small-rate q-near-one case and
  rejects a nonrepresentable compact-support endpoint. Final full suite:
  **386 passed, 43 subtests passed in 4.35s**, including **48 chapter-5 tests**.
  These changes leave the worked model curves unchanged.
- Reviewed all tracked diffs and full new teaching, helper, demo, tests and
  record. `git diff --check` and separate new-file whitespace/final-newline
  checks pass. No deleted or staged files: **22 modified and 10 untracked**.
  No commit, push, publication or external message was sent.

The hard-math review remains pending for CH05-C01 through CH05-C09, the
squared-Student and conditional-mean guide consequences, and the numerical
boundary behavior. No mathematical or editorial choice requires Xiang's
input before that separate review. The external build/check and subsequent
live Math Site Editor review remain the site follow-ups.

## Max review

Date: 2026-10-18. Reviewer: owner-selected **gpt-6-astra, MAX**. Reviewed the
uncommitted `scft/v4-ch05` work in this clone, including tracked diffs, full
new files, proofs, cited inputs, helpers, tests and all four exported figures.
No delegation or external consultant was used. The supplied PDF was read
without modification; source extracts and rendered previews remain in `/tmp`.

**Verdict: correct after the fixes below; no open mathematical claim within
the contracted scope.** “Fixed” includes an omitted hypothesis, an ambiguous
scope or figure description, or a reproducible numerical defect. It does not
mean that every formula in that row changed. Numerical checks support worked
examples; the proof and citation verdicts rest on the arguments and sources.

### Claim verdicts

| Claim | Verdict | Mathematical review |
| --- | --- | --- |
| C01: measurable representation | **correct** | BGT Theorem 1.3.1 supplies existence for a positive measurable slowly varying function. The note proves sufficiency only, with a locally integrable exponent and the correct limiting prefactor. |
| C01: logarithmic exponent | **correct** | Splitting the exponent integral beyond an arbitrary small bound proves $\log L(x)/\log x\to0$. The resulting logarithmic tail exponent makes no derivative claim. |
| C01: positive powers | **correct** | For $X\ge0$ and $r>0$, the transformed survival has exponent $\alpha/r$ and slowly varying factor $L(y^{1/r})$. Negative powers require information near zero. |
| C02: Karamata integrals | **correct** | Eventual positivity, measurability and local boundedness suffice in the stated strict ranges $\rho>-1$ and $\rho<-1$. The lower integration endpoint lies in the locally bounded region; the boundary $\rho=-1$ is excluded. |
| C02: moment consequences | **fixed** | Both integration-by-parts coefficients, $\alpha/(\alpha-p)$ and $\alpha/(p-\alpha)$, are correct. Restricted the prose about finite moments to **positive** orders $0<p<\alpha$; tail information alone does not control negative moments near zero. |
| C02: conditional means | **correct** | For $\alpha>1$, the conditional-mean ratio tends to $\alpha/(\alpha-1)$ and the mean-excess ratio to $1/(\alpha-1)$. Added the explicit definition $e(u)=\mathbb E[X-u\mid X>u]$. |
| C02: boundary-moment example | **correct** | The stated survival is a full probability law. Its $\alpha$th moment is $(1+\alpha)e^\alpha$, including the contribution below $e$. Exact Pareto still diverges at equality. |
| C03: dependent positive sums | **fixed** | Added the missing assumption that **each $L_i$ is slowly varying**. The maximum lower bound and union upper bound then both have logarithmic exponent $-\min_i\alpha_i$. They do not establish full regular variation under arbitrary dependence. |
| C03: independent Pareto products | **correct** | Conditioning gives the unequal-exponent formula and the equal-exponent logarithm. Cutoff rescaling is correct. The dependent-square and reciprocal examples correctly delimit the result. |
| C04: Student tail constant | **correct** | Integrating two-sided asymptotic density bounds gives the displayed $C_\alpha$. The Student scale contributes $s^\alpha$ to the right-tail constant. |
| C04: moments and matching | **fixed** | Made the absolute-moment criterion explicitly about positive orders. Tail matching uses $(2C_\alpha)^{-1/\alpha}$; variance matching uses $\sqrt{2/[\alpha(\alpha-1)]}$ for $\alpha>2$. The exponent-3 constants and variances are correct. The existing undefined-mean reporting convention is unchanged. |
| C05: logistic and Laplace ratios | **correct** | The centered logistic example is light-tailed, has an MGF for $\lvert\theta\rvert<2k$, and has $Q_F\to1$. The normalized squared-secant density and SciPy scale mapping agree. Centered Laplace has $Q_F=1/2$ on the positive half-line. |
| C05: prefactor and translation | **correct** | If $\bar F(x)\sim c e^{-\lambda x}$, then $Q_F\to c$. Translation by $d$ changes this to $c e^{\lambda d}$, so the ratio is not translation invariant. |
| C05: Weibull ratio | **correct** | $\log Q_F(x)=(2^\beta-2)x^\beta$ gives the three regimes at $\beta<1$, $\beta=1$ and $\beta>1$. This event ratio is kept separate from convolution subexponentiality. |
| C06: fixed-size equivalence | **correct** | The cited fixed-$n$ result applies to iid nonnegative variables with unbounded right support. The converse needs $n\ge2$; $n=1$ is trivial. No growing-sample maximum/sum conclusion is inferred. |
| C06: class citations | **correct** | FKZ's cited results support regular variation, lognormal and stretched Weibull. These are identified as cited results, while the elementary maximum and Pareto calculations are proved locally. |
| C06: log-Pareto | **fixed** | The survival, density, direct maximum-bound squeeze and divergence of every positive power moment are correct. Replaced an overly broad sentence about a “positive survival exponent” with the precise conclusion that a regularly varying survival can be subexponential at index zero. |
| C07: KL certificate | **correct** | Finite cross-entropy makes the KL identity well-defined, including $h(f)=-\infty$. Equal finite constraints give the same cross-entropy; equality requires $f=g$ almost everywhere. Existence is not claimed for arbitrary constraints. |
| C07: uniform and Gaussian maxima | **correct** | The uniform result fixes a finite interval; the Gaussian result fixes mean and positive finite variance on $\mathbb R$. Both are global maxima among densities on the stated support. |
| C07: Pareto maximum | **correct** | The support is $[x_m,\infty)$ with $x_m>0$ and fixed $\mathbb E\log(X/x_m)=m>0$. The exponent is $1/m$ and entropy is $\log(x_m m)+1+m$. The coordinate-change qualification is necessary and present. |
| C08: Tsallis composition | **correct** | The identity follows from factorization of the joint density's $q$th-power integral. It concerns the independent pair, not its sum; differential-entropy signs prevent an unconditional additive-order label. |
| C08: escort stationarity | **correct** | Differentiating the quotient gives the displayed multiplier equation for admissible interior variations. The nonlinear constraint and necessary-only status are explicit. No general global optimum is asserted. |
| C09: q-family normalization and support | **correct** | The normalizer, compact support for $q<1$, exponential definition at $q=1$, and integrability restriction $q<2$ on infinite support agree. The survival exponent is $(2-q)/(q-1)$ for $1<q<2$. |
| C09: ordinary and escort moments | **correct** | Positive ordinary moments require $p<\alpha$ in the power-tail case, with divergence at equality. The ordinary mean threshold is $q<3/2$. Escort mass $\beta^{q-1}(2-q)^q$ and mean $1/[\beta(2-q)]$ are correct. Zero escort mean is impossible for this nondegenerate density on the unchanged half-line. |
| C09: Shannon comparison | **correct** | The log-gamma competitor has the same log moment and a different ordinary mean. Its entropy agrees with the gamma entropy plus the Jacobian term; the independently integrated KL equals the entropy gap, about $0.115932$. |
| C09: q-survival helper | **fixed** | Removed avoidable loss of small nonzero log survivals near $q=1$ and incorrect support classification near a rounded compact endpoint. Six new cases check these defects; see below. |
| Guide: squared Student | **correct** | Squaring changes the survival exponent to $\nu/2$. Its mean requires $\nu>2$ and variance requires $\nu>4$; equality diverges. Those moment gates do not identify a stochastic-volatility process. |
| Guide: conditional-mean counterexample | **correct** | For $\bar F(u)=e^{-\sqrt u}$, direct integration gives $e(u)=2\sqrt u+2$, hence conditional mean divided by $u$ tends to one despite subexponentiality. |
| Figure descriptions | **fixed** | Corrected the regular-variation page's demo pointer, the compact-survival caption, and the matching panel's title. All plotted quantities, models, grids and numerical values agree with their captions after these edits. |

### Source and proof checks

Rechecked every chapter-5/appendix-B section and page locator in the changed
teaching against the supplied v4 PDF. The locator table above is correct.
In particular, §B.1.1 spans pp. 128–129; the Pareto and uniform examples
are in §§B.1.2–B.1.3 on p. 129. Composition is on p. 130, the escort
calculation spans pp. 130–132, and normalization is on pp. 132–133.
The chapter-5 qualifications about dependence, the double-Pareto factor
$1/2$, conditional means and escort centering are supported by the source
comparison. No source text, table or figure was copied into the teaching.

Rechecked BGT Theorem 1.3.1, p. 12; Theorem 1.5.11, p. 28; and
Propositions 1.5.8/1.5.10, pp. 26–27, using the publisher text linked above.
Rechecked FKZ, second edition, Corollary 3.20/Theorem 3.21, p. 52,
Theorem 3.29 and following paragraph, p. 57, and Theorem 3.30 and its
examples, p. 58. The general existence, integral and convolution theorems
remain cited; local consequences are not presented as proofs of those theorems.

The retained EKM Appendix A3 pointer agrees with the
[publisher's appendix text](https://link.springer.com/content/pdf/bbm%3A978-3-642-33483-2/1):
§A3.2 starts on p. 571. Retained beta-integral and Gaussian-tail inputs agree
with [DLMF 5.12.1](https://dlmf.nist.gov/5.12#E1) and
[DLMF 7.12.1](https://dlmf.nist.gov/7.12#E1). The unchanged Darling
Theorem 5.1 attribution was checked through
[Kevei and Mason, p. 632](https://alea.impa.br/articles/v11/11-30.pdf#page=2),
which explicitly identifies the iid counterpart; this is not a claim to have
retrieved Darling's original text. The retained earlier Taleb chapter/section
pointers on the touched pages were also checked in the supplied PDF.

### Fixes and numerical evidence

The q-survival defects were reproducible independently of the plotted cases:

- With $q$ the next float above one, $\beta=10^{-309}$ and $x=1$,
  the old result was zero instead of a representable log survival near
  $-10^{-309}$. The corresponding case below one also lost a small finite
  value. Factoring through the continuous ratio $\log(1+v)/v$ preserves it.
- At $q=1/4$, $\beta=7$, the rounded floating-point value of $4/21$ is
  still inside the support of the exact input parameters. The old helper
  returned $-\infty$ there, whereas the log survival is about $-87.336545$.
  A narrow endpoint branch now evaluates the sign and residual with exact
  ratios of the input floats. Four parameter sets compare the predecessor,
  rounded endpoint and successor against independent 90-digit decimal
  calculations. A nonrepresentable endpoint still raises as documented.

The other helpers agree with their formulas: independent conditioning for
products; indicator-truncated moment integrals including equality; Student
density constants and variances; and independent entropy/constraint/KL
integrals. The tests distinguish mathematical divergence from arithmetic
overflow. No distribution fit or empirical evidence is claimed.

Ran `UV_CACHE_DIR=/tmp/m05-uv-cache UV_OFFLINE=1 uv run pytest`:
**392 passed in 4.34s**, including **54 chapter-5 cases** (six added in this
review). This is the current suite result; the earlier 386-test/subtest
output above belongs to the implementation run.

Ran `UV_CACHE_DIR=/tmp/m05-uv-cache UV_OFFLINE=1 uv run python demos/incerto/power_laws.py`.
All quadrature-success and finite-value checks passed; the worked constants
and entropy gap above are unchanged. The runner regenerated all four SVGs
through the shared figure style. Diagnostics, integrals and entropy are
byte-for-byte unchanged. Only the matching figure changed, to title its top
panel **Same exponent, different central shapes**; all three laws are centered
at zero. The regular-variation pointer now describes the actual Student and
double-Pareto curves. The entropy caption states that compact survival reaches
zero at two and stays zero.

Rendered the actual regenerated SVGs with librsvg/Cairo at 390px and 900px
and inspected all eight previews. Labels and legends are readable and
unclipped; curves and captions agree. These are SVG checks, not a browser
review of generated pages.

Review edits affect six teaching pages, the helper and its tests, the demo,
one SVG, this record and the existing program status views. The other chapter-5
files were reviewed without further edits. Initial worktree changes remain
uncommitted; no file was deleted or staged.

The executable state/human-view validator passed, including **1,028** local
plan links. The source audit passed for **32 changed/new files**, including
**10 new files**, **746** relative file/fragment links and **75** citation-key
uses. All five guide titles agree across navigation; SVG XML, source membership
(53 Incerto pages, 77 total pages, 73 redirects), new-file whitespace and
final newlines passed. The changed teaching has no nine-word source-overlap
matches under the implementation audit's documented exclusions. Reviewed the
final diffs and new files; `git diff --check` passed. The supplied PDF retains
SHA-256 `758e18b7337840104db93296144d67cf5514bf2de128fe557dc84bc32a0ad567`.

### Decisions for Xiang and remaining checks

**No required decision and no open claim within this review scope.** Two
optional extensions remain outside it: a global optimization theorem under
the nonlinear escort constraint, and independent verification of the §5.4
historical data or the §5.6 special-function expression/mean-deviation table.
The current notes explicitly exclude those claims; this review does not
authorize expanding their scope or starting chapter 6.

HTML build/check, browser equations/navigation and a fresh live reader review
were not rerun here. The implementation run's MyST `spawnSync /bin/sh EPERM`
block remains unresolved. Wheel and Lean builds were not run; packaging is
unchanged and there is no new formalization. No commit, push or publication
was performed.

## Operator rerun outside the sandbox

On 2026-10-18 the operator reran the checks outside the Codex sandbox after
deleting `_build/`: `uv run pytest` (392 passed, 43 subtests), `npm ci`,
`npm run build` (exit 0, no `doi.org` fetches) and `npm run check:html`
(exit 0; 77 pages across four sites, 64 legacy compatibility pages). This
resolves the sandbox `EPERM` blocker above. Post-publication live reader
review remains pending until Xiang approves merge and publish.
