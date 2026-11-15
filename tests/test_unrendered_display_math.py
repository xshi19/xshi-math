"""Opening `$$` must not be followed by a blank line."""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from check_unrendered_display_math import findings, fix_text, html_findings, main

ROOT = Path(__file__).resolve().parents[1]


def test_content_has_no_opening_dollar_blank_lines():
    hits = [hit for path in (ROOT / "content").rglob("*.md") for hit in findings(path)]
    assert hits == []


def test_flags_blank_line_after_opening_dollars(tmp_path: Path):
    src = tmp_path / "note.md"
    src.write_text("A claim.\n\n$$\n\nM(n)=n^{1/\\alpha}M(1)\n$$\n\nNext.\n", encoding="utf-8")
    hits = findings(src)
    assert len(hits) == 1
    assert "note.md:3:" in hits[0]
    assert "opening $$ followed by a blank line" in hits[0]
    assert main([str(src)]) == 1


def test_accepts_tight_display_math_and_blank_after_close(tmp_path: Path):
    src = tmp_path / "note.md"
    src.write_text("A claim.\n\n$$\nM(n)=n^{1/\\alpha}M(1)\n$$\n\nNext paragraph.\n", encoding="utf-8")
    assert findings(src) == []
    assert main([str(src)]) == 0


def test_ignores_code_fence_and_code_directive(tmp_path: Path):
    src = tmp_path / "note.md"
    src.write_text(
        "```markdown\n$$\n\nM(n)=1\n$$\n```\n\n"
        "::::{code-block}\n$$\n\nM(n)=1\n$$\n::::\n",
        encoding="utf-8",
    )
    assert findings(src) == []


def test_fix_removes_only_blank_lines_after_opening(tmp_path: Path):
    src = tmp_path / "note.md"
    original = "Lead.\n\n$$\n\nM(n)=1\n$$\n\nAfter.\n"
    src.write_text(original, encoding="utf-8")
    assert fix_text(original) == "Lead.\n\n$$\nM(n)=1\n$$\n\nAfter.\n"
    assert main(["--fix", str(src)]) == 0
    assert src.read_text(encoding="utf-8") == "Lead.\n\n$$\nM(n)=1\n$$\n\nAfter.\n"


def test_html_scan_flags_raw_dollar_paragraphs(tmp_path: Path):
    html = tmp_path / "page.html"
    html.write_text(
        '<div class="myst-proof-body"><p>$$</p>'
        r"<p>M(n)=n^{1/\alpha}M(1)</p></div>"
        '<span class="katex"><annotation>\\alpha</annotation></span>',
        encoding="utf-8",
    )
    hits = html_findings(html)
    assert any("$$" in h for h in hits)
    assert any("M(n)=" in h for h in hits)
    # KaTeX annotation must not count
    assert not any("annotation" in h for h in hits)
    assert main(["--html", str(html)]) == 1


def test_html_scan_ignores_code_and_pre(tmp_path: Path):
    html = tmp_path / "page.html"
    html.write_text(
        "<pre><code>$$\nM(n)=n^{1/\\alpha}M(1)\n$$</code></pre>"
        '<p>ordinary <code>\\alpha</code> mention</p>',
        encoding="utf-8",
    )
    assert html_findings(html) == []
    assert main(["--html", str(html)]) == 0
