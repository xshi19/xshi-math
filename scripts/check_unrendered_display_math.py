"""Fail if an opening `$$` is followed by a blank line (stdlib only).

MyST/Markdown then treats the delimiter as its own paragraph and the
following TeX as ordinary prose, so display math appears raw in the HTML.
Blank lines after a closing `$$` are fine. Code fences (backticks/tildes)
and `{code}` / `{code-block}` / `{code-cell}` bodies are ignored.

Optionally scan built HTML for visible `$$` or TeX commands outside KaTeX.
"""

from __future__ import annotations

import argparse
from html.parser import HTMLParser
from pathlib import Path
import re
import sys


FENCE = re.compile(r"^ {0,3}(`{3,}|~{3,})(.*)$")
DIRECTIVE_OPEN = re.compile(r"^ {0,3}(:{3,})\{([\w:-]+)\}")
DIRECTIVE_CLOSE = re.compile(r"^ {0,3}(:{3,})\s*$")
CODE_DIRECTIVES = {"code", "code-block", "code-cell"}
DOLLAR_LINE = re.compile(r"^(\s*)\$\$(\s*)$")
TEX_CMD = re.compile(r"\\[a-zA-Z]{2,}")


def _fence_mark(marker: str) -> tuple[str, int]:
    return marker[0], len(marker)


def iter_visible_lines(source: str):
    """Yield (0-based index, line, in_skipped_region)."""
    lines = source.splitlines()
    fence: tuple[str, int] | None = None
    code_dir: int | None = None  # colon count of an open code directive
    for i, line in enumerate(lines):
        skipped = fence is not None or code_dir is not None
        if fence is None and code_dir is None:
            fm = FENCE.match(line)
            if fm:
                fence = _fence_mark(fm.group(1))
                yield i, line, True
                continue
            dm = DIRECTIVE_OPEN.match(line)
            if dm and dm.group(2) in CODE_DIRECTIVES:
                code_dir = len(dm.group(1))
                yield i, line, True
                continue
        else:
            if fence is not None:
                fm = FENCE.match(line)
                if fm:
                    char, n = _fence_mark(fm.group(1))
                    if char == fence[0] and n >= fence[1]:
                        fence = None
                yield i, line, True
                continue
            cm = DIRECTIVE_CLOSE.match(line)
            if cm and len(cm.group(1)) >= (code_dir or 0):
                code_dir = None
            yield i, line, True
            continue
        yield i, line, skipped


def findings(path: Path, text: str | None = None) -> list[str]:
    """Report opening `$$` lines followed by a blank line before math content."""
    source = text if text is not None else path.read_text(encoding="utf-8")
    lines = source.splitlines()
    visible = {i for i, _, skipped in iter_visible_lines(source) if not skipped}

    def is_blank(i: int) -> bool:
        return i in visible and not lines[i].strip()

    def is_dollar(i: int) -> bool:
        return i in visible and bool(DOLLAR_LINE.match(lines[i]))

    hits: list[str] = []
    inside = False
    i = 0
    n = len(lines)
    while i < n:
        if i not in visible:
            i += 1
            continue
        line = lines[i]
        if is_dollar(i):
            if not inside:
                j = i + 1
                while j < n and is_blank(j):
                    j += 1
                if j > i + 1 and j < n and j in visible and not is_dollar(j):
                    rel = path.as_posix()
                    nxt = lines[j].strip()[:80]
                    hits.append(
                        f"{rel}:{i + 1}: opening $$ followed by a blank line before {nxt!r}"
                    )
                inside = True
            else:
                inside = False
            i += 1
            continue
        if "$$" in line:
            count = line.count("$$")
            if not inside:
                if count >= 2:
                    i += 1
                    continue
                after = line.split("$$", 1)[1]
                if after.strip() == "":
                    j = i + 1
                    while j < n and is_blank(j):
                        j += 1
                    if j > i + 1 and j < n and j in visible:
                        rel = path.as_posix()
                        nxt = lines[j].strip()[:80]
                        hits.append(
                            f"{rel}:{i + 1}: opening $$ followed by a blank line before {nxt!r}"
                        )
                inside = True
            else:
                inside = False
        i += 1
    return hits


def fix_text(source: str) -> str:
    """Remove blank lines immediately after opening `$$` delimiters."""
    lines = source.splitlines(keepends=True)
    # Work with newline-stripped copies for classification, preserve endings.
    raw = source.splitlines()
    # Recompute using findings on the current text iteratively
    text = source
    # safer: rebuild
    visible = {i for i, _, skipped in iter_visible_lines(source) if not skipped}

    def is_blank(i: int) -> bool:
        return i in visible and not raw[i].strip()

    def is_dollar(i: int) -> bool:
        return i in visible and bool(DOLLAR_LINE.match(raw[i]))

    drop: set[int] = set()
    inside = False
    n = len(raw)
    i = 0
    while i < n:
        if i not in visible:
            i += 1
            continue
        if is_dollar(i):
            if not inside:
                j = i + 1
                while j < n and is_blank(j):
                    drop.add(j)
                    j += 1
                inside = True
            else:
                inside = False
            i += 1
            continue
        if "$$" in raw[i]:
            count = raw[i].count("$$")
            if not inside:
                if count >= 2:
                    i += 1
                    continue
                after = raw[i].split("$$", 1)[1]
                if after.strip() == "":
                    j = i + 1
                    while j < n and is_blank(j):
                        drop.add(j)
                        j += 1
                inside = True
            else:
                inside = False
        i += 1

    if not drop:
        return source
    kept = [lines[i] for i in range(n) if i not in drop]
    out = "".join(kept)
    if source.endswith("\n") and not out.endswith("\n"):
        out += "\n"
    return out


SKIP_HTML = {"script", "style", "svg", "annotation", "math", "noscript", "code", "pre", "kbd", "samp", "textarea"}


class _RawMathHTML(HTMLParser):
    def __init__(self, rel: str):
        super().__init__(convert_charrefs=True)
        self.rel = rel
        self.skip = 0
        self.katex = 0
        self.cls: list[str] = []
        self.findings: list[str] = []
        self.last_id = ""

    def handle_starttag(self, tag, attrs):
        ad = dict(attrs)
        classes = ad.get("class", "")
        self.cls.append(classes)
        if ad.get("id"):
            self.last_id = ad["id"]
        if tag in SKIP_HTML:
            self.skip += 1
        if tag == "math" or "katex" in classes.split() or "katex-display" in classes.split():
            self.katex += 1

    def handle_endtag(self, tag):
        classes = self.cls.pop() if self.cls else ""
        if tag in SKIP_HTML and self.skip:
            self.skip -= 1
        if (
            tag == "math" or "katex" in classes.split() or "katex-display" in classes.split()
        ) and self.katex:
            self.katex -= 1

    def handle_data(self, data):
        if self.skip or self.katex:
            return
        if "$$" in data or TEX_CMD.search(data):
            snippet = " ".join(data.split())[:120]
            ident = f" #{self.last_id}" if self.last_id else ""
            self.findings.append(f"{self.rel}:{self.getpos()[0]}:{ident} {snippet!r}")


def html_findings(path: Path, text: str | None = None) -> list[str]:
    """Report visible `$$` or TeX commands outside KaTeX/MathML."""
    source = text if text is not None else path.read_text(encoding="utf-8")
    parser = _RawMathHTML(path.as_posix())
    parser.feed(source)
    return parser.findings


def iter_markdown(paths: list[Path]) -> list[Path]:
    out: list[Path] = []
    for path in paths:
        if path.is_file() and path.suffix == ".md":
            out.append(path)
        elif path.is_dir():
            out.extend(sorted(path.rglob("*.md")))
    return out


def iter_html(paths: list[Path]) -> list[Path]:
    out: list[Path] = []
    for path in paths:
        if path.is_file() and path.suffix in {".html", ".htm"}:
            out.append(path)
        elif path.is_dir():
            out.extend(sorted(path.rglob("*.html")))
    return out


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "paths",
        nargs="*",
        type=Path,
        help="Markdown files or directories (default: content/)",
    )
    parser.add_argument(
        "--html",
        action="store_true",
        help="Scan built HTML for unrendered math instead of Markdown sources",
    )
    parser.add_argument(
        "--fix",
        action="store_true",
        help="Remove blank lines after opening $$ in Markdown sources",
    )
    args = parser.parse_args(argv)
    paths = list(args.paths) or [Path("content")]
    if args.html:
        if args.fix:
            print("error: --fix applies only to Markdown sources", file=sys.stderr)
            return 2
        hits = [h for p in iter_html(paths) for h in html_findings(p)]
        for h in hits:
            print(h)
        return 1 if hits else 0

    files = iter_markdown(paths)
    all_hits: list[str] = []
    changed = 0
    for path in files:
        text = path.read_text(encoding="utf-8")
        hits = findings(path, text)
        if args.fix and hits:
            new = fix_text(text)
            if new != text:
                path.write_text(new, encoding="utf-8")
                changed += 1
                hits = findings(path, new)
        all_hits.extend(hits)
    for h in all_hits:
        print(h)
    if args.fix:
        print(f"updated {changed} file(s); {len(all_hits)} remaining finding(s)")
    return 1 if all_hits else 0


if __name__ == "__main__":
    sys.exit(main())
