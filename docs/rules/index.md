# Rule Index

Shared rule bodies live here. Skills under `.agents/skills/` own procedures;
thin `.cursor/rules/*.mdc` adapters (P1, not installed yet) may point here but
must not duplicate policy. See
[AGENT_FRAMEWORK.md](../design/AGENT_FRAMEWORK.md) and
[AGENT_HARNESS_MIGRATION.md](../design/AGENT_HARNESS_MIGRATION.md).

## Installed rule bodies

| Task | Canonical guidance |
| --- | --- |
| Mathematical prose, voice, AI-pattern signals | [mathematical-writing.md](mathematical-writing.md) |
| Cross-track symbol reuse (`/math/notation/`) | [shared-notation.md](shared-notation.md) |

## Other durable sources

| Task | Canonical guidance |
| --- | --- |
| Documentation changes and completion checks | [Root agent router](../../AGENTS.md#completion-in-the-current-phase) |
| Repository and publishing boundaries | [Consolidation plan](../plan/consolidation.md#repository-boundaries) |
| Guidance placement and maintenance | [Agent framework](../design/AGENT_FRAMEWORK.md) |
| Harness port decisions and day-to-day read order | [Harness migration](../design/AGENT_HARNESS_MIGRATION.md) |
| Source rights and public-release review | [License advice](../design/LICENSE_ADVICE.md) |
| Task completion contracts | [Verification contracts](../design/AGENT_FRAMEWORK.md#verification-contracts) |

## Skills (procedures)

Installed under `.agents/skills/` with the `xshi-math-` prefix. Route from
[AGENTS.md](../../AGENTS.md). Do not add a competing `.cursor/skills/` tree.

Create further rule bodies only when implementation or repeated friction
requires them. Likely later subjects: reproducible computation, and
publication/source handling. A rule needs a trigger, a small set of
project-specific constraints, and a way to assess compliance.
