"""Exercise URL-map edge cases and the emitted redirect JavaScript with Node."""

import csv
from contextlib import redirect_stdout
import io
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import check_html
import write_legacy_incerto
from site_layout import ORIGIN, normalize_page_path, page_file
from write_legacy_incerto import load_legacy_routes, render_page


class LegacyRedirectTests(unittest.TestCase):
    def setUp(self):
        # Keep even temporary test outputs inside the repository.
        root = Path(__file__).resolve().parents[1] / "_build"
        root.mkdir(exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(dir=root)
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.csv = self.root / "url-map.csv"

    def load(self, rows):
        with self.csv.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.writer(handle)
            writer.writerow([
                "source_id", "old_url", "old_fragment", "new_url", "new_fragment",
                "route_behavior", "verification_status",
            ])
            for old, old_fragment, new, new_fragment in rows:
                writer.writerow(["test", ORIGIN + old, old_fragment,
                                 ORIGIN + new if new else "", new_fragment,
                                 "owner decision pending", "test fixture"])
        return load_legacy_routes(self.csv)

    def test_home_alias_notation_and_unresolved(self):
        pages, mapped, skipped = self.load([
            ("/incerto-wiki/", "", "/math/incerto", ""),
            ("/incerto-wiki/index.html", "", "/math/incerto/", ""),
            ("/incerto-wiki/index-1", "", "/math/notation", ""),
            ("/incerto-wiki/build/index-export.md", "", "", ""),
        ])
        self.assertEqual((len(pages), mapped, len(skipped)), (2, 3, 1))
        self.assertEqual(pages["/incerto-wiki/index-1/"].target, ORIGIN + "/math/notation/")
        self.assertIn("owner decision pending", skipped[0]["reason"])
        self.assertEqual(page_file(self.root, "/incerto-wiki/index.html", "/incerto-wiki"),
                         self.root / "index.html")

    def test_reject_conflicts_missing_fallback_and_unsafe_paths(self):
        cases = [
            [("/incerto-wiki/", "", "/math/incerto/", ""),
             ("/incerto-wiki/index.html", "", "/math/notation/", "")],
            [("/incerto-wiki/", "old", "/math/incerto/", "new")],
            [("/incerto-wiki/", "", "/normix/", "")],
            [("/incerto-wiki/../outside", "", "/math/incerto/", "")],
            [("/incerto-wiki/", "", "/math/%2e%2e/outside", "")],
            [("/incerto-wiki/?query=1", "", "/math/incerto/", "")],
        ]
        for rows in cases:
            with self.subTest(rows=rows), self.assertRaises(ValueError):
                self.load(rows)
        self.assertEqual(normalize_page_path("/incerto-wiki/pareto"), "/incerto-wiki/pareto/")

    def test_javascript_query_hash_translation_and_escaping(self):
        dangerous = '</script><a href="&">'
        pages, _, _ = self.load([
            ("/incerto-wiki/pareto/", "", "/math/incerto/incerto-pareto", "default"),
            ("/incerto-wiki/pareto/", "old label", "/math/incerto/incerto-pareto", "new-label"),
            ("/incerto-wiki/pareto/", dangerous, "/math/notation/", "new-label"),
        ])
        source = render_page(pages["/incerto-wiki/pareto/"])
        self.assertNotIn(dangerous, source)
        parser = check_html.Links()
        parser.feed(source)
        script = re.search(r"<script>\n(.*?)</script>", source, re.S).group(1)
        harness = r"""
const vm = require('node:vm');
const input = JSON.parse(require('node:fs').readFileSync(0, 'utf8'));
const outputs = input.hashes.map(hash => {
  let output;
  const location = {search: '?a=1&b=%2F', hash, replace: value => {output = value;}};
  vm.runInNewContext(input.script, {
    URL, window: {location},
    document: {getElementById: () => ({textContent: input.data})}
  });
  return output;
});
process.stdout.write(JSON.stringify(outputs));
"""
        result = subprocess.run(["node", "-e", harness], text=True, check=True,
                                input=json.dumps({"script": script, "data": parser.redirect_data[0],
                                                  "hashes": ["", "#old%20label", "#unknown", "#bad%ZZ"]}),
                                capture_output=True)
        base = ORIGIN + "/math/incerto/incerto-pareto/?a=1&b=%2F"
        self.assertEqual(json.loads(result.stdout), [base + fragment for fragment in
                                                    ("#default", "#new-label", "#unknown", "#bad%ZZ")])

    def test_checker_detects_corrupt_or_missing_artifacts(self):
        routes = self.load([("/incerto-wiki/", "", "/math/incerto/", "destination")])
        legacy = self.root / "legacy"
        html = self.root / "math"
        legacy.mkdir()
        (html / "incerto").mkdir(parents=True)
        target = html / "incerto/index.html"
        target.write_text('<h1 id="destination">Destination</h1>')
        output = legacy / "index.html"
        source = render_page(routes[0]["/incerto-wiki/"])

        def document(path):
            text = path.read_text()
            parser = check_html.Links()
            parser.feed(text)
            return text, parser

        def check():
            failures = []
            with patch.object(check_html, "LEGACY_HTML", legacy), \
                    patch.object(check_html, "HTML", html), \
                    patch.object(check_html, "load_legacy_routes", return_value=routes), \
                    redirect_stdout(io.StringIO()):
                check_html.check_legacy(failures, document)
            return failures

        output.write_text(source)
        self.assertEqual(check(), [])
        for before, after in [
            ('content="noindex"', 'content="index"'),
            ('rel="canonical"', 'rel="alternate"'),
            ('0; url=', '1; url='),
            ('<a href=', '<span data-href='),
            ('window.location.replace(target.href);', ''),
            ('"fragments": {}', '"fragments": {"wrong": "target"}'),
        ]:
            with self.subTest(before=before):
                output.write_text(source.replace(before, after))
                self.assertTrue(check())
        output.write_text(source)
        target.write_text('<h1>No matching fragment</h1>')
        self.assertTrue(check())
        target.unlink()
        self.assertTrue(check())
        output.unlink()
        self.assertTrue(check())

    def test_generation_replaces_stale_output_and_requires_targets(self):
        routes = self.load([
            ("/incerto-wiki/", "", "/math/incerto/", ""),
            ("/incerto-wiki/index.html", "", "/math/incerto/", ""),
        ])
        legacy = self.root / "legacy"
        html = self.root / "math"
        legacy.mkdir()
        stale = legacy / "stale.html"
        stale.write_text("stale generated output")
        (html / "incerto").mkdir(parents=True)
        target = html / "incerto/index.html"
        target.write_text("<h1>Destination</h1>")
        with patch.object(write_legacy_incerto, "LEGACY_HTML", legacy), \
                patch.object(write_legacy_incerto, "HTML", html), \
                patch.object(write_legacy_incerto, "load_legacy_routes", return_value=routes), \
                redirect_stdout(io.StringIO()):
            write_legacy_incerto.main()
            self.assertFalse(stale.exists())
            self.assertEqual(list(legacy.iterdir()), [legacy / "index.html"])
            target.unlink()
            with self.assertRaises(SystemExit):
                write_legacy_incerto.main()


if __name__ == "__main__":
    unittest.main()
