# Phase 0: Light Inventory

Status: representative inventory complete; full import and publication audit pending.
Review date: 2026-09-13.

This review covers repository metadata, content paths, publishing configurations,
and a sample of public artifacts. It imports no wiki bodies, implementation code,
or private history. The CSV dispositions are proposed preparation work, not
records of files already moved or cleared for publication.

## Sources and access

The requested `gh api` read failed to connect to `api.github.com`; `gh auth status`
also reported a credential failure. Authenticated connected GitHub reads supplied
the inventory instead. No credentials or private exclusion details are recorded.
The following are commit IDs, not individual file blob IDs:

| Repository | Inspected revision | Scope |
| --- | --- | --- |
| [Incerto](https://github.com/xshi19/incerto-wiki/tree/9717c9cf83aee18b47f423a14bce2f0d14bb8bcb) (private) | `9717c9cf83aee18b47f423a14bce2f0d14bb8bcb` | Root/content trees, MyST and Python metadata, license, all three workflows, documentation build script |
| [Normix](https://github.com/xshi19/normix/tree/763bb3608920661a012cf089888d349fbf680aad) | `763bb3608920661a012cf089888d349fbf680aad` | Docs/theory tree, Sphinx configuration, license, docs and package publishing workflows |
| [Hub](https://github.com/xshi19/xshi19.github.io/tree/0768d3ce6814072c1a8dce77a2f8331e0bf682d7) | `0768d3ce6814072c1a8dce77a2f8331e0bf682d7` | Complete tree listing, recent commits and Pages runs, representative Incerto JSON metadata |

These revisions anchor this review. They are not a rehearsed rollback package
or a claim that the deployed sites match the latest source revisions.

## Source shape and dispositions

Incerto has `content/` entries for concepts, notation, glossary, reading guides,
formalization, releases, a Chinese entry, bibliography, and an API reference.
Its root also contains `incerto/`, `tests/`, `assets/`, `data/`, `formalization/`,
`docs/`, `scripts/`, and legacy build configuration. This describes categories;
it is not a public list of private drafts or excluded assets.

Normix has identifiable `docs/theory/` pages, including `gig.md`, `gh.md`,
`em_algorithm.md`, and `online_em.md`. Its `docs/api/`, `docs/design/`,
`docs/user_guide/`, and implementation remain upstream. The selected theory
sample is a candidate for adaptation, not approval to move every theory page.

| Disposition | Representative material | Gate |
| --- | --- | --- |
| `adapt` | Incerto home, concepts, notation, reading guide; selected Normix theory | Review semantics, references, rights, labels, and actual old routes |
| `move` | A future reusable helper together with its tests, if selected | Establish consumers, behavior, dependencies, and notices first; no helper selected in this light sample |
| `stay` | Normix package/API/release machinery; private provenance archive | Preserve repository boundary and link to supported upstream behavior |
| `exclude` | Generated hub output as an import source | Rebuild from approved source; retain old artifacts separately for rollback and URL discovery |

[migration-manifest.csv](migration-manifest.csv) contains a representative sample
with revision/path provenance. Third-party rights and outside consumers of the
existing `incerto` import remain unreviewed. No claim of complete coverage is made.

## Hub publishing findings

The hub tree has `.nojekyll`, root HTML/blog/theme artifacts, `incerto-wiki/`, and
`normix/`. Its `.github/workflows` endpoint returned 404, consistent with the
tree containing no `.github` directory. The root HTML is consistent with the
existing Pelican/blog site; its generator source and writer were not audited.

The hub history records [Add updated normix docs site](https://github.com/xshi19/xshi19.github.io/commit/7ebc913e53aa00757facce046ef94553ca782ffa)
and [Publish Incerto Wiki](https://github.com/xshi19/xshi19.github.io/commit/b49b823d13ccfb02f28e012d6d8595c144dd16f5).
These demonstrate committed artifact updates. Commit authorship alone does not
identify the script, machine, or external automation that made them.

GitHub reports successful hub runs named `pages build and deployment`, with path
`dynamic/pages/pages-build-deployment` and event `dynamic` on `main`, including
[the inspected hub revision](https://github.com/xshi19/xshi19.github.io/actions/runs/26549852898).
This is evidence of GitHub's generated Pages pipeline without a checked-in
workflow. Branch-based Pages publication is the likely explanation; the exact
Pages source/settings were not read. Do not infer that the hub has no automation.

| Source writer | What the inspected configuration does | Relationship to the hub |
| --- | --- | --- |
| [Incerto `ci.yml`](https://github.com/xshi19/incerto-wiki/blob/9717c9cf83aee18b47f423a14bce2f0d14bb8bcb/.github/workflows/ci.yml) | Builds with `BASE_URL=/incerto-wiki`; uploads an artifact; default-branch push/manual runs use `actions/deploy-pages` | Publishes repository Pages; contains no checkout or write of the hub repository |
| [Incerto `release.yml`](https://github.com/xshi19/incerto-wiki/blob/9717c9cf83aee18b47f423a14bce2f0d14bb8bcb/.github/workflows/release.yml) | On version tags/manual runs, tests and builds `_build/html`, then uploads `incerto-wiki-site` | Artifact only; no deploy step and no explicit base-path environment in this workflow |
| Incerto `lean.yml` | Runs the Lean build for affected paths | No site publisher |
| [Normix `docs.yml`](https://github.com/xshi19/normix/blob/763bb3608920661a012cf089888d349fbf680aad/.github/workflows/docs.yml) | Builds Sphinx and ASV output; branch pushes deploy via `peaceiris/actions-gh-pages` with its repository token | Writes Normix's own `gh-pages`; no `external_repository` or hub checkout |
| [Normix `docs-full.yml`](https://github.com/xshi19/normix/blob/763bb3608920661a012cf089888d349fbf680aad/.github/workflows/docs-full.yml) | Tag/manual build forces notebook execution and deploys through the same action | Another writer of Normix's own `gh-pages`; separate concurrency group from `docs.yml` |
| [Normix `publish.yml`](https://github.com/xshi19/normix/blob/763bb3608920661a012cf089888d349fbf680aad/.github/workflows/publish.yml) | Builds distributions and publishes to PyPI | No documentation/hub deployment |

Normix also lists `asv.yml`, `ci.yml`, and `release-please.yml`; ASV was inspected
as a PR benchmark check. Package CI and release-please internals were outside
this publishing sample. None of the inspected publishers demonstrates automatic
transfer into the hub's committed trees. The transfer writer, root/blog writer,
effective live-prefix ownership, and coordination across repositories remain
open. Source-repository concurrency groups do not serialize hub writes.

## Build-stack differences

Incerto's [MyST configuration](https://github.com/xshi19/incerto-wiki/blob/9717c9cf83aee18b47f423a14bce2f0d14bb8bcb/myst.yml)
uses `book-theme`, an explicit TOC, bibliography, and custom CSS. Its Python
metadata names `incerto`, uses setuptools and Python >=3.10, and includes NumPy,
SciPy, Matplotlib, and requests. The development extra includes Jupyter Book 2
and Sphinx. `scripts/build_docs.py` runs executed MyST through `jupyter book`,
adds Sphinx API output under `api/`, copies graph assets, and wires custom
reading-navigation JavaScript into HTML.

Normix's [Sphinx configuration](https://github.com/xshi19/normix/blob/763bb3608920661a012cf089888d349fbf680aad/docs/conf.py)
uses `myst_nb`, `sphinx_book_theme`, autodoc/intersphinx, cached notebook execution,
and its own CSS. Sphinx roles, Python-domain links, directives, execution rules,
and CSS selectors need adaptation before those pages enter the new MyST site.
The new foundation uses the MyST CLI directly; it does not reproduce either
sibling's complete build stack or custom navigation patch.

## URLs and rights

The hub contains Incerto directory-index HTML, JSON page records, and many
`incerto-wiki/build/index-*.md` exports. The reviewed public JSON records identify
the home, Pareto, regular variation, Hill estimator, notation (`index-1`), and
SCoFT introduction (`intro`) by both title and source path. They still expose
the older `Technical-Incerto-Python` source/edit URLs and CC-BY-4.0 metadata.
Do not carry those links or blindly relabel historic exports in a future import.

[url-map.csv](url-map.csv) records observed artifact routes, one observed download,
and a small Normix theory sample. Proposed destinations are explicitly marked;
the new sample pages are not replacements for the old Pareto or GH pages.
Blank fragment fields mean page-level rows, not a completed fragment audit.
The Normix GH page was fetched from the live site; Incerto live requests failed
in the web tool, so its rows rely on committed artifact evidence only.

The [root licenses](../design/LICENSE_ADVICE.md#evidence-from-the-siblings) were
rechecked: Incerto carries MIT copyright 2023 xshi19; Normix carries MIT copyright
2020 xshi19. Incerto Python metadata says MIT while its MyST metadata says
CC-BY-4.0. The owner's decision remains MIT for owner-controlled imports, with
retained notices. Page-level contributions, quotations, figures, downloaded
sources, and data still require review. No third-party material was imported by
this foundation; dependencies retain their own licenses.

## Next gates

1. Complete the foundation's pinned HTML build and rendered desktop/mobile
   review; see [verification record](../records/phase-0-1-verification.md).
2. Obtain the Information Geometry entry list before choosing substantive pages.
3. Before Phase 2 import, expand the representative inventory, review rights and
   source/download metadata, identify Python consumers, and preserve notices.
4. Before artifact transfer, establish the actual hub/root writers, Pages settings,
   live routing precedence, and one publication coordination mechanism.
5. Before cutover, freeze the complete URL/fragment/download map, rehearse the
   combined artifact, preserve sibling prefixes, record rollback artifacts, and
   coordinate the existing source Pages publishers.
