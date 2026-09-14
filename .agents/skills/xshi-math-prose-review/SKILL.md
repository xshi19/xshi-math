---
name: xshi-math-prose-review
description: Review or rewrite user-facing xshi-math prose without changing its mathematical meaning. Use after claims and evidence are settled when creating or substantially editing notes, notation explanations, tutorials, figure commentary, public documentation, or when asked to remove AI-like writing patterns. Do not use as a substitute for math-content, proof, citation, or source review.
---

# xshi-math Prose Review

Run a final editorial pass after the content is mathematically settled. Remove
formulaic AI patterns while preserving every claim and its support.

## Inputs

- The prose to review and its page type / track.
- The intended reader and purpose of the passage.
- The settled statements, equations, notation, citations, and examples.

## Workflow

1. Read `docs/rules/mathematical-writing.md`. For register choice and AI-pattern
   scrubbing, also use `$xshi-math-unslop`.
2. Classify the passage as definition, theorem, proof, method, empirical
   example, figure commentary, or project documentation.
3. Lock the semantic contract before rewriting:
   - claims and conclusions;
   - hypotheses, quantifiers, domains, and limits;
   - notation and distinctions among technical terms;
   - citations and attribution;
   - whether support is a proof, computation, citation, empirical
     illustration, interpretation, or caveat.
4. Scan for the review signals in `docs/rules/mathematical-writing.md`. Treat
   them as contextual signals, not banned words.
5. Make the smallest rewrite that improves clarity. In tutorials and worked
   explanations, prefer first-person plural for choices and steps shared with
   the reader; state facts and mathematical claims directly. Preserve
   equations, MyST directives, labels, links, and citation keys unless the task
   includes changing them.
6. Audit the result claim by claim (broader certainty, lost assumptions,
   synonym drift, example-as-proof, formula restatement without mechanism).
7. Compare the diff. Run link, execution, or render checks when the edit touches
   structure, executable examples, labels, or interpretation of an output.

If the review exposes a mathematical, proof-scope, citation, or source problem,
stop the prose pass and use the applicable workflow before continuing.

## Completion Check

The prose review is not done until:

- mathematical meaning and evidentiary status are unchanged;
- assumptions, notation, confidence, and attribution remain visible;
- terminology is stable and precise;
- formulaic prose has been removed without manufacturing informality;
- any unresolved content issue or skipped verification is reported.
