# State contract and resumption

`state.yaml` is the canonical inventory; `inventory.md` and `concepts.md` are
human views of its records. Schema version 2 retains mappings keyed by stable
IDs and adds scope exclusions, ordered deliverables and the M0.5 review gate.
YAML aliases and duplicate keys are rejected. The parser is a validation
environment dependency, not a new runtime dependency of `xmath`.

## Record meanings

| Field or collection | Contract |
| --- | --- |
| `books` | Seven retained records: two technical books in scope, five non-technical books out of scope. Technical Incerto names the selected SCoFT volume and its required 2025 additions, not another book. SCoFT has first priority. |
| `chapters` | Book source units: numbered chapters, unnumbered thematic sections, essays, modules and selected paratext. Each has a kind and locator; a planner ordinal is not a fabricated source chapter number. |
| `papers` | Fourteen versioned starting records; on-demand additions for concrete mathematical claims are approved. Full-text locators remain to be checked. One record is a critical response. |
| `concepts` | One ID and proposed canonical home per concept; multiple source units may refer to it. `classification` maps evidence modes to their specific justification. |
| `completion_scope` / `out_of_scope_reason` | `in-scope` or `out-of-scope`; every excluded book, unit or concept requires a reason. No excluded record contributes to completion. |
| `concept_ids` / `required_concept_ids` | The first preserves all historical source associations. The second contains only active mathematical concepts for in-scope source units; it is empty for excluded units. |
| Source-unit `classification` | Union of required concepts' modes for active units, historical modes for excluded units. It does not imply a whole chapter is formalizable. |
| `status` | `todo`, `in-progress`, `done` or `out-of-scope`. Excluded records have no milestone and no required deliverables. Existing prose does not imply `done`; M0's design status is separate. |
| Concept `deliverables` | Active order is `website-math`, `python`, `lean`; website and Python are required, Lean is optional. Status distinguishes `review-required`, `todo`, `optional`, `approved-pilot` and `skipped-for-now`. Every Lean skip needs a reason, including skipped continuous-time subclaims within an otherwise feasible finite-model candidate. |
| Concept `page_status` | `existing`, `proposed` or `out-of-scope-reservation`; an excluded path is retained for reference and schedules no page. |
| `coverage` | Evidence already present at the baseline. Existing prose can contain citations or special-case proofs; no checked Lean result is present. `not-inventoried-as-runnable` avoids equating static calculations with an executed program. |
| `dependencies` on concepts | Mathematical/reading prerequisites; satisfying a needed lemma or cited prerequisite does not require finishing every evidence mode of that concept. |
| `dependencies` on chunks/milestones | Execution gates. A blocked prerequisite prevents closure of the dependent chunk. An empty list is meaningful. |
| Source-unit/book `milestone` | Active coverage closeout is M5. Concept milestones identify subsequent treatment; all 24 existing bodies receive M0.5 review first. Excluded milestones are null. |
| `assigned_role` | Lead role from the owner's role table; collaborators may assist only under the applicable authorization. |
| `next_chunk` | JSON Pointer to an active non-done chunk; now `#/chunks/m0.5-review`. M1 depends on its completion. |
| `edition_backlog` | Required 2025 Technical Incerto reconciliation; blocks edition-complete coverage even if currently mapped concepts close. No non-technical edition task remains. |
| `owner_decisions` / `open_questions` | Record approvals separately from unresolved Shadow Mean scope, stochastic-calculus depth and 2025 locator reconciliation. Do not reopen the pilot, exact Lean scope, data routing or paper inclusion. |
| `data_policy` | Portfolio Manager supplies financial data from Xiang's database and handles additions; Data Scientist supplies other data. Every dataset retains provenance and licensing. |
| `site_review_policy` | After every site update, Math Site Editor reviews the corresponding live pages as a reader and records evidence. M0.5 uses `m0.5-review.md`; later records use the stated records path. |
| `counts` | Derived totals and in-scope/out-of-scope counts; current mapped units exclude the unreconciled 2025 additions. Counts do not measure verified mathematics. |

Do not change an ID when renaming a page or adding an edition. Add a new source
unit namespace for changed chapter numbering; record correspondence to old
units. When retiring a planned concept, retain its ID with an explicit
disposition instead of deleting references. This revision retains all 101
concept IDs, including 29 excluded records; none is renumbered. Out-of-scope
concepts cannot be prerequisites of active concepts. Required local definitions
and mathematical conditions stay within the active technical note.

A concept becomes `done` only after its agreed scoped output, source review,
applicable evidence and checks are recorded. All required mathematical claims
must have exact checked support before the concept is described as fully
Lean-verified; partial formalization gets an explicit claim list. Ordinary
completion requires teaching and numerical evidence, with optional Lean skips
recorded; M1's approved two-declaration pilot has its own proof exit gate.
A chapter or book closes only after the manager reviews its mathematical scope,
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

Run from the repository root with Python and PyYAML 6.0.3 (the version used for
this revision's validation). This checks the
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
raw = Path('docs/plan/incerto-program/state.yaml').read_text()
assert not any(isinstance(event, yaml.events.AliasEvent)
               for event in yaml.parse(raw)), 'YAML aliases are not allowed'
s = yaml.load(raw, Loader=UniqueLoader)
assert s['schema_version'] == 2
assert s['scope'] == 'design-only' and not s['implementation_authorized']
statuses = {'todo', 'in-progress', 'done', 'out-of-scope'}
classes = {'lean-verifiable', 'numeric-demo', 'empirical', 'prose-only'}
roles, milestones = s['roles'], s['milestones']
concepts, chapters, books = s['concepts'], s['chapters'], s['books']
paper_units = {u['id']: u for p in s['papers'].values() for u in p['units']}
assert len(paper_units) == sum(len(p['units']) for p in s['papers'].values())
assert not (paper_units.keys() & chapters.keys())
units = dict(chapters, **paper_units)
active = {cid for cid, c in concepts.items() if c['completion_scope'] == 'in-scope'}
active_books = {bid for bid, b in books.items() if b['completion_scope'] == 'in-scope'}
active_chapters = {uid for uid, u in chapters.items() if u['completion_scope'] == 'in-scope'}
assert active_books == {'scft', 'dh'}
assert s['completion_policy']['book_priority'] == ['scft', 'dh']
order = ['website-math', 'python', 'lean']
assert s['completion_policy']['deliverable_order'] == order
assert s['completion_policy']['lean_optional']
assert s['completion_policy']['lean_evidence_scope'] == 'exact-declaration'

def records(table):
    for key, record in table.items():
        assert record['id'] == key
        assert record['status'] in statuses
        assert record['assigned_role'] in roles
        if record['status'] == 'out-of-scope':
            assert record['completion_scope'] == 'out-of-scope'
            assert record['out_of_scope_reason'] and record['milestone'] is None
        else:
            assert record['milestone'] in milestones
            assert record.get('completion_scope', 'in-scope') == 'in-scope'
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
    assert milestone['status'] in statuses - {'out-of-scope'}
    assert milestone['assigned_role'] in roles
assert set(milestones) == {'M0', 'M0.5', 'M1', 'M2', 'M3', 'M4', 'M5'}
assert milestones['M0.5']['dependencies'] == ['M0']
assert milestones['M1']['dependencies'] == ['M0.5']
assert s['chunks']['m1-scope']['dependencies'] == ['m0.5-review']

paths = set()
for cid, concept in concepts.items():
    assert concept['classification'] and set(concept['classification']) <= classes
    assert all(concept['classification'].values())
    deliverables = concept['deliverables']
    if cid in active:
        assert 'prose-only' not in concept['classification']
        assert set(concept['dependencies']) <= active
        assert deliverables['order'] == order
        assert deliverables['website_math']['required'] and deliverables['python']['required']
        assert concept['page_status'] in {'existing', 'proposed'}
        assert concept['source_priority'] in {1, 2, 3}
        lean = deliverables['lean']
        assert not lean['required']
        assert lean['status'] in {'optional', 'approved-pilot', 'skipped-for-now'}
        if lean['status'] == 'skipped-for-now':
            assert lean['reason']
        for skip in lean.get('skipped_scopes', []):
            assert skip['scope'] and skip['reason'] and skip['status'] == 'skipped-for-now'
    else:
        assert concept['status'] == 'out-of-scope'
        assert concept['page_status'] == 'out-of-scope-reservation'
        assert deliverables['order'] == []
        for key in ('website_math', 'python', 'lean'):
            assert not deliverables[key]['required']
            assert deliverables[key]['status'] == 'out-of-scope'
    path = Path(concept['page_path'])
    assert path.parent == Path('content') and path.name.startswith('incerto-')
    assert path.suffix == '.md' and str(path) not in paths
    paths.add(str(path))
    assert concept['canonical_url'] == f'/math/incerto/{path.stem}/'
    if concept['coverage']['prose'] == 'existing':
        assert cid in active and concept['page_status'] == 'existing' and path.is_file(), path
    for foundation in concept['coverage'].get('related_foundations', []):
        assert Path(foundation).is_file(), foundation
    assert concept['coverage']['lean'] == 'absent'
    assert concept['source_units']
    assert set(concept['source_units']) == {
        uid for uid, unit in units.items() if cid in unit['concept_ids']}

for uid, unit in units.items():
    assert unit['concept_ids'] and set(unit['concept_ids']) <= concepts.keys()
    required = set(unit['concept_ids']) & active if unit['completion_scope'] == 'in-scope' else set()
    assert set(unit['required_concept_ids']) == required
    if unit['completion_scope'] == 'in-scope':
        assert required
    mapped = required if unit['completion_scope'] == 'in-scope' else unit['concept_ids']
    assert set(unit['classification']) == {
        mode for cid in mapped for mode in concepts[cid]['classification']}
assert active == {cid for unit in units.values() for cid in unit['required_concept_ids']}
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
    assert all(chapters[uid]['completion_scope'] == book['completion_scope']
               for uid in book['chapters'])
for paper in s['papers'].values():
    assert paper['completion_scope'] == 'in-scope'
    assert set(paper['classification']) == {
        mode for unit in paper['units'] for mode in unit['classification']}

for chunk in s['chunks'].values():
    assert set(chunk['concept_ids']) <= active and chunk['acceptance']
prefix, collection, key = s['next_chunk'].split('/')
assert prefix == '#' and collection == 'chunks'
assert key == 'm0.5-review' and s['chunks'][key]['status'] == 'todo'
assert {cid for cid, c in concepts.items() if c['milestone'] == 'M1'} == {'c-exceedances'}
indexes = {f'content/incerto-{name}-concepts.md'
           for name in ('distribution', 'theorem', 'method')}
existing = {c['page_path'] for c in concepts.values()
            if c['coverage']['prose'] == 'existing'}
assert existing == {str(p) for p in Path('content').glob('incerto-*.md')} - indexes
review = s['chunks']['m0.5-review']
assert set(review['concept_ids']) == {
    cid for cid, c in concepts.items() if c['coverage']['prose'] == 'existing'}
assert len(review['concept_ids']) == 24 and Path(review['output_path']).is_file()
assert review['review_workstreams']['mathematics']['assigned_role'] == 'astra-max'
assert review['review_workstreams']['reader']['assigned_role'] == 'math-site-editor'
assert s['site_review_policy']['trigger'] == 'after every site update'
assert s['site_review_policy']['assigned_role'] == 'math-site-editor'
assert s['data_policy']['financial']['assigned_role'] == 'portfolio-manager'
assert s['data_policy']['other']['assigned_role'] == 'data-scientist'
assert set(s['open_questions']) == {
    'shadow-mean', 'stochastic-calculus-depth', 'technical-incerto-2025'}
for decision in ('m1-pilot', 'lean-claim-scope', 'data-routing', 'paper-inclusion'):
    assert s['owner_decisions'][decision]['status'] == 'approved'
assert {item['id'] for item in s['edition_backlog']} == {'edition-scft-v4'}
for item in s['edition_backlog']:
    assert item['book_id'] in active_books
    assert item['assigned_role'] in roles and item['milestone'] in milestones
    assert item['depends_on_chunk'] in s['chunks']
for cid in ('c-brownian', 'c-stochastic-pricing'):
    assert concepts[cid]['deliverables']['lean']['status'] == 'skipped-for-now'
numbered = sum(b['expected_numbered_chapters'] for b in books.values())
active_numbered = sum(books[bid]['expected_numbered_chapters'] for bid in active_books)
expected = dict(
    books_total=len(books), books_in_scope=len(active_books),
    books_out_of_scope=len(books) - len(active_books),
    numbered_chapters_total=numbered, numbered_chapters_in_scope=active_numbered,
    numbered_chapters_out_of_scope=numbered - active_numbered,
    book_source_units_total=len(chapters), book_source_units_in_scope=len(active_chapters),
    book_source_units_out_of_scope=len(chapters) - len(active_chapters),
    papers=len(s['papers']), concepts_total=len(concepts), concepts_in_scope=len(active),
    concepts_out_of_scope=len(concepts) - len(active),
    existing_concept_pages=len(existing), checked_lean_concepts=0)
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
