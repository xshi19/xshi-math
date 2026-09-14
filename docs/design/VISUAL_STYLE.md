# Incerto Wiki Visual Style

Maintainer: Xiang Shi
Last updated: 2026-05-24

This document turns the theme sentence in `DESIGN.md` into concrete visual
rules for Phase 4:

> Clean mathematical notes on good paper: readable, calm, print-aware, and
> visually restrained.

The site should feel like a careful set of mathematical lecture notes, not a
dashboard, magazine, or product landing page. Figures, tables, widgets, and
navigation are evidence and orientation. They should not compete with the
mathematics.

## 1. Global Principles

1. **Reading first.** The default page should be comfortable for long-form
   proof and explanation. Visual elements should clarify the page, not decorate
   it.
2. **Warm paper, dark ink.** Avoid pure white backgrounds and cool gray UI.
   Use warm neutrals, quiet borders, and high-contrast text.
3. **One accent, sparingly.** Ink blue is the primary accent for links,
   active navigation, and key reference marks. It should stay rare enough to
   remain meaningful.
4. **Mathematical honesty.** Plots must show scale, uncertainty, truncation,
   sample size, and model assumptions when those details affect the claim.
5. **Static first, interactive second.** Every interactive explanation should
   have a meaningful static default or fallback.
6. **Print is a first-class output.** A printed page should preserve the
   argument, figures, tables, code, citations, and captions without navigation
   clutter.

## 2. Design Tokens

These tokens are the source of truth for CSS, Matplotlib themes, tables, and
widgets.

| Token | Value | Use |
| ----- | ----- | --- |
| `paper` | `#F5F4ED` | Page background |
| `surface` | `#FAF9F5` | Figure panels, code blocks, compact widgets |
| `sand` | `#E8E6DC` | Subtle fills and plot grid lines |
| `rule` | `#D8D4C8` | Borders, dividers, table rules |
| `ink` | `#141413` | Primary text and dark plot strokes |
| `muted` | `#6B6A64` | Secondary text, ticks, inactive navigation |
| `accent` | `#1B365D` | Links, active navigation, primary plot series |
| `accent_light` | `#2D5A8A` | Hover states and secondary link emphasis |
| `green` | `#28724F` | Empirical tail quantities, positive stable signals |
| `umber` | `#8F5A2A` | Alternative model series, warnings with low severity |
| `brick` | `#9B3A34` | Caveats, high-risk thresholds, failed assumptions |
| `violet` | `#6D597A` | Additional categorical series |
| `teal` | `#2F6F73` | Additional categorical series |
| `gold` | `#A98324` | Highlight bands or finite-sample caution |

Use color as a secondary channel. Important distinctions should also use text,
line style, marker shape, facet, or ordering.

## 3. Typography

### Website

- Body font: Charter, Georgia, Palatino, serif, with CJK serif fallbacks.
- Code font: JetBrains Mono, Fira Code, SF Mono, Consolas, Monaco, monospace.
- Body size target: 17px to 18px on desktop, with line height around 1.58.
- Reading measure: roughly 68 to 78 characters for prose.
- Heading weight: medium, not heavy. Avoid synthetic bold.
- Letter spacing: normal. Do not use negative letter spacing.
- Math should inherit the calm text scale; avoid oversized display equations
  unless the equation is the page's central object.

### Figures

Matplotlib should use a serif family close to the site:

```python
font.family: serif
font.serif: Charter, Georgia, Palatino Linotype, Palatino, DejaVu Serif
mathtext.fontset: dejavuserif
```

Recommended sizes:

| Element | Size |
| ------- | ---- |
| Figure title | 12.5 pt |
| Axis label | 10.5 pt |
| Tick label | 9 pt |
| Legend text | 9 pt |
| Annotation | 9 pt |

Prefer captions and surrounding prose for interpretation. Figure titles should
name the object being shown, not try to carry the whole conclusion.

## 4. Python Figures

### Library Choice

Use native Matplotlib as the default plotting layer. It is already a project
dependency, renders reliably through MyST/Jupyter, works in static HTML and
print, and is enough for the first Phase 4 theme.

Seaborn may be used later for statistical plots if it buys real clarity, but it
should not become a required dependency only for styling. If Seaborn is added,
it must inherit the Incerto tokens through `rc` settings rather than imposing a
separate visual system.

Interactive plotting libraries should be adopted only for specific explainers.
Static Matplotlib output remains the canonical fallback.

### Theme API

Implement figure styling in `incerto/figures.py`, not in repeated notebook
cells. The expected public helpers are:

```python
from incerto.figures import set_theme, style_axes, savefig

set_theme()
```

`set_theme()` should set Matplotlib `rcParams`. `style_axes(ax)` should be safe
to call on existing axes. `savefig(fig, path)` should save with consistent DPI,
face color, and bounding box settings.

### Figure Geometry

| Use case | Size |
| -------- | ---- |
| Single concept plot | `(6.4, 3.8)` |
| Two-panel comparison | `(8.0, 3.8)` |
| Three-panel empirical diagnostic | `(10.5, 3.6)` |
| Tall explanatory plot | `(6.4, 4.6)` |

Use compact figures. A figure should fit inside the reading flow without
feeling like a slide.

Save defaults:

- `dpi=144` for notebook display.
- `dpi=200` or `300` for static exported PNGs when raster output is needed.
- SVG is preferred for simple line plots.
- PNG is acceptable for dense scatter, image-like output, or backend limits.
- Figure and axes face color: `surface`.
- Do not export with a pure white background unless required by a journal or
  external format.

### Color Cycle

Default cycle:

1. `accent` - `#1B365D`
2. `green` - `#28724F`
3. `umber` - `#8F5A2A`
4. `violet` - `#6D597A`
5. `teal` - `#2F6F73`
6. `brick` - `#9B3A34`
7. `gold` - `#A98324`
8. `muted` - `#6B6A64`

For more than six series, prefer facets, small multiples, direct labels, or
line styles over adding more colors.

### Lines, Markers, and Bands

| Element | Default |
| ------- | ------- |
| Primary line | 2.0 pt |
| Secondary line | 1.4 pt |
| Reference/asymptotic line | 1.0 pt, dashed |
| Highlight threshold | 1.2 pt, dotted or dashed |
| Marker size | 4.0 pt |
| Marker edge width | 0.7 pt |
| Confidence/uncertainty band | same hue, alpha 0.14 to 0.20 |
| Scatter alpha | 0.65 to 0.85 |

Use line style for semantics:

- Solid: observed or primary quantity.
- Dashed: model approximation or asymptotic reference.
- Dotted: threshold, cutoff, or diagnostic guide.
- Thin gray: neutral reference line.

### Axes and Grids

- Hide top and right spines by default.
- Use warm muted left and bottom spines.
- Prefer y-axis major grids only.
- Use x-axis grids only when they help read log-scale or threshold plots.
- Grid color: `sand`; grid line width: 0.8 pt.
- Tick color: `muted`; tick labels remain readable, not pale.
- Do not box every plot unless the bounded rectangle carries meaning.
- Use log scales for survival, rank-size, and tail diagnostics when appropriate.
  Label the scale clearly.
- Prefer direct labels over legends for one to three series. Use compact,
  borderless legends when direct labels would clutter the plot.

### Heavy-Tail Plot Semantics

The same visual roles should mean the same thing across pages:

- Survival or tail probability: `accent`.
- Empirical tail or sample path: `green`.
- Asymptotic reference: dashed `muted` or dashed `accent`.
- Finite-sample caution region: translucent `gold`.
- Failure zone, divergent moment, or invalid assumption: `brick`.
- Threshold parameter such as `u` or `k`: dotted `umber` or `muted`.

Whenever a figure depends on simulation, the page should state the sample size,
seed when relevant, and distribution parameters near the figure or in the code
cell.

### Captions and Annotations

Each figure should answer three questions:

1. What is being plotted?
2. Which scale and parameters are being used?
3. What should the reader notice?

Use annotations sparingly. A single well-placed label is better than a legend
plus a long caption plus repeated prose.

## 5. Tables and DataFrames

### When to Use Tables

Use tables for exact values, definitions, parameter comparisons, and compact
diagnostics. Use figures for shape, slope, instability, and trend.

### Markdown Tables

Hand-authored Markdown tables are preferred for stable conceptual material:
notation, assumptions, theorem comparisons, and reading guide maps.

Rules:

- Keep tables narrow: usually 2 to 4 columns, rarely more than 6.
- Left-align text columns.
- Right-align numeric columns when Markdown allows it.
- Do not put full paragraphs in cells. Move prose below the table when needed.
- Avoid repeated links in every row if a short page note would suffice.
- Use a table caption or lead-in sentence for anything referenced later.

### Code-Generated Tables

For generated numerical output:

- Round deliberately. Use 3 to 4 significant digits unless more precision is
  essential.
- Prefer scientific notation for tail probabilities and very large values.
- Include units, distribution parameters, and sample size in column names or
  nearby prose.
- Do not show raw DataFrame indexes unless the index is meaningful.
- Keep rows short enough for mobile. Show a compact summary and link to data or
  code for longer outputs.
- Avoid color gradients as the primary meaning. If a styled DataFrame uses
  color, the same information must be visible in numbers or labels.

If pandas becomes part of a page, prefer explicit formatting:

```python
display(
    df.style.format({
        "probability": "{:.3e}",
        "estimate": "{:.3f}",
    })
)
```

Do not rely on pandas' default HTML styling for final pages.

### Table Styling

- Background: transparent or `surface`.
- Header: `surface`, medium weight, bottom border with `rule`.
- Cell borders: horizontal rules only by default.
- Zebra striping: off by default; use very subtle `sand` striping only for
  wide scan-heavy tables.
- Numeric cells: tabular figures where CSS support allows.
- Mobile: allow horizontal scrolling rather than shrinking text into
  unreadability.
- Print: keep header rows visible and avoid breaking small tables across pages
  when possible.

## 6. Interactive Widgets

Interactivity is a teaching aid, not the default presentation mode.

### Accepted Patterns

- MyST-NB/Jupyter widgets for parameter sliders and toggles.
- Static Matplotlib or HTML fallback for print and non-executed builds.
- Compact controls above the output for simple explainers.
- Controls beside the output only when the viewport is wide enough.
- Small multiples when a slider would hide too much comparison.

### Controls

| Control | Use |
| ------- | --- |
| Slider | Numeric parameters such as alpha, threshold, sample size |
| Stepper or numeric input | Exact values that readers may want to reproduce |
| Toggle or checkbox | Binary options such as log scale or show reference line |
| Segmented control | Mutually exclusive modes with 2 to 4 choices |
| Select menu | Longer option sets such as distribution family |
| Button with icon or short label | Reset, rerun, pause, export |

Defaults should match the canonical example in the prose. Ranges should be
mathematically meaningful, not merely wide.

### Behavior

- Include a reset control when a widget has multiple stateful controls.
- Do not autoplay animations by default.
- Any animation must be pauseable.
- Avoid hidden network calls.
- Make keyboard focus visible.
- Target size should be at least 32px, preferably 36px to 40px.
- Do not put widgets in nested cards. A single quiet `surface` panel is enough.
- The print path should show the default static state and hide unusable
  controls.

### Visual Style

- Background: `surface`.
- Border: 1px solid `rule`.
- Border radius: 6px to 8px.
- Shadow: none.
- Active control: `accent`.
- Warning state: `umber` or `brick`, with text explanation.
- Labels: short, mathematical, and close to the control.

## 7. Website Chrome

### Page Layout

- Main content should be visually dominant.
- Left navigation is persistent on desktop and collapsible on mobile.
- Right table of contents is secondary and should never compete with prose.
- The content column should keep a readable measure even on wide screens.
- Page sections should feel like one document, not a stack of cards.

### Left Menu

- Organize around the durable information architecture:
  Reference, Concepts, Reading Guides, and Project Design.
- Keep section labels short.
- Use a thin accent mark or subtle background for the active page.
- Avoid icons unless they carry real navigational value.
- Do not use heavy boxes around every navigation item.
- Collapsed groups should retain enough context to show where the reader is.

### Right Table of Contents

- Show h2 and h3 headings by default.
- Avoid deep h4 nesting in the chrome.
- Use muted text for inactive entries and `accent` for the active entry.
- Keep it sticky on desktop.
- Hide it on narrow screens.

### Search

- Search should be present but visually quiet.
- Place it in the top chrome where the theme expects it.
- Use a simple label or placeholder, such as "Search".
- Results should emphasize page title, section path, and a short excerpt.
- Do not make search look like the primary action on a mathematical page.

### Links and Cross-References

- Use `accent` for links.
- Use underline or a subtle bottom border for body links when contrast alone is
  not enough.
- Keep visited links close to the same hue to avoid visual noise.
- Cross-reference badges, if added later, should be small and textual.

### Admonitions, Proofs, and Code

- Proofs and definitions should use quiet rules and typography, not bright
  colored boxes.
- Warnings and caveats may use `umber` or `brick`, but with restrained fills.
- Code blocks should use `surface`, a thin `rule` border, and the code font.
- Output blocks should be visually distinct from input code but not flashy.
- Copy buttons should be small and low-contrast until hovered or focused.

## 8. Print Rules

The print stylesheet should:

- Hide navigation, search, widget controls, and nonessential chrome.
- Preserve title, headings, equations, captions, code, tables, and references.
- Avoid page breaks inside small figures, tables, proof boxes, and code blocks.
- Use white or near-white backgrounds for ink economy.
- Preserve link URLs only when useful, such as references and external links.
- Keep figures legible in grayscale.
- Ensure color-coded claims also have labels, line styles, or captions.

Representative print checks should include:

- A distribution concept page with a plot.
- A theorem page with proof and equations.
- An empirical example with a multi-panel figure and numerical output.
- A reading guide with multiple tables.

## 9. Implementation Targets

Phase 4 should implement this document through small, reviewable pieces:

1. Expand `assets/css/incerto.css` to cover site chrome, tables, code blocks,
   admonitions, widgets, and print.
2. Implement `incerto/figures.py` with Matplotlib theme helpers.
3. Update existing content figures to call the shared helper.
4. Add table and DataFrame CSS for MyST-rendered outputs.
5. Add static fallbacks or print-safe states for existing interactive frames.
6. Verify representative pages in browser and print/PDF output.

Do not add Seaborn, Plotly, ipywidgets, or pandas as required dependencies only
for visual polish. Add them when a specific concept page needs their behavior
and the design remains consistent with this guide.
