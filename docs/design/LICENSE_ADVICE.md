# License Advice

Status: recommendation for a future licensing/publication decision.
Source review date: 2026-09-12.

Recommend **MIT for v1 across repository-owned code, documentation, mathematical
prose, original figures, notebooks, and Lean files**, subject to ownership review
and explicit third-party exceptions. It is the simplest policy for a repo that
mixes explanations with executable examples and follows the sibling root
licenses. The alternative is MIT for software and CC-BY-4.0 for authored
educational content when content-specific attribution is worth maintaining that
boundary.

This planning change does not add a `LICENSE`, grant new permissions, or relicense
source material. The owner still needs to adopt the policy and resolve the
Incerto source ambiguity before a public import.

## Evidence from the siblings

| Source inspected | Declaration | Implication |
| --- | --- | --- |
| [Normix root LICENSE](https://github.com/xshi19/normix/blob/master/LICENSE) | MIT; copyright 2020 xshi19 | Retain the notice when transferring covered material |
| [Incerto root LICENSE](https://github.com/xshi19/incerto-wiki/blob/main/LICENSE) (private) | MIT; copyright 2023 xshi19 | Evidence of a repository-level MIT declaration |
| [Incerto Python metadata](https://github.com/xshi19/incerto-wiki/blob/main/pyproject.toml) (private) | Package license is MIT | Consistent with MIT for its Python package |
| [Incerto MyST metadata](https://github.com/xshi19/incerto-wiki/blob/main/myst.yml) (private) | `project.license: CC-BY-4.0` | A separate content/site license signal that must be reconciled |

These files were read through authenticated GitHub access. The two root license
blob IDs were `b5cdc35c9593c920aa7f9e365ed3d3114c11d949` (Normix) and
`691e65ea893346051a2827d654b79ad47549b1dc` (Incerto). Incerto's inspected MyST
configuration blob was `3134a9ab0caf6067a8423b42a82d3666246bee2e`.
This checks specific declarations, not every file's ownership or the complete
history of published notices. It does not establish a license for the hub as a
whole.

## Source-license ambiguity

Both sibling **root** licenses are MIT. It would nevertheless be inaccurate to
conclude that all Incerto content is unambiguously MIT: the site configuration
declares CC-BY-4.0. This could reflect an intentional code/content split, an old
configuration default, or multiple grants by the owner. The files alone do not
settle which interpretation was intended or which permissions cover contributed
material.

**Open question:** what do the Incerto MIT and CC-BY-4.0 declarations each cover?
Before importing, inspect page-level metadata, published notices and exports,
contributor provenance, and earlier release declarations. Record the owner's
intended scope and the permissions available for each incoming work. Until then,
preserve the known notices and do not silently replace a content license with
MIT.

For material the owner fully controls, a new MIT grant can be considered without
assuming an earlier CC grant disappears. Creative Commons explains that its
licenses are irrevocable for compliant users. A new repository policy does not
erase permissions already granted for published versions.
[CC-BY-4.0 terms](https://creativecommons.org/licenses/by/4.0/).

If rights-cleared material cannot be offered under MIT, preserve its applicable
license as an identified exception, obtain permission from the relevant rights
holder, or omit it. Moving files and changing a site footer are not substitutes
for resolving rights.

## Compare the two policies

| Dimension | MIT across repository-owned material — recommended v1 | MIT software + CC-BY-4.0 content |
| --- | --- | --- |
| Scope | One default for code, prose, figures, notebooks, Lean, and developer guidance | Distinct licenses for software and educational expression |
| Reuse | Straightforward copying of an explanation together with its example | Familiar educational-content attribution terms; software keeps a software license |
| Required credit | Preserve applicable copyright and permission notices | MIT notices for software; CC attribution, license link, and change indication for covered content |
| Mixed files | One default for a notebook or a tutorial with embedded code | Must identify licenses for prose cells, code cells/snippets, figures, and other outputs |
| Maintenance | One default plus a third-party exception inventory | Two license texts, a scope map, and consistent source/site/export metadata |
| Best reason to choose | Low overhead while the project shape is still developing | A deliberate preference for content-specific attribution obligations |

MIT permits broad reuse, including commercial reuse, while requiring retention
of its notices in covered copies or substantial portions; it also contains a
warranty disclaimer. It covers software and associated documentation, making
it a practical default for this mixed project.
[OSI MIT license text](https://opensource.org/license/mit).

CC-BY-4.0 permits sharing and adaptation, including commercial use, with
attribution, a license link, and an indication of changes under its terms.
Creative Commons recommends software-specific licenses for software, while
allowing CC licenses for documentation. Keep Python and Lean code under MIT in
either proposal.
[CC-BY-4.0 summary](https://creativecommons.org/licenses/by/4.0/),
[CC guidance on software](https://creativecommons.org/faq/#can-i-apply-a-creative-commons-license-to-software).

MIT notice retention and academic citation serve different purposes. Under
either policy, the project's mathematical writing should still identify sources
and distinguish original derivation from an adapted explanation. Do not imply
that a scholarly citation request is an extra MIT license condition.

## Applying the MIT recommendation later

After the owner resolves scope and adopts MIT:

1. Add the standard MIT license with the appropriate rights-holder notice. Keep
   applicable upstream notices for imported Normix/Incerto material; do not
   replace earlier author/year information merely because files moved.
2. State in the README that MIT covers repository-owned material except for
   identified third-party items. Align package metadata, MyST metadata, rendered
   footers, downloadable source, and any exports with that scope.
3. Add `THIRD_PARTY_NOTICES.md` when incoming assets require it. Record origin,
   rights holder, license/permission, modifications, affected paths, and required
   attribution. Carry relevant notices into the deployed artifact as well.
4. Keep a clear contribution policy: contributors supply work they have the
   right to contribute under the declared license and identify exceptions. There
   is no need to introduce a complex contributor agreement for v1 by default.

“Whole-repo MIT” is shorthand for the default on rights-cleared, repository-owned
material. It does not overwrite licenses of dependencies, datasets, quoted text,
fonts, images, or bundled site assets. A public site needs to retain applicable
notices even though its source is maintained elsewhere.

## If the dual policy is chosen

Use an explicit division by material, not an unexplained pair of license badges.
A reasonable initial scope would be:

| Material | Proposed license |
| --- | --- |
| Python, Lean, scripts, tests, build configuration, agent guidance, engineering docs | MIT |
| Authored mathematical prose under `content/` and original explanatory figures | CC-BY-4.0 |
| Runnable code snippets embedded in content or notebooks | MIT, explicitly identified as an exception to the prose license |
| Notebook prose and original explanatory plots | CC-BY-4.0, with the mixed-file scope documented |
| External figures, data, quotations, or adapted material | Their actual license/permission; no automatic relabeling |

Use a root scope statement and separate full license texts, for example under
`LICENSES/`, with per-file or adjacent metadata where paths do not express the
boundary. Document mixed notebooks and generated outputs explicitly. A rendered
page should let a reader determine the license of both its prose and its code.
Check that MyST's supported metadata represents the chosen scope correctly.

This is a split policy: MIT applies to some material and CC-BY-4.0 to other
material. It is not an `MIT OR CC-BY-4.0` offer allowing either license for every
file, nor a blanket requirement to satisfy both licenses for all files. If the
same work is intentionally offered under either license, state that separately.

The extra boundary work is the main reason to prefer MIT for v1. A later policy
change must account for contributions and existing grants; it is not merely an
edit to the root license file.

## Private-to-public review

A private source repository and a public rendered site have different exposure
surfaces. Public source includes hidden directories, comments, Git history,
notebook metadata, test fixtures, and files excluded from the site table of
contents. Public artifacts may expose downloadable Markdown, notebook sources,
JSON, search indexes, and source/edit links.

The future import should use this sequence:

1. Inventory the candidate source and its rights/provenance at a recorded
   revision. Classify each item as publish, adapt, retain privately, or exclude.
   Keep the exclusion list private if it reveals private material.
2. Export only approved files into a clean staging area. Do not merge private
   repository history, agent transcripts, or an unreviewed archive into public
   Git history.
3. Inspect source, hidden files, comments, notebook outputs/metadata, absolute
   paths, data samples, embedded URLs, personal information, and credentials.
   Secret scanning is useful, but does not establish that publication is safe
   or that copyright permissions are sufficient.
4. Review every external PDF, diagram, screenshot, figure, data source, code
   excerpt, and substantial quotation. Retain the permission or license
   evidence; replace or exclude items that cannot be cleared.
5. Build from the approved export and review the full artifact, including source
   downloads, search/JSON data, metadata, notices, and links to private locations.
6. Review the exact proposed public commit and record which revision/artifact
   was reviewed before publication. Resolve identified issues before the
   [cutover gate](../plan/consolidation.md#one-time-consolidation-phases).

Keep already published source versions and notices in the rights assessment;
the private status of the authoring repository does not imply no public grant
was made. If a credential is discovered to have been exposed, removing it from a
new commit does not invalidate the old credential; handle its rotation as a
separate incident response.

## Paraphrase and cite

The default authoring method is original explanation, independent derivation or
reproduction of calculations, and precise citations to the work being discussed.
For a book or paper, record the author, title, edition/year, and relevant chapter,
section, theorem, or page where available. Link to an authorized source and make
the distinction between the source's claim and the repository's own analysis.

Use a short direct quotation only when the wording itself matters, mark it as a
quotation, and attribute it. Do not turn a reading guide into a replacement for
the book. Avoid closely paraphrasing a whole chapter, translating it as a means
of copying it, or reproducing its figures without a rights basis. A citation,
an openly downloadable PDF, or access through a private repository does not by
itself grant permission to redistribute the source.

Paraphrasing and citation are sound editorial defaults, not a legal safe harbor.
When relying on an exception such as U.S. fair use, the assessment depends on the
particular use; there is no universal safe word count or percentage. Use a
permission/license review for uncertain substantial reuse instead of inventing
an automatic excerpt allowance.
[U.S. Copyright Office fair-use guidance](https://www.copyright.gov/fair-use/).

**Open question:** is content-specific CC attribution important enough to justify
the mixed-file policy now? The recommendation remains MIT for v1 once ownership
and the Incerto declarations are resolved. This advice prepares that decision;
it does not make it on the owner's behalf.
