# Deep Math Report Contract

Ask the external agent for Markdown only. The report should be useful to Codex
as an intermediate artifact, not treated as publish-ready hub prose.

## Required Sections

1. `# Report`
2. `## Executive Summary`
3. `## Problem Restatement`
4. `## Assumptions and Notation`
5. `## Source and Context Inventory`
6. `## Main Analysis`
7. `## Proofs or Derivations`
8. `## Computations or Checks`
9. `## Caveats and Failure Modes`
10. `## Suggested xshi-math Changes`
11. `## References`

## Rules

- Cite repository files by path.
- Cite PDFs by filename and page, section, theorem, or equation when available.
- Cite web sources with URLs and access dates when web search is used.
- Mark conjectural steps clearly.
- Do not include hidden chain-of-thought. Provide concise derivations, proof
  sketches, counterexamples, and verification steps instead.
- Do not reproduce copyrighted prose or figures from source PDFs.
- Prefer shared notation from `content/notation.md` when supplied; otherwise
  list notation differences explicitly.
