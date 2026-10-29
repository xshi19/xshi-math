"""Tail-index estimators and finite-sample diagnostics."""

from __future__ import annotations

import operator
import warnings
from collections.abc import Iterable

import numpy as np
from numpy.typing import ArrayLike, NDArray
from scipy.optimize import fmin
from scipy.stats import genpareto


def _positive_1d_sample(x: ArrayLike) -> NDArray[np.float64]:
    """Return ``x`` as a finite, positive, one-dimensional float array."""

    sample = np.asarray(x, dtype=float)
    if sample.ndim != 1:
        raise ValueError("x must be one-dimensional")
    if sample.size < 2:
        raise ValueError("x must contain at least two observations")
    if not np.all(np.isfinite(sample)):
        raise ValueError("x must contain only finite values")
    if np.any(sample <= 0.0):
        raise ValueError("Hill estimators require positive observations")
    return sample


def _validate_k(k: int, n: int) -> int:
    try:
        k_int = operator.index(k)
    except TypeError as exc:
        raise TypeError("k must be an integer") from exc
    if k_int < 1 or k_int >= n:
        raise ValueError("k must satisfy 1 <= k < len(x)")
    return k_int


def hill_estimator(x: ArrayLike, k: int) -> float:
    """Return the Hill estimate of the extreme-value index ``xi``.

    Parameters
    ----------
    x:
        Positive observations from a right-tail sample.
    k:
        Number of upper order statistics to use.  Must satisfy
        ``1 <= k < len(x)``.

    Returns
    -------
    float
        Hill estimate ``xi_hat``.  For Pareto-type tails with exponent
        ``alpha``, ``xi = 1 / alpha``.

    Raises
    ------
    ValueError
        If observations are not one-dimensional, finite, and positive, or if
        ``k`` is outside the valid order-statistic range.
    TypeError
        If ``k`` is not an integer.

    Notes
    -----
    Exact ties contribute zero; identical largest k+1 values give zero xi.
    log1p retains nearby float spacings, while log differences avoid ratio
    overflow for widely separated values. Input conversion can erase gaps.
    tests/test_incerto_extremes.py checks four rescalings at rtol=1e-13 and
    adjacent floats near 1 and 1e200 against 70-digit Decimal. That latter
    comparison requests rtol=1e-14 but allows pytest.approx's atol=1e-12,
    which dominates these tiny values; it does not establish relative accuracy.
    Its subnormal-to-maximum-float test checks finiteness/positivity only.
    No uniform relative accuracy is promised for arbitrary samples or gaps.
    """

    sample = _positive_1d_sample(x)
    k_int = _validate_k(k, sample.size)

    weighted = _weighted_log_spacings(sample)
    return float(np.sum(weighted[:k_int]) / k_int)


def _weighted_log_spacings(sample):
    """j*log(x_j/x_{j+1}) in descending order, with nonnegative gaps.

    log1p preserves near ties; the log difference avoids overflowing a ratio
    of widely separated values. Sum through k to recover k times Hill xi.
    """
    ordered = np.sort(sample)[::-1]
    high, low = ordered[:-1], ordered[1:]
    delta = high-low
    near = delta <= low
    gaps = np.empty_like(delta)
    gaps[near] = np.log1p(delta[near]/low[near])
    gaps[~near] = np.log(high[~near])-np.log(low[~near])
    return np.arange(1, sample.size)*gaps


def hill_alpha_estimator(x: ArrayLike, k: int) -> float:
    """Return the reciprocal Hill estimate of the Pareto tail exponent.

    Parameters
    ----------
    x:
        Positive observations from a right-tail sample.
    k:
        Number of upper order statistics to use.

    Returns
    -------
    float
        Tail-exponent estimate ``alpha_hat = 1 / xi_hat``.  If the selected
        upper order statistics have zero log spacing, the result is
        ``numpy.inf``.

    Notes
    -----
    Validation and spacing accuracy are those of hill_estimator. A positive
    xi has a finite reciprocal only if representable; reciprocal overflow
    and extreme-parameter relative accuracy are not separately controlled.
    """

    xi_hat = hill_estimator(x, k)
    return float(np.inf if xi_hat == 0.0 else 1.0 / xi_hat)


def pareto_mean_plugin(
    x: ArrayLike,
    *,
    x_m: float,
    axis: int | None = None,
) -> float | NDArray[np.float64]:
    """Estimate an exact Pareto mean with a known lower cutoff.

    Parameters
    ----------
    x:
        Non-empty array-like of finite observations, all at least ``x_m``.
        A scalar is treated as one observation when ``axis=None``.
    x_m:
        Known finite positive scalar lower cutoff. For a conditional tail
        mean, pass a fixed threshold and only its exceedances as ``x``.
    axis:
        Axis containing observations. ``None`` pools all input values;
        otherwise each slice is fitted separately, removing this axis.

    Returns
    -------
    float or numpy.ndarray
        ``x_m / (1 - xi_hat)``, where ``xi_hat = mean(log(x / x_m))``
        is the reciprocal of the Pareto maximum-likelihood exponent estimate.
        Returns ``numpy.inf`` when ``xi_hat >= 1``: the fitted model has no
        finite mean. An all-cutoff slice returns ``x_m``, the limiting mean
        as the fitted exponent tends to infinity. Scalar results are floats.

    Raises
    ------
    ValueError
        If ``x_m`` is not a finite positive scalar, or observations are empty,
        non-finite, or below the cutoff.

    Notes
    -----
    Statistical calibration assumes iid exact Pareto observations above a
    known cutoff. This function does not select a threshold or validate a tail
    model. It does not clip estimates away from the mean-existence boundary.
    Even conditional on a finite result, the unregularized estimator has
    infinite first and second moments under the exact Pareto sampling model.
    """

    cutoff = np.asarray(x_m, dtype=float)
    if cutoff.ndim != 0 or not np.isfinite(cutoff) or cutoff <= 0.0:
        raise ValueError("x_m must be a finite positive scalar")
    cutoff = float(cutoff)
    sample = np.asarray(x, dtype=float)
    if sample.size == 0:
        raise ValueError("x must contain at least one observation")
    if not np.all(np.isfinite(sample)):
        raise ValueError("x must contain only finite values")
    if np.any(sample < cutoff):
        raise ValueError("all observations must be at least x_m")

    # Preserve small log-excesses near the cutoff without overflowing x / x_m.
    excess = sample - cutoff
    near = excess <= cutoff
    log_excess = np.empty_like(sample)
    log_excess[near] = np.log1p(excess[near] / cutoff)
    log_excess[~near] = np.log(sample[~near]) - np.log(cutoff)
    xi_hat = np.mean(log_excess, axis=axis)
    result = np.full_like(xi_hat, np.inf, dtype=float)
    np.divide(cutoff, 1.0 - xi_hat, out=result, where=xi_hat < 1.0)
    return float(result) if np.ndim(result) == 0 else result


def _default_k_values(n: int, *, num: int = 100) -> NDArray[np.int64]:
    if num < 1:
        raise ValueError("num must be positive")
    k_max = max(1, n // 3)
    if k_max == 1:
        return np.array([1], dtype=np.int64)
    return np.unique(np.geomspace(1, k_max, num=num).astype(np.int64))


def hill_stability(
    x: ArrayLike,
    k_values: Iterable[int] | ArrayLike | None = None,
    *,
    num: int = 100,
) -> dict[str, NDArray[np.float64]]:
    """Return Hill estimates across a range of upper order statistics.

    Parameters
    ----------
    x:
        Positive observations from a right-tail sample.
    k_values:
        Optional integer values of ``k`` to evaluate.  If omitted, use a
        logarithmically spaced grid from ``1`` to roughly ``len(x) / 3``.
    num:
        Number of grid points to request when ``k_values`` is omitted.

    Returns
    -------
    dict
        Dictionary with ``"k"``, ``"xi"``, and ``"alpha"`` arrays.  ``"k"`` is
        stored as floating point so the result can be passed directly to NumPy
        and plotting functions with the other arrays.

    Notes
    -----
    Shares hill_estimator's validation, tie behavior and accuracy limits.
    Cumulative sums can round differently from scalar summation. Scalar/vector
    agreement is tested at rtol=1e-14 for the rescaled samples in
    tests/test_incerto_extremes.py and rtol=1e-12 in
    tests/test_incerto_numerical_reliability.py, not for arbitrary long sums.
    """

    sample = _positive_1d_sample(x)
    n = sample.size
    if k_values is None:
        ks = _default_k_values(n, num=num)
    else:
        raw_ks = np.asarray(list(k_values))
        if raw_ks.ndim != 1 or raw_ks.size == 0:
            raise ValueError("k_values must be a non-empty one-dimensional sequence")
        if not np.issubdtype(raw_ks.dtype, np.integer):
            raise TypeError("k_values must contain integers")
        ks = raw_ks.astype(np.int64)

    for k in ks:
        _validate_k(int(k), n)

    prefix = np.cumsum(_weighted_log_spacings(sample))
    xi = prefix[ks-1] / ks
    alpha = np.divide(
        1.0,
        xi,
        out=np.full_like(xi, np.inf, dtype=float),
        where=xi != 0.0,
    )

    return {
        "k": ks.astype(float),
        "xi": xi.astype(float),
        "alpha": alpha.astype(float),
    }


def running_mean(
    x: ArrayLike,
    axis: int | None = None,
) -> NDArray[np.float64]:
    """Return cumulative arithmetic means along an axis.

    Parameters
    ----------
    x:
        Input observations.
    axis:
        Axis along which to compute cumulative means.  When ``None``, compute
        over the flattened input.

    Returns
    -------
    numpy.ndarray
        Cumulative means with the same shape as the input along ``axis``.
    """

    x_array = np.asarray(x, dtype=float)
    if axis is None:
        flat = x_array.ravel()
        if flat.size == 0:
            raise ValueError("x must contain at least one observation")
        return np.cumsum(flat) / np.arange(1, flat.size + 1)

    if x_array.shape[axis] == 0:
        raise ValueError("x must contain at least one observation along axis")
    cumulative = np.cumsum(x_array, axis=axis)
    counts_shape = [1] * x_array.ndim
    counts_shape[axis] = x_array.shape[axis]
    counts = np.arange(1, x_array.shape[axis] + 1, dtype=float).reshape(counts_shape)
    return cumulative / counts


def max_to_sum_ratio(
    x: ArrayLike,
    axis: int | None = None,
) -> float | NDArray[np.float64]:
    """Return the share of a nonnegative sum contributed by its maximum.

    Parameters
    ----------
    x:
        Nonnegative observations.
    axis:
        Axis along which to compute the ratio.  When ``None``, compute over the
        flattened input.

    Returns
    -------
    float or numpy.ndarray
        ``max(x) / sum(x)`` along the requested axis.

    Raises
    ------
    ValueError
        If observations are negative, non-finite, or sum to zero along the
        requested axis.
    """

    x_array = np.asarray(x, dtype=float)
    if not np.all(np.isfinite(x_array)):
        raise ValueError("x must contain only finite values")
    if np.any(x_array < 0.0):
        raise ValueError("max-to-sum ratio requires nonnegative observations")

    maximum = np.max(x_array, axis=axis, keepdims=True)
    if np.any(maximum <= 0.0):
        raise ValueError("sum of observations must be positive")

    result = 1.0 / np.sum(x_array / maximum, axis=axis)
    return float(result) if np.ndim(result) == 0 else result


def max_to_sum_path(x: ArrayLike) -> NDArray[np.float64]:
    """Return each prefix's maximum / sum for a finite nonnegative 1-D list.

    Zero-total prefixes return NaN, including an all-zero list. Empty,
    nonfinite, complex or negative inputs raise ValueError. Log accumulation
    avoids overflow of sums and preserves early tiny observations even when
    a later record is huge. Ordinary floating-point rounding remains.
    """
    if np.iscomplexobj(x):
        raise ValueError("x must be real")
    values = np.asarray(x, dtype=float)
    if (values.ndim != 1 or values.size == 0 or not np.all(np.isfinite(values))
            or np.any(values < 0)):
        raise ValueError("x must be a nonempty finite nonnegative vector")
    with np.errstate(divide="ignore"):
        logs = np.log(values)
    log_max = np.maximum.accumulate(logs)
    log_sum = np.logaddexp.accumulate(logs)
    result = np.full(values.shape, np.nan)
    positive = np.isfinite(log_sum)
    result[positive] = np.exp(log_max[positive] - log_sum[positive])
    return result


def gpd_threshold_fit(x: ArrayLike, threshold: float, *, min_exceedances: int = 30):
    """Fit a zero-location GPD to strict excesses x[x > threshold]-threshold.

    Finite real 1-D data and a finite scalar threshold are required. Return
    threshold, count, xi, beta, modified_scale=beta-xi*threshold, success and
    status. Insufficient/constant excesses, overflow in forming excesses, or a
    failed numerical fit retain the count but return NaN parameters and an
    explanatory status. Nelder-Mead
    is capped at 2000 iterations / 4000 evaluations; check convergence, finite
    parameters/log likelihood, and strict interior support for every excess.
    A successful local numerical fit is not a global MLE guarantee or a
    validation of the tail model. No uncertainty interval is computed.
    """
    if np.iscomplexobj(x) or np.iscomplexobj(threshold):
        raise ValueError("data and threshold must be real")
    values = np.asarray(x, dtype=float)
    if values.ndim != 1 or values.size == 0 or not np.all(np.isfinite(values)):
        raise ValueError("x must be a nonempty finite vector")
    if np.ndim(threshold) != 0 or not np.isfinite(threshold):
        raise ValueError("threshold must be a finite scalar")
    u = float(threshold)
    minimum = _validate_min_exceedances(min_exceedances)
    exceedances = values[values > u]
    result = dict(threshold=u, count=int(exceedances.size), xi=np.nan, beta=np.nan,
                  modified_scale=np.nan, success=False, status="insufficient count")
    if exceedances.size < minimum:
        return result
    try:
        with np.errstate(over="raise"):
            excesses = exceedances - u
    except FloatingPointError as exc:
        result["status"] = f"fit failed: {exc}"
        return result
    if np.ptp(excesses) == 0:
        result["status"] = "constant excesses"
        return result

    def optimizer(function, start, args=(), disp=0):
        fitted, _, _, _, flag = fmin(function, start, args=args, disp=False,
                                     full_output=True, maxiter=2000, maxfun=4000)
        if flag:
            raise RuntimeError("optimizer did not converge")
        return fitted

    try:
        with warnings.catch_warnings():
            warnings.simplefilter("error", RuntimeWarning)
            xi, loc, beta = genpareto.fit(excesses, floc=0, optimizer=optimizer)
            modified = beta - xi * u
            if (not np.all(np.isfinite([xi, loc, beta, modified])) or loc != 0
                    or beta <= 0 or np.any(1 + xi * (excesses / beta) <= 0)
                    or not np.all(np.isfinite(genpareto.logpdf(excesses, xi, scale=beta)))):
                raise ValueError("invalid fitted parameters or support")
    except (ValueError, RuntimeError, FloatingPointError, RuntimeWarning) as exc:
        result["status"] = f"fit failed: {exc}"
        return result
    result.update(xi=float(xi), beta=float(beta), modified_scale=float(modified),
                  success=True, status="ok")
    return result


def mean_excess(
    x: ArrayLike,
    thresholds: ArrayLike,
    *,
    min_exceedances: int = 1,
) -> dict[str, NDArray[np.float64]]:
    """Return the empirical mean excess above each threshold.

    Parameters
    ----------
    x:
        One-dimensional observations.  The statistic is usually applied to
        nonnegative losses or positive right-tail observations.
    thresholds:
        Threshold values ``u``.  For each threshold, the function averages
        ``x - u`` over observations satisfying ``x > u``.
    min_exceedances:
        Minimum number of observations above a threshold required to report a
        finite mean excess.  Thresholds with fewer exceedances return
        ``numpy.nan`` for ``"mean_excess"``.

    Returns
    -------
    dict
        Dictionary with ``"threshold"``, ``"mean_excess"``, and
        ``"exceedances"`` arrays.

    Raises
    ------
    ValueError
        If observations or thresholds are not finite one-dimensional arrays, or
        if ``min_exceedances`` is less than one.
    """

    sample = np.asarray(x, dtype=float)
    if sample.ndim != 1 or sample.size == 0:
        raise ValueError("x must be a non-empty one-dimensional array")
    if not np.all(np.isfinite(sample)):
        raise ValueError("x must contain only finite values")

    threshold_array = np.asarray(thresholds, dtype=float)
    if threshold_array.ndim != 1 or threshold_array.size == 0:
        raise ValueError("thresholds must be a non-empty one-dimensional array")
    if not np.all(np.isfinite(threshold_array)):
        raise ValueError("thresholds must contain only finite values")

    min_count = _validate_min_exceedances(min_exceedances)
    means = np.empty_like(threshold_array, dtype=float)
    counts = np.empty_like(threshold_array, dtype=float)

    for i, threshold in enumerate(threshold_array):
        excesses = sample[sample > threshold] - threshold
        counts[i] = excesses.size
        means[i] = np.nan if excesses.size < min_count else float(np.mean(excesses))

    return {
        "threshold": threshold_array.astype(float),
        "mean_excess": means,
        "exceedances": counts,
    }


def _validate_min_exceedances(min_exceedances: int) -> int:
    try:
        min_count = operator.index(min_exceedances)
    except TypeError as exc:
        raise TypeError("min_exceedances must be an integer") from exc
    if min_count < 1:
        raise ValueError("min_exceedances must be at least one")
    return min_count


__all__ = [
    "gpd_threshold_fit",
    "hill_alpha_estimator",
    "hill_estimator",
    "hill_stability",
    "max_to_sum_ratio",
    "max_to_sum_path",
    "mean_excess",
    "pareto_mean_plugin",
    "running_mean",
]
