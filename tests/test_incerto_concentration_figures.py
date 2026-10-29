"""Chapter-8 exports reproduce in independent processes and match the assets."""

import os
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]


def test_concentration_exports(tmp_path):
    script = ROOT / "demos/incerto/concentration.py"
    for run in ("a", "b"):
        code = f"import runpy; runpy.run_path({str(script)!r})['main']({str(tmp_path/run)!r})"
        env = {**os.environ, "MPLBACKEND": "Agg", "MPLCONFIGDIR": str(tmp_path/"mpl"),
               "OPENBLAS_NUM_THREADS": "1", "OMP_NUM_THREADS": "1"}
        result = subprocess.run([sys.executable, "-c", code], env=env, cwd=tmp_path,
                                capture_output=True, text=True, timeout=90)
        assert result.returncode == 0, result.stdout + result.stderr
    for name in ("kappa-aggregation", "kappa-sample-size", "kappa-lognormal", "kappa-shape"):
        data = (tmp_path/"a"/f"{name}.svg").read_bytes()
        assert data == (tmp_path/"b"/f"{name}.svg").read_bytes()
        assert data == (ROOT/"assets/figures/incerto"/f"{name}.svg").read_bytes()
        assert b"<dc:date>" not in data and b"Bold" not in data
