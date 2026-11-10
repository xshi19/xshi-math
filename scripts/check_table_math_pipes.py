r"""Fail if a markdown table row has an unescaped `|` inside math.

Markdown treats `|` as a column separator even when it sits inside `$...$`,
`$$...$$`, or `\(...\)`. Use `\lvert...\rvert`, `\lVert...\rVert`, or `\mid`
instead. A `|` preceded by a backslash (`\|`) is treated as escaped.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

SEPARATOR = re.compile(
    r"""^\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)+\|?\s*$"""
)


def is_separator(line: str) -> bool:
    return bool(SEPARATOR.match(line.rstrip()))


def table_row_indices(lines: list[str]) -> list[int]:
    """Return 0-based indices of markdown table data rows (not separators)."""
    n = len(lines)
    in_table = False
    rows: list[int] = []
    for i, line in enumerate(lines):
        has_pipe = "|" in line
        nxt = lines[i + 1] if i + 1 < n else ""
        starts = line.lstrip().startswith("|")
        enter = is_separator(line) or (has_pipe and is_separator(nxt)) or starts
        if enter:
            in_table = True
        elif in_table and not has_pipe:
            in_table = False
        if in_table and has_pipe and not is_separator(line):
            rows.append(i)
    return rows


def math_spans(line: str) -> list[tuple[int, int, str]]:
    """Return (start, end, body) for `$...$`, `$$...$$`, and `\\(...\\)` spans."""
    spans: list[tuple[int, int, str]] = []
    i = 0
    n = len(line)
    while i < n:
        if line.startswith("$$", i):
            j = line.find("$$", i + 2)
            if j < 0:
                break
            spans.append((i + 2, j, line[i + 2 : j]))
            i = j + 2
            continue
        if line.startswith(r"\(", i):
            j = line.find(r"\)", i + 2)
            if j < 0:
                break
            spans.append((i + 2, j, line[i + 2 : j]))
            i = j + 2
            continue
        if line[i] == "$":
            j = line.find("$", i + 1)
            if j < 0:
                break
            spans.append((i + 1, j, line[i + 1 : j]))
            i = j + 1
            continue
        i += 1
    return spans


def unescaped_pipes(body: str) -> list[int]:
    """Offsets of `|` in body that are not preceded by a backslash."""
    return [k for k, ch in enumerate(body) if ch == "|" and (k == 0 or body[k - 1] != "\\")]


def findings(path: Path, text: str | None = None) -> list[str]:
    lines = (text if text is not None else path.read_text(encoding="utf-8")).splitlines()
    out: list[str] = []
    for i in table_row_indices(lines):
        for _a, _b, body in math_spans(lines[i]):
            for k in unescaped_pipes(body):
                snippet = body.strip()
                out.append(f"{path}:{i + 1}: unescaped `|` in table math: ${snippet}$")
                break
    return out


def iter_markdown(root: Path) -> list[Path]:
    return sorted(p for p in root.rglob("*.md") if p.is_file())


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "paths",
        nargs="*",
        type=Path,
        help="Markdown files or directories (default: <repo>/content)",
    )
    args = parser.parse_args(argv)
    repo = Path(__file__).resolve().parents[1]
    targets = args.paths or [repo / "content"]
    files: list[Path] = []
    for p in targets:
        if p.is_dir():
            files.extend(iter_markdown(p))
        else:
            files.append(p)
    hits = [hit for path in files for hit in findings(path)]
    if hits:
        sys.stderr.write("\n".join(hits) + "\n")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
