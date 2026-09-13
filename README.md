# xshi-math

Mathematical notes and tutorials, supported by small Python demonstrations and
optional future Lean formalization.

The foundation has three tracks:

- **Incerto / fat tails:** an original finite-sample exceedance example and
  twenty-three adapted notes on Pareto tails, moments, estimation, extreme-value
  and stable limits, and diagnostics, plus three concept indexes.
- **Information Geometry:** six original entry notes on manifolds, exponential
  families, EM, conditional expectation, Fisher geometry, and duality.
- **Normix theory:** an original conditioning example and thirteen adapted notes
  on GIG/GH distributions, mixtures, exponential families, EM, factor analysis,
  shrinkage, and information quantities, linked to the
  independently maintained [normix package](https://github.com/xshi19/normix).

Shared mathematical symbols live in one canon at
`https://xshi19.github.io/math/notation/` (`content/notation.md`). New notes must
reuse those symbols rather than inventing parallel names for the same concept.

The [hub](https://github.com/xshi19/xshi19.github.io) owns assembly and publication
at `https://xshi19.github.io/math/`. Normix's implementation, public API, releases,
and API documentation stay upstream. No math site has been deployed by this change.

**Status:** Phase 0 light inventory and the Phase 1 local HTML gate are complete.
Foundation Python checks and earlier pinned site builds passed under `/math/`.
The [IG outline](docs/plan/ig-entry-outline.md), first IG entry batch,
[Incerto Batch 1](docs/plan/phase-2-incerto-batch-1.md),
[Incerto Batch 2](docs/plan/phase-2-incerto-batch-2.md),
[Incerto Batch 3](docs/plan/phase-2-incerto-batch-3.md),
[Normix Theory Batches 1](docs/plan/phase-2-normix-theory-batch-1.md) and
[2](docs/plan/phase-2-normix-theory-batch-2.md) are implemented.
See the [foundation record](docs/records/phase-0-1-verification.md),
[IG verification record](docs/records/ig-entry-verification.md),
[Incerto Batch 1 record](docs/records/phase-2-batch-1-verification.md),
[Incerto Batch 2 record](docs/records/phase-2-batch-2-verification.md),
[Incerto Batch 3 record](docs/records/phase-2-batch-3-verification.md),
[Normix Batch 1 record](docs/records/phase-2-normix-batch-1-verification.md), and
[Normix Batch 2 record](docs/records/phase-2-normix-batch-2-verification.md)
for results and remaining publication checks. The [subsite split](docs/records/subsite-split-verification.md)
replaces the combined book with a landing and three independent sites. Twenty-six Incerto concept pages and thirteen Normix
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

## Build the sites

Use Node.js >=20, npm >=8.6, and Python 3. MyST CLI 1.10.1 is pinned in the npm
manifest and lock. The book-theme alias downloads a separate theme on its first
build; DOI citation lookup can also need network access.

```sh
npm ci
npm run build
npm run check:html
```

The build runs these four independent MyST projects sequentially:

| Config | Home source | Public base | Pages |
| --- | --- | --- | --- |
| `myst.landing.yml` | `content/index.md` | `/math/` | 1 |
| `myst.incerto.yml` | `content/incerto/index.md` | `/math/incerto/` | 28 |
| `myst.ig.yml` | `content/ig/index.md` | `/math/ig/` | 7 |
| `myst.normix-theory.yml` | `content/normix-theory/index.md` | `/math/normix-theory/` | 15 |

For example, the Incerto command is:

```sh
BASE_URL=/math/incerto ./node_modules/.bin/myst --config myst.incerto.yml build --html --strict --ci
```

MyST takes the path prefix from `BASE_URL`; `site.domains` contains the host
without a path. See the [MyST base URL documentation](https://mystmd.org/guide/deployment).
Each project has its own title, logo text, TOC, search data, and assets. The
landing hides book navigation and only links the three tracks and separate
Normix package docs. `myst.yml` extends the landing config for default authoring.

`scripts/build_sites.py` clears intermediate project state between builds,
retains the downloaded theme and DOI cache, and saves each export in
`_build/subsites/{landing,incerto,ig,normix-theory}/`. It then copies the landing
to `_build/html/` and the tracks beneath `incerto/`, `ig/`, and `normix-theory/`.
Finally, `scripts/write_redirects.py` adds 48 compatibility pages for old flat
math URLs. Assembly also replaces localhost sitemap/discovery URLs with the
public nested URLs; the root sitemap covers all 51 pages. **Only the assembled `_build/html/` is the publication artifact.**
Running an individual MyST build overwrites that directory; rerun `npm run build`
before checking or publishing the combined site. Do not run builds concurrently.

The checker validates all 51 pages, each project's branding, TOC and search membership,
nested prefixes, local links/assets/fragments, shared CSS, 45 pages with display
math, public sitemaps, and every redirect. Fully qualified links to this site's `/math/` paths
are checked against the local artifact too. Browser results and limitations are
in the [subsite split record](docs/records/subsite-split-verification.md).

Within a track, use relative Markdown links. Cross-track links use
`https://xshi19.github.io/math/...`: this MyST/theme combination prepends
`BASE_URL` to root-absolute Markdown links, so `/math/...` would be doubled.
Keep the globally unique note stems, for example
`/math/ig/information-geometry-fisher-vs-l2/`. Each track hub is its project's
`index.md`, so its URL is the base itself, without a repeated track component.
The original Incerto and Normix home URLs already equal their new homes and
remain real pages. Other old flat routes redirect, for example
`/math/incerto-pareto/` → `/math/incerto/incerto-pareto/` and
`/math/information-geometry/` → `/math/ig/`. Redirects include a meta refresh,
canonical URL, and visible link; JavaScript preserves query strings and fragments.
The [URL map](docs/plan/url-map.csv) distinguishes these implemented math redirects
from the still-proposed `/incerto-wiki/` and upstream Normix migration routes.

For interactive authoring, use `npm start` for the landing or
`npm run start:incerto`, `npm run start:ig`, or `npm run start:normix-theory`.
For a static preview under the real path:

```sh
mkdir -p _build/preview/math
rsync -a --delete _build/html/ _build/preview/math/
python3 -m http.server 8000 --directory _build/preview
```

Open `http://localhost:8000/math/`, then the three track bases. Fully qualified
cross-track links point to the public host; when previewing before publication,
open their `/math/...` paths on localhost. Review equations and desktop/mobile
navigation when changing content or the theme.

The parent owns hub assembly and republishing. After rebuilding and checking,
run this from this repository with the hub checkout at `/workspace/xshi19.github.io`:

```sh
rsync -a --delete /workspace/xshi-math/_build/html/ /workspace/xshi19.github.io/math/
```

The trailing slashes copy the assembled contents into the hub's `math/`
directory. Adjust only the destination checkout path if it lives elsewhere.
Review and publish that hub change separately; this repository does not run the
transfer or change `/normix/`.

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
