"""Installable Python package for the Incerto."""

from xmath.incerto.datasets import (
    BookRankData,
    DatasetNotAvailable,
    DogNameFrequencyData,
    PriceSeries,
    load_amazon_bookrank,
    load_nyc_dog_name_frequencies,
    load_sp500_prices,
)
from xmath.incerto.distributions import (
    double_pareto,
    hypsecant2,
    pareto_type1,
    simple_normal_mixture,
    univariate_variance_gamma,
)
from xmath.incerto.estimators import (
    hill_alpha_estimator,
    hill_estimator,
    hill_stability,
    max_to_sum_ratio,
    mean_excess,
    pareto_mean_plugin,
    running_mean,
)
from xmath.incerto.stats import (
    mean_absolute_deviation,
    median_absolute_deviation,
    normal_peak_shoulder_tail,
    normal_variance_peak_shoulder_tail,
    t_peak_shoulder_tail,
)
from xmath.incerto.tail_diagnostics import (
    iid_two_sum_tail,
    regular_variation_ratio,
    subexponential_sum_ratio,
)

__all__ = [
    "BookRankData",
    "DatasetNotAvailable",
    "DogNameFrequencyData",
    "PriceSeries",
    "double_pareto",
    "hill_alpha_estimator",
    "hill_estimator",
    "hill_stability",
    "hypsecant2",
    "iid_two_sum_tail",
    "load_amazon_bookrank",
    "load_nyc_dog_name_frequencies",
    "load_sp500_prices",
    "max_to_sum_ratio",
    "mean_absolute_deviation",
    "mean_excess",
    "median_absolute_deviation",
    "normal_peak_shoulder_tail",
    "normal_variance_peak_shoulder_tail",
    "pareto_mean_plugin",
    "pareto_type1",
    "regular_variation_ratio",
    "running_mean",
    "simple_normal_mixture",
    "subexponential_sum_ratio",
    "t_peak_shoulder_tail",
    "univariate_variance_gamma",
]
