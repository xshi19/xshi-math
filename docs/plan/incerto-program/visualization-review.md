# Incerto visualization review

Reviewed 2026-10-20 at `0ff7d93` on `plan/incerto-visualization-review`.
This is a source-based review and proposed backlog; no figures, teaching pages,
code, program state, or chapter checkpoints were changed.

The largest gap is basic distribution shape and diagnostic instruction.
Pareto, GPD, GEV, and Fréchet have no embedded figures; Double Pareto's only
figure is an advanced matching comparison. Later chapter work already supplies
substantial figures, often reached through links from the reading guides.

Implementation follow-up (2026-10-28): ranks **11–15** are delivered in
[visualization P2](../../records/incerto-viz-p2.md), alongside chapter 7 and
requested threshold/GEV/Rayleigh mobile repairs. The inventory below remains
the original 2026-10-20 review, not a current figure count. Other P2/P3
recommendations are unstarted. See [P1 evidence](../../records/incerto-viz-p1.md)
for ranks 1–10.

## Scope and priorities

- The [Incerto TOC](../../../myst.incerto.yml) matches **55 public pages**:
  54 `content/incerto-*.md` files and `content/incerto/index.md`.
- **26 SVG files, embedded on 19 pages**: 20 in
  [assets/figures/incerto](../../../assets/figures/incerto/) and six in the older
  [assets/incerto/figures](../../../assets/incerto/figures/). Every SVG in those
  directories is used; none is orphaned. Counts below count files, not panels.
- **36 pages have no embedded SVG**. One is the dependency graph with its
  existing interactive iframe. Zero embedded figures does not imply zero visual
  coverage: guides and several concepts link to figures on other pages.
- Read all public pages, all 13 Python modules in `src/math/incerto/`, all 13
  scripts in `demos/incerto/`, SVG structure/labels, repository rules, and the
  program [README](README.md), [templates](templates.md), and [state](state.yaml).
  This review does not advance the chapter queue or schedule the chapter-7
  Cauchy experiment early.

**P1:** fill missing introductory figures and make existing diagnostic figures
readable on mobile. **P2:** explain mechanisms, sampling uncertainty, and
connections. **P3:** optional exploration or work dependent on additional data.
**S:** reuse/re-export or a small analytic plot. **M:** a new multi-panel demo,
simulation study, or fitted diagnostic. **L:** a reusable interactive component
or data/fitting workflow with validation. Effort includes captions and checks;
it is per deliverable, assuming shared style code is reused.

### Ranked top 15

| Rank | Tier | Deliverable | Effort |
| --- | --- | --- | --- |
| 1 | P1 | Pareto: PDF, CDF, and log-log survival distribution card | S |
| 2 | P1 | GPD: distribution card showing bounded, exponential, and heavy tails | M |
| 3 | P1 | GEV: distribution card showing shape-dependent support | M |
| 4 | P1 | Fréchet: distribution card plus the existing normalized-maxima comparison | M |
| 5 | P1 | Double Pareto: introductory distribution card before the matching figure | S |
| 6 | P1 | Hill estimator: threshold stability with known synthetic truth | M |
| 7 | P1 | Mean excess: increasing/flat/decreasing population curves and noisy estimates | M |
| 8 | P1 | Threshold selection: coordinated survival, Hill, mean-excess, GPD, and count diagnostics | M |
| 9 | P1 | Max-to-sum: trajectories and repeated-sample bands across the mean boundary | M |
| 10 | P1 | Regular variation: bring the existing slow-variation ratio figure onto the concept page | S |
| 11 | P2 | Subexponentiality: sum-event geometry and the existing convolution-ratio comparison | M |
| 12 | P2 | LLN failure: running means, repeated-sample spread, and capped-mean growth | M |
| 13 | P2 | Plug-in tail estimation: the mean singularity and finite/nonfinite estimate frequencies | M |
| 14 | P2 | Counting exceedances: strict empirical survival and its CDF complement at ties | S |
| 15 | P2 | Generalized CLT: repeated sums under the correct and square-root normalizations | M |

Build one distribution-card layout for ranks 1–5. Use one fixed synthetic
sample and shared diagnostics for ranks 6–8. Mobile repairs listed below are
P1 work alongside the affected figures, rather than a second content queue.

## Page-by-page inventory and recommendations

Every row is one public page. Figure names are exact basenames, including
`.svg`; **old/** marks `assets/incerto/figures/`, and unmarked names are in
`assets/figures/incerto/`. Linked figures are described separately from embedded
counts. **SVG is sufficient for every proposed plot below**; possible P3 widgets
are evaluated afterward. “Keep” means no additional figure is recommended.
Code abbreviations are resolved in the reuse map below; script names refer to
`demos/incerto/`. “New” identifies code that does not currently exist.

### Distribution pages

| Page | Embedded figures: count and names | Gap → recommendation and reader benefit | Tier / effort | Reuse and missing work |
| --- | --- | --- | --- | --- |
| [Pareto](../../../content/incerto-pareto.md) | 0 | Formulas and a parameter table lack shape. Add PDF/CDF/log-log survival; distinguish density slope from tail exponent and show the lower cutoff. | P1 / S | `D.pareto_type1`; new shared card demo. |
| [Double Pareto](../../../content/incerto-double-pareto.md) | 1: `power-law-matching.svg` | The only figure compares matched Student tails. Add a symmetric PDF/CDF and right-tail or absolute-tail survival for basic shape intuition, explicitly labeled. | P1 / S | `D.double_pareto`; retain `power_laws.py` matching figure. New card export; preserve this page's shifted, symmetric definition. |
| [Generalized Pareto](../../../content/incerto-generalized-pareto.md) | 0 | Add a shape sweep with the finite endpoint visible for negative shape. Readers see the three excess-tail regimes. | P1 / M | Page formulas; `nyc_dog_name_tail.py` uses SciPy `genpareto`. New distribution-card adapter; no GPD distribution wrapper in `D`. |
| [Generalized extreme value](../../../content/incerto-generalized-extreme-value.md) | 0 | Add PDF/CDF/survival and endpoint markers. Show how the sign of shape changes maxima support. | P1 / M | Page CDF; new support-aware evaluator/card. No GEV helper; verify any library's shape-sign convention against the page. |
| [Fréchet](../../../content/incerto-frechet.md) | 0 | Add the basic card, then compare finite-sample normalized-maxima CDFs with the limit. Connect the named law to a maxima experiment. | P1 / M | `G.pareto_normalized_maximum_cdf`, maxima panel of `glossary_worked_cases.py`; new Fréchet PDF/CDF/survival evaluator. |
| [Tail-class catalog](../../../content/incerto-tail-class-catalog.md) | 2: `prologue-tail-ratios.svg`; `multivariate-regimes.svg` | Existing ratio and regime figures are useful but do not display raw tails. Add aligned log-log and semilog survival comparisons so curvature distinguishes candidate families. | P2 / S | Models and `C.log_survival_multiplier_ratio` in `prologue_tail_classes.py`; new raw-survival export. State scale choices; a finite range cannot classify an unknown tail. |
| [Mixture uncertainty](../../../content/incerto-mixture-uncertainty.md) | 1: `finite-moment-mixtures.svg` | Keep: density and two-sided survival already expose hidden variance uncertainty. An optional variance-separation sweep can show tail changes at fixed total variance. | Keep; P3 / S optional sweep | `F.normal_mixture_log_density`, `normal_mixture_log_abs_survival`; `finite_moments.py`. Do not label a finite Gaussian mixture a power law. |
| [Multivariate tails](../../../content/incerto-multivariate-tails.md) | 3: `multivariate-information.svg`; `multivariate-spectra.svg`; `multivariate-sampling.svg` | Keep: dependence, spectra, joint extremes, and sampling instability are covered. Extra scatter clouds would add little unless tied to a specific conditional-event question. | Keep | `V.bivariate_student`, `student_mutual_information`, `symmetric_spectrum`; `multivariate_tails.py`. |

### Theorem and limit pages

| Page | Embedded figures: count and names | Gap → recommendation and reader benefit | Tier / effort | Reuse and missing work |
| --- | --- | --- | --- | --- |
| [Regular variation](../../../content/incerto-regular-variation.md) | 0 | Embed the existing slow-variation comparison: a nonstraight log-log tail can still have ratios approaching a power. Label the plotted law explicitly. | P1 / S | `glossary-slow-variation.svg`, `glossary_worked_cases.py`, `T.regular_variation_ratio`. Existing figure uses exponent 2; the page's worked example uses 1.5. |
| [Karamata](../../../content/incerto-karamata.md) | 0; links to Pareto-moment figure | Re-export its tail-integral ratio panel locally. It makes the limiting constant and slow convergence visible without another simulation. | P2 / S | Bottom panel of `power-law-integrals.svg`, `power_laws.py`; new focused export. |
| [Pareto moment existence](../../../content/incerto-pareto-moment-existence.md) | 1: `power-law-integrals.svg` | Keep the below/equal/above moment-boundary comparison. A focused moment panel would reduce the current product/integral detour. | P2 / S re-export | `P.pareto_truncated_moment`, middle panel of `power_laws.py`; no new mathematical helper needed. |
| [Mean excess](../../../content/incerto-mean-excess-function.md) | 0 | Plot Pareto/exponential/uniform population curves, then estimates with exceedance counts. Separate tail-shape information from high-threshold sampling noise. | P1 / M | `E.mean_excess`, `G.pareto_tail_quantities`, page formulas. New seeded demo and minimum-count masking; infinite population means must be labeled, not drawn as finite curves. |
| [Pickands–Balkema–de Haan](../../../content/incerto-pickands-balkema-de-haan.md) | 0 | Plot conditional excess survival at several thresholds after scaling. Start with exact Pareto/GPD agreement; add a labeled nonexact example only with its normalization checked. | P2 / M | `D.pareto_type1`, page's exact excess law. New threshold overlays; no general POT-limit demonstration exists. A fitted agreement is not a proof or a threshold selector. |
| [Subexponentiality](../../../content/incerto-subexponentiality.md) | 0; links to tail-ratio figure | Add the sum-event region in the first quadrant and extract the convolution-ratio panel. Explain why one large summand dominates asymptotically. | P2 / M | `T.iid_two_sum_tail`, `power_laws.py` / `power-law-diagnostics.svg`. New geometric diagram; distinguish the proof's region cover from a disjoint decomposition. |
| [Cramér condition](../../../content/incerto-cramer-condition.md) | 0 | Compare truncated exponential moments as the cutoff grows for thin and heavy tails. Reveal the condition's mechanism; retain the analytic conclusion beside the finite plot. | P2 / M | Page formulas, `D.pareto_type1`; new stable integration/analytic benchmark. No exponential-moment plotting helper exists. |
| [Generalized CLT](../../../content/incerto-generalized-central-limit-theorem.md) | 0 | Simulate the page's Pareto exponent 1.5 example under stable and square-root scaling. Empirical CDFs or quantile widths show which normalization keeps the spread comparable. | P2 / M | `D.pareto_type1`; batching pattern in `lln_preasymptotic.py`. New centered-sum experiment; no stable-sum runner or stable-limit evaluator exists. |
| [LLN failure](../../../content/incerto-lln-failure.md) | 0; links to pre-asymptotic example | Reuse running means and add repeated-sample spread plus capped-mean growth for infinite-mean regimes. Distinguish finite-run plateaus from a finite population mean. | P2 / M | `E.running_mean`, `lln_preasymptotic.py`, `P.pareto_truncated_moment` plus the cap correction. New capped-mean panel; the helper itself computes an indicator-truncated moment. |
| [Inference asymmetry](../../../content/incerto-inference-asymmetry.md) | 1: `lecture-inference-payoffs.svg` | Keep: the missed-component probability already illustrates finite-sample blindness. No additional chart is needed to make the counterexample work. | Keep | `R.repeated_event_probability`, `lecture_risk.py`. |
| [Ruin](../../../content/incerto-ruin.md) | 1: `lecture-ruin.svg` | Add two short absorbing resource paths with the same increments in different orders. Readers see why ruin changes the relevance of later gains. | P2 / S | `R.absorbing_resource_path`; new step plot in `lecture_risk.py`. Existing survival/hazard panels remain useful. |

### Methods

| Page | Embedded figures: count and names | Gap → recommendation and reader benefit | Tier / effort | Reuse and missing work |
| --- | --- | --- | --- | --- |
| [Hill estimator](../../../content/incerto-hill-estimator.md) | 0 | Plot estimated extreme-value index against retained count, with known truth; compare exact Pareto with the page's body/tail mixture. Show threshold bias and variance without promising a unique plateau. | P1 / M | `E.hill_stability`, `hill_estimator`, `hill_alpha_estimator`, `D.pareto_type1`. New synthetic demo; threshold coordinates and tie-aware counts must be computed separately. |
| [Extreme-value index](../../../content/incerto-extreme-value-index.md) | 0 | Reuse the GEV/GPD sign comparison with support endpoints. Show that a positive tail exponent reciprocal covers only the positive-index case. | P2 / S after cards | Proposed GEV/GPD cards; `G.pareto_normalized_maximum_cdf` covers only the Pareto maxima example. No all-regime EVI helper exists. |
| [Plug-in tail estimation](../../../content/incerto-plug-in-tail-estimation.md) | 0 | Plot the Pareto-mean singularity, then estimate quantiles and the fraction returning infinity. Explain why small tail-index errors can dominate mean estimates. | P2 / M | `E.pareto_mean_plugin`, `D.pareto_type1`. New repeated-sample figure; preserve nonfinite estimates and avoid an empirical MSE claim from a finite run. |
| [Moment estimation](../../../content/incerto-moment-estimation.md) | 2: `finite-moment-estimation.svg`; `finite-moment-norms.svg` | Existing sampling and norm comparisons are substantial. An optional order-versus-tail-exponent map would separate existence of the moment from finite estimator variance. | P2 / S optional | `F.pareto_moment_estimator_summary`, `finite_moments.py`; new analytic region diagram. |
| [Tail-threshold selection](../../../content/incerto-tail-threshold-selection.md) | 0 | Show one synthetic sample's survival, Hill, mean excess, fitted GPD shape/modified scale, and counts across thresholds. Add QQ or PP checks at a few selected thresholds; explain the bias/count tradeoff. | P1 / M | `S.empirical_survival_function`, `E.hill_stability`, `mean_excess`; adapt SciPy fit loop in `nyc_dog_name_tail.py`. New coordinated runner, QQ/PP plotting, fit/support/failure checks; no validated general GPD fitting helper exists. |
| [Survival-tail ratio](../../../content/incerto-survival-tail-ratio.md) | 1: `power-law-diagnostics.svg` | Keep: squared-survival and convolution ratios already distinguish different tail questions, with a separate near-zero detail panel. Additional log-log survival belongs in the distribution cards. | Keep | `T.iid_two_sum_tail`, `D.hypsecant2`, `power_laws.py`. Preserve the page's distinct ratio definitions. |
| [Maximum entropy](../../../content/incerto-maximum-entropy.md) | 1: `power-law-entropy.svg` | Keep: the constrained optimum and q-exponential tail sweep address the page's claims. Another density gallery would duplicate the cards. | Keep | `P.entropy_log_constraint_example`, `q_exponential_logsf`, `power_laws.py`. |
| [Max-to-sum ratio](../../../content/incerto-max-to-sum-ratio.md) | 0 | Plot running ratios and repeated-sample bands below, at, and above the finite-mean boundary. Show persistent concentration versus decay; do not imply a limit of one below the boundary. | P1 / M | `E.max_to_sum_ratio`, `D.pareto_type1`; `lln_preasymptotic.py` currently only prints final ratios. New checkpoint/ensemble plot; helper does not return a running path. |
| [Body, shoulder, tail](../../../content/incerto-body-shoulder-tail.md) | 1: `finite-moment-curvature.svg` | Add a simple density with body/shoulder/tail regions shaded before the variance-derivative plot. Give the derivative sign changes a spatial reference. | P2 / S | `S.normal_variance_peak_shoulder_tail`, `normal_peak_shoulder_tail`, `finite_moments.py`. New shaded-density export; these are not fitted EVT thresholds. |
| [Iso-density tail geometry](../../../content/incerto-iso-density-tail-geometry.md) | 1: `multivariate-geometry.svg` | Add the fixed-sum line and constrained maximizing points for Gaussian and independent Cauchy cases. Make equal sharing versus near-axis concentration visible. | P2 / M | `multivariate_tails.py` contours and page formulas. New line/point overlays and Gaussian comparison; two fixed sum levels suffice. |
| [Asymmetric payoffs](../../../content/incerto-asymmetric-payoffs.md) | 0; links to inference/payoff figure | Re-export the payoff panel next to its worked example. Show that identical input means do not fix expected transformed payoffs. | P2 / S | `R.finite_payoff_mean`; lower panel of `lecture-inference-payoffs.svg`, `lecture_risk.py`. |
| [Decentralization](../../../content/incerto-decentralization.md) | 1: `lecture-scale-dependence.svg` | Keep: splitting costs and common-shock dependence already have separate panels. A network drawing would not establish the independence assumptions. | Keep | `R.split_power_damage_logsf`, `block_failure_summary`, `lecture_risk.py`. |

### Examples

| Page | Embedded figures: count and names | Gap → recommendation and reader benefit | Tier / effort | Reuse and missing work |
| --- | --- | --- | --- | --- |
| [Counting exceedances](../../../content/incerto-counting-exceedances.md) | 0; links to chapter 2 | Put strict empirical-survival steps beside the CDF complement for `(1, 2, 2, 4)`, marking threshold 2. Open/closed endpoints explain ties and the value 1/4. | P2 / S | `S.empirical_survival_function`, `exceedances.py`, left panel of `glossary-exceedances-maxima.svg`; new focused CDF companion. |
| [Amazon book rank](../../../content/incerto-amazon-bookrank.md) | 1: **old/** `amazon-bookrank-1.svg` | Rank/sales, survival, and Hill already exist. Reflow the three horizontal panels vertically and improve alt text. Label rank plotting positions separately from strict survival; do not add another generic Zipf plot. | P1 / S repair | `L.load_amazon_bookrank`, `E.hill_stability`, `amazon_bookrank.py`. Repeated titles and a finite snapshot limit iid fitting claims. |
| [NYC dog-name tail](../../../content/incerto-nyc-dog-name-tail.md) | 3: **old/** `nyc-dog-name-tail-1.svg`; `nyc-dog-name-tail-2.svg`; `nyc-dog-name-tail-3.svg` | Zipf/rank, lognormal comparison, Hill and GPD diagnostics already exist. Stack the last figure and give counts their own aligned panel; improve generic alt text. Distinguish rank positions from strict survival with ties. | P1 / S repair | `L.load_nyc_dog_name_frequencies`, `E.hill_stability`, `nyc_dog_name_tail.py`. Optional discrete-aware QQ is P3 / M; a continuous fit is not a validated discrete tail model. |
| [S&P 500 tail](../../../content/incerto-sp500-tail.md) | 0, intentional data boundary | No chart until an approved, reproducible price input is available. Later: returns over time, negative-return survival, Hill and mean excess with counts; expose regime and threshold sensitivity. | P3 / L, data-dependent | `L.load_sp500_prices(fetch=False)`, `PriceSeries.negative_log_returns`, `E.hill_stability`, `mean_excess`; `sp500_tail.py` prints diagnostics only. New figure runner and provenance review; no fetching for this review. |
| [Dispersion ratio](../../../content/incerto-dispersion-ratio.md) | 1: **old/** `dispersion-ratio-1.svg` | Add the already-computed upper quantile and stack panels. Median-only curves conceal sampling spread. Keep the Gaussian calibration visible. | P1 / S layout; P2 / S spread | `S.dispersion_ratios`, `dispersion_ratio.py::ratio_quantiles` computes 0.5 and 0.9, but plots only 0.5. Label these quantiles accurately; they are not a central uncertainty band. |
| [LLN pre-asymptotic](../../../content/incerto-lln-preasymptotic.md) | 1: **old/** `lln-preasymptotic-1.svg` | Stack the path and sampling panels. Add repeated-sample results at the boundary exponent 1, currently shown only as a single path. Preserve visible large jumps. | P1 / S layout; P2 / M boundary | `E.running_mean`, `D.pareto_type1`, `lln_preasymptotic.py`; existing repeated-sample curves cover exponents 0.8 and 1.3. |

### Hub and concept indexes

| Page | Embedded figures | Gap → recommendation and reader benefit | Tier / effort | Reuse |
| --- | --- | --- | --- | --- |
| [Incerto hub](../../../content/incerto/index.md) | 0 | Keep text navigation. A density montage would compete with the entry paths; link readers to the cards through existing distribution pages. | Keep | Existing links. |
| [Distribution index](../../../content/incerto-distribution-concepts.md) | 0 | Keep the comparison/navigation table. Full cards belong on individual pages. | Keep | Distribution-page links. |
| [Theorem index](../../../content/incerto-theorem-concepts.md) | 0 | Keep the theorem map; no shared axes or single visual claim warrant a new chart. | Keep | Concept links and dependency graph. |
| [Method index](../../../content/incerto-method-concepts.md) | 0 | Keep task-based navigation; diagnostic screenshots would duplicate method pages. | Keep | Method-page links. |
| [Empirical-example index](../../../content/incerto-empirical-example-concepts.md) | 0 | Keep the example/provenance table; thumbnails add little to choosing a dataset. | Keep | Example-page links. |

### Reading guides and reference pages

| Page | Embedded figures: count and names | Gap → recommendation and reader benefit | Tier / effort | Reuse |
| --- | --- | --- | --- | --- |
| [SCoFT introduction](../../../content/incerto-scoft-intro.md) | 0 | Keep the reading route and scope; no independent mathematical claim needs a plot here. | Keep | Existing chapter/concept links. |
| [SCoFT chapter 1](../../../content/incerto-scoft-ch1.md) | 1: `prologue-kurtosis.svg` | Keep: the bounded-spike example already breaks the kurtosis/tail-class shortcut. The tail-ratio comparison is linked through the catalog. | Keep | `C.bounded_spike_summary`, `prologue_tail_classes.py`. |
| [SCoFT chapter 2](../../../content/incerto-scoft-ch2.md) | 2: `glossary-exceedances-maxima.svg`; `glossary-slow-variation.svg` | Split the horizontal exceedance/maxima pair into single-column panels; reuse them on the corresponding concepts. Preserve the slow-variation comparison. | P1 / S layout | `S.empirical_survival_function`, `G.pareto_normalized_maximum_cdf`, `glossary_worked_cases.py`. |
| [SCoFT chapter 3](../../../content/incerto-scoft-ch3.md) | 0; links to 3 `lecture-*` figures on concepts | Keep canonical figures on inference, ruin, and decentralization pages. No missing chapter-level gallery. | Keep | `lecture_risk.py`; concept-page links. |
| [SCoFT chapter 4](../../../content/incerto-scoft-ch4.md) | 0; links to 4 `finite-moment-*` figures and dispersion example | Keep the guide focused on claim boundaries. New concept diagrams should be linked here only where they support the reading route. | Keep | `finite_moments.py`, `dispersion_ratio.py`. |
| [SCoFT chapter 5](../../../content/incerto-scoft-ch5.md) | 0; links to 4 `power-law-*` figures on concepts | Keep links to matching, integrals, diagnostics, and entropy; avoid reproducing the whole set. | Keep | `power_laws.py`. |
| [SCoFT chapter 6](../../../content/incerto-scoft-ch6.md) | 0; links to 5 `multivariate-*` figures on concepts | Keep: geometry, dependence, sampling, spectra, and regimes already have canonical homes. | Keep | `multivariate_tails.py`. |
| [External reading](../../../content/incerto-external-reading.md) | 0 | Bibliographic routing benefits from links, not plots. | Keep | Existing reading links. |
| [Embrechts reading guide](../../../content/incerto-reading-embrechts.md) | 0 | Keep the source-to-concept map; point to strengthened EVT concepts. | Keep | Existing concept links. |
| [Dependency DAG](../../../content/incerto-dependency-dag.md) | 0 SVG; 1 interactive graph iframe | Keep the existing interaction and plain-list fallback. A duplicate static graph would add maintenance without fixing a recorded gap. | Keep | [concept-graph.html](../../../assets/graphs/concept-graph.html), [concept-list.html](../../../assets/graphs/concept-list.html). |
| [Glossary](../../../content/incerto-glossary.md) | 0 | Keep concise definitions and links. Stylized “Mediocristan/Extremistan” curves could imply formal tail classes the page does not define. | Keep | Formal concept pages. |
| [API reference](../../../content/incerto-api-reference.md) | 0 | Function tables and examples are the useful reference format. Put outputs on teaching pages. | Keep | Existing API/source links. |
| [Chinese entry](../../../content/incerto-chinese-entry.md) | 0 | Language/navigation policy has no visualization gap. | Keep | Existing navigation. |

## Reuse map and implementation gaps

These abbreviations denote existing source modules, not new APIs. Distribution
objects in `D` expose SciPy-style methods; functions in the other rows are named
in the inventory. `__init__.py` exports only a subset, so implementations should
check the defining module rather than assume every helper is available at the
package root.

| Key | Existing module | Relevant capability and limit |
| --- | --- | --- |
| D | [distributions.py](../../../src/math/incerto/distributions.py) | `pareto_type1`, `double_pareto`, `simple_normal_mixture`, `hypsecant2`, `univariate_variance_gamma`. No GPD/GEV/Fréchet objects. |
| E | [estimators.py](../../../src/math/incerto/estimators.py) | Hill estimates/stability, plug-in mean, running mean, final max-to-sum ratio, mean excess with counts. No combined threshold dashboard or QQ helper. |
| S | [stats.py](../../../src/math/incerto/stats.py) | Strict, tie-aware empirical survival; dispersion ratios and analytic shoulder boundaries. Rank plotting positions in empirical demos are a different convention. |
| G | [glossary.py](../../../src/math/incerto/glossary.py) | Pareto tail quantities and exact finite-sample normalized-maxima CDF. The latter does not implement a Fréchet distribution object. |
| T | [tail_diagnostics.py](../../../src/math/incerto/tail_diagnostics.py) | Regular-variation ratios, log-domain convolution integration, Monte Carlo sum-tail ratios. Preserve convergence/error diagnostics; rare-event counts can be zero. |
| C | [tail_classes.py](../../../src/math/incerto/tail_classes.py) | Bounded-spike moments and log survival multiplier ratios. The existing ratio chart is not a raw survival chart. |
| F | [finite_moments.py](../../../src/math/incerto/finite_moments.py) | Stable Gaussian-mixture density/tails, absolute moments, Pareto moment-estimator regimes, power means. |
| P | [power_laws.py](../../../src/math/incerto/power_laws.py) | Product tails, indicator-truncated Pareto moments, Student/Double-Pareto matching, q-exponential survival, entropy example. |
| R | [lecture_risk.py](../../../src/math/incerto/lecture_risk.py) | Detection/survival probabilities, finite payoff expectations, absorbing resource paths, splitting and dependence examples. |
| V | [multivariate.py](../../../src/math/incerto/multivariate.py) | Shared-scale Student sampling, entropy/information, correlation, spectra, population regression and location-mixture kurtosis. |
| L | [datasets.py](../../../src/math/incerto/datasets.py) | Explicit snapshot/cache loaders; S&P data absence is handled. Data acquisition and publication remain separate work. |
| Style | [figures.py](../../../src/math/incerto/figures.py) | `set_theme`, `style_axes`, `savefig`; bundled fonts, fixed SVG hash salt, stable metadata. Size presets include horizontal panels and do not enforce mobile stacking. |

### Existing figure producers

| Script | Committed SVG outputs | Reuse notes |
| --- | --- | --- |
| [prologue_tail_classes.py](../../../demos/incerto/prologue_tail_classes.py) | 2: `prologue-*` | Analytic bounded-spike and five-family tail comparison. |
| [glossary_worked_cases.py](../../../demos/incerto/glossary_worked_cases.py) | 2: `glossary-*` | Fixed tied sample, exact normalized maxima, slow-variation example. |
| [lecture_risk.py](../../../demos/incerto/lecture_risk.py) | 3: `lecture-*` | Deterministic detection, payoffs, survival, splitting and dependence. |
| [finite_moments.py](../../../demos/incerto/finite_moments.py) | 4: `finite-moment-*` | Analytic panels plus seeded repeated-sample estimation. |
| [power_laws.py](../../../demos/incerto/power_laws.py) | 4: `power-law-*` | Mostly analytic/quadrature; several panels can be exported individually. |
| [multivariate_tails.py](../../../demos/incerto/multivariate_tails.py) | 5: `multivariate-*` | Analytic geometry/information and seeded matrix/sampling experiments. |
| [amazon_bookrank.py](../../../demos/incerto/amazon_bookrank.py) | 1: **old/** `amazon-bookrank-1.svg` | Snapshot-based three-panel figure; reflow rather than replace diagnostics. |
| [nyc_dog_name_tail.py](../../../demos/incerto/nyc_dog_name_tail.py) | 3: **old/** `nyc-dog-name-tail-*.svg` | Snapshot rank/tail analysis; local SciPy GPD fit loop is a starting point, not a fitting API. |
| [dispersion_ratio.py](../../../demos/incerto/dispersion_ratio.py) | 1: **old/** `dispersion-ratio-1.svg` | Seeded ratio quantiles; upper quantile is computed but not plotted. |
| [lln_preasymptotic.py](../../../demos/incerto/lln_preasymptotic.py) | 1: **old/** `lln-preasymptotic-1.svg` | Seeded paths and batched sampling quantiles; max-to-sum is printed only. |

The remaining scripts produce console output, not committed figures:
[exceedances.py](../../../demos/incerto/exceedances.py),
[sp500_tail.py](../../../demos/incerto/sp500_tail.py), and
[normal_mixture.py](../../../demos/incerto/normal_mixture.py).
The last is a multivariate mixture moment check, not the producer of
`finite-moment-mixtures.svg`.

## Shared figure conventions

1. **Distribution cards:** one original, vertically stacked PDF/CDF/survival
   figure per distribution, using a common export function. Include support,
   parameter values, a legend, and endpoint markers. A linear CDF explains
   accumulated probability; a log-log survival panel reveals tail behavior.
   For distributions with negative support, plot survival only at positive
   thresholds in the log-log panel and label its restricted view. Never take
   logarithms of nonpositive coordinates or zero survival at finite endpoints.
   Use semilog survival as an additional comparison where exponential decay is
   the question. Double Pareto needs an explicit right-tail versus absolute-tail
   label. No automatic variance matching when the variance does not exist.

2. **Parameter choices:** retain the page tables: Pareto lower cutoff
   $x_m=1$ and exponents $\alpha\in\{0.8,1.5,3\}$; GPD scale $\beta=1$ and
   shape $\xi\in\{-0.4,0,0.4\}$; GEV location $\mu=0$, scale $\sigma=1$ and
   $\xi\in\{-0.3,0,0.3\}$. Reuse the Pareto exponent grid for new Fréchet and
   Double-Pareto cards, with their scale/shift definitions stated. Existing
   LLN experiments use $\alpha\in\{0.8,1,1.3\}$: retain that grid and label
   the boundary, rather than silently changing existing results. Keep colors
   consistent within each comparison and reuse [shared notation](../../../content/notation.md).

3. **Mobile single column:** repair the horizontal Amazon, NYC diagnostic,
   dispersion, LLN, and chapter-2 exceedance/maxima figures. Re-export panels
   vertically or as separate SVGs; shrinking a wide SVG does not reflow its
   contents. Verify labels and legends at 390px and 900px, including the long
   existing vertical figures. This review identifies a source-layout risk;
   it does not claim a new browser inspection passed. Separate counts from
   estimates rather than using a crowded secondary axis.

4. **One style/export path:** retain `figures.py`, its serif/math fonts, stable
   SVG metadata, and named palette. Add a vertical-card layout there when
   implementation is authorized. Keep overlapping curves visible through line
   styles or separate panels, never by shifting the underlying values. Reuse
   the existing asset path for a layout repair; put new exports in
   `assets/figures/incerto/`. Moving all legacy assets is unnecessary.

5. **Determinism and numerical honesty:** specify seed, RNG, repetitions,
   sample sizes, thresholds, and quantiles in the producer. Use independent,
   reproducible streams for distinct experiments; batch large simulations.
   Existing demos already provide seeded patterns. Use analytic curves and
   log survival where available; inspect quadrature status and error estimates.
   Show retained counts, invalid fits, and nonfinite plug-in estimates. Do not
   replace them silently with clipped values. Check support and the sign
   convention of fitted shape parameters. A log-log line, stable-looking Hill
   region, or finite simulation cannot prove an asymptotic claim.

6. **Captions and alt text:** identify the law/data, parameters, quantity,
   axis scale, population curve versus estimate, and the intended comparison.
   Label quantile envelopes as sampling quantiles, not confidence intervals
   without a justified construction. Include the sample size/seed or a direct
   producer link. For empirical plots, record provenance and whether ranks are
   plotting positions or strict exceedance counts. Replace generic Amazon/NYC/LLN
   alt text with a short description of the axes and main visible relationship;
   preserve details in the caption. SVG text is exported as paths, making the
   surrounding accessible text especially important.

7. **Reuse at the point of explanation:** keep concepts as canonical homes.
   Extract focused panels when the existing multi-topic figure would interrupt
   a definition; reuse the same producer and data. Reading guides should link
   to the relevant figure anchor. Avoid duplicating all concept figures inside
   chapters 3–6. Future captions and figures must be original repository work,
   consistent with the program's source-reuse boundary.

### Where interaction earns its maintenance cost

The existing dependency graph proves that this static site can host browser
interaction; it does not provide a mathematical widget framework. No public
Incerto page currently embeds a distribution or threshold slider. CSS selectors
for older widget names are not evidence that those widgets are present.

| Candidate | Decision | Additional work beyond the SVG |
| --- | --- | --- |
| Distribution shape slider | P3 / L for a shared accessible component; fixed three-parameter cards first. Smooth endpoint/tail changes are useful exploration, but static comparisons teach the main point. | New client-side formulas or precomputed curves, support handling, labels, keyboard controls, static fallback, and asset staging. |
| Threshold selector on one fixed sample | Best P3 / L candidate after ranks 6–8. Worthwhile because moving one threshold can update retained points, counts, Hill/mean excess, and fit diagnostics together. | New coordinated data/export component; precompute valid fits and diagnostics. Expose fit failures and avoid an “optimal threshold” badge. |
| LLN or max-to-sum animation | P3 / M after shared controls; modest added teaching value over paths plus sampling bands. Replay a fixed path with its seed visible. | New playback controls and reproducible sample paths; repeated-sample summaries must remain visible. |
| Mixture separation or fixed-sum geometry slider | P3 / M after shared controls; a small static parameter sweep is sufficient initially. | Shared slider infrastructure plus checked parameter ranges and analytic overlays. |

No Python backend is needed for these proposals. Any future widget should ship
local browser assets/precomputed data, work under `/math/`, and retain the SVG
and textual explanation when scripts are unavailable. Interactivity does not
justify fetching S&P inputs or moving financial-data decisions into the browser.

## Review checks and limits

- Reconciled all 55 inventory rows with the TOC and public source glob; checked
  the 26 figure references against both asset directories and parsed their SVGs.
- Checked this document's relative file links, page coverage, figure names,
  function references, and whitespace. No index registration is required by the
  planning conventions; this review remains outside the public MyST TOCs.
- No demos, Python tests, site build, or live/browser checks were run for this
  documentation-only review. Figure producers were read without regenerating
  tracked outputs. Existing recorded build/review results are not new evidence.
- Proposed new evaluators, diagnostics, simulations, and widgets still need
  implementation and relevant numerical/render checks. The source review is
  not a fresh mathematical proof review or an empirical tail-model validation.
