"""Unescaped `|` inside math in a markdown table splits the cell."""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from check_table_math_pipes import findings, main

ROOT = Path(__file__).resolve().parents[1]


def test_content_tables_have_no_unescaped_math_pipes():
    hits = [hit for path in (ROOT / "content").rglob("*.md") for hit in findings(path)]
    assert hits == []


def test_checker_flags_abs_bar_and_accepts_lvert_and_mid(tmp_path: Path):
    bad = tmp_path / "bad.md"
    bad.write_text(
        "| name | formula |\n"
        "| --- | --- |\n"
        "| abs | $(n^{-1}\\sum_i|x_i|^p)^{1/p}$ |\n",
        encoding="utf-8",
    )
    assert findings(bad)
    assert main([str(bad)]) == 1

    good = tmp_path / "good.md"
    good.write_text(
        "| name | formula |\n"
        "| --- | --- |\n"
        "| abs | $(n^{-1}\\sum_i\\lvert x_i\\rvert^p)^{1/p}$ |\n"
        "| cond | $e(u)=\\mathbb E[X-u\\mid X>u]$ |\n"
        "| norm | $\\|x\\|$ |\n",
        encoding="utf-8",
    )
    assert findings(good) == []
    assert main([str(good)]) == 0
