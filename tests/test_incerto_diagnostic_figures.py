"""Chapter-10 figures reproduce across processes and match committed SVG bytes."""

import os
from pathlib import Path
import subprocess
import sys

import pytest


ROOT=Path(__file__).resolve().parents[1]


def test_diagnostic_exports(tmp_path):
    script=ROOT/"demos/incerto/sp500_diagnostics.py"
    for run in ("a","b"):
        code=(f"import runpy; runpy.run_path({str(script)!r})"
              f"['main']({str(tmp_path/run)!r},local_report=False)")
        env={**os.environ,"MPLBACKEND":"Agg","MPLCONFIGDIR":str(tmp_path/"mpl"),
             "OPENBLAS_NUM_THREADS":"1","OMP_NUM_THREADS":"1"}
        result=subprocess.run([sys.executable,"-c",code],env=env,cwd=tmp_path,
                              capture_output=True,text=True,timeout=90)
        assert result.returncode == 0,result.stdout+result.stderr
    for name in ("diagnostics-aggregation","diagnostics-moments-records",
                 "diagnostics-drawdown-ratio","pipeline-contamination","hinge-calibration"):
        data=(tmp_path/"a"/f"{name}.svg").read_bytes()
        assert data == (tmp_path/"b"/f"{name}.svg").read_bytes()
        assert data == (ROOT/"assets/figures/incerto"/f"{name}.svg").read_bytes()
        assert b"<dc:date>" not in data and b"Bold" not in data


@pytest.mark.parametrize("producer,names", [
    ("amazon_bookrank", ["amazon-bookrank-1"]),
    ("nyc_dog_name_tail", [f"nyc-dog-name-tail-{i}" for i in (1,2,3)]),
])
def test_relabelled_empirical_exports(tmp_path, producer, names):
    for run in ("a", "b"):
        env = {**os.environ, "MPLBACKEND": "Agg", "MPLCONFIGDIR": str(tmp_path/"mpl"),
               "OPENBLAS_NUM_THREADS": "1", "OMP_NUM_THREADS": "1",
               "INCERTO_FIGURE_DIR": str(tmp_path/run),
               "INCERTO_DATA_DIR": str(ROOT/"data/incerto")}
        result = subprocess.run([sys.executable, str(ROOT/f"demos/incerto/{producer}.py")],
                                env=env, cwd=tmp_path, capture_output=True, text=True, timeout=90)
        assert result.returncode == 0, result.stdout+result.stderr
    for name in names:
        data = (tmp_path/"a"/f"{name}.svg").read_bytes()
        assert data == (tmp_path/"b"/f"{name}.svg").read_bytes()
        assert data == (ROOT/f"assets/incerto/figures/{name}.svg").read_bytes()
        assert b"<dc:date>" not in data and b"Bold" not in data
