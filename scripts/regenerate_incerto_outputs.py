"""Regenerate Incerto Output blocks from execution: uv run python scripts/regenerate_incerto_outputs.py.

Reuse the snippet tests' isolated runner, including its no-network/no-repository-
writes policy. The NYC full demo runs from a temporary copy so its figure writes
stay outside the repository. Only captured text replaces the recorded outputs.
When the local layoffs CSV is absent, rebuild its selected-estimate output
from the summary JSON without regenerating figures. When the local S&P CSV
is absent, preserve the dated observed output and report that it was skipped.
"""

import argparse
import json
from pathlib import Path
import re
import runpy
from tempfile import mkdtemp


ROOT = Path(__file__).resolve().parents[1]


def recorded_layoffs_output():
    demo = runpy.run_path(str(ROOT / 'demos/incerto/layoffs_tails.py'))
    result = json.loads((ROOT / 'assets/incerto/outputs/layoffs-tails.json').read_text())
    return demo['page_summary'](result)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pages", nargs="+", help="Only these page stems (without .md)")
    args = parser.parse_args()
    harness = runpy.run_path(str(ROOT / "tests/test_incerto_page_snippets.py"))
    scratch = Path(mkdtemp(prefix="incerto-outputs-"))
    updates = {}
    count = 0
    recorded_count = 0
    pages = [p for p in harness["PAGES"] if args.pages is None or p.stem in args.pages]
    unknown = set(args.pages or []) - {p.stem for p in pages}
    if unknown:
        parser.error(f"Unknown page stems: {sorted(unknown)}")
    for page in pages:
        text = page.read_text()
        replacements = []
        for index, block in enumerate(harness["PYTHON_BLOCK"].finditer(text), 1):
            expected = harness["OUTPUT_BLOCK"].match(text, block.end())
            if expected is None:
                raise ValueError(f"Missing Output block: {page.name}:{index}")
            if (harness["requires_sp500_data"](page, block.group(1))
                    and not harness["sp500_data_available"]()):
                print(f"Preserved dated S&P output: {page.name}:{index} (local CSV absent)")
                continue
            if (harness["requires_layoffs_data"](page, block.group(1))
                    and not harness["layoffs_data_available"]()):
                output = recorded_layoffs_output()
                recorded_count += 1
                print(f"Rebuilt from summary JSON: {page.name}:{index} (local CSV absent)")
            else:
                output = harness["run_snippet"](page, index, block.group(1), scratch)
                count += 1
                if count % 15 == 0:
                    print(f"Executed {count} snippets", flush=True)
            harness["assert_plain_numbers"](output)
            replacements.append((*expected.span(1), output.rstrip("\n")))
        for start, end, output in reversed(replacements):
            text = text[:start] + output + text[end:]
        if replacements:
            updates[page] = text

    demo_count = 0
    if args.pages is None or "incerto-nyc-dog-name-tail" in args.pages:
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

        demo_count = 1

    # Finish every execution and format check before updating any page.
    changed = 0
    for page, text in updates.items():
        if page.read_text() != text:
            page.write_text(text)
            changed += 1
    print(f"Regenerated {count} executed snippet outputs, {recorded_count} summary-derived outputs, "
          f"and {demo_count} full-demo output; changed {changed} pages.")
    print(f"Temporary execution files: {scratch}")


if __name__ == "__main__":
    main()
