# Phase 2 — Incerto Batch 2 (executed)

Status: **nine pages imported and adapted; execution complete locally**.
Strict build and the 38-page HTML check pass; see the
[verification record](../records/phase-2-batch-2-verification.md).
Changes are uncommitted; public cutover and further imports remain planned.
Date: 2026-09-12 (ET) / 2026-09-13 UTC.
Source checkout: `/workspace/incerto-wiki` @ pin
`9717c9cf83aee18b47f423a14bce2f0d14bb8bcb` (merge PR #53 / plug-in-tail).
**`content/` matches the requested pin**. The inspected checkout tip is
`0bb63be`, ahead only in planning documents; the import used the pinned blobs.
Execution scope: write only under `/workspace/xshi-math`; read the pinned
Incerto sources without modifying their checkout. Normix Theory Batch 1 is
already merged (PR #7); its content pages remain unchanged.

## Goal

Second PR-sized import into `xshi-math` for `/math/incerto*`: owner-written
concept / method / theorem pages that close the EVT (POT ↔ block-maxima) loop
and the one-big-jump / diagnostic spine left open after Batch 1. Defer Taleb
SCoFT reading guides (rights). Defer data-heavy empirical examples (or park in
a separate examples batch with explicit data-rights notes). Defer
normal-mixture / variance-gamma pending Normix theory coordination.

## Batch 1 already imported (do not re-list as work)

| Stem | Source |
| --- | --- |
| `incerto-pareto` | `concepts/distributions/pareto.md` |
| `incerto-regular-variation` | `concepts/theorems/regular-variation.md` |
| `incerto-karamata` | `concepts/theorems/karamata.md` |
| `incerto-pareto-moment-existence` | `concepts/theorems/pareto-moment-existence.md` |
| `incerto-mean-excess-function` | `concepts/theorems/mean-excess-function.md` |
| `incerto-hill-estimator` | `concepts/methods/hill-estimator.md` |
| `incerto-extreme-value-index` | `concepts/methods/extreme-value-index.md` |
| `incerto-generalized-pareto` | `concepts/distributions/generalized-pareto.md` |
| `incerto-plug-in-tail-estimation` | `concepts/methods/plug-in-tail-estimation.md` |

Also present (original, not wiki import): `incerto-counting-exceedances`, hub
`incerto.md`. Batch 1 adaptation pattern to reuse: flat stems, static math (no
`incerto.*` execute), local notation, MIT notices, plain-text “planned”
mentions for deferred targets.

## Source survey residual (`incerto-wiki/content/` @ 9717c9c)

| Area | Remaining after Batch 1 | Batch 2? |
| --- | --- | --- |
| `concepts/distributions/` | 6 left (GEV, Frechet, double-pareto, normal-mixture, VG, tail-class-catalog) | **3** (GEV, Frechet, double-pareto) |
| `concepts/theorems/` | 5 left (pickands, subexponentiality, Cramér, GCLT, LLN failure) | **2** (pickands, subexponentiality) |
| `concepts/methods/` | 5 left (threshold, BST, survival-tail-ratio, max-to-sum, iso-density) | **4** (threshold, BST, survival-tail-ratio, max-to-sum) |
| `concepts/examples/` | 5 | **defer** → examples batch + data rights |
| hubs (`*-concepts.md`, `dependency-dag.md`) | 5 | **defer** (DAG needs `assets/graphs/`) |
| `reading-guides/taleb-scoft/*` | 6 | **defer — rights** |
| `reading-guides/external/*` | 2 | defer |
| notation / glossary / bib | — | later shared-refs batch |
| api / Lean / releases / zh-cn | — | stay / exclude |

## Batch 2 pages (9)

MyST flat stems under `content/<stem>.md`; public slugs `/math/<stem>`.
Approximate source size: **~2.3k lines** (same order as Batch 1).

| # | Source path | Stem → `content/<stem>.md` | Legacy URL | Disposition |
| --- | --- | --- | --- | --- |
| 1 | `content/concepts/theorems/pickands-balkema-de-haan.md` | `incerto-pickands-balkema-de-haan` | https://xshi19.github.io/incerto-wiki/pickands-balkema-de-haan/ | imported |
| 2 | `content/concepts/distributions/generalized-extreme-value.md` | `incerto-generalized-extreme-value` | https://xshi19.github.io/incerto-wiki/generalized-extreme-value/ | imported |
| 3 | `content/concepts/distributions/frechet.md` | `incerto-frechet` | https://xshi19.github.io/incerto-wiki/frechet/ | imported |
| 4 | `content/concepts/theorems/subexponentiality.md` | `incerto-subexponentiality` | https://xshi19.github.io/incerto-wiki/subexponentiality/ | imported |
| 5 | `content/concepts/methods/survival-tail-ratio.md` | `incerto-survival-tail-ratio` | https://xshi19.github.io/incerto-wiki/survival-tail-ratio/ | imported |
| 6 | `content/concepts/methods/max-to-sum-ratio.md` | `incerto-max-to-sum-ratio` | https://xshi19.github.io/incerto-wiki/max-to-sum-ratio/ | imported |
| 7 | `content/concepts/distributions/double-pareto.md` | `incerto-double-pareto` | https://xshi19.github.io/incerto-wiki/double-pareto/ | imported |
| 8 | `content/concepts/methods/tail-threshold-selection.md` | `incerto-tail-threshold-selection` | https://xshi19.github.io/incerto-wiki/tail-threshold-selection/ | imported |
| 9 | `content/concepts/methods/body-shoulder-tail.md` | `incerto-body-shoulder-tail` | https://xshi19.github.io/incerto-wiki/body-shoulder-tail/ | imported |

Supporting updates extend the TOC and `content/incerto.md` with a second
reading path, add `migration-manifest.csv` / `url-map.csv` rows and notices,
and extend the HTML checker to all 38 current pages.

### Why these nine

Two coherent paths that Batch 1 left incomplete:

1. **EVT closure (POT ↔ maxima):** Pickands–Balkema–de Haan justifies GPD
   excesses already imported; GEV is the block-maxima limit family; Frechet is
   the heavy-tail GEV member tied to regular variation / Pareto-type.
   Threshold selection is the practical tuning step plug-in estimation already
   points at.
2. **One-big-jump / diagnostics:** Subexponentiality is the asymptotic
   one-big-jump class; survival-tail-ratio and max-to-sum are finite-sample /
   geometric diagnostics; double-Pareto gives a two-sided power-tail
   distribution used in demos; body-shoulder-tail is the mixture-shoulder
   diagnostic used alongside threshold choice.

All are owner-authored concept pages (same MIT import decision as Batch 1).
No Taleb chapter routers. No committed or cached market/index datasets
required if demos stay synthetic / static (Batch 1 pattern).

### Source line counts (pre-adaptation reference)

| Page | Lines | `{code-cell}` count (approx) |
| --- | ---: | ---: |
| pickands-balkema-de-haan | 237 | 1 |
| generalized-extreme-value | 186 | 2 |
| frechet | 217 | 1 |
| subexponentiality | 468 | 2 |
| survival-tail-ratio | 177 | 1 |
| max-to-sum-ratio | 230 | 1 |
| double-pareto | 247 | 3 |
| tail-threshold-selection | 300 | 1 |
| body-shoulder-tail | 264 | 1 |
| **Total** | **~2326** | **~13** |

### Soft dependencies (planned mentions, not Batch 2 pages)

| Deferred target | Why mentioned from Batch 2 |
| --- | --- |
| `lln-failure` | max-to-sum cites LLN failure under infinite mean |
| `lln-preasymptotic` (example) | max-to-sum / GCLT path; data-light but still an example page |
| `normal-mixture` | body-shoulder-tail `depends_on`; Normix overlap |
| `tail-class-catalog` | survival-tail / subexp “related”; large catalog hub |
| `iso-density-tail-geometry` | natural follow-on after survival-tail + subexp |
| `sp500-tail` | pickands / threshold pages link it; **data rights** |

Deferred links became plain-text “planned” mentions. The normal-mixture
reference points to the complementary `normix-normal-mixtures` note. No
deferred target was imported.

## Explicitly out of Batch 2

| Item | Reason |
| --- | --- |
| `reading-guides/taleb-scoft/*` | **Rights review** — do not import |
| Empirical examples (`sp500-tail`, `amazon-bookrank`, `nyc-dog-name-tail`, `dispersion-ratio`, `lln-preasymptotic`) | Data / fixtures; see **Examples batch** below |
| `normal-mixture`, `variance-gamma` | Overlap Normix Theory Batch 1 (`normix-normal-mixtures`, GH/VG family). Schedule a coordinated Normix↔Incerto mixtures pass; do not duplicate Normix narrative here |
| `tail-class-catalog` | Catalog hub (~451 lines); better after subexp is live (Batch 3 candidate) |
| `iso-density-tail-geometry` | Depends on survival-tail + subexp; Batch 3 |
| `cramer-condition`, `generalized-central-limit-theorem`, `lln-failure` | Next theorems cluster (thin-tail contrast / stable limits / LLN) |
| hubs `*-concepts.md`, `dependency-dag.md` + `assets/graphs/*` | Nav / iframe JS; not needed for math page PR |
| Full wiki home, API ref, Lean, zh-cn | Boundaries unchanged |
| Vendoring `incerto/` package | Same Python boundary as Batch 1 |

## Proposed examples batch (separate; not Batch 2)

When scheduling a later **Incerto examples** PR, keep rights notes explicit:

| Example | Data note |
| --- | --- |
| `amazon-bookrank` | Small CC0 Kaggle snapshot may be redistributed (`data/snapshots/amazon_bookrank_2001.csv`) |
| `nyc-dog-name-tail` | Public NYC Dog Licensing aggregate snapshot; record access/refresh date |
| `sp500-tail` | **Do not commit** S&P cache; FRED/S&P Dow Jones redistribution restrictions; page must degrade without cache |
| `dispersion-ratio`, `lln-preasymptotic` | Prefer synthetic; no external snapshot required if cells stay static |

Do not mix examples into the Batch 2 concept PR.

## Python package boundary

Unchanged from Batch 1:

- **Do not** vendor `incerto` or Normix/JAX into `xshi-math`.
- Prefer static formulas / tables (owner-authorized Batch 1 pattern). Optional
  later: thin NumPy helpers only for reused demos under `demos/incerto/`.
- No second Normix implementation via Incerto mixture pages.

## Applied adaptation checklist

1. Copy sanitized Markdown only (no private git history); pin source revision
   `9717c9c`.
2. Rewrite relative links → flat `incerto-*` stems for Batch 1+2 targets;
   deferred targets → plain-text planned mentions.
3. Replace `{code-cell}` / `incerto.*` with static math/tables; disable execute.
4. Preserve `(label)=` / `:label:` IDs used in URL fragments where possible.
5. Align frontmatter: drop conflicting CC-BY site metadata; keep useful
   `options.concept` metadata if desired; site license stays MIT.
6. Extend `incerto.md` TOC with EVT + diagnostics sections; update
   `migration-manifest.csv` + `url-map.csv`.
7. Retain `(c) 2023 xshi19` + MIT permission text in `THIRD_PARTY_NOTICES.md`
   and page provenance.
8. Cite lightly (year/DOI/publisher links) unless a shared bib lands in the
   same PR — Batch 1 style.

## Resolved execution gates

1. **Workspace and Normix:** Normix Theory Batch 1 is merged. This import writes
   only to `xshi-math` and leaves Normix content pages unchanged.
2. **Notices:** all nine pages retain the 2023 copyright and full MIT notice.
   No external figures, datasets, or substantial scholarly quotations were copied.
3. **Static content:** all 13 executable cells became static math, tables, or
   arguments. No package implementation or execution dependency was imported.
4. **Cross-links:** imported targets use flat stems; deferred examples, LLN
   notes, catalog, geometry, notation, and guides remain planned mentions.
5. **Mixture boundary:** body/shoulder/tail retains its local diagnostic and
   links to the existing Normix note for the conditional mixture construction.
6. **MyST and KaTeX:** strict HTML build and the extended 38-page checker pass;
   all 13 explicit source labels are retained and rendered.
7. **References:** lightweight author/year, DOI, and publisher references
   replace bibliography keys. No shared bibliography was introduced.
8. **Data and publication:** no data files, private history, commit, PR, push,
   or deployment is part of this execution.

See the verification record for checks actually run and remaining publication
limits. Legacy compatibility pages and historic fragment behavior still need
the later cutover review.

## Non-goals (this batch)

- Importing SCoFT guides, examples, mixture/VG pages, catalog hub, or DAG.
- Opening a PR / committing / pushing from this planning workspace.
- Merging private history; vendoring Normix or `incerto` package.

## Delivered change shape

1. Notices and pure static adaptations; no Python helpers added.
2. Nine adapted pages + TOC extension under `incerto.md` (EVT section +
   diagnostics section; keep Batch 1 spine intact).
3. Manifest / url-map updates; local MyST strict HTML + math checks covering
   new pages with the existing site set.
4. Keep examples and Normix-overlap pages out of the same PR.

Implemented TOC blocks under `incerto.md`:

- After Batch 1 plug-in: **Peaks over threshold & maxima** — Pickands → GEV →
  Frechet → threshold selection.
- **One-big-jump diagnostics** — Subexponentiality → survival-tail-ratio →
  max-to-sum → double-Pareto; body-shoulder-tail as mixture-shoulder diagnostic
  (with a link to the existing Normix normal-mixtures note).

## Survey counts (reference)

- Distributions 8 total · theorems 9 · methods 8 · examples 5 · SCoFT guides 6.
- Batch 1 imported **9**; Batch 2 imported **9** (~2.3k lines); residual
  concept body after Batch 2 ≈ LLN/GCLT/Cramér + iso-density + catalog +
  mixtures/VG + hubs + examples (~3.5k+ lines) — do not fold into this PR.

## Page count & path

- **Pages imported in Batch 2:** 9; total local site: 38
- **Plan file:** `docs/plan/phase-2-incerto-batch-2.md`
