"""Fresh-process byte reproducibility of the four chapter-13 SVGs."""

import os
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
NAMES = ('conflation-payoff-gap', 'conflation-probability-error',
         'risk-exponent-uncertainty', 'risk-estimation')


def test_probability_conflation_exports(tmp_path):
    for run in ('a', 'b'):
        env = {**os.environ, 'MPLBACKEND': 'Agg', 'MPLCONFIGDIR': str(tmp_path/'mpl'),
               'OPENBLAS_NUM_THREADS': '1', 'OMP_NUM_THREADS': '1'}
        result = subprocess.run(
            [sys.executable, str(ROOT/'demos/incerto/probability_conflation.py'),
             '--output', str(tmp_path/run)], cwd=tmp_path, env=env,
            capture_output=True, text=True, timeout=60)
        assert result.returncode == 0, result.stdout + result.stderr
        assert 'all 1,000,000 draws retained' in result.stdout
    for name in NAMES:
        data = (tmp_path/'a'/f'{name}.svg').read_bytes()
        assert data == (tmp_path/'b'/f'{name}.svg').read_bytes()
        assert data == (ROOT/'assets/figures/incerto'/f'{name}.svg').read_bytes()
        assert b'<dc:date>' not in data and b'Bold' not in data
