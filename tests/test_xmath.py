"""Check the counting convention and the unusual package-directory mapping."""

import math
from pathlib import Path

import numpy as np
import pytest

import xmath


def test_exceedances_and_imports():
    # Only 4 exceeds 2: values equal to the threshold must not be counted.
    assert xmath.exceedance_fraction([1, 2, 2, 4], 2) == 0.25
    assert xmath.exceedance_fraction([1, 2, 2, 4], 0) == 1.0
    assert xmath.exceedance_fraction([1, 2, 2, 4], 4) == 0.0
    assert math.sqrt(9) == 3
    origin = math.__spec__.origin
    assert origin == "built-in" or not Path(origin).resolve().is_relative_to(
        Path(__file__).resolve().parents[1] / "src"
    )
    assert np.sqrt(9) == 3


@pytest.mark.parametrize("samples", [[], [[1, 2]], [float("nan")], [float("inf")]])
def test_invalid_samples(samples):
    with pytest.raises(ValueError):
        xmath.exceedance_fraction(samples, 2)


def test_invalid_threshold():
    with pytest.raises(ValueError):
        xmath.exceedance_fraction([1, 2], float("nan"))
