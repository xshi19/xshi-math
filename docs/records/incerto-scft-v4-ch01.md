# SCoFT v4 chapter 1 implementation

Date: 2026-10-17. Branch: `scft/v4-ch01`. Base: `fbf2c6a` (published
PR #27). Owner-selected model: gpt-6-astra, xhigh. No commit or deployment.
The owner requested a separate max-reasoning review of the mathematics.

## Source and teaching scope

Read the supplied read-only `2001.10488v4.pdf`, chapter 1, printed pp. 3–6
(PDF pages 17–20). The Prologue is a discussion chapter; it has no numbered
mathematical theorem or equation. Its terminology discussion is on pp. 4–5.
The chapter motivates distinguishing distributional assumptions; it does not
supply a classification theorem or invalidate every use of a named statistic.
No book prose, figures, PDF, TOC or extracted text was added to the repository.

Added [the Prologue guide](../../content/incerto-scoft-ch1.md), with an original
bounded-law counterexample, and extended the canonical
[tail catalog](../../content/incerto-tail-class-catalog.md) with moment
contrasts, gamma derivations and a model-ratio figure. Wrote the teaching
content before implementing the numerical examples. The reused
[Cramér](../../content/incerto-cramer-condition.md),
[regular-variation](../../content/incerto-regular-variation.md) and
[subexponential](../../content/incerto-subexponentiality.md) notes received
scoped reference changes; their broader chapter-5/7 material was not rewritten.

Added `taleb2025scoftv4` to the bibliography. The old `taleb2020scoft` key
remains for other chapters' reconciliation. The new guide is in the Incerto
TOC, SCoFT overview and track hub; the helper module is in the API index.
The canonical route is `/math/incerto/incerto-scoft-ch1/`. The existing layout
code discovers its flat `/math/incerto-scoft-ch1/` redirect. No old
`/incerto-wiki/` chapter-1 URL was asserted, so `url-map.csv` is unchanged.
The expected source membership is 44 Incerto pages, 68 pages overall and
64 flat redirects; this is a source count, not a successful HTML build.

## Claims for the separate max review

These IDs cover the new or newly scoped mathematics. Definitions and source
motivation are not attributed to a numerical experiment. The existing
catalog convolution appendix remains unchanged and retains its M0.5 review.

| ID | Claim / assumptions | Evidence in the teaching pages |
| --- | --- | --- |
| CH01-C01 | Gaussian Pearson kurtosis 3; the three-point law at 0 and ±1/√ε, with masses 1−ε and ε/2, has mean 0, variance 1, kurtosis 1/ε and finite MGF for every real argument, for fixed 0<ε≤1. Each law is bounded, even as kurtosis varies without a common upper bound across the family. | Guide, “High kurtosis with bounded support”: integration by parts for the Gaussian reference; full finite-sum proof and support argument for the counterexample. |
| CH01-C02 | Exponential(rate 1) has every positive power moment and positive MGF only below 1. | Catalog, “Moment gates”: direct gamma integral and exponential integral, including divergence at the boundary. |
| CH01-C03 | For X=exp(Z), Z standard normal, E[X^q]=exp(q²/2) for all real q, while E[exp(θX)]=∞ for all θ>0. | Catalog, “Proof of the lognormal moment contrast”: completing the square and a divergent lower bound on the positive half-line. |
| CH01-C04 | Exact Pareto positive moments exist precisely below α; α=5/2, x_m=1 gives mean 5/3, variance 20/9 and infinite fourth moment, with no positive exponential moment. | Catalog moment table/example; existing Pareto moment and Cramér proofs are linked. Arithmetic is derived here; no new general regular-variation moment theorem is asserted. |
| CH01-C05 | Multiplier ratios for Pareto, lognormal, stretched Weibull, exponential and gamma; lognormal tail is between every exponential and every power. Standard-lognormal log survival expansion and its extension to finite log location and positive log scale. | Catalog diagnostics: algebra and derivation from the cited normal-tail asymptotic, DLMF Eq. 7.12.1. The finite plotted curves do not establish limits from data. |
| CH01-C06 | Independent common-rate gamma shapes add; gamma survival asymptotic and divergence of the iid two-sum ratio for every positive shape/rate; exact rate-one integer-shape checks. | Catalog, “Exact light-tail checks”: convolution using the cited beta identity (DLMF Eq. 5.12.1), l'Hôpital argument and integration by parts. This establishes the negative gamma/exponential classifications. |
| CH01-C07 | Nonnegative regularly varying laws with positive exponent are subexponential; lognormal and Weibull(shape in (0,1)) are subexponential but not regularly varying. | Positive subexponential classifications are cited, not proved: FKZ second edition, §3.5, Theorems 3.29–3.30 and following examples, pp. 57–58. Non-regular-variation follows from the displayed multiplier ratios. Citation scope also appears in the reused prerequisite notes. |

Verified the FKZ edition/title and full text at the
[second-edition PDF](https://www.math.u-szeged.hu/~kevei/tanitas/irodalom/Foss%20Korshunov%20Zachary%20An%20intro%20to%20heavy%20tailed%20and%20subexp%20dist.pdf),
printed pp. 57–58 (PDF pages 69–70). Theorem 3.29's following paragraph
identifies regularly varying laws; Theorem 3.30 and its examples give the
lognormal/Weibull applications. Checked the analytic inputs at
[DLMF 7.12.1](https://dlmf.nist.gov/7.12#E1) and
[DLMF 5.12.1](https://dlmf.nist.gov/5.12#E1).

## Python and figures

- Helper: [tail_classes.py](../../src/math/incerto/tail_classes.py), with
  `bounded_spike_summary` and `log_survival_multiplier_ratio`. The module uses
  the existing installed `xmath.incerto` mapping; no dependency or packaging
  mapping changed.
- Demo: [prologue_tail_classes.py](../../demos/incerto/prologue_tail_classes.py).
  No RNG, observed data, fitted parameters or distribution truncation. Three
  fixed ε values and a fixed 241-threshold grid from 1 to 10,000, multiplier 2,
  five named laws; dimensionless units. Runtime is normally a few seconds.
- Tests: [test_incerto_tail_classes.py](../../tests/test_incerto_tail_classes.py),
  30 cases including independent discrete-law moments, exact Pareto scaling,
  an ordinary-probability-underflow case, invalid domains, overflow,
  non-finite log probabilities and mismatched shapes.
- Figures: [bounded kurtosis](../../assets/figures/incerto/prologue-kurtosis.svg)
  and [tail ratios](../../assets/figures/incerto/prologue-tail-ratios.svg).
  Used the existing figure theme, fixed SVG hash salt and omitted timestamps.
  Both files were byte-identical on repeat and inspected through PNG previews.

Observed outputs: kurtoses 10, 100 and 1000, variance 1 throughout; all 1205
log-ratio grid values finite, no omitted points. Exponential two-sum ratios
at thresholds 2, 10 and 100 are 1.5, 5.5 and 50.5. Gamma(shape 2, rate 1)
gives approximately 1.055556, 10.348485 and 850.334983. SciPy gamma survival
at the far end of the plot can underflow internally, so the demo uses its
exact log-survival formula −u+log(1+u) for that curve. These computations
check the finite formulas, not the cited classification theorems.

## Review dispositions and Lean

M0.5 is now `done`: the owner reports Math Site Editor live review passed on
2026-10-17 after PR #27 (`fbf2c6a`) publication. This is a recorded handoff,
not a new browser session. Exact device/viewport details were not provided.

- 004: published apostrophe fix confirmed. Possible mixed-weight rendering
  without Charter (fallback serif stack) remains pending Xiang's check.
- 005: reader wording confirmed by the completed live review.
- 006/007: chapter-1 reuse resolved with precise mathematical locators and
  v4-pinned source context; the shared issues remain assigned for other chapters.

Lean is `skipped-for-now`. Chapter 1 contains no source theorem to formalize;
its original examples use finite sums and analytic integrals. Introducing a
new probability/integration library setup is unnecessary for this teaching
chunk. No checked declaration is claimed. The already-approved chapter-2
counting pilot remains optional and unchanged.

## Checks and remaining work

| Check | Result |
| --- | --- |
| Plain `uv run pytest` | Blocked by read-only default cache lock. |
| `UV_CACHE_DIR=/tmp/m05-uv-cache uv run --offline pytest` | **181 passed in 3.04s**; original baseline was 151 passed. |
| Demo with the same cache and `MPLCONFIGDIR=/tmp/ch01-matplotlib` | Passed, including finite-value checks and byte-identical SVG rerun. |
| `npm ci --offline --cache /tmp/m05-npm-cache --no-audit --no-fund` | Failed `ENOTCACHED`. Reused local `node_modules` from the published checkout with byte-identical package lock. |
| `UV_CACHE_DIR=/tmp/m05-uv-cache UV_OFFLINE=1 npm run build` | Blocked at MyST npm preflight. Direct Node child-process reproduction: `spawnSync /bin/sh EPERM`. No build completed. |
| `npm run check:html` | Failed because fresh pages/assets/config are absent after the blocked build; four pre-existing unresolved legacy rows remain skipped. |
| State, source links, TOC and whitespace | Passed documented state validator (988 plan links), 280 local links across 21 changed/new files, full 44-page Incerto TOC membership, 68-page/64-redirect source layout, citation keys, figure paths and `git diff --check`; checked all seven new files separately. |
| Equation rendering | Source formulas reviewed. Standalone KaTeX rendering was unavailable (`katex` module absent); no rendered-equation check is claimed. |
| Site/browser, deployment and live chapter-1 reader review | Not performed. Must follow an external successful build and publication; M0.5's live pass does not cover new content. |
| Lean and wheel build | Not run; Lean skipped and no package mapping changed. |

State marks chapter-1 implementation `done` and selects `scft-v4-ch02` as
requested. The tail-catalog concept remains `in-progress` for its later
chapter scopes. Separate Astra max review of CH01-C01–C07, a successful
external site build/check and Math Site Editor's subsequent live review
remain recorded follow-ups. No claim of publication or mathematical review
at max reasoning is made by this checkpoint.

## Max-reasoning math review

Reviewed 2026-10-17 by owner-selected gpt-6-astra at MAX reasoning, on the
uncommitted `scft/v4-ch01` worktree. Read the root/Incerto guidance, shared
notation canon and program notation lock, and proof-writing skill before
completing the review. Inspected all 14 tracked-file diffs and all seven
untracked files, including the prerequisite citations, helper, demo, tests
and SVGs. This section closes the separate mathematical review requested
above; site build and live reader review remain separate.

| Claim | Verdict | Verification |
| --- | --- | --- |
| CH01-C01 — Gaussian kurtosis and bounded counterexample | correct | Gaussian integration by parts has vanishing boundary terms and gives second/fourth moments 1 and 3. Direct summation gives mean 0, variance 1, fourth moment and Pearson kurtosis 1/ε, and the stated cosh MGF. Checked ε=1 and the exclusion of ε=0. Each fixed law has finite support; neither regular variation nor the stated unbounded-support subexponential definition applies. Numerical Gaussian integrals, atom sums and MGFs agree, including ε=10⁻¹⁰. |
| CH01-C02 — Exponential moments | correct | For q>0 the gamma integral is integrable at both endpoints. The MGF integral is 1/(1−θ) for θ<1; at θ=1 its integrand is 1 and for θ>1 it grows. Checked noninteger power moments, θ approaching 1 from below, and finite-cutoff integrals at/above the boundary. |
| CH01-C03 — Lognormal moments | correct | Completing the square proves E[X^q]=exp(q²/2) for every finite real q, including zero and negative q. For every θ>0, θ exp(z)−z²/2 eventually exceeds zero, giving a divergent half-line integral. Checked moments by normal-density quadrature and the lower-bound mechanism down to θ=10⁻²⁰. No finite numerical integral is treated as proof of MGF divergence or subexponentiality. |
| CH01-C04 — Pareto moment threshold/example | correct | Rechecked the linked density integral, finite formula α x_m^q/(α−q), logarithmic divergence at q=α, and power divergence above it. At α=5/2, x_m=1, mean 5/3, second moment 5 and variance 20/9 are exact. The centered fourth moment also diverges: for x≥2E[X], (x−E[X])⁴≥x⁴/16. The positive-MGF integral diverges for every θ>0. Independent quadrature, exact rational arithmetic and SciPy moments agree. |
| CH01-C05 — Multiplier ratios/lognormal asymptotics | correct | Recomputed all five ratios with fixed t>1 and positive denominators; Pareto's exact formula requires x≥x_m. DLMF 7.12.1 gives the stated normal-tail constant and lognormal log-survival expansion. For general μ and σ>0, set z=(log x−μ)/σ and d=log(t)/σ; the leading ratio is z/(z+d) exp(−dz−d²/2). This verifies the location/scale extension, both tail comparisons, and the zero limit. Compared all 1205 plotted values with independent high-precision formulas. |
| CH01-C06 — Gamma convolution/survival/two-sum ratios | correct | Substitution y=xv gives the beta integral with k,ℓ>0, including integrable endpoint singularities below shape 1. The convolution argument assumes independence and a common positive rate, as stated. The survival derivative ratio tends to 1 for every fixed k>0; the eventual denominator is nonzero. Rechecked Γ(k)/(2Γ(2k)), the rate factor (λx)^k, the integer-shape survival recurrence, and all six exact table values. Independent convolution quadrature and incomplete-gamma calculations agree for fractional shapes and rates 0.2, 1 and 3. |
| CH01-C07 — Positive subexponential classifications | cited-ok | Read FKZ 2013, second edition, §3.5, printed pp. 57–58 (PDF pages 69–70). Theorem 3.29(i) and its following paragraph cover regularly varying tails, without a finite-mean requirement. Theorem 3.30 and its examples cover nondegenerate lognormal and Weibull with 0<β<1. Nonnegative support and iid convolution match the notes' definition. Zero log-variance and β=1 are correctly excluded; the latter is exponential. |

The unchanged catalog appendix was also checked: conditioning gives the full
convolution integral, and the three regions are disjoint within the sum event
up to null boundaries. The factor 2 and square-tail term are correct for iid
continuous variables with lower endpoint a and x>2a. Its normalized logarithmic
form requires positive survival at x, as supplied by the diagnostic's
unbounded-support assumption. Twenty-seven shifted-gamma integrations, with
negative, zero and positive lower endpoints, agree with the exact sum law.
The guide's distinctions between population assumptions, empirical moments,
and finite numerical evidence are correct.

Source verification:

- Re-read the supplied `/workspace/scoft-toc/2001.10488v4.pdf`, printed
  pp. 3–6 (PDF pages 17–20). Chapter title, terminology on pp. 4–5, the
  absence of numbered theorems/equations, and the three reading-map locators
  agree. The title/copyright pages and
  [versioned arXiv record](https://arxiv.org/abs/2001.10488v4) confirm the
  third edition and 2025 date. The abbreviated bibliography title is accurate.
- The [FKZ PDF](https://www.math.u-szeged.hu/~kevei/tanitas/irodalom/Foss%20Korshunov%20Zachary%20An%20intro%20to%20heavy%20tailed%20and%20subexp%20dist.pdf)
  explicitly supplies the cited applications. Regular variation supplies the
  long-tail and dominated-variation hypotheses of 3.29; its finite-mean
  qualification concerns the stronger class in part (ii), not the cited
  subexponential conclusion. The lognormal/Weibull examples follow 3.30.
- Checked [DLMF 7.12.1](https://dlmf.nist.gov/7.12#E1), using
  normal survival = erfc(z/√2)/2, and
  [DLMF 5.12.1](https://dlmf.nist.gov/5.12#E1), whose positive-real-parameter
  hypotheses match the gamma calculation.
- Manual phrasing comparison found no copied chapter prose. An exhaustive
  normalized five-word overlap scan of the 19 changed/new text files against
  chapter 1 found no matches. Source extracts and scratch calculations stayed
  under `/tmp`; the two figures are regenerated repository-owned model plots.

Verification in this review:

- `UV_CACHE_DIR=/tmp/m05-uv-cache UV_OFFLINE=1 uv run pytest`:
  **181 passed in 3.19s**, including all 30 new helper cases. Confirmed that
  `xmath.incerto.tail_classes` imports from this worktree. The helper computes
  population moments and log-survival differences; the tests exercise the
  advertised domains, underflow, overflow and invalid-value handling.
- Scratch script `/tmp/ch01-max-review/numerical_review.py`:
  **1483 comparisons/assertions passed**, using NumPy 2.4.6, SciPy 1.18.1 and
  cached mpmath 1.4.1 at 70 decimal digits. No dependency files changed.
  The largest grid error divided by 1+|reference log ratio| was below
  2.3×10⁻¹⁵. Checks included gamma shapes 0.1, 0.5, 1, 2 and 5.5,
  general lognormal location/scale, and exact gamma-table fractions.
  Finite Pareto/lognormal/Weibull convolution checks illustrate convergence;
  the cited theorems, not quadrature, establish their classifications.
- Reran `demos/incerto/prologue_tail_classes.py` with the same offline cache
  and `MPLCONFIGDIR=/tmp/ch01-max-review/matplotlib`: all tables and finite
  grid checks passed; both SVGs were byte-identical to the initial assets.
  Inspected the existing PNG previews and checked the SVG structure/labels.
- The documented state validator passed, including 990 plan file/fragment
  links. Source checks passed for all 21 changed/new files, 282 local links,
  citation keys, figures and TOC membership. `git diff --check` and separate
  whitespace/final-newline checks of the seven untracked files passed.
- Site build, HTML/browser checks, wheel build and Lean were not rerun:
  no teaching formulas, code, tests, figures or package mappings changed.
  The earlier site-build limitation and post-publication reader gate remain.

Corrections: none required in the mathematics, citations or Python. Appended
this evidence and updated the pending review status in the program records.
No mathematical item needs Xiang's decision. The existing Charter fallback
device check remains outside this review. No files were deleted, staged or
committed.

## Operator rerun outside the sandbox (2026-10-17, America/New_York)

On this branch's working tree (base `fbf2c6a`), clean `_build/`:

| Check | Result |
| --- | --- |
| `uv run pytest -q` | pass: 181 passed, 43 subtests passed |
| `npm ci` | pass |
| `npm run build` | first attempt failed: doi.org returned no citation data for doi:10.1017/CBO9780511721434 (unchanged reference in `content/incerto-karamata.md`; transient upstream failure). Retry: pass |
| `npm run check:html` | pass: 68 pages across four sites, 64 redirects, 53 pages with display math; 4 pre-existing unresolved legacy url-map rows skipped |

Live reader review of the new and changed pages by the Math Site Editor is due after publication.
