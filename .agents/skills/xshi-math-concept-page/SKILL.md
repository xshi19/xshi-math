---
name: xshi-math-concept-page
description: Create or substantially update mathematical notes under content/ for Incerto, Information Geometry, or Normix theory. Use for definitions, theorems, methods, examples, math prose, proofs, runnable demos, notation, citations, caveats, and cross-links. Do not use for narrow typo fixes or math questions that did not request an edit.
---

# xshi-math Concept Page

Use this skill when creating or substantially updating a mathematical note under
`content/` (flat globally unique stems) or a track hub under
`content/{incerto,ig,normix-theory}/`.

## Inputs

- Target concept, track, and page path.
- Relevant source chapter, paper, upstream wiki/theory page, or existing note.
- Shared notation in `content/notation.md` and any citation keys already used.
- Any Python behavior needed from `src/math/` or `demos/`.

## Workflow

1. Read `docs/rules/shared-notation.md` and
   `docs/rules/mathematical-writing.md`.
2. Read the track router (`content/<track>/AGENTS.md`) and nearby notes for
   local style and cross-link patterns.
3. Check `content/notation.md` (`/math/notation/`) for symbols that already
   exist. Extend that page for cross-track names; declare one-off symbols
   locally.
4. If adding or revising theorem/proposition statements or proof sections, use
   `$xshi-math-proof-writing` to scope statements and proof coverage before
   drafting the proof.
5. Draft or update the page. Settle claim scope and sources before narrative
   polish. Prefer MIT-compatible paraphrase and attribution; do not copy
   copyrighted text or figures.
6. Keep relative Markdown links inside the same subsite. Cross-track links must
   use full public URLs under `https://xshi19.github.io/math/...` (theme
   prepends `BASE_URL` to root-absolute Markdown links).
7. Link the first substantive body mention of each existing related note when
   the reader needs it early.
8. If Python is included, use helpers from `src/math/` / `demos/` or add tested
   helpers there. Prefer deterministic seeds and explicit units.
9. After mathematical claims and evidence are settled, use
   `$xshi-math-prose-review` and, when AI-pattern scrubbing is needed,
   `$xshi-math-unslop`.
10. Verify links, executable examples, and citations as far as the task allows.
    For site-affecting edits, prefer `npm run build` then `npm run check:html`
    when feasible; report skipped checks.

## Completion Check

The page is not done until:

- assumptions are explicit;
- claims are traceable to a proof, computation, citation, or explicit caveat;
- each theorem/proposition has reader-facing support, and each proof section
  says which statements it proves, sketches, or cites;
- shared notation matches `content/notation.md` and local notation is declared;
- first body mentions of related notes are linked where helpful;
- every recurring symbol is defined locally or linked to `/math/notation/`
  before it is relied on;
- examples, figures, simulations, and numerical checks are reproducible or
  explicitly deferred;
- the final prose pass preserves assumptions, notation, confidence, and form of
  evidence;
- any skipped proof, test, citation, or build step is reported.
