"""Check all 38 foundation, IG, Incerto, and Normix pages under BASE_URL=/math.

Run after ``npm run build``. This checks files and URLs, not browser behavior.
"""

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit

ROOT = Path(__file__).resolve().parents[1] / "_build" / "html"
BASE = "/math"
PAGES = (
    "index.html",
    "incerto/index.html",
    "incerto-counting-exceedances/index.html",
    "incerto-pareto/index.html",
    "incerto-regular-variation/index.html",
    "incerto-karamata/index.html",
    "incerto-pareto-moment-existence/index.html",
    "incerto-mean-excess-function/index.html",
    "incerto-hill-estimator/index.html",
    "incerto-extreme-value-index/index.html",
    "incerto-generalized-pareto/index.html",
    "incerto-plug-in-tail-estimation/index.html",
    "incerto-pickands-balkema-de-haan/index.html",
    "incerto-generalized-extreme-value/index.html",
    "incerto-frechet/index.html",
    "incerto-tail-threshold-selection/index.html",
    "incerto-subexponentiality/index.html",
    "incerto-survival-tail-ratio/index.html",
    "incerto-max-to-sum-ratio/index.html",
    "incerto-double-pareto/index.html",
    "incerto-body-shoulder-tail/index.html",
    "information-geometry/index.html",
    "information-geometry-euclidean-to-manifold/index.html",
    "information-geometry-exponential-families/index.html",
    "information-geometry-latent-variables-em/index.html",
    "information-geometry-conditional-expectation/index.html",
    "information-geometry-fisher-vs-l2/index.html",
    "information-geometry-duality/index.html",
    "normix-theory/index.html",
    "normix-conditioning-a-mixture/index.html",
    "normix-generalized-inverse-gaussian/index.html",
    "normix-generalized-hyperbolic/index.html",
    "normix-em-algorithm/index.html",
    "normix-exponential-family-core/index.html",
    "normix-mixture-architecture/index.html",
    "normix-why-not-gradient-descent/index.html",
    "normix-gh-family-tour/index.html",
    "normix-normal-mixtures/index.html",
)
# Every note (including all twenty-six imports) and the IG hub require KaTeX display
# equations. Exclude only the three hubs without equations, so new notes inherit
# the math check instead of silently passing with unrendered source formulas.
MATH_PAGES = set(PAGES) - {
    "index.html", "incerto/index.html", "normix-theory/index.html"
}


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.urls = []
        self.ids = set()
        self.math_count = 0
        self.display_math_count = 0
        self.math_errors = 0

    def handle_starttag(self, tag, attrs):
        for name, value in attrs:
            if name in {"href", "src"} and value:
                self.urls.append(value)
            if (name == "id" or (tag == "a" and name == "name")) and value:
                self.ids.add(value)
            if name == "class" and value:
                classes = value.split()
                self.math_count += "katex" in classes
                self.display_math_count += "katex-display" in classes
                self.math_errors += "katex-error" in classes


def main() -> None:
    failures = []
    styles = set()
    documents = {}

    def document(path):
        if path not in documents:
            source = path.read_text(encoding="utf-8")
            parser = Links()
            parser.feed(source)
            documents[path] = (source, parser)
        return documents[path]

    for name in PAGES:
        page = ROOT / name
        if not page.is_file():
            failures.append(f"missing page: {name}")
            continue
        source, parser = document(page)
        if name in MATH_PAGES:
            if not parser.math_count or not parser.display_math_count:
                failures.append(f"missing rendered display math: {name}")
        if parser.math_errors:
            failures.append(f"KaTeX rendering error: {name}")
        for url in parser.urls:
            parsed = urlsplit(url)
            if parsed.scheme or parsed.netloc:
                continue
            path = unquote(urlsplit(urljoin(f"{BASE}/{name}", url)).path)
            if path == BASE:
                path += "/"
            if not path.startswith(f"{BASE}/"):
                failures.append(f"{name}: URL outside {BASE}/: {url}")
                continue
            target = ROOT / path.removeprefix(f"{BASE}/")
            if not target.is_file():
                target = target / "index.html"
            if not target.is_file():
                failures.append(f"{name}: missing local target: {url}")
                continue
            if parsed.fragment and target.suffix == ".html":
                _, target_parser = document(target)
                if unquote(parsed.fragment) not in target_parser.ids:
                    failures.append(f"{name}: missing local fragment: {url}")
            if target.suffix == ".css":
                styles.add(target)
        if "incerto-wiki/blob/" in source or "Technical-Incerto-Python" in source:
            failures.append(f"{name}: stale private source link")
    if not any("text-underline-offset" in path.read_text() for path in styles):
        failures.append("shared math.css not found among linked stylesheets")
    if failures:
        raise SystemExit("\n".join(sorted(set(failures))))
    print(
        f"Checked {len(PAGES)} pages, local links/assets/fragments, "
        "/math prefix, and rendered math."
    )


if __name__ == "__main__":
    main()
