# Phase 2 — Incerto Batch 3

Status: **imported / executed** — eight pages adapted or rewritten in
`xshi-math`. See the
[verification record](../records/phase-2-batch-3-verification.md): standard
`npm run build` and `npm run check:html` pass for **46** pages.
Date: 2026-09-12 (ET) / 2026-09-13 UTC.
Source checkout: `/workspace/incerto-wiki` @ pin
`9717c9cf83aee18b47f423a14bce2f0d14bb8bcb` (merge PR #53 / plug-in-tail).
**`content/` matches the pin** (surveyed blobs at that revision). Batches 1+2
imported **18** adapted concept stems before this batch, plus originals
(`incerto.md`, `incerto-counting-exceedances`).

## Goal

Third PR-sized import into `xshi-math` for `/math/incerto*`: close the remaining
owner **theorem / method / distribution / hub** pages that Batches 1–2 left open
— especially the thin-tail / infinite-mean / stable-limit cluster (Cramér, GCLT,
LLN-failure), the last diagnostic method (iso-density), the tail-class catalog,
and the three lightweight concept hubs that become useful once the body pages
are live.

**Hard exclusions (unchanged):**

| Item | Reason |
| --- | --- |
| `reading-guides/taleb-scoft/*` | **Rights review** — do not import |
| Empirical examples (`sp500-tail`, `amazon-bookrank`, `nyc-dog-name-tail`, `dispersion-ratio`, `lln-preasymptotic`) + `empirical-example-concepts.md` | Separate **examples** batch + data rights |
| `normal-mixture`, `variance-gamma` | **Normix owns** the mixture / GH–VG narrative (`normix-normal-mixtures`, GIG/GH/EM Batch 1). Do not duplicate |
| `dependency-dag.md` + `assets/graphs/*` | iframe / JS graph; keep deferred (or a later nav PR) |
| notation / glossary / bib / wiki home / API / Lean / releases / zh-cn | Shared-refs or stay upstream |

## Batches 1+2 already imported (do not re-list as work)

### Batch 1 (9)

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

### Batch 2 (9)

| Stem | Source |
| --- | --- |
| `incerto-pickands-balkema-de-haan` | `concepts/theorems/pickands-balkema-de-haan.md` |
| `incerto-generalized-extreme-value` | `concepts/distributions/generalized-extreme-value.md` |
| `incerto-frechet` | `concepts/distributions/frechet.md` |
| `incerto-subexponentiality` | `concepts/theorems/subexponentiality.md` |
| `incerto-survival-tail-ratio` | `concepts/methods/survival-tail-ratio.md` |
| `incerto-max-to-sum-ratio` | `concepts/methods/max-to-sum-ratio.md` |
| `incerto-double-pareto` | `concepts/distributions/double-pareto.md` |
| `incerto-tail-threshold-selection` | `concepts/methods/tail-threshold-selection.md` |
| `incerto-body-shoulder-tail` | `concepts/methods/body-shoulder-tail.md` |

Also present (original): `incerto-counting-exceedances`, hub `incerto.md`.

## Source survey residual (`incerto-wiki/content/` @ 9717c9c)

| Area | Remaining after Batches 1+2 | Batch 3? |
| --- | --- | --- |
| `concepts/theorems/` | 3 left (Cramér, GCLT, LLN-failure) | **3** |
| `concepts/methods/` | 1 left (iso-density-tail-geometry) | **1** |
| `concepts/distributions/` | 3 left (catalog, normal-mixture, VG) | **1** catalog only; mixture/VG → Normix |
| hubs (`*-concepts.md`, `dependency-dag.md`) | 5 | **3** thin TOC hubs; DAG deferred |
| `concepts/examples/` | 5 | **defer** → examples batch |
| `reading-guides/taleb-scoft/*` | 6 | **defer — rights** |
| `reading-guides/external/*` | 2 | defer |
| notation / glossary / bib / API / Lean / zh-cn | — | stay / later |

## Batch 3 pages (8)

MyST flat stems under `content/<stem>.md`; public slugs `/math/<stem>`.
Approximate source size: **~1.37k lines** body + **~64 lines** hubs
(~1.4k total; lighter than Batches 1–2). Cap satisfied (8 ∈ [8, 10]).

| # | Source path | Stem → `content/<stem>.md` | Legacy URL | Disposition |
| --- | --- | --- | --- | --- |
| 1 | `content/concepts/theorems/cramer-condition.md` | `incerto-cramer-condition` | https://xshi19.github.io/incerto-wiki/cramer-condition/ | **adapt** |
| 2 | `content/concepts/theorems/generalized-central-limit-theorem.md` | `incerto-generalized-central-limit-theorem` | https://xshi19.github.io/incerto-wiki/generalized-central-limit-theorem/ | **adapt** |
| 3 | `content/concepts/theorems/lln-failure.md` | `incerto-lln-failure` | https://xshi19.github.io/incerto-wiki/lln-failure/ | **adapt** |
| 4 | `content/concepts/methods/iso-density-tail-geometry.md` | `incerto-iso-density-tail-geometry` | https://xshi19.github.io/incerto-wiki/iso-density-tail-geometry/ | **adapt** |
| 5 | `content/concepts/distributions/tail-class-catalog.md` | `incerto-tail-class-catalog` | https://xshi19.github.io/incerto-wiki/tail-class-catalog/ | **adapt** |
| 6 | `content/concepts/theorem-concepts.md` | `incerto-theorem-concepts` | https://xshi19.github.io/incerto-wiki/theorem-concepts/ | **rewrite** (TOC hub → flat stems) |
| 7 | `content/concepts/method-concepts.md` | `incerto-method-concepts` | https://xshi19.github.io/incerto-wiki/method-concepts/ | **rewrite** (TOC hub → flat stems) |
| 8 | `content/concepts/distribution-concepts.md` | `incerto-distribution-concepts` | https://xshi19.github.io/incerto-wiki/distribution-concepts/ | **rewrite** (TOC hub; VG/mixture → Normix / planned) |

### Why these eight

1. **Thin-tail / sum contrast (must-have theorems):** Cramér states exponential-moment / large-deviation conditions that contrast the regularly varying / subexponential world already imported. GCLT classifies stable limits of normalized sums (Batch 2 max-to-sum and Pareto-moment pages already point here). LLN-failure under infinite mean closes the α≤1 story that max-to-sum and moment-existence cite as “planned”.
2. **Last diagnostic method:** Iso-density tail geometry is the remaining method page; it depends on survival-tail-ratio + subexponentiality (both live after Batch 2).
3. **Catalog hub:** Tail-class catalog (~451 lines) is the remaining high-value distribution page that is *not* Normix-owned; it organizes subexponential vs regularly varying examples once those theorems exist.
4. **Lightweight TOC hubs:** After all theorem/method/distribution body pages are imported (modulo Normix-owned mixtures), the three `*-concepts.md` lists become useful math-site indexes. Rewrite relative links to `incerto-*` stems; for VG / normal-mixture entries, link `normix-normal-mixtures` / GH family notes (or plain-text “planned”) — **do not import** those Incerto wiki pages.

### Source line counts (pre-adaptation reference)

| Page | Lines | `{code-cell}` (approx) |
| --- | ---: | ---: |
| cramer-condition | 200 | 1 |
| generalized-central-limit-theorem | 245 | 1 |
| lln-failure | 225 | 2 |
| iso-density-tail-geometry | 188 | 1 |
| tail-class-catalog | 451 | 2 |
| theorem-concepts | 22 | 0 |
| method-concepts | 21 | 0 |
| distribution-concepts | 21 | 0 |
| **Total** | **~1373** | **~7** |

### Soft dependencies (planned mentions, not Batch 3 pages)

| Deferred target | Why mentioned |
| --- | --- |
| `lln-preasymptotic` (example) | Natural companion to LLN-failure / GCLT; keep in examples batch |
| `normal-mixture` / `variance-gamma` (Incerto wiki) | Point to Normix stems instead |
| `dependency-dag` + graphs | Nav PR later |
| SCoFT reading guides | Rights |
| notation / glossary | Shared-refs batch |

## Explicitly out of Batch 3

| Item | Reason |
| --- | --- |
| `reading-guides/taleb-scoft/*` | Rights |
| All `concepts/examples/*` + `empirical-example-concepts.md` | Data / separate examples PR |
| `normal-mixture.md`, `variance-gamma.md` | Normix ownership |
| `dependency-dag.md` | iframe + `assets/graphs/` |
| External reading guides, Lean, API, zh-cn, releases | Boundaries unchanged |
| Vendoring `incerto/` package | Same Python boundary as Batches 1–2 |

## Python package boundary

Unchanged:

- **Do not** vendor `incerto` or Normix/JAX into `xshi-math`.
- Prefer static formulas / tables (Batches 1–2 pattern). Strip `{code-cell}` /
  `incerto.*` imports (~7 cells across body pages).
- No second mixture implementation via Incerto distribution pages.

## Executed adaptation checklist

1. Copy sanitized Markdown only; pin source revision `9717c9c`.
2. Rewrite relative links → flat `incerto-*` stems for Batches 1–3 targets;
   deferred / Normix-owned targets → plain-text planned mentions or absolute /
   relative Normix stems.
3. Replace `{code-cell}` with static math/tables; disable execute.
4. Preserve `(label)=` / `:label:` IDs used in URL fragments where possible.
5. Align frontmatter: drop conflicting site metadata; keep useful
   `options.concept` if desired; site license stays MIT.
6. Extend `incerto.md` TOC with a **sums / thin-tail contrast** section
   (Cramér → GCLT → LLN-failure) and attach iso-density under diagnostics;
   add catalog + the three concept hubs (or link hubs from the track home).
7. Retain `(c) 2023 xshi19` + MIT permission text in notices / provenance.
8. Update `migration-manifest.csv` + `url-map.csv`; extend HTML checker page set.

## Implemented TOC shape under `incerto.md`

- **Sums, stable limits, and thin-tail contrast** — Cramér → GCLT → LLN-failure.
- Extend **One-big-jump diagnostics** — add iso-density after survival-tail /
  max-to-sum / body-shoulder-tail.
- **Tail catalog & indexes** — tail-class-catalog; theorem / method / distribution concept hubs.

## Non-goals (this batch)

- Importing SCoFT guides, empirical examples, mixture/VG wiki pages, or the DAG.
- Opening a PR / committing / pushing; changes remain in the working tree.
- Merging private history; vendoring Normix or the `incerto` package.
- Executing the separate Normix Theory Batch 2 plan.

## After Batch 3 (residual concept body)

Owner concept/theorem/method/distribution pages from the wiki are now
**exhausted** on the math site except Normix-owned mixture/VG and the deferred
DAG/examples/SCoFT/shared-refs tracks. Next Incerto work is therefore an
**examples** PR (with data-rights notes), a **rights-reviewed SCoFT** decision,
or nav/DAG — not another concept dump of comparable size.

## Survey counts (reference)

- Distributions 8 · theorems 9 · methods 8 · examples 5 · SCoFT guides 6 · hubs 5.
- Batch 1 = **9**; Batch 2 = **9**; Batch 3 imported **8** (~1.4k lines).
- Cap: 8–10 pages — this batch uses **8**.

## Page count & path

- **Pages imported in Batch 3:** 8 (five body notes and three concept indexes)
- **Plan file:** `docs/plan/phase-2-incerto-batch-3.md`
