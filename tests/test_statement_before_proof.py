"""Fixture tests for the report checker; no strict gate on the existing corpus."""

from pathlib import Path
import sys

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from check_statement_before_proof import findings, main


ROOT = Path(__file__).resolve().parents[1]
FIXTURE = Path("fixture.md")


def statement(kind="proposition", fence=":::"):
    return f"{fence}{{prf:{kind}}} A result\n:label: prop-fixture\n\nClaim.\n{fence}\n"


def proof(fence=":::"):
    return f"{fence}{{prf:proof}}\nWe prove the claim.\n{fence}\n"


@pytest.mark.parametrize(
    ("source", "section", "reason", "line"),
    [
        ("## A claim\nWe prove the identity.\n", "A claim", "'We prove' lead-in", 2),
        ("## Proof of the identity\nArgument.\n", "Proof of the identity", "heading", 1),
        ("## Derivation of the formula\nArgument.\n", "Derivation of the formula", "heading", 1),
        ("## A claim\n" + proof(), "A claim", "prf:proof", 2),
    ],
)
def test_missing_statement_reports_location_and_reason(source, section, reason, line):
    hits = findings(FIXTURE, source)
    assert len(hits) == 1
    assert f"fixture.md:{line}: [{section}]" in hits[0]
    assert reason in hits[0]


@pytest.mark.parametrize("kind", ["proposition", "theorem", "lemma", "corollary"])
@pytest.mark.parametrize("fence", [":::", "```"])
def test_result_directives_before_proof_are_clean(kind, fence):
    source = "## A result\n" + statement(kind, fence) + proof(fence)
    assert findings(FIXTURE, source) == []


def test_introductory_cues_before_statement_are_clean():
    source = (
        "## Proof of the characterization\nWe prove the equivalence.\n"
        + statement() + proof() + "**Remark.** Interpretation.\n"
    )
    assert findings(FIXTURE, source) == []


def test_statement_after_explicit_proof_is_flagged():
    hits = findings(FIXTURE, "## Proof of the claim\n" + proof() + statement())
    assert len(hits) == 1
    assert "prf:proof has no preceding" in hits[0]


@pytest.mark.parametrize("unrelated_first", [True, False])
def test_statement_in_sibling_section_does_not_cover_proof(unrelated_first):
    unrelated = "## Other result\n" + statement()
    missing = "## Proof of this claim\nWe prove it here.\n"
    source = unrelated + missing if unrelated_first else missing + unrelated
    hits = findings(FIXTURE, source)
    assert len(hits) == 1
    assert "[Proof of this claim]" in hits[0]


def test_parent_statement_covers_proof_subsection():
    source = "## A result\n" + statement() + "### Proof\n" + proof()
    assert findings(FIXTURE, source) == []


def test_statement_in_sibling_subsection_does_not_cover_proof():
    source = (
        "## Results\n### First result\n" + statement()
        + "### Proof of another result\n" + proof()
    )
    hits = findings(FIXTURE, source)
    assert len(hits) == 1
    assert "[Proof of another result]" in hits[0]


@pytest.mark.parametrize(
    "wrap",
    [
        lambda text: f"````markdown\n{text}````\n",
        lambda text: f"~~~~markdown\n{text}~~~~\n",
        lambda text: f"<!--\n{text}-->\n",
        lambda text: "".join("    " + line + "\n" for line in text.splitlines()),
    ],
)
def test_examples_and_comments_neither_flag_nor_supply_statements(wrap):
    example = wrap("## Proof of an example\nWe prove this.\n" + statement())
    assert findings(FIXTURE, example) == []
    hits = findings(FIXTURE, example + "## Real claim\nWe prove the identity.\n")
    assert len(hits) == 1
    assert "[Real claim]" in hits[0]


def test_frontmatter_and_inline_code_do_not_trigger_findings():
    source = (
        "---\ntitle: We prove this\n---\n"
        "## Definition\nA definition.\n"
        "The checker looks for `We prove` and `:::{prf:proof}`.\n"
        "## Cited result\nWe cite the theorem without proof.\n"
    )
    assert findings(FIXTURE, source) == []


@pytest.mark.parametrize("directive", ["code", "code-block", "code-cell"])
@pytest.mark.parametrize("fence", ["::::", "````"])
def test_code_directives_neither_flag_nor_supply_statements(directive, fence):
    example = (
        f"{fence}{{{directive}}} markdown\n"
        "## Proof of an example\nWe prove this.\n"
        + statement() + f"{fence}\n"
    )
    assert findings(FIXTURE, example) == []
    hits = findings(FIXTURE, "## Real claim\n" + example + proof())
    assert len(hits) == 1
    assert "[Real claim] prf:proof has no preceding" in hits[0]


def test_nonstatement_prf_directive_does_not_cover_proof():
    source = "## A result\n" + statement("definition") + proof()
    assert len(findings(FIXTURE, source)) == 1


def test_nested_myst_containers_preserve_real_directives():
    source = "::::{note}\n## A result\n" + statement() + proof() + "::::\n"
    assert findings(FIXTURE, source) == []


def test_cli_report_and_strict_modes_with_recursive_paths(tmp_path, capsys):
    nested = tmp_path / "nested"
    nested.mkdir()
    bad = nested / "bad.md"
    bad.write_text("## Missing\nWe prove the claim.\n", encoding="utf-8")
    good = tmp_path / "good.md"
    good.write_text("## Result\n" + statement() + proof(), encoding="utf-8")
    (tmp_path / "ignored.txt").write_text("We prove a claim.\n", encoding="utf-8")

    assert main([str(tmp_path), str(bad)]) == 0
    report = capsys.readouterr().out
    assert f"{bad}:2: [Missing]" in report
    assert "1 finding(s) in 2 file(s)" in report  # Overlapping paths are deduplicated.
    assert main(["--strict", str(tmp_path)]) == 1
    capsys.readouterr()
    assert main(["--strict", str(good)]) == 0
    assert "0 finding(s) in 1 file(s)" in capsys.readouterr().out


def test_cli_missing_path_is_an_error_even_in_report_mode(tmp_path, capsys):
    with pytest.raises(SystemExit) as error:
        main([str(tmp_path / "missing.md")])
    assert error.value.code == 2
    assert "path does not exist" in capsys.readouterr().err


def test_regular_variation_smoke():
    assert findings(ROOT / "content/incerto-regular-variation.md") == []
