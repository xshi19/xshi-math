"""Exercise retained-page repair using synthetic HTML only."""

from contextlib import redirect_stdout
import io
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import repair_legacy_mirror as repair
from site_layout import LEGACY_BASE, ORIGIN, REPO, page_file
from write_legacy_incerto import load_legacy_routes


class LegacyMirrorRepairTests(unittest.TestCase):
    def setUp(self):
        build = REPO / "_build"
        build.mkdir(exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(dir=build)
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.mirror = self.root / "mirror"
        self.mirror.mkdir()
        self.output = self.root / "overlay"
        for name in ("style.css", "icon.svg", "build/manifest.js", "build/healthy.js"):
            self.write(name, b"synthetic asset")

    def write(self, name, source):
        path = self.mirror / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(source.encode("utf-8") if isinstance(source, str) else source)
        return path

    def run_repair(self, check=False, output=None):
        stdout = io.StringIO()
        with redirect_stdout(stdout):
            code = repair.repair_mirror(self.mirror, output or self.output, check)
        return code, stdout.getvalue()

    def page(self, runtime="", body=""):
        return '<html><head><title>Fixture</title></head><body>' + body + runtime + '</body></html>'

    def broken(self):
        return '<script type="module">import "/incerto-wiki/build/missing.js";</script>'

    def test_repair_preserves_every_other_byte(self):
        head = (
            '<!DOCTYPE html>\r\n<html lang="en"><head data-test="a>b">'
            '<title>Fixture &amp; text</title>\r\n'
            '<link rel="stylesheet" href="/incerto-wiki/style.css">'
            '<link rel="icon" href="/incerto-wiki/icon.svg" />'
            '<style>.test { color: navy; }</style>'
            '<script>const theme = localStorage.getItem("example-theme");</script>'
            '<script>const historyState = window.history.state;</script>'
            '<script>sessionStorage.setItem("example", "value");</script>'
            '<script>/* window.__remixContext = {}; */'
            'const example = "window.history.state sessionStorage scrollTo";</script>'
        )
        body = (
            '</head>\r\n<body><aside>Sidebar</aside><p>数学 α &amp; β</p>'
            '<span class="katex"><math><mi>x</mi></math></span>'
            '<!-- <script type="module">this is a comment</script> -->'
            '<script src="/incerto-wiki/build/healthy.js"></script>'
        )
        preloads = (
            '<link rel="modulepreload" href="/incerto-wiki/build/missing.js"/>'
            '<LINK href="/incerto-wiki/build/healthy.js" rel="MODULEPRELOAD">'
        )
        runtime = (
            '<script>window.__remixContext = {"fixture":true};</script>'
            '<script>const key = window.history.state.key;'
            'window.scrollTo(0, sessionStorage.getItem(key));</script>'
            '<script type="module">import "/incerto-wiki/build/manifest.js";'
            'import * as route from "/incerto-wiki/build/missing.js";</script>'
            '<script type="module" src="/incerto-wiki/build/healthy.js"></script>'
        )
        source = head + preloads + body + runtime + '</body></html>\r\n'
        path = self.write("retained/index.html", source)
        before = {p.relative_to(self.mirror): p.read_bytes() for p in self.mirror.rglob("*") if p.is_file()}
        code, summary = self.run_repair()
        self.assertEqual(code, 0, summary)
        expected = (head + body + '</body></html>\r\n').replace(
            '<head data-test="a>b">', '<head data-test="a>b">' + repair.MARKER,
        )
        self.assertEqual((self.output / "retained/index.html").read_bytes(), expected.encode("utf-8"))
        self.assertEqual(path.read_bytes(), source.encode("utf-8"))
        self.assertEqual(before, {
            p.relative_to(self.mirror): p.read_bytes() for p in self.mirror.rglob("*") if p.is_file()
        })
        self.assertIn("Pages repaired: 1", summary)

    def test_healthy_page_is_untouched_and_not_emitted(self):
        source = self.page('<script type="module">import "/incerto-wiki/build/healthy.js";</script>')
        path = self.write("healthy/index.html", source)
        code, summary = self.run_repair()
        self.assertEqual(code, 0, summary)
        self.assertEqual(list(self.output.rglob("*.html")), [])
        self.assertEqual(path.read_text(), source)

    def test_only_exact_compatibility_output_paths_are_skipped(self):
        routes, _, _ = load_legacy_routes()
        route = next(route for route in routes if route != LEGACY_BASE + "/")
        relative = page_file(self.mirror, route, LEGACY_BASE).relative_to(self.mirror)
        # Even a stale page at a compatibility path is owned by that generator.
        skipped = self.write(relative, self.page(self.broken(), '<img src="/incerto-wiki/missing.png">'))
        original = skipped.read_bytes()
        self.write(relative.parent / "child/index.html", self.page(self.broken()))
        code, summary = self.run_repair()
        self.assertEqual(code, 0, summary)
        self.assertIn("compatibility paths skipped: 1", summary)
        self.assertEqual(skipped.read_bytes(), original)
        self.assertFalse((self.output / relative).exists())
        self.assertTrue((self.output / relative.parent / "child/index.html").is_file())

    def test_missing_other_assets_abort_before_writing_any_pages(self):
        self.write("retained/index.html", self.page(self.broken()))
        for tag in (
            '<link rel="stylesheet" href="/incerto-wiki/missing.css">',
            '<img src="/incerto-wiki/missing.png">',
            '<link rel="preload" as="font" href="/incerto-wiki/missing.woff2">',
            '<link rel="preload" as="fetch" href="/incerto-wiki/missing.json">',
            '<script src="/incerto-wiki/missing.js"></script>',
            '<iframe src="../missing.html"></iframe>',
            '<a href="/incerto-wiki/missing.pdf">Download</a>',
        ):
            with self.subTest(tag=tag):
                self.write("other/index.html", self.page(body=tag))
                code, summary = self.run_repair()
                self.assertEqual(code, 1, summary)
                self.assertIn("missing asset", summary)
                self.assertFalse(self.output.exists())

    def test_existing_overlay_survives_a_failed_scan(self):
        self.write("retained/index.html", self.page(self.broken()))
        self.assertEqual(self.run_repair()[0], 0)
        previous = (self.output / "retained/index.html").read_bytes()
        self.write("other/index.html", self.page(body='<img src="/incerto-wiki/missing.png">'))
        self.assertEqual(self.run_repair()[0], 1)
        self.assertEqual((self.output / "retained/index.html").read_bytes(), previous)

    def test_known_gaps_warn_and_allow_repair_and_check(self):
        iframe = '<iframe src="../assets/graphs/concept-graph.html"></iframe>'
        stylesheet = '<link rel="stylesheet" href="/incerto-wiki/css/concept-graph.css">'
        self.write("dependency-dag/index.html", self.page(self.broken(), iframe))
        self.write("retained/index.html", self.page(self.broken()))
        self.write("build/concept-list-7ef20491bebc3cb4a7d50502026374c8.html",
                   self.page(body=stylesheet))
        code, summary = self.run_repair(check=True)
        self.assertEqual(code, 1, summary)  # Known gaps do not excuse needed repairs.
        self.assertIn("Pages needing repair: 1", summary)
        self.assertNotIn("ERROR:", summary)
        self.assertFalse(self.output.exists())
        code, summary = self.run_repair()
        self.assertEqual(code, 0, summary)
        self.assertIn("Warnings: 1", summary)
        self.assertEqual(summary.count("KNOWN GAP:"), 1)
        self.assertNotIn("dependency-dag/index.html", summary)
        self.assertIn("incerto-graph-assets", summary)
        self.assertNotIn("ERROR:", summary)
        self.assertFalse((self.output / "dependency-dag/index.html").exists())
        self.assertTrue((self.output / "retained/index.html").exists())
        self.assertEqual(len(list(self.output.rglob("*.html"))), 1)
        shutil.copytree(self.output, self.mirror, dirs_exist_ok=True)
        result = subprocess.run([
            sys.executable, str(REPO / "scripts/repair_legacy_mirror.py"),
            "--mirror", str(self.mirror), "--check",
        ], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("static-retained pages verified: 1", result.stdout)
        self.assertIn("Pages needing repair: 0", result.stdout)
        self.assertEqual(result.stdout.count("KNOWN GAP:"), 1)

    def test_known_gap_allowances_require_both_exact_paths(self):
        for relative, asset in (
            ("other/index.html", "assets/graphs/concept-graph.html"),
            ("other/index.html", "css/concept-graph.css"),
            ("other-dag/index.html", "assets/graphs/other.html"),
            ("build/concept-list-7ef20491bebc3cb4a7d50502026374c8.html", "css/other.css"),
        ):
            with self.subTest(relative=relative, asset=asset):
                path = self.write(relative, self.page(body=f'<iframe src="/incerto-wiki/{asset}"></iframe>'))
                for check in (False, True):
                    code, summary = self.run_repair(check=check)
                    self.assertEqual(code, 1, summary)
                    self.assertIn("ERROR:", summary)
                    self.assertIn(f"missing asset: /incerto-wiki/{asset}", summary)
                    self.assertNotIn("KNOWN GAP:", summary)
                    self.assertFalse(self.output.exists())
                path.unlink()

    def test_stale_known_gap_allowances_warn_without_failing(self):
        for relative, asset in (
            ("build/concept-list-7ef20491bebc3cb4a7d50502026374c8.html", "css/concept-graph.css"),
        ):
            self.write(relative, self.page(body=f'<iframe src="/incerto-wiki/{asset}"></iframe>'))
            self.write(asset, self.page() if asset.endswith(".html") else "/* synthetic stylesheet */")
        for check in (True, False):
            with self.subTest(check=check):
                code, summary = self.run_repair(check=check)
                self.assertEqual(code, 0, summary)
                self.assertIn("Warnings: 1", summary)
                self.assertEqual(summary.count("STALE ALLOWANCE: asset now exists:"), 1)
                self.assertNotIn("KNOWN GAP:", summary)
                self.assertNotIn("ERROR:", summary)
                self.assertIn("Pages needing repair: 0", summary)

    def test_check_ignores_unrelated_output_directory(self):
        self.write("retained/index.html", self.page())
        self.output.mkdir()
        unrelated = self.output / "keep.txt"
        unrelated.write_text("unrelated")
        self.assertEqual(self.run_repair(check=True)[0], 0)
        self.assertEqual(unrelated.read_text(), "unrelated")

    def test_idempotence_and_stale_generated_output_removal(self):
        self.write("retained/index.html", self.page(self.broken()))
        self.assertEqual(self.run_repair()[0], 0)
        shutil.copytree(self.output, self.mirror, dirs_exist_ok=True)
        source = (self.mirror / "retained/index.html").read_bytes()
        code, summary = self.run_repair()
        self.assertEqual(code, 0, summary)
        self.assertIn("Pages needing repair: 0", summary)
        self.assertIn("static-retained pages verified: 1", summary)
        self.assertEqual(list(self.output.rglob("*.html")), [])
        self.assertEqual((self.mirror / "retained/index.html").read_bytes(), source)
        self.assertEqual(self.run_repair(check=True)[0], 0)

    def test_marker_pages_are_reverified_instead_of_trusted(self):
        for extra in (
            '<img src="/incerto-wiki/missing.png">', self.broken(),
            '<script type="module">import "/incerto-wiki/build/healthy.js";</script>',
            '<link rel="modulepreload" href="/incerto-wiki/build/healthy.js">',
            '<script>window.__remixContext = {};</script>', repair.MARKER,
        ):
            with self.subTest(extra=extra):
                self.write("retained/index.html", self.page(extra).replace('<head>', '<head>' + repair.MARKER))
                self.assertEqual(self.run_repair(check=True)[0], 1)
                self.assertEqual(self.run_repair()[0], 1)
                self.assertFalse(self.output.exists())

    def test_check_cli_exit_codes_and_no_writes(self):
        command = [sys.executable, str(REPO / "scripts/repair_legacy_mirror.py"),
                   "--mirror", str(self.mirror), "--out", str(self.output), "--check"]
        for source, expected in (
            (self.page(), 0), (self.page(self.broken()), 1),
            (self.page(body='<img src="/incerto-wiki/missing.png">'), 1),
        ):
            with self.subTest(expected=expected, source=source):
                self.write("retained/index.html", source)
                result = subprocess.run(command, capture_output=True, text=True)
                self.assertEqual(result.returncode, expected, result.stdout + result.stderr)
                self.assertFalse(self.output.exists())
        self.write("retained/index.html", self.page(self.broken()))
        self.assertEqual(self.run_repair()[0], 0)
        previous = (self.output / "retained/index.html").read_bytes()
        self.assertEqual(subprocess.run(command, capture_output=True).returncode, 1)
        self.assertEqual((self.output / "retained/index.html").read_bytes(), previous)

    def test_literal_and_percent_encoded_dollars_resolve_to_same_file(self):
        bundle = self.write("build/routes/$-example.js", "// synthetic module")
        self.write("retained/index.html", self.page(
            '<link rel="modulepreload" href="/incerto-wiki/build/routes/%24-example.js?v=1#x">'
            '<script type="module">import * as route from "/incerto-wiki/build/routes/$-example.js";</script>'
        ))
        self.assertEqual(self.run_repair(check=True)[0], 0)
        bundle.unlink()
        self.assertEqual(self.run_repair(check=True)[0], 1)
        self.assertEqual(self.run_repair()[0], 0)

    def test_missing_inline_imports_without_preloads_trigger_repair(self):
        for statement in (
            'import "/incerto-wiki/build/missing.js";',
            "import * as route from '/incerto-wiki/build/missing.js';",
            'import { thing } from "/incerto-wiki/build/missing.js";',
            'import("/incerto-wiki/build/missing.js").then(run);',
        ):
            with self.subTest(statement=statement):
                self.write("retained/index.html", self.page('<script type="module">' + statement + '</script>'))
                code, summary = self.run_repair()
                self.assertEqual(code, 0, summary)
                self.assertIn("Pages repaired: 1", summary)

    def test_import_examples_in_comments_and_strings_are_not_requests(self):
        source = self.page('''<script type="module">
// import "/incerto-wiki/build/missing.js";
/* import * as route from "/incerto-wiki/build/missing.js"; */
const example = 'import "/incerto-wiki/build/missing.js";';
const template = `import "/incerto-wiki/build/missing.js";`;
import "/incerto-wiki/build/healthy.js";
</script>''')
        self.write("retained/index.html", source)
        self.assertEqual(self.run_repair(check=True)[0], 0)

    def test_navigation_aliases_relative_urls_external_urls_and_anchors(self):
        self.write("destination/index.html", "<p>Destination</p>")
        self.write("file.html", "<p>File</p>")
        body = ''.join(f'<a href="{url}">Link</a>' for url in (
            "/incerto-wiki/destination", "/incerto-wiki/destination/",
            "/incerto-wiki/destination/index.html?a=1&amp;b=2#fragment",
            "../file.html", ORIGIN + "/incerto-wiki/file.html", "#fragment",
            "https://example.org/incerto-wiki/absent.html", "//example.org/missing.js",
        ))
        self.write("retained/index.html", self.page(body=body))
        code, summary = self.run_repair(check=True)
        self.assertEqual(code, 0, summary)
        self.assertIn("Warnings: 0", summary)

    def test_missing_navigation_is_warning_only_and_empty_directory_is_missing(self):
        (self.mirror / "empty").mkdir()
        body = (
            '<a href="/incerto-wiki/missing.html">Link</a>'
            '<a href="../empty/">Empty</a>'
            '<link rel="next" href="/incerto-wiki/missing.html">'
        )
        self.write("retained/index.html", self.page(self.broken(), body))
        code, summary = self.run_repair()
        self.assertEqual(code, 0, summary)
        self.assertIn("Warnings: 2", summary)
        self.assertIn("missing navigation target", summary)
        shutil.copytree(self.output, self.mirror, dirs_exist_ok=True)
        self.assertEqual(self.run_repair(check=True)[0], 0)

    def test_unrendered_template_references_are_reported(self):
        source = self.page(body='<link rel="stylesheet" href="{{ asset_path }}">')
        self.write("api/template.html", source)
        code, summary = self.run_repair(check=True)
        self.assertEqual(code, 0, summary)
        self.assertIn("unexpanded template reference", summary)

    def test_no_output_if_missing_module_survives_in_a_classic_script(self):
        self.write("retained/index.html", self.page('<script src="/incerto-wiki/build/missing.js"></script>'))
        code, summary = self.run_repair()
        self.assertEqual(code, 1, summary)
        self.assertIn("missing asset after repair", summary)
        self.assertFalse(self.output.exists())

    def test_output_guards_protect_mirror_and_unrelated_files(self):
        self.write("retained/index.html", self.page(self.broken()))
        alias = self.root / "alias"
        alias.symlink_to(self.mirror, target_is_directory=True)
        for output in (self.mirror, self.mirror / "nested", self.root, alias, alias / "nested"):
            with self.subTest(output=output), self.assertRaises(ValueError):
                self.run_repair(output=output)
        self.output.mkdir()
        unrelated = self.output / "keep.txt"
        unrelated.write_text("unrelated")
        with self.assertRaises(ValueError):
            self.run_repair()
        self.assertEqual(unrelated.read_text(), "unrelated")


if __name__ == "__main__":
    unittest.main()
