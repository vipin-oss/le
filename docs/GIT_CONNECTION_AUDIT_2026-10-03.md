# GIT_CONNECTION_AUDIT — 2026-10-03 (updated after the follow-through)

**Question asked:** is the paper connected to the `le` repository, and is that connection sound?
**Mode first pass:** verify-only, nothing pushed. **Second pass (user-approved):** fix what the audit found,
commit, and push the session branch — `main` untouched.
**Checked by:** `python3 tools/connection_audit.py` (added in this pass) plus the repository's own QA
harness (`tools/audit_tex.py`, `tools/check_tex_commands.py`, `tools/check_crossrefs.py`,
`tools/test_md_to_tex.py`, `tools/renumber_crossrefs.py`, `tools/verify_pdf.py`).

---

## 1. The connection itself — healthy

| Item | Value |
|---|---|
| Working copy | `/home/user/le` (a real clone, not a loose folder) |
| `origin` | `https://github.com/vipin-oss/le.git` — reachable over the network; `gh` authenticated as `vipin-oss` |
| Branch at audit time | `arena/01a10176-le` @ `18368e9`, `origin/main` @ `18368e9` — **the same commit** |
| Ahead / behind at audit time | `0 / 0` — nothing to push, nothing to pull |
| Tracked files | 1032 on `main` (1034 with the two files this audit adds) |
| Worktree vs HEAD | **all tracked files hash-identical to their HEAD blobs** (checked with `git hash-object`, not with git's stat heuristic) → no uncommitted paper edits |
| GitHub side vs local | `gh api repos/vipin-oss/le/git/trees/main?recursive=1` → 1032 blobs, `truncated: false`, **0 blob-SHA mismatches** against the local tree |
| Object database | `git fsck --full` clean, 0 garbage, 927 objects, 85 MiB pack |
| Commit identity | `vipin-oss <271452828+vipin-oss@users.noreply.github.com>` (set, local commits work) |
| PR history | PR #1 "Manuscript restructure to the requested format + calculation companion" — **MERGED** 2026-10-02 |
| LFS / `.gitattributes` | none — everything is a plain git blob (fine at these sizes) |
| Fetch refspec | narrowed to `main` + `arena/01a10176-le*`, so `git fetch origin` will not see other branches |

Conclusion: the paper *is* the repository's content; nothing was missing, uncommitted or unpushed.

## 2. The paper's artifacts, as stored in the repo

`PAPER_PROJECT/13_Manuscript/` — all present, all tracked on `main`:
`manuscript_IJHMT.md` (source of truth) · `manuscript_IJHMT.docx` · `manuscript_IJHMT.pdf` ·
`FINAL_REVISED_MANUSCRIPT.tex/.pdf` · `FINAL_REVISED_CALCULATIONS.tex/.pdf` · `calculations_IJHMT.md/.pdf` ·
`FINAL_REVISED_REFERENCES.bib` (54 Crossref-verified) · `highlights.txt` · `cover_letter.md` ·
`JOURNAL_FIT.md` · `SUPPLEMENTARY_TABLES.xlsx` · `MANUSCRIPT_STATS.json`.

Two properties worth knowing: `manuscript_IJHMT.pdf` and `FINAL_REVISED_MANUSCRIPT.pdf` are the **same
bytes** (as are the two companion PDFs), and every `\includegraphics`/`\input` target of both `.tex` files
exists in `11_Figures/` / `12_Tables/`.

QA harness on the committed files, before any change:

```
tools/audit_tex.py          → RESULT: ALL CHECKS PASSED   (84 equations, 11 tables, carried numbers present)
tools/check_tex_commands.py → RESULT: ALL COMMANDS DEFINED (0 unknown, 0 spacing glue, both .tex)
tools/check_crossrefs.py    → all cross-references resolve (9 sections, 84 eq, 11 tab, 8 fig)
tools/verify_pdf.py         → ALL CHECKS PASSED — 317 text units, 0 missing, 8 figures, margins clean
tools/verify_pdf.py -c …    → ALL CHECKS PASSED — 183 units, 0 missing, 28 equation images
```

## 3. Provenance of the committed tree

* `le.zip` (52 MB, committed on purpose): 985 files inside; **every one of them is either tracked in the
  repo or explicitly matched by a `.gitignore` rule** — no paper content is stranded in the archive.
  51 tracked files are *not* in `le.zip` (`.gitignore`, phase states, Crossref pass 3, the refreshed freeze…)
  — the repo is a superset of the delivered archive, which is correct.
* `work/handoff/MANIFEST_SHA256.json` recomputed independently: **303/303 read-only input files intact**,
  exactly as `PAPER_PROJECT/README.md` claims (304 files on disk = 303 + the manifest itself).
* Ignored by design and absent (regenerable, nothing lost): `PAPER_PROJECT/packages/` — the ZIPs the README
  links, rebuild with `python PAPER_PROJECT/00_Project_Control/make_packages.py final`;
  `13_Manuscript/equations/` (rebuilt by `build_manuscript.py`); `baseline_provided/`; `work/handoff.zip`.

## 4. Findings

| # | Finding | Action |
|---|---|---|
| **F1** | **Stale code freeze (2 of 27 entries).** `CODE_FREEZE_submission_2026_10_02.json` was written at `2026-10-02T07:04:07`; `13_Manuscript/build_manuscript.py` and `13_Manuscript/build_calculations.py` were edited later in that same restructure pass (`13_Manuscript/CHANGELOG.md` §0.5), so their digests no longer described the committed files (`7db9e69d…→4dbf9b5c…`, `9d8e0fad…→b346dcb6…`). | **Fixed (approved).** New `CODE_FREEZE_submission_2026_10_03.json` (27 files, 3,047 B, md5 `58d7ec343b2d8d50dc4a1d6a89b3f992`, sha256[:16] `dbc39e01f9cb4d40`) is now the deposited manifest; the 2026-10-02 file is **byte-unchanged** because its size/md5 are cited in `FINAL_QA_REPORT.md`. §9.1 and companion §11 rebuilt to cite it. |
| **F2** | All *result-bearing* code was already correct: 25/27 of the 2026-10-02 freeze matched, including all 8 solver modules and every `07_Tests`/`08_Experiments` script; `CODE_FREEZE_v2_gate.json` is 9/15 identical with exactly the six files the manuscript names. | Confirmed by recomputation, and now **enforced**: `tools/connection_audit.py` verifies the 9-of-15 statement in both documents, and both builders abort if the deposited manifest is not current (guard tested: one corrupted entry → `exit 1`, message names the regeneration command). |
| **F3** | The session branch had no upstream (nothing of this pass was on GitHub yet). | Branch pushed as `arena/01a10176-le`; `main` not touched, no PR opened. |
| **F4** | `tools/verify_pdf.py` check [2] (margins) excluded the *hard-coded manuscript* running title instead of the `-r/--running-title` value, so a companion's own header was not excluded — latent false positive, harmless today because both headers sit inside the 2 cm column. | **Fixed**; both documents re-verified, identical results, exit 0. |
| **F5** | *Not a repo defect — a mis-invocation.* Running `verify_pdf.py` on the companion without `-c -r "…"` reports 3 "MISSING" units. The correct invocation is already documented in `FINAL_QA_REPORT.md` (row "Companion PDF fidelity"). | Documented; see F7 for the underlying fragility it exposed. |
| **F6** | `le.zip` (52 MB) is above GitHub's 50 MB advisory threshold (100 MB is the hard block); already stored fine, no LFS. | none |
| **F7** | The companion fidelity test is pagination-sensitive: a paragraph that straddles a page break is split by the page header, and the search tolerates only a run of digits (the footer number) — so pass/fail of such a unit depends on where page breaks fall (3 such units in the 2026-10-02 build, 2 after an unrelated sentence grew). | **Fixed**: out-of-order units are counted as `out-of-order`, not `missing`, and a real `MISSING` now prints after how many characters the PDF stops agreeing and what follows on both sides. The strict sequential order test itself is unchanged. |
| **F8** | Two record errors: `FINAL_QA_REPORT.md` §0.1 said the manuscript PDF is **32 pp** and `13_Manuscript/CHANGELOG.md` §0.1 "32-page preprint", but the PDF has been 33 pages (footer 1–33) since the 2026-10-02 build. Separately, `md_to_pdf.py` prints the *manuscript's* running header on any document unless `-r` is given, and its PDF **metadata** title is hard-coded to the manuscript title (`md_to_pdf.py:441`). | Page count corrected to 33 in both records (with a note); the `-r` requirement is recorded here and in §5; the metadata title was **left alone** — cosmetic, and "fixing" it would rewrite both PDFs for nothing. |

## 5. Net effect (after the follow-through the user approved)

| Change | Why |
|---|---|
| `PAPER_PROJECT/06_Source_Code/CODE_FREEZE_submission_2026_10_03.json` (new) | F1 — 27/27 identical to the committed code; the 2026-10-02 manifest kept untouched as history |
| `13_Manuscript/build_manuscript.py`, `build_calculations.py` | cite the new manifest (§9.1 / companion §11) and abort if it is not current |
| `manuscript_IJHMT.md/.docx/.pdf`, `FINAL_REVISED_MANUSCRIPT.tex/.pdf`, `calculations_IJHMT.md/.pdf`, `FINAL_REVISED_CALCULATIONS.tex/.pdf`, `MANUSCRIPT_STATS.json` | rebuilt: **one paragraph changed per document**, `.tex` differs by 2 lines, page counts unchanged (33, 13), PDF bytes differ only in the embedded timestamp; the two names of each PDF are byte-identical pairs |
| `tools/connection_audit.py` (new) | this audit, re-runnable — git integrity, `le.zip` coverage, handoff manifest, manuscript references, remote reachability, freeze recomputation + the paper's own claims |
| `tools/verify_pdf.py` | F4 + F7 |
| `docs/GIT_CONNECTION_AUDIT_2026-10-03.md`, `13_Manuscript/FINAL_QA_REPORT.md` (§0.1 rows, new §0.5), `13_Manuscript/CHANGELOG.md` (new top section), `00_Project_Control/CHANGELOG.md`, `DECISION_LOG.md` (P13-D002), `REPRODUCIBILITY_STATUS.md` | the record, updated to match |

**Not touched:** `06_Source_Code/src/` (solver), `07_Tests`, `08_Experiments`, `09_Raw_Data`–`12_Tables`,
`01_Literature`, `14_Documentation`, `15_Audits`, `work/`, `le.zip`. No simulation was run: no number,
figure, table, parameter, limitation or label in the paper changed.

## 6. Reproduce

```bash
python3 tools/connection_audit.py            # sections A–F; exit 0 = everything green
python3 tools/audit_tex.py                   # 70 checks on the manuscript .tex
python3 tools/audit_tex.py -t PAPER_PROJECT/13_Manuscript/FINAL_REVISED_CALCULATIONS.tex \
        -m PAPER_PROJECT/13_Manuscript/calculations_IJHMT.md -c          # 54 checks on the companion
python3 tools/check_tex_commands.py ; python3 tools/check_crossrefs.py ; python3 tools/test_md_to_tex.py
python3 tools/renumber_crossrefs.py
python3 tools/verify_pdf.py                  # manuscript PDF fidelity (needs PyMuPDF)
python3 tools/verify_pdf.py -p PAPER_PROJECT/13_Manuscript/calculations_IJHMT.pdf \
        -m PAPER_PROJECT/13_Manuscript/calculations_IJHMT.md -c \
        -r "Worked calculations — cavity thermoelasticity in monoclinic beta-Ga2O3"
```

Rebuild chain used for the deliverables (order matters: freeze **before** rebuild, because the prose quotes
the freeze file's digest):

```bash
sh bootstrap_paths.sh
python3 PAPER_PROJECT/06_Source_Code/make_code_freeze.py submission_2026_10_03
python3 PAPER_PROJECT/13_Manuscript/build_manuscript.py
python3 PAPER_PROJECT/13_Manuscript/build_calculations.py
python3 tools/refs_to_bib.py
python3 tools/md_to_tex.py
python3 tools/md_to_tex.py -i PAPER_PROJECT/13_Manuscript/calculations_IJHMT.md \
        -o PAPER_PROJECT/13_Manuscript/FINAL_REVISED_CALCULATIONS.tex -c
cd PAPER_PROJECT/13_Manuscript
python3 ../../tools/md_to_pdf.py -o FINAL_REVISED_MANUSCRIPT.pdf
python3 ../../tools/md_to_pdf.py -o manuscript_IJHMT.pdf
RT="Worked calculations — cavity thermoelasticity in monoclinic beta-Ga2O3"
python3 ../../tools/md_to_pdf.py -i calculations_IJHMT.md -o calculations_IJHMT.pdf -r "$RT"
python3 ../../tools/md_to_pdf.py -i calculations_IJHMT.md -o FINAL_REVISED_CALCULATIONS.pdf -r "$RT"
```

Environment used: Python 3.11.2, numpy 2.4.6, scipy 1.17.1, matplotlib 3.11.2, reportlab 5.0.1,
PyMuPDF 1.28.2, python-docx 1.2.0, openpyxl 3.1.5. The four library versions that the freeze records are
identical to the 2026-10-02 manifest's, which is why the regenerated manifest lists the same environment.
`reportlab` and `pymupdf` are not in the base sandbox image and were pip-installed to run the PDF tools
(no repository change implied).
