# Rule Index

Status: routing stub. No standalone rule bodies or Cursor adapters have been
installed. The repository remains a planning workspace with an adopted MIT
license and active Codex project defaults.

For now, use these existing sources:

| Task | Canonical guidance |
| --- | --- |
| Documentation changes and current completion checks | [Root agent router](../../AGENTS.md#completion-in-the-current-phase) |
| Repository and publishing boundaries | [Consolidation plan](../plan/consolidation.md#repository-boundaries) |
| Guidance placement and maintenance | [Agent framework](../design/AGENT_FRAMEWORK.md) |
| Source rights and public-release review | [License advice](../design/LICENSE_ADVICE.md) |
| Future task completion contracts | [Verification contracts](../design/AGENT_FRAMEWORK.md#verification-contracts) |

Create a rule body only when implementation or repeated friction requires it.
Likely first subjects are mathematical writing, reproducible computation, and
publication/source handling. A future rule needs a trigger, a small set of
project-specific constraints, and a way to assess compliance. Its canonical
body belongs here; a Cursor `.mdc` adapter may add activation metadata and a
pointer, but must not duplicate policy.

When extracting a policy from a design document, leave rationale and a link in
the design rather than maintaining two normative versions. Skills refer to
rules and own the workflow steps. Neither rules nor skills replace executable
verification when a constraint can be checked mechanically.
