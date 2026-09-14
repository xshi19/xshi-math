# Mathematical Writing

Use these rules for user-facing explanatory prose in mathematical notes under
`content/`, notation explanations, figure commentary, and public-facing project
documentation. Apply them after the mathematical claims and evidence have been
settled. For the procedural prose pass, use `$xshi-math-prose-review`; for
AI-pattern scrubbing and registers, use `$xshi-math-unslop`.

## Preserve Meaning First

- A prose edit must preserve the claim, its scope, hypotheses, quantifiers,
  notation, confidence level, and evidentiary status.
- Do not make a statement stronger, broader, or more certain merely to make it
  read more smoothly.
- Keep proof, computation, citation, empirical illustration, and interpretation
  distinct. A cleaner sentence must not turn one form of support into another.
- Keep assumptions visible. Do not edit away conditions such as independence,
  regular variation, finite moments, asymptotic limits, threshold choices,
  common support, or nonsingular Fisher information.
- Use one stable name for each concept. Do not cycle through synonyms when the
  terms may differ mathematically (especially tail exponent, tail index, and
  extreme-value index; natural vs expectation parameters).
- If a style edit appears to change mathematical content, stop the prose pass
  and resolve the content with `$xshi-math-concept-page` or
  `$xshi-math-proof-writing` first.

## Voice and Clarity

- Prefer direct, specific prose over promotional framing or abstract metaphors.
- In tutorials and worked explanations, use first-person plural for choices and
  steps shared with the reader. Use direct declarative prose for facts,
  definitions, and mathematical claims.
- Let voice come from explanatory judgment: choose the useful example, name the
  real failure mode, and state what the evidence warrants. Do not invent
  opinions or informality to sound human.
- Use plain words when they preserve technical meaning; keep established
  mathematical terminology when a plainer substitute would be less precise.
- Prefer one logical move per sentence, but keep hypotheses and conclusions
  together when separating them would obscure the theorem.
- Use headings, lists, and callouts when they reveal structure. Do not impose a
  repeated template on pages whose concepts need different shapes.

## Patterns to Review

Treat these as signals for editorial judgment, not banned tokens:

- inflated significance, promotional language, and generic importance claims;
- vague attribution without a named source;
- filler, chatbot phrases, superficial participial phrases, and mechanical
  transitions;
- forced groups of three, false ranges, synonym cycling, and "not just X, but Y";
- scaffolding such as "At its core," "The key insight," or "What to notice"
  when the sentence can state the point directly;
- prose that merely restates a displayed formula without consequence, mechanism,
  or limitation;
- dense bold lead-ins that make the page read like a generated outline.

Math-specific failure modes:

- "clearly," "obviously," "trivially," or "by standard results" without the
  missing argument, conditions, or citation;
- proof-shaped prose that does not support the stated conclusion;
- an example, simulation, or numerical diagnostic presented as proof;
- a contested interpretation presented as consensus;
- related but non-equivalent concepts treated as interchangeable;
- intuition that supplies a metaphor but no mathematical mechanism;
- a smooth transition that hides a change of assumptions, domain, limit, or
  notation.

## Context-Dependent Forms

- Parentheses, em dashes, colons, passive voice, and long sentences can be
  appropriate. Revise them only when they increase reader effort or become
  repetitive.
- Hedging is required when it encodes uncertainty, approximation, empirical
  evidence, disputed interpretation, or conditional scope. Remove only empty or
  duplicated hedges.
- Repetition of a technical term is often clearer than a stylistic synonym.

## Cross-Track and Licensing

- Reuse symbols from `content/notation.md` (`/math/notation/`). See
  [shared-notation.md](shared-notation.md).
- Keep relative links inside a subsite; use full public URLs for cross-track
  links.
- Paraphrase and attribute; do not reproduce copyrighted text or figures. Prefer
  MIT-compatible repository-owned wording.

## Automation and Verification

- Automated prose checks may flag high-confidence phrases, but should be
  warning-only unless the rule is objective and semantics-free.
- Do not auto-rewrite equations, theorem statements, proof text, citations, or
  nearby qualifying prose.
- Compare edited text with the original claim by claim.
- Re-run executable examples or render the page when the edit changes MyST
  structure, code-adjacent prose, labels, links, or the interpretation of an
  output.
