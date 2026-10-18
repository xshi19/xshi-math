# SCoFT v4 chapter 2 implementation

Date: 2026-10-17 (America/New_York). Branch: `scft/v4-ch02`.
Base: `cbda44920c6a7a358ce35ca3ebd708877d3bcedc` (`origin/main`).
Owner-selected model: gpt-6-astra, xhigh. No commit or deployment.
The separate owner-requested max-reasoning review is recorded below.

## Source and teaching scope

Read the supplied read-only `/workspace/scoft-toc/2001.10488v4.pdf`,
chapter 2, printed pp. 7–21 (PDF pages 21–35), and `v4-toc.txt`.
Extracted text stayed under `/tmp`. No PDF, extract, source prose or source
figure entered the repository. Citations use chapter/section/page locators.

Added [the chapter 2 guide](../../content/incerto-scoft-ch2.md), covering the
glossary through a notation table, source-to-page map, original worked cases,
and explicit boundaries on cited results. The core teaching additions live in
the four contracted concept pages:

- [Counting exceedances](../../content/incerto-counting-exceedances.md):
  local threshold $t$ maps to canonical $u$; right-continuous CDF, strict
  survival and atoms; finite-sample Bernoulli mean/variance and a pointwise bound.
- [Pareto](../../content/incerto-pareto.md): conditional excess law, mean
  excess versus conditional mean, tail contribution, and known-cutoff MLE proof.
- [EVI](../../content/incerto-extreme-value-index.md): exact finite maximum
  CDF, its Fréchet limit, and conversion to the page's GEV normalizations.
- [Tail catalog](../../content/incerto-tail-class-catalog.md): a complete
  log-corrected survival whose slowly varying factor diverges, plus the
  reader-requested explanation of the near-overlapping light-tail curves.

Teaching was drafted before the Python helper/demo/tests. The guide maps
later topics to existing pages or explicitly planned treatments; it does not
execute later chapter chunks or assert that their general theorems are proved.
The source's CDF/empirical-indicator conventions, conditional-tail-mean
notation, constant-factor language, and endpoint description are separated
from the definitions used here. General LLN/CLT statements are cited at
§§2.2.2–3, p. 10. General EVT/PBDH claims remain cited; the new EVI proof
establishes only the exact Pareto calibration.

The original guide is in the Incerto TOC, track hub and SCoFT overview.
Its canonical route is `/math/incerto/incerto-scoft-ch2/`; the existing layout
discovers its flat compatibility redirect. No URL-map or base-path change
was made. Expected source membership is 45 Incerto pages, 69 overall, and
65 flat redirects; these counts do not assert an HTML build.

## Claims for the separate max review

These are the new or newly scoped claims. Review hypotheses and proof scope
independently of the numerical checks. The existing Pareto growing-sample
regimes and fixed-size rare-event proofs were retained unchanged from M0.5.

| ID | Claim and scope | Evidence / location |
| --- | --- | --- |
| CH02-C01 | For nonempty finite real observations, strict survival complements the empirical CDF, including ties, and is bounded and nonincreasing. For iid draws and fixed nonrandom $u$, its expectation is $q=\bar F(u)$ and variance $q(1-q)/n$; the Chebyshev bound is pointwise and requires no moments of $X$. | [Exceedance note](../../content/incerto-counting-exceedances.md#exceedances-cdf-and-atoms): partition and indicator proofs. No uniform empirical-process result is claimed. |
| CH02-C02 | For exact Pareto with $\alpha,x_m>0$, $u\ge x_m$, the excess is exact GPD with $\xi=1/\alpha$, scale $u/\alpha$; mean excess and conditional mean are finite precisely for $\alpha>1$. For any nonnegative law and $u\ge0$, the tail first moment equals $u\bar F(u)+\int_u^\infty\bar F(v)dv$ in extended nonnegative reals. | [Pareto threshold quantities](../../content/incerto-pareto.md#pareto-threshold-quantities): conditional survival cancellation, integration and Tonelli argument; numeric example $(\alpha,x_m,u)=(3/2,1,4)$. |
| CH02-C03 | For iid exact Pareto, known cutoff and observations in support, $D=\sum\log(x_i/x_m)>0$ gives unique MLE $n/D$; $D=0$ has no finite maximizer. | [Likelihood proof](../../content/incerto-pareto.md#pareto-known-cutoff-likelihood): first/second derivatives and boundary behavior. No estimated-threshold extension. |
| CH02-C04 | Exact iid Pareto maxima normalized by $c_n=x_m n^{1/\alpha}$ have CDF $(1-y^{-\alpha}/n)^n$ on support, converging to $e^{-y^{-\alpha}}$ for $y>0$. Choosing $a_n=c_n/\alpha$, $b_n=c_n$ gives GEV index $1/\alpha$. Endpoint approach alone does not specify a normalized nondegenerate limit. | [EVI proof](../../content/incerto-extreme-value-index.md#evi-pareto-calibration): independence, logarithmic limit and affine change of variables. |
| CH02-C05 | The survival equal to 1 below 1 and $x^{-2}(1+\log x)$ above 1 defines a law, has variation index $-2$, and has a slowly varying factor tending to infinity. | [Catalog counterexample](../../content/incerto-tail-class-catalog.md#tail-class-catalog-slow-variation): monotonicity, endpoints and multiplier-ratio proof. |
| CH02-C06 | A quantile-integral tail mean differs from strict conditioning at an atom; the empirical law of $(1,2,2,4)$ gives 3 versus 4 at level 1/2. Uniform CDF convergence alone does not imply mean convergence: mass $1/j$ at $j^2$, otherwise zero, has CDF gap $1/j$ from a point mass at zero and mean $j$. | Guide, [tail payoff discussion](../../content/incerto-scoft-ch2.md#a-probability-does-not-specify-the-tail-payoff): exact finite sums and explicit sequence of laws. This sequence is not an iid empirical-process claim. |
| CH02-C07 | Notation cautions: weak LLN under iid integrability; classical standardized CLT under iid positive finite variance (both cited); normalized power expression is not a norm for $0<p<1$ (two-vector counterexample); product-law independence, scatter/covariance distinction, and lognormal mean parameter mapping. | Guide, [notation](../../content/incerto-scoft-ch2.md#notation-at-the-point-of-use), [concept map](../../content/incerto-scoft-ch2.md#map-of-the-glossary-concepts), and [convergence](../../content/incerto-scoft-ch2.md#which-limit-is-being-taken). General theorem locators are v4 §§2.2.2–3, p. 10; lognormal calculation links the previously reviewed catalog proof. |

## Python and figures

- Helper: [glossary.py](../../src/math/incerto/glossary.py), using the existing
  installed `xmath.incerto` mapping. It exposes exact Pareto tail quantities
  and a stable normalized maximum CDF. No new dependency or package mapping.
- Demo: [glossary_worked_cases.py](../../demos/incerto/glossary_worked_cases.py),
  reusing the existing strict empirical survival and base exceedance helpers.
  Fixed sample `(1,2,2,4)`; Pareto exponents `0.8,1,1.5,3`, cutoff 1,
  thresholds `1,4,16`; maxima at exponent 1.5, counts `1,4,16,64`,
  301 points from 0.25 to 4; 161 log-spaced thresholds from 1 to 10,000
  for the corrected-tail ratio. All inputs are dimensionless. No RNG,
  external data, fitted parameters, uncertainty intervals or truncation.
- Tests: [test_incerto_glossary.py](../../tests/test_incerto_glossary.py),
  36 new cases: ties/complements, binomial enumeration, independent density
  and GPD integration, scaling, infinite moments, underflow-safe products,
  exact support, SciPy CDF comparisons, large counts, invalid inputs and overflow.
- Figures: [counts and maxima](../../assets/figures/incerto/glossary-exceedances-maxima.svg)
  and [slow variation](../../assets/figures/incerto/glossary-slow-variation.svg).
  Fixed SVG hash salt, omitted timestamps; byte-identical repeat and PNG
  previews inspected. Numerical evidence illustrates, rather than proves, limits.

Observed maximum-CDF grid errors from the Fréchet limit for counts 1, 4,
16 and 64: `0.36787944, 0.07379577, 0.01727655, 0.00425069`.
Corrected-tail multiplier ratios at 1, 10, 100 and 10,000:
`0.42328680, 0.30247005, 0.28091553, 0.26697170`.
At exponent 1.5 and threshold 4, log survival is `-2.07944154`, mean excess
8, conditional mean 12, tail first moment 1.5. Exponents at or below 1 print
mathematical infinity. All 1204 maximum-CDF and 161 multiplier values are
finite; no points were omitted. Runtime is bounded by these grids and two
exports, normally a few seconds.

## Chapter-1 reader fixes and DOI audit

The [Prologue generator](../../demos/incerto/prologue_tail_classes.py) now
uses brick circles with a wider dotted exponential curve and teal squares
with a narrower gamma curve. Marker positions alternate; data are unchanged.
Regenerated [the SVG](../../assets/figures/incerto/prologue-tail-ratios.svg)
deterministically and inspected a PNG preview. The catalog caption explains
why the ordinate difference tends to $\log2$ while both grow like $u$.
The unrelated Prologue kurtosis SVG remains byte-identical to the base.

Chapters 1–4 now use matching `Chapter N — Title` sentence-case titles in
page frontmatter, explicit TOC titles and index links. Chapter 1 already had
that form. Chapter-3/4 changes are title-only, not edition-source review.
Existing stems, base paths and `url-map.csv` are unchanged.

The existing `bingham1987regular` bibliography entry now includes
`10.1017/CBO9780511721434`. Karamata, Pareto moment existence, regular
variation, subexponentiality and the tail catalog use that local citation.
The existing Embrechts, Resnick and Coles entries also gained their already
identified DOIs, a metadata-only repair that avoids remote lookup for their
existing DOI links. This adds no theorem verification.

Inspected the pinned MyST 1.10.1 bundle: loading BibTeX registers DOI-bearing
entries in `$doiRenderers`; `transformLinkedDOIs` calls `getCitation` only
when the normalized DOI is absent. Thus a plain DOI link is not necessarily
a live dependency when a matching local entry is loaded. Source scan found
13 distinct remaining DOI-link targets: nine match local Incerto entries
(Embrechts, Resnick, Coles, Hill, Pickands, Balkema–de Haan, Davison–Smith,
Foss–Korshunov–Zachary, Chistyakov). Four lacked a loaded local entry:
Darling (1952), Politis–Romano (1994), Amari–Nagaoka (2000) and Cappé–Moulines
online EM (2009).

**Follow-up (Xiang's decision, 2026-10-18):** all four now have local entries in
`content/bibliography.bib` (`darling1952influence`, `politis1994subsampling`,
`amari2000methods`, `cappe2009online`), with fields checked against Crossref,
and the in-text links became citations. The clean build log then showed three
more live lookups that the source scan had missed: MyST also treats
`link.springer.com/book/10.1007/...` URLs as DOIs. Those three now have local
entries as well (`ay2017information`, `amari2016information`,
`jorgensen1982gig`) and are cited by key. `myst.ig.yml` and
`myst.normix-theory.yml` now load `content/bibliography.bib`. A clean rebuild on
2026-10-18 logged no "Linked … DOIs from doi.org" lines, so no build-time
doi.org fetches remain. Theme fetching on a cold cache still needs network.

## M0.5 dispositions and optional Lean

The actual chapter contract assigned 001, 006 and 009. Added 007 to this
chapter's assignment because the new guide explicitly reconciles v4 notation
and source context; the issue remains open for later chapters.

- 001: retained the corrected MLE assumptions and added their proof.
- 006: chapter-2 scope now has verified section/page context and local exact
  proofs; retained the chapter-1 classification citations. General EVT/PBDH,
  Hill and other later-chapter claim-source audits are still assigned.
- 007: new guide/concept context uses the v4 key and checked locators; no
  mechanical change to historical chapter-3/4 source references.
- 009: retained the reviewed Pareto regimes and their proof/citation status;
  the guide states which variable tends to infinity in each use.

Lean: **`skipped-for-now`**. No Lean toolchain is installed on this machine,
and the sandbox has no network. Xiang ranks Lean last. The approved
exceedance-fraction pilot remains unimplemented; no new Lean project,
declaration or checked proof is claimed. The existing imported prototype was
not touched or built.

## Verification and resume

| Check | Result |
| --- | --- |
| Plain `uv run pytest` | Blocked by read-only default cache lock. |
| `UV_CACHE_DIR=/tmp/m05-uv-cache UV_OFFLINE=1 uv run pytest` | **217 passed in 3.31s**; baseline 181 passed, 36 new cases. |
| Exceedance, glossary and Prologue demos with the same cache and `MPLCONFIGDIR=/tmp/ch02-matplotlib` | Passed; original outputs 1, 1/4, 0. All four emitted SVGs byte-identical on repeat. Three changed/new plots inspected through PNG previews. |
| `npm ci --offline --cache /tmp/m05-npm-cache --no-audit --no-fund` | Failed `ENOTCACHED` for mystmd 1.10.1. Reused local `node_modules` from `/workspace/publish-ch01-202610172003/xm`, whose lockfile is byte-identical. |
| `UV_CACHE_DIR=/tmp/m05-uv-cache UV_OFFLINE=1 npm run build` | Blocked at MyST npm preflight. Direct Node reproduction: `spawnSync /bin/sh EPERM`. No fresh HTML build. |
| `npm run check:html` | Failed after blocked build: missing pages, redirects and subsite configs. Four pre-existing unresolved legacy rows remain skipped. |
| State, source links, TOC/citation membership and whitespace | Passed documented state validator (992 plan links), 366 relative links across 28 changed/new files, all 45 Incerto TOC entries, 69-page/65-redirect source layout, matching chapter-1–4 titles, citation keys, figure paths/XML and `git diff --check`. All seven new files separately checked for trailing whitespace/final newlines. |
| Rendered equations, browser desktop/mobile, deployment and live reader review | Not performed; no fresh HTML artifact. Figure previews do not substitute for page rendering. |
| Wheel/import-isolation build and Lean | Not run; package mapping unchanged, Lean explicitly skipped. Installed helper imports exercised by tests/demos. |

Reviewed the full new teaching/code/test/record files and all tracked diffs;
checked formulas and the public prose pass against their stated hypotheses.
Manual source comparison found no copied or close-paraphrased book prose;
a normalized nine-word overlap scan of new/added teaching and Python text
against the supplied chapter found no matches. The scan supplements that
review, rather than proving originality. SVG normalization is part of the
generators, so a rerun preserves both the artifact bytes and whitespace checks.
Confirmed unchanged shared notation, URL map, dependency locks and package
mapping; no staged changes or file deletions.

State marks `scft-v4-ch02` implementation done and selects `scft-v4-ch03`
as requested. The Pareto, EVI and tail-catalog concepts remain in progress
for later chapter scopes. The max review below is complete; an external
site build/check precedes publication, then Math Site Editor reviews the live
changed pages. No publication is asserted here.

## Max-reasoning math review

Reviewed 2026-10-17 by owner-selected gpt-6-astra at MAX reasoning, on the
uncommitted `scft/v4-ch02` worktree. Read the root/Incerto guidance, shared
notation canon, [program notation lock](../plan/incerto-program/architecture.md#urls-notation-and-publication-boundaries),
and proof-writing skill first. Followed the
[chapter-1 review procedure](incerto-scft-v4-ch01.md#max-reasoning-math-review):
inspected all 21 tracked-file diffs and all seven untracked files, derived
the claims independently, checked sources and numerical boundaries, and
reviewed the figures. This closes mathematical review, not site publication.

| Claim | Verdict | Method and scope |
| --- | --- | --- |
| CH02-C01 — Strict counts, indicator moments and Chebyshev | correct | The two indicator events partition each observation, including threshold atoms; bounds and monotonicity follow by counting and set inclusion. For fixed nonrandom $u$, iid indicators are Bernoulli with $q=\bar F(u)$, including $q=0,1$. Summing variances gives $q(1-q)/n$ and Chebyshev applies for every $\varepsilon>0$. Exact rational enumeration of Bernoulli outcomes verifies the moments and strict tail events. No moment of $X$, random-threshold guarantee or uniform theorem is used. |
| CH02-C02 — Conditional Pareto/GPD law, moments and tail integral | correct | Dividing positive Pareto survivals gives $(1+y/u)^{-\alpha}$ for $u\ge x_m>0$, $y\ge0$; matching the GPD form gives shape $1/\alpha$ and scale $u/\alpha$. Its integral is $u/(\alpha-1)$ for $\alpha>1$, with logarithmic divergence at 1 and power divergence below 1. Adding $u$ gives the conditional mean. The pointwise positive-part identity and Tonelli prove the tail first-moment identity in extended nonnegative reals, including atoms and $u=0$. Checked density and GPD integrals, discrete atoms, rescaling and the exact example $(1/8,8,12,3/2)$. |
| CH02-C03 — Known-cutoff MLE and zero denominator | correct | Reconstructed the exact density likelihood: $\ell=n\log\alpha-\alpha D+\mathrm{constant}$. For $D>0$ its derivative changes sign at $n/D$, its second derivative is negative, and both parameter endpoints give smaller likelihood. When $D=0$, all observations equal $x_m$ and $\ell\to\infty$ with $\alpha$. Checked $n=1$, mixed cutoff/interior observations, independent numerical maximization and SciPy's fixed-cutoff fit. The existing helper's all-cutoff mean is a limiting convention, not a finite exponent MLE. |
| CH02-C04 — Exact maximum CDF, Fréchet limit and EVI normalization | correct | Independence yields $F(c_ny)^n$ with cutoff $y=n^{-1/\alpha}$; the CDF is zero at and below that cutoff. For each fixed $y>0$, the logarithmic limit gives $\exp(-y^{-\alpha})$; for $y\le0$ it is zero. The transformation $z=\alpha(y-1)$ gives $a_n=c_n/\alpha$, $b_n=c_n$, and $H_{1/\alpha}$, including its lower endpoint. Also checked $F(r)^n\to0$ for $r<x_F$: endpoint approach supplies no normalized-limit theorem. High-precision population CDFs and SciPy GEV values agree. The Python boundary defect is recorded separately below. |
| CH02-C05 — Log-corrected survival and divergent slowly varying factor | correct | The survival is continuous, nonincreasing, between zero and one, and has the required limits at both infinities. Its density on $(1,\infty)$ is $x^{-3}(1+2\log x)$ and integrates to 1. For each fixed $t>0$, eventually $x,tx\ge1$ and the exact ratio tends to $t^{-2}$, while $L(x)=1+\log x\to\infty$. Checked multipliers below and above 1 and all 161 plotted values. Slow variation does not impose a finite constant limit or an exact finite Pareto transition. |
| CH02-C06 — Expected shortfall at atoms and CDF/mean counterexample | correct | For $v=Q(q)$, splitting the quantile integral gives $\int_q^1Q(s)ds=\mathbb E[X\mathbf1_{\{X>v\}}]+v(F(v)-q)$. If there is no atom at $v$, then $F(v)=q$, giving the strict conditional tail mean. With $(1,2,2,4)$ at $q=1/2$, the atom correction gives 3, while strict conditioning gives 4. Exact interval sums verify this and other levels. For $P_j$, the CDF discrepancy equals $1/j$ throughout $[0,j^2)$, and its mean equals $j$. This sequence is not an iid empirical process. |
| CH02-C07a — Notation and elementary qualifications | correct | The normalized $p$ expression is $n^{-1/p}$ times the usual norm for $p\ge1$; the two-vector example violates the triangle inequality for $0<p<1$. Product-law independence is stated for measurable sets; density ratios require densities and a positive denominator. Elliptical scatter need not be covariance, which additionally needs second moments and normalization. Rechecked the lognormal mean mapping by Gaussian integration, stable-index range against §2.1/§2.2.9, the three convergence definitions, and the distinction between fixed-$n$ tail limits, growing-$n$ sums, and moment order. All source-specific symbols are qualified against the canon. |
| CH02-C07b — Weak LLN and classical CLT | cited-ok | Read v4 §§2.2.2–3, printed p. 10 (PDF page 24). The LLN assumes iid Lebesgue-integrable variables, equivalent here to $\mathbb E|X_1|<\infty$. The CLT assumes iid finite variance; the guide explicitly requires positive variance before dividing by $\sigma$. Its standardized formulation follows from the source's variance-$\sigma^2$ Gaussian limit. These theorems are cited, not purportedly proved or assigned a universal finite-sample rate. |
| CH02-C08 — Demos, figures and tail-ratio caption | correct | Verified the strict empirical step heights/open and closed endpoints, exact maximum curves and all printed tables. Recomputed all 1205 Prologue log ratios independently. For the plotted rate-1 exponential and shape-2/rate-1 gamma, the ordinates are $u$ and $u-\log[(1+2u)/(1+u)]$; their positive gap tends to $\log2$, while their relative gap vanishes. Markers, widths and colors change appearance only. Inspected all three changed/new figure previews; regenerated all four emitted SVGs byte-identically to the input worktree. |
| CH02-PY01 — Numerical boundary behavior and API description | corrected | The maximum helper erased representable positive CDFs immediately above its support. Added stable `expm1` evaluation near the support and an 80-digit standard-library Decimal calculation only where the two logarithms cancel for $n>1$. Retained `log1p` for small tail probabilities at large $n$. Four regression cases and independent high-precision checks now pass. Clarified that positive expectations may underflow, whereas overflow raises; corrected the API table from “probability” to “log survival.” No mathematical formula or dependency changed. |

The new guide's remaining entries were checked as definitions, source-to-note
routes or explicitly planned topics. They do not assert proofs of general
EVT/PBDH, multivariate tail dependence, Kappa, hedging or interpretive claims.
The reused Pareto growing-sample regimes and catalog classification proofs
retain the preceding M0.5/chapter-1 review scope. Title and local citation
edits add no new theorem-source certification.

Corrections and verification:

- **Reproduced numerical defect:** with $n=1$, $\alpha=0.1$ and
  `y=nextafter(1, +inf)`, the previous helper returned zero instead of
  approximately `2.220446049250313e-17`. At $\alpha=1$, one float above
  $1/n$ for $n=8,16$, cancellation also returned zero instead of
  `5.909106315383e-126` and `3.491753744650e-251`. The revised helper
  preserves those values and exact support endpoints. Tests also retain the
  large-count case $n=2^{53}$. Ordinary underflow/rounding remains possible
  at the floating-point limits, as documented.
- `UV_CACHE_DIR=/tmp/m05-uv-cache UV_OFFLINE=1 uv run pytest`:
  **221 passed in 3.42s**, including 40 glossary cases (36 original plus
  four regressions). Installed imports resolve to this worktree.
- `/tmp/ch02-max-review/numerical_review.py`: **10,516 comparisons/assertions
  passed**, using NumPy 2.4.6, SciPy 1.18.1 and cached mpmath 1.4.1 at
  80 digits. Checks include exact Bernoulli enumeration, Pareto/GPD density
  integration, likelihood derivatives/optimization, atoms, support-adjacent
  floats, non-dyadic cutoffs and counts through $2^{53}$. All 1204 maximum
  figure values agree with high precision; maximum absolute error is below
  `3.2e-16`. Tiny tail probabilities were factored out before quadrature
  to avoid an absolute-integration-tolerance artifact. SciPy's extreme GEV
  reference evaluation emitted an overflow warning while returning the
  expected zero CDF; the checked helper results were finite.
- Reran the exceedance, glossary and Prologue demos with that offline cache
  and `MPLCONFIGDIR=/tmp/ch02-max-review/matplotlib`. Tables and grid counts
  match the pages; the four SVG hashes match their pre-review versions.
  Inspected PNG previews of the two glossary figures and tail-ratio figure,
  and parsed their full SVG trees.
- The current documented state validator passed, including 993 plan
  file/fragment links. Source checks passed for all 28 changed/new files,
  369 relative Markdown links, citation keys, figures, TOC membership and
  the 69-page/65-redirect source layout. `git diff --check` and separate
  whitespace/final-newline checks of all seven untracked files passed.
  Shared notation, URL map, dependency locks and package mapping are unchanged.

Source verification:

- Independently extracted and read the supplied read-only
  `/workspace/scoft-toc/2001.10488v4.pdf`, printed pp. 7–21 (PDF pages
  21–35), and compared the TOC. Every glossary table locator and new concept
  locator agrees, including the continuations on pp. 11, 13–14, 16–18 and 19–20.
  The [versioned arXiv record](https://arxiv.org/abs/2001.10488v4) confirms
  the 2025 third edition. The source's empirical indicator on p. 19 is
  non-strict survival; the guide correctly uses a right-continuous CDF and
  strict survival instead.
- Manual wording comparison found no copied or close-paraphrased book prose.
  Exhaustive normalized five-word and nine-word scans of changed additions
  and complete untracked text against all 15 chapter pages found no matches.
  Source extracts and scratch scripts remain under `/tmp`; figures are
  generated from repository-owned model code, without source images.
- Added DOI metadata matches the publisher records for
  [Bingham–Goldie–Teugels](https://www.cambridge.org/core/books/regular-variation/A71D6C4A65CFC1806E1DB7109128A358),
  [Embrechts–Klüppelberg–Mikosch](https://link.springer.com/book/10.1007/978-3-642-33483-2),
  [Resnick](https://link.springer.com/book/10.1007/978-0-387-45024-7), and
  [Coles](https://link.springer.com/book/10.1007/978-1-4471-3675-0).
  These are bibliographic checks, not fresh verification of those books'
  general theorems.

No mathematical item needs Xiang's decision. Site build, HTML/browser review,
wheel build and Lean were not rerun; the external build and post-publication
reader gates above remain open. This review changed the glossary helper,
its tests, the API description and review records/status only. No files were
deleted, staged or committed.

## Operator rerun outside the sandbox (2026-10-17, America/New_York)

On this branch's working tree (base `cbda449`), clean `_build/`:

| Check | Result |
| --- | --- |
| `uv run pytest -q` | pass: 221 passed, 43 subtests passed |
| `npm ci` | pass |
| `npm run build` | pass, first attempt (Karamata reference now resolved from the local bib entry); rerun 2026-10-18 after the DOI and title follow-up: pass, no doi.org lookups |
| `npm run check:html` | pass: 69 pages across four sites, 65 redirects, 54 pages with display math; 4 pre-existing unresolved legacy url-map rows skipped |

The Math Site Editor's live reader review of the new and changed pages is due after publication.
