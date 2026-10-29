# Incerto visualization P2

2026-10-28. Branch `scft/v4-ch07-viz-p2`, base `b863314` from
`origin/main`. Xiang selected **gpt-6-astra xhigh** for writing/code and
requested a separate **gpt-6-astra max** review afterwards. No delegation,
commit, push, publication or file deletion.

Implemented exactly ranks **11–15** in the
[visualization review](../plan/incerto-program/visualization-review.md),
alongside [chapter 7](incerto-scft-v4-ch07.md) and the five requested minor
repairs. Other P2/P3 proposals remain unstarted. All figures use shared
DejaVu Serif, a five-inch single-column layout, fixed SVG hash salt and
metadata, captions and descriptive alt text.

## Figures and their pages

Paths below are in `assets/figures/incerto/`. P2 adds seven figures;
chapter 7 adds Cauchy/growth figures. Two split exports and four regenerated
assets complete the requested minor repairs: **11 new, four changed SVGs**.

| Rank / repair | Figure file | Canonical page | Producer |
| --- | --- | --- | --- |
| 11 | `subexponential-geometry.svg` | [Subexponentiality](../../content/incerto-subexponentiality.md#subexponential-event-geometry) | `demos/incerto/visualization_p2.py` |
| 11 | `subexponential-convolution.svg` | [Subexponentiality](../../content/incerto-subexponentiality.md#subexponential-convolution-figure) | `visualization_p2.py`, reusing `power_laws.py::plot_convolution_ratio` |
| 12 | `lln-failure-paths.svg` | [LLN](../../content/incerto-lln-failure.md#lln-failure-sample-paths) | `demos/incerto/limit_distributions.py` |
| 12 | `lln-capped-means.svg` | [LLN](../../content/incerto-lln-failure.md#lln-failure-truncated-mean-check) | `limit_distributions.py` |
| 13 | `plugin-mean-singularity.svg` | [Plug-in estimation](../../content/incerto-plug-in-tail-estimation.md#plugin-singularity-figure) | `visualization_p2.py` |
| 14 | `exceedances-ties.svg` | [Counting exceedances](../../content/incerto-counting-exceedances.md#counting-exceedances-ties) | `visualization_p2.py` |
| 15 | `generalized-clt.svg` | [Generalized CLT](../../content/incerto-generalized-central-limit-theorem.md#generalized-clt-scaling-simulation) | `limit_distributions.py` |
| Chapter 7 | `cauchy-running.svg` | [Cauchy statistics](../../content/incerto-cauchy-running.md#cauchy-running-figures) | `limit_distributions.py` |
| Chapter 7 | `ergodicity-growth.svg` | [Time/ensemble averages](../../content/incerto-ergodicity.md#ergodicity-growth) | `limit_distributions.py` |
| b/d | `threshold-diagnostics.svg`, `threshold-gpd.svg` | [Threshold selection](../../content/incerto-tail-threshold-selection.md#threshold-synthetic-figures) | `demos/incerto/tail_estimation.py` |
| c | `gev-card.svg` | [GEV](../../content/incerto-generalized-extreme-value.md#gev-distribution-card) | `demos/incerto/distribution_cards.py` |
| e | `rayleigh-speed-fits.svg`, `rayleigh-speed-qq.svg`, `rayleigh-speed-qq-tail.svg` | [Rayleigh chamber speeds](../../content/incerto-rayleigh-speed.md) | `demos/incerto/rayleigh_speed.py` |

## Mechanisms and experiment bounds

Rank 11 splits the first quadrant into the maximum event and the residual
sum event. Colored area is explicitly not probability. The strict diagonal
boundary belongs to neither exceedance region. The convolution export reuses
the exact chapter-5 panel code, preserving Pareto 1.5, Weibull 0.5 and
exponential mean 1, 81 thresholds from 3 to 10^4, relative tolerance 1e-9
and refinement limit 12. Failed quadrature stops generation. The exponential
ratio is analytically (1+u)/2; the subexponential curves approach one.

Rank 12 preserves Pareto exponents 0.8/1/1.3 and cutoff one. Complete
10,000-prefix paths use seeds 20261080–82; repeated-sample bands use
600 independent samples at 30/100/300/1000/3000 with seeds 20261180–82.
The capped-mean panel is a separate population calculation; it does not
truncate observations in either simulation. It distinguishes power growth,
logarithmic growth and the finite limit 13/3.

Rank 13 plots the functional alpha/(alpha−1) only above one and marks the
infinite-mean region. Exact infinite-fit probabilities use the Gamma law of
the known-cutoff log-excess sum. Dots use 600 independent fits at
n=10/30/100/300, true exponents 0.8/1/1.5 and PCG64 seeds 20261090–92.
Every fit is classified; none is dropped. The finite fraction is the complement.

| True exponent | Finite fits, n=10/30/100/300 | Infinite fits, same sizes |
| --- | --- | --- |
| 0.8 | 193 / 83 / 8 / 0 | 407 / 517 / 592 / 600 |
| 1 | 337 / 323 / 326 / 319 | 263 / 277 / 274 / 281 |
| 1.5 | 562 / 598 / 600 / 600 | 38 / 2 / 0 / 0 |

Rank 14 uses the exact tied sample [1,2,2,4]. Filled points show values
at the threshold; open points show left limits. At u=2, strict survival is
1/4 and the CDF is 3/4. This differs from distinct rank plotting positions.

Rank 15 uses the same 800 centered Pareto-1.5 sums in both panels, with
center 3, sizes 30/100/300/1000/3000 and seed 20261074. The correct
n^(2/3) scale leaves a comparable spread; sqrt(n) multiplies the displayed
IQR by n^(1/6) exactly. This finite experiment does not prove stable attraction
or prescribe a skew-stable parameterization. All bands are pointwise
10th/90th sampling quantiles, with median curves, not confidence bands.

## Helpers, visible code and minor repairs

[limits.py](../../src/math/incerto/limits.py) adds the analytic capped mean,
known-cutoff infinite-fit probability and bounded repeated-sum runner used
by P2. Chapter 7 also uses symmetric stable MAD and a Bernoulli Chernoff
bound. Existing `running_mean`, `pareto_mean_plugin`, strict empirical
survival and convolution diagnostics are reused. The API reference supplies
an anchor for every package function named in page code.

- **a:** `hypsecant2.chf` prints real parts, so Output contains plain values
  rather than complex `+0j` representations. All 122 snippets and the existing
  full NYC output were regenerated through the standard script.
- **b/d:** the six threshold panels now form two three-panel figures,
  each about 700 px tall at width 390. One sample and threshold grid remain
  shared. The count title derives from actual statuses: all eligible fits
  succeeded in this run; four below-count fits remain masked, with counts
  visible. No optimizer or statistical-validity guarantee was added.
- **c:** the GEV card has a one-line title. Support conditions and finite
  endpoints remain in the caption and panels.
- **e:** Rayleigh equation (18), the inward GIG boundary score, uses two
  aligned display lines. QQs are split into two two-panel figures, each
  about 544 px tall at width 390, retaining all 199 quantiles per fit.
  Density figures were regenerated through the same demo/shared style.
  The manual References heading is now Sources and context, leaving MyST's
  bibliography heading separate. Fit calculations and recorded values are
  unchanged. Full browser verification of the equation remains blocked.

Inline DOI links across Incerto were converted to existing local citations
so they cannot trigger inline DOI resolution. This changes reference syntax
on additional pages; it is not a new mathematical audit of their claims.

## hard_math_claims_for_max_review

| Location | Claim or convention |
| --- | --- |
| `content/incerto-subexponentiality.md:66`, `:328` | Nonnegative sum-event partition, strict boundaries and negligible residual probability; ratio P(sum>u)/(2 survival(u)), distinct from squared-survival diagnostics. |
| `content/incerto-lln-failure.md:136`, `:165` | Running/repeated-sample evidence versus almost-sure divergence; capped expectation includes the mass above the cap. |
| `content/incerto-plug-in-tail-estimation.md:192` | Exact Gamma infinite-fit probability, finite complement and limit 1/2 at true alpha=1; finite estimates do not imply a finite population mean. |
| `content/incerto-counting-exceedances.md:116` | Strict survival and right-continuous CDF at ties; open/filled endpoint conventions. |
| `content/incerto-generalized-central-limit-theorem.md:132` | Full-mean centering for exact Pareto 1.5, shared draws and n^(2/3) versus sqrt(n) scaling. |
| `content/incerto-tail-threshold-selection.md:144`; `demos/incerto/tail_estimation.py:143` | Shared sample/grid and count masking preserved through the split; status title describes numerical fit outcomes only. |

## Verification and limitations

- Full local `uv run pytest`, with no sync and the available environment:
  **887 passed, 43 subtests passed**. The suite includes 71 new helper cases,
  six P2 identity/reproducibility cases, existing P1 export comparisons and
  updated Rayleigh two-panel layout checks. Exports are generated twice in
  fresh processes and compared byte-for-byte with repository SVGs.
- All **15 SVGs** were rendered at **390 and 900 px** with system
  librsvg/Cairo and visually inspected (30 PNGs). No cropped titles, legends
  or tick labels remain. The figure source and PNGs agree; previews live
  in `/tmp/ch07-previews` and are not a fresh website build.
- Chrome via Playwright is blocked by sandbox socket restrictions.
  `npm ci` fails ENOTCACHED offline and DNS EAI_AGAIN online. Build/check
  were attempted in a temporary copy: MyST is absent, then HTML checks fail
  on missing output. Full equation/navigation and live reader checks remain.
- The exact locked Python environment could not be installed. Final tests
  used the local versions listed in the [chapter record](incerto-scft-v4-ch07.md#verification-and-remaining-limits).
  The dependency lock is unchanged. A locked external rerun remains needed.
- Source links/citations/TOC, program-state validation and whitespace are
  audited with the chapter. Separate max review is pending; Lean is skipped.

No new decision is required from Xiang. The remaining work is the planned
max review and external build/browser verification, followed by reader review
after any authorized publication.

The final source audit passed: 1,142 program links and 1,227 links across
changed/new Markdown, valid local citations/figure targets, exact TOC
membership, and clean tracked/new-file whitespace. The extracted convolution
plotter also regenerates all four chapter-5 SVGs byte-identically. Git remains
at b863314 with no staged changes or deletions.
