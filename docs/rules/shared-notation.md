# Shared Notation

This rule governs symbol reuse across the Incerto, Information Geometry, and
Normix theory tracks. The canonical page is
[content/notation.md](../../content/notation.md), published at
`/math/notation/`.

## Requirements

- Before introducing a symbol for a concept that already appears in another
  track, read `content/notation.md` and reuse the shared form.
- When a concept needs a cross-track name that is not yet listed, **extend the
  shared page first**, then use the symbol in the note.
- Do not create per-track glossaries that redefine the same concept under a
  parallel symbol.
- Track hubs and body notes may still define **local** symbols for one-off
  arguments. Mark them as local and do not promote them silently into another
  track.
- On first substantive use of a shared symbol in a note, either define it
  locally in agreement with the canon or link to `/math/notation/`.
- When mapping to Normix package API names
  (`https://xshi19.github.io/normix/`), keep mathematical notes on this canon
  and state the mapping explicitly if needed.

## Track routers

Each of `content/incerto/AGENTS.md`, `content/ig/AGENTS.md`, and
`content/normix-theory/AGENTS.md` restates the shared-notation pointer for
agents that start inside a track. Keep those pointers in sync with this rule.

## Related skills

- `$xshi-math-concept-page` — checks notation before drafting.
- `$xshi-math-math-question` — resolves symbol confusion before editing.
- `$xshi-math-prose-review` / `$xshi-math-unslop` — must not "vary" symbols for
  style.
