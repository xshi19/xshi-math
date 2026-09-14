---
name: xshi-math-reading-guide
description: Author or update a source-to-concept reading map for xshi-math. Use when mapping a book, paper, chapter, or section onto flat content/*.md stems and track hubs, recording notation differences, planned missing notes, and copyright-safe paraphrase. Do not invent a reading-guides/ tree or fake guide pages; fold short mappings into concept notes or track hubs when a dedicated guide is not warranted.
---

# xshi-math Reading Guide

Use this skill when a source chapter or paper needs an explicit map onto this
repo's notes. There is **no** `content/reading-guides/` tree and no
`content/concepts/` hierarchy here: notes use flat globally unique stems under
`content/` plus track hubs under `content/{incerto,ig,normix-theory}/`.

## When to author a dedicated guide

Create a dedicated guide page only when the mapping is large enough that it
would crowd a concept note or hub (multiple chapters, many planned atoms, or
repeated source→concept navigation). Prefer:

1. A short "Sources / reading map" section on an existing concept note, or
2. A hub subsection under the relevant track, or
3. A new flat stem such as `content/<track>-reading-<source-slug>.md` linked
   from the track hub and MyST TOC when the owner asks to publish it.

Do **not** invent placeholder guide URLs or empty guide files "for later."

## Inputs

- Source work and chapter or section scope.
- Existing notes (flat stems) and the track hub that should surface them.
- Notation differences vs `content/notation.md`.
- Copyright-sensitive passages or figures to paraphrase, not reproduce.

## Workflow

1. Read `docs/rules/shared-notation.md` and
   `docs/rules/mathematical-writing.md`.
2. Read the track router and nearby notes; use `$xshi-math-concept-page` for
   any atom that needs a real page rather than a long inline derivation.
3. Identify the source's main argumentative path.
4. Map each definition, theorem, method, and empirical example to an existing
   stem, a planned stem (explicitly marked planned), or a short local note.
5. Record source notation differences against `content/notation.md`; extend
   the shared page for cross-track symbols before inventing parallels.
6. Link the first substantive mention of each existing note; do not re-derive
   full results in the guide when a concept page already owns them.
7. Flag imprecise, nonstandard, or contested claims and point to clarifying
   notes.
8. Prefer MIT-compatible paraphrase and attribution; never copy copyrighted
   prose or figures.
9. After mapping, claims, and citations settle, use `$xshi-math-prose-review`
   (and `$xshi-math-unslop` if AI-pattern scrubbing is needed).
10. Keep relative Markdown links inside the same subsite; cross-track links use
    full `https://xshi19.github.io/math/...` URLs.

## Folding source→concept without a guide page

When the owner only needs a few atoms from a source:

- Open or create the concept notes with `$xshi-math-concept-page`.
- Put a brief source attribution and section pointer on each note.
- Update the track hub with links to those notes.
- Stop; do not create an empty reading-guide shell.

## Completion Check

Not done until:

- the source section's goal is stated;
- source material maps to existing or explicitly planned stems;
- notation differences are visible;
- first body mentions of existing notes are linked where helpful;
- no copyrighted prose or figures are reproduced;
- the final prose pass preserves attribution, uncertainty, and the distinction
  between the source's claims and this hub's interpretation;
- missing notes are marked planned rather than silently replaced by long guide
  text;
- no fake `content/reading-guides/` paths were invented.
