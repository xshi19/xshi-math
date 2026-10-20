---
title: Python API
---

The installed distribution is `xshi-math`; these helpers are imported as
`xmath.incerto`. Install the numerical and plotting extra with:

```sh
uv sync --locked --extra incerto
```

Run page examples in Python after installing from a repository checkout.
Every fenced `python` block on the Incerto pages is executed by pytest;
examples do not fetch data or save files. Each **Output** block is captured
from its preceding example and checked against stdout, ignoring trailing
whitespace only. Bundled dataset examples require an
editable checkout (or a populated `INCERTO_DATA_DIR`). Longer examples expand
under a **Code** dropdown.

The base `xmath` helpers require only NumPy. The Incerto extra adds SciPy and
Matplotlib; graph generation uses NetworkX and PyYAML from the development
group. Dataset fetching uses standard-library `urllib`. The Python modules
contain the full signatures and docstrings; there is no separate Sphinx build.
Browse the [module sources](https://github.com/xshi19/xshi-math/tree/main/src/math/incerto)
for implementations and use local `help()` for the installed version.

| Module | Entry points and purpose |
| --- | --- |
| `xmath.incerto.datasets` | [`load_amazon_bookrank`](incerto-api-reference.md#api-load-amazon-bookrank), [`load_nyc_dog_name_frequencies`](incerto-api-reference.md#api-load-nyc-dog-name-frequencies), [`load_sp500_prices`](incerto-api-reference.md#api-load-sp500-prices); explicit local-cache and refresh helpers |
| `xmath.incerto.distributions` | [`pareto_type1`](incerto-api-reference.md#api-pareto-type1), [`double_pareto`](incerto-api-reference.md#api-double-pareto), [`hypsecant2`](incerto-api-reference.md#api-hypsecant2), [`simple_normal_mixture`](incerto-api-reference.md#api-simple-normal-mixture), [`univariate_variance_gamma`](incerto-api-reference.md#api-univariate-variance-gamma); SciPy-style distribution objects |
| `xmath.incerto.estimators` | [`hill_estimator`](incerto-api-reference.md#api-hill-estimator) (extreme-value index), [`hill_alpha_estimator`](incerto-api-reference.md#api-hill-alpha-estimator) (reciprocal exponent), [`hill_stability`](incerto-api-reference.md#api-hill-stability), [`pareto_mean_plugin`](incerto-api-reference.md#api-pareto-mean-plugin), [`mean_excess`](incerto-api-reference.md#api-mean-excess), [`running_mean`](incerto-api-reference.md#api-running-mean), [`max_to_sum_ratio`](incerto-api-reference.md#api-max-to-sum-ratio) |
| `xmath.incerto.stats` | Gaussian-calibrated [`dispersion_ratios`](incerto-api-reference.md#api-dispersion-ratios), [`mean_absolute_deviation`](incerto-api-reference.md#api-mean-absolute-deviation), [`median_absolute_deviation`](incerto-api-reference.md#api-median-absolute-deviation); normal and Student-t shoulder boundaries; [`empirical_survival_function`](incerto-api-reference.md#api-empirical-survival-function) (strict exceedance with ties) and [`lognorm_params_from_mean_and_variance`](incerto-api-reference.md#api-lognorm-params-from-mean-and-variance) |
| `xmath.incerto.tail_diagnostics` | [`regular_variation_ratio`](incerto-api-reference.md#api-regular-variation-ratio), [`iid_two_sum_tail`](incerto-api-reference.md#api-iid-two-sum-tail), [`subexponential_sum_ratio`](incerto-api-reference.md#api-subexponential-sum-ratio); numerical calculations with support and integration checks |
| `xmath.incerto.tail_classes` | [`bounded_spike_summary`](incerto-api-reference.md#api-bounded-spike-summary) (population moments), [`log_survival_multiplier_ratio`](incerto-api-reference.md#api-log-survival-multiplier-ratio) (log-domain tail ratios); used by the [Prologue models](incerto-scoft-ch1.md) |
| `xmath.incerto.glossary` | [`pareto_tail_quantities`](incerto-api-reference.md#api-pareto-tail-quantities) (log survival, conditional means, tail contribution), [`pareto_normalized_maximum_cdf`](incerto-api-reference.md#api-pareto-normalized-maximum-cdf) (exact iid maximum law); [chapter 2 worked cases](incerto-scoft-ch2.md#scoft-ch2-demo) |
| `xmath.incerto.lecture_risk` | [`repeated_event_probability`](incerto-api-reference.md#api-repeated-event-probability), [`survival_from_hazards`](incerto-api-reference.md#api-survival-from-hazards), [`finite_payoff_mean`](incerto-api-reference.md#api-finite-payoff-mean), [`absorbing_resource_path`](incerto-api-reference.md#api-absorbing-resource-path), [`split_power_damage_logsf`](incerto-api-reference.md#api-split-power-damage-logsf), [`block_failure_summary`](incerto-api-reference.md#api-block-failure-summary); [chapter 3 worked models](incerto-scoft-ch3.md#scoft-ch3-demo) |
| `xmath.incerto.finite_moments` | [`normal_mixture_log_density`](incerto-api-reference.md#api-normal-mixture-log-density), [`normal_mixture_log_abs_survival`](incerto-api-reference.md#api-normal-mixture-log-abs-survival), [`normal_mixture_absolute_moment`](incerto-api-reference.md#api-normal-mixture-absolute-moment), [`pareto_moment_estimator_summary`](incerto-api-reference.md#api-pareto-moment-estimator-summary), [`power_mean`](incerto-api-reference.md#api-power-mean); [finite-moment worked cases](incerto-scoft-ch4.md#worked-cases) |
| `xmath.incerto.multivariate` | [`student_entropy`](incerto-api-reference.md#api-student-entropy), [`student_mutual_information`](incerto-api-reference.md#api-student-mutual-information), [`bivariate_student`](incerto-api-reference.md#api-bivariate-student), [`sample_correlation`](incerto-api-reference.md#api-sample-correlation), [`symmetric_spectrum`](incerto-api-reference.md#api-symmetric-spectrum), [`regression_population_r2`](incerto-api-reference.md#api-regression-population-r2), [`normal_location_mixture_kurtosis`](incerto-api-reference.md#api-normal-location-mixture-kurtosis); [chapter 6 worked cases](incerto-scoft-ch6.md#scoft-ch6-demo). Student helpers deliberately restrict degrees of freedom to [0.5, 1000]. |
| `xmath.incerto.figures` | [`set_theme`](incerto-api-reference.md#api-set-theme), [`style_axes`](incerto-api-reference.md#api-style-axes), [`savefig`](incerto-api-reference.md#api-savefig); shared figure style and deterministic export helpers |
| `xmath.incerto.power_laws` | [`pareto_product_logsf`](incerto-api-reference.md#api-pareto-product-logsf), [`pareto_truncated_moment`](incerto-api-reference.md#api-pareto-truncated-moment), [`student_double_pareto_scales`](incerto-api-reference.md#api-student-double-pareto-scales), [`q_exponential_logsf`](incerto-api-reference.md#api-q-exponential-logsf), [`entropy_log_constraint_example`](incerto-api-reference.md#api-entropy-log-constraint-example); [chapter 5 worked cases](incerto-scoft-ch5.md#scoft-ch5-demo) |

Use [`pareto_type1`](incerto-api-reference.md#api-pareto-type1) and
[`hill_alpha_estimator`](incerto-api-reference.md#api-hill-alpha-estimator).

```python
import numpy as np
from xmath.incerto.distributions import pareto_type1
from xmath.incerto.estimators import hill_alpha_estimator

rng = np.random.default_rng(20261017)
x = pareto_type1.rvs(2.5, size=1000, random_state=rng)
alpha_hat = hill_alpha_estimator(x, k=100)
print("Estimated alpha:", round(alpha_hat, 3))
```

**Output**

```text
Estimated alpha: 2.405
```

The example is a simulation, not a guarantee about estimation accuracy.
The [Hill note](incerto-hill-estimator.md) states the model and threshold
assumptions. Use `help()` on an imported function for argument validation,
return types, and numerical limits.

The [empirical examples](incerto-empirical-example-concepts.md) link to committed
demo scripts and static figures. Dataset loading does not fetch by default.
The [S&P method](incerto-sp500-tail.md) explains the deliberately absent financial
cache. The separate [Normix API](https://xshi19.github.io/normix/) remains
maintained upstream; this educational package does not vendor Normix.

## Function reference

Signatures omit type annotations for readability; keyword-only markers and
defaults match the installed helpers. See local `help()` for validation and
return details. Distribution objects use SciPy’s frozen-law interface.

### Datasets

Module: `xmath.incerto.datasets`.

(api-datasetnotavailable)=
#### [`DatasetNotAvailable`](incerto-api-reference.md#api-datasetnotavailable)

Raised when a dataset is missing or a fetch cannot provide usable data.

(api-priceseries)=
#### [`PriceSeries`](incerto-api-reference.md#api-priceseries)

Daily close-price series used by empirical examples.

(api-priceseries-log-returns)=
#### [`PriceSeries.log_returns`](incerto-api-reference.md#api-priceseries-log-returns)

`PriceSeries.log_returns()`

```python
import numpy as np
from xmath.incerto.datasets import PriceSeries

prices = PriceSeries(
    name="synthetic", date=np.array(["2020-01-01", "2020-01-02", "2020-01-03"], dtype="datetime64[D]"),
    close=np.array([100., 90., 99.]), source="synthetic example",
)
dates, values = prices.log_returns()
print("Ending dates:", dates)
print("Log returns:", values.round(6))
```

**Output**

```text
Ending dates: ['2020-01-02' '2020-01-03']
Log returns: [-0.105361  0.09531 ]
```


(api-priceseries-negative-log-returns)=
#### [`PriceSeries.negative_log_returns`](incerto-api-reference.md#api-priceseries-negative-log-returns)

`PriceSeries.negative_log_returns()`

```python
import numpy as np
from xmath.incerto.datasets import PriceSeries

prices = PriceSeries(
    name="synthetic", date=np.array(["2020-01-01", "2020-01-02", "2020-01-03"], dtype="datetime64[D]"),
    close=np.array([100., 90., 99.]), source="synthetic example",
)
dates, values = prices.negative_log_returns()
print("Ending dates:", dates)
print("Positive losses:", values.round(6))
```

**Output**

```text
Ending dates: ['2020-01-02']
Positive losses: [0.105361]
```


(api-bookrankdata)=
#### [`BookRankData`](incerto-api-reference.md#api-bookrankdata)

Amazon book sales-rank observations.

(api-dognamefrequencydata)=
#### [`DogNameFrequencyData`](incerto-api-reference.md#api-dognamefrequencydata)

Normalized NYC dog-name frequencies from license-period records.

(api-dognamefrequencydata-frequency-for)=
#### [`DogNameFrequencyData.frequency_for`](incerto-api-reference.md#api-dognamefrequencydata-frequency-for)

`DogNameFrequencyData.frequency_for(name)`

```python
import numpy as np
from xmath.incerto.datasets import DogNameFrequencyData

names = DogNameFrequencyData(np.array(["SAFARI"]), np.array([3]), "synthetic example")
for name in ("Safari", " safari ", "MISSING"):
    print(repr(name), names.frequency_for(name))
```

**Output**

```text
'Safari' 3
' safari ' 3
'MISSING' 0
```


(api-data-root)=
#### [`data_root`](incerto-api-reference.md#api-data-root)

`data_root(data_dir=None)`

```python
from xmath.incerto.datasets import data_root

print(data_root(data_dir="/tmp/incerto-example-data").as_posix())
```

**Output**

```text
/tmp/incerto-example-data
```


(api-snapshot-path)=
#### [`snapshot_path`](incerto-api-reference.md#api-snapshot-path)

`snapshot_path(filename, data_dir=None)`

```python
from xmath.incerto.datasets import snapshot_path

print(snapshot_path("example.csv", data_dir="/tmp/incerto-example-data").as_posix())
```

**Output**

```text
/tmp/incerto-example-data/snapshots/example.csv
```


(api-cache-path)=
#### [`cache_path`](incerto-api-reference.md#api-cache-path)

`cache_path(filename, data_dir=None)`

```python
from xmath.incerto.datasets import cache_path

print(cache_path("example.csv", data_dir="/tmp/incerto-example-data").as_posix())
```

**Output**

```text
/tmp/incerto-example-data/cache/example.csv
```


(api-load-sp500-prices)=
#### [`load_sp500_prices`](incerto-api-reference.md#api-load-sp500-prices)

`load_sp500_prices(*, data_dir=None, fetch=False)`

Load S&P 500 daily closes from the local cache, optionally fetching FRED.

(api-load-amazon-bookrank)=
#### [`load_amazon_bookrank`](incerto-api-reference.md#api-load-amazon-bookrank)

`load_amazon_bookrank(*, data_dir=None)`

Load the CC0 Amazon book sales-rank snapshot.

(api-load-nyc-dog-name-frequencies)=
#### [`load_nyc_dog_name_frequencies`](incerto-api-reference.md#api-load-nyc-dog-name-frequencies)

`load_nyc_dog_name_frequencies(*, data_dir=None)`

Load the NYC Open Data dog-name frequency snapshot.

(api-write-sp500-fred-cache)=
#### [`write_sp500_fred_cache`](incerto-api-reference.md#api-write-sp500-fred-cache)

`write_sp500_fred_cache(destination, *, url=FRED_SP500_CSV_URL)`

Fetch and clean the public FRED S&P 500 CSV into an untracked cache.

(api-write-sp500-cache-from-csv)=
#### [`write_sp500_cache_from_csv`](incerto-api-reference.md#api-write-sp500-cache-from-csv)

`write_sp500_cache_from_csv(source, destination)`

Clean a local S&P 500-like CSV into the standard untracked cache.

(api-write-amazon-bookrank-snapshot)=
#### [`write_amazon_bookrank_snapshot`](incerto-api-reference.md#api-write-amazon-bookrank-snapshot)

`write_amazon_bookrank_snapshot(destination, *, url=KAGGLE_AMAZON_BOOKRANK_DOWNLOAD_URL)`

Fetch and clean the CC0 Kaggle Amazon bookrank dataset.

(api-write-nyc-dog-name-frequency-snapshot)=
#### [`write_nyc_dog_name_frequency_snapshot`](incerto-api-reference.md#api-write-nyc-dog-name-frequency-snapshot)

`write_nyc_dog_name_frequency_snapshot(destination, *, url=NYC_DOG_NAME_FREQUENCY_API_URL)`

Fetch the server-aggregated NYC dog-name frequencies into a snapshot.

### Distributions

Module: `xmath.incerto.distributions`.

Call an object below with its shape parameters to freeze a law; then use
`pdf(x)`, `logpdf(x)`, `cdf(x)`, `sf(x)`, `logsf(x)`, `ppf(q)`,
`rvs(size=..., random_state=rng)` or `stats(moments="mv")`.
These methods belong to the linked distribution entry. `scale` is a
positive scale multiplier, and `loc` shifts the support.

(api-pareto-type1)=
#### [`pareto_type1`](incerto-api-reference.md#api-pareto-type1)

`pareto_type1(alpha, loc=0, scale=1)`

Pareto Type I with positive exponent `alpha`; at `loc=0`, `scale` is the lower cutoff.

(api-double-pareto)=
#### [`double_pareto`](incerto-api-reference.md#api-double-pareto)

`double_pareto(alpha, loc=0, scale=1)`

Symmetric shifted double Pareto with positive exponent `alpha`; ordinary mean exists only above one.

(api-hypsecant2)=
#### [`hypsecant2`](incerto-api-reference.md#api-hypsecant2)

`hypsecant2(loc=0, scale=1)`

Density `0.5 / cosh(x)**2` at default location and scale (logistic scale one half).

(api-simple-normal-mixture)=
#### [`simple_normal_mixture`](incerto-api-reference.md#api-simple-normal-mixture)

`simple_normal_mixture(a, loc=0, scale=1)`

Equal centered normal mixture with component variances `1-a` and `1+a`, for `0 <= a < 1`.

(api-univariate-variance-gamma)=
#### [`univariate_variance_gamma`](incerto-api-reference.md#api-univariate-variance-gamma)

`univariate_variance_gamma(alpha, beta, lam, loc=0, scale=1)`

Variance–gamma law requiring `alpha > abs(beta)` and `lam > 0`; this `alpha` is a decay parameter, not a Pareto exponent.

(api-hypsecant2-chf)=
#### [`hypsecant2.chf`](incerto-api-reference.md#api-hypsecant2-chf)

`hypsecant2.chf(t, loc=0.0, scale=1.0)`

```python
from xmath.incerto.distributions import hypsecant2

print(hypsecant2.chf([0, 1, 2]).round(6))
```

**Output**

```text
[1.      +0.j 0.682569+0.j 0.272029+0.j]
```


### Estimators

Module: `xmath.incerto.estimators`.

(api-hill-estimator)=
#### [`hill_estimator`](incerto-api-reference.md#api-hill-estimator)

`hill_estimator(x, k)`

```python
from xmath.incerto.estimators import hill_estimator

print("xi:", round(hill_estimator([1, 2, 4, 8], k=2), 6))
```

**Output**

```text
xi: 1.039721
```


(api-hill-alpha-estimator)=
#### [`hill_alpha_estimator`](incerto-api-reference.md#api-hill-alpha-estimator)

`hill_alpha_estimator(x, k)`

```python
from xmath.incerto.estimators import hill_alpha_estimator

for sample in ([1, 2, 4, 8], [1, 1, 1, 1]):
    print(sample, "alpha:", round(hill_alpha_estimator(sample, k=2), 6))
```

**Output**

```text
[1, 2, 4, 8] alpha: 0.961797
[1, 1, 1, 1] alpha: inf
```


(api-pareto-mean-plugin)=
#### [`pareto_mean_plugin`](incerto-api-reference.md#api-pareto-mean-plugin)

`pareto_mean_plugin(x, *, x_m, axis=None)`

```python
from xmath.incerto.estimators import pareto_mean_plugin

for sample in ([1, 1], [1, 2], [4, 4]):
    print(sample, round(pareto_mean_plugin(sample, x_m=1), 6))
```

**Output**

```text
[1, 1] 1.0
[1, 2] 1.530394
[4, 4] inf
```

The cutoff is known; statistical calibration assumes an exact iid Pareto model.


(api-hill-stability)=
#### [`hill_stability`](incerto-api-reference.md#api-hill-stability)

`hill_stability(x, k_values=None, *, num=100)`

```python
from xmath.incerto.estimators import hill_stability

for name, values in hill_stability([1, 2, 4, 8], [1, 2]).items():
    print(name, values.round(6))
```

**Output**

```text
k [1. 2.]
xi [0.693147 1.039721]
alpha [1.442695 0.961797]
```


(api-running-mean)=
#### [`running_mean`](incerto-api-reference.md#api-running-mean)

`running_mean(x, axis=None)`

```python
from xmath.incerto.estimators import running_mean

print(running_mean([1, 2, 6]))
print(running_mean([[1, 2, 6], [2, 4, 12]], axis=1))
```

**Output**

```text
[1.  1.5 3. ]
[[1.  1.5 3. ]
 [2.  3.  6. ]]
```


(api-max-to-sum-ratio)=
#### [`max_to_sum_ratio`](incerto-api-reference.md#api-max-to-sum-ratio)

`max_to_sum_ratio(x, axis=None)`

```python
from xmath.incerto.estimators import max_to_sum_ratio

print(max_to_sum_ratio([1, 2, 7]))
```

**Output**

```text
0.7
```


(api-mean-excess)=
#### [`mean_excess`](incerto-api-reference.md#api-mean-excess)

`mean_excess(x, thresholds, *, min_exceedances=1)`

```python
from xmath.incerto.estimators import mean_excess

for name, values in mean_excess([1, 2, 2, 4], [1, 2, 4]).items():
    print(name, values)
```

**Output**

```text
threshold [1. 2. 4.]
mean_excess [1.66666667 2.                nan]
exceedances [3. 1. 0.]
```


### Stats

Module: `xmath.incerto.stats`.

(api-mean-absolute-deviation)=
#### [`mean_absolute_deviation`](incerto-api-reference.md#api-mean-absolute-deviation)

`mean_absolute_deviation(x, axis=None)`

```python
from xmath.incerto.stats import mean_absolute_deviation

print("Gaussian-calibrated MeanAD:", round(mean_absolute_deviation([1, 2, 3]), 6))
```

**Output**

```text
Gaussian-calibrated MeanAD: 0.835543
```


(api-median-absolute-deviation)=
#### [`median_absolute_deviation`](incerto-api-reference.md#api-median-absolute-deviation)

`median_absolute_deviation(x, axis=None)`

```python
from xmath.incerto.stats import median_absolute_deviation

print("Gaussian-calibrated MedianAD:", round(median_absolute_deviation([1, 2, 3]), 6))
```

**Output**

```text
Gaussian-calibrated MedianAD: 1.482602
```


(api-normal-peak-shoulder-tail)=
#### [`normal_peak_shoulder_tail`](incerto-api-reference.md#api-normal-peak-shoulder-tail)

`normal_peak_shoulder_tail(mu=0.0, sigma=1.0)`

```python
from xmath.incerto.stats import normal_peak_shoulder_tail

print("Normal scale boundaries:", normal_peak_shoulder_tail().round(6))
```

**Output**

```text
Normal scale boundaries: [-2.135779 -0.662153  0.662153  2.135779]
```


(api-normal-variance-peak-shoulder-tail)=
#### [`normal_variance_peak_shoulder_tail`](incerto-api-reference.md#api-normal-variance-peak-shoulder-tail)

`normal_variance_peak_shoulder_tail(mu=0.0, variance=1.0)`

```python
from xmath.incerto.stats import normal_variance_peak_shoulder_tail

print("Normal variance boundaries:", normal_variance_peak_shoulder_tail().round(6))
```

**Output**

```text
Normal variance boundaries: [-2.334414 -0.741964  0.741964  2.334414]
```


(api-t-peak-shoulder-tail)=
#### [`t_peak_shoulder_tail`](incerto-api-reference.md#api-t-peak-shoulder-tail)

`t_peak_shoulder_tail(df, mu=0.0, sigma=1.0)`

```python
from xmath.incerto.stats import t_peak_shoulder_tail

print("Student-3 scale boundaries:", t_peak_shoulder_tail(3).round(6))
```

**Output**

```text
Student-3 scale boundaries: [-2.757816 -0.628052  0.628052  2.757816]
```


(api-lognorm-params-from-mean-and-variance)=
#### [`lognorm_params_from_mean_and_variance`](incerto-api-reference.md#api-lognorm-params-from-mean-and-variance)

`lognorm_params_from_mean_and_variance(mean, variance)`

```python
from xmath.incerto.stats import lognorm_params_from_mean_and_variance

mu, sigma = lognorm_params_from_mean_and_variance(mean=2, variance=3)
print(f"Log-location: {mu:.6f}; log-scale: {sigma:.6f}")
```

**Output**

```text
Log-location: 0.413339; log-scale: 0.748075
```


(api-empirical-survival-function)=
#### [`empirical_survival_function`](incerto-api-reference.md#api-empirical-survival-function)

`empirical_survival_function(x)`

```python
from xmath.incerto.stats import empirical_survival_function

support, survival = empirical_survival_function([1, 2, 2, 4])
print("Support:", support)
print("Strict survival:", survival)
```

**Output**

```text
Support: [1. 2. 4.]
Strict survival: [0.75 0.25 0.  ]
```


(api-dispersion-ratios)=
#### [`dispersion_ratios`](incerto-api-reference.md#api-dispersion-ratios)

`dispersion_ratios(sample)`

```python
from xmath.incerto.stats import dispersion_ratios

for sample in ([2, 2, 2], [0, 0, 10], [1, 2, 3]):
    mean_ratio, median_ratio = dispersion_ratios(sample)
    print(f"{sample}: Std/MeanAD={mean_ratio:.6g}, Std/MedianAD={median_ratio:.6g}")
```

**Output**

```text
[2, 2, 2]: Std/MeanAD=nan, Std/MedianAD=nan
[0, 0, 10]: Std/MeanAD=0.846284, Std/MedianAD=inf
[1, 2, 3]: Std/MeanAD=0.977205, Std/MedianAD=0.550719
```

Standard deviation uses `ddof=0`; both absolute deviations are Gaussian-calibrated.


### Tail diagnostics

Module: `xmath.incerto.tail_diagnostics`.

(api-regular-variation-ratio)=
#### [`regular_variation_ratio`](incerto-api-reference.md#api-regular-variation-ratio)

`regular_variation_ratio(survival, thresholds, *, multiplier=2.0)`

```python
from xmath.incerto.distributions import pareto_type1
from xmath.incerto.tail_diagnostics import regular_variation_ratio

result = regular_variation_ratio(pareto_type1(2).sf, [2, 4], multiplier=2)
for name, values in result.items():
    print(name, values)
```

**Output**

```text
threshold [2. 4.]
survival [0.25   0.0625]
multiplied_survival [0.0625   0.015625]
ratio [0.25 0.25]
```


(api-iid-two-sum-tail)=
#### [`iid_two_sum_tail`](incerto-api-reference.md#api-iid-two-sum-tail)

`iid_two_sum_tail(rv, thresholds, *, rtol=1e-10, maxlevel=12)`

```python
from xmath.incerto.distributions import pareto_type1
from xmath.incerto.tail_diagnostics import iid_two_sum_tail

result = iid_two_sum_tail(pareto_type1(1.5), [3, 10, 100])
print("Fields:", ", ".join(result))
print("Two-sum ratio:", result["ratio"].round(6))
print("Quadrature success:", result["success"])
```

**Output**

```text
Fields: x, threshold, log_tail, tail, log_ratio, ratio, success, log_abs_error, nfev
Two-sum ratio: [1.769076 1.391402 1.044435]
Quadrature success: [ True  True  True]
```


(api-subexponential-sum-ratio)=
#### [`subexponential_sum_ratio`](incerto-api-reference.md#api-subexponential-sum-ratio)

`subexponential_sum_ratio(sampler, survival, thresholds, *, sample_size=100000, random_state=None)`

```python
from xmath.incerto.distributions import pareto_type1
from xmath.incerto.tail_diagnostics import subexponential_sum_ratio

law = pareto_type1(1.5)
result = subexponential_sum_ratio(
    law.rvs, law.sf, [3, 10], sample_size=10000, random_state=20261020,
)
for name, values in result.items():
    print(name, values.round(6))
```

**Output**

```text
threshold [ 3. 10.]
single_tail [0.19245  0.031623]
sum_tail [0.6793 0.0875]
ratio [1.764873 1.383496]
sum_exceedances [6793.  875.]
```

These seeded Monte Carlo values are finite-sample diagnostics.


### Tail classes

Module: `xmath.incerto.tail_classes`.

(api-bounded-spike-summary)=
#### [`bounded_spike_summary`](incerto-api-reference.md#api-bounded-spike-summary)

`bounded_spike_summary(epsilon)`

```python
from xmath.incerto.tail_classes import bounded_spike_summary

for name, value in bounded_spike_summary(0.01).items():
    print(name, round(value, 6))
```

**Output**

```text
support_radius 10.0
mean 0.0
variance 1.0
kurtosis 100.0
```

The symmetric three-point law has total nonzero probability `epsilon`.


(api-log-survival-multiplier-ratio)=
#### [`log_survival_multiplier_ratio`](incerto-api-reference.md#api-log-survival-multiplier-ratio)

`log_survival_multiplier_ratio(log_survival, thresholds, *, multiplier=2.0)`

```python
from xmath.incerto.distributions import pareto_type1
from xmath.incerto.tail_classes import log_survival_multiplier_ratio

print(log_survival_multiplier_ratio(pareto_type1(2).logsf, [2, 10, 100]).round(6))
```

**Output**

```text
[-1.386294 -1.386294 -1.386294]
```


### Glossary

Module: `xmath.incerto.glossary`.

(api-pareto-tail-quantities)=
#### [`pareto_tail_quantities`](incerto-api-reference.md#api-pareto-tail-quantities)

`pareto_tail_quantities(alpha, x_m, threshold)`

```python
from xmath.incerto.glossary import pareto_tail_quantities

for alpha in (1, 1.5):
    result = pareto_tail_quantities(alpha, x_m=1, threshold=4)
    print(alpha, {name: round(value, 6) for name, value in result.items()})
```

**Output**

```text
1 {'log_survival': -1.386294, 'mean_excess': inf, 'conditional_mean': inf, 'tail_first_moment': inf}
1.5 {'log_survival': -2.079442, 'mean_excess': 8.0, 'conditional_mean': 12.0, 'tail_first_moment': 1.5}
```


(api-pareto-normalized-maximum-cdf)=
#### [`pareto_normalized_maximum_cdf`](incerto-api-reference.md#api-pareto-normalized-maximum-cdf)

`pareto_normalized_maximum_cdf(y, *, alpha, n)`

```python
from xmath.incerto.glossary import pareto_normalized_maximum_cdf

for n in (1, 4, 16):
    print(n, pareto_normalized_maximum_cdf([0.5, 1, 2], alpha=1.5, n=n).round(6))
```

**Output**

```text
1 [0.       0.       0.646447]
4 [0.007359 0.316406 0.690621]
16 [0.044492 0.356074 0.69941 ]
```

The maximum is divided by $x_m n^{1/\alpha}$ under an exact iid Pareto model.


### Lecture risk

Module: `xmath.incerto.lecture_risk`.

(api-repeated-event-probability)=
#### [`repeated_event_probability`](incerto-api-reference.md#api-repeated-event-probability)

`repeated_event_probability(probability, trials)`

```python
from xmath.incerto.lecture_risk import repeated_event_probability

for trials in (0, 1, 1000):
    print(trials, round(repeated_event_probability(1e-4, trials), 6))
```

**Output**

```text
0 0.0
1 0.0001
1000 0.095167
```

Trials are independent with the same event probability.


(api-survival-from-hazards)=
#### [`survival_from_hazards`](incerto-api-reference.md#api-survival-from-hazards)

`survival_from_hazards(hazards)`

```python
from xmath.incerto.lecture_risk import survival_from_hazards

print(survival_from_hazards([0.02] * 3))
```

**Output**

```text
[1.       0.98     0.9604   0.941192]
```

The initial survival is included; inputs are conditional hazards.


(api-finite-payoff-mean)=
#### [`finite_payoff_mean`](incerto-api-reference.md#api-finite-payoff-mean)

`finite_payoff_mean(probabilities, payoffs)`

```python
from xmath.incerto.lecture_risk import finite_payoff_mean

print(finite_payoff_mean([0.98, 0.02], [1, -80]))
```

**Output**

```text
-0.6200000000000001
```

Probabilities must sum to one; there is no implicit normalization.


(api-absorbing-resource-path)=
#### [`absorbing_resource_path`](incerto-api-reference.md#api-absorbing-resource-path)

`absorbing_resource_path(initial, increments)`

```python
from xmath.incerto.lecture_risk import absorbing_resource_path

for increments in ([-4, 4], [4, -4]):
    print(increments, absorbing_resource_path(3, increments))
```

**Output**

```text
[-4, 4] [3. 0. 0.]
[4, -4] [3. 7. 3.]
```

The initial resource level is included and ruin is absorbing.


(api-split-power-damage-logsf)=
#### [`split_power_damage_logsf`](incerto-api-reference.md#api-split-power-damage-logsf)

`split_power_damage_logsf(threshold, *, alpha, power, modules, exposure=1.0, x_m=1.0)`

```python
from xmath.incerto.lecture_risk import split_power_damage_logsf

for modules in (1, 16):
    value = split_power_damage_logsf(4, alpha=1.5, power=2, modules=modules)
    print(modules, "log survival:", round(float(value), 6))
```

**Output**

```text
1 log survival: -1.039721
16 log survival: -3.119162
```

The model splits a Pareto power-damage exposure into equal modules.


(api-block-failure-summary)=
#### [`block_failure_summary`](incerto-api-reference.md#api-block-failure-summary)

`block_failure_summary(probability, blocks, exposure=1.0)`

```python
from xmath.incerto.lecture_risk import block_failure_summary

for name, value in block_failure_summary(0.02, blocks=10).items():
    print(f"{name}: {value:.6g}")
```

**Output**

```text
mean: 0.02
variance: 0.00196
any_failure: 0.182927
total_failure: 1.024e-17
```

Blocks fail independently and have equal all-or-nothing exposures.


### Finite moments

Module: `xmath.incerto.finite_moments`.

(api-normal-mixture-log-density)=
#### [`normal_mixture_log_density`](incerto-api-reference.md#api-normal-mixture-log-density)

`normal_mixture_log_density(x, variances, weights)`

```python
from xmath.incerto.finite_moments import normal_mixture_log_density

print(normal_mixture_log_density([0, 1, 4], [0.5, 50.5], [0.99, 0.01]).round(6))
```

**Output**

```text
[-0.581411 -1.579714 -7.64338 ]
```

Components are centered Gaussian laws with the stated variances and weights.


(api-normal-mixture-log-abs-survival)=
#### [`normal_mixture_log_abs_survival`](incerto-api-reference.md#api-normal-mixture-log-abs-survival)

`normal_mixture_log_abs_survival(u, variances, weights)`

```python
from xmath.incerto.finite_moments import normal_mixture_log_abs_survival

print(normal_mixture_log_abs_survival([0, 1, 4], [0.5, 50.5], [0.99, 0.01]).round(6))
```

**Output**

```text
[ 0.       -1.804194 -5.161134]
```

Thresholds are finite and nonnegative; exceedances are two-sided absolute values.


(api-normal-mixture-absolute-moment)=
#### [`normal_mixture_absolute_moment`](incerto-api-reference.md#api-normal-mixture-absolute-moment)

`normal_mixture_absolute_moment(q, variances, weights)`

```python
from xmath.incerto.finite_moments import normal_mixture_absolute_moment

for order in (2, 4):
    print(order, round(normal_mixture_absolute_moment(order, [0.5, 50.5], [0.99, 0.01]), 6))
```

**Output**

```text
2 1.0
4 77.25
```

All positive-order absolute moments exist for a finite Gaussian mixture.


(api-pareto-moment-estimator-summary)=
#### [`pareto_moment_estimator_summary`](incerto-api-reference.md#api-pareto-moment-estimator-summary)

`pareto_moment_estimator_summary(alpha, q, n, x_m=1.0)`

```python
from xmath.incerto.finite_moments import pareto_moment_estimator_summary

for alpha in (1.5, 3, 6):
    print(alpha, pareto_moment_estimator_summary(alpha, q=2, n=200))
```

**Output**

```text
1.5 {'moment': inf, 'estimator_variance': nan}
3 {'moment': 3.0000000000000004, 'estimator_variance': inf}
6 {'moment': 1.5, 'estimator_variance': 0.003750000000000002}
```

The empirical moment averages `n` iid exact Pareto observations.


(api-power-mean)=
#### [`power_mean`](incerto-api-reference.md#api-power-mean)

`power_mean(sample, order)`

```python
from xmath.incerto.finite_moments import power_mean

for order in (1, 2, 4, float("inf")):
    print(order, round(power_mean([0, 0, 0, -4], order), 6))
```

**Output**

```text
1 1.0
2 2.0
4 2.828427
inf 4.0
```

Orders are at least one; powers use absolute values and normalization by sample size.


### Multivariate

Module: `xmath.incerto.multivariate`.

(api-student-entropy)=
#### [`student_entropy`](incerto-api-reference.md#api-student-entropy)

`student_entropy(nu, dimension, logdet=0.0)`

```python
from xmath.incerto.multivariate import student_entropy

for dimension in (1, 2):
    print(dimension, round(student_entropy(3, dimension, logdet=0), 6))
```

**Output**

```text
1 1.773478
2 3.504544
```

Entropy is in nats; `logdet` is the log determinant of scatter.


(api-student-mutual-information)=
#### [`student_mutual_information`](incerto-api-reference.md#api-student-mutual-information)

`student_mutual_information(nu, rho=0.0)`

```python
from xmath.incerto.multivariate import student_mutual_information

for nu in (1, 5):
    print(nu, round(student_mutual_information(nu, rho=0), 6))
```

**Output**

```text
1 0.224171
5 0.017128
```

Mutual information is in nats for unit diagonal scatter.


(api-bivariate-student)=
#### [`bivariate_student`](incerto-api-reference.md#api-bivariate-student)

`bivariate_student(rng, nu, rho, size)`

```python
import numpy as np
from xmath.incerto.multivariate import bivariate_student

rng = np.random.default_rng(20261020)
print(bivariate_student(rng, nu=3, rho=0.6, size=3).round(6))
```

**Output**

```text
[[-1.722413 -1.126431]
 [-1.263474 -0.024399]
 [ 7.266111  2.57196 ]]
```

Each pair shares one gamma precision, with unit diagonal scatter and off-diagonal `rho`.


(api-sample-correlation)=
#### [`sample_correlation`](incerto-api-reference.md#api-sample-correlation)

`sample_correlation(x, y, *, centered=True)`

```python
from xmath.incerto.multivariate import sample_correlation

for centered in (True, False):
    print(centered, round(sample_correlation([1, 2, 3], [3, 2, 1], centered=centered), 6))
print("Constant centered column:", sample_correlation([1, 1, 1], [1, 2, 3]))
```

**Output**

```text
True -1.0
False 0.714286
Constant centered column: nan
```

`centered=True` uses Pearson correlation; `False` uses the uncentered cosine along the last axis.


(api-symmetric-spectrum)=
#### [`symmetric_spectrum`](incerto-api-reference.md#api-symmetric-spectrum)

`symmetric_spectrum(matrix)`

```python
from xmath.incerto.multivariate import symmetric_spectrum

print(symmetric_spectrum([[0, 2], [2, 0]]))
```

**Output**

```text
[-2.  2.]
```

The real square input must be finite, nonempty, and exactly symmetric.


(api-regression-population-r2)=
#### [`regression_population_r2`](incerto-api-reference.md#api-regression-population-r2)

`regression_population_r2(slope, error_variance)`

```python
from xmath.incerto.multivariate import regression_population_r2

print(regression_population_r2(slope=1, error_variance=3))
```

**Output**

```text
0.24999999999999994
```

The error is independent and the predictor has variance one.


(api-normal-location-mixture-kurtosis)=
#### [`normal_location_mixture_kurtosis`](incerto-api-reference.md#api-normal-location-mixture-kurtosis)

`normal_location_mixture_kurtosis(separation, sigma=1.0)`

```python
from xmath.incerto.multivariate import normal_location_mixture_kurtosis

for separation in (0, 2):
    print(separation, normal_location_mixture_kurtosis(separation, sigma=1))
```

**Output**

```text
0 3.0
2 1.7199999999999998
```

Equal Gaussian components are centered at plus and minus `separation`, with common standard deviation `sigma`.


### Power laws

Module: `xmath.incerto.power_laws`.

(api-pareto-product-logsf)=
#### [`pareto_product_logsf`](incerto-api-reference.md#api-pareto-product-logsf)

`pareto_product_logsf(log_threshold, a, b)`

```python
import numpy as np
from xmath.incerto.power_laws import pareto_product_logsf

for a, b in ((1, 2), (1, 1)):
    print((a, b), pareto_product_logsf(np.log([1, 10, 100]), a, b).round(6))
```

**Output**

```text
(1, 2) [-0.       -1.660731 -3.917036]
(1, 1) [-0.       -1.10788  -2.881481]
```

The factors are independent unit-minimum Paretos; thresholds enter on the log scale.


(api-pareto-truncated-moment)=
#### [`pareto_truncated_moment`](incerto-api-reference.md#api-pareto-truncated-moment)

`pareto_truncated_moment(cutoff, alpha, order, *, x_m=1.0)`

```python
from xmath.incerto.power_laws import pareto_truncated_moment

for order in (1, 1.5, 2):
    print(order, pareto_truncated_moment([10, 100], alpha=1.5, order=order).round(6))
```

**Output**

```text
1 [2.051317 2.7     ]
1.5 [3.453878 6.907755]
2 [ 6.486833 27.      ]
```

Truncation uses the indicator below `cutoff`, without conditional renormalization.


(api-student-double-pareto-scales)=
#### [`student_double_pareto_scales`](incerto-api-reference.md#api-student-double-pareto-scales)

`student_double_pareto_scales(alpha)`

```python
from xmath.incerto.power_laws import student_double_pareto_scales

for name, value in student_double_pareto_scales(3).items():
    print(name, round(value, 6))
```

**Output**

```text
student_tail_constant 1.102658
tail_scale 0.768263
variance_scale 0.57735
tail_matched_variance 1.770683
```

Matching uses a unit shifted double Pareto and requires `alpha > 2`.


(api-q-exponential-logsf)=
#### [`q_exponential_logsf`](incerto-api-reference.md#api-q-exponential-logsf)

`q_exponential_logsf(x, q, beta=1.0)`

```python
from xmath.incerto.power_laws import q_exponential_logsf

for q in (0.75, 1, 1.25):
    print(q, q_exponential_logsf([0, 1, 2], q, beta=2).round(6))
```

**Output**

```text
0.75 [-0.       -3.465736      -inf]
1 [-0. -2. -4.]
1.25 [-0.       -1.216395 -2.079442]
```

The normalized law requires `x >= 0` and `0 < q < 2`; `-inf` means zero survival.


(api-entropy-log-constraint-example)=
#### [`entropy_log_constraint_example`](incerto-api-reference.md#api-entropy-log-constraint-example)

`entropy_log_constraint_example()`

```python
from xmath.incerto.power_laws import entropy_log_constraint_example

for name, value in entropy_log_constraint_example().items():
    print(name, round(value, 6))
```

**Output**

```text
pareto_mass 1.0
pareto_log_moment 0.5
pareto_entropy 0.806853
log_gamma_mass 1.0
log_gamma_log_moment 0.5
log_gamma_entropy 0.690921
kl 0.115932
```

Independent quadrature uses $x_m=1$ and $\mathbb E\log X=1/2$.


### Figures

Module: `xmath.incerto.figures`.

(api-set-theme)=
#### [`set_theme`](incerto-api-reference.md#api-set-theme)

`set_theme(*, scale=1.0)`

Apply the Incerto Matplotlib theme.

(api-style-axes)=
#### [`style_axes`](incerto-api-reference.md#api-style-axes)

`style_axes(axes, *, grid_axis='y', legend=True)`

Apply final Incerto styling to one or more axes.

(api-savefig)=
#### [`savefig`](incerto-api-reference.md#api-savefig)

`savefig(fig, path, **kwargs)`

Save a figure with Incerto defaults.

### Base package

(api-exceedance-fraction)=
#### [`exceedance_fraction`](incerto-api-reference.md#api-exceedance-fraction)

`xmath.exceedance_fraction(samples, threshold)`

```python
from xmath import exceedance_fraction

for threshold in (0, 2, 4):
    print(threshold, exceedance_fraction([1, 2, 2, 4], threshold))
```

**Output**

```text
0 1.0
2 0.25
4 0.0
```

Exceedances are strict; the sample must be nonempty and finite.
