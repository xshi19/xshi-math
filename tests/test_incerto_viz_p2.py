"""P2 finite identities and fresh-process SVG reproducibility."""

from pathlib import Path
import os
import subprocess
import sys

import numpy as np
from numpy.testing import assert_allclose
import pytest
from scipy.stats import expon

from xmath import exceedance_fraction
from xmath.incerto.distributions import pareto_type1
from xmath.incerto.limits import repeated_centered_sums
from xmath.incerto.stats import empirical_survival_function
from xmath.incerto.tail_diagnostics import iid_two_sum_tail

ROOT = Path(__file__).resolve().parents[1]


def test_tied_survival_complement_including_endpoints():
    sample = [1, 2, 2, 4]
    support, survival = empirical_survival_function(sample)
    assert_allclose(support, [1, 2, 4])
    assert_allclose(survival, [.75, .25, 0])
    assert_allclose(1-survival, [.25, .75, 1])
    assert_allclose(survival, [exceedance_fraction(sample, t) for t in support])


def test_same_centered_sums_have_exact_spread_ratio():
    n = np.array([10, 100, 1000])
    sums = repeated_centered_sums(pareto_type1(1.5), n, center=3,
                                  repetitions=100, random_state=2)
    stable_iqr = np.diff(np.quantile(sums/n[:, None]**(2/3), [.25, .75], axis=1), axis=0)[0]
    sqrt_iqr = np.diff(np.quantile(sums/np.sqrt(n[:, None]), [.25, .75], axis=1), axis=0)[0]
    assert_allclose(sqrt_iqr/stable_iqr, n**(1/6))


def test_exponential_convolution_is_not_subexponential():
    u = np.array([3, 10, 1000])
    result = iid_two_sum_tail(expon(), u, rtol=1e-9, maxlevel=12)
    assert result["success"].all()
    assert_allclose(result["ratio"], (1+u)/2, rtol=1e-9)


@pytest.mark.parametrize("producer,names", [
    ("limit_distributions", ["cauchy-running", "lln-failure-paths", "lln-capped-means",
                             "generalized-clt", "ergodicity-growth"]),
    ("visualization_p2", ["subexponential-geometry", "subexponential-convolution",
                          "plugin-mean-singularity", "exceedances-ties"]),
    ("rayleigh_speed", ["rayleigh-speed-fits", "rayleigh-speed-qq", "rayleigh-speed-qq-tail"]),
])
def test_p2_exports_match_two_fresh_runs_and_committed_assets(producer, names, tmp_path):
    script = ROOT/f"demos/incerto/{producer}.py"
    for run in ("a", "b"):
        code = f"import runpy; runpy.run_path({str(script)!r})['main']({str(tmp_path/run)!r})"
        env = {**os.environ, "MPLBACKEND": "Agg", "MPLCONFIGDIR": str(tmp_path/"mpl"),
               "OPENBLAS_NUM_THREADS": "1", "OMP_NUM_THREADS": "1"}
        result = subprocess.run([sys.executable, "-c", code], env=env, cwd=tmp_path,
                                capture_output=True, text=True, timeout=90)
        assert result.returncode == 0, result.stdout+result.stderr
    for name in names:
        data = (tmp_path/"a"/f"{name}.svg").read_bytes()
        assert data == (tmp_path/"b"/f"{name}.svg").read_bytes(), name
        assert data == (ROOT/f"assets/figures/incerto/{name}.svg").read_bytes(), name
        assert b"<dc:date>" not in data and b"Bold" not in data
