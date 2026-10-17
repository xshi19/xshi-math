"""Stage static retained pages from a legacy mirror with missing Remix modules.

The mirror is read-only input. Output contains only repaired HTML, for overlay
without --delete; it is not a replacement for the mirror or its assets.
"""

import argparse
from html.parser import HTMLParser
from pathlib import Path
import re
import shutil
from urllib.parse import unquote, urljoin, urlsplit

from site_layout import LEGACY_BASE, LEGACY_HTML, ORIGIN, page_file
from write_legacy_incerto import load_legacy_routes

OUTPUT = LEGACY_HTML.parent / "retained-repair" / LEGACY_HTML.name
MARKER = '<meta name="xshi-math-legacy" content="static-retained">'
# Exact (referring file, asset) paths relative to the mirror, never wildcards.
# The operator confirmed these gaps in the 2026-10-10 live snapshot. Restoration
# awaits the deferred DAG decision; the runbook forbids copying private source.
# Warn when an asset returns so the allowance can be reviewed and removed.
KNOWN_MISSING_ASSETS = {
    ("dependency-dag/index.html", "assets/graphs/concept-graph.html"): (
        "Deferred iframe; migration-manifest.csv rows incerto-dependency-dag / "
        "incerto-graph-assets"
    ),
    ("build/concept-list-7ef20491bebc3cb4a7d50502026374c8.html", "css/concept-graph.css"): (
        "Deferred graph stylesheet; migration-manifest.csv rows incerto-dependency-dag / "
        "incerto-graph-assets"
    ),
}
# Static side-effect, namespace, default and named imports, plus literal dynamic
# imports used by the legacy entry-client loader. No JavaScript is executed.
JS_LITERAL_OR_COMMENT = (
    r"//[^\r\n]*|/\*[\s\S]*?\*/|"
    r'''"(?:\\.|[^"\\])*"|'(?:\\.|[^'\\])*'|`(?:\\.|[^`\\])*`'''
)
IMPORT = re.compile(
    JS_LITERAL_OR_COMMENT + r"|\bimport\s*(?:[\w$*,{}\s]+\s+from\s*|\(\s*)?"
    r"(?P<quote>['\"])(?P<url>[^'\"\r\n]+)(?P=quote)"
)
CONTEXT = re.compile(r"\bwindow\s*\.\s*__remixContext\s*=(?!=)")


class LegacyHTML(HTMLParser):
    """Collect references and exact source spans; never serialize parsed HTML."""

    def __init__(self, source):
        super().__init__(convert_charrefs=True)
        self.source = source
        self.lines = [0]
        self.lines.extend(match.end() for match in re.finditer("\n", source))
        self.references = []
        self.removals = []
        self.modules = 0
        self.markers = 0
        self.head_end = None
        self.script = None
        self.feed(source)
        self.close()
        if self.script is not None:
            raise ValueError("Unclosed script element")

    def source_offset(self):
        line, column = self.getpos()
        return self.lines[line - 1] + column

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        start = self.source_offset()
        end = start + len(self.get_starttag_text())
        rel = (attrs.get("rel") or "").lower().split()
        for key in ("src", "href"):
            if attrs.get(key):
                navigation = key == "href" and (
                    tag in {"a", "area"}
                    or (tag == "link" and bool(
                        {"canonical", "alternate", "prev", "next", "up"} & set(rel)
                    ))
                )
                self.references.append((attrs[key], navigation))
        if tag == "head":
            self.head_end = end
        if (tag == "meta" and attrs.get("name") == "xshi-math-legacy"
                and attrs.get("content") == "static-retained"):
            self.markers += 1
        if tag == "link" and "modulepreload" in rel:
            self.removals.append((start, end))
        if tag == "script":
            module = (attrs.get("type") or "").strip().lower() == "module"
            self.modules += module
            self.script = (start, end, module, "src" in attrs)

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag == "script":
            # HTML script elements require an end tag even with a trailing slash.
            raise ValueError("Self-closing script element is unsupported")

    def handle_endtag(self, tag):
        if tag != "script" or self.script is None:
            return
        start, body_start, module, external = self.script
        body = self.source[body_start:self.source_offset()]
        if module and not external:
            self.references.extend((match["url"], False) for match in IMPORT.finditer(body)
                                   if match["url"] is not None)
        code = re.sub(JS_LITERAL_OR_COMMENT, " ", body)
        scroll = all(token in code for token in (
            "window.history.state", "sessionStorage", "scrollTo",
        ))
        if module or (not external and (CONTEXT.search(code) or scroll)):
            end = self.source.index(">", self.source_offset()) + 1
            self.removals.append((start, end))
        self.script = None

    def static_source(self):
        if self.head_end is None:
            raise ValueError("Cannot insert static marker: no head element")
        edits = [(start, end, "") for start, end in self.removals]
        edits.append((self.head_end, self.head_end, MARKER))
        result = self.source
        for start, end, replacement in sorted(edits, reverse=True):
            result = result[:start] + replacement + result[end:]
        return result


def missing_references(document, relative, mirror):
    """Return missing modules, asset errors, and warnings (including known gaps)."""
    modules, assets, warnings = set(), set(), set()
    page_url = f"{ORIGIN}{LEGACY_BASE}/{relative.as_posix()}"
    for reference, navigation in document.references:
        reference = reference.strip()
        if not reference or reference.startswith("#"):
            continue
        url = urlsplit(urljoin(page_url, reference))
        if url.scheme not in {"http", "https"} or url.netloc != urlsplit(ORIGIN).netloc:
            continue
        path = unquote(url.path)
        if path != LEGACY_BASE and not path.startswith(LEGACY_BASE + "/"):
            continue
        # The frozen API tree also contains unrendered Sphinx template assets.
        # Their placeholders are not concrete URLs; retain and report them.
        if "{{" in reference or "{%" in reference:
            warnings.add(f"unexpanded template reference: {reference}")
            continue
        asset_relative = path.removeprefix(LEGACY_BASE).lstrip("/")
        target = mirror / asset_relative
        if not target.resolve().is_relative_to(mirror):
            assets.add(f"reference escapes mirror: {reference}")
            continue
        reason = KNOWN_MISSING_ASSETS.get((relative.as_posix(), asset_relative))
        if target.is_file() or (target / "index.html").is_file():
            if reason:
                warnings.add(f"STALE ALLOWANCE: asset now exists: {asset_relative} ({reason})")
            continue
        suffix = Path(path).suffix.lower()
        if navigation and suffix in {"", ".html", ".htm"}:
            warnings.add(f"missing navigation target: {reference}")
        elif path.startswith(LEGACY_BASE + "/build/") and suffix == ".js":
            modules.add(reference)
        elif reason:
            warnings.add(f"KNOWN GAP: missing asset: {asset_relative} ({reason})")
        else:
            assets.add(reference)
    return modules, assets, warnings


def validate_static(document, relative, mirror):
    modules, assets, _ = missing_references(document, relative, mirror)
    errors = [f"missing asset after repair: {ref}" for ref in sorted(modules | assets)]
    if document.markers != 1:
        errors.append("expected exactly one static-retained marker")
    if document.modules or document.removals:
        errors.append("static-retained page still contains Remix runtime tags")
    return errors


def validate_output(output, mirror):
    """Only refresh a separate directory containing this tool's generated HTML."""
    if output.is_symlink():
        raise ValueError("Output must not be a symlink")
    output = output.resolve()
    if output.is_relative_to(mirror) or mirror.is_relative_to(output):
        raise ValueError("Output and mirror must be separate, non-overlapping directories")
    if output.exists():
        if not output.is_dir():
            raise ValueError("Output must be a directory")
        for path in output.rglob("*"):
            if path.is_symlink():
                raise ValueError(f"Output contains a symlink: {path}")
            if path.is_file() and (
                path.suffix != ".html"
                or LegacyHTML(path.read_bytes().decode("utf-8")).markers != 1
            ):
                raise ValueError(f"Output contains a file not generated by this tool: {path}")
    return output


def repair_mirror(mirror, output=OUTPUT, check=False):
    mirror = Path(mirror).resolve()
    if not mirror.is_dir():
        raise ValueError(f"Mirror is not a directory: {mirror}")
    # Check mode depends only on the mirror, regardless of any old output tree.
    if not check:
        output = validate_output(Path(output), mirror)
    routes, _, _ = load_legacy_routes()
    compatibility = {
        page_file(mirror, route, LEGACY_BASE).relative_to(mirror) for route in routes
    }
    scanned = skipped = verified = 0
    repairs, warnings, errors = {}, [], []
    for path in sorted(mirror.rglob("*.html")):
        scanned += 1
        relative = path.relative_to(mirror)
        if relative in compatibility:
            skipped += 1
            continue
        try:
            document = LegacyHTML(path.read_bytes().decode("utf-8"))
            modules, assets, page_warnings = missing_references(document, relative, mirror)
            warnings.extend(f"{relative}: {warning}" for warning in sorted(page_warnings))
            errors.extend(f"{relative}: missing asset: {ref}" for ref in sorted(assets))
            if document.markers:
                page_errors = validate_static(document, relative, mirror)
                errors.extend(f"{relative}: {error}" for error in page_errors)
                verified += not page_errors
            elif modules:
                repaired = document.static_source()
                page_errors = validate_static(LegacyHTML(repaired), relative, mirror)
                errors.extend(f"{relative}: {error}" for error in page_errors)
                repairs[relative] = repaired.encode("utf-8")
        except (OSError, UnicodeError, ValueError) as error:
            errors.append(f"{relative}: {error}")

    print(f"Pages scanned: {scanned}; compatibility paths skipped: {skipped}; "
          f"static-retained pages verified: {verified}")
    print(f"Pages needing repair: {len(repairs)}")
    for relative in repairs:
        print(f"  {relative}")
    print(f"Warnings: {len(warnings)}")
    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}")
    if check or errors:
        print("Pages repaired: 0 (check mode)" if check else "Pages repaired: 0 (errors; no output written)")
        return int(bool(errors or (check and repairs)))

    # Validate the entire scan before replacing any previously generated output.
    # Removing this dedicated tree prevents stale repairs from being overlaid.
    if output.exists():
        shutil.rmtree(output)
    output.mkdir(parents=True)
    for relative, source in repairs.items():
        target = output / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(source)
    print(f"Pages repaired: {len(repairs)}. Output: {output}")
    return 0


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mirror", type=Path, required=True,
                        help="Read-only input: the hub's incerto-wiki directory")
    parser.add_argument("--out", type=Path, default=OUTPUT,
                        help=f"Dedicated generated overlay directory (default: {OUTPUT})")
    parser.add_argument("--check", action="store_true",
                        help="Write nothing; exit 1 for needed repairs or asset errors")
    args = parser.parse_args(argv)
    try:
        return repair_mirror(args.mirror, args.out, args.check)
    except (OSError, UnicodeError, ValueError) as error:
        print(f"ERROR: {error}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
