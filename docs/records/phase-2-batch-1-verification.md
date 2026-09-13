# Phase 2 — Incerto Batch 1 verification

Date: 2026-09-13 (UTC).
Status: nine-page Batch 1 import complete locally; strict HTML build and extended
checker pass. All changes are uncommitted working-tree edits. Further Phase 2
imports and public cutover remain planned.

## Source and scope

The source is `xshi19/incerto-wiki`, pinned to
`9717c9cf83aee18b47f423a14bce2f0d14bb8bcb` (`origin/main`). The source checkout's
`content/` had no differences from that revision. Each of the nine selected
files was also compared byte-for-byte with its Git blob at the pin. Sources
were read from the sibling checkout; all writes were confined to `xshi-math`.

The [executed plan](../plan/phase-2-incerto-batch-1.md) retains the source-path
mapping and exclusions. These flat files now follow the existing counting
example beneath the [Incerto hub](../../content/incerto/index.md):

| Adapted file / route stem below `/math/` | Explicit source labels retained | Rendered display equations |
| --- | --- | --- |
| [incerto-pareto](../../content/incerto-pareto.md) | 6 | 12 |
| [incerto-regular-variation](../../content/incerto-regular-variation.md) | 2 | 7 |
| [incerto-karamata](../../content/incerto-karamata.md) | 1 | 13 |
| [incerto-pareto-moment-existence](../../content/incerto-pareto-moment-existence.md) | 4 | 8 |
| [incerto-mean-excess-function](../../content/incerto-mean-excess-function.md) | 1 | 8 |
| [incerto-hill-estimator](../../content/incerto-hill-estimator.md) | 3 | 7 |
| [incerto-extreme-value-index](../../content/incerto-extreme-value-index.md) | 1 | 6 |
| [incerto-generalized-pareto](../../content/incerto-generalized-pareto.md) | 2 | 8 |
| [incerto-plug-in-tail-estimation](../../content/incerto-plug-in-tail-estimation.md) | 7 | 14 |

No SCoFT reading guides, empirical datasets, snapshots, private Git history,
`incerto` package implementation, or Normix/JAX code were imported. The SCoFT
book citation in the plug-in note remains an attributed external reference.

## Adaptation decisions

- **Static calculations:** the owner-authorized static option replaces all
  executable cells with equations, exact tables, or explanatory prose. Former
  cell labels now identify those replacements. No kernel, SciPy, matplotlib,
  or upstream `incerto` dependency is needed. `src/math/`, `demos/`, Python
  dependencies, and the `xmath` package mapping are unchanged.
- **Navigation and notation:** imported cross-links use `./incerto-*.md`.
  Deferred targets are plain text with planned status, or their link markup was
  removed. Necessary notation is defined on each page. Useful concept metadata
  remains; notebook kernelspecs and deferred prerequisite metadata were removed.
- **Mathematical scope:** the Pareto moment proof, regular-variation
  characterization, Karamata moment consequences, Hill calibration, and
  plug-in delta-method derivation remain. General limit theorems and Karamata's
  integral theorem remain cited results. The static examples make no claims
  about measured simulation performance or checked Lean proofs.
- **Clarifications:** the adaptation distinguishes truncated population moments
  from sample moments, specifies GPD endpoint values and threshold stability,
  states Hill's log-survival domain and behavior with ties, and distinguishes
  GPD moment boundaries from the slowly-varying-factor dependence of general
  regular-variation boundary moments. The plug-in note retains its conditional
  normal limit, finite-sample singularity, non-finite fits, and body contribution.
- **References:** source bibliography keys became attributed year/DOI or
  publisher links. Selected bibliographic metadata was checked against the
  source bibliography and publisher/DOI records; no shared bibliography was
  copied. MyST resolves DOI links into citation metadata. The first build
  stopped on unavailable metadata for van der Vaart's book; using its
  [publisher page](https://www.cambridge.org/core/books/asymptotic-statistics/A3C7DAD3F7E66A1FA60E9C8FE132EE1D)
  resolved that failure without suppressing strict checks. MyST documents this
  [DOI lookup behavior](https://mystmd.org/guide/citations).
- **Notices:** [THIRD_PARTY_NOTICES.md](../../THIRD_PARTY_NOTICES.md) records the
  pin, source paths, adaptations, and the original `Copyright (c) 2023 xshi19`
  with the complete MIT text. Each page repeats the notice in its rendered
  permission dropdown and downloadable Markdown. Project and generated page
  license metadata remain MIT. No third-party images or substantial quoted
  passages were included in the adapted Markdown.

Supporting edits update [myst.yml](../../myst.yml), the site index and Incerto hub,
[check_html.py](../../scripts/check_html.py), the
[migration manifest](../plan/migration-manifest.csv), and
[URL map](../plan/url-map.csv). All nine manifest entries are `imported`; the
URL map contains nine Batch 1 routes, including six new rows. Live compatibility
pages remain proposed. README, architecture, the planning index, and the
consolidation status now distinguish this completed batch from future imports.

## Executed verification

Environment: Node.js 20.19.2, npm 9.2.0, Python 3.13.5, MyST CLI 1.10.1.
Browser checks used Chrome 151.0.7922.169 through Playwright Core 1.63.0,
installed only in ignored `_build/browser-tools/` for this review.

| Check | Result |
| --- | --- |
| Source pin | `origin/main` equals the pin; `content/` diff empty; all nine selected files match their pinned Git blobs |
| `npm ci` | Passed using the unchanged npm lockfile |
| `npm run build` | Passed with `BASE_URL=/math myst build --html --strict --ci`; 21 pages built, no warnings or errors |
| Clean output rebuild | `myst clean --site --html --yes`, followed by `npm run build`, passed; exactly 21 current Markdown exports remain, with no stale source exports |
| `npm run check:html` | Passed on the clean output for all 21 pages, local links/assets/fragments, `/math/` prefix, shared CSS, and KaTeX math |
| TOC / routes / checker | Identical ordered set of 21 unique flat sources and expected routes; no extra HTML pages or `index-N/` routes |
| Imported math and labels | All nine pages contain display math (83 display equations total); all 27 explicit source IDs are retained in Markdown and present in HTML |
| Notices and artifact | MIT page metadata and complete notices verified in all nine pages and their JSON-linked Markdown exports; HTML/JSON/Markdown scan found no stale private-source links, source-checkout paths, or `from incerto.*` imports |
| Desktop, 1440 × 1000 | All 21 pages loaded with no page-wide overflow; representative equations and screenshots reviewed |
| Mobile, 390 × 844 | All 21 pages loaded with no page-wide overflow; representative equations and screenshots reviewed; a wide equation was successfully scrolled horizontally |
| Navigation, both widths | All ten Incerto TOC children visible; TOC-to-Hill, hub-to-Pareto-to-moments, and mean-excess-to-GPD section link worked |
| Browser runtime | No page errors, failed resource requests, HTTP errors, or KaTeX error elements during the checks |
| Source and diff review | Nine new pages read in full; assumptions, citations, deferred links, notices, and all supporting changes reviewed |
| Relative Markdown links and whitespace | Checked changed/new Markdown paths; `git diff --check` and a separate new-file whitespace scan passed |

The browser served the static export beneath `/math/` from a local server,
without writing to the publishing hub. Temporary browser scripts, screenshots,
JSON results, and the clean-build log remain under ignored `_build/` directories.
The final clean rebuild used the same sources and theme as the browser checks;
its HTML checker, notice/export audit, and artifact scan were repeated afterward.

The tested theme is `@myst-theme/book` 1.3.1. Its `template.zip` SHA-256 is
`9ce315ec6cfe3d96f99f2c2d96e07ee4bd076b896da97178c10e32f883077bea`.
The `book-theme` alias is still not pinned to an upstream source revision.

## Checks not run and remaining limits

No Batch 1 local build blocker remains. Python sync/tests, the exceedance demo,
wheel builds, and import-isolation checks were not rerun: this batch changes no
Python helper, dependency, package mapping, or demo. The HTML checker itself
was exercised by `npm run check:html`. Earlier Python results remain in the
[foundation record](phase-0-1-verification.md).

The former plots, stochastic diagnostics, and repeated-sample performance
tables were not executed. No Lean project or formal-proof check was added.
The site uses static mathematical explanations; runnable numerical additions
are deferred until there is a concrete reuse need.

Fresh builds still need the theme download and may need DOI metadata requests;
an offline or fully hermetic build was not tested. Browser review covers Chrome
at the two stated sizes, not cross-browser or assistive-technology conformance.
No CI, hub assembly, public deployment, live legacy redirects, or full historic
fragment compatibility audit was performed. Retaining explicit source labels
does not establish compatibility for every historic automatically generated
heading fragment. Rights review for further imports remains outside Batch 1.

The pre-existing manifest edits and untracked Batch 1 plan were incorporated;
unrelated manifest proposals were preserved. No commit, branch, Git
configuration change, push, PR, Cursor CloudAgent, or source-repository write
was made.
