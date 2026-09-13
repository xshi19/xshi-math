# xshi-math

Mathematical notes and tutorials, supported by Python visualizations and numerical
demos, with optional Lean formalization as a way to learn while using it.

The planned monorepo has three tracks:

- **Incerto / fat tails:** concepts, reading guides, and computational examples
  from the existing Incerto project, subject to a future public-release review.
- **Information Geometry:** new notes, tutorials, and numerical explorations.
- **Normix theory:** mathematical explanations and demos that use the separately
  maintained [normix package](https://github.com/xshi19/normix).

The hub is the [xshi19.github.io repository](https://github.com/xshi19/xshi19.github.io),
the assembly and publishing boundary for the [personal site](https://xshi19.github.io/).
It hosts the existing
[Normix documentation](https://xshi19.github.io/normix/) and
[Incerto Wiki](https://xshi19.github.io/incerto-wiki/). The future math site will
use the owner-selected `/math/` base and a shared MyST presentation with a
Kami-like reading experience. Normix's JAX implementation, public API, package
releases, and API documentation stay in `xshi19/normix`.

**Status:** planning and design, with an adopted MIT license and active Codex
project defaults. This repository has no migrated wiki content, configured site
build, executable demos, Lean project, or CI workflow.

Start with the [planning index](docs/plan/index.md):

| Document | Purpose |
| --- | --- |
| [Consolidation plan](docs/plan/consolidation.md) | Repository boundaries, target tree, publishing, URLs, phases, and risks |
| [Agent framework](docs/design/AGENT_FRAMEWORK.md) | Shared guidance for Codex and Cursor, with one canonical skill tree |
| [License advice](docs/design/LICENSE_ADVICE.md) | Adopted MIT scope, deferred MIT/CC-BY alternative, and publication review |
| [Agent router](AGENTS.md) | Task-specific entry points and current verification expectations |

Repository-owned code, prose, figures, notebooks, Lean, and guidance are licensed
under [MIT](LICENSE). Third-party exceptions will be recorded in
`THIRD_PARTY_NOTICES.md` when needed; see the [adopted scope and Incerto import
decision](docs/design/LICENSE_ADVICE.md).
