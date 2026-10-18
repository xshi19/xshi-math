# SCoFT v4 chapter 3 implementation

Date: 2026-10-18 (America/New_York). Branch: `scft/v4-ch03`.
Base: `697d55a7ec3d6a019308d4a9a6043e5a7485fcfa` (`origin/main`).
Owner-selected model: gpt-6-astra, xhigh. No subagents, commit or deployment.
The owner-requested gpt-6-astra max review is completed below.

## Source and teaching scope

Read the supplied read-only `/workspace/scoft-toc/2001.10488v4.pdf`,
chapter 3, printed pp. 25–68 (PDF pages 39–82), and `v4-toc.txt`.
Also read appendix E.1, printed p. 191 (PDF page 205), to check the
guide's existing restriction on the exponent estimate. Extraction included
the preceding part divider and the following blank appendix page; these
are not additional claim sources. Extracts stayed in `/tmp`.

Read the attached [precaution paper, arXiv:1410.5787v1](https://arxiv.org/pdf/1410.5787v1)
at §II.B/III, pp. 2–3, and §VII.A–C, p. 6. The selected scope is absorbing
failure, repeated exposure, nonlinear damage and finite dependence models.
Its institutional, biological, medical and policy claims are excluded.
The paper's repeated-risk discussion needs explicit conditional-hazard
conditions; our note supplies them and a counterexample when hazards are
positive but summable. No general network or contagion theorem is asserted.

Updated the existing [chapter 3 guide](../../content/incerto-scoft-ch3.md)
in place. Its title remains **Chapter 3 — Non-technical overview** and its
route remains `/math/incerto/incerto-scoft-ch3/`. It maps v4 sections and
the consequence list to mathematical questions, original models and existing
notes. Appendix E.1's conditioning restriction is retained with its verified
v4 locator; its displayed estimator densities are not certified here.
The original adaptation/MIT notice remains. No source prose, figures, PDF
or extract was imported.

Four new canonical concept pages provide the chapter's teaching:

- [Inference asymmetry](../../content/incerto-inference-asymmetry.md):
  product-law contamination bound, testing consequence, disjoint-support
  equality, arbitrary mean gaps and the contrast with bounded payoffs.
- [Asymmetric payoffs](../../content/incerto-asymmetric-payoffs.md):
  finite gain/loss table, differentiable Jensen proof, exact power-tail
  transform, cap calculation and an explicit downside-bound distinction.
- [Ruin](../../content/incerto-ruin.md): constant and conditional hazards,
  an infinite-product criterion, counterexamples, ensemble/path difference
  and an absorbing additive resource example.
- [Decentralization](../../content/incerto-decentralization.md): convex
  damage splitting, exact Pareto scale effects, and independent versus
  common-block Bernoulli losses. Model scope is explicit at every comparison.

Teaching was drafted before the Python helper, demo and tests. The inference
note proves its needed mean comparison directly, leaving the full
`c-moment-estimation` treatment for chapter 4. It does not create an empty
prerequisite page or advance another chunk. General ergodicity stays with
its later concept; chapter 3 proves only its explicit absorbing example.

New pages are in the Incerto TOC, theorem/method indexes, track hub,
SCoFT overview and regenerated concept graph. The API index lists the
helper module. Source membership is 49 Incerto pages, 73 pages overall,
and 69 flat redirects; those are source counts, not an HTML build result.
Shared notation, dependency locks, package mapping, URL map and base paths
are unchanged. The graph generator refreshes its other current source
references as well as adding the four nodes.

## Hard mathematics for the separate max review

Review these statements and proofs independently of the numerical evidence.
The public pages distinguish their own proofs from source context and
results proved in linked prerequisites.

| ID | Claim and assumptions | Teaching location |
| --- | --- | --- |
| CH03-C01 | For $Q=(1-\varepsilon)P+\varepsilon R$, iid size-$n$ sample TV is at most $1-(1-\varepsilon)^n\le n\varepsilon$; every measurable $[0,1]$-valued test obeys the corresponding power bound. Disjoint uniform/Pareto supports attain equality. | [Contamination proof](../../content/incerto-inference-asymmetry.md#inference-contamination), [equality](../../content/incerto-inference-asymmetry.md#inference-separated-tails) |
| CH03-C02 | With fixed $n$ and arbitrarily small sample TV, a rare Pareto component can produce an arbitrarily large finite mean gap and infinite second moment. Quantifiers allow the alternative to vary; a fixed positive mixture weight is eventually detected. A payoff in $[0,B]$ has expectation discrepancy at most $\varepsilon B$. | [Mean gap](../../content/incerto-inference-asymmetry.md#inference-separated-tails), [bounded payoffs](../../content/incerto-inference-asymmetry.md#inference-bounded-payoffs) |
| CH03-C03 | Finite gain frequency need not order means. Under the stated interval/differentiability/integrability assumptions, the supporting-line proof gives Jensen and its concave reverse; equal variance does not order all convex expectations. Exact Pareto $X^r$ has exponent $\alpha/r$ and finite mean iff $r<\alpha$; capping a nonnegative payoff gives all exponential moments. | [Payoff note](../../content/incerto-asymmetric-payoffs.md#payoffs-hit-rate), [Jensen](../../content/incerto-asymmetric-payoffs.md#payoffs-jensen), [tail transform](../../content/incerto-asymmetric-payoffs.md#payoffs-tail-transform) |
| CH03-C04 | Constant independent ruin probability gives $(1-q)^N$ survival. Conditional hazards give a product without independence. For all $h_k<1$, eventual ruin is certain iff $\sum h_k=\infty$; a reached unit hazard is a separate case. The displayed summable sequence leaves survival $1/2$; fixed marginals alone do not imply eventual ruin. | [Ruin and hazards](../../content/incerto-ruin.md#ruin-constant-hazard), [criterion and counterexamples](../../content/incerto-ruin.md#ruin-varying-hazard) |
| CH03-C05 | With $W_k=W_0a^k\mathbf1_{T>k}$, constant $0<q<1$ and $a(1-q)>1$, ensemble expectation diverges while almost every path is eventually zero and its Cesàro resource average tends to zero. The absorbing additive model makes payoff order matter. | [Ensemble and time calculation](../../content/incerto-ruin.md#ruin-ensemble-time) |
| CH03-C06 | Convex nonnegative $h$ with $h(0)=0$ obeys $mh(z/m)\le h(z)$. Additive local power damage under a fixed common shock scales by $m^{1-r}$; pooling before applying the response removes that benefit. | [Convex scale proof](../../content/incerto-decentralization.md#decentralization-convex-scale) |
| CH03-C07 | For an exact Pareto shock, split power damage has survival $(d_m/u)^{\alpha/r}$ on support, unchanged tail exponent, and finite mean iff $\alpha>r$. Above both minima the tail-probability ratio is $m^{-\alpha(r-1)/r}$. | [Damage tail calculation](../../content/incerto-decentralization.md#decentralization-pareto-tail) |
| CH03-C08 | Equal-exposure independent Bernoulli modules have mean $aq$, variance $a^2q(1-q)/m$, total-failure probability $q^m$ and any-loss probability $1-(1-q)^m$. Common shocks preserve the mean but change the latter quantities; the number of independent blocks determines the intermediate model. | [Finite dependence comparison](../../content/incerto-decentralization.md#decentralization-dependence) |

The guide's additional caveats retain ordinary definitions: iid integrable
sample means are unbiased; finite samples do not prove moment existence;
Gaussian events of extreme size have positive probability; unknown bounded
supports cannot be ruled out by one finite observation. General limit
theorems remain with their linked, previously reviewed concept pages.

## Python and figures

Helper: [lecture_risk.py](../../src/math/incerto/lecture_risk.py).
Demo: [lecture_risk.py](../../demos/incerto/lecture_risk.py).
Tests: [test_incerto_lecture_risk.py](../../tests/test_incerto_lecture_risk.py).
The installed `xmath.incerto` mapping is unchanged. The six helpers expose
finite probability, payoff, absorbing-path and exact damage-law calculations.
Validation rejects nonfinite or out-of-domain inputs. Integer counts are
bounded by $2^{53}$; probabilities use `log1p`/`expm1`, damage stays in log
space, and block variance combines scales in log space. Numerical underflow
is documented; the code does not turn a mathematical infinite mean into a
finite estimate.

The demo uses no RNG, external data, fitting or sampling uncertainty.
Inputs are dimensionless: 161 mixture probabilities from $10^{-6}$ to
$10^{-2}$ at sample sizes 100, 1000 and 10000; 121 symmetric spreads
from 0 to 3 around 4; 401 survival horizons and 201 resource horizons;
161 damage thresholds from 0.01 to 100 for module counts 1, 4 and 16;
40 independent-block counts at failure probability 0.02. Runtime is normally
a few seconds; grid endpoints do not truncate any distribution.

Original deterministic SVGs:

- [Inference and payoffs](../../assets/figures/incerto/lecture-inference-payoffs.svg).
- [Ruin](../../assets/figures/incerto/lecture-ruin.svg).
- [Scale and dependence](../../assets/figures/incerto/lecture-scale-dependence.svg).

Key printed values: contamination probability 0.0001 at $n=1000$ gives
detection `0.095167106`, while the contaminated mean is `300.49995`
versus `0.5`; finite payoffs have means `-0.62` and `0.62`; ruin at
$q=0.02$, $N=100$ is `0.8673804441`; summable-hazard survival at
$N=400$ is `0.501246883`; ensemble resource growth factor is `1.0192`;
ten independent blocks give total failure `1.024e-17` and any loss
`0.1829271931`. All plotted values are finite and none is omitted.

The 44 new test cases use exact rational enumeration of sample laws and
Bernoulli damage, a specified finite ruin-time law, telescoping survival,
payoff cancellation, absorbing-order examples, SciPy Pareto quantiles,
independent density/tail integrals, rare-probability and scaled-variance
boundaries, and invalid inputs. The first run found a one-trial result one
ulp below its input probability; returning that input directly resolved
the boundary case. No test or finite grid substitutes for the proofs above.

## Chapter-2 reader fixes

Audited every `[@key]` occurrence in `content/*.md`, including multiline
paragraphs and reference lists. Changed 19 existing files for duplicated
author/year wording, plus the chapter-3 rewrite. Narrative `@key` now owns
the author/year when titles follow it; the Darling theorem uses
`[@darling1952influence, Theorem 5.1]`. This covers Bingham–Goldie–Teugels,
Politis–Romano, Ay et al., Amari–Nagaoka, Amari 2016, Jørgensen,
Cappé–Moulines and analogous local book/data references. Keys and
bibliographic metadata are unchanged. Historical source years outside
chapter 3 were not mechanically upgraded. These are citation presentation
changes, not new certifications of the referenced mathematics.

The [tail-ratio generator](../../demos/incerto/prologue_tail_classes.py)
already used automatic legend handles with the plotted dash patterns.
The theme's 1.8-em handle ended before the Weibull dot became visible.
Increasing this figure's handle length to 4.8 em shows a full cycle.
Verified all five handles against their lines for dash pattern, color,
width and marker, and inspected the regenerated PNG preview. Numerical
curves are unchanged; the unrelated kurtosis SVG remains byte-identical.

## M0.5 dispositions, checks and resume

- **005:** chapter-3 wording and delivered-concept links are updated.
  The historical M0.5 live pass stays closed; the new edits await their own
  post-publication reader review.
- **007:** chapter-3 scope is pinned to `taleb2025scoftv4` with checked
  chapter/section/page locators, including appendix E.1's restriction.
  Later chapter assignments remain open.
- **Lean:** `skipped-for-now`. No toolchain is installed and sandbox network
  is unavailable. No project, declaration or checked proof was added;
  the imported prototype was not built.

| Check | Actual result |
| --- | --- |
| Plain `uv run pytest` | Failed to acquire a lock in the read-only default uv cache. |
| `UV_CACHE_DIR=/tmp/m05-uv-cache UV_OFFLINE=1 uv sync --locked` | Passed from the existing writable cache; installed this checkout. |
| `UV_CACHE_DIR=/tmp/m05-uv-cache UV_OFFLINE=1 uv run pytest` | **265 passed in 3.09s**, including 44 new cases. |
| Concept graph tests after regeneration | **10 passed in 0.83s**. |
| Chapter-3 and Prologue demos | Passed; finite tables/grids checked. Deterministic SVG repeat and PNG previews reviewed. |
| `npm ci --offline --cache /tmp/m05-npm-cache --no-audit --no-fund` | Failed `ENOTCACHED` for MyST 1.10.1. Reused `node_modules` from `/workspace/pub-math-1792333606` after verifying byte-identical `package-lock.json`. |
| `UV_CACHE_DIR=/tmp/m05-uv-cache UV_OFFLINE=1 npm run build` | Blocked by MyST's npm preflight; direct `child_process.execSync("npm --version")` reproduces `EPERM spawnSync /bin/sh`. No fresh HTML build completed. |
| `npm run check:html` | Failed on missing fresh pages/configuration after the blocked build. The legacy portion checked 64 compatibility pages for 65 mapped rows and skipped four pre-existing unresolved rows. |
| State, links, source membership, citations and whitespace | Passed the documented state validator (1001 plan file/fragment links) and source audit: 48 changed/new files, 11 new files, 833 relative file/fragment links, 55 local citation references, matching chapter titles, complete TOC membership, SVG XML and whitespace checks. |
| Browser equations, citation appearance, desktop/mobile navigation, publication and live review | Not performed; no fresh HTML artifact or deployment. Plot previews are separate evidence. |
| Wheel build and Lean | Not run; package mapping unchanged, Lean explicitly skipped. |

State marks `scft-v4-ch03` implementation done and advances `next_chunk`
to `scft-v4-ch04`, as requested. The four concepts and attached paper are
complete only at the implemented mathematical scope. The M0.5 denominator
remains 24 reviewed bodies; the current implemented concept count is 28.
The validator distinguishes pages created in this chunk from pages reused
at its start. The max review below is complete; a successful external site build/check
and a later live reader review remain open. No decision from Xiang is
needed for this implementation.

Final source review: reviewed tracked diffs and complete new teaching, code,
test and record files; inspected the generated graph/fallback changes and
four new/changed figure previews. No normalized nine-word overlap was found
between the five chapter-3 teaching pages and the supplied chapter; manual
review also found no copied or close-paraphrased source prose. The automatic
scan supplements that review. All 13 remaining parenthetical-citation
occurrences across `content/*.md` were checked for duplicated author/year
prose. Bibliographic keys/metadata are unchanged.

Eight later chunk records now list the newly available payoff/ruin pages as
reusable prerequisites. Their statuses, source assignments and deliverables
remain unchanged; no later chapter was executed. All 48 changes are unstaged,
with no deletions, commit, push or publication. Logs and scratch checks remain
under `/tmp/ch03-*`; they are not repository deliverables.

## Max-reasoning math review

Reviewed 2026-10-18 by owner-selected gpt-6-astra at MAX reasoning on the
uncommitted `scft/v4-ch03` worktree. Read root/track guidance, the shared
notation canon and [program notation lock](../plan/incerto-program/architecture.md#urls-notation-and-publication-boundaries),
and the proof-writing skill first. Followed the
[chapter-1](incerto-scft-v4-ch01.md#max-reasoning-math-review) and
[chapter-2](incerto-scft-v4-ch02.md#max-reasoning-math-review) procedure:
reviewed all 37 tracked-file diffs and all 11 new files, independently
derived the claims, checked numerical boundaries and sources, and inspected
the figures. This closes the separate mathematical review; it does not
close the site-build or live reader-review gates.

| Claim | Verdict | Method and scope |
| --- | --- | --- |
| CH03-C01 — Product total variation and testing | correct | Conditioning on whether any component selector chooses R gives the stated product-law mixture, with weight d = 1 − (1 − ε)^n. This bounds every event and every measurable randomized test in [0,1]; the union bound gives d ≤ nε. For the disjoint uniform/Pareto supports, the event max X_i > 1 attains d. Exact rational enumeration checked disjoint, overlapping and identical component laws, randomized tests and the maximizing rejection event. The rejection level is under the baseline sample law. |
| CH03-C02 — Mean gaps, moments and bounded-payoff contrast | correct | For any fixed n and η > 0, choose ε ≤ η/n and then b > 1 sufficiently large; α may be fixed at 3/2. Both means are finite, their gap is ε(αb/(α−1) − 1/2), and the second moment of Q is infinite when 1 < α ≤ 2. Fixed ε is eventually detected. The one-draw mixture gives εB for [0,B] payoffs and 2εB for signed bounded payoffs. Common uniform integrability excludes the unbounded mean-gap family: truncate at a common cap, bound the truncated difference, then control both tail remainders. Density integration and high-precision arithmetic verify the worked mean and no-contamination probability. Linearity proves sample-mean unbiasedness; no variance assumption is needed. |
| CH03-C03 — Gain frequency, Jensen, transforms and caps | correct | Direct finite sums give −0.62 and 0.62. The supporting line at the finite interior mean is integrable under the stated hypotheses, proving differentiable Jensen; applying it to −g gives the concave case. Recomputed the square-root example, quadratic changes ±s², and the equal-variance laws' opposing absolute/fourth moments. Event inversion gives Pareto exponent α/r and the density integral gives mean existence iff r < α, including logarithmic divergence at equality. Tonelli gives the capped tail integral and mean 2; the cap bounds every real exponential moment. The strictly convex e^x+x has unbounded negative downside, whereas the displayed call-shaped payoff is bounded below by −d. Numerical integrations and finite sums agree. |
| CH03-C04 — Survival products and hazard criterion | correct | Independence proves constant-q survival; continuity from above proves the infinite-horizon limit, with q = 0, q = 1 and N = 0 treated separately. The conditional chain rule needs no independence. If every reached h_k < 1, the two logarithmic bounds prove that the product is zero iff Σh_k diverges; a reached unit hazard is a separate terminating case. The positive summable sequence telescopes to (N+2)/(2(N+1)), leaving survival 1/2. A shared Bernoulli failure indicator has constant marginal failure probability but zero hazards after surviving step 1. Checked exact finite ruin-time laws, all plotted hazards and a nonsummable 1/(k+1) sequence with survival 1/(N+1). |
| CH03-C05 — Ensemble growth and almost-sure termination | correct | Indicator expectation gives E W_k = W_0[a(1−q)]^k. Under 0 < q < 1, T is finite almost surely, leaving only finitely many finite nonzero path terms, so the Cesàro resource average tends to zero. If a(1−q) > 1, both ensemble resources and their expected Cesàro averages diverge; this is a counterexample to exchanging expectation and path limits, without an ergodic-theorem claim. Recomputed 1.0192, finite survival-state expectations and the absorbing additive paths (3,0,0) and (3,7,3). |
| CH03-C06 — Convex splitting and power damage | correct | Apply convexity to z/m = (1/m)z + (1−1/m)0, then multiply by m. Nonnegative finite h and h(0)=0 give the stated inequality for z ≥ 0, including z = 0 and m = 1. Substitution gives the pathwise factor m^(1−r) under the common shock. Pooling before the nonlinear response removes the reduction. Linear and concave powers have the stated equality/reversal. These comparisons fix the response function, total input and additive damage rule. |
| CH03-C07 — Damage survival, ratio and moment threshold | correct | D_m has minimum d_m = a^r m^(1−r)x_m^r. Inverting D_m > u gives survival 1 below the minimum and (d_m/u)^(α/r) at and above it; continuity gives survival 1 at the minimum. For u above both minima, dividing survivals gives m^(−α(r−1)/r). Every finite m retains exponent α/r, hence the same strict mean threshold α > r. Verified the 1/16 path factor, 1/8 tail ratio and infinite means at α = 3/2, r = 2. Independent density/tail integrals and high-precision event inversion agree. The numerical implementation defect is separate below. |
| CH03-C08 — Independent and common-block losses | correct | Bernoulli moments, independence and the all-fail/all-survive intersections give the four formulas. Perfect dependence retains mean aq and gives variance a²q(1−q), with either failure event having probability q. Equal-exposure independent blocks have a scaled binomial law indexed by the actual block count. Exact enumeration and SciPy binomial calculations verify the distributions, moments, 1.024×10^−17 and 0.1829271931. Boundedness holds for every dependence pattern; no heavy-tail or contagion conclusion follows. |
| CH03-Q01 — Gaussian rejection wording and guide qualifications | corrected | Changed “a large observation under a Gaussian has positive probability” to positive exceedance probability beyond each finite threshold for a nondegenerate Gaussian. Exact Gaussian observations are singleton events of probability zero. The unknown-bound and known-uniform-support distinctions are valid. The guide's unbiasedness, strict Pareto moment boundary, restricted ξ = 1/α identity, scale/standard-deviation caveat and four worked models agree with the concept pages. Its remaining consequence entries are questions or explicitly deferred subjects, not general theorems. |
| CH03-PY01 — Helpers and numerical boundaries | corrected | The damage helper lost its transformed minimum through cancellation at large powers, and lost the log distance to the cutoff at very small powers or adjacent floating-point thresholds. Regrouped the minimum and used standard-library Decimal refinement for cancellation and near-support evaluation. Added 12 regression cases, retaining exact support endpoints, scalars/arrays and the existing validation behavior. The other five helpers agree with their finite-law definitions; endpoint, rare-probability, hazard-one, absorbing-order and extreme scaled-variance cases pass. |
| CH03-S01 — Source context and citation presentation | cited-ok | Checked v4 chapter 3 and appendix E.1 locators against the supplied PDF, and the precaution paper at its pinned v1 sections. These are context/restriction citations; the original proofs above do not depend on the source's policy assertions or appendix estimator densities. Existing citation-form edits preserve all mathematical spans, citation-key counts, locators and bibliographic metadata. Inspected all 39 citation-containing paragraphs, including all 13 remaining parenthetical occurrences: no duplicated author/year wording remains. This does not recertify every unchanged cited theorem. |
| CH03-F01 — Demos, SVGs and Weibull legend | correct | Checked every chapter-3 plotted curve against independent formulas and reviewed all four changed/new figure previews, labels, scales and captions. They show deterministic population quantities, not simulation or empirical evidence. Regenerated the three new SVGs and both Prologue SVGs byte-identically to their input versions. All 1205 Prologue curve values agree with high precision; all five automatic legend handles match line dash pattern, color, width and marker. The 4.8-em handle includes a full Weibull dash-dot cycle. |

Corrections and numerical evidence:

- **Reproduced damage defect:** with `alpha=power=1e16`, `modules=2`,
  `exposure=2`, `x_m=1`, the exact damage minimum is 2 and its exponent
  is 1. At threshold 2, the original helper returned `−log(2)` (survival
  1/2) instead of zero (survival 1). At threshold 4 it returned `−log(4)`
  instead of `−log(2)`. A second example, `power=1e-308`, `alpha=1`,
  `modules=2`, `exposure=x_m=1`, has `P(D_m>2)=1/2`, but the original
  helper returned log survival zero. The revised calculation preserves
  both examples and the log tail immediately above a representable cutoff.
  The regression cases include powers through `1e308`, tiny powers down
  to `1e-308`, and a one-float excess above 3 with large tail exponent.
  Refinement uses 80 decimal digits, increased when a tiny power requires
  it; no runtime dependency or package mapping changed. Ordinary floating
  rounding, underflow and rejection of unrepresentable transformed
  parameters remain documented limitations.
- The first full test run after refinement caught a decimal-rounding
  residual at an exact support endpoint. Forming the high-precision
  threshold/minimum ratio before taking its logarithm resolved it;
  existing endpoint assertions remain exact rather than relaxed.
- `UV_CACHE_DIR=/tmp/m05-uv-cache UV_OFFLINE=1 uv run pytest`:
  **277 passed in 3.32s**, including 56 chapter-3 cases (44 original and
  12 regressions). Confirmed imports resolve to this worktree.
- `/tmp/ch03-max-review/numerical_review.py`: **9450 comparisons/assertions
  passed**, using NumPy 2.4.6, SciPy 1.18.1 and cached mpmath 1.4.1 at
  100 decimal digits. The maximum error divided by 1+|reference| was
  below `9.0e-14`. Checks include exact rational product laws, finite
  expectations, independent density/survival integration, conditional
  hazards, every chapter-3 figure grid, transformed-support boundaries,
  block counts through `2^53` and subnormal probabilities. These finite
  checks supplement the proofs of divergence and almost-sure statements.
- The figure audit made another **1225 comparisons/assertions**: 1205
  independent Prologue ordinates and 20 legend-property comparisons.
  Its maximum normalized ordinate error was below `2.3e-15`. Parsed the
  full SVG trees and inspected freshly generated PNG previews. All five
  SVG hashes are unchanged by this review.

Source and repository checks:

- Independently extracted the supplied read-only
  `/workspace/scoft-toc/2001.10488v4.pdf`: chapter 3, printed pp. 25–68
  (PDF pages 39–82), and appendix E.1, printed p. 191 (PDF page 205).
  Checked all reading-map section ranges, the 17 consequence locations,
  §§3.4.1, 3.6.1, 3.10–12, the source-specific S/L/F notation and the
  appendix's strict conditioning restriction. The
  [versioned arXiv record](https://arxiv.org/abs/2001.10488v4) confirms the
  third edition and 2025 source identity. No claim about the appendix's
  displayed estimator densities is added.
- Read the [precaution paper v1](https://arxiv.org/pdf/1410.5787v1),
  §II.B/III, pp. 2–3, and §VII.A–C, p. 6. The absorbing-state and
  nonlinear-response context matches the notes. The local hazard
  criterion supplies conditions absent from the paper's unqualified
  repeated-risk wording; the summable/common-shock examples limit that
  wording. The notes exclude the paper's institutional and policy claims.
- Manual comparison found no copied or close-paraphrased chapter prose.
  A normalized nine-word scan of the 44 non-SVG text files in the
  48-file diff found no matches. Five-/seven-word matches were source/chapter titles or generic
  mathematical phrases, such as “the moment of order p”; none was copied
  exposition. Source extracts and scratch scripts remain under `/tmp`, and all
  plots are generated from repository-owned model code.
- State validation, source/link/citation/TOC checks and SVG parsing passed:
  1001 plan file/fragment links, 836 changed/new-file relative links and
  55 citation references, with all keys resolved.
  The graph adds precisely the four new concept nodes, preserves every
  existing node's fields, and has the expected new relations and layouts.
  The source layout is 49 Incerto pages, 73 pages overall and 69 redirects.
  `git diff --check` and separate new-file whitespace/final-newline checks
  passed. Shared notation, bibliography, URL map and dependency locks
  are unchanged.

This review changed the inference note's Gaussian sentence, the damage
helper, its regression tests and review records/status. The core teaching
formulas, demo code and figures required no correction. No mathematical
item needs Xiang's decision. Site build, HTML/browser checks, wheel build
and Lean were not rerun; the earlier blocked site build and required
post-publication reader review remain open. The historical Charter fallback
device check remains separate. No files were deleted, staged or committed.

Status edits are confined to `docs/plan/index.md` and
`docs/plan/incerto-program/{README.md,concepts.md,m0.5-review.md,state.yaml,validation.md}`.
Together with this record, `content/incerto-inference-asymmetry.md`,
`src/math/incerto/lecture_risk.py` and `tests/test_incerto_lecture_risk.py`,
these are the ten files changed by the review within the original 48-file scope.

## Operator rerun outside the sandbox (2026-10-18, America/New_York)

On this branch's working tree (base `697d55a`), clean `_build/`:

| Check | Result |
| --- | --- |
| `uv run pytest -q` | pass: 277 passed, 43 subtests passed |
| `npm ci` | pass |
| `npm run build` | pass; no "Linked … DOIs from doi.org" lines |
| `npm run check:html` | pass: 73 pages across four sites, 69 redirects, 58 pages with display math; 4 pre-existing unresolved legacy url-map rows skipped |
| Built-HTML citation check | Pareto, max-to-sum, IG, Normix online EM, GIG and Karamata pages: each citation renders author/year once (e.g. "Amari & Nagaoka (2000), *Methods of Information Geometry*"; "Darling, 1952, Theorem 5.1" in parentheses) |
| Tail-ratio SVG | Weibull legend handle renders as dash-dot, matching the plotted line |

The Math Site Editor's live reader review of the new and changed pages is due after publication.
