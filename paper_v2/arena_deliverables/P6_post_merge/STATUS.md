# Post-merge status — review-paper-v2 (164 pages, commit 89fd325)

Written 2026-11-02, after the merge of `review-paper-v2` into this branch. Everything below is counted from
files in this repository, not from memory: the claim ledger is `paper_v2/claim_register.csv`, the
post-merge audit of the new text is `post_merge_claims.csv` in this folder, and the paper's own numbers are
in `final_paper_numbers.csv`. No `.tex` file and nothing in `paper_v2/scripts/` was touched.

## 1. Where the claim ledger stands

`claim_register.csv` holds **224 rows**: one per technical claim carried by the paper's appendix material.

| verdict | rows | what it means |
|---|---|---|
| SUPPORTED | 78 | a source, read at page level, says what the paper says |
| PARTLY SUPPORTED | 38 | a source says most of it; the paper's wording is stronger than the page |
| NOT SUPPORTED | 5 | a source in hand contradicts, or does not carry, the attribution |
| SOURCE NOT AVAILABLE | 103 | no copy in hand; nothing has been read, nothing is assumed |

Verification levels: **R3 = 81 rows** (page-level read with a locator and quoted wording), R0 = 75,
V0 = 28, V1 = 29, V2 = 10, R1 = 1. Before this pass R3 stood at 73 and 111 rows were SOURCE NOT AVAILABLE; the
eight rows settled in `claim_check_C_batch_008` account for the difference.

`claim_check_C` batches 001–008 now hold 71 decided rows (39 SUPPORTED, 27 PARTLY, 3 NOT SUPPORTED,
2 SOURCE NOT AVAILABLE).

## 2. What is still not in hand

- **103 distinct works** still carry SOURCE NOT AVAILABLE. Most block exactly one claim each; none is
  read, so none is described.
- `pdfs_needed_final.csv` lists the **57 highest-ranked of them** plus **3 works that are held only as
  image-only scans** (Stoneley 1924, Barnett 1985, Green–Naghdi 1991) — 60 rows, the cap. The remaining
  46 works are deferred only because of that cap, not because they matter less.
- One priority-list row is *not* a source: the held file for Chirita, D'Apice and Zampoli (2016) is a
  single-author paper in a different journal, so the three-author *Int. J. Heat Mass Transfer* article is
  still missing and still blocks its claims.

## 3. What the post-merge audit of the new text found

`post_merge_claims.csv`: **63 rows** — 48 SUPPORTED, 8 PARTLY, 5 SOURCE NOT AVAILABLE, 2 NOT SUPPORTED.
The 5 SOURCE NOT AVAILABLE rows are the provenance notes in Table 7 (Biot 1956, Green 1972, Green 1993,
Roy Choudhuri 2007, Quintanilla 2003 DPL): the page numbers printed there could not be checked.

### 3a. NOT SUPPORTED — the paper is wrong as printed

| where | what is printed | what is true |
|---|---|---|
| Table 2 (contributions C1–C7), p. 14, and Appendix A | C4/P6 uses `\cref` to an equation, which prints "(A)" | the intended target is equation (1); the label sits on an unnumbered heading |
| Tables 21–23 | they float to pp. 162–164, after the reference list ends on p. 161 | the appendix bodies name them in place; a reader following the text meets a reference list first |

### 3b. PARTLY — wording that overstates

1. **C3** claims "one worked example per family"; §31 carries four examples, and they are not one per family.
2. **§1.6 rule 4** tells the reader to consult an R0–R3 register the reader of the PDF cannot reach.
3. **p. 24** says energy is conserved exactly only for GN-II, which contradicts equation (19); the true
   statement is that GN-II is the case with a positive-definite functional.
4. **§22** quotes the flux split as 1.34 / 1.1 from figure scripts that were not re-run for this build.
5. **§36** presents a three-group taxonomy (Table 14) never mapped onto the paper's five axes.
6. **Table 25** caption implies *this* paper's equation numbers; they are the source's numbers.
7. **Table 24** basis column cites author–year while the paper cites numerically.
8. **Declarations** carry a generative-tool statement that cannot be verified from the PDF.

## 4. What was verified and holds

- The equation register prints 10 equations and 8 statuses; the benchmark registry prints 14 entries
  (B01–B14), all present in `benchmark_registry.csv`; the source register has 61 entries
  (30 CONDITIONAL, 17 UNVERIFIED, 5 DERIVED, 4 PRIMARY-SOURCE-CHECKED, 3 OPEN, 1 WITHHELD,
  1 VERIFIED-SYMBOLIC) and states coverage as 11 of 136.
- Table 19's R1–R10 "stated in" targets (§3, §22, §24, §27, §32, §33, Appendix I) all exist.
- Zener 1937 is the reed paper, as cited.
- Paper numbers: 164 pages, 90 numbered equations, 25 tables, 40 figures, 337 references, 38 sections,
  10 appendices, 49 section files (`final_paper_numbers.csv`).

## 5. Top ten next actions

1. Fix the `\cref` behind Table 2's C4/P6 so it prints (1) instead of "(A)"; re-check every `\cref` in
   the appendix set while the file is open.
2. Force Tables 21–23 to sit inside their appendix bodies, before the reference list.
3. Rewrite C3's "one worked example per family" to match §31's four examples.
4. Rewrite p. 24's GN-II sentence so it speaks of a positive-definite functional, not exact conservation.
5. Rewrite §1.6 rule 4 so it does not point at a register the reader cannot consult.
6. Re-run the §22 figure scripts, or state in the caption that the 1.34 / 1.1 split comes from an earlier
   build.
7. Map the §36 three-group taxonomy onto the five axes, or say explicitly that it is an orthogonal view.
8. Correct the Table 25 caption and the Table 24 basis column.
9. Decide the declarations' generative-tool wording so it is checkable from the paper itself.
10. Ask for the 57 listed sources (and text-layer copies of the three scans); each one settles exactly the
    claim it blocks, and the 46 deferred works follow once the cap allows.

## 6. Gates

| gate | command | state |
|---|---|---|
| paper numbers | `python3 paper_v2/arena_deliverables/P6_post_merge/measure_final_pdf.py` | PASS |
| post-merge claims | `python3 paper_v2/arena_deliverables/P6_post_merge/build_post_merge_claims.py` | PASS (63 rows) |
| needed list | `python3 paper_v2/arena_deliverables/P6_post_merge/build_pdfs_needed.py` | PASS (60 rows) |
| claim checks | `python3 paper_v2/arena_deliverables/P3_evidence_claims_C/check_claim_check_C.py` | PASS (8 batches) |
| README paths | `python3 paper_v2/arena_deliverables/check_readme_paths.py --root .` | PASS |
