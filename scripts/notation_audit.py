#!/usr/bin/env python3
"""Run the installed math-notation skill's audit script with these arguments.

Install from xshi19/xshi-skills with `./install.sh math-notation`.
Set MATH_NOTATION_SKILL_DIR if the skill lives outside ~/.agents/skills.
See docs/rules/notation-economy.md for the hub workflow.
"""

import os
import runpy
import sys
from pathlib import Path


def main():
    skill_dir = Path(os.environ.get(
        "MATH_NOTATION_SKILL_DIR", str(Path.home() / ".agents/skills/math-notation")
    )).expanduser()
    script = skill_dir / "scripts/notation_audit.py"
    if not script.is_file():
        raise SystemExit(
            f"math-notation audit script not found: {script}\n"
            "From an xshi19/xshi-skills checkout, run ./install.sh math-notation; "
            "or set MATH_NOTATION_SKILL_DIR to its skill directory."
        )
    sys.argv[0] = str(script)
    runpy.run_path(str(script), run_name="__main__")


if __name__ == "__main__":
    main()
