"""Probability distributions used by Incerto examples.

The classes in this module migrate the useful distributions from
``legacy/src/distributions.py`` into the installable package.  They follow the
``scipy.stats.rv_continuous`` pattern so content pages can use familiar methods
such as ``pdf``, ``cdf``, ``sf``, ``ppf``, ``rvs``, and ``stats``.
"""

from __future__ import annotations

import numpy as np
from numpy.typing import ArrayLike, NDArray
from scipy import special
from scipy.stats import gamma as gamma_distribution
from scipy.stats import genextreme, genpareto, invweibull, norm, rv_continuous


def _finite_parameter(value: float, name: str, *, positive: bool = False) -> float:
    if np.iscomplexobj(value) or np.ndim(value) != 0:
        raise ValueError(f"{name} must be a real scalar")
    try:
        value = float(value)
    except (TypeError, ValueError, OverflowError) as exc:
        raise ValueError(f"{name} must be a finite real scalar") from exc
    if not np.isfinite(value) or (positive and value <= 0):
        raise ValueError(f"{name} must be finite" + (" and positive" if positive else ""))
    return value


def generalized_pareto(xi: float, beta: float = 1.0):
    """Frozen zero-location GPD with the page's shape xi and scale beta > 0.

    Exposes SciPy pdf/cdf/sf/logsf/ppf/rvs/support methods. Support is [0, inf)
    for xi >= 0, otherwise [0, -beta/xi]. CDF/survival extend by 0/1 below
    zero and by 1/0 at and above a finite upper endpoint. The density at that
    endpoint can be infinite when xi < -1. Finite scalar parameters required.
    """
    return genpareto(_finite_parameter(xi, "xi"),
                     scale=_finite_parameter(beta, "beta", positive=True))


def generalized_extreme_value(xi: float, mu: float = 0.0, sigma: float = 1.0):
    """Frozen GEV with CDF exp(-(1 + xi*(x-mu)/sigma)**(-1/xi)).

    Uses SciPy genextreme(c=-xi): positive xi is the heavy right-tail regime.
    The xi=0 limit is Gumbel. Support ends at mu-sigma/xi on the left for
    xi>0 and on the right for xi<0; cdf/sf extend continuously outside it.
    Exposes pdf/cdf/sf/logsf/ppf/rvs/support. Parameters are finite scalars,
    sigma > 0. For xi < -1 the density diverges on approach to the right
    endpoint, but SciPy 1.18 assigns pdf=0 at the endpoint itself. A density's
    value at one point does not change the law; cdf=1 and sf=0 there.
    """
    return genextreme(-_finite_parameter(xi, "xi"),
                      loc=_finite_parameter(mu, "mu"),
                      scale=_finite_parameter(sigma, "sigma", positive=True))


def frechet(alpha: float, scale: float = 1.0):
    """Frozen Frechet law: CDF exp(-(y/scale)**(-alpha)) for y > 0.

    Finite positive scalar alpha and scale; zero location. Uses SciPy's
    invweibull and exposes pdf/cdf/sf/logsf/ppf/rvs/support. Below/at zero,
    pdf=cdf=0 and sf=1. Use sf directly to preserve small right tails.
    Inherits SciPy's numerical limits: tiny positive y/scale can overflow
    intermediate powers (e.g. alpha=3, y/scale=1e-100 gives pdf=NaN in 1.18).
    """
    return invweibull(_finite_parameter(alpha, "alpha", positive=True),
                      scale=_finite_parameter(scale, "scale", positive=True))


def _csch(x: ArrayLike) -> NDArray[np.float64]:
    """Return the hyperbolic cosecant of ``x``."""

    return 1.0 / np.sinh(x)


class double_pareto_gen(rv_continuous):
    r"""Symmetric double Pareto distribution.

    The distribution is formed by taking a Pareto random variable ``Y`` with
    lower cutoff 1 and shape ``alpha``, then assigning the sign of ``Y - 1``
    with equal probability.  Its density is

    .. math::

       f(x; \alpha) = \frac{\alpha}{2}(1 + |x|)^{-(\alpha + 1)}.

    Parameters
    ----------
    alpha:
        Positive Pareto tail exponent. Smaller values produce heavier tails.
        The ordinary mean exists only for ``alpha > 1``.

    Notes
    -----
    For ``0 < alpha <= 1``, the mean is reported as ``NaN`` and the variance
    as ``+inf``. The latter is a convention reflecting the infinite raw second
    moment: variance about the ordinary mean is undefined because both the
    positive and negative first moments are infinite. For ``1 < alpha <= 2``,
    the mean is zero and the variance is infinite. For ``alpha > 2``, the mean
    is zero and the variance is ``2 / ((alpha - 1) * (alpha - 2))``.
    """

    def _argcheck(self, alpha: ArrayLike) -> NDArray[np.bool_]:
        return np.asarray(alpha) > 0

    def _pdf(self, x: ArrayLike, alpha: ArrayLike) -> NDArray[np.float64]:
        x_array = np.asarray(x)
        return 0.5 * alpha * np.power(1.0 + np.abs(x_array), -(alpha + 1.0))

    def _cdf(self, x: ArrayLike, alpha: ArrayLike) -> NDArray[np.float64]:
        x_array, alpha_array = np.broadcast_arrays(np.asarray(x), np.asarray(alpha))
        result = np.empty_like(x_array, dtype=float)
        left = x_array < 0.0
        result[left] = 0.5 * np.power(1.0 - x_array[left], -alpha_array[left])
        result[~left] = 1.0 - 0.5 * np.power(
            1.0 + x_array[~left],
            -alpha_array[~left],
        )
        return result

    def _sf(self, x: ArrayLike, alpha: ArrayLike) -> NDArray[np.float64]:
        x_array, alpha_array = np.broadcast_arrays(np.asarray(x), np.asarray(alpha))
        result = np.empty_like(x_array, dtype=float)
        left = x_array < 0.0
        result[left] = 1.0 - 0.5 * np.power(1.0 - x_array[left], -alpha_array[left])
        result[~left] = 0.5 * np.power(1.0 + x_array[~left], -alpha_array[~left])
        return result

    def _ppf(self, q: ArrayLike, alpha: ArrayLike) -> NDArray[np.float64]:
        q_array = np.asarray(q)
        left = 1.0 - np.power(2.0 * q_array, -1.0 / alpha)
        right = np.power(2.0 * (1.0 - q_array), -1.0 / alpha) - 1.0
        return np.where(q_array < 0.5, left, right)

    def _stats(self, alpha: ArrayLike) -> tuple[
        NDArray[np.float64],
        NDArray[np.float64],
        None,
        None,
    ]:
        alpha_array = np.asarray(alpha, dtype=float)
        mean = np.where(alpha_array > 1.0, 0.0, np.nan)
        variance = np.full_like(alpha_array, np.inf, dtype=float)
        np.divide(
            2.0,
            (alpha_array - 1.0) * (alpha_array - 2.0),
            out=variance,
            where=alpha_array > 2.0,
        )
        return mean, variance, None, None


class pareto_type1_gen(rv_continuous):
    """Pareto Type I distribution with unit lower cutoff.

    The canonical distribution has survival function
    ``sf(x, alpha) = x ** (-alpha)`` for ``x >= 1``.  Use SciPy's standard
    ``scale`` keyword to set a lower cutoff ``x_m`` other than 1.

    Parameters
    ----------
    alpha:
        Positive Pareto tail exponent.  The mean is finite only for
        ``alpha > 1`` and the variance only for ``alpha > 2``.
    """

    def _argcheck(self, alpha: ArrayLike) -> NDArray[np.bool_]:
        return np.asarray(alpha) > 0.0

    def _pdf(self, x: ArrayLike, alpha: ArrayLike) -> NDArray[np.float64]:
        return alpha * np.power(x, -(alpha + 1.0))

    def _cdf(self, x: ArrayLike, alpha: ArrayLike) -> NDArray[np.float64]:
        return 1.0 - np.power(x, -alpha)

    def _sf(self, x: ArrayLike, alpha: ArrayLike) -> NDArray[np.float64]:
        return np.power(x, -alpha)

    def _logsf(self, x: ArrayLike, alpha: ArrayLike) -> NDArray[np.float64]:
        return -alpha * np.log(x)

    def _ppf(self, q: ArrayLike, alpha: ArrayLike) -> NDArray[np.float64]:
        return np.power(1.0 - np.asarray(q), -1.0 / alpha)

    def _stats(self, alpha: ArrayLike) -> tuple[
        NDArray[np.float64],
        NDArray[np.float64],
        None,
        None,
    ]:
        alpha_array = np.asarray(alpha, dtype=float)
        mean = np.full_like(alpha_array, np.inf, dtype=float)
        variance = np.full_like(alpha_array, np.inf, dtype=float)

        np.divide(
            alpha_array,
            alpha_array - 1.0,
            out=mean,
            where=alpha_array > 1.0,
        )
        np.divide(
            alpha_array,
            (alpha_array - 1.0) ** 2 * (alpha_array - 2.0),
            out=variance,
            where=alpha_array > 2.0,
        )
        return mean, variance, None, None


class hypsecant2_gen(rv_continuous):
    """Distribution with density ``0.5 / cosh(x) ** 2``.

    This is a logistic distribution with location 0 and scale ``1/2`` written
    in the hyperbolic-secant form used by the legacy notebooks.
    """

    def _argcheck(self) -> bool:
        return True

    def _pdf(self, x: ArrayLike) -> NDArray[np.float64]:
        return 0.5 / np.cosh(x) ** 2

    def _cdf(self, x: ArrayLike) -> NDArray[np.float64]:
        return 0.5 * (1.0 + np.tanh(x))

    def _ppf(self, q: ArrayLike) -> NDArray[np.float64]:
        return np.arctanh(2.0 * np.asarray(q) - 1.0)

    def _stats(self) -> tuple[float, float, float, float]:
        return 0.0, np.pi**2 / 12.0, 0.0, 6.0 / 5.0

    def chf(
        self,
        t: ArrayLike,
        loc: float = 0.0,
        scale: float = 1.0,
    ) -> NDArray[np.complex128]:
        """Return the characteristic function at frequencies ``t``.

        Parameters
        ----------
        t:
            Frequency or array of frequencies.
        loc:
            Location shift applied to the distribution.
        scale:
            Positive scale multiplier applied to the distribution.

        Returns
        -------
        numpy.ndarray
            Complex characteristic-function values.
        """

        if scale <= 0:
            raise ValueError("scale must be positive")

        t_array = np.asarray(t, dtype=float)
        z = np.pi * t_array * scale / 2.0
        base = np.ones_like(t_array, dtype=float)
        nonzero = t_array != 0.0
        base[nonzero] = z[nonzero] * _csch(z[nonzero])
        return np.exp(1j * loc * t_array) * base


class simple_normal_mixture_gen(rv_continuous):
    """Equal-weight mixture of two centered normal distributions.

    The component variances are ``1 + a`` and ``1 - a``.  The continuous
    distribution requires ``0 <= a < 1``; at ``a = 1`` one component degenerates
    at zero and no longer has an ordinary density.
    """

    def _argcheck(self, a: ArrayLike) -> NDArray[np.bool_]:
        a_array = np.asarray(a)
        return (0.0 <= a_array) & (a_array < 1.0)

    def _pdf(self, x: ArrayLike, a: ArrayLike) -> NDArray[np.float64]:
        scale_high = np.sqrt(1.0 + a)
        scale_low = np.sqrt(1.0 - a)
        return 0.5 * (
            norm.pdf(x, loc=0.0, scale=scale_high)
            + norm.pdf(x, loc=0.0, scale=scale_low)
        )

    def _cdf(self, x: ArrayLike, a: ArrayLike) -> NDArray[np.float64]:
        scale_high = np.sqrt(1.0 + a)
        scale_low = np.sqrt(1.0 - a)
        return 0.5 * (
            norm.cdf(x, loc=0.0, scale=scale_high)
            + norm.cdf(x, loc=0.0, scale=scale_low)
        )

    def _sf(self, x: ArrayLike, a: ArrayLike) -> NDArray[np.float64]:
        return 0.5 * (norm.sf(x, scale=np.sqrt(1.0 + a))
                      + norm.sf(x, scale=np.sqrt(1.0 - a)))

    def _logsf(self, x: ArrayLike, a: ArrayLike) -> NDArray[np.float64]:
        return np.logaddexp(norm.logsf(x, scale=np.sqrt(1.0 + a)),
                            norm.logsf(x, scale=np.sqrt(1.0 - a))) - np.log(2.0)

    def _stats(self, a: ArrayLike) -> tuple[float, float, None, None]:
        return 0.0, 1.0, None, None

    def _rvs(
        self,
        a: ArrayLike,
        size: int | tuple[int, ...] | None = None,
        random_state=None,
    ) -> NDArray[np.float64]:
        high = random_state.uniform(size=size) < 0.5
        variances = np.where(high, 1.0 + a, 1.0 - a)
        return random_state.normal(loc=0.0, scale=np.sqrt(variances), size=size)


class univariate_variance_gamma_gen(rv_continuous):
    """Univariate variance-gamma distribution.

    Parameters follow the legacy notebook convention: ``alpha`` controls tail
    decay, ``beta`` controls skew, and ``lam`` is the gamma shape parameter.
    The parameter domain is ``alpha > abs(beta)`` and ``lam > 0``.
    """

    def _argcheck(
        self,
        alpha: ArrayLike,
        beta: ArrayLike,
        lam: ArrayLike,
    ) -> NDArray[np.bool_]:
        return (np.asarray(alpha) > np.abs(beta)) & (np.asarray(lam) > 0.0)

    def _pdf(self, x, alpha, beta, lam):
        return np.exp(self._logpdf(x, alpha, beta, lam))

    def _logpdf(self, x, alpha, beta, lam):
        x, alpha, beta, lam = np.broadcast_arrays(
            *[np.asarray(v, dtype=float) for v in (x, alpha, beta, lam)]
        )
        x_abs = np.abs(x)
        nu = lam - 0.5
        # Factoring the difference of squares avoids cancellation near |beta|=alpha.
        log_delta = np.log(alpha - beta) + np.log(alpha + beta)
        normalizer = lam * log_delta - 0.5 * np.log(np.pi) - special.gammaln(lam)
        result = np.full(x.shape, np.inf)
        nonzero = x_abs > 0
        if np.any(nonzero):
            ax = alpha[nonzero]
            xx = x_abs[nonzero]
            order = nu[nonzero]
            # kve(v,z) = exp(z) K_v(z); combine the exponential decay
            # before multiplication, so neither exp(beta*x) nor K_v underflows.
            decay = -(ax - beta[nonzero] * np.sign(x[nonzero])) * xx
            result[nonzero] = (normalizer[nonzero]
                + order * (np.log(xx) - np.log(2.0) - np.log(ax))
                + np.log(special.kve(order, ax * xx)) + decay)
        finite_zero = (x_abs == 0) & (nu > 0)
        if np.any(finite_zero):
            result[finite_zero] = (normalizer[finite_zero] - np.log(2.0)
                + special.gammaln(nu[finite_zero])
                - 2.0 * nu[finite_zero] * np.log(alpha[finite_zero]))
        return result

    def _rvs(
        self,
        alpha: ArrayLike,
        beta: ArrayLike,
        lam: ArrayLike,
        size: int | tuple[int, ...] | None = None,
        random_state=None,
    ) -> NDArray[np.float64]:
        theta = 2.0 / (alpha**2 - beta**2)
        gamma_rvs = gamma_distribution.rvs(
            lam,
            loc=0.0,
            scale=theta,
            size=size,
            random_state=random_state,
        )
        normal_rvs = random_state.normal(loc=0.0, scale=1.0, size=size)
        return beta * gamma_rvs + np.sqrt(gamma_rvs) * normal_rvs

    def _stats(
        self,
        alpha: ArrayLike,
        beta: ArrayLike,
        lam: ArrayLike,
    ) -> tuple[NDArray[np.float64], NDArray[np.float64], None, None]:
        theta = 2.0 / (alpha**2 - beta**2)
        mean = beta * lam * theta
        variance = lam * theta * (1.0 + beta**2 * theta)
        return mean, variance, None, None


double_pareto = double_pareto_gen(name="double_pareto", a=-np.inf, b=np.inf)
hypsecant2 = hypsecant2_gen(name="hypsecant2", a=-np.inf, b=np.inf)
pareto_type1 = pareto_type1_gen(name="pareto_type1", a=1.0, b=np.inf)
simple_normal_mixture = simple_normal_mixture_gen(
    name="simple_normal_mixture",
    a=-np.inf,
    b=np.inf,
)
univariate_variance_gamma = univariate_variance_gamma_gen(
    name="univariate_variance_gamma",
    a=-np.inf,
    b=np.inf,
)

__all__ = [
    "generalized_pareto",
    "generalized_extreme_value",
    "frechet",
    "double_pareto",
    "double_pareto_gen",
    "hypsecant2",
    "hypsecant2_gen",
    "pareto_type1",
    "pareto_type1_gen",
    "simple_normal_mixture",
    "simple_normal_mixture_gen",
    "univariate_variance_gamma",
    "univariate_variance_gamma_gen",
]
