"""Exact-model calculations for maxima, hidden moments and Pareto calibration.

Counts are integers in [1, 10**9]. These are population calculations, not
fits or guarantees for a selected threshold. See the chapter-9 teaching pages.
"""

from math import isfinite, log
import operator

import numpy as np
from scipy.integrate import quad
from scipy.special import betaln
from scipy.stats import beta, invgamma, norm


def _count(value, minimum=1):
    if isinstance(value, (bool, np.bool_)):
        raise ValueError("count must be an integer")
    try:
        result = operator.index(value)
    except TypeError as exc:
        raise ValueError("count must be an integer") from exc
    if not minimum <= result <= 10**9:
        raise ValueError(f"count must lie between {minimum} and 1000000000")
    return result


def _positive(value, name):
    if np.ndim(value) != 0 or not isfinite(value) or value <= 0:
        raise ValueError(f"{name} must be a finite positive scalar")
    return float(value)


def _order(p):
    if np.ndim(p) != 0 or not isfinite(p) or p < 0:
        raise ValueError("p must be a finite nonnegative scalar")
    return float(p)


def pareto_hidden_moment(threshold, alpha, *, x_m=1.0, p=1.0):
    """Return E[X**p 1{X > threshold}] for an exact Pareto parent.

    alpha and x_m are positive finite scalars, p >= 0 is finite, and every
    threshold is finite and >= x_m. Returns inf for p >= alpha; otherwise
    evaluates the moment in logs. Numerical overflow raises FloatingPointError,
    while underflow to zero is allowed. Scalar input returns a Python float.
    This is neither a conditional moment nor an overshoot expectation.
    """
    alpha, x_m, p = _positive(alpha, "alpha"), _positive(x_m, "x_m"), _order(p)
    t = np.asarray(threshold, dtype=float)
    if np.any(~np.isfinite(t)) or np.any(t < x_m):
        raise ValueError("threshold must be finite and at least x_m")
    if p >= alpha:
        result = np.full_like(t, np.inf)
    else:
        difference = t-x_m
        near = difference <= x_m
        log_ratio = np.empty_like(t)
        log_ratio[near] = np.log1p(difference[near]/x_m)
        log_ratio[~near] = np.log(t[~near])-log(x_m)
        # Combine the power terms before adding the potentially small prefactor.
        # A negative infinite log power represents permitted underflow to zero.
        with np.errstate(over="ignore", invalid="ignore"):
            log_power = p*log(x_m)-(alpha-p)*log_ratio
            if np.any(np.isnan(log_power)):
                # Factor out alpha when both products overflow before cancelling.
                balanced = alpha*((p/alpha)*log(x_m)-((alpha-p)/alpha)*log_ratio)
                log_power = np.where(np.isnan(log_power), balanced, log_power)
        if np.any(np.isposinf(log_power)):
            raise FloatingPointError("Pareto hidden moment is not representable")
        with np.errstate(over="raise", invalid="raise", under="ignore"):
            result = np.exp(np.log1p(p/(alpha-p))+log_power)
    return float(result) if result.ndim == 0 else result


def expected_pareto_hidden_fraction(n, alpha, *, p=1.0):
    """Expected fraction of the population pth moment beyond an iid maximum.

    Exact Pareto model, n >= 1, alpha > 0, p >= 0. For p < alpha this is
    n*B(n, 2-p/alpha), independent of the lower cutoff. Returns nan when
    p >= alpha because the population moment used as denominator is infinite.
    The p=0 case is missing probability, exactly 1/(n+1).
    """
    n, alpha, p = _count(n), _positive(alpha, "alpha"), _order(p)
    if p >= alpha:
        return float("nan")
    if p == 0:
        return 1.0/(n+1)
    return float(np.exp(log(n)+betaln(n, 2-p/alpha)))


def maximum_missing_mass(n):
    """Frozen Beta(1,n) law of bar F(M_n) for iid draws from continuous F.

    The CDF, survival and quantiles refer to probability mass, not magnitudes.
    Atoms, dependence, or substituting an estimated F invalidate this exact law.
    """
    return beta(1, _count(n))


def pareto_exponent_sampling(alpha, count, *, debiased=False):
    """Frozen inverse-gamma law of an exact Pareto exponent estimate.

    Known fixed cutoff: count is the sample size. Hill at a deterministic
    retained count k: count=k, with k strictly smaller than the original size.
    The MLE law has shape=count, scale=count*alpha. Debiasing multiplies the
    estimate by (count-1)/count, retaining shape=count and changing the scale
    to (count-1)*alpha; this option requires count>=2. No calibration after
    data-dependent threshold/count selection, or for general Pareto-type tails.
    """
    alpha, count = _positive(alpha, "alpha"), _count(count)
    if not isinstance(debiased, (bool, np.bool_)):
        raise ValueError("debiased must be boolean")
    if debiased and count < 2:
        raise ValueError("debiasing requires at least two log-excesses")
    scale = (count-1 if debiased else count)*alpha
    if not isfinite(scale) or scale <= 0:
        raise FloatingPointError("inverse-gamma scale is not representable")
    return invgamma(a=count, scale=scale)


def gaussian_maximum_norming(n, *, method="mills"):
    """Return (a_n,b_n) for (M_n-b_n)/a_n, iid standard normals, n>=3.

    mills: b_n=normal.isf(1/n), a_n=sf(b_n)/pdf(b_n).
    asymptotic: a_n=1/sqrt(2 log n), with the log-log correction to b_n.
    Both yield the standard maxima Gumbel limit. Neither is a finite-n fit.
    """
    n = _count(n, 3)
    if method == "mills":
        b = norm.isf(1.0/n)
        a = np.exp(norm.logsf(b)-norm.logpdf(b))
    elif method == "asymptotic":
        root = np.sqrt(2*log(n))
        a = 1/root
        b = root-(log(log(n))+log(4*np.pi))/(2*root)
    else:
        raise ValueError("method must be 'mills' or 'asymptotic'")
    return float(a), float(b)


def gaussian_maximum_cdf(x, n):
    """Exact standard-normal iid maximum CDF Phi(x)**n, evaluated in logs.

    x may be scalar or array and may include infinities; NaNs are rejected.
    n is a positive integer. Underflow is returned as zero.
    """
    n = _count(n)
    values = np.asarray(x, dtype=float)
    if np.any(np.isnan(values)):
        raise ValueError("x must not contain nan")
    with np.errstate(under="ignore"):
        result = np.exp(n*norm.logcdf(values))
    return float(result) if result.ndim == 0 else result


def expected_gaussian_hidden_mean(n):
    """Quadrature of E[phi(M_n)] for iid standard-normal maxima, n>=1.

    Returns {'value', 'abs_error'}; the error is QUADPACK's estimate, not a
    rigorous bound. Integrates over an Exp(1) variable W using the exact map
    M_n = normal.isf(-expm1(-W/n)). All possible maxima, including negative
    ones, are included. The result is in standard-deviation units, never a
    fraction of the zero population mean. Quadrature failure raises.
    """
    n = _count(n)

    def integrand(w):
        z = norm.isf(-np.expm1(-w/n))
        return np.exp(norm.logpdf(z)-w)

    result = quad(integrand, 0, np.inf, epsabs=1e-14, epsrel=2e-9,
                  limit=150, full_output=1)
    value, error = result[:2]
    if len(result) != 3 or not isfinite(value) or error > max(1e-14, 2e-9*abs(value)):
        raise RuntimeError("Gaussian hidden-mean quadrature did not converge")
    return {"value": float(value), "abs_error": float(error)}
