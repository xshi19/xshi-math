# State contract and resumption

`state.yaml` is the canonical inventory; `inventory.md` and `concepts.md` are
human views of its records. Schema version 1 uses mappings keyed by stable IDs.
YAML aliases and duplicate keys are not intended. The parser is a validation
environment dependency, not a new runtime dependency of `xmath`.

## Record meanings

| Field or collection | Contract |
| --- | --- |
| `books` | Seven bibliographic works. Technical Incerto is an alternate/series description of the selected SCoFT volume, not an eighth book. Edition review remains open. |
| `chapters` | Book source units: numbered chapters, unnumbered thematic sections, essays, modules and selected paratext. Each has a kind and locator; a planner ordinal is not a fabricated source chapter number. |
| `papers` | Versioned starter corpus, with units whose exact full-text locators still need verification. One record is a critical response by another author. |
| `concepts` | One ID and proposed canonical home per concept; multiple source units may refer to it. `classification` maps evidence modes to their specific justification. |
| Source-unit `classification` | Union of its concepts' modes; a routing aid, not a statement that an entire chapter is formalizable. |
| `status` | Exactly `todo`, `in-progress` or `done`. Existing prose does not imply the program record is done. M0's design status is distinct from implementation status. |
| `coverage` | Evidence already present at the baseline. Existing prose can contain citations or special-case proofs; no checked Lean result is present. `not-inventoried-as-runnable` avoids equating static calculations with an executed program. |
| `dependencies` on concepts | Mathematical/reading prerequisites; satisfying a needed lemma or cited prerequisite does not require finishing every evidence mode of that concept. |
| `dependencies` on chunks/milestones | Execution gates. A blocked prerequisite prevents closure of the dependent chunk. An empty list is meaningful. |
| Source-unit/book `milestone` | Coverage-closeout target, currently M6. Concept milestone is first planned treatment. |
| `assigned_role` | Lead role from the owner's role table; collaborators may assist only under the applicable authorization. |
| `next_chunk` | JSON Pointer to a non-done chunk record, initially `#/chunks/m1-scope`. |
| `edition_backlog` | Unreconciled edition changes; these prevent claims of edition-complete coverage even if all currently mapped concepts close. |
| `counts` | Derived consistency checks, never a substitute for reviewing content or proof scope. |

Do not change an ID when renaming a page or adding an edition. Add a new source
unit namespace for changed chapter numbering; record correspondence to old
units. When retiring a planned concept, retain its ID with an explicit
disposition and schema update instead of silently deleting references. No
present record is being retired by this design.

A concept becomes `done` only after its agreed scoped output, source review,
applicable evidence and checks are recorded. All required mathematical claims
must have exact checked support before the concept is described as fully
Lean-verified; partial formalization gets an explicit claim list. A chapter or
book closes only after the manager reviews the whole intended source scope,
not merely after every linked page exists. Add a checkpoint record with claim
IDs, artifact paths, revision, command results, remaining limits and reviewer
when work starts; this initial state invents no implementation evidence.

## Resume procedure

1. Read `next_chunk`, its prerequisites and acceptance list. Confirm the task
   authorizes implementation; this state currently says it does not.
2. Recheck the actual repository and relevant guidance. A proposed path is not
   evidence that the file now exists. Resolve edition/theorem locators for the
   selected work before making sourced claims.
3. Set only the selected chunk and actively worked concepts to `in-progress`.
   Record changed scope and owner decisions with dates. Keep source-unit review
   and program progress separate from baseline coverage.
4. On completion, record evidence and limitations, then mark the scoped work
   `done`. If interrupted, keep it `in-progress` with a concrete checkpoint;
   do not relabel unfinished work to move the pointer.
5. Advance `next_chunk` to the next executable non-done chunk. Update human
   views and derived counts, then run the checks below. Larger milestones need
   new bounded chunks before execution; the concept list alone is not a task.

## Reproducible structural check

Run from the repository root with Python and PyYAML available. This checks the
current schema, graphs, mappings, route conventions, baseline files and
counts. It does not validate a mathematical assertion or a source's contents.

```bash
python3 - <<'PY'
from pathlib import Path
import yaml

class UniqueLoader(yaml.SafeLoader):
    pass

def unique_mapping(loader, node, deep=False):
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in result:
            raise ValueError(f'duplicate YAML key: {key}')
        result[key] = loader.construct_object(value_node, deep=deep)
    return result

UniqueLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)
s = yaml.load(Path('docs/plan/incerto-program/state.yaml').read_text(),
              Loader=UniqueLoader)
assert s['schema_version'] == 1
assert s['scope'] == 'design-only' and not s['implementation_authorized']
statuses = {'todo', 'in-progress', 'done'}
classes = {'lean-verifiable', 'numeric-demo', 'empirical', 'prose-only'}
roles, milestones = s['roles'], s['milestones']
concepts, chapters, books = s['concepts'], s['chapters'], s['books']
paper_units = {u['id']: u for p in s['papers'].values() for u in p['units']}
units = dict(chapters, **paper_units)

def records(table):
    for key, record in table.items():
        assert record['id'] == key
        assert record['status'] in statuses
        assert record['assigned_role'] in roles
        assert record['milestone'] in milestones
        assert isinstance(record['dependencies'], list)

for table in (books, chapters, s['papers'], paper_units, concepts, s['chunks']):
    records(table)

def dag(table):
    active, complete = set(), set()
    def visit(key):
        assert key in table, f'unknown dependency: {key}'
        assert key not in active, f'cycle at {key}'
        if key in complete:
            return
        active.add(key)
        for dep in table[key]['dependencies']:
            visit(dep)
        active.remove(key)
        complete.add(key)
    for key in table:
        visit(key)

for table in (concepts, s['chunks'], milestones):
    dag(table)
for milestone in milestones.values():
    assert milestone['status'] in statuses
    assert milestone['assigned_role'] in roles

paths = set()
for cid, concept in concepts.items():
    assert concept['classification'] and set(concept['classification']) <= classes
    assert all(concept['classification'].values())
    path = Path(concept['page_path'])
    assert path.parent == Path('content') and path.name.startswith('incerto-')
    assert path.suffix == '.md' and str(path) not in paths
    paths.add(str(path))
    assert concept['canonical_url'] == f'/math/incerto/{path.stem}/'
    if concept['coverage']['prose'] == 'existing':
        assert path.is_file(), path
    for foundation in concept['coverage'].get('related_foundations', []):
        assert Path(foundation).is_file(), foundation
    assert concept['coverage']['lean'] == 'absent'
    assert concept['source_units']
    assert set(concept['source_units']) == {
        uid for uid, unit in units.items() if cid in unit['concept_ids']}

for uid, unit in units.items():
    assert unit['concept_ids'] and set(unit['concept_ids']) <= concepts.keys()
    assert set(unit['classification']) == {
        mode for cid in unit['concept_ids'] for mode in concepts[cid]['classification']}
for bid, book in books.items():
    assert set(book['source_ids']) <= s['sources'].keys()
    assert set(book['chapters']) == {
        uid for uid, chapter in chapters.items() if chapter['book_id'] == bid}
    numbered = [chapters[uid] for uid in book['chapters']
                if chapters[uid]['kind'] == 'chapter']
    assert len(numbered) == book['expected_numbered_chapters']
    assert {u['locator'] for u in numbered} == {
        f'ch. {n}' for n in range(1, len(numbered) + 1)}
    assert set(book['classification']) == {
        mode for uid in book['chapters'] for mode in chapters[uid]['classification']}

for chunk in s['chunks'].values():
    assert set(chunk['concept_ids']) <= concepts.keys() and chunk['acceptance']
prefix, collection, key = s['next_chunk'].split('/')
assert prefix == '#' and collection == 'chunks'
assert s['chunks'][key]['status'] != 'done'
assert {cid for cid, c in concepts.items() if c['milestone'] == 'M1'} == {'c-exceedances'}
indexes = {f'content/incerto-{name}-concepts.md'
           for name in ('distribution', 'theorem', 'method')}
existing = {c['page_path'] for c in concepts.values()
            if c['coverage']['prose'] == 'existing'}
assert existing == {str(p) for p in Path('content').glob('incerto-*.md')} - indexes
expected = dict(books=len(books),
                numbered_chapters=sum(b['expected_numbered_chapters'] for b in books.values()),
                book_source_units=len(chapters), papers=len(s['papers']),
                concepts=len(concepts), existing_concept_pages=len(existing),
                checked_lean_concepts=0)
assert s['counts'] == expected
print('State validation passed:', expected)
PY
```

The baseline checks intentionally require no checked Lean and exactly the
current existing pages. Update them with the schema/coverage when real
implementation changes those facts; do not leave a stale passing validator.
Review local links and explicit concept anchors in the human views. Check
`git diff --check` plus new-file whitespace separately, inspect full new files,
and confirm the change stays in the authorized plan scope. Run the requested
site checks and report failures without claiming they passed.
