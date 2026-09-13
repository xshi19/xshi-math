# Architecture

The repository now contains a minimal source foundation for one mathematical
site and one educational Python package. The
[consolidation plan](docs/plan/consolidation.md) owns future migration and
publication decisions; the [verification record](docs/records/phase-0-1-verification.md)
records the completed local foundation gate. The
[IG verification record](docs/records/ig-entry-verification.md) covers the first
substantive entry batch and remaining publication checks.
The [Incerto Batch 1 record](docs/records/phase-2-batch-1-verification.md) covers
the nine adapted tail notes. The
[Normix Batch 1 record](docs/records/phase-2-normix-batch-1-verification.md)
covers eight adapted theory notes. The
[Incerto Batch 2 record](docs/records/phase-2-batch-2-verification.md) covers
nine further adapted notes and the expanded 38-page local gate. The
[Incerto Batch 3 record](docs/records/phase-2-batch-3-verification.md) covers
five further body notes, three concept indexes, the 46-page HTML inspection,
and the sandbox restriction blocking the standard HTML build and browser gate.

| Surface | Current responsibility |
| --- | --- |
| `myst.yml`, `content/` | One forty-six-page book-theme site: the index, three track hubs, two original worked examples, six IG entry notes, twenty-three adapted Incerto notes and three concept indexes, and eight adapted Normix notes |
| `assets/styles/math.css` | Original typography, equation overflow, and focus styles layered over the theme |
| `package.json`, `package-lock.json` | MyST CLI 1.10.1; `npm run build` sets `BASE_URL=/math` |
| `pyproject.toml`, `uv.lock`, `.python-version` | Locked NumPy/pytest environment; Python 3.13 development default |
| `src/math/` | Source directory explicitly installed as `xmath` by setuptools; no top-level `math` package |
| `demos/`, `tests/` | A deterministic exceedance example and checks of counting, invalid input, and import isolation |
| `scripts/check_html.py` | Checks generated local routes, assets, fragments, base path, and rendered equations after HTML export |
| `docs/plan/` | Representative inventory, imported Incerto Batch 1/2/3 and Normix Batch 1 dispositions, remaining proposals, URL mappings, and pending gates |

Content uses globally unique Markdown stems flat under `content/`; the six
`information-geometry-*.md` notes are TOC children of `information-geometry.md`.
The twenty-six imported `incerto-*.md` concept pages follow the counting example beneath
`incerto.md`; their former executable cells are static calculations. The eight
Normix theory notes follow the original conditioning example beneath
`normix-theory.md`; design/tutorial sources were rewritten as mathematical notes.
No new Python helpers, plotting dependencies, or notebook execution are required.
MyST CLI 1.10.1 derives routes from these filenames and ignores `slug:`.
Repeated nested `index.md` filenames produce `index-N/` routes. MyST's host
metadata is `xshi19.github.io`; the `/math` prefix is supplied at build time as
an environment variable. The intended artifact is `_build/html/`, later assembled into `math/`
in the hub. Build outputs, environments, and installed tools are ignored by Git.
The CLI is pinned; the upstream `book-theme` alias downloads a separate theme
whose exact revision must be recorded before publication.

The dependency direction remains `xshi-math -> normix` for future package demos.
This foundation links upstream without installing or vendoring Normix. The hub
owns public assembly; no workflow here writes to it. Twenty-six Incerto concept pages and eight
Normix notes are adapted with source notices; no private history, Lean project, CI
workflow, or public math deployment was added. The
[Information Geometry outline](docs/plan/ig-entry-outline.md) separates the
implemented Basics / early IG notes from later marginalization and GH/Normix
research pages.
