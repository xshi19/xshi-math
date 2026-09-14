---
name: xshi-math-deep-math-agent
description: Run a repo-local OpenAI consultant (GPT-5.5 pro by default) for difficult xshi-math work. Use when Codex needs an external deep technical report for hard proofs, EVT or fat-tail derivations, information-geometry or mixture-model notes, PDF/source synthesis, figure-aware analysis, or web-supported research before editing content/. Do not use for routine typo, link, or small prose fixes.
---

# xshi-math Deep Math Agent

Ask a deliberately scoped GPT-5.5 pro agent for a rigorous Markdown report,
then refine and integrate under ordinary xshi-math content skills.

## Prerequisites (honest)

- `OPENAI_API_KEY` in the environment for paid runs.
- Python package `openai` for direct Responses API runs
  (`uv pip install openai` or `python3 -m pip install openai` in the active env).
- `openai-agents` only when hosted tools are needed (web search, vector-store
  file search, or `--api-backend agents`).
- These packages are **not** required dependencies of the math hub itself; do
  not treat a missing install as a broken site. Document the gap and stop at
  dry-run if deps are absent.

## Delegate When

- The task needs sustained proof search, derivation, or theorem comparison.
- The answer should synthesize PDFs, papers, source pages, figures, or web
  research before editing notes.
- The user explicitly asks for GPT-5.5 pro, the OpenAI Agents SDK, or a deep
  external math consultant.
- The likely output is a report rather than a small copy edit.

For routine notation fixes, short prose edits, small link updates, or ordinary
note maintenance, use `$xshi-math-concept-page`, `$xshi-math-proof-writing`,
`$xshi-math-prose-review`, or `$xshi-math-math-question` directly.

## Archive layout

Store artifacts under `docs/records/deep-math/` using stem
`YYYY-MM-DD-topic` (see that directory's README). Suffixes:

| Suffix | Contents |
| --- | --- |
| `-prompt.md` | Exact research request |
| `-dry-run.txt` | `--dry-run` manifest |
| `-report.md` | Unedited successful report |
| `-integration.md` | Accepted/rejected/deferred findings + verification |

## Workflow

1. Read `docs/rules/mathematical-writing.md`,
   `docs/rules/shared-notation.md`, and any target note / track router.
2. Read `docs/records/deep-math/README.md`. Save the exact request as the run's
   `-prompt.md`.
3. Curate only needed context. Prefer specific files over broad directories.
   Include relevant notes, `content/notation.md`, PDFs, and figures.
4. Dry-run first. From the repo root:

   ```bash
   uv run python .agents/skills/xshi-math-deep-math-agent/scripts/run_deep_math_agent.py \
     --prompt-file docs/records/deep-math/YYYY-MM-DD-topic-prompt.md \
     --context content/incerto-subexponentiality.md \
     --no-web-search --dry-run \
     --output docs/records/deep-math/YYYY-MM-DD-topic-dry-run.txt
   ```

   If `openai` / `openai-agents` is missing, stop after documenting install
   steps; do not invent a report. For an authorized paid run, keep the same
   inputs, drop `--dry-run`, and write the matching `-report.md`. Enable web
   search when source discovery is part of the question.
5. Treat the report as advisory. Check proofs, citations, notation, and source
   claims before using it.
6. Integrate through `$xshi-math-concept-page`, `$xshi-math-proof-writing`,
   and/or `$xshi-math-reading-guide` as appropriate.
7. Record settings and accepted/rejected/deferred findings in
   `-integration.md`. Report what remains uncertain.

## Runner notes

- Defaults: model `gpt-5.5-pro`, reasoning effort `xhigh`, max output tokens
  `100000` (includes reasoning tokens). Override with flags or
  `XSHI_MATH_DEEP_MATH_MODEL`, `XSHI_MATH_DEEP_MATH_REASONING_EFFORT`,
  `XSHI_MATH_DEEP_MATH_MAX_OUTPUT_TOKENS`.
- Hosted web search is on by default; disable with `--no-web-search`.
- Direct Responses API is used when hosted tools are off; Agents SDK when web
  or hosted file search is requested.
- Background mode polls until terminal status; `--no-background` only for short
  checks.
- Fails loudly on incomplete/failed/empty visible output.
- PDFs upload as file inputs; images as vision; text inlined with size limits.
- Auto-included context when present: `AGENTS.md`,
  `docs/rules/mathematical-writing.md`, `docs/rules/shared-notation.md`,
  `content/notation.md` (there is no shared `content/bibliography.bib` yet).
- See `references/report_contract.md` for the expected report shape.

## Completion Check

- Prompt, dry-run manifest, successful report, and integration note are
  archived together; failed or dry-run-only attempts are clearly identified.
- Imported math claims have proof, computation, citation, or explicit caveat.
- Notation matches `content/notation.md`.
- Copyright-sensitive material is paraphrased and cited.
- Skipped API runs, missing deps, failed uploads, or unverified parts are named
  in the final response.
