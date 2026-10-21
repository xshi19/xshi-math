"""Regenerate Incerto Output blocks from execution: uv run python scripts/regenerate_incerto_outputs.py.

Reuse the snippet tests' isolated runner, including its no-network/no-repository-
writes policy. The NYC full demo runs from a temporary copy so its figure writes
stay outside the repository. Only captured text replaces the recorded outputs.
"""

from pathlib import Path
import re
import runpy
from tempfile import mkdtemp


ROOT = Path(__file__).resolve().parents[1]


def main():
    harness = runpy.run_path(str(ROOT / "tests/test_incerto_page_snippets.py"))
    scratch = Path(mkdtemp(prefix="incerto-outputs-"))
    updates = {}
    count = 0
    for page in harness["PAGES"]:
        text = page.read_text()
        replacements = []
        for index, block in enumerate(harness["PYTHON_BLOCK"].finditer(text), 1):
            expected = harness["OUTPUT_BLOCK"].match(text, block.end())
            if expected is None:
                raise ValueError(f"Missing Output block: {page.name}:{index}")
            output = harness["run_snippet"](page, index, block.group(1), scratch)
            harness["assert_plain_numbers"](output)
            replacements.append((*expected.span(1), output.rstrip("\n")))
            count += 1
            if count % 15 == 0:
                print(f"Executed {count} snippets", flush=True)
        for start, end, output in reversed(replacements):
            text = text[:start] + output + text[end:]
        if replacements:
            updates[page] = text

    page = ROOT / "content/incerto-nyc-dog-name-tail.md"
    demo = scratch / "demos/incerto/nyc_dog_name_tail.py"
    demo.parent.mkdir(parents=True)
    demo.write_text((ROOT / "demos/incerto/nyc_dog_name_tail.py").read_text())
    code = f"import runpy\nrunpy.run_path({str(demo)!r}, run_name='__main__')"
    output = harness["run_snippet"](page, "full-demo", code, scratch)
    harness["assert_plain_numbers"](output)
    recorded = re.search(
        r"^:::\{dropdown\} Output: full demo\n\s*```text\n(.*?)\n```",
        updates[page], re.M | re.S,
    )
    if recorded is None:
        raise ValueError("Missing NYC full-demo Output block")
    updates[page] = (
        updates[page][:recorded.start(1)] + output.rstrip("\n")
        + updates[page][recorded.end(1):]
    )

    # Finish every execution and format check before updating any page.
    changed = 0
    for page, text in updates.items():
        if page.read_text() != text:
            page.write_text(text)
            changed += 1
    print(f"Regenerated {count} snippet outputs and 1 full-demo output; changed {changed} pages.")
    print(f"Temporary execution files: {scratch}")


if __name__ == "__main__":
    main()
