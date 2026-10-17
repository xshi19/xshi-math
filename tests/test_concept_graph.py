import sys
import subprocess
from pathlib import Path
import pytest
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))


from build_concept_graph import build_graph_data


@pytest.mark.parametrize("staged", [False, True], ids=["source", "staged"])
def test_concept_graph_pointer_interactions(tmp_path, staged):
    """Check touch pan direction and cancellation rollback in both asset copies."""
    from build_concept_graph import stage_graph_assets

    root = Path(__file__).resolve().parents[1]
    if staged:
        stage_graph_assets(tmp_path)
        root = tmp_path
    result = subprocess.run(
        ["node", str(Path(__file__).with_name("concept_graph_interactions.cjs")),
         str(root / "assets/js/concept-graph.js")],
        capture_output=True, text=True, timeout=30,
    )
    assert result.returncode == 0, result.stdout + result.stderr


def test_graph_touch_scroll_policy_and_static_fallback(tmp_path):
    import re
    from build_concept_graph import stage_graph_assets
    from check_html import Links

    data = stage_graph_assets(tmp_path)
    assets = tmp_path / "assets"
    css = (assets / "css/concept-graph.css").read_text()
    background = re.search(r"#concept-graph\s*\{([^}]+)\}", css)[1]
    node = re.search(r"\.node\s*\{([^}]+)\}", css)[1]
    assert re.search(r"touch-action:\s*pan-y(?:\s+pinch-zoom)?\s*;", background)
    assert "touch-action: none;" in node
    assert 'href="concept-list.html"' in (assets / "graphs/concept-graph.html").read_text()
    fallback = (assets / "graphs/concept-list.html").read_text()
    assert "<script" not in fallback
    links = Links()
    links.feed(fallback)
    assert {node["url"] for node in data["nodes"]} <= set(links.urls)
    root = Path(__file__).resolve().parents[1]
    for relative in ("js/concept-graph.js", "css/concept-graph.css"):
        assert (assets / relative).read_bytes() == (root / "assets" / relative).read_bytes()


def test_concept_graph_excludes_notation() -> None:
    data = build_graph_data()
    node_ids = {node["id"] for node in data["nodes"]}

    assert "notation" not in node_ids
    assert all("content/notation" not in node["path"] for node in data["nodes"])
    assert all(edge["source"] in node_ids for edge in data["edges"])
    assert all(edge["target"] in node_ids for edge in data["edges"])


def test_concept_graph_has_expected_node_types() -> None:
    data = build_graph_data()
    type_counts = data["stats"]["type_counts"]

    assert type_counts["distribution"] >= 1
    assert type_counts["theorem"] >= 1
    assert type_counts["method"] >= 1
    assert type_counts["empirical-example"] >= 1


def test_concept_graph_dependency_order() -> None:
    data = build_graph_data()
    order = {concept_id: index for index, concept_id in enumerate(data["topological_order"])}

    assert order["pareto"] < order["regular-variation"]
    assert order["pareto"] < order["pareto-moment-existence"]
    assert order["hill-estimator"] < order["sp500-tail"]


def test_mathematical_relationship_can_reverse_reading_order():
    data = build_graph_data()
    edges = {(e['kind'], e['source'], e['target']) for e in data['edges']}
    assert ('dependency', 'pareto', 'regular-variation') in edges
    assert ('generalization', 'pareto', 'regular-variation') in edges
    assert ('proof-dependency', 'pareto', 'generalized-central-limit-theorem') in edges
    assert all('/content/' not in n['url'] for n in data['nodes'])


def test_only_prerequisites_reject_cycles():
    from dataclasses import replace
    import pytest
    from build_concept_graph import load_concepts, _dependency_graph, _build_edges
    pages = load_concepts()
    a, b = pages[:2]
    a = replace(a, depends_on=(), proof_depends_on=(b.concept_id,),
                special_case_of=(), applications=(), related=(), body="")
    b = replace(b, depends_on=(), proof_depends_on=(a.concept_id,),
                special_case_of=(), applications=(), related=(), body="")
    graph = _dependency_graph([a, b])
    assert len(_build_edges([a, b], graph)) == 2
    with pytest.raises(ValueError, match="cycle"):
        _dependency_graph([replace(a, depends_on=(b.concept_id,)),
                           replace(b, depends_on=(a.concept_id,))])
    with pytest.raises(ValueError, match="unknown"):
        _build_edges([replace(a, proof_depends_on=("missing",)), b], graph)


def test_staged_assets_resolve_inside_incerto_and_build_from_frontmatter(tmp_path):
    import json
    from urllib.parse import urljoin, urlsplit
    from build_concept_graph import stage_graph_assets
    from check_html import Links
    artifact = tmp_path / "math/incerto"
    data = stage_graph_assets(artifact)
    assert not (artifact / "assets/data/reading-paths.json").exists()
    assert json.loads((artifact / "assets/data/concept-graph.json").read_text()) == data
    for node in data["nodes"]:
        assert node["url"] == "/math/incerto/" + Path(node["path"]).stem + "/"
        assert (Path(__file__).resolve().parents[1] / node["path"]).is_file()
        target = tmp_path / node["url"].lstrip("/") / "index.html"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text("<html><title>Concept fixture</title></html>")
    for path in (artifact / "assets/graphs").glob("*.html"):
        parser = Links()
        parser.feed(path.read_text())
        for link in parser.urls:
            resolved = urlsplit(urljoin("https://xshi19.github.io/" + path.relative_to(tmp_path).as_posix(), link)).path
            target = tmp_path / resolved.lstrip("/")
            assert target.is_file() or (target / "index.html").is_file(), (path, link)


def test_bad_metadata_is_not_silently_ignored(tmp_path):
    import pytest
    from build_concept_graph import build_graph_data
    content = tmp_path / "content"
    content.mkdir()
    (content / "incerto-test.md").write_text('---\ntitle: Invalid\noptions:\n  concept: wrong\n---\n')
    with pytest.raises(ValueError, match="mapping"):
        build_graph_data(tmp_path)
