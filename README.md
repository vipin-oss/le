# `le` — review paper workspace

**What this repository is:** the sources, the audit machinery and the evidence record for one review
paper. It is not a code library and not a book. If you are picking this up cold, read this page, then
`paper_v2/arena_deliverables/README_FOR_CLAUDE.md` (the deep log), then run the gates in §4.

| | |
|---|---|
| Paper | *Waves in Thermoelastic and Multiphysics Continua: Generalized Heat Conduction, Coupled Fields and Interface Phenomena* |
| Author | Vipin Gupta |
| Form | review paper — 38 sections + 10 appendices (A–J) + declarations |
| Current sources | `paper_v2/overleaf_package.zip` — the Overleaf tree as compiled (49 section files, the tables directory, the tikz figure sources and `refs*.bib`) |
| Last measured build | `paper_v2/main.pdf`: **164 pages, 90 numbered equations, 25 tables, 40 figures, 337 references** |
| Measured by | `paper_v2/arena_deliverables/P6_post_merge/measure_final_pdf.py` → `final_paper_numbers.csv` |
| Branch | `arena/9b458c54-le` |

The compiled PDF and the Overleaf package are in the repository so that the numbers above can be
re-measured; the figure PDFs they embed are inside the package. **`paper_v2/manuscript_v2/` is an older
snapshot (v1.1/v1.2), not the current paper** — it is kept because the audit trail refers to it.

---

## 1. Where to look, by what you want

| I want to… | Go to |
|---|---|
| **Read the paper** | `paper_v2/main.pdf` (164 pages) |
| **Read or rebuild its source** | `paper_v2/overleaf_package.zip` — main.tex, 49 section files, tables, tikz figures and `refs*.bib`; upload as-is to Overleaf |
| **Know what the P5 merge added** | `paper_v2/arena_deliverables/P5_merge/REPORT.md` and its `snippets/` |
| **See the post-merge audit** | `paper_v2/arena_deliverables/P6_post_merge/` — `post_merge_claims.csv`, `pdfs_needed_final.csv`, `STATUS.md` |
| **See what was checked, and how, in the earlier manuscript** | `paper_v2/arena_deliverables/P1_audit/PAGE_LEVEL_AUDIT_2026-11-01.md` |
| **Re-run the README gate** | §4, first command |
| **See the evidence registers** | `paper_v2/claim_register.csv`, `paper_v2/verification_register.csv`, `paper_v2/benchmark_registry.csv`, `paper_v2/atlas_targets.csv` |
| **Read the older manuscript** | `paper_v2/manuscript_v2/master/` — v1.2, 142 pages, 136 equations; snapshot only |
| **Know what is still open** | `paper_v2/arena_deliverables/P6_post_merge/STATUS.md` and `paper_v2/P1_DEFECT_REGISTER.md` |
| **The plan the work follows** | `paper_v2/BLUEPRINT_v3.1.md` (§10: phases P0–P7 with exit conditions) |

## 2. Layout

```
paper_v2/
├── main.pdf                  the paper as built (164 pages)
├── overleaf_package.zip      the paper as source (upload this to Overleaf)
├── arena_deliverables/
│   ├── README_FOR_CLAUDE.md  ★ the deep log: ground rules, provenance of every number
│   ├── P1_audit/             page-level audit of the v1.2 snapshot: scripts, CSV results, report
│   ├── P2…P4                 source audit, landmarks, evidence batches, second implementation
│   ├── P5_merge/             the merge package that produced the current text (snippets, conflicts, ledger)
│   ├── P6_post_merge/        audit OF the merge: claims, PDFs still needed, status
│   ├── submission/           zips that ship
│   └── check_readme_paths.py gate: keeps these READMEs true
├── manuscript_v2/            older snapshot (v1.1/v1.2) — not the current paper
├── versions/                 frozen v1.1 snapshot + pre-edit copies
├── claim_register.csv, verification_register.csv, benchmark_registry.csv, atlas_targets.csv
└── BLUEPRINT_v3.1.md         the plan, with per-phase exit conditions
```

## 3. Rules that explain most of this repository

1. **Nothing is asserted that cannot be located.** Every registered governing equation carries a status from a
   fixed vocabulary (Appendix J, Table 24); every printed DOI was checked against a bibliographic record
   before it was printed; a number that can be recomputed is given with its specification and tolerance
   (Appendix I).
2. **An edit is never silent.** A merged block of text is traceable to the snippet that produced it
   (`arena_deliverables/P5_merge/snippets/`), and the merge's disagreements are recorded in
   `P5_merge/conflicts.csv` rather than resolved invisibly.
3. **A coverage claim is a table, not an adjective.** The register states how many of the source
   manuscript's equations it covers (11 of 136, Table 25) instead of implying completeness.

The claim ledger behind those rules is `paper_v2/claim_register.csv`: **224 rows**, of which 78 are
supported, 38 partly supported, 5 not supported as worded and 103 still have no source; 81 rows rest on a
page-level read with a printed locator. The post-merge audit of the new text is a separate 63-row table,
`P6_post_merge/post_merge_claims.csv`.

## 4. Gates — run these before believing anything

```bash
cd paper_v2/arena_deliverables
python3 check_readme_paths.py --root ../..      # these READMEs: every path exists, numbers match the PDF
python3 P6_post_merge/measure_final_pdf.py      # re-measures paper_v2/main.pdf
python3 P6_post_merge/check_post_merge.py       # the post-merge audit tables are internally consistent
python3 P1_audit/check_refs.py                  # (v1.2 snapshot) labels unique, refs resolve, cites exist
```

Each prints a line beginning with `PASS` and exits 0.

The README gate compares the numbers quoted on this page and on `paper_v2/README.md` with
`P6_post_merge/final_paper_numbers.csv`, which is regenerated from `paper_v2/main.pdf` and
`paper_v2/overleaf_package.zip`. If the paper is rebuilt, re-run `measure_final_pdf.py` first.

## 5. What is genuinely open

| Item | Status |
|---|---|
| Register coverage | 11 of the 136 equations inventoried from the source manuscript carry a status; the rest are inventoried but not registered (Table 25). Expanding it needs per-equation verdicts — an author's call. |
| Post-merge defects | Two are open and recorded in `P6_post_merge/post_merge_claims.csv`: a cross-reference that prints "(A)" where it should print the momentum equation (Appendix A), and three appendix tables that float after the reference list (Tables 21–23). |
| Sources not yet read | `P6_post_merge/pdfs_needed_final.csv` lists what is still needed, most-blocking first. |
| Journal, DOI, expert review | Outside this workspace: no journal chosen (P0), no external reviewer (G5/G6). |
| Atlas case results | 40 case specifications with executable invariants exist; **0** case results. Never present these as results. |

## 6. Things not to do

- Do not edit the paper's `.tex` or `scripts/` — read-only.
- Do not present the atlas as results, or a status label as a validity certificate.
- Do not invent a DOI, page, quotation or title. Two works in the bibliography predate DOI assignment and
  say so; that is the correct handling.
- Do not put PDFs, Drive identifiers, links or source-library folder names into the repository.
- Do not quote a page or equation count from memory: read `final_paper_numbers.csv`.

Detail, provenance and the reasoning behind all of the above: `paper_v2/arena_deliverables/README_FOR_CLAUDE.md`.
