# Phase 2 — Incerto Batch 3 verification

Date: 2026-09-13 (UTC).
Status: eight-page Batch 3 import complete locally; strict HTML build and
extended 46-page checker pass. Parent commit/PR/merge follow. Browser review
beyond the file-level HTML gate remains optional.

## Source and scope

The source is `xshi19/incerto-wiki`, pinned to
`9717c9cf83aee18b47f423a14bce2f0d14bb8bcb`. The checkout tip is
`0bb63beb029947bae3aa39e8ff067da8866a9ef7`; its `content/` matches the pin.
All eight selected files were read from pinned Git blobs and compared
byte-for-byte with the matching checkout files. The source checkout remains
clean and unchanged. Writes, generated output, and review artifacts are confined
to `xshi-math`.

The [executed import plan](../plan/phase-2-incerto-batch-3.md) records the exact
source paths, legacy URLs, and exclusions. The five body pages and three indexes
extend the [Incerto hub](../../content/incerto/index.md):

| Adapted / rewritten file below `/math/` | Explicit source labels retained | Rendered display equations |
| --- | --- | --- |
| [incerto-cramer-condition](../../content/incerto-cramer-condition.md) | 1 | 7 |
| [incerto-generalized-central-limit-theorem](../../content/incerto-generalized-central-limit-theorem.md) | 2 | 7 |
| [incerto-lln-failure](../../content/incerto-lln-failure.md) | 2 | 8 |
| [incerto-iso-density-tail-geometry](../../content/incerto-iso-density-tail-geometry.md) | 1 | 8 |
| [incerto-tail-class-catalog](../../content/incerto-tail-class-catalog.md) | 2 | 8 |
| [incerto-theorem-concepts](../../content/incerto-theorem-concepts.md) | 0 | 0 |
| [incerto-method-concepts](../../content/incerto-method-concepts.md) | 0 | 0 |
| [incerto-distribution-concepts](../../content/incerto-distribution-concepts.md) | 0 | 0 |

No empirical examples, data snapshots, SCoFT reading guides, dependency graphs,
shared bibliography, Lean project, private history, `incerto` implementation,
Normix/JAX code, or Incerto mixture/VG body pages were imported. Normix content
is unchanged. Bibliographic references identify external works; their text,
figures, and PDFs were not copied.

## Adaptation decisions

- **Static mathematics:** all seven code cells became formulas, tables, or
  arguments. Kernelspecs and execution claims were removed. There are no
  executable cells or new Python dependencies; the site build executes none
  of these notes. All eight explicit source labels remain, including labels
  whose historical names refer to simulations or contours.
- **Cramér:** retain the one-sided exponential-moment condition, neighborhood
  condition, Chernoff proof, and rate-function definition. Clarify that an
  exponential law also has an mgf near zero on both sides. An analytic Pareto
  lower bound replaces the truncated-moment plot; failure of exponential
  moments is distinguished from infinite variance.
- **Stable limits:** preserve tail balance, slowly varying scaling, centering
  conventions, the index-one moment caveat, and the infinite-variance Gaussian
  boundary. The full classification remains cited. Exact Pareto maximum
  scaling and the algebraic ratio of two sum normalizations replace simulation;
  neither is presented as a proof of the full stable-limit theorem.
- **Infinite mean:** retain the nonnegative iid truncation proof, including the
  countable intersection of almost-sure events. A running-average identity
  and capped population-mean table replace sample paths and code output.
  Capped means are distinguished from indicator-truncated means and sample
  averages; the exact Pareto boundary is not generalized to every index-one tail.
- **Density geometry:** normal/Cauchy ratios replace contours. The axial
  comparison points are distinguished from the exact constrained Cauchy
  maximizers, derived by factoring the density denominator's derivative.
  Point density, probability mass, and the two-sided Cauchy setting remain
  distinct from the nonnegative subexponential theorem.
- **Catalog:** preserve the tail-class comparison and convolution argument.
  Exact multiplier formulas, gamma/exponential sum ratios, and a table of
  disjoint regions replace numerical integration and plotting helpers.
  The cited lognormal and stretched-Weibull classifications remain separate
  from the elementary identities proved here.
- **Navigation:** new links use flat stems. Deferred notation and empirical
  companions are plain-text planned mentions. The three indexes link all
  listed concepts to live Incerto notes or existing Normix mixture/GH notes.
  The equation-free indexes are in `PAGES` and excluded from `MATH_PAGES`.
- **References and notices:** bibliography keys became ordinary year/DOI or
  publisher links using the pinned bibliography. Selected metadata was checked
  against the Wiley Feller and Springer Resnick/Foss records. The normal-tail
  asymptotic used in the lognormal calculation follows from
  [NIST DLMF, Section 7.12](https://dlmf.nist.gov/7.12). No exhaustive independent
  review of the cited books is claimed. The
  [Batch 3 notices](../../THIRD_PARTY_NOTICES.md#incerto-batch-3) and each page
  retain `Copyright (c) 2023 xshi19` and the complete MIT permission text.

Supporting updates cover the hub, site index, [TOC](../../myst.yml),
[checker](../../scripts/check_html.py), [manifest](../plan/migration-manifest.csv),
[URL map](../plan/url-map.csv), README, architecture, and planning status.
Both CSV files append exactly eight rows; all earlier rows are unchanged.
Batch 1 order and Batch 2 titled blocks remain intact. The new sums and catalog
blocks follow them; iso-density follows body/shoulder/tail in diagnostics.
The track now has 26 concept imports: 23 body notes and three indexes, alongside
the original counting example and track hub.

Seven prior body pages received only links for Batch 3 planned mentions:
Karamata, Pareto moment existence, plug-in tail estimation, regular variation,
subexponentiality, survival-tail ratio, and max-to-sum ratio. No prior body was
re-imported. Other deferred mentions outside Batch 3 were left alone.
A small original [SVG favicon](../../assets/favicon.svg) is configured locally
because the theme's default favicon otherwise requires a network fetch.

## Executed verification

Environment: Node.js 20.19.2, npm 9.2.0, Python 3.13.5, MyST CLI 1.10.1.
The installed book theme is `@myst-theme/book` 1.3.1; its `template.zip` SHA-256 is
`9ce315ec6cfe3d96f99f2c2d96e07ee4bd076b896da97178c10e32f883077bea`.
The theme alias is still not pinned to an upstream source revision.

| Check | Result |
| --- | --- |
| Source pin | All eight selected files match pinned blobs; source `content/` diff is empty and checkout remains clean |
| `npm run build` | **Blocked / exit 1**, not a passing HTML build; see environment details below |
| Strict content processing | All 46 pages parsed and linked without content warnings before HTML-server startup failed |
| Clean generated content | `myst clean --site --html --yes` succeeded with file-based npm-version capture; subsequent processing regenerated 46 current Markdown exports |
| Separate theme export | 46 pages rendered using the cached Remix/book-theme renderer, with content transport changed to local file reads in a review-only harness |
| `npm run check:html` | Passed on that separate export: 46 pages, local links/assets/fragments, `/math/` prefix, shared CSS, and rendered KaTeX |
| TOC / routes / checker | Same ordered set of 46 unique sources/routes; five new body pages require math and three new indexes do not |
| Math and source labels | 38 display equations across the five new body notes; all eight explicit source labels present in Markdown and rendered HTML |
| Notices and exports | Complete pinned MIT notice present in all eight sources, rendered pages, and downloadable Markdown; content metadata is MIT |
| Registry and artifact audit | Eight exact source/target and legacy-route pairs; old rows unchanged; no checkout paths, stale private-source links, or executable package imports in HTML/JSON/Markdown |
| Static numerical checks | 82 comparisons passed using only Python's standard library |
| Source and diff review | New files and supporting changes reviewed for assumptions, notation, scope, citations, provenance, and current/proposed status |
| Relative links and whitespace | Changed/new Markdown targets checked; `git diff --check` and separate untracked-file whitespace scan passed |
| Browser / desktop / mobile | Not run: localhost listeners are denied in this sandbox |

The first build failed before content parsing because Node's npm-version
subprocess returned `EPERM`, reported by MyST as “Package Not Found.” Direct
`npm --version` returned 9.2.0. A review-only preload captured the actual
subprocess output through files under `_build/` instead of Node's denied pipe
transport. It did not fabricate a version or skip the version check.

With that preload, the unchanged strict build command processed all 46 pages,
then failed at `uv_interface_addresses`. A separate localhost-listener probe
also returned `listen EPERM: operation not permitted 127.0.0.1`. No sandbox
escalation was requested or used during the Codex session. The parent runner later completed the standard build outside that sandbox.

To inspect rendering without a server, a separate harness called the cached
book theme's Remix request handler directly. Only its content-fetch transport
was replaced with reads of the generated site files. The harness exported HTML,
JSON, theme assets, and Markdown and applied MyST's `/math/` asset-path rewrite.
The cached renderer and installed CLI files were not modified. This verifies
static rendering through that harness, **not** the normal server/export path,
browser hydration, or navigation interactions. Its initial favicon omission and
unavailable external default favicon were resolved with the local SVG asset.

Numerical checks recomputed rounded table values, compared exponential truncated
moments and capped Pareto means with Simpson integration, checked the Pareto
exponential-moment bound, running-mean identity, normal/Cauchy ratios and density
stationary points, and compared normalized convolution integrals against the
closed gamma/exponential sum formulas. Integration used 10,000 subintervals;
finite differences used a five-point stencil. Tolerances reflect displayed
precision or the finite numerical method. These checks do not prove asymptotic
limits or validate upstream simulation and fitting code.

Logs, source blob IDs, numerical checks, artifact audit, and the two review-only
transport/rendering scripts are retained under ignored
`_build/incerto-batch3-review/`. No review tool or runtime dependency was added
to repository manifests.

## Parent runner follow-up

After the Codex sandbox session, the parent runner executed the standard
`npm run build` (`BASE_URL=/math myst build --html --strict --ci`) and
`npm run check:html`. Both passed for **46** pages under `_build/html`. The
sandbox-only transport workarounds above remain historical notes of the Codex
session; the ordinary HTML gate is now green.

## Checks not run and remaining limits

Desktop/mobile browser review beyond the file-level HTML checker was not
required for this batch gate. Cross-browser and assistive-technology checks
remain out of scope.

`npm ci` was not rerun; the existing pinned installation was used and npm
manifests are unchanged. Python sync/pytest, the demo, packaging, and import
isolation were not rerun because Python sources, dependencies, and package
mappings are unchanged. Source simulations, numerical tail-class inference,
Lean, cross-browser checks, CI, hub assembly, deployment, and live legacy
redirects were not executed. Historical automatic heading fragments remain
unaudited; preserving explicit labels does not establish full compatibility.
Fresh builds may still require theme and DOI metadata downloads.

The Batch 3 plan was updated in place. The separate
`docs/plan/phase-2-normix-theory-batch-2.md` remains present for a later Normix
batch and was not executed. No Cursor CloudAgent or source-checkout write was
made. Parent commit/PR/merge follow on branch `content/incerto-batch-3`.
