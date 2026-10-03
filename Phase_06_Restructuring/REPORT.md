# Phase 6 - restructuring to Q1 (IJHMT / Elsevier) conformance

## Phase 6 (part 1) - numbered citation style

Applied in the builders, so the change is reproducible and survives regeneration:

1. **Numbered style.** Citations are renumbered to order of first appearance and the
   printed list is reordered to match (`1,2,3,...`, no duplicates, 55/55 entries cited,
   none orphaned; 48 of the 55 entries moved position - the Gurtin-Pipkin anchor went
   from [55] to [15]). The map is published as `13_Manuscript/REF_ORDER.json` and the
   printed order as `REFERENCES_ORDERED.json`, which `tools/md_to_tex.py` consumes, so
   Markdown, LaTeX, .docx and PDF agree. `01_Literature/REFERENCES_VERIFIED.json` keeps
   its thematic order on purpose: it is the verification record, not the printed list.
   Patch script: `verification/patch_phase6_numbering.py`.
2. **Table-row citations** are renumbered by the same pass. The first version skipped
   list-shaped block payloads, which left stale numbers in the provenance rows and
   orphaned two entries; `tools/audit_tex.py` caught it and the pass now recurses.
3. **Back matter.** Appendix A precedes the References section in the Markdown; the
   LaTeX path keeps it after `\bibliography` per `elsarticle`, which is also accepted.
4. **Freeze re-anchored** when the builders changed (03e at that point), with the
   2026-10-02 and earlier `10_03*` freezes byte-unchanged and no numerical input edited.
## Phase 6 (part 2) - back matter and Data availability

* **Data availability** named `CODE_FREEZE_v2_gate.json`, a freeze predating the
  submission anchoring, and repeated the Section 9 package inventory across a broken
  sentence boundary. It now resolves the submitted freeze through `SUB_FREEZE`, points at
  Section 9.1 instead of re-listing the package, and keeps the
  `[PUBLIC REPOSITORY/DOI TO BE INSERTED]` marker that `tools/audit_tex.py` gates on -
  the wording was fitted to the gate rather than the gate loosened, because the gate is
  what stops an unfinished statement from reaching the journal.
* **Acknowledgements** added as an unnumbered block ahead of the Declarations with an
  explicit author-input placeholder; `tools/md_to_tex.py` emits it as `\section*` so the
  LaTeX path does not number the back matter. Rendered Markdown order: Acknowledgements,
  Declarations, Appendix A, References (offsets 88001 / 88211 / 90126 / 92945).
* **Companion PDF** was stale after the bracket repair (`manuscript reference [15]`);
  regenerated with `tools/md_to_pdf.py -i/-o`.

## Phase 6 (part 3) - the AI disclosure (closes Phase 1 finding A4)

The declaration is rewritten in Elsevier's own sentence form: tool named, purpose stated,
authors reviewed and take full responsibility; the `[TEMPLATE - ...]` wrapper and the
clause about which models the service runs are gone, the research-process use stays in the
methods disclosure paragraph, and the safeguards are kept (no AI-generated physical result,
no AI-selected number, nothing acted without author review, AI is not an author and not a
citable source). Patch script: `verification/patch_phase6_ai_declaration.py`.

## Reviewed and deliberately unchanged

Abstract 249 of 250 words, single paragraph, no citations, no undefined abbreviations;
six semicolon-separated keywords (`thermoelasticity; cavity; monoclinic crystal;
beta-Ga2O3; Lord-Shulman theory; Bromwich inversion`); five Highlights at
78/70/69/74/69 characters against the 85-character limit; Section 7.2 already an explicit
limitations list (no physical validation, hypothetical relaxation times, model scope); the
title keeps its subtitle because the clauses after the colon carry the verification and
ablation claims that distinguish the paper. Recording these as reviewed is deliberate: a
later pass should not "fix" what already conforms.

## Verification after the last rebuild (freeze `submission_2026_10_03g`, 27 files)

`tools/audit_tex.py` ALL CHECKS PASSED; `tools/check_crossrefs.py` all cross-references
resolve; `tools/check_tex_commands.py` ALL COMMANDS DEFINED; `tools/verify_pdf.py` ALL
CHECKS PASSED for the manuscript (33 pages, 323 text units, 0 missing, 0 out-of-order) and
for the companion with `-c` (14 pages); structure 9 sections / 41 subsections / 84
equations / 8 figures / 11 tables / 55 references, ~10494 words; companion 11 / 37 / 29 /
9 tables, ~5272 words; citations 55/55 in monotone first-appearance order with no orphans.

**Phase 6 is closed** except for author-supplied content (`AUTHOR_FILLIN.md`) and the
literature-side P5-1 (Cattaneo 1948 / Vernotte 1958 primary sourcing). Phase 7 is the
language and style pass; Phase 8 the final audit and cover letter.
