# `le` — review paper workspace

**What this repository is:** the LaTeX sources, the verification machinery, and the audit record for one review
paper. It is not a code library and not a book. If you are picking this up cold, read this page, then
`paper_v2/arena_deliverables/README_FOR_CLAUDE.md` (the deep log), then run the gates in §4 below.

| | |
|---|---|
| Paper | *Multiphysics Wave Mechanics in Generalized Continua: A Constructive Review of Theory, Energy Transport, and Interface Phenomena* |
| Author | Vipin Gupta |
| Form | review paper — 17 sections + 6 appendices + declarations |
| Current sources | `paper_v2/manuscript_v2/master/` (39 `.tex`, 47,854 words) |
| Last measured build | 142 pages, 64,932 words, 136 numbered equations, 16 figures, 55 tables, 107 cited works |
| Branch | `arena/9b458c54-le` |

The compiled PDFs and the figure PDFs are **not** in this repository (size). Sources, audit tables and gates are.

---

## 1. Where to look, by what you want

| I want to… | Go to |
|---|---|
| **Read the paper's source** | `paper_v2/manuscript_v2/master/main.tex` → `sections/`, `appendices/`, `frontmatter/` |
| **Build it** | `paper_v2/manuscript_v2/master/BUILD.md` — `pdflatex main → bibtex main → pdflatex ×2` (Overleaf does this) |
| **Know what changed and when** | `paper_v2/manuscript_v2/CHANGELOG_v2.md` (v1.1 → v1.2 → v1.2a → v1.2b) |
| **See the editorial decisions** | `paper_v2/manuscript_v2/REVIEW_CYCLES.md` — three cycles, author→reviewer→editor→author |
| **See what was checked, and how** | `paper_v2/arena_deliverables/P1_audit/PAGE_LEVEL_AUDIT_2026-11-01.md` |
| **Re-run every number myself** | §4 below (five gates, each prints `PASS` and exits 0) |
| **Hand the package to someone** | `paper_v2/arena_deliverables/submission/le_review_v1.2_2026-11-01.zip` |
| **Know what is still open** | §5 below — and `P1_DEFECT_REGISTER.md` |
| **The plan the work follows** | `paper_v2/BLUEPRINT_v3.1.md` (§10: phases P0–P7 with exit conditions) |
| **The evidence registers** | `paper_v2/claim_register.csv`, `paper_v2/verification_register.csv`, `paper_v2/atlas_targets.csv`, `paper_v2/benchmark_registry.csv` |
| **An old version, unchanged** | `paper_v2/versions/v1.1_source_snapshot/` (frozen), `paper_v2/versions/v1.2_edits_2026-11-01/` (every edit's pre-edit file) |

## 2. Layout

```
paper_v2/
├── manuscript_v2/            working manuscript (this is the paper)
│   ├── master/               main.tex, sections/ (17), appendices/ (6), frontmatter/, figures/, tables/
│   ├── CHANGELOG_v2.md       every change, dated, with the reason
│   ├── REVIEW_CYCLES.md      the author→reviewer→editor→author record
│   └── README.md             build notes for the manuscript
├── arena_deliverables/
│   ├── README_FOR_CLAUDE.md  ★ the deep log: ground rules, what was verified, every number's origin
│   ├── P1_audit/             the page-level audit: script, CSV results, narrative report, gates
│   ├── submission/           the zip that ships (sources + figures + build docs)
│   └── P1…P4 artefacts       source audit, second implementation, defect register, release manifest
├── versions/                 frozen v1.1 snapshot + pre-edit copies of every edited file
├── working_notes/            retained working collections that are deliberately NOT part of the paper
└── BLUEPRINT_v3.1.md         the plan, with per-phase exit conditions
```

## 3. Two rules that explain most of this repository

1. **Nothing is asserted that cannot be located.** Every registered governing equation carries a status from a
   fixed vocabulary (Appendix A); every printed DOI was checked against a bibliographic registry before it was
   printed; a number that can be recomputed is given with its specification and tolerance (Appendix C).
2. **An edit is never silent.** A source may be edited, but the pre-edit file is kept in `versions/` and the change
   is declared in `CHANGELOG_v2.md`. The gate in §4 fails if either is skipped.

## 4. Gates — run these before believing anything

```bash
cd paper_v2/arena_deliverables
python3 check_readiness.py            # phases, claims, references, defects
python3 check_publish_pending.py      # publication gates, R0 items, atlas counts
python3 P1_audit/check_source_audit.py  # the source-level audit is intact
python3 P1_audit/check_refs.py          # labels unique, refs resolve, cites exist, braces/environments match
python3 P1_audit/check_page_audit.py    # the recorded page-level audit state, incl. equation inventory
python3 check_readme_paths.py --root ../..   # this README itself: every path it names exists, every number it quotes matches
```

Each prints a line beginning with `PASS` and exits 0. The page-level audit itself is recomputed with:

```bash
python3 P1_audit/audit_pages.py --pdf <compiled.pdf> --master ../manuscript_v2/master --out P1_audit
python3 P1_audit/build_equation_inventory.py --master ../manuscript_v2/master --pdf <compiled.pdf>
```

`audit_pages.py` deliberately distinguishes **pending rebuild** (source newer than the PDF) from **missing**
(source absent from the PDF). If you edit a source, the audit will say `N pending rebuild` until the PDF is rebuilt —
that is not a defect, and check P25 names the files.

## 5. What is genuinely open

| Item | Status |
|---|---|
| Equation register coverage | 29 register rows for 136 printed equations (21%). 6 of the 29 are DERIVED or PRIMARY-SOURCE-CHECKED. Expanding it is the main remaining P1 item and it needs per-equation verdicts — an author's call, not an auditor's. |
| Register traceability | 11 of 29 rows carry a `\eqref` pointer (added where the row's mathematics occurs in exactly one printed equation). 4 rows need a choice among restatements; 14 are prose rows. Candidates: `P1_audit/register_linkage.csv`. |
| Overfull boxes | Only the compile log reports them; they cannot be recovered from a PDF. Check the Overleaf log. |
| Journal, DOI, expert review | Outside this workspace: no journal chosen (P0), no external reviewer (G5/G6). |
| Atlas case results | 40 case specifications with executable invariants exist; **0** case results. Never present these as results. |

## 6. Workspace state you inherit (read this before trusting anything)

Two things live **outside** this repository and can be lost independently of git:

- the compiled PDFs (they are what `P1_audit/audit_pages.py --pdf …` measures), and
- the 18 figure source PDFs, of which 16 are shipped inside the submission zip and 2 (fig07, fig18) are declared
  provisional in Appendix D and were never tracked.

On 2026-11-01 both were lost when the sandbox reset: the 16 shipped figures were restored from the submission zip,
the two provisional sources and the compiled PDFs are **not recoverable from this repository**, and the local git
history was rolled back to the base commit and then restored with `git fetch origin` + `git reset --hard`.
Consequences for you:

1. Before trusting local `HEAD`, run `git fetch origin && git status` — the remote branch is authoritative.
2. The recorded audit results in `P1_audit/` stay valid for the builds they name (see the lineage table, §9 of the
   report); re-running `audit_pages.py` needs a PDF, i.e. a rebuild.
3. If a check reports a figure as absent, check whether it is one of the two provisional sources before treating it
   as a defect — `check_source_audit.py` now distinguishes "present but unaccounted for" from "not in this workspace".

## 7. Things not to do

- Do not edit `scripts/` — read-only.
- Do not present the atlas as results, or a status label as a validity certificate.
- Do not invent a DOI, page, quotation or title. Two works in the bibliography predate DOI assignment and say so;
  that is the correct handling.
- Do not put PDFs, Drive identifiers, links or source-library folder names into the repository.
- Do not rewrite the register's verdict column without the author.

Detail, provenance and the reasoning behind all of the above: `paper_v2/arena_deliverables/README_FOR_CLAUDE.md`.
