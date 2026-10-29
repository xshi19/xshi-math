"""Independent integrals, exact sampling checks, ties and reproducible SVGs."""
from decimal import Decimal, localcontext
import os
from pathlib import Path
import subprocess
import sys

import numpy as np
from numpy.testing import assert_allclose
import pytest
from scipy.integrate import quad
from scipy.stats import gamma, norm, pareto

from xmath.incerto.estimators import hill_estimator, hill_stability
from xmath.incerto.extremes import (
    expected_gaussian_hidden_mean, expected_pareto_hidden_fraction,
    gaussian_maximum_cdf, gaussian_maximum_norming, maximum_missing_mass,
    pareto_exponent_sampling, pareto_hidden_moment,
)

ROOT = Path(__file__).resolve().parents[1]


@pytest.mark.parametrize('alpha,p,t', [(1.2, 0, 3), (1.2, 1, 3), (3, 2, 4), (2.5, .7, 2)])
def test_hidden_moment_against_direct_density_integral(alpha, p, t):
    law = pareto(alpha, scale=2)
    integral = quad(lambda x: x**p*law.pdf(x), t, np.inf, epsabs=1e-9)[0]
    assert pareto_hidden_moment(t, alpha, p=p, x_m=2) == pytest.approx(integral, rel=1e-8)
    assert pareto_hidden_moment(3*t, alpha, p=p, x_m=6) == pytest.approx(3**p*integral, rel=1e-8)


@pytest.mark.parametrize('n', [1, 2, 10, 1000])
@pytest.mark.parametrize('alpha,p', [(1.1, 1), (1.5, 1), (3, 2), (1.2, 0)])
def test_expected_fraction_against_maximum_quantile_integral(n, alpha, p):
    # Integrate using F(M_n)=V**(1/n), with V uniform, instead of Beta moments.
    power = 1-p/alpha
    integral = quad(lambda v: (-np.expm1(np.log(v)/n))**power, 0, 1,
                    epsabs=1e-11)[0]
    assert expected_pareto_hidden_fraction(n, alpha, p=p) == pytest.approx(integral, rel=2e-8)


def test_missing_mass_exact_and_scaled_limit():
    for n in (1, 10, 100, 10**9):
        law = maximum_missing_mass(n)
        assert law.mean() == pytest.approx(1/(n+1))
        assert law.sf(.25) == pytest.approx(.75**n)
        assert law.cdf(law.ppf(.95)) == pytest.approx(.95)
    assert maximum_missing_mass(100000).sf(2/100000) == pytest.approx(np.exp(-2), rel=3e-5)


@pytest.mark.parametrize('m', [1, 2, 5, 30])
@pytest.mark.parametrize('alpha', [.8, 1.5, 3])
def test_exponent_cdf_against_gamma_pivot(m, alpha):
    law = pareto_exponent_sampling(alpha, m)
    grid = np.array([.5, 1, 2, 5])
    assert_allclose(law.cdf(grid), gamma(m, scale=1/alpha).sf(m/grid), rtol=1e-12)
    if m > 1:
        corrected = pareto_exponent_sampling(alpha, m, debiased=True)
        assert corrected.mean() == pytest.approx(alpha)
        assert_allclose(corrected.cdf(grid), law.cdf(grid*m/(m-1)))
    if m > 2:
        assert law.var() == pytest.approx(m*m*alpha*alpha/((m-1)**2*(m-2)))


def test_fixed_k_hill_simulation_checks_distribution_not_one_draw():
    rng = np.random.default_rng(192711)
    estimates = np.array([1/hill_estimator(x, 12)
                          for x in np.exp(rng.exponential(1/1.7, (6000, 80)))])
    law = pareto_exponent_sampling(1.7, 12)
    for p in (.1, .5, .9):
        # A fixed, generous 6-standard-error binomial tolerance.
        observed = np.mean(estimates <= law.ppf(p))
        assert abs(observed-p) < 6*np.sqrt(p*(1-p)/len(estimates))


@pytest.mark.parametrize('scale', [1e-200, 1, 10, 1e200])
def test_hill_ties_and_rescaling(scale):
    x = scale*np.array([1, 1, 2, 2, 4, 8])
    curve = hill_stability(x, [1, 2, 4, 5])
    exact = [np.log(2), 1.5*np.log(2), 1.75*np.log(2), 1.4*np.log(2)]
    assert_allclose(curve['xi'], exact, rtol=1e-13)
    assert_allclose(curve['xi'], [hill_estimator(x, k) for k in (1, 2, 4, 5)], rtol=1e-14)
    constant = hill_stability(np.full(20, scale), [1, 18, 19])
    assert_allclose(constant['xi'], 0, atol=0)
    assert np.all(np.isposinf(constant['alpha']))


def test_hill_near_ties_and_full_float_range():
    for origin in (1.0, 1e200):
        x = np.array([origin, np.nextafter(origin, np.inf), np.nextafter(np.nextafter(origin, np.inf), np.inf)])
        with localcontext() as ctx:
            ctx.prec = 70
            d = [Decimal.from_float(float(v)) for v in x]
            expected = float(((d[1]/d[0]).ln()+(d[2]/d[0]).ln())/2)
        assert hill_estimator(x, 2) == pytest.approx(expected, rel=1e-14)
        assert hill_stability(x, [2])['xi'][0] == pytest.approx(expected, rel=1e-14)
    x = [np.nextafter(0., 1.), 1., np.finfo(float).max]
    assert np.isfinite(hill_estimator(x, 2))
    assert hill_stability(x, [1, 2])['xi'].min() > 0


@pytest.mark.parametrize('n', [3, 10, 1000, 10**9])
def test_normal_norming_and_exact_cdf(n):
    a, b = gaussian_maximum_norming(n)
    assert a > 0 and b > 0
    assert norm.sf(b) == pytest.approx(1/n, rel=2e-13)
    assert a*norm.pdf(b) == pytest.approx(1/n, rel=2e-13)
    assert gaussian_maximum_cdf(b, n) == pytest.approx(np.exp(n*np.log1p(-1/n)))
    assert_allclose(gaussian_maximum_cdf([-np.inf, 0, np.inf], n), [0, 2.**(-n), 1])
    for method in ('mills', 'asymptotic'):
        a, b = gaussian_maximum_norming(n, method=method)
        assert a > 0 and np.isfinite(b)


@pytest.mark.parametrize('n', [1, 2, 10, 100, 10000])
def test_gaussian_hidden_mean_against_density_integral(n):
    direct = quad(lambda t: n*norm.pdf(t)**2*norm.cdf(t)**(n-1),
                  -np.inf, np.inf, epsabs=1e-12)[0]
    result = expected_gaussian_hidden_mean(n)
    assert result['value'] == pytest.approx(direct, rel=1e-8)
    assert 0 <= result['abs_error'] < 1e-9
    if n == 1:
        assert result['value'] == pytest.approx(1/(2*np.sqrt(np.pi)))


def test_explicit_nonfinite_results_and_numerical_overflow():
    assert np.isinf(pareto_hidden_moment([1, 100], 1)).all()
    assert np.isnan(expected_pareto_hidden_fraction(100, 1))
    assert np.isinf(pareto_exponent_sampling(1, 1).mean())
    assert np.isinf(pareto_exponent_sampling(1, 2).var())
    with pytest.raises(FloatingPointError):
        pareto_exponent_sampling(1e308, 10)
    with pytest.raises(FloatingPointError):
        pareto_hidden_moment(1e200, 4, x_m=1e200, p=2)


@pytest.mark.parametrize('alpha', [1e16, 1e308])
@pytest.mark.parametrize('x_m', [2., 64.])
def test_hidden_moment_retains_prefactor_when_powers_cancel(alpha, x_m):
    # At t=x_m**2 and p=alpha/2, the two powers cancel exactly; alpha/(alpha-p)=2.
    assert pareto_hidden_moment(x_m**2, alpha, x_m=x_m, p=alpha/2) == pytest.approx(2)


def test_hidden_probability_allows_underflow_of_log_power():
    # The probability 10**(-1e308) rounds to zero; it is not moment overflow.
    assert pareto_hidden_moment(10, 1e308, p=0) == 0
    with pytest.raises(FloatingPointError):
        pareto_hidden_moment(1e200, 1e308, x_m=1e200, p=5e307)


@pytest.mark.parametrize('bad', [True, 0, -1, 1.5, 10**9+1, np.inf, np.nan])
def test_bad_counts(bad):
    for function in (maximum_missing_mass, expected_gaussian_hidden_mean,
                     lambda n: gaussian_maximum_cdf(0, n),
                     lambda n: expected_pareto_hidden_fraction(n, 1.5),
                     lambda n: pareto_exponent_sampling(1.5, n)):
        with pytest.raises(ValueError):
            function(bad)


@pytest.mark.parametrize('bad', [0, -1, np.inf, np.nan, [1, 2]])
def test_bad_parameters(bad):
    for function in (lambda a: pareto_hidden_moment(10, a),
                     lambda a: expected_pareto_hidden_fraction(10, a),
                     lambda a: pareto_exponent_sampling(a, 10)):
        with pytest.raises(ValueError):
            function(bad)


def test_other_domain_errors():
    calls = [lambda: pareto_hidden_moment(.5, 2), lambda: pareto_hidden_moment(np.inf, 2),
             lambda: pareto_hidden_moment(2, 2, p=-1), lambda: pareto_hidden_moment(2, 2, x_m=0),
             lambda: expected_pareto_hidden_fraction(3, 2, p=np.nan),
             lambda: pareto_exponent_sampling(2, 1, debiased=True),
             lambda: pareto_exponent_sampling(2, 2, debiased='yes'),
             lambda: gaussian_maximum_norming(2), lambda: gaussian_maximum_norming(10, method='other'),
             lambda: gaussian_maximum_cdf(np.nan, 10)]
    for call in calls:
        with pytest.raises(ValueError):
            call()


def test_extreme_value_figures_reproduce(tmp_path):
    script = ROOT/'demos/incerto/extreme_values.py'
    for run in ('a', 'b'):
        out = tmp_path/run
        code = f"import runpy; runpy.run_path({str(script)!r})['main']({str(out)!r})"
        result = subprocess.run([sys.executable, '-c', code], cwd=tmp_path,
            env={**os.environ, 'MPLBACKEND': 'Agg', 'MPLCONFIGDIR': str(tmp_path/'mpl'),
                 'OPENBLAS_NUM_THREADS': '1', 'OMP_NUM_THREADS': '1'},
            capture_output=True, text=True, timeout=90)
        assert result.returncode == 0, result.stdout+result.stderr
    for name in ('gaussian-maxima', 'hidden-tail-pareto', 'hidden-tail-normal', 'hill-sampling-law'):
        first = (tmp_path/'a'/f'{name}.svg').read_bytes()
        assert first == (tmp_path/'b'/f'{name}.svg').read_bytes()
        assert first == (ROOT/'assets/figures/incerto'/f'{name}.svg').read_bytes()
        assert b'<dc:date>' not in first
