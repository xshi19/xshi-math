# xshi-math

Mathematical notes and tutorials, supported by Python visualizations and numerical
demos, with optional Lean formalization as a way to learn while using it.

The planned monorepo has three tracks:

- **Incerto / fat tails:** concepts, reading guides, and computational examples
  from the existing Incerto project, subject to a future public-release review.
- **Information Geometry:** new notes, tutorials, and numerical explorations.
- **Normix theory:** mathematical explanations and demos that use the separately
  maintained [normix package](https://github.com/xshi19/normix).

The publishing hub remains [xshi19.github.io](https://xshi19.github.io/), whose
[repository](https://github.com/xshi19/xshi19.github.io) hosts the existing
[Normix documentation](https://xshi19.github.io/normix/) and
[Incerto Wiki](https://xshi19.github.io/incerto-wiki/). The proposed math site uses
a shared MyST presentation with a Kami-like reading experience. Normix's JAX
implementation, public API, package releases, and API documentation stay in
`xshi19/normix`.

**Status:** planning and design only. This repository has no migrated wiki
content, configured site build, executable demos, Lean project, or CI workflow.

Start with the [planning index](docs/plan/index.md):

| Document | Purpose |
| --- | --- |
| [Consolidation plan](docs/plan/consolidation.md) | Repository boundaries, target tree, publishing, URLs, phases, and risks |
| [Agent framework](docs/design/AGENT_FRAMEWORK.md) | Shared guidance for Codex and Cursor, with one canonical skill tree |
| [License advice](docs/design/LICENSE_ADVICE.md) | MIT recommendation, the MIT/CC-BY alternative, and publication review |
| [Agent router](AGENTS.md) | Task-specific entry points and current verification expectations |

The proposed v1 license is MIT for repository-owned material, with explicit
third-party exceptions. This is a recommendation; no repository license has been
adopted by this planning change. The license advice also records conflicting
MIT and CC-BY-4.0 signals in the Incerto source configuration.
