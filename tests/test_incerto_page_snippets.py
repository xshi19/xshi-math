"""Execute every fenced ``python`` block on the public Incerto pages.

Convention: a line containing exactly ```python starts a runnable example;
the local-data layoffs and S&P blocks skip when their CSVs are absent.
Blocks inside MyST dropdowns count too. Each
block must be self-contained, print a result or create a figure, and finish
quickly. Processes run with Agg, a temporary cwd/cache, no network, and no
writes beneath the repository. The financial example also runs against a
synthetic local price cache so its data-present branch cannot silently rot.
An immediately following **Output** text block is checked against captured
stdout, ignoring trailing whitespace on each line and at the end only.
All text output must use plain numbers with at most six decimal places.
"""

import ast
import os
from pathlib import Path
import re
import subprocess
import sys

import numpy as np
import pytest


ROOT = Path(__file__).resolve().parents[1]
PAGES = sorted((ROOT / "content").glob("incerto-*.md")) + [ROOT / "content/incerto/index.md"]
PYTHON_BLOCK = re.compile(r"^```python\n(.*?)\n```[ \t]*$", re.M | re.S)
OUTPUT_BLOCK = re.compile(r"\s*\*\*Output\*\*[ \t]*\n\s*```text\n(.*?)\n```[ \t]*(?:\n|$)", re.S)
TEXT_BLOCK = re.compile(r"^```text\n(.*?)\n```[ \t]*$", re.M | re.S)
LONG_DECIMAL = re.compile(r"(?<![\w.])[+-]?(?:\d+)?\.\d{7,}(?:[eE][+-]?\d+)?")
API = (ROOT / "content/incerto-api-reference.md").read_text()


def page_snippets(text):
    for index, match in enumerate(PYTHON_BLOCK.finditer(text), 1):
        output = OUTPUT_BLOCK.match(text, match.end())
        yield index, match.group(1), output.group(1) if output else None


SNIPPETS = [
    pytest.param(page, index, code, expected, id=f"{page.stem}-{index}")
    for page in PAGES
    for index, code, expected in page_snippets(page.read_text())
]

# Avoid accidental writes even if a later example uses an absolute repo path.
# Read-only dataset access is allowed; snapshots are resolved by the loader.
RUNNER = r'''
import os
from pathlib import Path
import sys

repository = Path(sys.argv[1]).resolve()
def audit(event, args):
    if event in {"socket.connect", "socket.getaddrinfo"}:
        raise AssertionError("Page snippets must not use the network")
    if event == "open":
        path, mode, flags = args
        writing = flags & (os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_TRUNC | os.O_APPEND)
        if writing and isinstance(path, (str, bytes, os.PathLike)):
            if Path(os.fsdecode(path)).resolve().is_relative_to(repository):
                raise AssertionError(f"Page snippet attempted a repository write: {path}")
sys.addaudithook(audit)
exec(compile(sys.stdin.read(), sys.argv[2], "exec"), {"__name__": "__main__"})
'''


def requires_layoffs_data(page, code):
    return page.stem == "incerto-layoffs-tails" and "load_layoffs(" in code


def layoffs_data_available():
    path = os.environ.get("INCERTO_LAYOFFS_PATH")
    return Path(path or ROOT / "data/incerto/cache/layoffs/layoffs.csv").is_file()


def requires_sp500_data(page, code):
    return page.stem in {"incerto-sp500", "incerto-sp500-tail"} and "load_sp500_prices(" in code


def sp500_data_root():
    return Path(os.environ.get("INCERTO_DATA_DIR", ROOT / "data/incerto"))


def sp500_data_available():
    return (sp500_data_root() / "cache/sp500_daily.csv").is_file()


def run_snippet(page, index, code, tmp_path, *, data_dir=None):
    env = {
        **os.environ,
        "MPLBACKEND": "Agg",
        "MPLCONFIGDIR": str(tmp_path / "mpl"),
        "XDG_CACHE_HOME": str(tmp_path / "cache"),
        "PYTHONDONTWRITEBYTECODE": "1",
        "OPENBLAS_NUM_THREADS": "1",
        "OMP_NUM_THREADS": "1",
    }
    env.pop("PYTHONPATH", None)
    env["INCERTO_DATA_DIR"] = str(data_dir or ROOT / "data/incerto")
    if requires_sp500_data(page, code) and data_dir is None:
        env["INCERTO_DATA_DIR"] = str(sp500_data_root())
    result = subprocess.run(
        [sys.executable, "-c", RUNNER, str(ROOT), f"{page.name}:python-{index}"],
        input=code, text=True, capture_output=True, cwd=tmp_path, env=env,
        timeout=30,  # full-history diagnostics take several seconds
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert result.stdout.strip() or "plt.show(" in code, "Example must expose its result"
    return result.stdout


def strip_trailing_whitespace(text):
    return "\n".join(line.rstrip() for line in text.rstrip().splitlines())


def assert_plain_numbers(output):
    for token in ("np.float64", "np.int64", "array("):
        assert token not in output, f"NumPy representation in output: {token}"
    assert not LONG_DECIMAL.search(output), f"More than six decimal places in output: {output}"


@pytest.mark.parametrize("page,index,code,expected", SNIPPETS)
def test_incerto_python_block(page, index, code, expected, tmp_path):
    if requires_layoffs_data(page, code) and not layoffs_data_available():
        pytest.skip("Local layoffs CSV absent; recorded output is checked separately")
    if requires_sp500_data(page, code) and not sp500_data_available():
        pytest.skip("Local S&P CSV absent (not redistributed); supply the dated cache to check observed output")
    output = run_snippet(page, index, code, tmp_path)
    assert_plain_numbers(output)
    if expected is not None:
        assert strip_trailing_whitespace(output) == strip_trailing_whitespace(expected)


@pytest.mark.parametrize("page,index,code,expected", SNIPPETS)
def test_snippet_api_links(page, index, code, expected):
    """Every imported package callable has a stable, linked reference entry."""
    names = []
    for node in ast.walk(ast.parse(code)):
        if isinstance(node, ast.ImportFrom) and (node.module or "").startswith("xmath"):
            names.extend(alias.name for alias in node.names)
    for name in names:
        anchor = "api-" + name.replace("_", "-").replace(".", "-").lower()
        assert f"({anchor})=" in API, (page, index, name)
        assert f"incerto-api-reference.md#{anchor})" in page.read_text(), (page, index, name)


def test_output_blocks_are_paired():
    """Do not silently skip an Output block after a misplaced dropdown close."""
    for page in PAGES:
        text = page.read_text()
        labelled = len(re.findall(r"^\*\*Output\*\*[ \t]*$", text, re.M))
        paired = sum(expected is not None for _, _, expected in page_snippets(text))
        assert labelled == paired, page


def test_output_blocks_use_plain_numbers():
    # Include the recorded full-demo output as well as paired snippet outputs.
    for page in PAGES:
        for block in TEXT_BLOCK.finditer(page.read_text()):
            assert_plain_numbers(block.group(1))


@pytest.mark.parametrize("output", [
    "np.float64(0.0)", "np.int64(3)", "array([1, 2])",
    "value: -0.1234567", "[.1234567]", "value: 1.2345678e-10",
])
def test_plain_number_check_rejects_reprs_and_long_decimals(output):
    with pytest.raises(AssertionError):
        assert_plain_numbers(output)


def test_plain_number_check_accepts_short_numbers():
    assert_plain_numbers("count: 789724\n[0, -2, 0.123456, 1.024e-17, inf, -inf, nan]")


def test_output_comparison_rejects_changed_values(tmp_path):
    page = ROOT / "content/incerto-api-reference.md"
    with pytest.raises(AssertionError):
        test_incerto_python_block(page, 0, 'print("value: 2")', "value: 3", tmp_path)
    test_incerto_python_block(page, 0, 'print("value: 2  ")', "value: 2\t\n", tmp_path)
    with pytest.raises(AssertionError):
        test_incerto_python_block(page, 0, 'print(" value: 2")', "value: 2", tmp_path)


def test_financial_snippet_with_local_synthetic_prices(tmp_path):
    page = ROOT / "content/incerto-sp500-tail.md"
    code = PYTHON_BLOCK.search(page.read_text()).group(1)
    cache = tmp_path / "synthetic-data/cache"
    cache.mkdir(parents=True)
    # Deterministic synthetic prices: 500 strictly positive, distinct log losses.
    losses = np.linspace(0.0001, 0.003, 500)
    prices = 100 * np.exp(-np.r_[0.0, np.cumsum(losses)])
    dates = np.datetime64("2020-01-01") + np.arange(prices.size)
    (cache / "sp500_daily.csv").write_text(
        "date,close\n" + "".join(f"{day},{price:.16g}\n" for day, price in zip(dates, prices))
    )
    output = run_snippet(page, 1, code, tmp_path, data_dir=cache.parent)
    assert_plain_numbers(output)
    assert "Return window: 2020-01-02 to 2021-05-15" in output
    assert "loss days: 500" in output
    assert "Hill k=25:" in output and "Hill k=400:" in output
    assert "mean excess" in output and "exceedances" in output


def test_chapter10_financial_snippet_with_local_synthetic_prices(tmp_path):
    page = ROOT / "content/incerto-sp500.md"
    code = next(code for _, code, _ in page_snippets(page.read_text())
                if "load_sp500_prices(" in code)
    cache = tmp_path / "synthetic-data/cache"
    cache.mkdir(parents=True)
    returns = .01 * np.sin(np.arange(300)) + .001
    prices = 100 * np.exp(np.r_[0, np.cumsum(returns)])
    dates = np.datetime64("2020-01-01") + np.arange(len(prices))
    (cache / "sp500_daily.csv").write_text(
        "date,close\n" + "".join(f"{d},{p:.16g}\n" for d, p in zip(dates, prices)))
    output = run_snippet(page, 7, code, tmp_path, data_dir=cache.parent)
    assert_plain_numbers(output)
    assert "returns=300" in output and "h=21:" in output
    assert "gain:" in output and "loss:" in output and "alpha=" in output
    assert "Maximum drawdown:" in output and "No local" not in output


@pytest.mark.parametrize("stem", ["incerto-sp500", "incerto-sp500-tail"])
def test_financial_snippet_skips_when_cache_is_absent(tmp_path, monkeypatch, stem):
    monkeypatch.setenv("INCERTO_DATA_DIR", str(tmp_path / "absent-data"))
    page = ROOT / "content" / f"{stem}.md"
    index, code, expected = next(row for row in page_snippets(page.read_text())
                                if requires_sp500_data(page, row[1]))
    with pytest.raises(pytest.skip.Exception, match="Local S&P CSV absent"):
        test_incerto_python_block(page, index, code, expected, tmp_path)


def test_regenerator_preserves_observed_output_without_cache(tmp_path, monkeypatch):
    """Use temporary page copies; absent data must not overwrite dated output."""
    import runpy
    harness = runpy.run_path(str(ROOT / "tests/test_incerto_page_snippets.py"))
    pages = []
    for name in ("incerto-sp500", "incerto-sp500-tail"):
        page = tmp_path / f"{name}.md"
        # Keep just the empirical block to exercise the missing-input route.
        code, expected = next((code, expected) for _, code, expected in
            page_snippets((ROOT / "content" / page.name).read_text())
            if requires_sp500_data(page, code))
        page.write_text(f"```python\n{code}\n```\n\n**Output**\n\n```text\n{expected}\n```\n")
        pages.append(page)
    originals = [p.read_bytes() for p in pages]
    harness["PAGES"] = pages
    harness["sp500_data_available"] = lambda: False
    regen = runpy.run_path(str(ROOT / "scripts/regenerate_incerto_outputs.py"))
    monkeypatch.setattr(runpy, "run_path", lambda *a, **kw: harness)
    monkeypatch.setattr(sys, "argv", ["regenerate", "--pages", *[p.stem for p in pages]])
    regen["main"]()
    assert [p.read_bytes() for p in pages] == originals


def test_demo_pages_have_visible_examples():
    for page in PAGES:
        text = page.read_text()
        if "demos/incerto/" in text:
            assert PYTHON_BLOCK.search(text), f"Demo-only instructions on {page.name}"


def test_long_code_blocks_use_dropdowns():
    for page in PAGES:
        text = page.read_text()
        dropdowns = list(re.finditer(r"^:::\{dropdown\}[^\n]*\n.*?^:::[ \t]*$", text, re.M | re.S))
        for block in re.finditer(r"^```(?:python|text|sh|bash)\n(.*?)\n```", text, re.M | re.S):
            if len(block.group(1).splitlines()) > 12:
                assert any(d.start() < block.start() < block.end() < d.end()
                           for d in dropdowns), page


def test_powerlaw_theory_examples_are_registered_for_exact_output_checks():
    # The discovery rule is automatic; retain explicit coverage of this pair.
    for name in ("incerto-power-law-fitting", "incerto-power-law-goodness-of-fit"):
        page = ROOT / "content" / f"{name}.md"
        assert page in PAGES
        snippets = list(page_snippets(page.read_text()))
        assert len(snippets) == 4
        assert all(expected is not None for _, _, expected in snippets)


def test_layoffs_snippet_with_synthetic_local_csv(tmp_path, monkeypatch):
    page = ROOT / "content/incerto-layoffs-tails.md"
    code = next(code for _, code, _ in page_snippets(page.read_text())
                if requires_layoffs_data(page, code))
    source = tmp_path / "synthetic-layoffs.csv"
    source.write_text("company,date,n,frac\n" + "".join(
        f"Synthetic {i},2020-03-11,{10+i*i},{(i % 80 + 1)/100}\n" for i in range(180)))
    monkeypatch.setenv("INCERTO_LAYOFFS_PATH", str(source))
    output = run_snippet(page, 2, code, tmp_path)
    assert_plain_numbers(output)
    assert "Events: 180" in output
    assert "Counts: 180 observations" in output
    assert "Log loss: 180 observations" in output
    assert "Hill k=18" in output and "Hill k=36" in output


def test_layoffs_recorded_snippet_matches_aggregate_output():
    import json
    page = ROOT / "content/incerto-layoffs-tails.md"
    record = json.loads((ROOT / "assets/incerto/outputs/layoffs-tails.json").read_text())
    expected = next(expected for _, code, expected in page_snippets(page.read_text())
                    if requires_layoffs_data(page, code))
    lines = [f"Events: {record['events']}"]
    for title, key in (("Counts", "counts"), ("Log loss", "pct_logloss_reported")):
        sample = record['samples'][key]
        lines.append(f"{title}: {sample['n']} observations")
        for point in sample['hill_reported']:
            lines.append(f"  Hill k={point['k']}: {point['alpha']:.2f}")
        fit = sample['csn']
        lines.append(f"  CSN cutoff={fit['xmin']:.3f}, tail={fit['n_tail']}, alpha={fit['alpha']:.2f}")
    assert "\n".join(lines) == expected
