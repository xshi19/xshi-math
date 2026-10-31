"""Independent-process chapter-11 exports match repository bytes."""

import os
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]


def test_calibration_exports(tmp_path):
    for run in ("a", "b"):
        env = {**os.environ, "MPLBACKEND": "Agg", "MPLCONFIGDIR": str(tmp_path/"mpl"),
               "OPENBLAS_NUM_THREADS": "1", "OMP_NUM_THREADS": "1"}
        result = subprocess.run(
            [sys.executable, str(ROOT/"demos/incerto/calibration_payoffs.py"),
             "--output", str(tmp_path/run)], env=env, cwd=tmp_path,
            capture_output=True, text=True, timeout=60,
        )
        assert result.returncode == 0, result.stdout+result.stderr
    for name in ("calibration-tail-payoffs", "calibration-curves",
                 "calibration-score-laws", "point-forecast-losses"):
        data = (tmp_path/"a"/f"{name}.svg").read_bytes()
        assert data == (tmp_path/"b"/f"{name}.svg").read_bytes()
        assert data == (ROOT/"assets/figures/incerto"/f"{name}.svg").read_bytes()
        assert b"<dc:date>" not in data and b"Bold" not in data
