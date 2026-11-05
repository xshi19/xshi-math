# Notation audit integration

The general [`math-notation` skill](https://github.com/xshi19/xshi-skills/blob/master/skills/math-notation/SKILL.md)
owns symbol-selection criteria, the final-draft audit, WLOG, reuse after
transformation, and the optional audit script. This file only connects that
procedure to xshi-math; do not copy it into repo rules or skill checklists.

## Install

From an `xshi19/xshi-skills` checkout containing merge `826d163` or later, use
its [installer](https://github.com/xshi19/xshi-skills/blob/master/install.sh):

```bash
./install.sh math-notation
```

Use the user-level installation; keep the general skill outside this repo.
If unavailable, read the upstream skill and its linked references, or report
the audit as not run. The optional `scripts/notation_audit.py` launcher uses
`~/.agents/skills/math-notation`; set `MATH_NOTATION_SKILL_DIR` for another location.

## Hub workflow

Run `$math-notation` during the final prose pass, after claims and proofs settle
and before rendered-page verification. Cross-track notation remains governed
by [shared-notation.md](shared-notation.md), which points to the hub's
`/math/notation/` canon.
