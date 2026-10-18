"""Figure styling helpers for Incerto examples."""

from __future__ import annotations

from collections.abc import Iterable
from math import isfinite
from pathlib import Path
from typing import Any

from cycler import cycler
from matplotlib.axes import Axes
from matplotlib.figure import Figure
import matplotlib as mpl

COLORS: dict[str, str] = {
    "paper": "#F5F4ED",
    "surface": "#FAF9F5",
    "sand": "#E8E6DC",
    "rule": "#D8D4C8",
    "ink": "#141413",
    "muted": "#6B6A64",
    "accent": "#1B365D",
    "accent_light": "#2D5A8A",
    "green": "#28724F",
    "umber": "#8F5A2A",
    "brick": "#9B3A34",
    "violet": "#6D597A",
    "teal": "#2F6F73",
    "gold": "#A98324",
}

COLOR_CYCLE: tuple[str, ...] = (
    COLORS["accent"],
    COLORS["green"],
    COLORS["umber"],
    COLORS["violet"],
    COLORS["teal"],
    COLORS["brick"],
    COLORS["gold"],
    COLORS["muted"],
)

FIGURE_SIZES: dict[str, tuple[float, float]] = {
    "single": (6.4, 3.8),
    "two_panel": (8.0, 3.8),
    "three_panel": (10.5, 3.6),
    "tall": (6.4, 4.6),
}

# Use the family shipped by the locked Matplotlib distribution. A host serif
# stack can select a different face on each machine; SVG paths bake it in.
_FONT_SERIF = ["DejaVu Serif"]
SVG_METADATA = {"Date": None, "Creator": "xshi-math Incerto"}


def set_theme(*, scale: float = 1.0) -> None:
    """Apply the Incerto Matplotlib theme.

    Parameters
    ----------
    scale:
        Multiplicative scale for text and marker sizes.  Use the default for
        ordinary concept-page figures.

    Raises
    ------
    ValueError
        If ``scale`` is not positive.
    """

    if not isfinite(scale) or scale <= 0:
        raise ValueError("scale must be positive")

    mpl.rcParams.update(
        {
            "figure.dpi": 144,
            "figure.figsize": FIGURE_SIZES["single"],
            "figure.facecolor": COLORS["surface"],
            "savefig.dpi": 200,
            "savefig.bbox": "tight",
            "savefig.facecolor": COLORS["surface"],
            "savefig.edgecolor": COLORS["surface"],
            "savefig.pad_inches": 0.08,
            "font.family": "serif",
            "font.serif": _FONT_SERIF,
            "font.size": 10 * scale,
            "font.weight": "normal",
            "font.style": "normal",
            "text.usetex": False,
            "text.hinting": "none",
            "svg.fonttype": "path",
            "svg.hashsalt": "xshi-math-incerto",
            "mathtext.default": "it",
            "mathtext.fontset": "dejavuserif",
            "axes.facecolor": COLORS["surface"],
            "axes.edgecolor": COLORS["muted"],
            "axes.labelcolor": COLORS["ink"],
            "axes.labelsize": 10.5 * scale,
            "axes.labelweight": "normal",
            "axes.linewidth": 1.0,
            "axes.prop_cycle": cycler(color=COLOR_CYCLE),
            "axes.spines.top": False,
            "axes.spines.right": False,
            "axes.titlecolor": COLORS["ink"],
            "axes.titlesize": 12.5 * scale,
            "axes.titleweight": "normal",
            "figure.titleweight": "normal",
            "figure.labelweight": "normal",
            "axes.grid": True,
            "axes.grid.axis": "y",
            "axes.axisbelow": True,
            "grid.color": COLORS["sand"],
            "grid.linewidth": 0.8,
            "grid.alpha": 1.0,
            "lines.linewidth": 2.0,
            "lines.markersize": 4.0 * scale,
            "lines.markeredgewidth": 0.7,
            "xtick.color": COLORS["muted"],
            "ytick.color": COLORS["muted"],
            "xtick.labelsize": 9 * scale,
            "ytick.labelsize": 9 * scale,
            "legend.frameon": False,
            "legend.fontsize": 9 * scale,
            "legend.handlelength": 1.8,
            "legend.borderaxespad": 0.2,
            "patch.edgecolor": COLORS["rule"],
            "patch.linewidth": 0.8,
        }
    )


def style_axes(
    axes: Axes | Iterable[Axes],
    *,
    grid_axis: str = "y",
    legend: bool = True,
) -> Axes | list[Axes]:
    """Apply final Incerto styling to one or more axes.

    Parameters
    ----------
    axes:
        A Matplotlib ``Axes`` instance or iterable of axes.
    grid_axis:
        Which major grid to show: ``"x"``, ``"y"``, ``"both"``, or ``"none"``.
    legend:
        When true, remove legend frames from existing legends.

    Returns
    -------
    matplotlib.axes.Axes or list[matplotlib.axes.Axes]
        The styled axes, matching the input shape as closely as practical.
    """

    if grid_axis not in {"x", "y", "both", "none"}:
        raise ValueError('grid_axis must be one of "x", "y", "both", or "none"')

    single_axis = isinstance(axes, Axes)
    axes_list = [axes] if single_axis else _flatten_axes(axes)

    for ax in axes_list:
        ax.set_facecolor(COLORS["surface"])
        for side in ("top", "right"):
            ax.spines[side].set_visible(False)
        for side in ("left", "bottom"):
            ax.spines[side].set_color(COLORS["muted"])
            ax.spines[side].set_linewidth(1.0)

        ax.tick_params(axis="both", colors=COLORS["muted"], length=3.0, width=0.8)
        ax.title.set_color(COLORS["ink"])
        ax.xaxis.label.set_color(COLORS["ink"])
        ax.yaxis.label.set_color(COLORS["ink"])
        ax.set_axisbelow(True)

        ax.grid(False)
        if grid_axis != "none":
            ax.grid(
                True,
                which="major",
                axis=grid_axis,
                color=COLORS["sand"],
                linewidth=0.8,
            )

        if legend:
            axis_legend = ax.get_legend()
            if axis_legend is not None:
                axis_legend.set_frame_on(False)

    return axes_list[0] if single_axis else axes_list


def _flatten_axes(axes: Iterable[Axes]) -> list[Axes]:
    axes_list: list[Axes] = []
    for item in axes:
        if isinstance(item, Axes):
            axes_list.append(item)
        elif isinstance(item, Iterable):
            axes_list.extend(_flatten_axes(item))
        else:
            raise TypeError("axes must contain Matplotlib Axes instances")
    return axes_list


def savefig(fig: Figure, path: str | Path, **kwargs: Any) -> Path:
    """Save a figure with Incerto defaults.

    Parameters
    ----------
    fig:
        Figure to save.
    path:
        Output path.
    **kwargs:
        Additional keyword arguments passed to ``Figure.savefig``.

    Returns
    -------
    pathlib.Path
        The resolved path supplied to Matplotlib.
    """

    output_path = Path(path)
    for ax in fig.axes:
        style_axes(ax)

    save_kwargs: dict[str, Any] = {
        "dpi": 200,
        "bbox_inches": "tight",
        "facecolor": COLORS["surface"],
        "edgecolor": COLORS["surface"],
        "pad_inches": 0.08,
    }
    save_kwargs.update(kwargs)
    if output_path.suffix.lower() == ".svg":
        # Suppress timestamps even when the caller adds descriptive metadata.
        save_kwargs["metadata"] = {**SVG_METADATA, **save_kwargs.get("metadata", {}), "Date": None}
    fig.savefig(output_path, **save_kwargs)
    if output_path.suffix.lower() == ".svg":
        output_path.write_text("\n".join(line.rstrip() for line in output_path.read_text().splitlines()) + "\n")
    return output_path


__all__ = [
    "COLORS",
    "COLOR_CYCLE",
    "FIGURE_SIZES",
    "SVG_METADATA",
    "savefig",
    "set_theme",
    "style_axes",
]
