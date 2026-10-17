"""Smoke tests for the installed xmath.incerto modules."""

import importlib


def test_incerto_package_imports() -> None:
    """The installed package exposes the imported modules."""
    for module_name in (
        "xmath.incerto",
        "xmath.incerto.datasets",
        "xmath.incerto.distributions",
        "xmath.incerto.estimators",
        "xmath.incerto.figures",
        "xmath.incerto.stats",
        "xmath.incerto.tail_diagnostics",
    ):
        assert importlib.import_module(module_name)
