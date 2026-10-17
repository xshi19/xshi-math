"""Tail-class diagnostic helpers used by Incerto examples."""

from __future__ import annotations

import operator
from collections.abc import Callable
from typing import TypeAlias

import numpy as np
from numpy.typing import ArrayLike, NDArray
from scipy import integrate

SurvivalFunction: TypeAlias = Callable[[NDArray[np.float64]], ArrayLike]
Sampler: TypeAlias = Callable[[int, np.random.Generator], ArrayLike]


def _positive_thresholds(thresholds: ArrayLike) -> NDArray[np.float64]:
    x = np.atleast_1d(np.asarray(thresholds, dtype=float))
    if x.ndim != 1:
        raise ValueError("thresholds must be one-dimensional")
    if x.size == 0:
        raise ValueError("thresholds must contain at least one value")
    if not np.all(np.isfinite(x)):
        raise ValueError("thresholds must contain only finite values")
    if np.any(x <= 0.0):
        raise ValueError("thresholds must be positive")
    return x


def _survival_values(
    survival: SurvivalFunction,
    x: NDArray[np.float64],
) -> NDArray[np.float64]:
    values = np.asarray(survival(x), dtype=float)
    if values.shape == ():
        values = np.full_like(x, float(values))
    try:
        values = np.broadcast_to(values, x.shape).astype(float, copy=False)
    except ValueError as exc:
        raise ValueError("survival must return values broadcastable to thresholds") from exc
    if not np.all(np.isfinite(values)):
        raise ValueError("survival values must be finite")
    if np.any(values < 0.0):
        raise ValueError("survival values must be nonnegative")
    return values


def _rng_from_state(
    random_state: int | np.random.Generator | None,
) -> np.random.Generator:
    if isinstance(random_state, np.random.Generator):
        return random_state
    return np.random.default_rng(random_state)


def _validate_sample_size(sample_size: int) -> int:
    try:
        size = operator.index(sample_size)
    except TypeError as exc:
        raise TypeError("sample_size must be an integer") from exc
    if size < 1:
        raise ValueError("sample_size must be positive")
    return size


def _draw_sample(
    sampler: Sampler,
    sample_size: int,
    rng: np.random.Generator,
    *,
    name: str,
) -> NDArray[np.float64]:
    sample = np.asarray(sampler(sample_size, rng), dtype=float)
    if sample.shape != (sample_size,):
        raise ValueError(f"{name} must return a one-dimensional sample of length sample_size")
    if not np.all(np.isfinite(sample)):
        raise ValueError(f"{name} must contain only finite values")
    return sample


def regular_variation_ratio(
    survival: SurvivalFunction,
    thresholds: ArrayLike,
    *,
    multiplier: float = 2.0,
) -> dict[str, NDArray[np.float64]]:
    r"""Evaluate the fixed-multiplier survival ratio.

    This diagnostic computes

    .. math::

       \bar F(t x) / \bar F(x)

    on a grid of positive thresholds.  For a regularly varying survival tail
    with index ``-alpha``, the ratio converges to ``t ** (-alpha)`` for fixed
    ``t > 0``.

    Parameters
    ----------
    survival:
        Callable that accepts a NumPy array of thresholds and returns survival
        probabilities broadcastable to the same shape.
    thresholds:
        Positive threshold values ``x``.
    multiplier:
        Positive threshold multiplier ``t``.

    Returns
    -------
    dict
        Dictionary with ``"threshold"``, ``"survival"``,
        ``"multiplied_survival"``, and ``"ratio"`` arrays.

    Raises
    ------
    ValueError
        If thresholds, multiplier, or survival values are outside their valid
        domains.
    """

    if not np.isfinite(multiplier) or multiplier <= 0.0:
        raise ValueError("multiplier must be positive and finite")

    x = _positive_thresholds(thresholds)
    denominator = _survival_values(survival, x)
    numerator = _survival_values(survival, multiplier * x)
    if np.any(denominator <= 0.0):
        raise ValueError("survival must be positive at each threshold")

    return {
        "threshold": x,
        "survival": denominator,
        "multiplied_survival": numerator,
        "ratio": numerator / denominator,
    }


def _finite_or_infinite_support(rv) -> tuple[float, float]:
    lower, upper = rv.support()
    lower_float = float(lower)
    upper_float = float(upper)
    if np.isnan(lower_float) or np.isnan(upper_float):
        raise ValueError("distribution support endpoints must not be NaN")
    if np.isfinite(upper_float):
        raise ValueError("right support endpoint must be infinite")
    return lower_float, upper_float


def iid_two_sum_tail(
    rv,
    thresholds: ArrayLike,
    *,
    rtol: float = 1e-10,
    maxlevel: int = 12,
) -> dict[str, NDArray[np.float64]]:
    r"""Compute the iid two-summand right-tail ratio by convolution.

    For iid continuous variables with density ``f`` and survival function
    ``sf``, this evaluates

    .. math::

       \mathbb P(X_1 + X_2 > x) / (2\mathbb P(X > x)).

    The implementation uses the symmetry identity

    .. math::

       \mathbb P(X_1 + X_2 > x)
       = 2\int_a^{x/2} f(y)\bar F(x-y)\,dy + \bar F(x/2)^2,

    where ``a`` is the lower support endpoint.  The integral is normalized by
    ``sf(x)`` and evaluated in the log domain with SciPy's vectorized
    ``tanhsinh`` quadrature.

    Parameters
    ----------
    rv:
        SciPy-like frozen continuous distribution with ``support()``,
        ``logpdf()``, and ``logsf()`` methods.
    thresholds:
        Positive threshold values ``x``.  When the lower support endpoint is
        finite, each threshold must satisfy ``x > 2 * lower``.
    rtol:
        Relative quadrature tolerance.
    maxlevel:
        Maximum tanh-sinh refinement level.

    Returns
    -------
    dict
        Dictionary with ``"x"``, ``"threshold"``, ``"log_tail"``, ``"tail"``,
        ``"log_ratio"``, ``"ratio"``, ``"success"``, ``"log_abs_error"``,
        and ``"nfev"`` arrays.

    Raises
    ------
    ValueError
        If thresholds, support, or tolerance parameters are invalid.
    FloatingPointError
        If the distribution cannot provide finite ``logsf`` values at the
        requested thresholds.
    """

    if not np.isfinite(rtol) or rtol <= 0.0:
        raise ValueError("rtol must be positive and finite")
    try:
        maxlevel_int = operator.index(maxlevel)
    except TypeError as exc:
        raise TypeError("maxlevel must be an integer") from exc
    if maxlevel_int < 0:
        raise ValueError("maxlevel must be nonnegative")

    x = _positive_thresholds(thresholds)
    lower, _ = _finite_or_infinite_support(rv)
    if np.isfinite(lower) and np.any(x <= 2.0 * lower):
        raise ValueError(
            f"thresholds must exceed twice the lower support: x > {2.0 * lower}"
        )

    log_sf_x = np.asarray(rv.logsf(x), dtype=float)
    log_sf_half = np.asarray(rv.logsf(x / 2.0), dtype=float)
    if np.any(~np.isfinite(log_sf_x)):
        raise FloatingPointError(
            "rv.logsf(thresholds) returned non-finite values; use a smaller "
            "range or a distribution-specific stable log-tail"
        )
    if np.any(~np.isfinite(log_sf_half)):
        raise FloatingPointError(
            "rv.logsf(thresholds / 2) returned non-finite values; use a smaller "
            "range or a distribution-specific stable log-tail"
        )

    def log_scaled_kernel(
        y: NDArray[np.float64],
        threshold: NDArray[np.float64],
        log_sf_threshold: NDArray[np.float64],
    ) -> NDArray[np.float64]:
        return rv.logpdf(y) + rv.logsf(threshold - y) - log_sf_threshold

    quad_result = integrate.tanhsinh(
        log_scaled_kernel,
        lower,
        x / 2.0,
        args=(x, log_sf_x),
        log=True,
        rtol=np.log(rtol),
        maxlevel=maxlevel_int,
    )

    log_integral_ratio = np.asarray(quad_result.integral, dtype=float)
    log_middle_ratio = 2.0 * log_sf_half - log_sf_x - np.log(2.0)
    log_ratio = np.logaddexp(log_integral_ratio, log_middle_ratio)
    log_tail = np.log(2.0) + log_sf_x + log_ratio

    return {
        "x": x,
        "threshold": x,
        "log_tail": log_tail,
        "tail": np.exp(log_tail),
        "log_ratio": log_ratio,
        "ratio": np.exp(log_ratio),
        "success": np.asarray(quad_result.success, dtype=bool),
        "log_abs_error": np.asarray(quad_result.error, dtype=float),
        "nfev": np.asarray(quad_result.nfev, dtype=float),
    }


def subexponential_sum_ratio(
    sampler: Sampler,
    survival: SurvivalFunction,
    thresholds: ArrayLike,
    *,
    sample_size: int = 100_000,
    random_state: int | np.random.Generator | None = None,
) -> dict[str, NDArray[np.float64]]:
    r"""Estimate the two-summand subexponential tail ratio by simulation.

    The diagnostic draws iid pairs and estimates

    .. math::

       \mathbb P(X_1 + X_2 > x) / (2 \bar F(x)).

    The denominator uses the supplied survival function; the numerator is a
    Monte Carlo estimate.  A survival function alone is not enough to simulate
    sums, so the caller must also provide a sampler.

    Parameters
    ----------
    sampler:
        Callable with signature ``sampler(sample_size, rng)`` that returns a
        one-dimensional array of iid draws.
    survival:
        Callable that accepts a NumPy array of thresholds and returns survival
        probabilities broadcastable to the same shape.
    thresholds:
        Positive threshold values ``x``.
    sample_size:
        Number of iid pairs to draw.
    random_state:
        Optional integer seed or ``numpy.random.Generator``.

    Returns
    -------
    dict
        Dictionary with ``"threshold"``, ``"single_tail"``, ``"sum_tail"``,
        ``"ratio"``, and ``"sum_exceedances"`` arrays.

    Raises
    ------
    ValueError
        If thresholds, survival values, or simulated samples are invalid.
    TypeError
        If ``sample_size`` is not an integer.
    """

    size = _validate_sample_size(sample_size)
    x = _positive_thresholds(thresholds)
    rng = _rng_from_state(random_state)
    first = _draw_sample(sampler, size, rng, name="first sample")
    second = _draw_sample(sampler, size, rng, name="second sample")

    single_tail = _survival_values(survival, x)
    if np.any(single_tail <= 0.0):
        raise ValueError("survival must be positive at each threshold")

    sums = first + second
    sum_exceedances = np.array(
        [np.count_nonzero(sums > threshold) for threshold in x],
        dtype=float,
    )
    sum_tail = sum_exceedances / size

    return {
        "threshold": x,
        "single_tail": single_tail,
        "sum_tail": sum_tail,
        "ratio": sum_tail / (2.0 * single_tail),
        "sum_exceedances": sum_exceedances,
    }


__all__ = [
    "iid_two_sum_tail",
    "regular_variation_ratio",
    "subexponential_sum_ratio",
]
