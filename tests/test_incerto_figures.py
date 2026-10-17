"""Tests for Incerto figure styling helpers."""

import matplotlib

matplotlib.use("Agg")

import matplotlib as mpl
import matplotlib.pyplot as plt
import pytest

from xmath.incerto.figures import COLORS, COLOR_CYCLE, savefig, set_theme, style_axes


def test_set_theme_updates_matplotlib_defaults() -> None:
    set_theme()

    assert mpl.rcParams["figure.facecolor"] == COLORS["surface"]
    assert mpl.rcParams["axes.facecolor"] == COLORS["surface"]
    assert list(mpl.rcParams["axes.prop_cycle"].by_key()["color"]) == list(COLOR_CYCLE)
    assert mpl.rcParams["axes.spines.top"] is False
    assert mpl.rcParams["axes.spines.right"] is False


def test_set_theme_rejects_nonpositive_scale() -> None:
    with pytest.raises(ValueError):
        set_theme(scale=0)


def test_style_axes_hides_extra_spines_and_styles_legend() -> None:
    set_theme()
    fig, ax = plt.subplots()
    ax.plot([1.0, 2.0], [3.0, 4.0], label="sample")
    ax.legend()

    returned = style_axes(ax, grid_axis="both")

    assert returned is ax
    assert not ax.spines["top"].get_visible()
    assert not ax.spines["right"].get_visible()
    assert ax.get_legend() is not None
    assert not ax.get_legend().get_frame_on()
    plt.close(fig)


def test_style_axes_accepts_nested_axes() -> None:
    fig, axes = plt.subplots(2, 2)

    styled = style_axes(axes)

    assert len(styled) == 4
    assert all(not ax.spines["top"].get_visible() for ax in styled)
    plt.close(fig)


def test_style_axes_rejects_unknown_grid_axis() -> None:
    fig, ax = plt.subplots()

    with pytest.raises(ValueError):
        style_axes(ax, grid_axis="diagonal")

    plt.close(fig)


def test_savefig_writes_file(tmp_path) -> None:
    set_theme()
    fig, ax = plt.subplots()
    ax.plot([1.0, 2.0], [1.0, 4.0])

    output = savefig(fig, tmp_path / "figure.png")

    assert output.exists()
    assert output.stat().st_size > 0
    plt.close(fig)
