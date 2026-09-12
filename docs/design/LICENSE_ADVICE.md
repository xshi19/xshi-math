# License Advice

Maintainer: Xiang Shi
Last updated: 2026-09-12

Recommendation for licensing public `xshi-math`. No `LICENSE` file is added
until Xiang picks an option.

## Sibling repos

| Repo | Visibility | License |
| --- | --- | --- |
| [`xshi19/normix`](https://github.com/xshi19/normix) | Public | MIT (`LICENSE`, copyright 2020 xshi19) |
| [`xshi19/incerto-wiki`](https://github.com/xshi19/incerto-wiki) | Private | MIT (`LICENSE` in tree) |
| [`xshi19/xshi-math`](https://github.com/xshi19/xshi-math) | Public | **Undecided** (this doc) |

Incerto's private MIT still matters: it is the license of the code and
original notes that would move here. It does **not** license Taleb's
books, papers, or figures.

## Options

### A. MIT for the whole repo (default)

One `LICENSE` covering code, Lean, scripts, theme, and tutorial prose.

- Simplest GitHub UX; matches both siblings.
- Downstream can reuse notes and demos with only the MIT notice.
- Weak on **attribution of the prose itself**. MIT is a software license;
  it does not give a clean "cite the notes" norm the way CC-BY does.

### B. Dual: MIT for code / Lean / scripts; CC-BY-4.0 for tutorial prose

- Stronger, conventional split for "software + textbooks."
- CC-BY-4.0 requires attribution when notes are reused, which fits a
  public teaching wiki.
- Costs: `LICENSE` plus a short `NOTICE` that maps paths (`packages/`,
  `scripts/`, `**/*.lean` → MIT; `tracks/*/content/`, `site/**/*.md` →
  CC-BY-4.0). Some GitHub license detection becomes messy. Agents and
  humans must not paste code-license headers onto essays or vice versa.

### C. Apache-2.0 (whole repo or code side)

- Patent grant and NOTICE conventions.
- Unlikely to matter for personal math notes and small demo packages.
- Diverges from MIT siblings without a concrete patent threat.

## Recommendation

**Choose A: MIT whole-repo for v1.**

Rationale:

- Matches `normix` and `incerto-wiki`, so moved files do not change
  license.
- The first cutover is already loaded (private→public scrub, redirects,
  shared theme). Dual licensing is a real process cost and a footgun for
  agents.
- Xiang can move to option B later by adding CC-BY-4.0 on
  `tracks/*/content/` without breaking MIT for existing code, if
  attribution on the notes becomes the priority.

Choose **B now** if Xiang already wants people to treat the notes as a
citable text with a mandatory credit line. That is a preference, not a
legal requirement of the siblings.

Do not choose C unless a collaborator or employer requires the patent
grant.

`Open question:` confirm A vs B before Phase 1 scaffold writes `LICENSE`.

## After the decision

Add, in the same scaffold PR:

1. Root `LICENSE` (MIT text, and CC-BY-4.0 text if B).
2. Short `NOTICE` stating copyright holder (Xiang Shi), year, and — if B —
   the path split.
3. `CITATION.cff` (and optionally a one-paragraph `CITATION.md`) so the
   site and repo can be cited as a software/notes project.

Point `README.md` at those files. Do not add SPDX headers to every
Markdown page in v1.

## Copyright gates that license choice does not solve

Making the repo MIT (or CC-BY) only covers **Xiang's** original files. It
does not clear third-party copyright.

Before any Incerto migration (see
[consolidation.md](../plan/consolidation.md) Phase 3):

- Paraphrased Incerto / Taleb material must stay **paraphrase + cite**.
  The wiki is a companion, not a replica.
- Do not dump copyrighted figures, tables, or extended quotations.
- Recreate figures from code or original drawings.
- Private→public scrub: private notes, secrets, reviewer names, and
  license-restricted data (for example vendor index series that Incerto
  already refuses to commit) stay out.
- Third-party snippets keep their own license (Mathlib, KaTeX, Kami
  tokens if attribution is required, dataset licenses). Record those in
  `NOTICE` when they ship.

A public MIT repo that contains a copyrighted scan is still a problem.

## Sources

- [MIT License](https://opensource.org/license/mit)
- [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
- [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0)
