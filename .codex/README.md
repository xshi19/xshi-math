# Codex project defaults

[config.toml](config.toml) actively selects `gpt-6-astra` with `xhigh` reasoning.
Follow the [owner model chooser](../AGENTS.md#model-selection) before coding or
command execution unless a choice is already named for the task or session.

Codex loads project configuration for trusted projects; command-line overrides
take precedence. See the [official configuration guide](https://developers.openai.com/codex/config-basic/).
Keep authentication, provider settings, and personal configuration in
`~/.codex/`, with no secrets in this repository. Environment permissions remain
controlled outside this project configuration.

Shared guidance belongs in [AGENTS.md](../AGENTS.md) and the
[agent framework](../docs/design/AGENT_FRAMEWORK.md). Canonical repository skills
will live only in `.agents/skills/` when needed; do not add `.codex/rules/` or
`.codex/skills/`.
