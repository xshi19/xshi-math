"""Fresh-process, checked-in SVG byte reproducibility for chapter 14."""

import os
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
NAMES = ("forecast-uncertainty", "forecast-dual-paths", "forecast-revision-budget")


def test_forecast_martingale_exports(tmp_path):
    for run in ("a", "b"):
        env = {**os.environ, "MPLBACKEND": "Agg", "MPLCONFIGDIR": str(tmp_path/"mpl"),
               "OPENBLAS_NUM_THREADS": "1", "OMP_NUM_THREADS": "1"}
        result = subprocess.run(
            [sys.executable, str(ROOT/"demos/incerto/forecast_martingales.py"),
             "--output", str(tmp_path/run)], cwd=tmp_path, env=env,
            capture_output=True, text=True, timeout=60)
        assert result.returncode == 0, result.stdout + result.stderr
        assert "400400 normal draws, all paths retained" in result.stdout
    for name in NAMES:
        data = (tmp_path/"a"/f"{name}.svg").read_bytes()
        assert data == (tmp_path/"b"/f"{name}.svg").read_bytes()
        assert data == (ROOT/"assets/figures/incerto"/f"{name}.svg").read_bytes()
        assert b"<dc:date>" not in data and b"Bold" not in data
