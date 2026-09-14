# Deep-Math Report Archive

Convention for running or integrating a deep-math consultant report for
xshi-math. The consultant skill owns invocation; this directory owns artifact
naming.

## One stem per run

Store artifacts here using `YYYY-MM-DD-topic` as a shared stem. Add a suffix
such as `-retry-2` when prompt, context, or settings change; retain earlier
attempts and identify which produced the report being integrated.

| Suffix | Contents |
| --- | --- |
| `-prompt.md` | Exact research request supplied to the runner. |
| `-dry-run.txt` | Runner output from `--dry-run --output ...`, including resolved settings, context manifest, and skipped or truncated inputs. |
| `-report.md` | Unedited returned report from the successful run. |
| `-integration.md` | Actual run settings, findings accepted/rejected/deferred, verification evidence, and affected repository paths. |

The integration note should record the date, repository revision and relevant
uncommitted context, exact invocation (excluding secrets), model, reasoning
effort, output budget, verbosity, backend, and hosted-tool settings. Record
response ID and usage when available; mark unavailable information as unknown.
The dry run records intended settings, not evidence of a successful API call.

For each accepted finding, say what was checked and where the change landed.
Record rejected, already-covered, and uncertain findings explicitly. Do not
commit API keys, private inputs, restricted PDFs, or raw payload dumps.

## Capture the manifest before a call

From the repository root, after writing a focused prompt:

```bash
uv run python .agents/skills/xshi-math-deep-math-agent/scripts/run_deep_math_agent.py \
  --prompt-file docs/records/deep-math/YYYY-MM-DD-topic-prompt.md \
  --context content/incerto-subexponentiality.md \
  --no-web-search --dry-run \
  --output docs/records/deep-math/YYYY-MM-DD-topic-dry-run.txt
```

Inspect the manifest before an authorized paid run. Keep its prompt, context,
and model settings, remove `--dry-run`, and change `--output` to the report
path. A dry-run-only or failed attempt is not a completed report.

Skill:
[`.agents/skills/xshi-math-deep-math-agent/SKILL.md`](../../../.agents/skills/xshi-math-deep-math-agent/SKILL.md).

## Dependency note

`openai` / `openai-agents` may be absent from the hub environment. Install them
in the active Python env only when preparing a real run; the math site build
does not depend on them.
