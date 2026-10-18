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


def test_theme_overrides_host_font_weight_and_uses_bundled_serif():
    from pathlib import Path
    from matplotlib import font_manager, get_data_path
    with mpl.rc_context({'font.family': 'sans-serif', 'font.weight': 'bold',
                         'axes.labelweight': 'bold', 'axes.titleweight': 'bold'}):
        set_theme()
        fig, ax = plt.subplots()
        ax.set(xlabel='Horizon N', ylabel='Step k', title='Same mean input, different payoff')
        for label in (ax.title, ax.xaxis.label, ax.yaxis.label):
            path = Path(font_manager.findfont(label.get_fontproperties()))
            assert path == Path(get_data_path()) / 'fonts/ttf/DejaVuSerif.ttf'
            assert label.get_fontweight() == 'normal'
        plt.close(fig)


def test_svg_export_is_deterministic_and_has_no_bold_glyphs(tmp_path):
    set_theme()
    fig, ax = plt.subplots()
    ax.plot([0, 1], [0, 1], label=r'Normal $x^2$')
    ax.set_title('Same mean input, different payoff')
    ax.legend()
    a = savefig(fig, tmp_path / 'a.svg')
    b = savefig(fig, tmp_path / 'b.svg')
    assert a.read_bytes() == b.read_bytes()
    assert '<dc:date>' not in a.read_text()
    assert 'Bold' not in a.read_text()
    assert 'DejaVuSerif' in a.read_text()
    plt.close(fig)
