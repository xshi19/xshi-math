# Planning Index

Status: Phase 0 light inventory complete; Phase 1 scaffold present, HTML gate open.
Source review date: 2026-09-13.

This planning set guides the foundation and later consolidation before any
source content is imported. The agreed product boundary is a math monorepo with
Incerto, Information Geometry, and Normix theory tracks, published through the existing
personal hub. Normix remains an independent JAX package and API project.

## Reading map

| Document | Owns |
| --- | --- |
| [Light inventory](phase-0-inventory.md) | Representative source/URL records, inspected publisher behavior, unknowns, next gates |
| [Consolidation](consolidation.md) | Proposed tree, what moves or stays, build and publishing boundaries, URL policy, migration phases, risks, v1 non-goals |
| [Agent framework](../design/AGENT_FRAMEWORK.md) | Guidance sources of truth, Codex/Cursor discovery, shared skills, adapters, verification contracts, maintenance |
| [License advice](../design/LICENSE_ADVICE.md) | Adopted MIT scope, deferred alternative, Incerto import decision, private-to-public review |
| [Rule index](../rules/index.md) | Current rule routes and intentionally deferred rule bodies |

[ARCHITECTURE.md](../../ARCHITECTURE.md) describes the source scaffold now present.
The consolidation plan continues to own future boundaries and cutover gates.
Proposed paths in its target tree are not a claim that all files are present.

## Current deliverable

Phase 0 supplies a representative inventory and populated CSV samples. Phase 1
adds original track entries and sample explanations, shared CSS, pinned MyST
configuration, and the `xmath` Python package mapped to `src/math/`.

Python installation, six tests, the demo, and wheel import isolation pass with
cached dependencies. The required pinned MyST HTML build is blocked by this
authoring environment's network and child-process restrictions; it is not marked
complete. See the [verification record](../records/phase-0-1-verification.md).
No wiki bodies, private history, or Normix implementation were imported. No site
was deployed, CI configured, Lean project created, or agent skills installed.

## Implementation sequence

The [one-time consolidation phases](consolidation.md#one-time-consolidation-phases)
define acceptance gates and rollback. The light Phase 0 scope is complete;
full import coverage remains a later gate:

- [x] Phase 0 (light): inspect source/build/publisher configurations, record
  representative dispositions and URLs, and retain explicit unknowns. Full rights,
  consumer, and route coverage is required before import/cutover.
- [ ] Phase 1: source scaffold and Python verification complete; the pinned
  `BASE_URL=/math` HTML build and rendered review still need a successful run.
- [ ] After Phase 1 builds: start Information Geometry entry pages from the
  owner's concept list; do not wait for the full Incerto import. **Pending
  input:** wait for the owner list; see [IG timing](consolidation.md#information-geometry-timing).
- [ ] Phase 2: prepare the complete eligible import in a separate implementation
  change, with provenance and semantic checks.
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
| Information Geometry timing | Start entry pages after the Phase 1 MyST build succeeds with `BASE_URL=/math`, once the owner supplies the concept list; full Incerto migration is not a prerequisite. |

| Open question | Recommended starting point | Resolve before |
| --- | --- | --- |
| **Open question:** which existing Incerto Python imports have outside consumers? | One internal helper package; compatibility only where an actual consumer needs it | Moving or renaming code |
| **Open question:** which writer refreshes the hub trees, and which Pages site effectively owns each live prefix? | Source Pages publishers and hub dynamic Pages runs identified; transfer/root writer, Pages settings, and cross-repo coordination unknown. See [inventory](phase-0-inventory.md#hub-publishing-findings). | Implementing artifact transfer |
| **Open question:** which Lean statement is a useful first exercise? | One small theorem linked to a note, with exact proof status | Starting optional formalization |

Update the owning document when a decision changes. This index tracks the next
step and its gate; it should not become another copy of the design.
