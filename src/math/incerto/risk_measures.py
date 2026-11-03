"""Loss quantiles, expected shortfall, and specified Pareto uncertainty models.

``tail_probability`` is the upper-tail mass, not the confidence level.
Mathematical infinite moments return inf; finite-result overflow raises.
These are model evaluations, not fitted risk guarantees.
"""

from fractions import Fraction
from math import fsum

import numpy as np
from scipy.optimize import brentq
from scipy.special import betaln, logsumexp

from xmath.incerto.limits import _scalar


def _tail_probability(value):
    p = _scalar(value, "tail_probability")
    if not 0 < p < 1:
        raise ValueError("tail_probability must lie strictly between zero and one")
    return p


def _positive_exp(log_value):
    with np.errstate(over="ignore", under="ignore", invalid="ignore"):
        value = float(np.exp(log_value))
    if not np.isfinite(value) or value <= 0:
        raise FloatingPointError("finite positive result is not representable")
    return value


def _vector(value, name):
    if np.iscomplexobj(value):
        raise ValueError(f"{name} must be a finite real vector")
    try:
        result = np.asarray(value, dtype=float)
    except (ValueError, TypeError, OverflowError) as error:
        raise ValueError(f"{name} must be a finite real vector") from error
    if result.ndim != 1 or result.size == 0 or not np.all(np.isfinite(result)):
        raise ValueError(f"{name} must be a nonempty finite vector")
    return result


def _weighted_vectors(values, probabilities):
    x, w = _vector(values, "values"), _vector(probabilities, "probabilities")
    if x.shape != w.shape or np.any((w < 0) | (w > 1)):
        raise ValueError("probabilities must match values and lie in [0, 1]")
    total = fsum(w)
    if abs(total - 1) > 1e-12:
        raise ValueError("probabilities must sum to one within 1e-12")
    keep = w > 0
    return x[keep], w[keep] / total


def pareto_risk(alpha, tail_probability, *, xm=1.0):
    """Return {var, es} for an exact Type-I Pareto loss.

    Finite scalars alpha>0, xm>0 and 0<tail_probability<1. VaR is at
    confidence 1-tail_probability. ES is +inf exactly when alpha<=1.
    Compute in logs to avoid intermediate power overflow. Unrepresentable
    finite positive results raise FloatingPointError; NaN/inf inputs reject.
    """
    a = _scalar(alpha, "alpha", positive=True)
    m = _scalar(xm, "xm", positive=True)
    p = _tail_probability(tail_probability)
    with np.errstate(over="ignore"):
        log_q = np.log(m) - np.log(p) / a
    q = _positive_exp(log_q)
    es = np.inf if a <= 1 else _positive_exp(log_q + np.log1p(1 / (a - 1)))
    return {"var": q, "es": float(es)}


def discrete_risk(values, probabilities, tail_probability):
    """VaR and ES of a finite nonnegative loss law, including quantile atoms.

    Equal nonempty finite vectors; nonnegative values; probabilities in
    [0,1] summing to one within 1e-12 (then normalized). Zero masses are
    ignored. ES averages exactly the upper tail_probability mass, splitting
    the quantile atom when needed. It is not the strict-exceedance average.
    """
    x, w = _weighted_vectors(values, probabilities)
    if np.any(x < 0):
        raise ValueError("loss values must be nonnegative")
    p = _tail_probability(tail_probability)
    order = np.argsort(x)
    x, w = x[order], w[order]
    # Work from the upper tail: computing 1-p would lose tiny probabilities.
    above = np.r_[np.cumsum(w[:0:-1], dtype=np.longdouble)[::-1], 0]
    q = float(x[np.flatnonzero(above <= np.longdouble(p))[0]])
    remaining = np.longdouble(p)
    terms = []
    for value, mass in zip(x[::-1], w[::-1]):
        take = min(remaining, np.longdouble(mass))
        terms.append(float(np.longdouble(value) * (take / np.longdouble(p))))
        remaining -= take
        if remaining <= 0:
            break
    return {"var": q, "es": fsum(terms)}


def pareto_mixture_risk(alphas, probabilities, tail_probability, *, xm=1.0):
    """Risk of a finite mixture of Pareto laws with one common minimum xm.

    alphas in [0.001,1000]; probability-vector contract as in discrete_risk;
    finite xm>0 and 0<tail_probability<1. This returns the mixture's quantile
    and ES, not averages of component risk measures. Solve the log-survival
    equation in log(x/xm), then integrate at that common quantile. Any
    positive-weight component with alpha<=1 makes ES infinite. Zero-weight
    components are ignored after input validation. Finite overflow raises.
    """
    original = _vector(alphas, "alphas")
    if np.any((original < .001) | (original > 1000)):
        raise ValueError("alphas must lie in [0.001, 1000]")
    a, w = _weighted_vectors(original, probabilities)
    p = _tail_probability(tail_probability)
    m = _scalar(xm, "xm", positive=True)
    if np.all(a == a[0]):
        return pareto_risk(a[0], p, xm=m)
    log_p, log_w = np.log(p), np.log(w)
    log_w = log_w - logsumexp(log_w)

    def log_survival(z):
        az = a*z
        if np.max(az) < .5:
            # Near p=1, subtracting almost equal log-sums can lose the
            # bracket sign. Compute the small CDF before taking log1p.
            return np.log1p(np.dot(w, np.expm1(-az)))
        return logsumexp(log_w - az)

    upper = (-log_p / np.min(a)) * (1 + 1e-14)
    t = brentq(lambda z: log_survival(z) - log_p,
               0, upper, xtol=np.nextafter(0., 1.), rtol=8*np.finfo(float).eps)
    log_q = np.log(m) + t
    q = _positive_exp(log_q)
    if np.any(a <= 1):
        return {"var": q, "es": float("inf")}
    log_excess = logsumexp(log_w + np.log(m) + (1-a)*t - np.log(a-1))
    es = _positive_exp(np.logaddexp(log_q, log_excess-log_p))
    return {"var": q, "es": es}


def beta_pareto_quantile_moment(a, b, alpha, order, *, xm=1.0):
    """E[(xm*P**(-1/alpha))**order] for P~Beta(a,b), fixed alpha.

    Beta shapes in [0.001,10000], finite alpha>0, order>=0 and xm>0.
    The order-zero moment is one. For positive order the result is +inf
    when order>=a*alpha; otherwise evaluate a beta-function ratio in logs.
    Finite positive overflow/underflow raises FloatingPointError. This
    randomizes a probability, not a tail exponent or the underlying loss.
    """
    a, b = _scalar(a, "a", positive=True), _scalar(b, "b", positive=True)
    if not (.001 <= a <= 10000 and .001 <= b <= 10000):
        raise ValueError("beta shapes must lie in [0.001, 10000]")
    alpha = _scalar(alpha, "alpha", positive=True)
    order = _scalar(order, "order")
    m = _scalar(xm, "xm", positive=True)
    if order < 0:
        raise ValueError("order must be nonnegative")
    if order == 0:
        return 1.0
    # Preserve the exact sign and size of the gap for the supplied floats.
    # Even extended-precision subtraction can turn a finite moment into inf.
    exact_delta = Fraction(a) - Fraction(order) / Fraction(alpha)
    if exact_delta <= 0:
        return float("inf")
    delta = float(exact_delta)
    ratio = np.longdouble(order) / np.longdouble(alpha)
    # b=1 has an elementary ratio; avoid cancelling nearly equal log-betas.
    log_ratio = (float(np.log1p(ratio / delta)) if b == 1 else
                 betaln(float(delta), b) - betaln(a, b))
    with np.errstate(over="ignore", invalid="ignore"):
        log_value = order*np.log(m) + log_ratio
    return _positive_exp(log_value)


__all__ = ["pareto_risk", "discrete_risk", "pareto_mixture_risk",
           "beta_pareto_quantile_moment"]
