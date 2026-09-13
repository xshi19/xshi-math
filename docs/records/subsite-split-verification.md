# Independent math subsites: verification

Date: 2026-09-13. Base: `main` at `9e4ee05` (PR #10). The owner selected
Codex GPT-6-Astra xhigh and authorized branch/PR/merge work. No Cursor CloudAgent
or hub repository work was used.

## Result and URL decisions

The former 51-page book is now four independent MyST projects, assembled into
one publication artifact at `_build/html/`:

| Site | Config | Home source | Public home | Pages |
| --- | --- | --- | --- | --- |
| Landing | `myst.landing.yml` | `content/index.md` | `/math/` | 1 |
| Incerto | `myst.incerto.yml` | `content/incerto/index.md` | `/math/incerto/` | 28 |
| Information Geometry | `myst.ig.yml` | `content/ig/index.md` | `/math/ig/` | 7 |
| Normix theory | `myst.normix-theory.yml` | `content/normix-theory/index.md` | `/math/normix-theory/` | 15 |

Each track has its own project/site title, logo text, TOC, search data, and
assets. The landing hides the TOC, outline, search, and previous/next links.
`myst.yml` extends the landing for default authoring; production explicitly builds
all four configs. Shared styles and favicon still come from `assets/`.

Notes retain globally unique stems under `content/`. Each track's sole index is
its home, so there is no `/math/incerto/incerto/` or repeated Normix hub segment.
IG uses the short public base while retaining `information-geometry-*` stems:
`/math/ig/information-geometry-fisher-vs-l2/`.

Within-track links remain relative Markdown paths, with adjusted paths to/from
moved indexes. Cross-track links use full `https://xshi19.github.io/math/...`
URLs. A trial with root-absolute Markdown links rendered `/math/math/incerto/`
on the landing: this MyST/theme combination prepends `BASE_URL`. Full URLs avoid
that duplication without editing rendered HTML. The theme treats these as
external links and opens a new tab; browser checks verify the destination's
independent branding. Normix package/API links retain `https://xshi19.github.io/normix/`.

`scripts/site_layout.py` centralizes the four bases, source membership, and
old flat routes. The sequential build saves exports under `_build/subsites/`,
clears `_build/site/` between projects, and retains the theme and DOI cache.
After assembly it writes public sitemaps and discovery URLs because the theme's
static export originally contained `localhost:3000`. The root sitemap covers
all 51 canonical pages; track sitemaps cover only their own pages.

## Compatibility routes

All 47 note/concept stems and the old IG hub have redirect HTML with a canonical
link, meta refresh, and visible destination. JavaScript preserves query strings
and fragments. `/math/`, `/math/incerto/`, and `/math/normix-theory/` already equal
their new homes and remain real pages, avoiding self-redirects.

| Old path | Destination |
| --- | --- |
| `/math/incerto-pareto/` | `/math/incerto/incerto-pareto/` |
| `/math/information-geometry/` | `/math/ig/` |
| `/math/information-geometry-fisher-vs-l2/` | `/math/ig/information-geometry-fisher-vs-l2/` |
| `/math/normix-varentropy/` | `/math/normix-theory/normix-varentropy/` |

The [URL map](../plan/url-map.csv) updates earlier destinations and adds all 51
old flat math mappings, including the three retained homes. These generated math
redirects do not implement the older `/incerto-wiki/` or upstream Normix
migration proposals. Their source-site compatibility work remains separate.

## Verification performed

| Check | Result |
| --- | --- |
| Latest main / identity inspection | Fetched `origin`; main was `9e4ee05`, author `Xiang Shi <soarshi@gmail.com>`, committer `GitHub <noreply@github.com>` |
| `npm ci` | Passed; MyST 1.10.1 and unchanged dependency lock; zero reported vulnerabilities |
| `npm run build` | Passed for landing (1), Incerto (28), IG (7), and Normix theory (15), each using `--html --strict --ci` and its nested `BASE_URL`; assembled all four plus 48 redirects |
| `npm run check:html` | Passed for all 51 pages, 48 redirects, and 45 pages requiring display equations; local links/assets/fragments, branding/TOCs/search, public sitemaps, nested prefixes, shared CSS, and stale private-source checks |
| Static preview | README rsync staging passed; local Python HTTP server returned 200 for 11 representative home, note, redirect, and CSS paths under `/math/` (used an available ephemeral port because 8000 was occupied) |
| Default `myst.yml` | `BASE_URL=/math myst --config myst.yml build --site --strict --ci` passed and built only the landing |
| Python syntax | `python3 -m py_compile` passed for all four build/check/route scripts |
| Checker negative probes | Six isolated artifact mutations were rejected: wrong redirect, foreign branding, doubled base path, KaTeX error, altered shared CSS, and foreign search page |
| Source preservation | Compared all 50 existing track sources against main after removing Markdown link destinations: identical; all equations, assumptions, notices, and prose preserved; all 51 Markdown sources belong to exactly one subsite |
| Desktop/mobile browser | All 51 pages inspected at 1440 and 390 px (102 visits); correct logo/home links and track-only sidebars, zero KaTeX errors or viewport overflow; sidebar-to-note and logo-to-home interactions passed for all three tracks at both widths |
| Redirect and cross-track browser interaction | All 48 redirects preserve query strings and fragments; all three landing links and three representative cross-track body links open the correct independent site; meta refresh works without JavaScript for Incerto, old IG hub, and Normix examples; final navigation run has no browser errors |
| Diff, new files, and documentation links | Reviewed changed diffs and full new files; `git diff --check` and separate whitespace scan passed; 407 relative Markdown links resolve; all 51 CSV math mappings match the assembled routes |

Browser review uses Chromium 151.0.7922.169 via Playwright. The browser's public
`https://xshi19.github.io/math/...` requests are fulfilled from the local assembled
artifact, allowing full-URL cross-track navigation without fetching unpublished
public pages. Other theme CDN assets load normally. This is local artifact
verification, not a live-host check. Review scripts, screenshots, logs, and JSON
results are under ignored `_build/subsite-review/` and `_build/subsite-*.log`.

The initial build encountered transient DOI metadata failures for two Incerto
citations; other concurrent lookups populated the normal DOI cache, and a rerun
passed. No citation or mathematical content was changed to bypass strict checks.
The browser page review completed; its first redirect pass overlapped the
sitemap rebuild and was restarted after assembly finished.

Toolchain: Node 20.19.2, npm 9.2.0, Python 3.13, MyST CLI 1.10.1. The reused
book-theme package reports 1.3.1. Its downloaded files have SHA-256 identities:

```text
template.zip   9ce315ec6cfe3d96f99f2c2d96e07ee4bd076b896da97178c10e32f883077bea
template.yml   23026075f17327b7d8cacebbf8460aeb0f3b0c81fecad8d05b98ad731f533f79
build/index.js ffcb56f443c86b1996da91121e245e219d6619a385c0b40693005290b235bfe6
```

The theme alias remains a separate download, so the CLI pin alone does not pin
a future fresh theme fetch.

## Parent handoff and remaining limits

From the rebuilt, checked source checkout, the parent's exact transfer is:

```sh
rsync -a --delete /workspace/xshi-math/_build/html/ /workspace/xshi19.github.io/math/
```

Adjust the destination checkout path if necessary; preserve the trailing slash
and the `math/` destination. The parent must review and publish that hub change,
then check live direct URLs, fragments, navigation, and sibling `/normix/`
content. This task neither copies files into the hub nor republishes it.

Python package tests, demos, and wheel builds were not rerun because no Python
library, dependency, package mapping, or numerical behavior changed. Interactive
`npm start:*` servers were not separately exercised; their configs were validated
by the strict exports. There is no CI workflow in this repository. Existing
untracked `.codex/prompts/` files are outside this change.
