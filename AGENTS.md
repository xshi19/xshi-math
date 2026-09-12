# Agent Router

This repository is currently a planning and design workspace for mathematical
notes, Python demos, and optional Lean. Read [README.md](README.md) for scope.
The files and commands described as proposed in the plans do not yet exist.

## Read only what the task needs

| Task | Read next |
| --- | --- |
| Roadmap, current phase, unresolved decisions | [Planning index](docs/plan/index.md) |
| Repository boundaries, tracks, URLs, deployment | [Consolidation plan](docs/plan/consolidation.md) |
| Agent instructions, rules, skills, client configuration | [Agent framework](docs/design/AGENT_FRAMEWORK.md) |
| Licensing, source reuse, private-to-public preparation | [License advice](docs/design/LICENSE_ADVICE.md) |
| Locate a task-specific rule | [Rule index](docs/rules/index.md) |

Before changing a subtree, inspect any more specific `AGENTS.md` along its path.
When working from the repo root, explicitly read applicable nested guidance;
do not assume a client has loaded instructions below its starting directory.

## Working boundaries

- Follow the user's task scope. A future phase in a plan is not an instruction
  to execute that phase. This planning task does not authorize content migration.
- Preserve the [Normix boundary](docs/plan/consolidation.md#repository-boundaries).
- Keep durable decisions in the repository. Use links to canonical guidance;
  load rules and recipes only for the task they govern.
- Canonical repository skills belong only in `.agents/skills/`. None are
  installed here yet. See the framework before adding a rule, skill, or adapter.
- Preserve assumptions, notation, attribution, and the distinction between
  proof and numerical evidence when editing mathematical prose.

## Completion in the current phase

Review the diff and the full contents of new files; `git diff` alone omits
untracked files. Check relative links, factual citations, scope, and consistency
between current state and proposals. Run `git diff --check` and check new files
for whitespace errors separately. No site, Python, or Lean test command is
configured in this repository yet.

Report changed files, verification actually performed, checks not run, and any
remaining limitations. Report Git state accurately; a written file is not a
commit, and a proposed verification contract is not passing CI.
