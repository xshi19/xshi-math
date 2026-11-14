"""Report likely proofs missing a MyST result statement (stdlib only).

Checks ATX heading sections for proof/derivation headings, 'We prove', and
prf:proof directives. Introductory cues may precede a statement in the same
section; explicit proof directives require an earlier statement. Earlier
statements in parent sections count, but statements in sibling sections do not.
This is a review aid, not a full MyST parser or a check of mathematical validity.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass, field
from pathlib import Path
import re
from typing import Iterator


FENCE = re.compile(r"^ {0,3}(`{3,}|~{3,}|:{3,})(.*)$")
DIRECTIVE = re.compile(r"\{([\w:-]+)\}")
HEADING = re.compile(r"^ {0,3}(#{1,6})[ \t]+(.+?)\s*$")
PROOF_HEADING = re.compile(r"\b(?:proof|derivation)\b", re.IGNORECASE)
LEAD_IN = re.compile(r"\bwe\s+prove\b", re.IGNORECASE)
STATEMENTS = {"prf:proposition", "prf:theorem", "prf:lemma", "prf:corollary"}
CODE_DIRECTIVES = {"code", "code-block", "code-cell"}


@dataclass
class Section:
    title: str
    level: int
    parent: Section | None = None
    statements: list[int] = field(default_factory=list)
    proofs: list[int] = field(default_factory=list)
    cues: list[tuple[int, str]] = field(default_factory=list)


def visible_lines(source: str) -> Iterator[tuple[int, str]]:
    """Keep source line numbers; omit comments, frontmatter and fenced bodies.

    Yield prf openers but skip their bodies so internal prose/headings do not
    create new proof candidates. Code directives are also opaque; other MyST
    containers retain visible prose.
    """
    source = re.sub(
        r"<!--.*?(?:-->|\Z)",
        lambda match: re.sub(r"[^\n]", " ", match.group()),
        source,
        flags=re.DOTALL,
    )
    lines = source.splitlines()
    frontmatter = bool(lines and lines[0].lstrip("\ufeff").strip() == "---")
    # (fence character, minimum closing length, opaque body)
    fences: list[tuple[str, int, bool]] = []
    for number, line in enumerate(lines, 1):
        if frontmatter:
            if number > 1 and line.strip() in {"---", "..."}:
                frontmatter = False
            continue
        fence = FENCE.match(line)
        if fence and fences:
            marker, tail = fence.groups()
            char, length, _ = fences[-1]
            if marker[0] == char and len(marker) >= length and not tail.strip():
                fences.pop()
                continue
        if fences and fences[-1][2]:
            continue
        if fence:
            marker, tail = fence.groups()
            directive = DIRECTIVE.match(tail.strip())
            if directive:
                name = directive[1]
                is_prf = name.startswith("prf:")
                if is_prf:
                    yield number, line
                fences.append((marker[0], len(marker), is_prf or name in CODE_DIRECTIVES))
            elif marker[0] != ":":
                fences.append((marker[0], len(marker), True))
            continue
        if not line.startswith(("    ", "\t")):
            yield number, re.sub(r"(`+).*?\1", "", line)


def earlier_statement(section: Section, before: int) -> bool:
    """Look only in this section and its ancestors, before the candidate."""
    current: Section | None = section
    while current is not None:
        if any(line < before for line in current.statements):
            return True
        current = current.parent
    return False


def findings(path: Path, text: str | None = None) -> list[str]:
    source = path.read_text(encoding="utf-8") if text is None else text
    sections = [Section("(preamble)", 0)]
    stack = [sections[0]]
    for number, line in visible_lines(source):
        heading = HEADING.match(line)
        if heading:
            level = len(heading[1])
            title = re.sub(r"\s+#+\s*$", "", heading[2])
            while stack[-1].level >= level:
                stack.pop()
            section = Section(title, level, parent=stack[-1])
            sections.append(section)
            stack.append(section)
            if PROOF_HEADING.search(title):
                section.cues.append((number, "proof/derivation heading"))
            continue
        section = stack[-1]
        fence = FENCE.match(line)
        if fence:
            directive = DIRECTIVE.match(fence[2].strip())
            if directive and directive[1] in STATEMENTS:
                section.statements.append(number)
            elif directive and directive[1] == "prf:proof":
                section.proofs.append(number)
        elif LEAD_IN.search(line):
            section.cues.append((number, "'We prove' lead-in"))

    hits: list[tuple[int, str]] = []
    for section in sections:
        # Explicit proof markers give a stronger, ordered check than prose.
        missing_proofs = [
            line for line in section.proofs if not earlier_statement(section, line)
        ]
        for line in missing_proofs:
            hits.append((line, f"[{section.title}] prf:proof has no preceding "
                         "MyST prf statement in this section or a parent section"))
        for line, reason in section.cues:
            if missing_proofs:
                break  # Avoid repeating the same section's missing-statement warning.
            if earlier_statement(section, line):
                continue
            # A heading/lead-in may introduce a statement, as on regular-variation.
            if any(
                statement > line
                and not any(line < proof < statement for proof in section.proofs)
                for statement in section.statements
            ):
                continue
            hits.append((line, f"[{section.title}] {reason} has no MyST prf statement "
                         "in this section or preceding it in a parent section"))
            break  # One prose-cue finding per section is enough for review.
    return [f"{path}:{line}: {reason}" for line, reason in sorted(hits)]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "paths", nargs="*", type=Path,
        help="Markdown files or directories (default: <repo>/content)",
    )
    parser.add_argument(
        "--strict", action="store_true",
        help="exit 1 on findings; default report mode exits 0 (input errors exit 2)",
    )
    args = parser.parse_args(argv)
    targets = args.paths or [Path(__file__).resolve().parents[1] / "content"]
    files: dict[Path, Path] = {}
    for target in targets:
        if target.is_dir():
            candidates = sorted(p for p in target.rglob("*.md") if p.is_file())
        elif target.is_file():
            candidates = [target]
        else:
            parser.error(f"path does not exist or is not a file/directory: {target}")
        for path in candidates:
            files.setdefault(path.resolve(), path)
    hits: list[str] = []
    try:
        for path in files.values():
            hits.extend(findings(path))
    except (OSError, UnicodeError) as error:
        parser.error(str(error))
    for hit in hits:
        print(hit)
    print(f"{len(hits)} finding(s) in {len(files)} file(s); heuristic review only.")
    return int(args.strict and bool(hits))


if __name__ == "__main__":
    raise SystemExit(main())
