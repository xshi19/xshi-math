# State contract and resumption

`state.yaml` is canonical; inventory and concept pages in this directory are
human views. **Schema 3** uses the SCoFT v4 locator namespace and an ordered
chapter queue. Duplicate YAML keys and aliases are rejected. PyYAML is a
validation-environment dependency, not a new runtime dependency of `xmath`.

## Record meanings

| Field or collection | Contract |
| --- | --- |
| `books` | Seven retained books: SCoFT v4 and Dynamic Hedging active; five non-technical books excluded. |
| `chapters` | 193 book source units, of which 70 are active. Active SCoFT IDs are `scft-v4-ch01`–`scft-v4-ch30` and `scft-v4-appa`–`scft-v4-appi`; titles and starting pages come from the v4 TOC. |
| `edition_mappings` | All 33 historical v2 unit IDs map to v4 units; six additions are explicit. Old IDs are correspondence keys only, never active aliases with changed meanings. |
| `edition_backlog` | The v4 reconciliation record is retained as `done`, with evidence. This does not certify mathematical claims. |
| `papers` | Sixteen records with immutable preprint versions or a journal citation, chapter attachments and correspondence type. Full-text claims require later review. |
| `concepts` | All 101 prior IDs retained plus two appended IDs; 75 active and 28 excluded. `c-lindy` is reactivated with its former scope preserved. One canonical home per concept. |
| `completion_scope` / `out_of_scope_reason` | Excluded records need a reason, null milestone and no required deliverables. They do not enter completion counts. |
| `concept_ids` / `required_concept_ids` | Historical associations versus active obligations. Required concepts exclude contextual interpretations and inactive books. |
| `classification` / `coverage` | Candidate evidence modes versus existing evidence in the design inventory. The 24 M0.5 bodies now have a mathematical review; additional migrated pages are listed separately. No checked Lean concept was added. |
| Concept `deliverables` | `website-math`, `python`, then optional `lean`. Required teaching/numerical flags remain true. Lean skips need reasons; optional approval is not proof evidence. |
| Concept `chunk_ids` / `first_chunk` | All chapter-scoped uses, in execution order, and first treatment. A later chapter may extend the same canonical page. |
| `chunks` | Insertion order is the execution order: M0.5, 30 SCoFT chapters, 23 DH chapters, closeout. Every chapter has one chunk. Each stores ID, locator, title only, concepts, deliverables, dependencies, role, status and existing pages reused. |
| Chunk `deliverables` | Required `teaching_pages` and `demos`, then `optional_lean`; review/closeout chunks mark these not applicable and name their own output. The exceedance pilot is optional inside chapter 2. |
| `source_unit_ids` / `paper_ids` | The main chapter and every attached appendix/module/paper. Attachments belong to one chapter and must be reviewed in its checkpoint. |
| `supplement_policy` | All nine SCoFT appendices and eight DH supporting units attach to chapters; none creates a separate chunk. |
| `dependencies` | Concepts encode reading prerequisites; chunks/milestones encode execution gates. Use reviewed pages or bounded cited prerequisites without reordering chapters. |
| `milestone` | M0 design; M0.5 review; M1 SCoFT; M2 DH; M3 closeout. A concept takes its first chapter's milestone. |
| `next_chunk` | `#/chunks/scft-v4-ch11`, following chapter-10 implementation; separate chapter-10 max review and external site/browser checks remain recorded follow-ups. |
| `owner_decisions` / `open_questions` | Prior program scope decisions remain approved. M0.5 findings and pending Xiang decisions are in the review chunk's `issues`, distinct from those earlier scope questions. |
| `scope` / `authorized_chunks` | Current authorization covers M0.5 closure, chapters 1–10 implementation and the requested earlier-chapter reader fixes; it does not authorize all later chapters. |
| M0.5 `review_workstreams` / `issues` | Mathematics and live reader review are done; owner reports 24/24 live coverage after PR #27. Exact viewport details were not supplied. Shared issues retain other chapters’ assignments. |
| `assigned_role` | Owner-assigned lead; role labels neither guarantee availability nor authorize delegation. |
| `data_policy` / `site_review_policy` | Data via the assigned bots with provenance; live reader review after every site update. Build evidence cannot replace reader review. |
| `counts` | Derived active/historical totals, 30 v4 chapters, nine v4 appendices, 53 chapter chunks and 55 total chunks. Not a measure of mathematical verification. |

Do not rename concept IDs. For a future edition with changed numbering, use a
new explicit unit namespace and retain correspondence. A chapter closes only
after its selected mathematical claims, required teaching/demos, attached
source scope and applicable reviews close. An optional Lean attempt needs
exact checked evidence before being called complete, but a recorded skip
never blocks chapter closure or the next chapter. Scope approval for the two
exceedance claims remains valid.

## Resume procedure

1. Read `next_chunk`, its dependencies and acceptance criteria. Confirm the
   current task authorizes the selected work; M0.5 authorization does not
   authorize a later chapter. Chapter-1/2/3/4/5/6/7/8/9/10 authorization and the M0.5 live closure are explicitly recorded.
2. Recheck guidance and sources. For SCoFT use v4 locators, consulting the v2
   correspondence only for historical references. Resolve exact claim
   locators without copying book text.
3. Set the selected chunk and actively worked concepts to `in-progress`.
   Record a [chapter checkpoint](templates.md#chapter-checkpoint): claim IDs,
   completed/pending pages and demos, evidence, revision and next action.
4. Close required teaching and demos at this chapter's scope. Record optional
   Lean results or skips. Resolve relevant M0.5 findings before reuse; after
   a site update obtain the Math Site Editor live reader review.
5. Mark completed scoped work `done`, or retain an interruption checkpoint.
   Advance to the next ordered non-done chapter. Update human views and counts.
   Existing source-unit or concept associations do not create a separate queue.

## Reproducible structural and local-link check

Run from the repository root with Python and PyYAML 6.0.3. The validator also
reads the recorded Git revision to check ID/path preservation. It needs no
network or external PDF. It checks structure and source correspondence data,
not the truth of mathematical claims. The optional source comparison below
rechecks those data against the supplied files.

```bash
python3 - <<'PY'
from pathlib import Path
import re
import subprocess
from urllib.parse import unquote, urlsplit
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
assert s['schema_version'] == 3
assert s['scope'] == 'scft-v4-ch10' and s['implementation_authorized']
assert s['authorized_chunks'] == ['m0.5-review', 'scft-v4-ch01', 'scft-v4-ch02', 'scft-v4-ch03', 'scft-v4-ch04', 'scft-v4-ch05', 'scft-v4-ch06', 'scft-v4-ch07', 'scft-v4-ch08', 'scft-v4-ch09', 'scft-v4-ch10']
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
assert set(milestones) == {'M0', 'M0.5', 'M1', 'M2', 'M3'}
assert milestones['M0.5']['dependencies'] == ['M0']
assert milestones['M1']['dependencies'] == ['M0.5']
assert s['chunks']['scft-v4-ch01']['dependencies'] == ['m0.5-review']

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
        assert lean['status'] in {'optional', 'optional-approved-pilot', 'skipped-for-now'}
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
assert key == 'scft-v4-ch11' and s['chunks'][key]['status'] == 'todo'
assert all(s['chunks'][k]['status'] == 'done' for k in ('scft-v4-ch01', 'scft-v4-ch02', 'scft-v4-ch03', 'scft-v4-ch04', 'scft-v4-ch05', 'scft-v4-ch06', 'scft-v4-ch07', 'scft-v4-ch08', 'scft-v4-ch09', 'scft-v4-ch10'))
indexes = {f'content/incerto-{name}-concepts.md'
           for name in ('distribution', 'theorem', 'method')}
existing = {c['page_path'] for c in concepts.values()
            if c['coverage']['prose'] == 'existing'}
review = s['chunks']['m0.5-review']
flat_pages = {str(p) for p in Path('content').glob('incerto-*.md')}
assert existing <= flat_pages - indexes
post_review_pages = {'content/incerto-scoft-ch1.md', 'content/incerto-scoft-ch2.md',
                     'content/incerto-scoft-ch5.md', 'content/incerto-scoft-ch6.md', 'content/incerto-scoft-ch7.md', 'content/incerto-scoft-ch8.md',
                     'content/incerto-rayleigh-speed.md', 'content/incerto-scoft-ch9.md',
                     'content/incerto-hidden-tail.md', 'content/incerto-power-law-fitting.md',
                     'content/incerto-power-law-goodness-of-fit.md', 'content/incerto-scoft-ch10.md',
                     'content/incerto-layoffs-tails.md'}
assert set(review['additional_pages_skimmed']) == flat_pages - existing - post_review_pages
assert len(review['additional_pages_skimmed']) == 18
# M0.5 is a frozen review inventory; later original pages do not enlarge it.
assert set(review['concept_ids']) == {
    cid for cid, c in concepts.items()
    if c['coverage']['prose'] == 'existing' and not c['coverage'].get('created_in_chunk')}
assert {cid for cid, c in concepts.items() if c['coverage'].get('created_in_chunk')} == {
    'c-inference-asymmetry', 'c-asymmetric-payoffs', 'c-ruin', 'c-decentralization',
    'c-mixture-uncertainty', 'c-moment-estimation', 'c-maximum-entropy',
    'c-multivariate-tails', 'c-cauchy-running', 'c-ergodicity', 'c-kappa',
    'c-sp500', 'c-ml-econometrics'}
assert len(review['concept_ids']) == 24 and Path(review['output_path']).is_file()
assert review['review_workstreams']['mathematics']['assigned_role'] == 'astra-max'
assert review['review_workstreams']['reader']['assigned_role'] == 'math-site-editor'
math_review = review['review_workstreams']['mathematics']
reader_review = review['review_workstreams']['reader']
assert math_review['status'] == 'done' and math_review['pages_reviewed'] == 24
assert reader_review['status'] == 'done' and reader_review['pages_reviewed_live'] == 24
assert reader_review['deployment_revision'] == 'fbf2c6a' and reader_review['evidence']
assert reader_review['follow_up']
assert review['status'] == milestones['M0.5']['status'] == 'done'
assert review['deliverables']['issues_list']['status'] == 'done'
claim_text = Path(math_review['claim_log_path']).read_text()
claim_ids = re.findall(r'^\| `(c-[^`]+-claim-\d{3})` \|', claim_text, re.M)
assert len(claim_ids) == len(set(claim_ids)) == math_review['claim_records'] == 448
assert {cid.rsplit('-claim-', 1)[0] for cid in claim_ids} == set(review['concept_ids'])
assert len(review['issues']) == len({i['id'] for i in review['issues']}) == 15
assert review['issue_summary']['by_severity'] == {
    level: sum(i['severity'] == level for i in review['issues'])
    for level in ('blocker', 'major', 'minor')}
for issue in review['issues']:
    assert issue['status'] in {'fixed in this PR', 'needs Xiang decision', 'assigned to chapter chunk'}
    assert issue['chapters'] and set(issue['chapters']) <= s['chunks'].keys()
    assert all(issue['id'] in s['chunks'][chunk]['m0_5_issue_ids'] for chunk in issue['chapters'])
assert s['site_review_policy']['trigger'] == 'after every site update'
assert s['site_review_policy']['assigned_role'] == 'math-site-editor'
assert s['data_policy']['financial']['assigned_role'] == 'portfolio-manager'
assert s['data_policy']['other']['assigned_role'] == 'data-scientist'
assert s['chunks']['scft-v4-ch10']['checkpoint']['empirical_evaluation']['status'] == 'pending-authorized-data'
assert all(concepts[c]['status'] == 'in-progress' for c in ('c-sp500', 'c-ml-econometrics'))
assert s['open_questions'] == {}
for decision in ('m1-pilot', 'lean-claim-scope', 'data-routing', 'paper-inclusion',
                 'shadow-mean', 'stochastic-calculus-depth', 'technical-incerto-2025',
                 'chapter-order', 'scft-v4-baseline'):
    assert s['owner_decisions'][decision]['status'] == 'approved'
assert {item['id'] for item in s['edition_backlog']} == {'edition-scft-v4'}
for item in s['edition_backlog']:
    assert item['book_id'] in active_books
    assert item['assigned_role'] in roles and item['milestone'] in milestones
    assert item['status'] == 'done' and item['evidence']
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
    existing_concept_pages=len(existing), checked_lean_concepts=0,
    scft_v4_chapters=sum(u['book_id'] == 'scft' and u['kind'] == 'chapter'
                         for u in chapters.values()),
    scft_v4_appendices=sum(k.startswith('scft-v4-app') for k in chapters),
    chunks_total=len(s['chunks']),
    chapter_chunks=sum(k in chapters and chapters[k]['kind'] == 'chapter'
                       for k in s['chunks']))
assert s['counts'] == expected
assert expected == dict(
    books_total=7, books_in_scope=2, books_out_of_scope=5,
    numbered_chapters_total=130, numbered_chapters_in_scope=53,
    numbered_chapters_out_of_scope=77, book_source_units_total=193,
    book_source_units_in_scope=70, book_source_units_out_of_scope=123,
    papers=16, concepts_total=103, concepts_in_scope=75, concepts_out_of_scope=28,
    existing_concept_pages=37, checked_lean_concepts=0,
    scft_v4_chapters=30, scft_v4_appendices=9, chunks_total=55, chapter_chunks=53)

# Chapter order, explicit gates, source coverage and optional Lean.
scft = [f'scft-v4-ch{n:02d}' for n in range(1, 31)]
dh = [f'dh-ch{n:02d}' for n in range(1, 24)]
sequence = ['m0.5-review'] + scft + dh + ['technical-closeout']
assert list(s['chunks']) == sequence
assert list(milestones) == ['M0', 'M0.5', 'M1', 'M2', 'M3']
assert [m['dependencies'] for m in milestones.values()] == [
    [], ['M0'], ['M0.5'], ['M1'], ['M2']]
assert books['scft']['expected_appendices'] == 9
assert books['scft']['edition_review'] == 'done'
assert books['scft']['locator_namespace'] == 'scft-v4'
assert books['scft']['chapters'] == scft + [f'scft-v4-app{c}' for c in 'abcdefghi']
assert all(not k.startswith('scft-') or k.startswith('scft-v4-') for k in chapters)
attachments = s['supplement_policy']['attachments']
assert {u: h for u, h in attachments.items() if u.startswith('scft-')} == {
    f'scft-v4-app{c}': f'scft-v4-ch{n:02d}' for c, n in
    zip('abcdefghi', (6, 5, 7, 7, 9, 10, 10, 18, 22))}
assert len(attachments) == 17  # nine appendices, seven modules, introduction
seen_units, seen_papers = [], []
for i, key in enumerate(sequence):
    ch = s['chunks'][key]
    assert ch['dependencies'] == ([] if i == 0 else [sequence[i-1]])
    for field in ('id', 'locator', 'title', 'concept_ids', 'deliverables',
                  'dependencies', 'assigned_role', 'status', 'existing_pages_reused'):
        assert field in ch, (key, field)
    assert all(Path(p).is_file() for p in ch['existing_pages_reused'])
    d = ch['deliverables']
    assert not d['optional_lean']['required']
    if key not in scft + dh:
        continue
    assert ch['title'] == chapters[key]['title']
    assert ch['locator'] == ('SCoFT v4 ' if key in scft else 'Dynamic Hedging ') + chapters[key]['locator']
    assert d['order'] == order
    assert d['teaching_pages']['required'] and d['demos']['required']
    assert d['optional_lean']['status'] in {'optional', 'optional-approved-pilot', 'skipped-for-now'}
    if d['optional_lean']['status'] == 'skipped-for-now':
        assert d['optional_lean']['reason']
    assert {concepts[c]['page_path'] for c in ch['concept_ids']} <= set(d['teaching_pages']['page_paths'])
    if ch['status'] == 'done':
        assert d['teaching_pages']['status'] == d['demos']['status'] == 'done'
        assert all(Path(p).is_file() for p in d['teaching_pages']['page_paths'])
        assert Path(ch['checkpoint']['evidence_path']).is_file()
        assert all(Path(p).is_file() for field in ('script_paths', 'helper_paths', 'test_paths', 'figure_paths')
                   for p in d['demos'][field])
    assert d['demos']['concept_ids'] == ch['concept_ids']
    assert ch['source_unit_ids'] == [key] + [u for u, host in attachments.items() if host == key]
    required = {c for u in ch['source_unit_ids'] for c in chapters[u]['required_concept_ids']}
    for p in ch['paper_ids']:
        assert s['papers'][p]['attached_chunk_ids'] == [key]
        assert {r['unit_id'] for r in s['papers'][p]['chapter_correspondence']} == {key}
        required |= {c for u in s['papers'][p]['units'] for c in u['required_concept_ids']}
    assert set(ch['concept_ids']) == required
    assert set(ch['prerequisite_concept_ids']) == {
        dep for c in required for dep in concepts[c]['dependencies']} - required
    # Do not backdate a later-created prerequisite into an earlier checkpoint.
    chunk_order = list(s['chunks'])
    assert set(ch['existing_pages_reused']) == {
        concepts[c]['page_path'] for c in required | set(ch['prerequisite_concept_ids'])
        if concepts[c]['coverage']['prose'] == 'existing'
        and (not concepts[c]['coverage'].get('created_in_chunk')
             or chunk_order.index(concepts[c]['coverage']['created_in_chunk'])
             < chunk_order.index(key))}
    for u in ch['source_unit_ids']:
        assert chapters[u]['chunk_id'] == key
        assert chapters[u]['milestone'] == ch['milestone']
        if key in scft:
            assert chapters[u]['edition'] == '2001.10488v4'
    seen_units.extend(ch['source_unit_ids'])
    seen_papers.extend(ch['paper_ids'])
assert len(seen_units) == len(set(seen_units)) == len(active_chapters)
assert set(seen_units) == active_chapters
assert len(seen_papers) == len(set(seen_papers)) == len(s['papers'])
assert set(seen_papers) == set(s['papers'])
for cid in active:
    c = concepts[cid]
    hosts = [k for k in scft + dh if cid in s['chunks'][k]['concept_ids']]
    assert c['chunk_ids'] == hosts and c['first_chunk'] == hosts[0]
    assert c['milestone'] == s['chunks'][hosts[0]]['milestone']
pilot = s['chunks']['scft-v4-ch02']['deliverables']['optional_lean']
assert pilot['status'] == 'skipped-for-now' and pilot['reason']
assert len(pilot['approved_claims']) == 2
assert pilot['concept_ids'] == ['c-exceedances']
assert concepts['c-exceedances']['deliverables']['lean']['chunk_id'] == 'scft-v4-ch02'
assert s['chunks']['scft-v4-ch03']['queue_items'] == ['Inference Asymmetry']
assert s['chunks']['scft-v4-ch04']['queue_items'] == ['Moment-Estimation Failure']
assert s['chunks']['scft-v4-ch07']['queue_items'] == ['Bounded Cauchy running-statistics simulation']
assert s['chunks']['scft-v4-ch17']['queue_items'] == ['Shadow Mean']
assert concepts['c-shadow-mean']['first_chunk'] == 'scft-v4-ch17'
assert concepts['c-conflict-study']['first_chunk'] == 'scft-v4-ch18'

# Versioned correspondence preserves old source identities without rebinding.
edition = s['edition_mappings']['scft-v2-to-v4']
assert edition['status'] == 'done' and edition['numbering_deviations'] == []
expected_map = {f'scft-ch{n:02d}': f'scft-v4-ch{n if n <= 11 else n+2 if n <= 16 else n+3 if n <= 19 else n+4 if n <= 24 else n+5:02d}'
                for n in range(1, 26)}
expected_map.update({f'scft-app{c}': f'scft-v4-app{c if c == "a" else chr(ord(c)+1)}' for c in 'abcdefgh'})
assert {m['previous_unit_id']: m['v4_unit_id'] for m in edition['units']} == expected_map
assert len(edition['units']) == len({m['previous_unit_id'] for m in edition['units']}) == 33
for m in edition['units']:
    u = chapters[m['v4_unit_id']]
    assert (m['v4_locator'], m['v4_title'], m['v4_printed_page']) == (u['locator'], u['title'], u['printed_page'])
    assert m['title_changed'] == (m['v2_title'] != m['v4_title'])
assert {m['previous_unit_id'] for m in edition['units'] if m['title_changed']} == {
    'scft-ch08', 'scft-ch14', 'scft-ch21', 'scft-ch22', 'scft-appb'}
assert set(edition['added_unit_ids']) == {
    'scft-v4-ch12', 'scft-v4-ch13', 'scft-v4-ch19', 'scft-v4-ch23', 'scft-v4-ch29', 'scft-v4-appb'}
assert set(expected_map.values()) | set(edition['added_unit_ids']) == set(books['scft']['chapters'])
baseline = yaml.safe_load(subprocess.check_output(
    ['git', 'show', s['revision_baseline'] + ':docs/plan/incerto-program/state.yaml'], text=True))
assert set(baseline['concepts']) <= concepts.keys()
assert list(concepts)[:len(baseline['concepts'])] == list(baseline['concepts'])
assert set(concepts) - set(baseline['concepts']) == {
    'c-probability-conflation', 'c-portfolio-tail-dependence'}
assert {cid for cid in baseline['concepts']
        if baseline['concepts'][cid]['completion_scope'] != concepts[cid]['completion_scope']} == {'c-lindy'}
assert concepts['c-lindy']['prior_scope']['completion_scope'] == 'out-of-scope'
for cid, c in baseline['concepts'].items():
    assert concepts[cid]['id'] == c['id'] and concepts[cid]['page_path'] == c['page_path']
assert set(baseline['chapters']) == set(expected_map) | {
    k for k in chapters if chapters[k]['book_id'] != 'scft'}

# Human views must agree on identities, titles, scopes and mappings.
plan = Path('docs/plan/incerto-program')
inventory = (plan / 'inventory.md').read_text()
register = (plan / 'concepts.md').read_text()
for key in active_chapters:
    u = chapters[key]
    assert f'<a id="{key}"></a>' in inventory
    row = next(line for line in inventory.splitlines() if f'<a id="{key}"></a>' in line)
    assert u['title'] in row and f'`{u["chunk_id"]}`' in row
    for cid in u['concept_ids']:
        assert f'(concepts.md#{cid})' in row
assert len(re.findall(r'<a id="c-[^"]+"></a>', register)) == len(concepts)
for cid, c in concepts.items():
    body = register.split(f'<a id="{cid}"></a>', 1)[1].split('<a id=', 1)[0]
    assert c['title'] in body and c['scope'] in body and c['page_path'] in body
    assert all(reason in body for reason in c['classification'].values())
    if cid in active:
        assert f'Milestone: **{c["milestone"]}**' in body
        assert all(f'`{k}`' in body for k in c['chunk_ids'])
    else:
        assert c['out_of_scope_reason'] in body
    for u in c['source_units']:
        if u in active_chapters:
            assert f'(inventory.md#{u})' in body
review_text = (plan / 'm0.5-review.md').read_text()
assert set(re.findall(r'^\| `(c-[^`]+)` \|', review_text, re.M)) == set(review['concept_ids'])

# Local file links and Markdown/MyST/HTML anchors; external URLs are not fetched.
def without_fences(text):
    return re.sub(r'(?ms)^(`{3,}|~{3,})[^\n]*\n.*?^\1[ \t]*$', '', text)

def anchors(path):
    text = without_fences(path.read_text())
    result = set(re.findall(r'<a\s+id=["\']([^"\']+)', text))
    result |= set(re.findall(r'^\(([^)]+)\)=', text, re.M))
    result |= set(re.findall(r'^:name:\s+(\S+)\s*$', path.read_text(), re.M))
    seen = {}
    for heading in re.findall(r'^#{1,6}\s+(.+)', text, re.M):
        heading = re.sub(r'\[([^]]+)\]\([^)]+\)', r'\1', heading)
        slug = re.sub(r'[^\w\s-]', '', heading.lower()).replace(' ', '-')
        ordinal = seen.get(slug, 0)
        seen[slug] = ordinal + 1
        result.add(slug + (f'-{ordinal}' if ordinal else ''))
    return result

checked_links = 0
for path in list(plan.glob('*.md')) + [Path('docs/plan/index.md')]:
    text = without_fences(path.read_text())
    for target in re.findall(r'(?<!!)\[[^]\n]+\]\(([^\s)]+)\)', text):
        if urlsplit(target).scheme or target.startswith('//'):
            continue
        file, _, fragment = unquote(target).partition('#')
        dest = (path.parent / file).resolve() if file else path.resolve()
        assert dest.is_file() or (not fragment and file.endswith("/") and dest.is_dir()), (path, target)
        if fragment and dest.suffix == '.md':
            assert fragment in anchors(dest), (path, target, 'missing anchor')
        checked_links += 1
print('State and human-view validation passed:', expected)
print('Local file/fragment links passed:', checked_links)
print('First three chunks:', sequence[:3])
PY
```

## Source and change-scope review

When the supplied files are available, use `pdftotext -f 7 -l 14 -layout`
on each read-only PDF and compare numbered/lettered TOC records with the
correspondence and v4 `title`, `locator`, `printed_page` fields. Exclude Roman
part headings and front/back matter. Verify all 33 old units, all 39 v4 units
and the six additions; keep raw extracts outside the repository. Record
PDF identities and any discrepancy in `sources.md` and `verification.md`.

The validation contract reflects completed mathematical review of the fixed
24-body inventory and its completed live review. Chapters 1–9 add seven guides,
eleven registered concept bodies, the supplementary hidden-tail note and
updated chapter-3/4 guides, with no added Lean evidence. The two CSN power-law
pages also postdate that frozen inventory.
Existing-page reuse is evaluated in chapter order so a later-created note
does not retroactively become evidence for an earlier chapter.
Chapter-specific build/max/publication reviews remain separate from implementation status.
Update it when later work changes those facts. Review the diff and any full
new files, run `git diff --check` plus new-file whitespace checks, and ensure
changed paths stay inside the authorized task scope. Site checks are separate;
an old artifact or an earlier operator
pass cannot establish a fresh build for this revision.
