# xshi-math

Mathematical notes and tutorials, supported by small Python demonstrations and
optional future Lean formalization.

The foundation has three tracks:

- **Incerto / fat tails:** an original finite-sample exceedance example and
  twenty-three adapted notes on Pareto tails, moments, estimation, extreme-value
  and stable limits, and diagnostics, plus three concept indexes.
- **Information Geometry:** six original entry notes on manifolds, exponential
  families, EM, conditional expectation, Fisher geometry, and duality.
- **Normix theory:** an original conditioning example and eight adapted notes
  on GIG/GH distributions, mixtures, exponential families, and EM, linked to the
  independently maintained [normix package](https://github.com/xshi19/normix).

The [hub](https://github.com/xshi19/xshi19.github.io) owns assembly and publication
at `https://xshi19.github.io/math/`. Normix's implementation, public API, releases,
and API documentation stay upstream. No math site has been deployed by this change.

**Status:** Phase 0 light inventory and the Phase 1 local HTML gate are complete.
Foundation Python checks and earlier pinned site builds passed under `/math/`.
The [IG outline](docs/plan/ig-entry-outline.md), first IG entry batch,
[Incerto Batch 1](docs/plan/phase-2-incerto-batch-1.md),
[Incerto Batch 2](docs/plan/phase-2-incerto-batch-2.md),
[Incerto Batch 3](docs/plan/phase-2-incerto-batch-3.md), and
[Normix Theory Batch 1](docs/plan/phase-2-normix-theory-batch-1.md) are implemented.
See the [foundation record](docs/records/phase-0-1-verification.md),
[IG verification record](docs/records/ig-entry-verification.md),
[Incerto Batch 1 record](docs/records/phase-2-batch-1-verification.md),
[Incerto Batch 2 record](docs/records/phase-2-batch-2-verification.md),
[Incerto Batch 3 record](docs/records/phase-2-batch-3-verification.md), and
[Normix verification record](docs/records/phase-2-normix-batch-1-verification.md)
for results and remaining publication checks. Twenty-six Incerto concept pages and eight Normix
notes have been imported; no private history was imported and no CI is
configured. Further imports remain planned.

## Install and run Python

Use Python 3.13 (the `.python-version` development default) and `uv`. Package
metadata supports Python >=3.12; only Python 3.13.5 was tested here.

```sh
uv sync --locked
uv run pytest
uv run python demos/incerto/exceedances.py
```

The distribution is named `xshi-math`, but the import is `xmath`. Setuptools maps
it explicitly to `src/math/`; do not add `src/` to `PYTHONPATH`. Both editable and
wheel installations were checked alongside stdlib `math` and NumPy.

```python
from xmath import exceedance_fraction

assert exceedance_fraction([1, 2, 2, 4], 2) == 0.25
```

To check the ordinary wheel installation in a separate environment:

```sh
uv build
UV_PROJECT_ENVIRONMENT=.venv-wheel uv sync --locked --no-editable
.venv-wheel/bin/python -I -c 'import math, xmath; print(math.sqrt(9), xmath.__file__)'
```

## Build the site

Use Node.js >=20 and npm >=8.6. MyST CLI 1.10.1 is pinned in the npm manifest and
lock. The book-theme alias downloads a separate theme on its first build, so a
fresh build needs network access. The npm scripts below use POSIX shell syntax.

```sh
npm ci
npm run build
npm run check:html
```

The exact configured MyST command is:

```sh
BASE_URL=/math ./node_modules/.bin/myst build --html --strict --ci
```

MyST takes the path prefix from `BASE_URL`; `site.domains` contains the host
without a path. This follows the [MyST base URL documentation](https://mystmd.org/guide/deployment).
The Batch 3 sandbox blocks the localhost servers required by `npm run build`.
The 46-page checker passes on a separate export using the cached theme renderer;
the standard build and browser gate still need a runner that permits localhost.
See the [Batch 3 record](docs/records/phase-2-batch-3-verification.md).

HTML should be written to `_build/html/`, ready for later assembly into the hub's
`math/` directory. `check:html` checks the forty-six expected pages, local
links/assets/fragments, prefix, shared CSS, and rendered equations, including
KaTeX error markers. It is not a browser review.
Build and browser inspection results and limits are recorded separately.

For interactive local authoring, use `npm start`. To inspect the exported site
under the real base path, stage it beneath `math/` rather than serving its files
at the host root:

```sh
mkdir -p _build/preview/math
cp -R _build/html/. _build/preview/math/
python3 -m http.server 8000 --directory _build/preview
```

Then open `http://localhost:8000/math/`. Review equations, navigation, and narrow
screens when changing pages or the theme. Publishing into the hub and legacy
route redirects belong to later phases.

## Repository map

| Document | Purpose |
| --- | --- |
| [Architecture](ARCHITECTURE.md) | What the scaffold contains and its dependency boundaries |
| [Planning index](docs/plan/index.md) | Phase status and remaining decisions |
| [Light inventory](docs/plan/phase-0-inventory.md) | Source revisions, representative dispositions, routes, and publisher findings |
| [Consolidation plan](docs/plan/consolidation.md) | Future import, assembly, and cutover gates |
| [Agent router](AGENTS.md) | Task routes and verification entry points |
| [Agent framework](docs/design/AGENT_FRAMEWORK.md) | Guidance ownership and optional future rules/skills |

Repository-owned code, prose, figures, notebooks, Lean, and guidance use the root
[MIT license](LICENSE). Identify third-party exceptions when introducing them;
the [import notices](THIRD_PARTY_NOTICES.md) retain the Incerto and Normix copyright and MIT
permission text, also carried on each adapted page. See the
[license advice](docs/design/LICENSE_ADVICE.md) for the adopted Incerto decision.
