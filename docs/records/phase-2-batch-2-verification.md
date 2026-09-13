# Phase 2 — Incerto Batch 2 verification

Date: 2026-09-13 (UTC).
Status: nine-page Batch 2 import complete locally; strict HTML build and extended
38-page checker pass. Changes are uncommitted working-tree edits. Further
Phase 2 imports and public cutover remain planned.

## Source and scope

The source is `xshi19/incerto-wiki`, pinned to
`9717c9cf83aee18b47f423a14bce2f0d14bb8bcb`. The source checkout tip is
`0bb63beb029947bae3aa39e8ff067da8866a9ef7`, ahead only in planning documents;
its `content/` has no differences from the requested pin. All nine selected
files were read from their pinned Git blobs and compared byte-for-byte with
the matching checkout files. The source checkout remains clean and unchanged.
Repository edits, generated site output, and retained review artifacts are
confined to `xshi-math`.

The [executed plan](../plan/phase-2-incerto-batch-2.md) records exact source paths,
legacy URLs, adaptations, and exclusions. These files extend the existing
[Incerto hub](../../content/incerto/index.md) after the unchanged Batch 1 reading spine:

| Adapted file / route stem below `/math/` | Explicit source labels retained | Rendered display equations |
| --- | --- | --- |
| [incerto-pickands-balkema-de-haan](../../content/incerto-pickands-balkema-de-haan.md) | 1 | 6 |
| [incerto-generalized-extreme-value](../../content/incerto-generalized-extreme-value.md) | 2 | 5 |
| [incerto-frechet](../../content/incerto-frechet.md) | 1 | 8 |
| [incerto-subexponentiality](../../content/incerto-subexponentiality.md) | 2 | 18 |
| [incerto-survival-tail-ratio](../../content/incerto-survival-tail-ratio.md) | 1 | 5 |
| [incerto-max-to-sum-ratio](../../content/incerto-max-to-sum-ratio.md) | 1 | 4 |
| [incerto-double-pareto](../../content/incerto-double-pareto.md) | 3 | 13 |
| [incerto-tail-threshold-selection](../../content/incerto-tail-threshold-selection.md) | 1 | 3 |
| [incerto-body-shoulder-tail](../../content/incerto-body-shoulder-tail.md) | 1 | 14 |

No SCoFT reading guides, empirical examples, data snapshots, cached market data,
private Git history, `incerto` package implementation, or Normix/JAX code were
imported. Existing Normix and Batch 1 Incerto content pages were not edited.
The new body/shoulder/tail page links to the existing Normix normal-mixtures
note for complementary theory. External book citations remain references;
no book text, figures, or PDFs were copied into this batch.

## Adaptation decisions

- **Static calculations:** all 13 source code cells became formulas, tables,
  or arguments. Their labels now identify the static replacements. Kernelspecs
  were removed; no executable cells, fitting calls, plot generation, or notebook
  execution remain. No new runtime dependency or Python helper was added.
- **Navigation and notation:** titles moved into frontmatter and useful
  `options.concept` metadata remains. New-page links use flat `./incerto-*.md`
  stems. Deferred LLN, catalog, geometry, notation, and example pages are
  plain-text planned mentions. Required symbols are defined locally.
- **Extreme-value limits:** the GPD comparison uses its endpoint-completed
  CDF. GEV support and endpoint values are explicit, and the maxima theorem
  assumes existence of a nondegenerate iid maximum limit. Gumbel attraction
  is distinguished from exponential parent-tail decay. Exact Pareto excess
  algebra and finite-block CDF calculations replace fitting simulations.
- **Subexponentiality:** the nonnegative iid and fixed-number-of-summands
  assumptions remain explicit. The universal maximum-tail proof and Pareto
  residual-event covering proof are retained. The intermediate cutoff is
  written as `h = x_m (x/x_m)^gamma` to preserve units. A conservative bound
  table replaces the simulated convolution ratio; full equivalence and
  regular-variation results remain cited theorems.
- **Diagnostics and moments:** survival-tail geometry is distinguished from
  the convolution definition. The max-to-sum finite-mean proof remains, with
  the infinite-mean limits identified as cited results and a finite list
  replacing Monte Carlo quantiles. Double Pareto retains its signed shifted
  construction and absolute moments; an undefined ordinary mean at exponent
  at most one is distinguished from an infinite second raw moment.
- **Threshold and mixture qualifications:** the body-plus-tail threshold
  example reports population probabilities and expected counts, including the
  body contribution below the Pareto cutoff. GPD modified-scale stability is
  distinguished from the exact Pareto scale ratio. GPD moment boundaries are
  distinguished from general regular-variation boundary behavior. The local
  variance-mixture Taylor expansion has a bounded perturbation family and a
  controlled remainder; density, survival, and scale-curvature boundaries are
  derived separately. The finite normal-mixture example remains light-tailed.
- **References:** bibliography keys became ordinary author/year, DOI, or
  publisher references using the pinned bibliography. Selected metadata was
  checked against Springer's Foss–Korshunov–Zachary book record and the arXiv
  Taleb record; [NIST DLMF, Section 7.12](https://dlmf.nist.gov/7.12) supports
  the Gaussian survival asymptotic. No shared bibliography was added and no
  exhaustive independent review of all cited books or papers is claimed.
- **Notices:** [THIRD_PARTY_NOTICES.md](../../THIRD_PARTY_NOTICES.md) appends an
  Incerto Batch 2 section with all nine source/target pairs, the full pin,
  `Copyright (c) 2023 xshi19`, and the complete MIT text. Every new page repeats
  the notice in source, rendered dropdown, and downloadable Markdown. The site
  and generated content license metadata remain MIT.

Supporting updates cover the hub, site index, [myst.yml](../../myst.yml),
[HTML checker](../../scripts/check_html.py),
[migration manifest](../plan/migration-manifest.csv), and
[URL map](../plan/url-map.csv). Both CSV files add exactly nine rows; every
pre-existing row is unchanged. All nine new dispositions are `imported`.
The TOC groups the new pages into “Peaks over threshold & maxima” and
“One-big-jump diagnostics” in the specified order, retaining Batch 1 order.
README, architecture, planning index, consolidation status, and the previously
untracked Batch 2 plan now reflect eighteen imported Incerto notes and the
38-page local site.

## Executed verification

Environment: Node.js 20.19.2, npm 9.2.0, Python 3.13.5, MyST CLI 1.10.1.
Browser review uses the existing local Chrome 151.0.7922.169 and Playwright
Core 1.63.0 installation in ignored `_build/browser-tools/`; no browser
dependency was added to repository manifests.

| Check | Result |
| --- | --- |
| Source pin | Source `content/` diff empty; all nine selected files match their pinned Git blobs; source checkout remains clean |
| `npm run build` | Passed with `BASE_URL=/math myst build --html --strict --ci`; 38 pages built |
| Clean output rebuild | `myst clean --site --html --yes` followed by the strict build passed; exactly 38 current Markdown exports remain |
| `npm run check:html` | Passed for all 38 pages, local links/assets/fragments, `/math/` prefix, shared CSS, and rendered KaTeX math |
| TOC / routes / checker | Same ordered set of 38 unique sources and routes; no extra HTML routes; all nine new pages belong to `MATH_PAGES` |
| Math and labels | 76 display equations across the nine imports; all 13 explicit source labels retained in Markdown and present in HTML |
| Notices and exports | Complete pinned MIT notice present in every imported source, rendered page, and JSON-linked Markdown export; content metadata is MIT |
| Registry and artifact audit | Nine exact source/target and legacy-route mappings; old CSV rows unchanged; HTML/JSON/Markdown contain no checkout paths, stale private-source links, or executable package imports |
| Static numerical spot checks | 64 comparisons passed, including finite-block probabilities, rounded tables, normal curvature finite differences, and double-Pareto moment quadrature |
| Desktop and mobile | All 38 pages loaded at 1440 × 1000 and 390 × 844 with no page-wide overflow; representative equation/table screenshots reviewed |
| Browser navigation and runtime | Both TOC groups expand; all 19 Incerto children are accessible; hub-to-PBDH-to-GPD, TOC-to-threshold, and body-to-Normix links work; no page errors, failed resource requests, HTTP errors, or KaTeX errors |
| Source and diff review | All nine new pages and supporting edits reviewed for mathematics, scope, citations, notation, notices, and current/proposed status |
| Relative links and whitespace | Changed/new Markdown targets checked; `git diff --check` and a separate untracked-file whitespace scan passed |

The browser served the final static export locally below `/math/`. It checked
all 13 retained source IDs at both widths and confirmed consistent column
counts in the new tables. Wide display equations scroll horizontally, including
the double-Pareto formulas on mobile. The two new TOC groups use the theme's
collapsible folders; opening them exposes the new notes without changing the
existing Batch 1 order.

The first sandboxed build stopped before content parsing because MyST's npm
version subprocess was blocked with `EPERM`, reported as “Package Not Found.”
The authorized build succeeded with sandbox escalation; npm cache and build
temporary files were directed into ignored `_build/` paths. No source or
dependency change was required to resolve that environment failure.

Numerical spot checks use only Python's standard library. The normal density,
survival, and scale second derivatives were compared with five-point finite
differences at three variances and four positive observation values (scaled
tolerance `1e-6`). Six double-Pareto moments were checked by Simpson integration
after mapping the positive half-line to `[0,1]` (10,000 intervals; tolerance
`1e-10`). Remaining checks recompute the displayed rounded values and exact
formula entries with tolerances appropriate to their displayed precision.
These are finite numerical checks, not proofs of asymptotic theorems or tests
of an upstream sampler or fitter.

The tested theme is `@myst-theme/book` 1.3.1. Its `template.zip` SHA-256 is
`9ce315ec6cfe3d96f99f2c2d96e07ee4bd076b896da97178c10e32f883077bea`.
The `book-theme` alias is still not pinned to an upstream source revision.
Retained audit scripts, logs, results, and screenshots are under ignored
`_build/incerto-batch2-review/`.

## Checks not run and remaining limits

No Batch 2 local build blocker remains. `npm ci` was not rerun: the existing
pinned installation was used and the manifest and lockfile were unchanged.
Python sync/pytest, the exceedance demo, packaging, and import-isolation checks
were not rerun because `src/math/`, package mappings, dependencies, and demos
were unchanged. Earlier package checks remain in the
[foundation record](phase-0-1-verification.md).

Source simulations, GPD/GEV fitting, Monte Carlo performance comparisons, and
Lean verification were not executed. This adaptation claims ordinary
mathematical arguments and static calculations only.

Fresh builds can require theme downloads and DOI metadata requests; an offline
or hermetic build was not tested. Browser coverage is limited to Chrome at the
two stated sizes, without cross-browser or assistive-technology conformance
claims. No CI, hub assembly, public deployment, live legacy redirect, or full
historic-fragment compatibility check was performed. Retaining explicit IDs
does not establish compatibility for historical automatic heading anchors.
Legacy routes and compatibility pages retain their proposed cutover status.

The pre-existing untracked Batch 2 plan was updated in place. No commit, branch
change, Git configuration change, push, PR, Cursor CloudAgent, or source-checkout
write was made. All requested changes remain uncommitted for the parent to
commit and review.
