# Planning Index

Status: design proposal; implementation has not started.
Source review date: 2026-09-12.

This planning set defines the repository and agent framework before any content
is imported. The agreed product boundary is a math monorepo with Incerto,
Information Geometry, and Normix theory tracks, published through the existing
personal hub. Normix remains an independent JAX package and API project.

## Reading map

| Document | Owns |
| --- | --- |
| [Consolidation](consolidation.md) | Proposed tree, what moves or stays, build and publishing boundaries, URL policy, migration phases, risks, v1 non-goals |
| [Agent framework](../design/AGENT_FRAMEWORK.md) | Guidance sources of truth, Codex/Cursor discovery, shared skills, adapters, verification contracts, maintenance |
| [License advice](../design/LICENSE_ADVICE.md) | License recommendation and alternative, source-license ambiguity, private-to-public review |
| [Rule index](../rules/index.md) | Current rule routes and intentionally deferred rule bodies |

The consolidation plan owns the proposed architecture until there is an actual
implementation. Add `ARCHITECTURE.md` when a working scaffold exists; it should
describe that implementation and link back to decisions, without duplicating the
roadmap. Proposed paths in code blocks are not a claim that files are present.

## Current deliverable

This change supplies the four planning/design documents, a README, a lean root
agent router, and a rule-index stub. It does not copy mathematical content,
install skills, create runtime configuration, change a license, or publish a
site. The optional Codex configuration is documented as a commented example
in the framework rather than activated.

Source review covered the two sibling agent design documents, their root
licenses, Incerto's MyST and Python metadata, Normix's documentation build
configuration, and current official client documentation. References and source
qualifications are recorded in the owning design documents. This is not a
complete content inventory or a review of all existing deployment workflows.

## Implementation sequence

The [one-time consolidation phases](consolidation.md#one-time-consolidation-phases)
define acceptance gates and rollback. All implementation phases remain pending:

- [ ] Phase 0: inventory public-eligible sources, licenses, dependencies, URLs,
  and existing hub publishers; settle the publication decisions.
- [ ] Phase 1: build and verify the minimal MyST/Python foundation with original
  sample material and shared agent routes.
- [ ] Phase 2: prepare the complete eligible import in a separate implementation
  change, with provenance and semantic checks.
- [ ] Phase 3: rehearse the combined hub artifact and every mapped legacy route.
- [ ] Phase 4: perform one coordinated public cutover and stop duplicate authoring.
- [ ] Phase 5: verify the live result and prune obsolete guidance and machinery.

“一次性全合” means one bounded consolidation and one canonical authoring source
after cutover. Preparation can use several reviewable changes. It does not mean
publishing private history or moving Normix's package into this repository.

## Decision queue

| Open question | Recommended starting point | Resolve before |
| --- | --- | --- |
| **Open question:** should the new site use `/math/` or `/xshi-math/`? | `/math/`, with explicit page slugs | Freezing the URL manifest |
| **Open question:** what do Incerto's MIT root license and CC-BY-4.0 site declaration each cover? | Establish ownership and intended scope; see [license advice](../design/LICENSE_ADVICE.md#source-license-ambiguity) | Any public import |
| **Open question:** adopt MIT for v1 or separate code/content licenses? | MIT for rights-cleared repository-owned material | Adding license text and publishing |
| **Open question:** which existing Incerto Python imports have outside consumers? | One internal helper package; compatibility only where an actual consumer needs it | Moving or renaming code |
| **Open question:** which hub publisher currently owns each output prefix? | Retain one coordinated deployment of the combined hub | Implementing artifact transfer |
| **Open question:** which Lean statement is a useful first exercise? | One small theorem linked to a note, with exact proof status | Starting optional formalization |

Update the owning document when a decision changes. This index tracks the next
step and its gate; it should not become another copy of the design.
