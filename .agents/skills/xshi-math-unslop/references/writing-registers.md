# xshi-math writing registers

Identify the register before writing or editing. Unslop patterns and carve-outs
apply to all of them.

## `docs/design/`, `docs/plan/`, `docs/records/` — design and planning

- Decision-oriented: tables and short bullets over warm-up prose.
- Terse — every line costs agent context. Link, don't inline.
- Em dashes, status checkboxes, and TODO markers are fine.
- Separate current state from proposals.

## Root project docs (`README.md`, `ARCHITECTURE.md`, `AGENTS.md`)

- Operator voice: what exists, how to run it, where boundaries are.
- No marketing adjectives. Commands and paths must be real.
- Keep `AGENTS.md` a short router; push detail into rules/skills.

## `content/` mathematical notes — paper/appendix voice

- Notation defined before use or linked to `/math/notation/`.
- "We" for shared derivation steps; direct declaratives for facts.
- Full sentences; display math for load-bearing formulas.
- Proof vs citation vs illustration must stay visible.
- Relative links inside a track; full public URLs across tracks.

## Track hubs (`content/{incerto,ig,normix-theory}/`)

- Orientation and navigation, not full derivations.
- Point to body notes and shared notation; avoid duplicating canon.

## `demos/` and numerical commentary

- Reproducible: seed, units, inputs, what the figure shows.
- A plot is evidence about a computation, not a theorem proof.
- Friendly but not chatty: no "Let's dive in!".

## Quick test

Read the paragraph aloud: would a careful human author *of this register*
have written that sentence? A theorem sentence in marketing voice ("the
powerful GH family") or a design note in tutorial cheer fails the test.
