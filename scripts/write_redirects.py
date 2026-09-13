"""Write old flat /math/ routes into the assembled HTML artifact."""

from html import escape
import json

from site_layout import BASE, HTML, ORIGIN, redirects


def main():
    routes = redirects()
    for old, new in routes.items():
        target = HTML / new.removeprefix(f"{BASE}/") / "index.html"
        if not target.is_file():
            raise SystemExit(f"Missing redirect destination: {new}")
        page = HTML / old.removeprefix(f"{BASE}/") / "index.html"
        page.parent.mkdir(parents=True, exist_ok=True)
        page.write_text(f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Page moved</title>
<link rel="canonical" href="{ORIGIN}{escape(new, quote=True)}">
<meta http-equiv="refresh" content="0; url={escape(new, quote=True)}">
<script>window.location.replace({json.dumps(new)} + window.location.search + window.location.hash);</script>
</head>
<body><p>This page has moved to <a href="{escape(new, quote=True)}">{escape(new)}</a>.</p></body>
</html>
""", encoding="utf-8")
    print(f"Wrote {len(routes)} redirects; existing Incerto and Normix homes retained.")


if __name__ == "__main__":
    main()
