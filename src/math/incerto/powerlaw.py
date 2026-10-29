"""Power-law tail fitting and model checks for iid positive observations.

All ``alpha`` arguments/results use the repository's SURVIVAL exponent:
CSN's density/mass exponent is ``a = alpha + 1``. Discrete laws have mass
k**(-a)/zeta(a, xmin), not a rounded continuous Pareto law. Fits include ties
at xmin. Invalid inputs raise ValueError; failed numerical work raises or
returns an explicit unsuccessful alternative fit. No observations are dropped
because they are nonfinite. Alternative densities are continuous only.
"""
from __future__ import annotations

import warnings

import numpy as np
from numpy.typing import ArrayLike
from scipy.integrate import IntegrationWarning, quad
from scipy.optimize import minimize, minimize_scalar
from scipy.special import log_ndtr, zeta
from scipy.stats import chi2, norm

from .distributions import pareto_type1
from .estimators import _positive_1d_sample
from .power_laws import _positive
from .tail_diagnostics import _rng_from_state, _validate_sample_size

__all__ = [
    "powerlaw_mle_continuous", "powerlaw_mle_discrete", "ks_distance_powerlaw",
    "select_xmin", "powerlaw_standard_error", "sample_powerlaw",
    "powerlaw_bootstrap_se", "powerlaw_gof_bootstrap", "fit_tail_model",
    "likelihood_ratio_test",
]


def _cutoff(xmin, discrete=False):
    if np.iscomplexobj(xmin) or np.ndim(xmin) != 0:
        raise ValueError("xmin must be a positive finite scalar")
    u = _positive(xmin, "xmin")
    if discrete and (u != np.floor(u) or u > 2**53 - 1):
        raise ValueError("discrete xmin must be an exactly represented positive integer")
    return u


def _sample(x, discrete=False):
    if np.iscomplexobj(x):
        raise ValueError("x must be real")
    values = _positive_1d_sample(x)
    if discrete and (np.any(values != np.floor(values)) or np.any(values > 2**53 - 1)):
        raise ValueError("discrete data must be exactly represented positive integers")
    return values


def _tail(x, xmin, discrete=False):
    u = _cutoff(xmin, discrete)
    values = _sample(x, discrete)
    tail = values[values >= u]
    if tail.size < 2:
        raise ValueError("at least two observations at or above xmin are required")
    return tail, u


def _log_ratio(x, u):
    result = np.log(x) - np.log(u)
    near = x <= 2 * u if u < np.finfo(float).max / 2 else np.ones(x.shape, bool)
    result[near] = np.log1p((x[near] - u) / u)
    return result


def powerlaw_mle_continuous(x: ArrayLike, xmin: float) -> float:
    """Return n_tail / sum(log(x/xmin)), the survival-exponent MLE.

    Validate the entire positive finite vector, then retain x >= xmin.
    xmin is fixed for this calculation; at least two tail values are required.
    An all-xmin tail has no finite MLE and raises ValueError.
    """
    tail, u = _tail(x, xmin)
    mean_log = float(np.mean(_log_ratio(tail, u)))
    if mean_log <= 0:
        raise ValueError("all tail values equal xmin; no finite exponent MLE")
    alpha = 1 / mean_log
    if not np.isfinite(alpha):
        raise FloatingPointError("exponent overflow")
    return float(alpha)


def _log_zeta(a, u):
    value = zeta(a, u)
    if not np.all(np.isfinite(value)) or np.any(value <= 0):
        raise FloatingPointError("Hurwitz zeta is outside floating-point range")
    return np.log(value)


def powerlaw_mle_discrete(x: ArrayLike, xmin: int, *, approximate=False) -> float:
    """Fit mass k**(-(alpha+1))/zeta(alpha+1,xmin), returning alpha.

    Default: numerical maximization of the exact zeta likelihood. The optional
    approximation returns 1/mean(log(x/(xmin-.5))); it can be badly biased at
    small xmin or for steep laws. Exact optimization expands its upper bracket
    up to 12 times, with at most 300 scalar iterations per bracket. Failure or
    zeta underflow raises; there is no silent return of a search boundary.
    """
    tail, u = _tail(x, xmin, True)
    if np.all(tail == u):
        raise ValueError("all tail values equal xmin; no finite exponent MLE")
    approx = float(1 / np.mean(_log_ratio(tail, u - .5)))
    if approximate:
        return approx
    mean_log = float(np.mean(_log_ratio(tail, u)))

    def objective(log_alpha):
        alpha = np.exp(log_alpha)
        return (alpha + 1) * mean_log + _log_zeta(alpha + 1, u) + (alpha + 1)*np.log(u)

    upper = max(2., 2 * approx)
    for _ in range(12):
        result = minimize_scalar(objective, bounds=(-16., np.log(upper)), method="bounded",
                                 options={"xatol": 1e-10, "maxiter": 300})
        if not result.success or not np.isfinite(result.fun):
            raise RuntimeError("discrete exponent optimization failed")
        if result.x <= -15.99:
            raise FloatingPointError("exponent below numerical search range")
        if result.x < np.log(upper) - .01:
            return float(np.exp(result.x))
        upper *= 2
    raise RuntimeError("could not bracket discrete exponent MLE")


def ks_distance_powerlaw(x: ArrayLike, alpha: float, xmin: float, *, discrete=False) -> float:
    """Supremum CDF distance on x >= xmin, including both sides of jumps.

    For integer data compare at k-1 and k for every observed integer k; this
    also covers empty lattice gaps without enumerating them. Continuous ties
    are compared before/after the empirical jump against the same model CDF.
    This statistic has no fixed-null KS p-value after fitting parameters.
    """
    tail, u = _tail(x, xmin, discrete)
    alpha = _positive(alpha, "alpha")
    points, counts = np.unique(tail, return_counts=True)
    right = np.cumsum(counts) / tail.size
    left = right - counts / tail.size
    if discrete:
        denominator = np.exp(_log_zeta(alpha + 1, u))
        model_right = 1 - zeta(alpha + 1, points + 1) / denominator
        model_left = 1 - zeta(alpha + 1, points) / denominator
    else:
        model_right = -np.expm1(-alpha * _log_ratio(points, u))
        model_left = model_right
    return float(max(np.max(np.abs(right - model_right)), np.max(np.abs(left - model_left))))


def select_xmin(x: ArrayLike, *, discrete=False, min_tail=50, candidates=None) -> dict:
    """Minimize refitted KS over unique observed values or supplied thresholds.

    ``min_tail`` is an integer >=2. Explicit candidates are a positive finite
    1-D grid (integers in discrete mode); ties in KS choose the lowest xmin.
    Returns xmin, alpha, n_tail, ks, discrete, and candidate arrays xmins,
    alphas, counts, distances. Ineligible/all-cutoff tails have NaN entries;
    numerical failures raise. No eligible finite MLE raises ValueError.
    Default work is quadratic in sample size; use a declared grid for large n.
    """
    values = _sample(x, discrete)
    minimum = _validate_sample_size(min_tail)
    if minimum < 2:
        raise ValueError("min_tail must be at least two")
    if candidates is None:
        grid = np.unique(values)
    else:
        if np.iscomplexobj(candidates):
            raise ValueError("candidates must be real")
        grid = np.asarray(candidates, dtype=float)
        if grid.ndim != 1 or grid.size == 0:
            raise ValueError("candidates must be a nonempty vector")
        grid = np.unique([_cutoff(v, discrete) for v in grid])
    counts = np.array([np.count_nonzero(values >= u) for u in grid])
    alphas = np.full(grid.size, np.nan)
    distances = np.full(grid.size, np.nan)
    mle = powerlaw_mle_discrete if discrete else powerlaw_mle_continuous
    for i, u in enumerate(grid):
        if counts[i] < minimum or np.max(values) <= u:
            continue
        alphas[i] = mle(values, u)
        distances[i] = ks_distance_powerlaw(values, alphas[i], u, discrete=discrete)
    if not np.any(np.isfinite(distances)):
        raise ValueError("no candidate has enough tail observations and a finite MLE")
    best = int(np.nanargmin(distances))
    return dict(xmin=float(grid[best]), alpha=float(alphas[best]), n_tail=int(counts[best]),
                ks=float(distances[best]), discrete=bool(discrete), xmins=grid,
                alphas=alphas, counts=counts, distances=distances)


def _discrete_log_variance(alpha, u):
    # Sum (k/u)**(-a) * log(k/u)**r, r=0,1,2. Scaling by u avoids
    # zeta underflow, and retains tiny positive log moments for steep laws.
    # Euler--Maclaurin tail through B4; differentiate its terms analytically.
    # See https://dlmf.nist.gov/25.11.iii. Check convergence by doubling the sum.
    a, previous = alpha + 1, None
    for count in (32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536):
        logs = np.log1p(np.arange(count, dtype=float) / u)
        weights = np.exp(-a * logs)
        moments = np.array([np.sum(weights * logs**r) for r in range(3)])
        endpoint = u + count
        log_end = np.log1p(count / u)
        weight = np.exp(-a * log_end)
        integral = u * np.exp(-alpha * log_end) / alpha
        moments += integral * np.array([
            1., log_end + 1/alpha,
            log_end**2 + 2*log_end/alpha + 2/alpha**2,
        ])
        moments += .5 * weight * np.array([1., log_end, log_end**2])
        for order, coefficient in ((1, 1/12), (3, -1/720)):
            factors = a + np.arange(order)
            term = coefficient * weight * np.prod(factors / endpoint)
            shift = log_end - np.sum(1/factors)
            moments += term * np.array([1., shift, shift**2 - np.sum(1/factors**2)])
        if not np.all(np.isfinite(moments)) or np.any(moments <= 0):
            raise FloatingPointError("discrete Fisher curvature is not resolved")
        mean, second = moments[1:] / moments[0]
        variance = second - mean**2
        # Both truncation changes and roundoff must be small relative to I.
        if previous is not None:
            error = np.abs(moments - previous) / moments[0]
            variance_error = error[2] + 2*abs(mean)*error[1] + (second + 2*mean**2)*error[0]
            rounding = 64*(np.finfo(float).eps*(second + mean**2) + np.nextafter(0., 1.))
            if variance > 0 and variance_error + rounding < 1e-9*variance:
                return float(variance)
        previous = moments
    raise FloatingPointError("discrete Fisher curvature is not resolved")


def powerlaw_standard_error(alpha: float, n_tail: int, *, xmin=1, discrete=False) -> float:
    """Fixed-threshold asymptotic SE for the survival (or density) exponent.

    Continuous: alpha/sqrt(n_tail). Discrete: 1/sqrt(n_tail*I), with I the
    variance of log X, evaluated by scaled log-moment sums with an
    Euler--Maclaurin tail and a convergence/roundoff check. Does not include
    threshold choice or model error. Ill-resolved/nonpositive curvature raises.
    """
    alpha = _positive(alpha, "alpha")
    n = _validate_sample_size(n_tail)
    u = _cutoff(xmin, discrete)
    if not discrete:
        return float(alpha / np.sqrt(n))
    with np.errstate(over="raise", invalid="raise", divide="raise"):
        information = _discrete_log_variance(alpha, u)
    return float(1 / np.sqrt(n * information))


def sample_powerlaw(alpha: float, xmin: float, size: int, *, discrete=False, random_state=None):
    """Draw a continuous Pareto or exact discrete zeta tail with a PCG64 seed.

    Reuses pareto_type1 for continuous draws. Discrete inverse-CDF search uses
    Hurwitz-zeta survival with a doubling bracket and integer bisection. It
    fails on draws beyond 2**53-1, rather than rounding/clipping the tail.
    Positive integer size is required; returns a 1-D array. Nonfinite draws
    raise FloatingPointError.
    """
    alpha, u = _positive(alpha, "alpha"), _cutoff(xmin, discrete)
    n, rng = _validate_sample_size(size), _rng_from_state(random_state)
    if not discrete:
        with np.errstate(over="raise", invalid="raise"):
            values = pareto_type1.rvs(alpha, scale=u, size=n, random_state=rng)
        if not np.all(np.isfinite(values)):
            raise FloatingPointError("continuous draw overflow")
        return values
    denominator = np.exp(_log_zeta(alpha + 1, u))
    target = 1 - rng.random(n)
    low = np.full(n, int(u) - 1, dtype=np.int64)
    high = np.full(n, int(u), dtype=np.int64)
    ceiling = 2**53 - 1
    while True:
        expand = zeta(alpha + 1, high.astype(float) + 1) / denominator > target
        if not np.any(expand):
            break
        if np.any(high[expand] == ceiling):
            raise FloatingPointError("discrete draw exceeds exact integer range")
        low[expand] = high[expand]
        high[expand] = np.minimum(2 * high[expand], ceiling)
    while np.any(high - low > 1):
        mid = low + (high - low) // 2
        above = zeta(alpha + 1, mid.astype(float) + 1) / denominator > target
        active = high - low > 1
        low = np.where(active & above, mid, low)
        high = np.where(active & ~above, mid, high)
    return high


def _bootstrap(x, replicates, random_state, discrete, min_tail, candidates, semiparametric):
    values = _sample(x, discrete)
    b = _validate_sample_size(replicates)
    if b < 2:
        raise ValueError("at least two replicates required")
    rng = _rng_from_state(random_state)
    fitted = select_xmin(values, discrete=discrete, min_tail=min_tail, candidates=candidates)
    body = values[values < fitted["xmin"]]
    rows = np.empty((b, 4))
    generated_counts = np.empty(b, dtype=int)
    for j in range(b):
        if semiparametric:
            nt = int(rng.binomial(values.size, fitted["n_tail"] / values.size))
            generated_counts[j] = nt
            tail = (sample_powerlaw(fitted["alpha"], fitted["xmin"], nt,
                    discrete=discrete, random_state=rng) if nt else np.empty(0))
            body_draw = rng.choice(body, values.size-nt) if nt < values.size else np.empty(0)
            draw = np.concatenate((body_draw, tail))
        else:
            draw = rng.choice(values, values.size)
            generated_counts[j] = np.count_nonzero(draw >= fitted["xmin"])
        try:
            refit = select_xmin(draw, discrete=discrete, min_tail=min_tail, candidates=candidates)
        except (ValueError, RuntimeError, FloatingPointError) as exc:
            raise RuntimeError(f"bootstrap replicate {j} failed; no replicates discarded") from exc
        rows[j] = [refit["alpha"], refit["xmin"], refit["ks"], refit["n_tail"]]
    return fitted, rows, generated_counts


def powerlaw_bootstrap_se(x: ArrayLike, *, replicates=199, random_state=None,
                          discrete=False, min_tail=50, candidates=None) -> dict:
    """Full-sample empirical bootstrap; reselect xmin and alpha each replicate.

    Return fit, alpha_se, xmin_se, covariance (alpha,xmin order), alphas,
    xmins. Standard deviations/covariance use divisor B-1. These descriptive
    uncertainty estimates need not give valid confidence coverage for a
    discontinuous threshold selector. Failures abort instead of being dropped.
    """
    fit, rows, _ = _bootstrap(x, replicates, random_state, discrete, min_tail, candidates, False)
    covariance = np.cov(rows[:, :2], rowvar=False, ddof=1)
    return dict(fit=fit, alpha_se=float(np.sqrt(covariance[0, 0])),
                xmin_se=float(np.sqrt(covariance[1, 1])), covariance=covariance,
                alphas=rows[:, 0], xmins=rows[:, 1])


def powerlaw_gof_bootstrap(x: ArrayLike, *, replicates=499, random_state=None,
                           discrete=False, min_tail=50, candidates=None) -> dict:
    """CSN semiparametric goodness-of-fit bootstrap with refitted thresholds.

    Each size-n replicate mixes the empirical below-xmin body with the fitted
    tail with probability n_tail/n. Reapply the same candidate RULE, using
    fresh observed values by default, or the same explicit grid if supplied.
    Return fit, p_value = mean(D_boot >= D_observed), mc_se, worst_case_mc_se,
    ks_samples, alphas, xmins, tail_counts and generated_tail_counts. A zero
    estimated mc_se at p=0 or 1 does not remove Monte Carlo uncertainty.
    Failure aborts; no retrying or dropping hard replicates. This is fitted-null
    calibration, not an exact finite-sample test.
    """
    fit, rows, counts = _bootstrap(x, replicates, random_state, discrete, min_tail, candidates, True)
    p = float(np.mean(rows[:, 2] >= fit["ks"]))
    b = rows.shape[0]
    return dict(fit=fit, p_value=p, mc_se=float(np.sqrt(p*(1-p)/b)),
                worst_case_mc_se=float(.5/np.sqrt(b)), ks_samples=rows[:, 2],
                alphas=rows[:, 0], xmins=rows[:, 1], tail_counts=rows[:, 3].astype(int),
                generated_tail_counts=counts)


def _cutoff_log_normalizer(alpha, beta):
    # In t=log(x/u): integral exp(-alpha*t-beta*(exp(t)-1)) dt.
    if beta == 0:
        return -np.log(alpha) if alpha > 0 else np.inf
    mode = max(0., np.log(-alpha) - np.log(beta)) if alpha < 0 else 0.
    at_mode = -alpha if mode > 0 else beta
    log_at_mode = np.log(at_mode)
    peak = -alpha*mode - at_mode + beta
    scale = max(1., np.sqrt(at_mode), alpha + at_mode)

    def integrand(v):
        # Recenter AND scale the peak; subtracting its height alone can leave
        # quadrature sampling only a negligible tail of the integrand.
        s = v / scale
        if s > 50:
            # beta*exp(s) can be representable even when exp(s) overflows.
            log_decay = log_at_mode + s
            if log_decay > 700:
                return 0.
            return np.exp(-alpha*s - np.exp(log_decay) + at_mode)
        return np.exp(-alpha*s - at_mode*np.expm1(s))

    with warnings.catch_warnings():
        warnings.simplefilter("error", IntegrationWarning)
        pieces = [quad(integrand, 0, 1, epsabs=1e-11, epsrel=1e-10),
                  quad(integrand, 1, np.inf, epsabs=1e-11, epsrel=1e-10, limit=200)]
        if mode > 0:
            left = mode * scale
            pieces.append(quad(integrand, -min(left, 1.), 0, epsabs=1e-11, epsrel=1e-10))
            if left > 1:
                points = -2.**np.arange(1, np.ceil(np.log2(left)))
                pieces.append(quad(integrand, -left, -1, epsabs=1e-11,
                                   epsrel=1e-10, points=points, limit=200))
    value, error = np.sum(pieces, axis=0)
    if not np.isfinite(value) or value <= 0 or error > max(1e-9, 1e-7*value):
        raise FloatingPointError("cutoff normalizer quadrature failed")
    return float(np.log(value) - np.log(scale) + peak)


def _fit_cutoff(y, u):
    alpha0 = 1/float(np.mean(y))
    pure_ll = np.log(alpha0) - np.log(u) - (alpha0+1)*y
    with np.errstate(over="raise", invalid="raise"):
        excess = np.expm1(y)
        mean_excess = float(np.mean(excess))
    # The log likelihood is concave in (alpha,beta). At the Pareto MLE,
    # the inward beta score is E_beta=0[X/u-1] - mean(X/u-1).
    # For alpha0<=1 it is +infinity, so that boundary cannot maximize it.
    if alpha0 > 1:
        expected = 1/(alpha0-1)
        tolerance = 64*np.finfo(float).eps*max(expected, mean_excess)
        if expected - mean_excess < -tolerance:
            return (pure_ll, dict(a=alpha0+1, rate=0.), True, True,
                    "pure-power-law boundary")

    log_beta = -np.log(mean_excess)
    bounds = [(-20., 100.), (max(-700., min(-18., log_beta-4)),
                             min(700., max(8., log_beta+4)))]
    starts = [(min(alpha0, 50.), np.clip(log_beta, *bounds[1])),
              (0., np.clip(log_beta, *bounds[1])), (-1., 0.)]

    def loglik(p):
        alpha, beta = p[0], np.exp(p[1])
        with np.errstate(over="ignore", invalid="ignore"):
            return (-(alpha+1)*y - beta*excess - np.log(u)
                    - _cutoff_log_normalizer(alpha, beta))

    def objective(p):
        try:
            ll = loglik(p)
        except (FloatingPointError, IntegrationWarning):
            return 1e100
        return -float(np.mean(ll)) if np.all(np.isfinite(ll)) else 1e100

    for _ in range(8):
        results = [minimize(objective, start, method="L-BFGS-B", bounds=bounds,
                            options={"maxiter": 2000, "ftol": 1e-12, "gtol": 1e-7})
                   for start in starts]
        candidates = [r for r in results if np.isfinite(r.fun) and r.fun < 1e99]
        if not candidates:
            raise RuntimeError("truncated_powerlaw optimization failed at every start")
        best = min(candidates, key=lambda r: r.fun)
        at_bound = [min(v-lo, hi-v) < 1e-4 for v, (lo, hi) in zip(best.x, bounds)]
        inferior = best.fun >= -float(np.mean(pure_ll))
        if not any(at_bound) and not inferior:
            break
        # Expand artificial bounds and restart at the best point and a
        # smaller cutoff. Exhaustion must remain an unsuccessful fit.
        bounds = [(2*bounds[0][0], 2*bounds[0][1]),
                  (max(-700., bounds[1][0]-16), min(700., bounds[1][1]+8))]
        starts = [best.x, (alpha0, max(bounds[1][0], best.x[1]-8)),
                  (0., np.clip(log_beta, *bounds[1]))]
    ll = loglik(best.x)
    if inferior:
        return (pure_ll, dict(a=alpha0+1, rate=0.), False, True,
                "unresolved cutoff optimization; pure-law boundary not certified")
    success = bool(best.success and not any(at_bound))
    status = ("numerical search boundary" if any(at_bound) else
              "ok" if success else "cutoff optimization failed")
    parameters = dict(a=float(best.x[0]+1), rate=float(np.exp(best.x[1])/u))
    return ll, parameters, success, False, status


def fit_tail_model(x: ArrayLike, xmin: float, model="powerlaw", *, discrete=False) -> dict:
    """Fit conditional densities to the SAME retained observations x >= xmin.

    Models: powerlaw, lognormal, exponential, stretched_exponential (Weibull),
    truncated_powerlaw (exponential cutoff). Discrete mode supports powerlaw
    only; comparing integer masses to continuous densities is not valid.
    Returns model, xmin, discrete, n_tail, parameters, per-observation loglik
    in input-tail order, loglikelihood, success, boundary, status.

    Alternative fits use dimensionless x/xmin. Lognormal parameters are
    mu=E(log X) before truncation and sigma. Weibull uses shape and scale.
    Cutoff uses a (density exponent, unrestricted in the interior) and rate.
    Multi-start L-BFGS-B uses finite numerical search boxes, at most 2000
    iterations each; reaching an artificial bound marks success=False.
    Cutoff bounds adapt to the sample scale over at most eight search rounds.
    A rate=0 cutoff fit is certified only by its inward score; an unresolved
    search stays unsuccessful. Interior numerical success is not a certificate
    of a global maximum.
    """
    tail, u = _tail(x, xmin, discrete)
    allowed = {"powerlaw", "lognormal", "exponential", "stretched_exponential", "truncated_powerlaw"}
    if model not in allowed:
        raise ValueError(f"model must be one of {sorted(allowed)}")
    if discrete and model != "powerlaw":
        raise ValueError("alternative fits are continuous; discrete masses need their own likelihood")
    y, logx = _log_ratio(tail, u), np.log(tail)
    if np.all(y == 0) or (model not in {"powerlaw", "exponential"} and np.ptp(y) == 0):
        raise ValueError("degenerate tail has no supported finite fit")
    success, boundary, status = True, False, "ok"
    if model == "powerlaw":
        alpha = powerlaw_mle_discrete(tail, u) if discrete else powerlaw_mle_continuous(tail, u)
        parameters = dict(alpha=alpha)
        ll = (-(alpha+1)*logx - _log_zeta(alpha+1, u) if discrete
              else np.log(alpha) - np.log(u) - (alpha+1)*y)
    elif model == "exponential":
        excess = tail - u
        mean_excess = float(np.mean(excess))
        if not np.isfinite(mean_excess) or mean_excess <= 0:
            raise FloatingPointError("exponential scale outside numerical range")
        parameters = dict(rate=1/mean_excess)
        ll = -np.log(mean_excess) - excess/mean_excess
    elif model == "truncated_powerlaw":
        ll, parameters, success, boundary, status = _fit_cutoff(y, u)
    else:
        if model == "lognormal":
            # Gaussian log-coordinate density conditional on y>=0.
            bounds = [(-100., 100.), (-6., 5.)]
            starts = [(float(np.mean(y)), np.log(max(float(np.std(y)), .1))),
                      (-1., 0.), (-10., 1.)]

            def loglik(p):
                m, s = p[0], np.exp(p[1])
                return -.5*((y-m)/s)**2 - np.log(s) - .5*np.log(2*np.pi) - log_ndtr(m/s) - logx
        elif model == "stretched_exponential":
            # beta=(u/scale)**shape, profiled out at fixed shape.
            bounds = [(-5., 5.)]
            starts = [(0.,), (-1.,), (1.,)]

            def loglik(p):
                shape = np.exp(p[0])
                z = shape*y
                if np.max(z) > 700:
                    return np.full(y.shape, -np.inf)
                beta = 1/np.mean(np.expm1(z))
                return np.log(shape) + np.log(beta) - np.log(u) + (shape-1)*y - beta*np.expm1(z)

        def objective(p):
            try:
                ll_try = loglik(p)
            except (FloatingPointError, IntegrationWarning):
                return 1e100
            return -float(np.mean(ll_try)) if np.all(np.isfinite(ll_try)) else 1e100

        results = [minimize(objective, start, method="L-BFGS-B", bounds=bounds,
                            options={"maxiter": 2000, "ftol": 1e-12, "gtol": 1e-7})
                   for start in starts]
        usable = [r for r in results if r.success and np.isfinite(r.fun) and r.fun < 1e99]
        if not usable:
            raise RuntimeError(f"{model} optimization failed at every start")
        best = min(usable, key=lambda r: r.fun)
        p, ll = best.x, loglik(best.x)
        at_bound = any(min(v-lo, hi-v) < 1e-4 for v, (lo, hi) in zip(p, bounds))
        success = not at_bound
        status = "numerical search boundary" if at_bound else "ok"
        if model == "lognormal":
            parameters = dict(mu=float(p[0]+np.log(u)), sigma=float(np.exp(p[1])))
        elif model == "stretched_exponential":
            shape = float(np.exp(p[0]))
            beta = 1/float(np.mean(np.expm1(shape*y)))
            parameters = dict(shape=shape, scale=float(u*np.exp(-np.log(beta)/shape)))
    if not np.all(np.isfinite(ll)) or not np.all(np.isfinite(list(parameters.values()))):
        raise FloatingPointError("nonfinite fitted log likelihood or parameters")
    return dict(model=model, xmin=u, discrete=bool(discrete), n_tail=int(tail.size),
                parameters=parameters, loglik=ll, loglikelihood=float(np.sum(ll)),
                success=success, boundary=boundary, status=status)


def likelihood_ratio_test(loglik1: ArrayLike, loglik2: ArrayLike, *, nested=False,
                          calibration=None, df=1) -> dict:
    """Compare paired log likelihoods: R=sum(loglik1-loglik2), positive favors 1.

    Non-nested: normalized_R=R/(sqrt(n)*std(d,ddof=0)), two-sided normal p.
    Requires iid observations, regular fitted models, finite nonzero contrast
    variance, a common measure and the same fixed tail. Arrays cannot certify
    these conditions. Zero contrast variance returns NaN statistic/p.
    Nested: model 1 MUST be the smaller null, statistic=-2R. Default p=NaN
    requests simulation calibration. Explicit calibration='chi2' asserts
    regular interior Wilks conditions; 'boundary' asserts the regular one-
    parameter 50:50 point-mass/chi2_1 case (df=1). These are not automatic
    calibrations for a power-law cutoff; heavy tails can violate regularity.
    """
    if np.iscomplexobj(loglik1) or np.iscomplexobj(loglik2):
        raise ValueError("log likelihoods must be real")
    first, second = np.asarray(loglik1, float), np.asarray(loglik2, float)
    if (first.ndim != 1 or first.size < 2 or first.shape != second.shape
            or not np.all(np.isfinite(first)) or not np.all(np.isfinite(second))):
        raise ValueError("paired finite log likelihood vectors of length >=2 required")
    if calibration not in (None, "chi2", "boundary") or (not nested and calibration is not None):
        raise ValueError("calibration applies only to nested tests")
    with np.errstate(over="raise", invalid="raise"):
        d = first-second
        r = float(np.sum(d))
        sd = float(np.std(d, ddof=0))
    normalized, statistic, p, status = np.nan, np.nan, np.nan, "ok"
    if nested:
        degrees = _validate_sample_size(df)
        if r > 1e-7:
            raise ValueError("nested model 2 must fit at least as well as model 1")
        statistic = max(0., -2*r)
        if calibration == "chi2":
            p = float(chi2.sf(statistic, degrees))
        elif calibration == "boundary":
            if degrees != 1:
                raise ValueError("boundary mixture requires df=1")
            p = float(.5*chi2.sf(statistic, 1)) if statistic > 0 else 1.
        else:
            status = "nested statistic requires calibration"
    elif sd == 0:
        status = "zero contrast variance; normal calibration undefined"
    else:
        normalized = r/(np.sqrt(first.size)*sd)
        p = float(2*norm.sf(abs(normalized)))
    return dict(R=r, normalized_R=float(normalized), statistic=float(statistic),
                p_value=p, n=int(first.size), status=status)
