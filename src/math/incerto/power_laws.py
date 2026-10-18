"""Population calculations for SCoFT v4 chapter 5; no sampling or fitting.

Log tails are retained when ordinary probabilities underflow. Invalid domains
raise ValueError; nonrepresentable arithmetic raises FloatingPointError.
Truncated moments may underflow to zero. The q-family alone returns -inf
for its mathematically zero survival at/beyond a compact support endpoint.
"""

from __future__ import annotations

import warnings
from fractions import Fraction
from math import factorial

import numpy as np
from numpy.typing import ArrayLike
from scipy.integrate import IntegrationWarning, quad
from scipy.special import betaln
from scipy.stats import gamma


def _positive(value: float, name: str) -> float:
    value = float(value)
    if not np.isfinite(value) or value <= 0:
        raise ValueError(f"{name} must be positive and finite")
    return value


def _nonnegative(values: ArrayLike, name: str) -> np.ndarray:
    values = np.asarray(values, dtype=float)
    if values.size == 0 or not np.all(np.isfinite(values)) or np.any(values < 0):
        raise ValueError(f"{name} must contain finite nonnegative values")
    return values


def _finite(value):
    if not np.all(np.isfinite(value)):
        raise FloatingPointError("nonrepresentable result")
    return value


def _log1p_over_x(x):
    """Continuous log1p(x)/x, including an argument rounded to zero."""
    ratio = np.ones_like(x)
    np.divide(np.log1p(x), x, out=ratio, where=x != 0)
    return ratio


def pareto_product_logsf(log_threshold: ArrayLike, a: float, b: float):
    """Log P(X1 X2 > exp(t)), t >= 0, for independent unit-minimum Paretos.

    Positive finite exponents a,b may coincide. Log thresholds avoid forming
    exp(t). Scalars and array shapes are preserved. No dependence extension.
    """
    a, b = sorted((_positive(a, "a"), _positive(b, "b")))
    t = _nonnegative(log_threshold, "log_threshold")
    with np.errstate(over="raise", invalid="raise", divide="raise", under="ignore"):
        delta = b - a
        if delta == 0:
            correction = np.log1p(a * t)
        else:
            # This is continuous at a=b, without subtracting near-equal tails.
            correction = np.log1p(a * (-np.expm1(-delta * t) / delta))
        result = np.asarray(-a * t + correction)
        small = b * t < .001
        # Near the support, CDF = a*b*t²/2 + O(t³). Avoid subtracting
        # the two O(t) terms in the log survival when the answer is O(t²).
        u, v = a * t[small], b * t[small]
        series = np.zeros_like(u)
        for n in range(2, 10):
            homogeneous = sum(u**k * v**(n-2-k) for k in range(n-1))
            series += (-1)**n * homogeneous / factorial(n)
        result[small] = np.log1p(-u * v * series)
        return _finite(result)


def pareto_truncated_moment(cutoff: ArrayLike, alpha: float, order: float,
                            *, x_m: float = 1.0):
    """E[X**order 1{X <= cutoff}] for exact Pareto, including order=alpha.

    alpha,order,x_m are positive finite scalars and cutoff >= x_m. This is
    indicator truncation, not conditioning or winsorization. Powers are
    combined in log space; near the lower support use log1p for accuracy.
    """
    alpha, order, x_m = (_positive(alpha, "alpha"), _positive(order, "order"),
                         _positive(x_m, "x_m"))
    b = _nonnegative(cutoff, "cutoff")
    if np.any(b < x_m):
        raise ValueError("cutoff must be at least x_m")
    t = np.log(b) - np.log(x_m)
    near = b / 2 <= x_m
    # Indexing also works for zero-dimensional arrays.
    t = np.asarray(t)
    t[near] = np.log1p((b[near] - x_m) / x_m)
    result = np.zeros_like(b)
    active = t > 0
    with np.errstate(over="raise", invalid="raise", divide="raise", under="ignore"):
        z = (order - alpha) * t[active]
        log_exprel = np.empty_like(z)
        small = np.abs(z) < 1e-5
        # log(expm1(z)/z) = z/2 + z²/24 + O(z⁴).
        log_exprel[small] = z[small] / 2 + z[small]**2 / 24
        positive = (z > 0) & ~small
        negative = (z < 0) & ~small
        log_exprel[positive] = (z[positive] + np.log(-np.expm1(-z[positive]))
                               - np.log(z[positive]))
        log_exprel[negative] = (np.log(-np.expm1(z[negative]))
                               - np.log(-z[negative]))
        log_result = (np.log(alpha) + order * np.log(x_m)
                      + np.log(t[active]) + log_exprel)
        result[active] = np.exp(log_result)
    return _finite(result)


def student_double_pareto_scales(alpha: float) -> dict[str, float]:
    """Student scales matching the unit shifted double Pareto, alpha > 2.

    Returns its Student right-tail constant at scale one, the two scales,
    and the Student variance under tail matching. beta-log arithmetic avoids
    subtracting two large log-gamma values. Very extreme arithmetic may raise.
    """
    alpha = _positive(alpha, "alpha")
    if alpha <= 2:
        raise ValueError("finite variance matching requires alpha > 2")
    with np.errstate(over="raise", invalid="raise", divide="raise", under="ignore"):
        log_c = (alpha / 2 - 1) * np.log(alpha) - betaln(alpha / 2, .5)
        log_tail_scale = -(np.log(2) + log_c) / alpha
        result = {
            "student_tail_constant": float(np.exp(log_c)),
            "tail_scale": float(np.exp(log_tail_scale)),
            "variance_scale": float(np.exp((np.log(2) - np.log(alpha)
                                             - np.log(alpha - 1)) / 2)),
            "tail_matched_variance": float(np.exp(2 * log_tail_scale
                                                   + np.log(alpha) - np.log(alpha - 2))),
        }
    _finite(list(result.values()))
    if min(result.values()) <= 0:
        raise FloatingPointError("positive matching quantity underflowed")
    return result


def q_exponential_logsf(x: ArrayLike, q: float, beta: float = 1.0):
    """Normalized q-exponential log survival for x >= 0, 0 < q < 2.

    beta > 0; q=1 is exponential. For q<1 the upper endpoint is
    1/((1-q)*beta) and log survival is -inf at/beyond it. The escort mean
    is 1/(beta*(2-q)); it is not a free centering parameter in this family.
    Near the compact endpoint, exact ratios of the input floats distinguish
    interior points from the endpoint's rounded floating-point value.
    """
    q, beta = _positive(q, "q"), _positive(beta, "beta")
    if q >= 2:
        raise ValueError("normalization requires q < 2")
    x = _nonnegative(x, "x")
    with np.errstate(over="raise", invalid="raise", divide="raise", under="ignore"):
        if q == 1:
            return _finite(-beta * x)
        d = q - 1
        if d > 0:
            beta_x = beta * x
            v = d * beta_x
            # Scaling by beta*x retains a representable log survival even
            # when the extra factor q-1 makes v underflow to zero.
            result = -(2 - q) * beta_x * _log1p_over_x(v)
            return _finite(result)
        endpoint = (1 / (1 - q)) / beta
        _finite(endpoint)
        near_endpoint = np.abs(x - endpoint) <= 1e-8 * endpoint
        active = (x < endpoint) & ~near_endpoint
        result = np.full_like(x, -np.inf)
        v = x[active] / endpoint
        values = np.empty_like(v)
        low = v < .5
        values[low] = -(2 - q) * (beta * x[active][low]) * _log1p_over_x(-v[low])
        values[~low] = (2 - q) / (1 - q) * (
            np.log(endpoint - x[active][~low]) - np.log(endpoint))
        result[active] = values
        _finite(result[active])
        # Subtracting a rounded endpoint loses relative accuracy close to
        # the cutoff and can even turn an interior point into zero survival.
        # Only this narrow region needs exact arithmetic; no new dependency.
        if np.any(near_endpoint):
            slope = (1 - Fraction(q)) * Fraction(beta)
            for index in np.flatnonzero(near_endpoint):
                base = 1 - slope * Fraction(float(x.flat[index]))
                if base > 0:
                    result.flat[index] = _finite((2 - q) / (1 - q) * np.log(float(base)))
        return result


def entropy_log_constraint_example() -> dict[str, float]:
    """Independent integrals for x_m=1 and E log X=1/2.

    In z=log x coordinates compare Gamma(1,rate=2) with Gamma(2,rate=4).
    Every quad call integrates [0,infinity), limit=160, epsabs=epsrel=1e-10.
    Warnings or an estimated absolute error > 2e-9 fail the computation.
    This is one worked case, not an optimizer or a proof of global optimality.
    """
    candidate, competitor = gamma(1, scale=.5), gamma(2, scale=.25)

    def integrate(function):
        with warnings.catch_warnings():
            warnings.simplefilter("error", IntegrationWarning)
            value, error = quad(function, 0, np.inf, epsabs=1e-10,
                                epsrel=1e-10, limit=160)
        _finite([value, error])
        if error > 2e-9:
            raise FloatingPointError("entropy quadrature missed its error budget")
        return value

    def integrand(z, rv, mode):
        log_f = rv.logpdf(z)
        density = np.exp(log_f)
        if density == 0:  # limiting endpoint/underflow contribution, no draw removed
            return 0.0
        if mode == "entropy":
            return density * (-log_f + z)  # Jacobian from z to x
        if mode == "kl":
            return density * (log_f - candidate.logpdf(z))
        return density * (z if mode == "log_moment" else 1)

    result = {}
    for name, rv in (("pareto", candidate), ("log_gamma", competitor)):
        for mode in ("mass", "log_moment", "entropy"):
            result[f"{name}_{mode}"] = integrate(lambda z: integrand(z, rv, mode))
    result["kl"] = integrate(lambda z: integrand(z, competitor, "kl"))
    return result
