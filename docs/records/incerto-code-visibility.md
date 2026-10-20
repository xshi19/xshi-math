# Incerto code visibility and reader fixes

2026-10-20. Base `0ff7d93`, branch `site/code-visibility`. Xiang selected
Codex GPT-6-Astra xhigh and authorized these page changes without a commit.
The package mapping remains `xmath.incerto` → `src/math/incerto` in
`pyproject.toml`; no package API or dependency changed.

## Visible runnable examples

The initial pass covered 31 standalone `python` blocks on 29 pages. The test
convention is **every** such block in `content/incerto-*.md` and
`content/incerto/index.md`, including blocks inside dropdowns. There is no
execution opt-out. Seeds are explicit where sampling occurs; the largest new
sample has 20,000 values. Examples print results and neither fetch data nor
save figures. Full figure scripts remain as regeneration notes.

`tests/test_incerto_page_snippets.py` runs each block in a fresh process with
Agg, temporary working/cache directories, blocked network calls and blocked
repository writes. It checks API links and dropdowns for blocks over 12 lines.
The S&P block is tested both without data and with a temporary deterministic
synthetic price cache; that fixture is not represented as S&P observations.
Amazon and NYC examples read the existing bundled snapshots through loaders.

| Page | Code added or revised |
| --- | --- |
| [incerto-amazon-bookrank.md](../../content/incerto-amazon-bookrank.md) | Bundled CC0 sales snapshot; Hill estimates across five upper-order counts. |
| [incerto-api-reference.md](../../content/incerto-api-reference.md) | Existing seeded Pareto/Hill example now prints its estimate; execution convention documented. |
| [incerto-asymmetric-payoffs.md](../../content/incerto-asymmetric-payoffs.md) | Exact payoff means and a convexity gap for a fixed finite law. |
| [incerto-body-shoulder-tail.md](../../content/incerto-body-shoulder-tail.md) | Normal scale/variance and Student-3 scale curvature boundaries. |
| [incerto-counting-exceedances.md](../../content/incerto-counting-exceedances.md) | Strict finite-sample fractions and tie-aware empirical survival. |
| [incerto-decentralization.md](../../content/incerto-decentralization.md) | Split quadratic-damage survival and independent-block failure summaries. |
| [incerto-dispersion-ratio.md](../../content/incerto-dispersion-ratio.md) | Seeded normal/Student-3 samples and both Gaussian-calibrated dispersion ratios. |
| [incerto-double-pareto.md](../../content/incerto-double-pareto.md) | Distribution moments/survival and Student tail-versus-variance matching scales. |
| [incerto-extreme-value-index.md](../../content/incerto-extreme-value-index.md) | Exact normalized Pareto maximum CDFs and the Fréchet limit. |
| [incerto-inference-asymmetry.md](../../content/incerto-inference-asymmetry.md) | Rare-component mixture mean and finite-sample detection probabilities. |
| [incerto-iso-density-tail-geometry.md](../../content/incerto-iso-density-tail-geometry.md) | Seeded spherical-Cauchy sector frequency versus its exact probability. |
| [incerto-lln-preasymptotic.md](../../content/incerto-lln-preasymptotic.md) | Seeded Pareto running means and maximum shares at three moment regimes. |
| [incerto-maximum-entropy.md](../../content/incerto-maximum-entropy.md) | Mass, log-moment, entropy and KL quadrature for the worked pair of laws. |
| [incerto-mixture-uncertainty.md](../../content/incerto-mixture-uncertainty.md) | Second/fourth moments, kurtosis and absolute tails of finite normal mixtures. |
| [incerto-moment-estimation.md](../../content/incerto-moment-estimation.md) | Seeded second-moment estimates; analytic target/estimator variance and sample quantiles. |
| [incerto-multivariate-tails.md](../../content/incerto-multivariate-tails.md) | Seeded Student sample correlations and population mutual information. |
| [incerto-nyc-dog-name-tail.md](../../content/incerto-nyc-dog-name-tail.md) | Bundled name aggregate; counts, Safari lookup and Hill sensitivity. |
| [incerto-pareto.md](../../content/incerto-pareto.md) | Two blocks: conditional tail quantities and independent-product survival. |
| [incerto-pareto-moment-existence.md](../../content/incerto-pareto-moment-existence.md) | Indicator-truncated moments below, at and above the moment boundary. |
| [incerto-ruin.md](../../content/incerto-ruin.md) | Conditional-hazard survival and absorbing resource paths under reversed increments. |
| [incerto-scoft-ch1.md](../../content/incerto-scoft-ch1.md) | Bounded three-point moments and large Pearson kurtosis. |
| [incerto-scoft-ch2.md](../../content/incerto-scoft-ch2.md) | Empirical ties versus population Pareto conditional quantities. |
| [incerto-scoft-ch3.md](../../content/incerto-scoft-ch3.md) | Rare-component detection and finite expected payoff. |
| [incerto-scoft-ch4.md](../../content/incerto-scoft-ch4.md) | Finite-mixture moments and normalized power means. |
| [incerto-scoft-ch5.md](../../content/incerto-scoft-ch5.md) | Boundary truncated moments and normalized q-exponential log survival. |
| [incerto-scoft-ch6.md](../../content/incerto-scoft-ch6.md) | Student mutual information, regression target and a small symmetric spectrum. |
| [incerto-sp500-tail.md](../../content/incerto-sp500-tail.md) | Revised local-cache example: availability branch and loss/Hill/mean-excess calculations; no fetch. |
| [incerto-survival-tail-ratio.md](../../content/incerto-survival-tail-ratio.md) | Squared-survival versus convolution ratios, with quadrature-success check. |
| [incerto-tail-class-catalog.md](../../content/incerto-tail-class-catalog.md) | Two blocks: model log-survival ratios; location-mixture kurtosis and conditional survival. |

## API anchors

The [API reference](../../content/incerto-api-reference.md) now has 72 stable
`api-*` anchors: function/distribution entries, dataset result types and
methods, plus the base exceedance helper. Function signatures omit type
annotations but retain defaults and keyword-only arguments. Distribution
entries document the common SciPy methods. Every package callable named in
a runnable block has an adjacent API link; prose mentions are linked too.

| Module | Anchored entries |
| --- | --- |
| Datasets | [DatasetNotAvailable](../../content/incerto-api-reference.md#api-datasetnotavailable), [PriceSeries](../../content/incerto-api-reference.md#api-priceseries), [PriceSeries.log_returns](../../content/incerto-api-reference.md#api-priceseries-log-returns), [PriceSeries.negative_log_returns](../../content/incerto-api-reference.md#api-priceseries-negative-log-returns), [BookRankData](../../content/incerto-api-reference.md#api-bookrankdata), [DogNameFrequencyData](../../content/incerto-api-reference.md#api-dognamefrequencydata), [DogNameFrequencyData.frequency_for](../../content/incerto-api-reference.md#api-dognamefrequencydata-frequency-for), [data_root](../../content/incerto-api-reference.md#api-data-root), [snapshot_path](../../content/incerto-api-reference.md#api-snapshot-path), [cache_path](../../content/incerto-api-reference.md#api-cache-path), [load_sp500_prices](../../content/incerto-api-reference.md#api-load-sp500-prices), [load_amazon_bookrank](../../content/incerto-api-reference.md#api-load-amazon-bookrank), [load_nyc_dog_name_frequencies](../../content/incerto-api-reference.md#api-load-nyc-dog-name-frequencies), [write_sp500_fred_cache](../../content/incerto-api-reference.md#api-write-sp500-fred-cache), [write_sp500_cache_from_csv](../../content/incerto-api-reference.md#api-write-sp500-cache-from-csv), [write_amazon_bookrank_snapshot](../../content/incerto-api-reference.md#api-write-amazon-bookrank-snapshot), [write_nyc_dog_name_frequency_snapshot](../../content/incerto-api-reference.md#api-write-nyc-dog-name-frequency-snapshot) |
| Distributions | [pareto_type1](../../content/incerto-api-reference.md#api-pareto-type1), [double_pareto](../../content/incerto-api-reference.md#api-double-pareto), [hypsecant2](../../content/incerto-api-reference.md#api-hypsecant2), [simple_normal_mixture](../../content/incerto-api-reference.md#api-simple-normal-mixture), [univariate_variance_gamma](../../content/incerto-api-reference.md#api-univariate-variance-gamma), [hypsecant2.chf](../../content/incerto-api-reference.md#api-hypsecant2-chf) |
| Estimators | [hill_estimator](../../content/incerto-api-reference.md#api-hill-estimator), [hill_alpha_estimator](../../content/incerto-api-reference.md#api-hill-alpha-estimator), [pareto_mean_plugin](../../content/incerto-api-reference.md#api-pareto-mean-plugin), [hill_stability](../../content/incerto-api-reference.md#api-hill-stability), [running_mean](../../content/incerto-api-reference.md#api-running-mean), [max_to_sum_ratio](../../content/incerto-api-reference.md#api-max-to-sum-ratio), [mean_excess](../../content/incerto-api-reference.md#api-mean-excess) |
| Stats | [mean_absolute_deviation](../../content/incerto-api-reference.md#api-mean-absolute-deviation), [median_absolute_deviation](../../content/incerto-api-reference.md#api-median-absolute-deviation), [normal_peak_shoulder_tail](../../content/incerto-api-reference.md#api-normal-peak-shoulder-tail), [normal_variance_peak_shoulder_tail](../../content/incerto-api-reference.md#api-normal-variance-peak-shoulder-tail), [t_peak_shoulder_tail](../../content/incerto-api-reference.md#api-t-peak-shoulder-tail), [lognorm_params_from_mean_and_variance](../../content/incerto-api-reference.md#api-lognorm-params-from-mean-and-variance), [empirical_survival_function](../../content/incerto-api-reference.md#api-empirical-survival-function), [dispersion_ratios](../../content/incerto-api-reference.md#api-dispersion-ratios) |
| Tail diagnostics | [regular_variation_ratio](../../content/incerto-api-reference.md#api-regular-variation-ratio), [iid_two_sum_tail](../../content/incerto-api-reference.md#api-iid-two-sum-tail), [subexponential_sum_ratio](../../content/incerto-api-reference.md#api-subexponential-sum-ratio) |
| Tail classes | [bounded_spike_summary](../../content/incerto-api-reference.md#api-bounded-spike-summary), [log_survival_multiplier_ratio](../../content/incerto-api-reference.md#api-log-survival-multiplier-ratio) |
| Glossary | [pareto_tail_quantities](../../content/incerto-api-reference.md#api-pareto-tail-quantities), [pareto_normalized_maximum_cdf](../../content/incerto-api-reference.md#api-pareto-normalized-maximum-cdf) |
| Lecture risk | [repeated_event_probability](../../content/incerto-api-reference.md#api-repeated-event-probability), [survival_from_hazards](../../content/incerto-api-reference.md#api-survival-from-hazards), [finite_payoff_mean](../../content/incerto-api-reference.md#api-finite-payoff-mean), [absorbing_resource_path](../../content/incerto-api-reference.md#api-absorbing-resource-path), [split_power_damage_logsf](../../content/incerto-api-reference.md#api-split-power-damage-logsf), [block_failure_summary](../../content/incerto-api-reference.md#api-block-failure-summary) |
| Finite moments | [normal_mixture_log_density](../../content/incerto-api-reference.md#api-normal-mixture-log-density), [normal_mixture_log_abs_survival](../../content/incerto-api-reference.md#api-normal-mixture-log-abs-survival), [normal_mixture_absolute_moment](../../content/incerto-api-reference.md#api-normal-mixture-absolute-moment), [pareto_moment_estimator_summary](../../content/incerto-api-reference.md#api-pareto-moment-estimator-summary), [power_mean](../../content/incerto-api-reference.md#api-power-mean) |
| Multivariate | [student_entropy](../../content/incerto-api-reference.md#api-student-entropy), [student_mutual_information](../../content/incerto-api-reference.md#api-student-mutual-information), [bivariate_student](../../content/incerto-api-reference.md#api-bivariate-student), [sample_correlation](../../content/incerto-api-reference.md#api-sample-correlation), [symmetric_spectrum](../../content/incerto-api-reference.md#api-symmetric-spectrum), [regression_population_r2](../../content/incerto-api-reference.md#api-regression-population-r2), [normal_location_mixture_kurtosis](../../content/incerto-api-reference.md#api-normal-location-mixture-kurtosis) |
| Power laws | [pareto_product_logsf](../../content/incerto-api-reference.md#api-pareto-product-logsf), [pareto_truncated_moment](../../content/incerto-api-reference.md#api-pareto-truncated-moment), [student_double_pareto_scales](../../content/incerto-api-reference.md#api-student-double-pareto-scales), [q_exponential_logsf](../../content/incerto-api-reference.md#api-q-exponential-logsf), [entropy_log_constraint_example](../../content/incerto-api-reference.md#api-entropy-log-constraint-example) |
| Figures | [set_theme](../../content/incerto-api-reference.md#api-set-theme), [style_axes](../../content/incerto-api-reference.md#api-style-axes), [savefig](../../content/incerto-api-reference.md#api-savefig) |
| Base package | [exceedance_fraction](../../content/incerto-api-reference.md#api-exceedance-fraction) |

## Attribution removals

Xiang states that this material is his own and requests no reader-facing
self-attribution, migration history or license notice. This table records the
42 removed footer sections and scattered self-attribution/migration asides.
Removed footer text includes xshi19 copyright/MIT dropdowns and historical
execution disclaimers. Existing documentation records, root license files,
third-party notices, data files and provider terms are unchanged.

| Page | Removed text (short) | Reason |
| --- | --- | --- |
| [incerto-amazon-bookrank.md](../../content/incerto-amazon-bookrank.md) | “Adapted from `xshi19/incerto-wiki`”; xshi19 copyright/MIT notice | Owner-directed removal of self-attribution or migration history. |
| [incerto-api-reference.md](../../content/incerto-api-reference.md) | “Adapted from `xshi19/incerto-wiki`”; xshi19 copyright/MIT notice | Owner-directed removal of self-attribution or migration history. |
| [incerto-asymmetric-payoffs.md](../../content/incerto-asymmetric-payoffs.md) | “Consider this original finite payoff table” | Owner-directed removal of self-attribution or migration history. |
| [incerto-body-shoulder-tail.md](../../content/incerto-body-shoulder-tail.md) | “Adapted from `incerto-wiki`”; xshi19 copyright/MIT notice | Owner-directed removal of self-attribution or migration history. |
| [incerto-chinese-entry.md](../../content/incerto-chinese-entry.md) | “Adapted from `xshi19/incerto-wiki`”; xshi19 copyright/MIT notice | Owner-directed removal of self-attribution or migration history. |
| [incerto-cramer-condition.md](../../content/incerto-cramer-condition.md) | “Adapted from `incerto-wiki`”; xshi19 copyright/MIT notice | Owner-directed removal of self-attribution or migration history. |
| [incerto-dependency-dag.md](../../content/incerto-dependency-dag.md) | “Adapted from `xshi19/incerto-wiki`”; xshi19 copyright/MIT notice | Owner-directed removal of self-attribution or migration history. |
| [incerto-dispersion-ratio.md](../../content/incerto-dispersion-ratio.md) | “Adapted from `xshi19/incerto-wiki`”; xshi19 copyright/MIT notice | Owner-directed removal of self-attribution or migration history. |
| [incerto-distribution-concepts.md](../../content/incerto-distribution-concepts.md) | “Rewritten from `incerto-wiki`”; xshi19 copyright/MIT notice | Owner-directed removal of self-attribution or migration history. |
| [incerto-double-pareto.md](../../content/incerto-double-pareto.md) | “Adapted from `incerto-wiki`”; xshi19 copyright/MIT notice | Owner-directed removal of self-attribution or migration history. |
| [incerto-empirical-example-concepts.md](../../content/incerto-empirical-example-concepts.md) | “Adapted from `xshi19/incerto-wiki`”; xshi19 copyright/MIT notice | Owner-directed removal of self-attribution or migration history. |
| [incerto-external-reading.md](../../content/incerto-external-reading.md) | “Adapted from `xshi19/incerto-wiki`”; xshi19 copyright/MIT notice | Owner-directed removal of self-attribution or migration history. |
| [incerto-extreme-value-index.md](../../content/incerto-extreme-value-index.md) | “Adapted from `incerto-wiki`”; xshi19 copyright/MIT notice | Owner-directed removal of self-attribution or migration history. |
| [incerto-frechet.md](../../content/incerto-frechet.md) | “Adapted from `incerto-wiki`”; xshi19 copyright/MIT notice | Owner-directed removal of self-attribution or migration history. |
| [incerto-generalized-central-limit-theorem.md](../../content/incerto-generalized-central-limit-theorem.md) | “Adapted from `incerto-wiki`”; xshi19 copyright/MIT notice | Owner-directed removal of self-attribution or migration history. |
| [incerto-generalized-extreme-value.md](../../content/incerto-generalized-extreme-value.md) | “Adapted from `incerto-wiki`”; xshi19 copyright/MIT notice | Owner-directed removal of self-attribution or migration history. |
| [incerto-generalized-pareto.md](../../content/incerto-generalized-pareto.md) | “Adapted from `incerto-wiki`”; xshi19 copyright/MIT notice | Owner-directed removal of self-attribution or migration history. |
| [incerto-glossary.md](../../content/incerto-glossary.md) | “Adapted from `xshi19/incerto-wiki`”; xshi19 copyright/MIT notice | Owner-directed removal of self-attribution or migration history. |
| [incerto-hill-estimator.md](../../content/incerto-hill-estimator.md) | “Adapted from `incerto-wiki`”; xshi19 copyright/MIT notice | Owner-directed removal of self-attribution or migration history. |
| [incerto-iso-density-tail-geometry.md](../../content/incerto-iso-density-tail-geometry.md) | “Adapted from `incerto-wiki`”; xshi19 copyright/MIT notice | Owner-directed removal of self-attribution or migration history. |
| [incerto-karamata.md](../../content/incerto-karamata.md) | “Adapted from `incerto-wiki`”; xshi19 copyright/MIT notice | Owner-directed removal of self-attribution or migration history. |
| [incerto-lln-failure.md](../../content/incerto-lln-failure.md) | “Adapted from `incerto-wiki`”; xshi19 copyright/MIT notice | Owner-directed removal of self-attribution or migration history. |
| [incerto-lln-preasymptotic.md](../../content/incerto-lln-preasymptotic.md) | “Adapted from `xshi19/incerto-wiki`”; xshi19 copyright/MIT notice | Owner-directed removal of self-attribution or migration history. |
| [incerto-max-to-sum-ratio.md](../../content/incerto-max-to-sum-ratio.md) | “Adapted from `incerto-wiki`”; xshi19 copyright/MIT notice | Owner-directed removal of self-attribution or migration history. |
| [incerto-mean-excess-function.md](../../content/incerto-mean-excess-function.md) | “Adapted from `incerto-wiki`”; xshi19 copyright/MIT notice | Owner-directed removal of self-attribution or migration history. |
| [incerto-method-concepts.md](../../content/incerto-method-concepts.md) | “Rewritten from `incerto-wiki`”; xshi19 copyright/MIT notice | Owner-directed removal of self-attribution or migration history. |
| [incerto-mixture-uncertainty.md](../../content/incerto-mixture-uncertainty.md) | “Original mixture and moment explanations … adapted from `xshi19/incerto-wiki`”; MIT notice; “The following extension permits a moving conditional mean. It retains the scalar calculation previously given in the chapter guide.”; “The legacy helper `univariate_variance_gamma(alpha, beta, lam)` uses” | Owner-directed removal of self-attribution or migration history. |
| [incerto-multivariate-tails.md](../../content/incerto-multivariate-tails.md) | “the original models proved here” | Owner-directed removal of self-attribution or migration history. |
| [incerto-nyc-dog-name-tail.md](../../content/incerto-nyc-dog-name-tail.md) | “Adapted from `xshi19/incerto-wiki`”; xshi19 copyright/MIT notice | Owner-directed removal of self-attribution or migration history. |
| [incerto-pareto-moment-existence.md](../../content/incerto-pareto-moment-existence.md) | “Adapted from `incerto-wiki`”; xshi19 copyright/MIT notice | Owner-directed removal of self-attribution or migration history. |
| [incerto-pareto.md](../../content/incerto-pareto.md) | “Adapted from `incerto-wiki`”; xshi19 copyright/MIT notice; “Here is a separate original example that does.” | Owner-directed removal of self-attribution or migration history. |
| [incerto-pickands-balkema-de-haan.md](../../content/incerto-pickands-balkema-de-haan.md) | “Adapted from `incerto-wiki`”; xshi19 copyright/MIT notice | Owner-directed removal of self-attribution or migration history. |
| [incerto-plug-in-tail-estimation.md](../../content/incerto-plug-in-tail-estimation.md) | “Adapted from `incerto-wiki`”; xshi19 copyright/MIT notice; “The original simulation is not run in this static adaptation; there is no measured performance table here.” | Owner-directed removal of self-attribution or migration history. |
| [incerto-reading-embrechts.md](../../content/incerto-reading-embrechts.md) | “Adapted from `xshi19/incerto-wiki`”; xshi19 copyright/MIT notice | Owner-directed removal of self-attribution or migration history. |
| [incerto-regular-variation.md](../../content/incerto-regular-variation.md) | “Adapted from `incerto-wiki`”; xshi19 copyright/MIT notice | Owner-directed removal of self-attribution or migration history. |
| [incerto-scoft-ch3.md](../../content/incerto-scoft-ch3.md) | “Adapted from `xshi19/incerto-wiki`”; xshi19 copyright/MIT notice; “original models and proofs;”; “The linked notes supply original” | Owner-directed removal of self-attribution or migration history. |
| [incerto-scoft-ch4.md](../../content/incerto-scoft-ch4.md) | “Adapted from `xshi19/incerto-wiki`”; xshi19 copyright/MIT notice; “The scalar variance–mean gamma derivation previously on this page now lives in the” | Owner-directed removal of self-attribution or migration history. |
| [incerto-scoft-ch5.md](../../content/incerto-scoft-ch5.md) | “It produces four original figures:” | Owner-directed removal of self-attribution or migration history. |
| [incerto-scoft-ch6.md](../../content/incerto-scoft-ch6.md) | “The notes supply original” | Owner-directed removal of self-attribution or migration history. |
| [incerto-scoft-intro.md](../../content/incerto-scoft-intro.md) | “Adapted from `xshi19/incerto-wiki`”; xshi19 copyright/MIT notice | Owner-directed removal of self-attribution or migration history. |
| [incerto-sp500-tail.md](../../content/incerto-sp500-tail.md) | “Adapted from `xshi19/incerto-wiki`”; xshi19 copyright/MIT notice | Owner-directed removal of self-attribution or migration history. |
| [incerto-subexponentiality.md](../../content/incerto-subexponentiality.md) | “Adapted from `incerto-wiki`”; xshi19 copyright/MIT notice | Owner-directed removal of self-attribution or migration history. |
| [incerto-survival-tail-ratio.md](../../content/incerto-survival-tail-ratio.md) | “Adapted from `incerto-wiki`”; xshi19 copyright/MIT notice | Owner-directed removal of self-attribution or migration history. |
| [incerto-tail-class-catalog.md](../../content/incerto-tail-class-catalog.md) | “Adapted from `incerto-wiki`”; xshi19 copyright/MIT notice | Owner-directed removal of self-attribution or migration history. |
| [incerto-tail-threshold-selection.md](../../content/incerto-tail-threshold-selection.md) | “Adapted from `incerto-wiki`”; xshi19 copyright/MIT notice | Owner-directed removal of self-attribution or migration history. |
| [incerto-theorem-concepts.md](../../content/incerto-theorem-concepts.md) | “Rewritten from `incerto-wiki`”; xshi19 copyright/MIT notice | Owner-directed removal of self-attribution or migration history. |
| [incerto/index.md](../../content/incerto/index.md) | “an original worked example” | Owner-directed removal of self-attribution or migration history. |

## Kept / unsure

The following exact page text remains. Third-party citations to Taleb,
Embrechts, papers, books, DLMF and other sources are also preserved: an audit
against `0ff7d93` found no removed citation key or external URL on any of the
55 public Incerto pages. The removal of a generic footer about external
rights does not remove any provider-specific credit or license term.

1. **Kept — Amazon data credit and CC0 statement**
   ([page](../../content/incerto-amazon-bookrank.md)):

> This empirical example uses the CC0 Kaggle snapshot from @zhu2021amazonbookrank
> of Amazon book sales and weekly average sales ranks from 2001.  The cleaned
> snapshot is committed at `data/incerto/snapshots/amazon_bookrank_2001.csv` because it
> is small and redistributable.

2. **Kept — NYC source credit and observed-unit qualification**
   ([page](../../content/incerto-nyc-dog-name-tail.md)):

> The source is the [NYC Dog Licensing Dataset](https://data.cityofnewyork.us/Health/NYC-Dog-Licensing-Dataset/nu7n-tubp)
> [@nycdohmh2026doglicenses].  Each source row is an active license period, not
> necessarily a unique dog.  A renewal within the same year can add another row
> for the same animal.  We therefore call the aggregated values *license-period
> frequencies*, not dog counts.

3. **Kept / terms not re-evaluated — S&P/FRED restriction and local-use note**
   ([page](../../content/incerto-sp500-tail.md)):

> No S&P index levels or derived empirical figures are distributed with this
> page. The source repository records redistribution restrictions for the
> S&P 500 series supplied through FRED [@fred2026sp500].
> Use a local data file whose terms permit your intended analysis.

The exact shell comment also remains:

```text
# Alternatively, where source terms permit downloading for local use:
```

No provider-specific notice was removed. The exact current legal obligations
of third-party datasets were not reassessed in this page-edit task; the
existing credits, restrictions and data documentation are retained.

## Chapter 6 figures and equations

- Split the normal variance-mixture construction and characteristic function
  into separate displays. Also broke the Student density derivation,
  moment/covariance relations, joint-exceedance identity, information integral,
  entropy formula, information decomposition, spectral identities and
  regression relations into shorter lines without changing their claims.
- Regenerated with `demos/incerto/multivariate_tails.py` using the unchanged
  shared `xmath.incerto.figures` style. Only the three requested SVGs changed.
- `multivariate-spectra.svg`: Student-1.5 viewport is `[-10,10]`; annotation
  and caption report **39 below and 40 above, out of 960**. Full range is
  approximately `[-90.0787534,89.8717092]`. All eigenvalues remain in each
  80-value CDF; ranks and denominators are unchanged.
- `multivariate-geometry.svg`: per-panel legend gives 5%, 15%, 35%, 65% of
  density at the origin, distinguished by color and line style. These are
  density levels, not enclosed probabilities. Shortened geometry titles to
  leave room on mobile; captions and alt text agree.
- `multivariate-sampling.svg`: first title is now “Sample correlation”.
  Updated alt text; numerical results are unchanged.
- Rendered the actual changed SVGs through librsvg/Cairo to PNG at 390 and
  900 px and visually inspected all six. No cropped titles or legends;
  central Student-1.5 CDF shape is visible. Previews are local artifacts at
  `/tmp/incerto-codevis-previews/` and are not additional publication assets.

## Verification (initial pass)

- `uv sync --locked --offline` passed with `UV_CACHE_DIR=/tmp/m05-uv-cache`.
  The default cache is read-only in this sandbox.
- Full `uv run --offline pytest -q --durations=5`: **517 passed, 43 subtests
  passed in 22.55 s**. The slowest standalone snippet was 0.62 s, including
  interpreter startup, with `OPENBLAS_NUM_THREADS=1` and temporary Agg caches.
  Initial cold snippet checks were also below 1.4 s each.
- Multivariate demo passed, including the spectral trace check, finite sample
  checks and quadrature budget (maximum reported error `9.97e-10`).
- `npm ci --offline` could not find the MyST 1.10.1 tarball in the writable
  npm cache. Reused the installed MyST from the chapter-6 checkout after
  verifying its `package-lock.json` is byte-identical, together with its cached
  pinned book-theme `45706bc` (v1.3.1).
- `npm run build` stops at MyST's version preflight: npm is reported as
  “Package Not Found” despite the shell npm command being available. Direct
  `--site` and Markdown-export checks encounter the same preflight failure.
  `npm run check:html` was attempted and fails because no assembled HTML
  artifact exists. No HTML build or link check is claimed as passing.
- Inspected the pinned theme bundle: the `dropdown` directive yields a
  `details` node with a `summary`; its renderer emits `<details>`/`<summary>`
  and leaves the node closed unless `open` is specified. Used this supported
  directive for the long S&P block and the long NYC console output.
- The pinned theme's KaTeX 0.16.25 parses all 16 revised display equations
  with errors enabled. A Playwright browser launch fails at Chrome's
  `setsockopt: Operation not permitted`. Actual 390 px page layout, dropdown
  interaction and rendered API fragments therefore still need a browser check
  outside this sandbox. SVG raster inspection is complete and separate.
- Source audit: all API fragment links target explicit labels; all original
  external URLs and citation keys are retained; no self-license or migration
  footer remains on the Incerto pages. Long code/output blocks use dropdowns.
- `git diff --check` passed. Reviewed the diff and both new files in full;
  separate whitespace and relative-link checks passed for the new record
  and test. Only the 55 public Incerto pages, three requested SVGs, the
  multivariate demo, snippet test and this record are changed.

No commit, staging, push, hub transfer or publication was performed. No tracked
file was deleted. Only this new record is added under `docs/`; existing records
remain unchanged. Re-run the full site build/check and mobile browser review
before publication.

## Captured helper outputs (follow-up)

Xiang requested a second pass over all 55 public Incerto pages, including the
API reference and track index. The audit searched prose for `helper`,
`reports`, `returns`, `library`, `xmath.incerto`, `NaN`, `nan`, `inf`, and
`prints`, then checked the surrounding paragraphs. Mathematical definitions,
proofs, data-source descriptions, figure captions and regeneration instructions
remain in place where they do not describe a library return value. The track
index needs no replacement.

There are now **90 standalone Python examples on 30 pages**, each immediately
followed by **Output** and a `text` fence: the original 31 examples, six new
concept-page examples, and 53 API examples. All output blocks were generated
by executing their preceding code through the isolated snippet runner; none
was transcribed by hand. The double-Pareto example covers alpha = 0.5, 1,
1.5, 2 and 3, including both moment boundaries. Other new edge cases cover
constant/outlier dispersion, degenerate correlation, and finite/infinite
Pareto plug-in fits. Existing API anchors are retained and callable headings
link to them.

`tests/test_incerto_page_snippets.py` now pairs every adjacent **Output** fence
with its Python block and compares captured stdout exactly after stripping
trailing whitespace on each line and at the end. Leading whitespace and
internal spacing remain significant. A regression check rejects changed
values and leading indentation but accepts trailing whitespace; a pairing
check catches misplaced dropdown closures. Long code and its output share
the same dropdown. Network and repository-write guards, API-link checks, and
the synthetic local-price test remain active.

The S&P page shows the absent-cache branch and labels that condition; the
existing synthetic-cache test still exercises the data-present branch. API
price-series examples use explicit synthetic prices. Bundled Amazon and NYC
snapshots are unchanged, and generated path examples use a fixed explicit
path without creating files. Seeds and displayed rounding are explicit.
Generation used Python 3.13.5, NumPy 2.4.6 and SciPy 1.18.1.

### Prose-to-code replacements

Each row records one replaced passage; rows on the same page may reuse one
example. Existing snippets retain their computations unless the row records
an expanded case. API rows retain one convention sentence where needed.

| Page | Helper | Before | After |
| --- | --- | --- | --- |
| [incerto-amazon-bookrank.md](../../content/incerto-amazon-bookrank.md) | `load_amazon_bookrank`, `hill_alpha_estimator` | Run in an editable checkout with the bundled CC0 snapshot. It prints 861 rows and Hill exponents from about 3.67 at $k=10$ to 2.07 at $k=120$; these are threshold-sensitive descriptions of this sample. | Existing runnable example paired with captured stdout. |
| [incerto-api-reference.md](../../content/incerto-api-reference.md) | `DogNameFrequencyData.frequency_for` | Return the license-period frequency for a case-insensitive name. | Standalone call with captured stdout. |
| [incerto-api-reference.md](../../content/incerto-api-reference.md) | `PriceSeries.log_returns` | Return close-to-close log returns and their ending dates. | Standalone call with captured stdout. |
| [incerto-api-reference.md](../../content/incerto-api-reference.md) | `PriceSeries.negative_log_returns` | Return positive losses, defined as negative close-to-close log returns. | Standalone call with captured stdout. |
| [incerto-api-reference.md](../../content/incerto-api-reference.md) | `absorbing_resource_path` | Resources including the initial value, stopped at a nonpositive total. | Standalone call with captured stdout; one convention sentence retained. |
| [incerto-api-reference.md](../../content/incerto-api-reference.md) | `bivariate_student` | Draw `size` pairs sharing one gamma precision per pair, with unit diagonal scatter and off-diagonal entry `rho`. | Standalone call with captured stdout; one convention sentence retained. |
| [incerto-api-reference.md](../../content/incerto-api-reference.md) | `block_failure_summary` | Exact summary of equal independent all-or-nothing exposure blocks. | Standalone call with captured stdout; one convention sentence retained. |
| [incerto-api-reference.md](../../content/incerto-api-reference.md) | `bounded_spike_summary` | Moments of a symmetric three-point law with nonzero probability `epsilon`, mean zero and variance one. | Standalone call with captured stdout; one convention sentence retained. |
| [incerto-api-reference.md](../../content/incerto-api-reference.md) | `cache_path` | Return the path to an untracked local cache file. | Standalone call with captured stdout. |
| [incerto-api-reference.md](../../content/incerto-api-reference.md) | `data_root` | Return the configured data directory. | Standalone call with captured stdout. |
| [incerto-api-reference.md](../../content/incerto-api-reference.md) | `dispersion_ratios` | Return sample standard deviation (`ddof=0`) divided by Gaussian-calibrated mean and median absolute deviations. | Standalone call with captured stdout; one convention sentence retained. |
| [incerto-api-reference.md](../../content/incerto-api-reference.md) | `empirical_survival_function` | Return unique sorted observations and their strict empirical survival probabilities. | Standalone call with captured stdout. |
| [incerto-api-reference.md](../../content/incerto-api-reference.md) | `entropy_log_constraint_example` | Independent mass, log-moment, entropy and KL integrals for the worked case $x_m=1$, $\mathbb E\log X=1/2$. | Standalone call with captured stdout; one convention sentence retained. |
| [incerto-api-reference.md](../../content/incerto-api-reference.md) | `exceedance_fraction` | Fraction of a nonempty finite sample strictly above a finite threshold. | Standalone call with captured stdout; one convention sentence retained. |
| [incerto-api-reference.md](../../content/incerto-api-reference.md) | `finite_payoff_mean` | Expected payoff of a finite law; no implicit normalization. | Standalone call with captured stdout; one convention sentence retained. |
| [incerto-api-reference.md](../../content/incerto-api-reference.md) | `hill_alpha_estimator` | Return the reciprocal Hill estimate of the Pareto tail exponent. | Standalone call with captured stdout. |
| [incerto-api-reference.md](../../content/incerto-api-reference.md) | `hill_estimator` | Return the Hill estimate of the extreme-value index `xi`. | Standalone call with captured stdout. |
| [incerto-api-reference.md](../../content/incerto-api-reference.md) | `hill_stability` | Return Hill estimates across a range of upper order statistics. | Standalone call with captured stdout. |
| [incerto-api-reference.md](../../content/incerto-api-reference.md) | `hypsecant2.chf` | Characteristic function at frequencies `t`; call on the distribution object. | Standalone call with captured stdout. |
| [incerto-api-reference.md](../../content/incerto-api-reference.md) | `iid_two_sum_tail` | Compute the iid two-summand right-tail ratio by convolution. | Standalone call with captured stdout. |
| [incerto-api-reference.md](../../content/incerto-api-reference.md) | `log_survival_multiplier_ratio` | Log survival ratio at a multiplied threshold versus the original positive threshold. | Standalone call with captured stdout. |
| [incerto-api-reference.md](../../content/incerto-api-reference.md) | `lognorm_params_from_mean_and_variance` | Return log-location and log-scale matching positive mean and variance. | Standalone call with captured stdout. |
| [incerto-api-reference.md](../../content/incerto-api-reference.md) | `max_to_sum_ratio` | Return the share of a nonnegative sum contributed by its maximum. | Standalone call with captured stdout. |
| [incerto-api-reference.md](../../content/incerto-api-reference.md) | `mean_absolute_deviation` | Return mean absolute deviation scaled to match normal standard deviation. | Standalone call with captured stdout. |
| [incerto-api-reference.md](../../content/incerto-api-reference.md) | `mean_excess` | Return the empirical mean excess above each threshold. | Standalone call with captured stdout. |
| [incerto-api-reference.md](../../content/incerto-api-reference.md) | `median_absolute_deviation` | Return median absolute deviation scaled to match normal standard deviation. | Standalone call with captured stdout. |
| [incerto-api-reference.md](../../content/incerto-api-reference.md) | `normal_location_mixture_kurtosis` | Pearson kurtosis of equal normal components centered at plus and minus `separation`, with common standard deviation `sigma`. | Standalone call with captured stdout; one convention sentence retained. |
| [incerto-api-reference.md](../../content/incerto-api-reference.md) | `normal_mixture_absolute_moment` | Absolute moment of positive order `q`; all such moments exist for this finite mixture. | Standalone call with captured stdout; one convention sentence retained. |
| [incerto-api-reference.md](../../content/incerto-api-reference.md) | `normal_mixture_log_abs_survival` | Log absolute-exceedance probability at finite nonnegative thresholds under the mixture. | Standalone call with captured stdout; one convention sentence retained. |
| [incerto-api-reference.md](../../content/incerto-api-reference.md) | `normal_mixture_log_density` | Log density of a finite centered Gaussian variance mixture. | Standalone call with captured stdout; one convention sentence retained. |
| [incerto-api-reference.md](../../content/incerto-api-reference.md) | `normal_peak_shoulder_tail` | Return normal scale-curvature boundaries for tail diagnostics. | Standalone call with captured stdout. |
| [incerto-api-reference.md](../../content/incerto-api-reference.md) | `normal_variance_peak_shoulder_tail` | Return normal variance-curvature boundaries for tail diagnostics. | Standalone call with captured stdout. |
| [incerto-api-reference.md](../../content/incerto-api-reference.md) | `pareto_mean_plugin` | Estimate an exact Pareto mean with a known lower cutoff. | Standalone call with captured stdout; one convention sentence retained. |
| [incerto-api-reference.md](../../content/incerto-api-reference.md) | `pareto_moment_estimator_summary` | Population moment and variance of its empirical average for iid exact Pareto draws. | Standalone call with captured stdout; one convention sentence retained. |
| [incerto-api-reference.md](../../content/incerto-api-reference.md) | `pareto_normalized_maximum_cdf` | CDF of the maximum divided by $x_m n^{1/\alpha}$ for iid exact Pareto observations. | Standalone call with captured stdout; one convention sentence retained. |
| [incerto-api-reference.md](../../content/incerto-api-reference.md) | `pareto_product_logsf` | Log survival of the product of two independent unit-minimum Paretos at `exp(log_threshold)`. | Standalone call with captured stdout; one convention sentence retained. |
| [incerto-api-reference.md](../../content/incerto-api-reference.md) | `pareto_tail_quantities` | Return log survival, mean excess, conditional mean and tail first moment. | Standalone call with captured stdout. |
| [incerto-api-reference.md](../../content/incerto-api-reference.md) | `pareto_truncated_moment` | Indicator-truncated moment of an exact Pareto law below `cutoff`, including `order=alpha`. | Standalone call with captured stdout; one convention sentence retained. |
| [incerto-api-reference.md](../../content/incerto-api-reference.md) | `pareto_type1`, `hill_alpha_estimator` | This prints a seeded Hill estimate of the generating exponent 2.5. The example is a simulation, not a guarantee about estimation accuracy. The Hill note states the model and threshold assumptions. Use `help()` on an imported function for argument validation, return types, and numerical limits. | Existing runnable example paired with captured stdout. |
| [incerto-api-reference.md](../../content/incerto-api-reference.md) | `power_mean` | Normalized absolute power mean, for `order >= 1`; infinite order selects the maximum magnitude. | Standalone call with captured stdout; one convention sentence retained. |
| [incerto-api-reference.md](../../content/incerto-api-reference.md) | `q_exponential_logsf` | Normalized q-exponential log survival for `x >= 0` and `0 < q < 2`. | Standalone call with captured stdout; one convention sentence retained. |
| [incerto-api-reference.md](../../content/incerto-api-reference.md) | `regression_population_r2` | Squared population correlation for independent regression error and a predictor with variance one. | Standalone call with captured stdout; one convention sentence retained. |
| [incerto-api-reference.md](../../content/incerto-api-reference.md) | `regular_variation_ratio` | Evaluate the fixed-multiplier survival ratio. | Standalone call with captured stdout. |
| [incerto-api-reference.md](../../content/incerto-api-reference.md) | `repeated_event_probability` | Chance of at least one event in independent equal-probability trials. | Standalone call with captured stdout; one convention sentence retained. |
| [incerto-api-reference.md](../../content/incerto-api-reference.md) | `running_mean` | Return cumulative arithmetic means along an axis. | Standalone call with captured stdout. |
| [incerto-api-reference.md](../../content/incerto-api-reference.md) | `sample_correlation` | Centered Pearson coefficient or uncentered cosine along the last axis. | Standalone call with captured stdout; one convention sentence retained. |
| [incerto-api-reference.md](../../content/incerto-api-reference.md) | `snapshot_path` | Return the path to a committed or externally synchronized snapshot. | Standalone call with captured stdout. |
| [incerto-api-reference.md](../../content/incerto-api-reference.md) | `split_power_damage_logsf` | Log survival of Pareto input transformed by a power-damage model and split into equal modules. | Standalone call with captured stdout; one convention sentence retained. |
| [incerto-api-reference.md](../../content/incerto-api-reference.md) | `student_double_pareto_scales` | Student scales matching the tail constant or variance of a unit shifted double Pareto, for `alpha > 2`. | Standalone call with captured stdout; one convention sentence retained. |
| [incerto-api-reference.md](../../content/incerto-api-reference.md) | `student_entropy` | Differential entropy in nats, with the log determinant of scatter. | Standalone call with captured stdout; one convention sentence retained. |
| [incerto-api-reference.md](../../content/incerto-api-reference.md) | `student_mutual_information` | Bivariate Student mutual information in nats for unit diagonal scatter. | Standalone call with captured stdout; one convention sentence retained. |
| [incerto-api-reference.md](../../content/incerto-api-reference.md) | `subexponential_sum_ratio` | Estimate the two-summand subexponential tail ratio by simulation. | Standalone call with captured stdout; one convention sentence retained. |
| [incerto-api-reference.md](../../content/incerto-api-reference.md) | `survival_from_hazards` | Survival at horizons zero through `N` from `N` conditional hazards in `[0, 1]`. | Standalone call with captured stdout; one convention sentence retained. |
| [incerto-api-reference.md](../../content/incerto-api-reference.md) | `symmetric_spectrum` | Eigenvalues of a finite, exactly symmetric nonempty real square matrix. | Standalone call with captured stdout; one convention sentence retained. |
| [incerto-api-reference.md](../../content/incerto-api-reference.md) | `t_peak_shoulder_tail` | Return Student-t scale-curvature boundaries for tail diagnostics. | Standalone call with captured stdout. |
| [incerto-asymmetric-payoffs.md](../../content/incerto-asymmetric-payoffs.md) | `finite_payoff_mean` | The means are $-0.62$ and $0.62$, despite A’s higher gain frequency. The last line prints the convexity gap $4$ for a spread of two around four. | Existing runnable example paired with captured stdout. |
| [incerto-body-shoulder-tail.md](../../content/incerto-body-shoulder-tail.md) | `normal_peak_shoulder_tail`, `normal_variance_peak_shoulder_tail`, `t_peak_shoulder_tail` | Each line prints four ordered curvature boundaries at unit scale. The normal variance boundaries are approximately $\pm0.7420$ and $\pm2.3344$; they are local perturbation boundaries, not fitted tail thresholds. | Existing runnable example paired with captured stdout. |
| [incerto-counting-exceedances.md](../../content/incerto-counting-exceedances.md) | `empirical_survival_function` | Helper groups ties and returns survival values in the table. | Captured tied-sample output appears with the existing call. |
| [incerto-counting-exceedances.md](../../content/incerto-counting-exceedances.md) | `exceedance_fraction`, `empirical_survival_function` | This prints fractions `[1.0, 0.25, 0.0]` and strict survival values `[(1.0, 0.75), (2.0, 0.25), (4.0, 0.0)]`. Ties form one jump. | Existing runnable example paired with captured stdout. |
| [incerto-decentralization.md](../../content/incerto-decentralization.md) | `split_power_damage_logsf`, `block_failure_summary` | The first two probabilities differ by a factor of eight for the split quadratic-damage model. The dictionaries separately report mean loss, variance, any failure and total failure for independent equal-exposure blocks. | Existing runnable example paired with captured stdout. |
| [incerto-dispersion-ratio.md](../../content/incerto-dispersion-ratio.md) | `dispersion_ratios` | This prints Std/MeanAD and Std/MedianAD for one seeded sample per law. The normal ratios are near one; the Student values illustrate sensitivity to extremes. These are sample diagnostics, not estimates of a tail exponent. | Existing runnable example paired with captured stdout. |
| [incerto-dispersion-ratio.md](../../content/incerto-dispersion-ratio.md) | `dispersion_ratios` | Constant samples return NaN; a positive numerator over zero returns infinity. | Constant, single-outlier, and ordinary samples with both ratios printed. |
| [incerto-double-pareto.md](../../content/incerto-double-pareto.md) | `double_pareto` | Mean/variance reporting by exponent regime. | Loop over alpha = 0.5, 1, 1.5, 2, 3 with printed mean and variance. |
| [incerto-double-pareto.md](../../content/incerto-double-pareto.md) | `double_pareto` | Repeated NaN/+inf convention after matching example. | Convention appears once beside the executed moment-regime example. |
| [incerto-double-pareto.md](../../content/incerto-double-pareto.md) | `double_pareto`, `student_double_pareto_scales` | This prints mean zero, variance one, two right-tail probabilities, and the distinct Student scales that match either the tail constant or variance. | Existing runnable example paired with captured stdout. |
| [incerto-extreme-value-index.md](../../content/incerto-extreme-value-index.md) | `pareto_normalized_maximum_cdf` | This prints exact normalized-maximum CDFs at three points and the Fréchet limit for $\xi=2/3$. The finite-$n$ values are population calculations, not estimates from sampled maxima. | Existing runnable example paired with captured stdout. |
| [incerto-inference-asymmetry.md](../../content/incerto-inference-asymmetry.md) | `repeated_event_probability`, `finite_payoff_mean` | This prints mixture mean 300.49995 and the probability of observing at least one rare component in $n$ independent draws. The baseline mean is 0.5; the component label is detectable here because the supports are disjoint. | Existing runnable example paired with captured stdout. |
| [incerto-iso-density-tail-geometry.md](../../content/incerto-iso-density-tail-geometry.md) | `bivariate_student` | This samples the spherical Cauchy law and compares a sector frequency with the exact probability $1/(6\sqrt{10})\approx0.052705$. The 10,000 seeded draws illustrate an integrated probability, not a density contour level. | Existing runnable example paired with captured stdout. |
| [incerto-lln-preasymptotic.md](../../content/incerto-lln-preasymptotic.md) | `pareto_type1`, `running_mean`, `max_to_sum_ratio` | This prints running means at 100, 1,000 and 5,000 observations and the largest observation’s share of the final total. Only the $\alpha=1.3$ law has a finite population mean, $13/3$; a finite path does not prove convergence. | Existing runnable example paired with captured stdout. |
| [incerto-maximum-entropy.md](../../content/incerto-maximum-entropy.md) | `entropy_log_constraint_example` | The independent integrals give mass one and log moment $1/2$ for both laws. The Pareto entropy is about 0.806853; the entropy gap to the log-gamma competitor equals its positive KL divergence. This checks one worked case, not global optimality. | Existing runnable example paired with captured stdout. |
| [incerto-mixture-uncertainty.md](../../content/incerto-mixture-uncertainty.md) | `normal_mixture_absolute_moment`, `normal_mixture_log_abs_survival` | Both variances are one, while Pearson kurtosis changes from 3 to 77.25. The last value compares absolute exceedance probabilities at four. All moments of these two finite Gaussian mixtures exist. | Existing runnable example paired with captured stdout. |
| [incerto-moment-estimation.md](../../content/incerto-moment-estimation.md) | `pareto_mean_plugin` | Prose formula and infinity branch. | All-cutoff, finite-mean, and infinite-mean fits with printed estimates. |
| [incerto-moment-estimation.md](../../content/incerto-moment-estimation.md) | `pareto_type1`, `pareto_moment_estimator_summary` | This compares 100 second-moment estimates from samples of size 200. The targets are 3 and 1.5; estimator variance is infinite for $\alpha=3$ and finite for $\alpha=6$. Printed quantiles describe this seeded experiment. | Existing runnable example paired with captured stdout. |
| [incerto-multivariate-tails.md](../../content/incerto-multivariate-tails.md) | `bivariate_student`, `sample_correlation`, `student_mutual_information` | This prints a finite sample coefficient and positive population mutual information in nats for each Student law. Diagonal scatter gives zero population correlation only for $\nu=5$ here; at $\nu=1.5$ that population coefficient is undefined. | Existing runnable example paired with captured stdout. |
| [incerto-multivariate-tails.md](../../content/incerto-multivariate-tails.md) | `sample_correlation` | Numerical helper returns NaN on degenerate samples. | Centered constant, uncentered zero, and nondegenerate calls with output. |
| [incerto-nyc-dog-name-tail.md](../../content/incerto-nyc-dog-name-tail.md) | `load_nyc_dog_name_frequencies`, `DogNameFrequencyData.frequency_for` | Script prints the license-period frequency of Safari. | Case/whitespace variants with actual lookup results. |
| [incerto-nyc-dog-name-tail.md](../../content/incerto-nyc-dog-name-tail.md) | `load_nyc_dog_name_frequencies`, `hill_stability` | The bundled aggregate is read locally in an editable checkout. This prints 34,680 names, 789,724 license-period records, Safari’s frequency of 3, and Hill exponents near `[1.896, 1.287, 1.056]`. No individual records are fetched. | Existing runnable example paired with captured stdout. |
| [incerto-pareto.md](../../content/incerto-pareto.md) | `pareto_product_logsf` | This prints exact product survivals for independent unit-minimum Paretos. Equal exponents introduce the logarithmic factor derived above. | Existing runnable example paired with captured stdout. |
| [incerto-pareto.md](../../content/incerto-pareto.md) | `pareto_tail_quantities` | Each dictionary gives log survival, mean excess, conditional mean and tail first moment. At $\alpha=1.5$ the last three are 8, 12 and 1.5; at $\alpha=1$ all three expectations are infinite. | Existing runnable example paired with captured stdout. |
| [incerto-pareto-moment-existence.md](../../content/incerto-pareto-moment-existence.md) | `pareto_truncated_moment` | The rows evaluate $\mathbb E[X^p\mathbf1_{\{X\le b\}}]$ at three cutoffs. For $p=1$ the values approach 3; at $p=1.5$ they grow logarithmically, and at $p=2$ they grow as a power. No sample is censored. | Existing runnable example paired with captured stdout. |
| [incerto-plug-in-tail-estimation.md](../../content/incerto-plug-in-tail-estimation.md) | `pareto_mean_plugin` | Infinity reporting and all-cutoff limiting convention. | All-cutoff, finite-mean, and infinite-mean calls with captured stdout. |
| [incerto-ruin.md](../../content/incerto-ruin.md) | `survival_from_hazards`, `absorbing_resource_path` | This prints survival `[1, 0.98, 0.9604, 0.941192]`. Reversing the same increments changes the resource path from `[3, 0, 0]` to `[3, 7, 3]`: ruin is absorbing. | Existing runnable example paired with captured stdout. |
| [incerto-scoft-ch1.md](../../content/incerto-scoft-ch1.md) | `bounded_spike_summary` | The dictionaries show variance one and Pearson kurtoses 10, 100 and 1,000. Every law has bounded support, so large kurtosis alone does not establish a heavy asymptotic tail. | Existing runnable example paired with captured stdout. |
| [incerto-scoft-ch2.md](../../content/incerto-scoft-ch2.md) | `empirical_survival_function`, `pareto_tail_quantities` | The first line prints the empirical support and strict survival. The second distinguishes mean excess 8, conditional mean 12 and unconditional tail contribution 1.5 under the specified Pareto model. | Existing runnable example paired with captured stdout. |
| [incerto-scoft-ch2.md](../../content/incerto-scoft-ch2.md) | `pareto_tail_quantities` | Helper reports mathematical infinity when alpha <= 1. | Existing example expanded across infinite- and finite-mean regimes. |
| [incerto-scoft-ch2.md](../../content/incerto-scoft-ch2.md) | `pareto_tail_quantities` | Repeated helper implementation/output paragraph. | Moment regimes shown in the executed example; CDF rounding caveat retained. |
| [incerto-scoft-ch3.md](../../content/incerto-scoft-ch3.md) | `repeated_event_probability`, `finite_payoff_mean` | This prints detection probability about 0.09517 for 1,000 independent trials, followed by expected payoff $-0.62$ despite a 98% gain frequency. | Existing runnable example paired with captured stdout. |
| [incerto-scoft-ch4.md](../../content/incerto-scoft-ch4.md) | `normal_mixture_absolute_moment`, `power_mean` | This prints second moment 1, fourth moment 77.25, and normalized power means 1, 2 and approximately 2.8284. The finite mixture and the fixed vector answer different moment and norm questions. | Existing runnable example paired with captured stdout. |
| [incerto-scoft-ch5.md](../../content/incerto-scoft-ch5.md) | `pareto_truncated_moment`, `q_exponential_logsf` | The first row shows logarithmic growth at the Pareto moment boundary. The remaining rows are log survivals: `-inf` at the compact endpoint for $q=0.75$ means zero survival, rather than a failed numerical calculation. | Existing runnable example paired with captured stdout. |
| [incerto-scoft-ch6.md](../../content/incerto-scoft-ch6.md) | `student_mutual_information`, `regression_population_r2`, `symmetric_spectrum` | This prints about 0.224171 nats of dependence despite diagonal scatter, the finite-variance regression target $1/4$, and eigenvalues $[-2,2]$ of an explicitly symmetric matrix. No random-matrix limit is inferred. | Existing runnable example paired with captured stdout. |
| [incerto-sp500-tail.md](../../content/incerto-sp500-tail.md) | `DatasetNotAvailable`, `load_sp500_prices`, `hill_alpha_estimator`, `mean_excess` | Without a local cache this prints an availability message. With one, it prints the date window, loss count, Hill estimates and empirical mean excess. Results depend on that local sample; no data are downloaded or written. The same diagnostics are available as `uv run python demos/incerto/sp500_tail.py`. | Existing runnable example paired with captured stdout. |
| [incerto-survival-tail-ratio.md](../../content/incerto-survival-tail-ratio.md) | `pareto_type1`, `iid_two_sum_tail` | The first row compares two exceedances of $u$ with one exceedance of $2u$. The second computes the separate convolution ratio $P(X_1+X_2>u)/(2\bar F(u))$ and checks quadrature success. | Existing runnable example paired with captured stdout. |
| [incerto-tail-class-catalog.md](../../content/incerto-tail-class-catalog.md) | `normal_location_mixture_kurtosis`, `survival_from_hazards` | This prints kurtosis 1.72 and two finite-horizon intact probabilities. The decreasing-hazard value stays above $1/2$; neither example asserts a power-tail law. | Existing runnable example paired with captured stdout. |
| [incerto-tail-class-catalog.md](../../content/incerto-tail-class-catalog.md) | `pareto_type1`, `log_survival_multiplier_ratio` | This prints log multiplier ratios at three thresholds. The exact Pareto row is constant at $-2.5\log 2$; the other rows change with the threshold. A finite grid illustrates the specified laws and cannot classify unknown data. | Existing runnable example paired with captured stdout. |

### Follow-up verification

- Full `UV_CACHE_DIR=/tmp/m05-uv-cache uv run pytest`: **637 passed in
  56.35 s**, including all 90 exact stdout comparisons, API links, output
  pairing, whitespace-comparison regression checks and both financial-data
  branches. The writable cache is required by this sandbox.
- `git diff --check` passed. Reviewed the incremental content/test diff and
  the complete untracked test and record. Separate whitespace checks passed
  for all 32 files changed in this pass. Relative links and all 72 unique
  API anchors resolve; prior display equations, external URLs and citation
  keys are preserved. All 90 Python fences have adjacent Output fences.
- Site build, HTML checks and browser review were not rerun in this pass;
  the initial pass's MyST preflight and browser sandbox blockers remain
  unresolved. No rendered-page verification is claimed.
- This pass changes 30 public Markdown pages, the existing untracked snippet
  test and this record. Earlier attribution removals, API anchors, runnable
  code, chapter-6 figure fixes and demo changes are retained. No repository
  files were deleted and no staging, commit, push, transfer or publication
  was performed.
