# Codex project config

This directory is for **project model defaults** only (see `config.toml`).

Do not add `.codex/rules/` or `.codex/skills/`. Codex discovers:

- standing guidance from root and nested `AGENTS.md`;
- repo skills from `.agents/skills/`;
- optional custom agents from `.codex/agents/` if we ever need them.

Rationale: [docs/design/AGENT_FRAMEWORK.md](../docs/design/AGENT_FRAMEWORK.md).
