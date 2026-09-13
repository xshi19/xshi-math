# Architecture

The repository now contains a minimal source foundation for one mathematical
site and one educational Python package. The
[consolidation plan](docs/plan/consolidation.md) owns future migration and
publication decisions; the [verification record](docs/records/phase-0-1-verification.md)
distinguishes executed checks from the remaining HTML build gate.

| Surface | Current responsibility |
| --- | --- |
| `myst.yml`, `content/` | One book-theme site with an explicit TOC, three track entries, and two original worked examples |
| `assets/styles/math.css` | Original typography, equation overflow, and focus styles layered over the theme |
| `package.json`, `package-lock.json` | MyST CLI 1.10.1; `npm run build` sets `BASE_URL=/math` |
| `pyproject.toml`, `uv.lock`, `.python-version` | Locked NumPy/pytest environment; Python 3.13 development default |
| `src/math/` | Source directory explicitly installed as `xmath` by setuptools; no top-level `math` package |
| `demos/`, `tests/` | A deterministic exceedance example and checks of counting, invalid input, and import isolation |
| `scripts/check_html.py` | Checks generated local routes, assets, base path, and sample equations after HTML export |
| `docs/plan/` | Representative inventory, proposed migration dispositions, URL candidates, and pending gates |

Page slugs are explicit and globally unique. MyST's host metadata is
`xshi19.github.io`; the `/math` prefix is supplied at build time as an environment
variable. The intended artifact is `_build/html/`, later assembled into `math/`
in the hub. Build outputs, environments, and installed tools are ignored by Git.
The CLI is pinned; the upstream `book-theme` alias downloads a separate theme
whose exact revision must be recorded before publication.

The dependency direction remains `xshi-math -> normix` for future package demos.
This foundation links upstream without installing or vendoring Normix. The hub
owns public assembly; no workflow here writes to it. There is no imported wiki
body, Lean project, CI workflow, or public math deployment. The Information
Geometry entry remains a placeholder pending the owner's concept list.
