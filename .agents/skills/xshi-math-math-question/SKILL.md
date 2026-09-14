---
name: xshi-math-math-question
description: Answer xshi-math content questions about notes, definitions, notation, statements, derivations, or organization before editing. Use when the user asks a math or content-refinement question about a page or concept across Incerto, IG, or Normix theory. Do not use for technical display, build, styling, or figure-rendering issues.
---

# xshi-math Math Question

Use this skill when the user asks a question about the mathematical content,
notation, explanation, organization, or reader clarity of a note on this hub.

Do not use this skill for technical website issues such as font size,
responsive layout, broken builds, missing image files, or figures not rendering.

## Inputs

- The user's question.
- Any page URL, title, section, formula, statement, or symbol mentioned.
- Relevant note, `content/notation.md`, track hub, or bibliography/citation text.
- Any prior chat context needed to understand what confused the user.

## Workflow

1. Classify the request. If it is a technical display or build issue, stop using
   this skill and handle it as a technical task.
2. Read the relevant page or source files before deciding whether the note is
   unclear. Include linked notation or adjacent notes when the question depends
   on them. Respect track boundaries and shared `/math/notation/`.
3. Answer the user's question in chat first. Be direct, and distinguish what
   the page currently says from what follows mathematically.
4. Diagnose the source of confusion:
   - if the user missed something already explained well, say where it appears
     and do not propose an edit;
   - if the page is incomplete, ambiguous, poorly ordered, missing notation, or
     skipping a load-bearing step, describe the reader problem;
   - if the issue is a mathematical uncertainty, state the uncertainty and what
     evidence would settle it.
5. When proposing a page change, propose a reader-friendly revision plan before
   editing. Name the target page(s), the section-level change, and the teaching
   reason.
6. Do not edit content in response to a question until the user explicitly
   approves the proposed plan. Avoid one-sentence patches that merely answer the
   chat prompt.
7. After approval, use `$xshi-math-concept-page` for notes and
   `$xshi-math-proof-writing` for theorem or proof changes.

## Completion Check

The response is not done until:

- the user's math-content question is answered before any edit proposal;
- the answer states whether the current page already covers the point;
- any proposed edit is framed as a reader improvement, not a chat-answer insert;
- target pages and section-level changes are named when an edit is proposed;
- no content files are edited unless the user has approved the proposed plan;
- any later approved edits use the appropriate skill and report verification.
