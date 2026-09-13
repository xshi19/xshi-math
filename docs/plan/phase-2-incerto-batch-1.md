# Phase 2 — Incerto Batch 1

Status: **Batch 1 executed locally** on 2026-09-13. Nine adapted pages are
written; the strict HTML build and extended 21-page checker pass. Changes are
uncommitted. Further Phase 2 imports and public cutover remain planned.
See the [verification record](../records/phase-2-batch-1-verification.md).
Date: 2026-09-13 (ET).
Survey checkout: `/workspace/incerto-wiki` on `codex/update-plan-after-plugin` @ `0bb63be` (1 commit ahead of `origin/main` @ `9717c9c`; **content/ identical to origin/main**). Manifest revision pinned to `9717c9cf83aee18b47f423a14bce2f0d14bb8bcb`.

## Goal

First bounded import into `xshi-math` for `/math/incerto*`: owner-written concept / method / theorem pages that form the Pareto-type + tail-estimation spine. Defer Taleb SCoFT chapter dumps and data-heavy examples.

## Source survey (`incerto-wiki/content/`)

| Area | Count (approx) | Batch 1? |
| --- | --- | --- |
| `concepts/distributions/` | 8 | 2 pages (Pareto, GPD) |
| `concepts/theorems/` | 9 | 4 pages |
| `concepts/methods/` | 8 | 3 pages |
| `concepts/examples/` | 5 | defer (data / datasets) |
| hubs (`*-concepts.md`, `dependency-dag.md`) | 5 | defer (DAG needs `assets/graphs/`) |
| `reading-guides/taleb-scoft/*` | 6 | **defer — rights review** |
| `reading-guides/external/*` | 2 | defer |
| `notation/`, `glossary/`, bib, home | — | later batch (shared refs) |
| `api-reference.md`, Lean, releases, zh-cn | — | stay / exclude from public math import |

## Batch 1 pages (9)

MyST needs **unique flat stems** under `content/*.md` (match current scaffold; no nested `index.md`). Locally verified routes (not yet deployed): `/math/<stem>`.

| # | Source path | Stem → `content/<stem>.md` | Legacy URL | Disposition |
| --- | --- | --- | --- | --- |
| 1 | `content/concepts/distributions/pareto.md` | `incerto-pareto` | https://xshi19.github.io/incerto-wiki/pareto/ | imported (adapted) |
| 2 | `content/concepts/theorems/regular-variation.md` | `incerto-regular-variation` | https://xshi19.github.io/incerto-wiki/regular-variation/ | imported (adapted) |
| 3 | `content/concepts/theorems/karamata.md` | `incerto-karamata` | https://xshi19.github.io/incerto-wiki/karamata/ | imported (adapted) |
| 4 | `content/concepts/theorems/pareto-moment-existence.md` | `incerto-pareto-moment-existence` | https://xshi19.github.io/incerto-wiki/pareto-moment-existence/ | imported (adapted) |
| 5 | `content/concepts/theorems/mean-excess-function.md` | `incerto-mean-excess-function` | https://xshi19.github.io/incerto-wiki/mean-excess-function/ | imported (adapted) |
| 6 | `content/concepts/methods/hill-estimator.md` | `incerto-hill-estimator` | https://xshi19.github.io/incerto-wiki/hill-estimator/ | imported (adapted) |
| 7 | `content/concepts/methods/extreme-value-index.md` | `incerto-extreme-value-index` | https://xshi19.github.io/incerto-wiki/extreme-value-index/ | imported (adapted) |
| 8 | `content/concepts/distributions/generalized-pareto.md` | `incerto-generalized-pareto` | https://xshi19.github.io/incerto-wiki/generalized-pareto/ | imported (adapted) |
| 9 | `content/concepts/methods/plug-in-tail-estimation.md` | `incerto-plug-in-tail-estimation` | https://xshi19.github.io/incerto-wiki/plug-in-tail-estimation/ | imported (adapted) |

All nine are wired beneath `content/incerto.md`, after the original counting
example. The hub was extended without importing the wiki home body.

### Why these nine

Coherent reading path: Pareto → regular variation → Karamata / moment existence / mean excess → Hill / EVI → GPD → plug-in estimation. All are owner-authored concept pages (MIT owner decision; retained notices). High value for the Incerto track sample already promised in Phase 0 CSVs.

### Explicitly out of Batch 1

| Item | Reason |
| --- | --- |
| `reading-guides/taleb-scoft/*` (incl. intro already in CSV) | Copyright-sensitive paraphrase / router to SCoFT; **separate rights review** before any public import |
| Empirical examples (`sp500-tail`, `amazon-bookrank`, `nyc-dog-name-tail`, …) | Data provenance under `data/`; rights + fixtures |
| `normal-mixture`, `variance-gamma` | Overlap Normix theory boundary; schedule with Normix theory batch |
| `dependency-dag.md` + `assets/graphs/*` | Custom iframe / JS; not needed for first math pages |
| Full wiki `index.md`, API ref, Lean blueprint | Navigation / package / formalization boundaries |
| Vendoring `incerto/` JAX-free NumPy package wholesale | See Python boundary |

## Python package boundary

- **Do not** vendor `incerto` package or any Normix/JAX code into `xshi-math`.
- Wiki code-cells use `from incerto.distributions / estimators / figures …`.
  The owner authorized static formulas and narrative when adapting these cells;
  this batch uses that option. Static figures from a separate rebuild or thin
  NumPy demos in `xmath` + `demos/incerto/` remain possible later additions.
- Add helpers only for computation actually reused by notes or demos (e.g.
  `pareto_type1`, Hill, or `pareto_mean_plugin`). No second Normix implementation.

## Adapt checklist (applied to this batch)

1. Copy sanitized Markdown only (no private git history).
2. Rewrite relative links → MyST labels / flat stems; drop links to deferred pages or mark “planned”.
3. Replace executable cells with static math and tables; no `incerto.*` imports
   or notebook execution remain. Helpers can be introduced later for actual reuse.
4. Preserve `(label)=` / `:label:` IDs used in url fragments where possible.
5. Align frontmatter: drop conflicting CC-BY site metadata; keep concept `options` if useful; site license stays MIT.
6. Add all nine TOC entries and update both CSVs with imported targets and local
   verification, while leaving live compatibility routes pending.
7. Retain copyright notice `(c) 2023 xshi19` + MIT permission text in `THIRD_PARTY_NOTICES.md` / page provenance.

## Import gate outcomes

| Original concern | Batch 1 outcome |
| --- | --- |
| License notices | MIT site setting retained. Full upstream notice appears in `THIRD_PARTY_NOTICES.md` and all nine page sources/rendered pages. No external figures or substantial quotations were included. |
| Executable cells | Replaced with static calculations and tables. No Python helper, package, JAX, or plotting dependency was added. |
| Deferred cross-links | Imported targets use flat stems; other targets are plain-text planned mentions. Notation needed for each page is defined locally. |
| KaTeX / MyST | Strict build and extended HTML checker pass for all 21 pages. All 27 explicit source labels are retained and present in rendered HTML. |
| Bibliography | Bibliographic keys became attributed year/DOI links, with publisher links where needed; no shared bibliography was copied. An unavailable van der Vaart DOI metadata lookup was replaced with the publisher's book page. |
| Phase 1 / IG prerequisite | Existing local gate and IG batch were already present in this checkout. |
| Data | No external data or snapshots were needed or copied. |

The numerical plots and repeated-sample performance tables are deferred. Their
former labels now identify the corresponding static explanations. The imported
proofs keep their scope: Karamata's integral theorem and general limit theorems
remain cited results; local derivations are ordinary mathematical arguments,
not claims of checked Lean formalization.

No Batch 1 build blocker remains. Theme pinning, full legacy route rehearsal,
rights review for further imports, hub assembly, and public deployment remain
later gates; details are in the verification record.

## Non-goals (this batch)

- Full Incerto tree import; SCoFT chapter guides; hub cutover / compatibility pages live deploy.
- Opening a PR, committing, or pushing; the owner handles later Git publication.
- Merging private history; vendoring Normix.

## Delivered change shape

1. Retained notices and static examples; `xmath` and demos unchanged.
2. Nine adapted pages + TOC under `incerto.md`.
3. Manifest/url-map updates, plan status, and a verification record; local MyST
   build and HTML checks cover the full 21-page site.

## Survey counts (reference)

- Distributions 8 · theorems 9 · methods 8 · examples 5 · SCoFT guides 6 · external guides 2.
- Batch 1 = **9** pages (~2.3k lines source); full concept body ~8k lines — do not attempt in one PR.
