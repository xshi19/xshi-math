# Roadmap

Maintainer: Xiang Shi
Last updated: 2026-09-12

This directory is the active planning surface for `xshi-math`. Design rationale
lives in `docs/design/`. This index tracks what to approve and execute next.

## Status

`xshi-math` is a **planning-only** public repo. No tutorial content, Python
packages, Lean projects, or site CI have been migrated yet.

The intended next move is one approved consolidation ("一次性全合"): scaffold
the monorepo, bring Incerto across after a private→public scrub, stub
Information Geometry, point or port Normix theory pages, then cut over public
URLs and archive the old site sources.

## Plans

| Doc | Purpose |
| --- | --- |
| [consolidation.md](consolidation.md) | Target layout, track model, migrate-vs-stay, hub deploy, URL strategy, sequenced phases, risks, v1 non-goals |
| [../design/AGENT_FRAMEWORK.md](../design/AGENT_FRAMEWORK.md) | Dual Codex + Cursor harness: single sources of truth, skills, rules, adapters vs symlinks, verification contracts |
| [../design/LICENSE_ADVICE.md](../design/LICENSE_ADVICE.md) | Public-repo license recommendation (default MIT) and citation/copyright gates |

## Execution order after approval

1. Decide license (`LICENSE` + short `NOTICE` / `CITATION.cff`). See
   [LICENSE_ADVICE.md](../design/LICENSE_ADVICE.md).
2. Execute [consolidation.md](consolidation.md) phases 0–7 as one coordinated
   program, not a long dual-site drip.
3. Grow agent skills and `.cursor/rules/*.mdc` adapters only as those phases
   create real workflows. See [AGENT_FRAMEWORK.md](../design/AGENT_FRAMEWORK.md).

## Not in this repo yet

Do not treat empty future paths (`tracks/`, `packages/`, `site/`) as present.
They are proposed in the consolidation plan and should be created during the
scaffold phase.
