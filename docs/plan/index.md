# Planning Index

Status: Phase 0 light inventory and Phase 1 local HTML gate complete; IG outline
and first entry batch implemented; Phase 2 Incerto Batch 1 executed locally.
Source review date: 2026-09-13.

This planning set guides the foundation, approved imports, and later
consolidation. The agreed product boundary is a math monorepo with
Incerto, Information Geometry, and Normix theory tracks, published through the existing
personal hub. Normix remains an independent JAX package and API project.

## Reading map

| Document | Owns |
| --- | --- |
| [Light inventory](phase-0-inventory.md) | Representative source/URL records, inspected publisher behavior, unknowns, next gates |
| [Consolidation](consolidation.md) | Proposed tree, what moves or stays, build and publishing boundaries, URL policy, migration phases, risks, v1 non-goals |
| [Agent framework](../design/AGENT_FRAMEWORK.md) | Guidance sources of truth, Codex/Cursor discovery, shared skills, adapters, verification contracts, maintenance |
| [License advice](../design/LICENSE_ADVICE.md) | Adopted MIT scope, deferred alternative, Incerto import decision, private-to-public review |
| [IG entry outline](ig-entry-outline.md) | Implemented Basics / early IG pages, prerequisites, and the later GH/Normix research sequence |
| [Incerto Batch 1](phase-2-incerto-batch-1.md) | Executed nine-page import scope, adaptations, and deferred material |
| [Rule index](../rules/index.md) | Current rule routes and intentionally deferred rule bodies |

[ARCHITECTURE.md](../../ARCHITECTURE.md) describes the source scaffold now present.
The consolidation plan continues to own future boundaries and cutover gates.
Proposed paths in its target tree are not a claim that all files are present.

## Current deliverable

Phase 0 supplies a representative inventory and populated CSV samples. Phase 1
adds original track entries and sample explanations, shared CSS, pinned MyST
configuration, and the `xmath` Python package mapped to `src/math/`.

Python installation, six tests, the demo, and wheel import isolation passed in
the foundation checks. The pinned MyST HTML build and `check:html` now pass
locally with `BASE_URL=/math`; see the
[foundation verification record](../records/phase-0-1-verification.md).
The [owner curriculum](ig-entry-curriculum-draft.md) has been organized into the
[IG entry outline](ig-entry-outline.md), and the hub now links six original
Basics / early IG notes. Their checks and remaining publication limits are in
the [IG verification record](../records/ig-entry-verification.md).
The nine approved Incerto concept bodies have now been adapted under MIT; see
the [Batch 1 verification record](../records/phase-2-batch-1-verification.md).
No private history or Normix implementation was imported. No site
was deployed, CI configured, Lean project created, or agent skills installed.

## Implementation sequence

The [one-time consolidation phases](consolidation.md#one-time-consolidation-phases)
define acceptance gates and rollback. The light Phase 0 scope is complete;
full import coverage remains a later gate:

- [x] Phase 0 (light): inspect source/build/publisher configurations, record
  representative dispositions and URLs, and retain explicit unknowns. Full rights,
  consumer, and route coverage is required before import/cutover.
- [x] Phase 1 local HTML gate: the pinned `BASE_URL=/math` build and HTML
  checker pass. Foundation Python verification is recorded separately; hub
  assembly and public-host review remain later gates.
- [x] Start the IG outline and entry pages from the supplied owner curriculum:
  [outline and first batch](ig-entry-outline.md) implemented independently of
  Incerto import. Later marginalization and GH/Normix pages remain planned.
- [x] Phase 2 Batch 1: adapt the nine approved Incerto concepts with provenance,
  static calculations, semantic review, and local HTML checks.
- [ ] Phase 2 remainder: prepare further eligible imports in separate changes
  with provenance and semantic checks; Batch 1 does not complete this phase.
- [ ] Phase 3: rehearse the combined hub artifact and every mapped legacy route.
- [ ] Phase 4: perform one coordinated public cutover and stop duplicate authoring.
- [ ] Phase 5: verify the live result and prune obsolete guidance and machinery.

“一次性全合” means one bounded consolidation and one canonical authoring source
after cutover. Preparation can use several reviewable changes. It does not mean
publishing private history or moving Normix's package into this repository.

## Decision queue

Owner decisions recorded on 2026-09-12; `xmath` confirmed for this foundation:

| Resolved decision | Recorded outcome |
| --- | --- |
| Public base path | `/math/` is selected; `/xshi-math/` is not the canonical base. See [URL strategy](consolidation.md#url-strategy). |
| Repository license | MIT adopted for repository-owned material; root license and README statement added. MIT + CC-BY-4.0 is deferred, not chosen for v1. See [license advice](../design/LICENSE_ADVICE.md). |
| Incerto license ambiguity | Owner-controlled material will be published under MIT on import despite the MIT root / CC-BY-4.0 MyST declarations; preserve copyright notices and align future site metadata. Third-party rights still need inventory. See [source-license ambiguity](../design/LICENSE_ADVICE.md#source-license-ambiguity). |
| Internal Python directory | `src/math/` for one NumPy-based educational library, imported as owner-confirmed `xmath` through explicit setuptools mapping. See [Python naming](consolidation.md#python-import-name). |
| Hub | `xshi19.github.io` is the assembly and publishing boundary. See [repository boundaries](consolidation.md#repository-boundaries). |
| Agent model policy | Ask for a model before coding/exec work unless already named; Codex is primary and its project defaults are active. See [model selection](../../AGENTS.md#model-selection). |
| Information Geometry timing | Both prerequisites are met: the Phase 1 `/math` build passes and the owner curriculum is supplied. The outline and first entry batch are implemented; full Incerto migration is not a prerequisite. |

| Open question | Recommended starting point | Resolve before |
| --- | --- | --- |
| **Open question:** which existing Incerto Python imports have outside consumers? | One internal helper package; compatibility only where an actual consumer needs it | Moving or renaming code |
| **Open question:** which writer refreshes the hub trees, and which Pages site effectively owns each live prefix? | Source Pages publishers and hub dynamic Pages runs identified; transfer/root writer, Pages settings, and cross-repo coordination unknown. See [inventory](phase-0-inventory.md#hub-publishing-findings). | Implementing artifact transfer |
| **Open question:** which Lean statement is a useful first exercise? | One small theorem linked to a note, with exact proof status | Starting optional formalization |

Update the owning document when a decision changes. This index tracks the next
step and its gate; it should not become another copy of the design.
