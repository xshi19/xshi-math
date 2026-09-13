# Agent Framework Design

Status: design for a shared Codex and Cursor workflow.
Source review date: 2026-09-12.

The repository should give either client enough context to make a scoped change
and enough evidence to judge its completion. Durable knowledge lives in Git.
`AGENTS.md` routes work; rules express preferences and constraints; skills encode
repeatable procedures; executable checks enforce objective properties.

Use **one canonical skill tree at `.agents/skills/`**. Both Codex and Cursor can
discover it. Put shared rule bodies in `docs/rules/` and use thin
`.cursor/rules/*.mdc` adapters only where Cursor's activation metadata is useful.
The framework must remain usable with Codex alone: no task requires Cursor
quota, an editor-specific command, or a cross-provider review panel.

The root router, rule-index stub, and active [Codex project defaults](../../.codex/config.toml)
with a short [README](../../.codex/README.md) are present. The skill names,
adapters, and nested routers below remain proposed.

## Model selection policy

The owner's portfolio policy is to ask for a model before coding or command
execution unless a choice is already named for the task or session. The
[root router](../../AGENTS.md#model-selection) owns the chooser: Cursor Grok 4.6
xhigh, Cursor Fable 5.1 high, or Codex GPT-6-Astra xhigh. These are owner-selected
options, not a claim that every account has access.

Codex is primary and its project defaults are active. Cursor quota may be
exhausted, so the workflow must remain usable with Codex alone. Respect an
existing owner choice without asking again; if that model is unavailable,
report the limitation and ask for an alternative rather than silently switching.
Keep the chooser here and in the router, out of reusable skill bodies.

## Synthesis of the three approaches

| Source | Preserve | Adapt for this repository |
| --- | --- | --- |
| [Normix agent instructions design](https://github.com/xshi19/normix/blob/master/dev-notes/design/agent_instructions_design.md) | A short map, progressive disclosure, one owner per fact, rules as preferences, skills as recipes, mechanical enforcement, refinement after friction | Its historical `.cursor/rules` and `.cursor/skills` locations are source-project choices; use shared rule bodies and `.agents/skills` here |
| [Incerto agent framework](https://github.com/xshi19/incerto-wiki/blob/main/docs/design/AGENT_FRAMEWORK.md) (private) | Routing, context budget, verification as the completion criterion, local versioned memory, mathematical and bibliographic rigor, semantics-preserving prose review | Generalize track-specific procedures to the math monorepo; retain optional Lean and task-specific verification |
| Project-CC thin adapters, as supplied in the project brief | Canonical bodies under `guidelines/AI协作/模块/`, with small discovery adapters rather than copied policy | Preserve the separation of meaning from client metadata; use this repo's `docs/rules` and shared skills instead of recreating its multilingual module tree or three client skill trees |

The original planning review inspected the two sibling design documents through an authenticated GitHub
read after the requested `gh api` reads were unavailable in the authoring
environment. Their content blob IDs were respectively
`9d68744f122bd2891b08698102a4b471daf4f10d` and
`ab6f400c25d4ae346ec6cbbfc2dd8665626ac0f0`; these are blob IDs, not commit IDs.
The Project-CC layout is brief-supplied context, not an independently fetched
repository audit. Private source text is synthesized here rather than copied;
ordinary contributors should not need private-repository access to use this design.

The resulting rule is simple: separate policy from activation, but add an
adapter only when a discovery boundary actually requires one. Shared skill
discovery removes that boundary for Codex and Cursor.

## Discovery contract

The following behavior was checked against official documentation on the source
review date. Recheck it when upgrading clients; these are client capabilities,
not promises made by a directory name.

| Surface | Codex | Cursor | Repository decision |
| --- | --- | --- | --- |
| `AGENTS.md` | Builds a project instruction chain from root to starting working directory; nearer guidance specializes earlier guidance | Supports root and nested instructions | Keep a short root router; add local specialization only when needed |
| `.agents/skills/<name>/SKILL.md` | Discovers repository skills from working directory upward to the repository root | Discovers project skills here | Sole canonical location, at repo root initially |
| `.cursor/skills/` | Not the shared discovery contract | Also a project skill location | Do not create it, including as a symlink or mirror |
| `docs/rules/*.md` | Read through explicit routing | Read through routing or an adapter | Canonical shared rule bodies; ordinary Markdown is not automatically injected merely by being here |
| `.cursor/rules/*.mdc` | Do not rely on Codex reading these automatically | Supports rule metadata and scoped activation | Thin adapters, with no independent policy body |
| `.codex/config.toml` | Project defaults for trusted projects | Not shared client configuration | Active owner-selected model and reasoning defaults only |

Sources: [Codex instructions](https://developers.openai.com/codex/guides/agents-md/),
[Codex skills](https://developers.openai.com/codex/skills/),
[Codex configuration](https://developers.openai.com/codex/config-basic/),
[Cursor skills](https://cursor.com/docs/skills), and
[Cursor rules](https://cursor.com/docs/rules).

Codex checks `AGENTS.override.md` before `AGENTS.md` at a directory and includes
at most one instruction file there. A root-started session should explicitly
read applicable child guidance before editing a child area; do not assume that
opening a file recreates its startup instruction chain. Avoid checked-in
override files unless replacing the ordinary instruction file is intentional.
[Codex instruction discovery](https://developers.openai.com/codex/guides/agents-md/).

This repo deliberately has **no `.codex/rules/` or `.codex/skills/` trees**.
Optional role definitions may eventually live under `.codex/agents/`; they are
client configuration, not a new home for canonical rules or recipes. Compatibility
paths accepted by another client are not a reason to multiply sources of truth.

## Sources of truth

| Information | Canonical surface | What other surfaces should do |
| --- | --- | --- |
| Task routing and essential repo boundaries | Root `AGENTS.md` | Link to deeper guidance; avoid reproducing the full manual |
| Proposed repository architecture and cutover | `docs/plan/consolidation.md` | Reference its boundaries and phase gates |
| Implemented structure | [ARCHITECTURE.md](../../ARCHITECTURE.md) | Describe actual paths and dependency direction, linking to design rationale |
| Active phase and pending decisions | `docs/plan/index.md` | Update status without duplicating the design |
| Framework rationale | This document | Link to active rules/skills as they are introduced |
| Stable task constraints/preferences | `docs/rules/*.md` | Route directly or through a thin adapter |
| Ordered workflow and its completion criteria | `.agents/skills/<name>/SKILL.md` | Reference shared policy and actual verification entry points |
| Tool-specific activation | `.cursor/rules/*.mdc` | Own only description, globs, activation, and a pointer |
| Mathematical truth and evidence | Content pages, citations, executable sources, checked Lean declarations | Skills teach how to change these; they do not become another copy of them |
| Concrete verification commands | Actual project configuration or scripts, when implemented | Routers/skills name those entry points and the evidence expected |
| Durable decisions and resumable task state | Small records in `docs/design/`, `docs/plan/`, or future `docs/records/` | Link to sources/revisions; keep temporary chat and raw transcripts out |

A rule being promoted out of a design document should leave behind rationale
and a link, not a competing normative copy. A skill must not repeat the rule's
constraints. A client adapter must not repair a defect in the canonical rule
only for that client.

User instructions and the active task define the authorized work. A roadmap
item, recipe, or stale task record is context, not authorization to migrate,
publish, or broaden a task. Within the authorized scope, proceed with routine
reversible work without adding unnecessary approval steps.

## Progressive disclosure and nested routing

The root router gives identity, a task map, and the current completion standard.
As a local design heuristic, keep it around 50–80 useful lines. Its purpose is
to reduce the cost of finding context, not to consume the client's instruction
limit. Do not solve routine context bloat by increasing that limit.

A typical task loads:

1. The root router and applicable nested router.
2. The smallest relevant rule and, if a repeated procedure applies, one skill.
3. The source files, citations, or configuration needed to assess the change.
4. Broader design rationale only when the task changes a boundary or exposes an
   unresolved decision.

Do not load all three tracks, the license plan, the full roadmap, and every skill
for a spelling correction. Skill descriptions also have a context cost, so use
specific names and triggers rather than a catalog of broad “expert” roles.

Add `content/AGENTS.md` only when mathematical authoring needs a distinct route;
add `demos/AGENTS.md` for execution/output constraints and `lean/AGENTS.md` for
formalization status and toolchain checks when those areas exist. A track-specific
router is justified by a real difference, such as source-reading conventions,
not merely by having another directory. Each nested router points to shared
policy and records only the local difference. Keep skills in the single root
`.agents/skills/` tree for v1 to avoid working-directory-dependent availability.

## Thin adapters and symlinks

Prefer small checked-in adapters for Cursor rules. A future adapter might look
like this **after** `docs/rules/mathematical-writing.md` has been created:

```mdc
---
description: Apply shared mathematical writing constraints to content edits.
globs: "content/**/*.md"
alwaysApply: false
---
Read and apply the canonical rule before editing mathematical content:
@docs/rules/mathematical-writing.md
```

Cursor requires `.mdc` for project rules; a plain `.md` file in its rules directory
is ignored. Its documented file-reference syntax supports this pointer pattern.
Check the target exists and inspect the resolved rule context when validating an
adapter; do not assume any arbitrary Markdown link is automatically followed.
[Cursor rule format and references](https://cursor.com/docs/rules).

The adapter contains no alternate wording of the mathematical policy. Use
`alwaysApply: false` for task-scoped routes; the shared root `AGENTS.md` already
serves as the general entry point. Add more globs only when real work needs them.

| Approach | Advice |
| --- | --- |
| One shared `.agents/skills/` directory | Preferred: both clients use the same recipe without synchronization |
| `.cursor/skills` symlinked to `.agents/skills` | Avoid: both locations are discovered by Cursor; this reintroduces duplicate discovery paths |
| Copying the same `SKILL.md` into both trees | Avoid: creates two separately editable recipes and duplicate triggers |
| Symlinking a shared Markdown rule to a `.mdc` filename | Avoid: extension changes do not supply activation metadata; relative-reference behavior also needs checking |
| Thin `.mdc` file pointing to `docs/rules` | Preferred when scoped Cursor activation adds value |
| Generated rule adapters | Consider only after enough adapters exist to justify a generator and a drift check |
| Symlink for a controlled local setup | An opt-in convenience after checking checkout, discovery, and path resolution; not a prerequisite for collaborators |

Codex documents support for symlinked skill folders. That capability does not
make duplicate shared/client skill roots useful here.
[Codex skill locations](https://developers.openai.com/codex/skills/).

Project-CC's adapter pattern is useful where clients require different entry
surfaces. For this two-client design, recreating `.agents`, `.cursor`, and
`.claude` copies of each skill would discard the benefit of shared discovery.
Claude-specific integration is outside v1 scope.

## Verification contracts

Define completion against the changed artifact. A successful build is evidence
about rendering; it is not evidence that a theorem is true. A numerical plot is
an illustration unless the argument establishes more. A confident agent report
is not a substitute for either.

| Task | Minimum useful completion evidence | Availability |
| --- | --- | --- |
| Planning/design edit | Read changed and new files, check relative links and citations, separate current state from proposals, check whitespace and the actual diff | Current documentation workflow; `git diff --check` exists, but does not cover untracked files |
| Math page or reading guide | Assumptions, notation, claim scope, proof coverage, attribution, and bibliography reviewed; changed equations and links inspected in a rendered page | Content exists; pinned HTML build gate remains open |
| Python helper or numerical demo | Relevant behavior tests plus execution of the actual demo; known cases, units, seeds, data provenance, numerical tolerances, and generated figures checked | Current Python scaffold; see README for test and demo commands |
| MyST/CSS change | Pinned static build, changed pages viewed at desktop/mobile sizes, equations and navigation checked under the real base path | Site scaffold exists; HTML/rendered verification remains pending |
| Lean declaration | Build with the pinned toolchain; inspect assumptions and proof dependencies; map the exact checked statement to the informal claim | Optional future Lean project, using its actual `lake build` target |
| Guidance or skill change | Check pointers/metadata and unique names; try a representative trigger and a non-trigger; inspect the resulting diff or artifact | Metadata checks when files exist; client execution checks only in clients actually available |
| Public import or publication | Rights/provenance review of source and artifact, complete URL mapping, sibling-prefix preservation, recorded revision and rollback artifact | Future consolidation/publishing phases |

For numerical work, test a known limit, invariant, or independently justified
reference value rather than merely asserting that output matches the current
implementation. A heavy-tail simulation should not silently assume finite
moments or convert finite-sample behavior into an asymptotic theorem. Small
reversible prose edits do not require a new test suite.

For formalization, a successful build alone is insufficient if the target still
uses `sorry`, `admit`, or an unreviewed axiom. A claim labeled “checked” needs an
audited dependency path and a precise statement correspondence. Partial
formalizations remain explicitly partial; Lean is optional for other tracks.

Prose review is part of math review. Preserve hypotheses, quantifiers, notation,
confidence, attribution, and evidence type. Automation may flag broken labels,
missing citation keys, or suspicious prose patterns. It should not automatically
rewrite theorem statements, proofs, or surrounding mathematical qualifications.
Editorial warnings require judgment and counterexamples, not token bans.

This design document does not itself implement checks. The foundation now has
Python tests and configured site commands; see [README](../../README.md) for their
actual verification status. Lean, adapter checks, and CI remain deferred. Add
deterministic checks with the code they verify, run them locally, and only then
wire useful checks into CI. Do not add a workflow whose
commands refer to nonexistent files or whose success implies unperformed review.

## Starter skills

Start with the recipes that actual authoring repeats. These are candidates, not
an installed catalog:

| Candidate under `.agents/skills/` | Trigger and non-trigger | Output / completion |
| --- | --- | --- |
| `math-page` | Create or substantially revise a concept/tutorial/reading-guide page; skip a narrow typo fix or a math question that did not request an edit | Scoped page with sources, explicit claim/evidence status, links, and relevant rendering checks |
| `math-prose-review` | Final semantic review of substantial mathematical prose; skip code-only work and already settled small wording fixes | Concrete edits or findings preserving the mathematics, with any unresolved claim clearly identified |
| `numerical-demo` | Add or change a reproducible computation/visualization; skip a static link update | Executed demo, inspectable figures, dependency/input record, and meaningful numerical checks |
| `agent-guidance` | Repair a recurring routing failure, adapt a common workflow, or prune guidance after a phase | One canonical change, updated pointers, and evidence that the route helps without creating duplicate triggers |

Keep source-to-concept reading-guide steps within `math-page` at first; split
them out when that procedure becomes distinct and common. Add
`lean-formalization` only when Lean work starts, and `publish-site` only after
the publication path exists and has been rehearsed. A one-time migration can
remain a phase checklist instead of becoming a permanent skill.

Each implemented skill should contain:

- YAML `name` and a precise `description` identifying when to use it.
- Inputs and a non-trigger, plus links to the relevant canonical rules.
- A short procedure whose meaningful stages each have a checkable exit condition.
- The artifact to produce, actual verification entry points, and how to report
  skipped checks or unresolved evidence.
- A small gotchas section based on observed failures; supporting references or
  scripts only when they reduce repeated work.

For example, a math-page procedure first settles the claim and sources, then
drafts the explanation, verifies its evidence/rendering, and reviews prose for
semantic drift. It does not start by choosing a narrative and filling it with
plausible claims. Avoid editor slash-command syntax, fixed model names, local
transcript paths, or mandatory delegation in shared recipe bodies.

## Codex project configuration

Project defaults live in [`.codex/config.toml`](../../.codex/config.toml).
Codex loads these layers for trusted projects, with command-line overrides
taking precedence. Keep personal
settings in user configuration and follow any enforced environment policy.
[Official Codex configuration](https://developers.openai.com/codex/config-basic/).

The owner selected these active defaults:

```toml
model = "gpt-6-astra"
model_reasoning_effort = "xhigh"
```

The setting names are documented in the
[Codex configuration reference](https://developers.openai.com/codex/config-reference/).

Authentication and provider settings stay in the user's `~/.codex/`; do not put
secrets, personal absolute paths, canonical prose rules, or skill bodies in the
repository configuration. A configured default does not establish account access
or override the [model chooser](#model-selection-policy). Leave
permissions and sandbox controls to the user's environment; a repo default must
not be used to work around an execution restriction. Defer `.codex/agents/`
until a repeated bounded role needs it, and have that role reference shared
rules/skills instead of restating them.

## Local memory and client handoff

Record decisions with the problem, selected approach, reason, affected boundary,
and a link to evidence. A resumable task note needs scope, current revision,
completed work, actual verification results, unresolved questions, and the next
step. It does not need a transcript or private reasoning trace.

A Codex-to-Cursor or Cursor-to-Codex handoff should be possible from the branch
and those records. Recheck dirty files and the source revision before continuing;
do not trust an old “tests passed” sentence for new changes. If one client is
unavailable, complete and report the work possible with the other. Report a
client-specific discovery check as not run rather than presenting architectural
compatibility as a tested integration.

## Improve and prune from friction

Add guidance when a mistake recurs, a workflow becomes common, or a verification
failure exposes a missing contract. As a heuristic, repeating a procedure three
or more times is a reason to consider a skill, not a requirement to create one.

For each addition, record the observed failure and ask which intervention is
smallest: clearer structure, a deterministic check, a rule, or a recipe. Prefer
mechanical enforcement for objective constraints such as broken references or
duplicate skill names; retain human judgment for mathematical explanation.

After each consolidation phase, and whenever guidance becomes hard to navigate,
review unused triggers, duplicated policy, missing targets, stale commands, and
instructions superseded by tooling. Merge or remove them. Keep useful gotchas
near the workflow that encounters them. Prune details from the root router as
deeper routes become reliable.

The measure of success is fewer repeated errors and more checkable results with
less ambient context. A growing rules directory is not itself progress.
