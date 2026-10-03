# Phase 7 - language, style, internal vocabulary, duplication

Read-only screening first (`verification/lang_audit.py`, machine output
`lang_audit.json`), then edits applied **in the builders** so they survive every
regeneration (`verification/patch_phase7_language.py`, plus two follow-up passes
recorded below). No number, no claim, no citation and no deposited filename changed.

## What the screen found and what was done

| Finding class | Before | After | Action |
|---|---|---|---|
| A - project-internal vocabulary in printed text | "Code state and re-checks", "the gate freeze", "the audit records", "manuscript builders", "the number of runs audited", a `PAPER_PROJECT/` path prefix in a sentence | none of those phrases | reworded to reader-facing terms: **Code state**, the archived manifest, the verification records, the manuscript sources / manuscript build scripts, the number of runs covered, "in the deposited package under 06_Source_Code/..." |
| B - banned hyperbole ("robust") | 1 (companion) | 0 | "the shape ... is robust to which expansion set is used" -> "is insensitive to which expansion set is used" (same claim, no forbidden word) |
| C - duplication | 4 duplicate/4 shared sentences | unchanged | all four are the front matter and the declarations, which **must** agree between manuscript and companion; there is no duplicated *content* paragraph |
| D - orthography and mechanics | -ized/-ise mixed (prose "generalized", "generalizations"), "Sections 5.1-5.3" with a hyphen while every other numeric range uses an en dash, 0 double spaces, "et al." always punctuated | prose unified to -ise, range fixed to 5.1–5.3 | the two **-ized** words left in the manuscript are inside verbatim reference titles (Lord-Shulman [13]; Huang et al. [18]) and were deliberately not touched |
| E - readability | 62 sentences >= 45 words, longest 113 | 4 of the worst clause chains split | the dimensionless-number paragraph (Lambda / epsilon / delta) and the memory-deviation result were split at their semicolon clause boundaries, and the Data availability sentence was divided in two; clauses kept verbatim |
| F - abbreviations | CV / F used with no definition | CV/F glossed at first use | "where CV and F denote the Cattaneo-Vernotte (single-relaxation-time) and Fourier responses"; the screen's "(X)" heuristic still lists CV, which is why the gloss was checked by hand |

Also repaired while in this area (a Phase 6 leftover, grammar not content): the Data
availability sentence read "... under the persistent identifier to be deposited at
[PUBLIC REPOSITORY/DOI TO BE INSERTED]" - an artefact of a placeholder substitution - and
now reads "... under the persistent identifier recorded at submission [PUBLIC
REPOSITORY/DOI TO BE INSERTED]", keeping the literal marker `tools/audit_tex.py` gates on.

## Reviewed and deliberately kept

* The archived manifest filenames (`CODE_FREEZE_v2_gate.json`, `CODE_FREEZE_v2_blockF.json`)
  and the package's folder names: they name real files inside the deposited package, so
  they are evidence, not jargon. What was removed is the internal *labelling* of them
  ("gate freeze") and the programme vocabulary around them.
* The 113-word contributions sentence: it is a single (i)-(iv) enumeration, which is normal
  for a contributions paragraph; splitting it would have obscured the parallel structure.
* `MCV3 = two-relaxation-time kernel (exploratory)` in the Table 10 caption already glosses
  the other model label; the "(74) is the mistake this plan replaces" style phrasing in
  Section 4 is a deliberate, factual statement about a superseded method.
* Acronyms the screen flagged but which are standard or already defined: ACM (in journal
  titles), LU (factorisation), CSV, SHA, GB, AI; AUTHOR/INPUT are placeholder capitals.

## Rebuild and gates

Builders changed twice during the pass, so the documents were regenerated against
`CODE_FREEZE_submission_2026_10_03i.json` (27 files); 03h, 03g and every earlier freeze are
byte-unchanged, and the companion's supersession list names 03h/03g/03f.

`tools/audit_tex.py` ALL CHECKS PASSED; `tools/check_crossrefs.py` all cross-references
resolve; `tools/check_tex_commands.py` ALL COMMANDS DEFINED; `tools/verify_pdf.py` ALL
CHECKS PASSED on the manuscript PDF and on the companion PDF (`-c`). Structure and limits
unchanged: 9 sections / 41 subsections / 84 equations / 8 figures / 11 tables / 55
references, abstract 249 of 250 words, highlights 78/70/69/74/69 characters, ~10.5k words
in the body, companion ~5.3k.

Next: Phase 8 - final audit, consistency, submission checklist and the cover letter.
