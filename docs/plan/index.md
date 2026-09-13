# Planning Index

Status: owner decisions recorded; site, Python, and migration implementation pending.
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
| [License advice](../design/LICENSE_ADVICE.md) | Adopted MIT scope, deferred alternative, Incerto import decision, private-to-public review |
| [Rule index](../rules/index.md) | Current rule routes and intentionally deferred rule bodies |

The consolidation plan owns the proposed architecture until there is an actual
implementation. Add `ARCHITECTURE.md` when a working scaffold exists; it should
describe that implementation and link back to decisions, without duplicating the
roadmap. Proposed paths in code blocks are not a claim that files are present.

## Current deliverable

The repository contains the planning/design documents, README, root agent
router, and rule-index stub. This change records the owner's decisions, adopts
the root [MIT license](../../LICENSE), activates the requested
[Codex defaults](../../.codex/config.toml), and adds header-only migration and
URL CSV stubs. No mathematical content is imported, skills installed, MyST or
Python scaffold created, or site published.

The original planning source review covered the two sibling agent design documents, their root
licenses, Incerto's MyST and Python metadata, Normix's documentation build
configuration, and current official client documentation. References and source
qualifications are recorded in the owning design documents. This is not a
complete content inventory or a review of all existing deployment workflows.

## Implementation sequence

The [one-time consolidation phases](consolidation.md#one-time-consolidation-phases)
define acceptance gates and rollback. All implementation phases remain pending:

- [ ] Phase 0: inventory public-eligible sources, licenses, dependencies, URLs,
  and existing hub publishers; apply the adopted license and base path.
- [ ] Phase 1: build and verify the minimal MyST/Python foundation with original
  sample material and shared agent routes, using `BASE_URL=/math`.
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

Owner decisions recorded on 2026-09-12:

| Resolved decision | Recorded outcome |
| --- | --- |
| Public base path | `/math/` is selected; `/xshi-math/` is not the canonical base. See [URL strategy](consolidation.md#url-strategy). |
| Repository license | MIT adopted for repository-owned material; root license and README statement added. MIT + CC-BY-4.0 is deferred, not chosen for v1. See [license advice](../design/LICENSE_ADVICE.md). |
| Incerto license ambiguity | Owner-controlled material will be published under MIT on import despite the MIT root / CC-BY-4.0 MyST declarations; preserve copyright notices and align future site metadata. Third-party rights still need inventory. See [source-license ambiguity](../design/LICENSE_ADVICE.md#source-license-ambiguity). |
| Internal Python directory | `src/math/` for one NumPy-based educational library. Import naming remains open below. See [Python naming](consolidation.md#python-import-name). |
| Hub | `xshi19.github.io` is the assembly and publishing boundary. See [repository boundaries](consolidation.md#repository-boundaries). |
| Agent model policy | Ask for a model before coding/exec work unless already named; Codex is primary and its project defaults are active. See [model selection](../../AGENTS.md#model-selection). |
| Information Geometry timing | Start entry pages after the Phase 1 MyST build succeeds with `BASE_URL=/math`, once the owner supplies the concept list; full Incerto migration is not a prerequisite. |

| Open question | Recommended starting point | Resolve before |
| --- | --- | --- |
| **Open question:** confirm `xmath` as the import name for `src/math/`? | Explicit package configuration mapping `xmath` to `src/math/`; avoid shadowing stdlib `math`. Recommendation pending owner confirmation. | Phase 1 Python packaging |
| **Open question:** which existing Incerto Python imports have outside consumers? | One internal helper package; compatibility only where an actual consumer needs it | Moving or renaming code |
| **Open question:** which hub publisher currently owns each output prefix? | Retain one coordinated deployment of the combined hub | Implementing artifact transfer |
| **Open question:** which Lean statement is a useful first exercise? | One small theorem linked to a note, with exact proof status | Starting optional formalization |

Update the owning document when a decision changes. This index tracks the next
step and its gate; it should not become another copy of the design.
