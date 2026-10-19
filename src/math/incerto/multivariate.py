"""Bounded chapter-6 calculations; no inference or population-moment fitting.

Student entropy helpers cover 0.5 <= nu <= 1000 and dimensions one/two.
This deliberate numerical scope avoids unsupported extreme gamma subtraction.
Parameters are real. Scatter is not covariance. Samplers never clip or
silently discard draws.
"""

from __future__ import annotations

import numpy as np
from scipy.special import gammaln, digamma


def _nu(nu):
    if np.iscomplexobj(nu):
        raise ValueError("nu must be real")
    nu = float(nu)
    if not np.isfinite(nu) or not 0.5 <= nu <= 1000:
        raise ValueError("nu must be finite and in [0.5, 1000]")
    return nu


def _rho(rho):
    if np.iscomplexobj(rho):
        raise ValueError("rho must be real")
    rho = float(rho)
    if not np.isfinite(rho) or abs(rho) >= 1:
        raise ValueError("rho must be finite and strictly between -1 and 1")
    return rho


def student_entropy(nu, dimension, logdet=0.0):
    """Differential entropy in nats, with the log determinant of scatter.

    dimension is 1 or 2; logdet must be finite. Formula includes the gamma
    normalizer and the beta-integral log-radius expectation. Arithmetic
    overflow raises; this routine does not decide existence of covariance.
    """
    nu = _nu(nu)
    if isinstance(dimension, (bool, np.bool_)) or not isinstance(dimension, (int, np.integer)) or dimension not in (1, 2):
        raise ValueError("dimension must be 1 or 2")
    if np.iscomplexobj(logdet):
        raise ValueError("logdet must be real")
    logdet = float(logdet)
    if not np.isfinite(logdet):
        raise ValueError("logdet must be finite")
    a, b = nu/2, (nu+dimension)/2
    value = (gammaln(a)-gammaln(b) + dimension/2*np.log(nu*np.pi)
             + logdet/2 + b*(digamma(b)-digamma(a)))
    if not np.isfinite(value):
        raise FloatingPointError("entropy is not representable")
    return float(value)


def student_mutual_information(nu, rho=0.0):
    """Bivariate Student mutual information in nats for unit diagonal scatter.

    0.5 <= nu <= 1000, |rho| < 1. At nu <= 2 rho is a scatter parameter,
    not Pearson correlation. No negative estimate is clipped to zero.
    """
    rho = _rho(rho)
    return (2*student_entropy(nu, 1)-student_entropy(nu, 2)
            - 0.5*np.log1p(-rho*rho))


def bivariate_student(rng, nu, rho, size):
    """Draw size pairs sharing one gamma precision per pair (unit scatter).

    rng must be a NumPy Generator. size is a positive integer. Returns
    shape (size, 2). Rejects nonfinite or zero precision, never resamples it.
    """
    nu, rho = _nu(nu), _rho(rho)
    if not isinstance(rng, np.random.Generator):
        raise ValueError("rng must be a numpy Generator")
    if isinstance(size, (bool, np.bool_)) or not isinstance(size, (int, np.integer)) or size < 1:
        raise ValueError("size must be a positive integer")
    z = rng.standard_normal((size, 2))
    z[:, 1] = rho*z[:, 0] + np.sqrt((1-rho)*(1+rho))*z[:, 1]
    precision = rng.gamma(nu/2, 2/nu, size)
    if np.any(precision <= 0) or not np.all(np.isfinite(precision)):
        raise FloatingPointError("unrepresentable sampled precision")
    with np.errstate(over="ignore", divide="ignore", invalid="ignore"):
        sample = z/np.sqrt(precision[:, None])
    if not np.all(np.isfinite(sample)):
        raise FloatingPointError("unrepresentable Student draw")
    return sample


def sample_correlation(x, y, *, centered=True):
    """Centered Pearson coefficient or uncentered cosine along the last axis.

    Equal finite 1-D or 2-D arrays, at least two observations per row.
    Constant centered rows and zero uncentered rows return NaN. Rescaling
    before centering/norms prevents avoidable overflow of squares. Final
    roundoff is bounded to [-1, 1]; no observations are removed.
    """
    if np.iscomplexobj(x) or np.iscomplexobj(y):
        raise ValueError("observations must be real")
    x, y = np.asarray(x, dtype=float), np.asarray(y, dtype=float)
    if x.shape != y.shape or x.ndim not in (1, 2) or x.size == 0 or x.shape[-1] < 2:
        raise ValueError("equal 1-D/2-D arrays with at least two observations required")
    if not isinstance(centered, (bool, np.bool_)):
        raise ValueError("centered must be boolean")
    if not np.all(np.isfinite(x)) or not np.all(np.isfinite(y)):
        raise ValueError("observations must be finite")

    def unit_rows(a):
        scale = np.max(np.abs(a), axis=-1, keepdims=True)
        # Power-of-two scaling preserves nearby floats at a large offset.
        # Subtract a reference before the mean to retain their differences.
        a = np.ldexp(a, -np.frexp(scale)[1])
        if centered:
            a = a-a[..., :1]
            a = a-np.mean(a, axis=-1, keepdims=True)
        norm = np.linalg.norm(a, axis=-1, keepdims=True)
        return np.divide(a, norm, out=np.full_like(a, np.nan), where=norm > 0)

    result = np.clip(np.sum(unit_rows(x)*unit_rows(y), axis=-1), -1, 1)
    return float(result) if result.ndim == 0 else result


def symmetric_spectrum(matrix):
    """Eigenvalues of a finite, exactly symmetric nonempty real square matrix.

    Normalizes before eigh; raises on unrepresentable eigenvalues. No
    normalization by sample size or variance is implicit in this helper.
    """
    raw = np.asarray(matrix)
    if np.iscomplexobj(raw):
        raise ValueError("matrix must be real")
    matrix = np.asarray(raw, dtype=float)
    if matrix.ndim != 2 or matrix.shape[0] != matrix.shape[1] or matrix.shape[0] == 0:
        raise ValueError("matrix must be a nonempty square array")
    if not np.all(np.isfinite(matrix)) or not np.array_equal(matrix, matrix.T):
        raise ValueError("matrix must be finite and exactly symmetric")
    scale = np.max(np.abs(matrix))
    if scale == 0:
        return np.zeros(matrix.shape[0])
    with np.errstate(over="ignore", invalid="ignore"):
        values = np.linalg.eigvalsh(matrix/scale)*scale
    if not np.all(np.isfinite(values)):
        raise FloatingPointError("eigenvalues are not representable")
    return values


def regression_population_r2(slope, error_variance):
    """Squared population correlation for independent error and Var(X)=1.

    slope finite, error_variance finite and strictly positive. Infinite
    error variance has no Pearson target and is rejected, not mapped to zero.
    """
    if np.iscomplexobj(slope) or np.iscomplexobj(error_variance):
        raise ValueError("slope and error variance must be real")
    slope, error_variance = float(slope), float(error_variance)
    if not np.isfinite(slope) or not np.isfinite(error_variance) or error_variance <= 0:
        raise ValueError("finite slope and finite positive error variance required")
    if slope == 0:
        return 0.0
    log_odds = np.log(error_variance)-2*np.log(abs(slope))
    return float(np.exp(-np.logaddexp(0, log_odds)))


def normal_location_mixture_kurtosis(separation, sigma=1.0):
    """Pearson kurtosis of X = separation*B + sigma*Z, B equally +/-1.

    separation is nonnegative, sigma positive; inputs finite. Broadcasting
    is supported. Scaled ratios avoid overflow in fourth powers.
    """
    if np.iscomplexobj(separation) or np.iscomplexobj(sigma):
        raise ValueError("separation and sigma must be real")
    m, sigma = np.broadcast_arrays(np.asarray(separation, dtype=float),
                                    np.asarray(sigma, dtype=float))
    if not np.all(np.isfinite(m)) or not np.all(np.isfinite(sigma)) or np.any(m < 0) or np.any(sigma <= 0):
        raise ValueError("finite nonnegative separation and positive sigma required")
    scale = np.maximum(m, sigma)
    fraction = (m/scale)**2 / ((m/scale)**2+(sigma/scale)**2)
    return 3-2*fraction**2
