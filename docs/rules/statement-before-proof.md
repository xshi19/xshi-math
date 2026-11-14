# Statement before proof: site integration

The external [`$statement-before-proof` skill](https://github.com/xshi19/xshi-skills/blob/master/skills/statement-before-proof/SKILL.md)
owns the general principle, result-type choices, and statement/proof audit.
Apply it when drafting or reviewing proofs and formal derivations in this hub.
This file owns only xshi-math's rendering, links, and checker; keep the general
rule upstream.

## Install

From an `xshi19/xshi-skills` checkout containing the skill, use its
[installer](https://github.com/xshi19/xshi-skills/blob/master/install.sh):

```bash
./install.sh statement-before-proof
```

Use the user-level installation; do not vendor the skill here. The link above
is the intended `master` path even while the upstream merge is pending. If the
installed skill is unavailable, read the upstream skill or an owner-supplied
copy; if neither is available, report its audit as not run.

## MyST markup and links

Use `:::{prf:proposition}`, `:::{prf:theorem}`, `:::{prf:lemma}`, or
`:::{prf:corollary}` for a result, with a descriptive title and a stable
`:label:`. Let MyST supply the displayed result numbering. Place the separate
`:::{prf:proof}` directive after the result's closing fence, then put remarks
after the proof's closing fence:

````markdown
:::{prf:proposition} Descriptive result name
:label: prop-note-stem-result

Statement text.
:::

:::{prf:proof}
Proof text.
:::

**Remark.** Follow-up commentary.
````

Use a unique label with a result-type prefix (`prop-`, `thm-`, `lem-`, or
`cor-`) and the note's identifying stem. Refer to it with MyST syntax such as
`[](#prop-note-stem-result)`, rather than hard-coding a displayed number.

The existing [regular-variation page](../../content/incerto-regular-variation.md)
is the verified rendering example: `prop-regular-variation-characterization`
and `prop-regular-variation-positive-powers` render as HTML `aside.myst-proof`
blocks. For content conversions, inspect the rendered statement, proof,
numbering, and cross-references using the [site checks](../../README.md#build-the-sites).

Preserve existing Normix theory slugs and heading anchors: external Normix
Engineer links depend on them. Keep existing headings and explicit anchors
when inserting directives; adding new `prf` labels is fine.

## Report checker

Run the stdlib-only [checker](../../scripts/check_statement_before_proof.py)
from the repo root:

```bash
python3 scripts/check_statement_before_proof.py              # content/**/*.md
python3 scripts/check_statement_before_proof.py content/incerto-regular-variation.md
python3 scripts/check_statement_before_proof.py --strict path/to/converted-note.md
```

It accepts files or directories and reports file, line, section, and reason.
Default report mode exits 0 even with findings; `--strict` exits 1 when findings
exist. Input errors exit 2. Keep the unconverted corpus out of a default strict
test gate; [detector tests](../../tests/test_statement_before_proof.py) use
fixtures and a regular-variation smoke check.

The checker looks for proof/derivation headings, “We prove” lead-ins, and
`prf:proof` blocks. It checks statements within the same heading section or a
parent section, not unrelated sibling sections. Introductory headings and
lead-ins may precede a statement in their section, as on regular-variation;
an explicit proof block needs an earlier statement. Code examples, frontmatter,
and HTML comments are ignored.

Treat findings as review candidates. The checker does not parse full MyST,
match a proof to a particular claim, check labels or hypotheses, or recognize
all prose derivations. Cross-section proofs may need manual review; a clean
report does not replace the external skill's audit or rendered-page checks.
