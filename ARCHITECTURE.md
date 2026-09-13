# Architecture

The repository contains three independent mathematical subsites, a landing,
and one educational Python package. The
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
and the sandbox restriction encountered during that batch. The
[Normix Batch 2 record](docs/records/phase-2-normix-batch-2-verification.md)
covers five further theory notes and the standard 51-page HTML gate.

| Surface | Current responsibility |
| --- | --- |
| `myst.{landing,incerto,ig,normix-theory}.yml`, `content/` | Four independent projects: landing (1 page), Incerto (28), Information Geometry (7), and Normix theory (15); `myst.yml` extends the landing for default authoring |
| `content/notation.md` | One shared notation canon for all three tracks (`/math/notation/`) |
| `assets/styles/math.css` | Original typography, equation overflow, and focus styles layered over the theme |
| `package.json`, `package-lock.json` | MyST CLI 1.10.1; `npm run build` builds and assembles all four sites with their own `BASE_URL` |
| `pyproject.toml`, `uv.lock`, `.python-version` | Locked NumPy/pytest environment; Python 3.13 development default |
| `src/math/` | Source directory explicitly installed as `xmath` by setuptools; no top-level `math` package |
| `demos/`, `tests/` | A deterministic exceedance example and checks of counting, invalid input, and import isolation |
| `scripts/build_sites.py`, `scripts/site_layout.py`, `scripts/write_redirects.py` | Export separately, assemble `_build/html/`, and generate 48 old flat math redirects from the shared route layout |
| `scripts/check_html.py` | Checks all pages and redirects, independent branding/TOCs, local routes/assets/fragments, nested base paths, shared CSS, and rendered equations |
| `docs/plan/` | Representative inventory, imported Incerto Batch 1/2/3 and Normix Batch 1/2 dispositions, remaining proposals, URL mappings, and pending gates |

Body notes and concept indexes keep globally unique Markdown stems flat under
`content/`. Each former track hub now lives at `content/{incerto,ig,normix-theory}/index.md`
and is the first entry in its own explicit TOC. Repeated `index.md` names are
safe across independent projects; there is only one index per build. No new
mathematical material, Python helpers, or notebook execution was introduced.
MIT notices remain on the adapted notes.

MyST CLI 1.10.1 derives note routes from filenames and ignores `slug:`. The
host metadata is `xshi19.github.io`; each build supplies `/math`, `/math/incerto`,
`/math/ig`, or `/math/normix-theory` as `BASE_URL`. The landing has no book TOC;
each track has independent branding, navigation, search data, and assets.
Relative Markdown links stay within a track. Cross-track links use full public
URLs because the theme prepends the base to root-absolute Markdown links.
Normix package/API links retain the separate `https://xshi19.github.io/normix/` base.

The sequential build clears `_build/site/` and saves each MyST HTML export in
`_build/subsites/<site>/`, retaining the theme and DOI cache. It then assembles:

```text
_build/html/
  index.html                     # landing at /math/
  incerto/index.html             # Incerto home
  incerto/incerto-pareto/         # example Incerto note
  ig/index.html                  # Information Geometry home
  ig/information-geometry-*/     # IG notes retain their stems
  normix-theory/index.html       # Normix theory home
  normix-theory/normix-*/        # Normix theory notes
  incerto-pareto/index.html      # old flat route redirect
  information-geometry/index.html # old IG hub redirect
  normix-varentropy/index.html   # old flat route redirect
```

Each site carries its own assets alongside these pages. Assembly replaces the
theme's localhost sitemap/discovery URLs with public URLs; the root sitemap
covers all 51 canonical pages and track sitemaps cover their own pages. All 47 body/concept
note URLs and the old IG hub get static redirects with canonical links and
visible destinations; JavaScript preserves queries and fragments. Incerto and
Normix hub paths already match, so they remain real pages without self-redirects.
Older `/incerto-wiki/` and upstream Normix migration routes remain separate
publication work. See the [URL map](docs/plan/url-map.csv) and
[subsite verification record](docs/records/subsite-split-verification.md).

The intended artifact is the assembled `_build/html/`, copied by the parent into
`math/` in the hub; the exact rsync is in the [README](README.md#build-the-sites).
Build outputs, environments, and installed tools are ignored by Git. The CLI is
pinned; the upstream `book-theme` alias downloads a separate theme whose build
identity is recorded with verification.

The dependency direction remains `xshi-math -> normix` for future package demos.
This foundation links upstream without installing or vendoring Normix. The hub
owns public assembly; no workflow here writes to it. Twenty-six Incerto concept pages and thirteen
Normix notes are adapted with source notices; no private history, Lean project, CI
workflow, or public math deployment was added. The
[Information Geometry outline](docs/plan/ig-entry-outline.md) separates the
implemented Basics / early IG notes from later marginalization and GH/Normix
research pages.
