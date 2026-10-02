# FINAL QA REPORT

**Manuscript:** *Orientation-dependent wall stress around circular and elliptical cavities in
monoclinic β-Ga₂O₃ under a transient thermal pulse: a verified continuum study with thermal-memory
and mechanism ablations*
**Target:** International Journal of Heat and Mass Transfer (Elsevier, `elsarticle`)
**Branch / date:** `arena/01a0f67f-le` · 2026-10-01
**Scope of this revision:** publication readiness — editorial completeness, labelling, cross-
references, nomenclature, submission format. **Not** a re-run of the science: no number, result,
parameter, boundary condition or limitation was changed (see `CHANGELOG.md` §4).

---

## 1. What was produced

| File | Size | md5 | Notes |
|---|---|---|---|
| `FINAL_REVISED_MANUSCRIPT.tex` | 50,663 B | `92be5323a1ed3927d6f998c750ffed2e` | elsarticle source, generated from the `.md` |
| `FINAL_REVISED_REFERENCES.bib` | 9,663 B | `f043602236ce0ee628268e2ba4762533` | 23 entries, generated from the Crossref-verified JSON |
| `FINAL_REVISED_MANUSCRIPT.pdf` | 1,268,166 B | `d8129443dae188a9a8f85ad3a3034d9e` | 16 pages (md5 changes on every rebuild: PDF metadata carries a timestamp) |
| `manuscript_IJHMT.md` | 48,472 B | `72e8b7b2c0eb306779ac11d9bc48a95c` | the single source of truth |
| `manuscript_IJHMT.docx` | 1,079,829 B | `8d779040c358544d18c29a471292993f` | regenerated from the same build |
| `manuscript_IJHMT.pdf` | 1,268,166 B | `57d51f7fea6bda5c5af637b79bce7436` | project's own PDF, same content as the deliverable |

Content counts: **8 figures, 8 tables (79 rows), 3 numbered equations, 23 references**,
abstract **248 words** (limit 250), **5 highlights** of 69–78 characters (limit 85),
body ≈ **4,540 words**, 7 numbered sections + unnumbered Declarations + Appendix A (nomenclature).

---

## 2. How it was checked

Four independent gates. All are re-runnable and all exit 0 = pass.

### Gate 1 — static audit of the LaTeX source (`tools/audit_tex.py`): **66 checks, ALL PASSED**
No TeX engine exists in this environment, so the source is checked statically:

* **Portability** — file is pure ASCII (0 non-ASCII characters), no control characters, math
  delimiters balanced on every line, no empty or triple `$`.
* **Structure** — braces balanced (519/519); `begin`/`end` paired for `document`, `frontmatter`,
  `abstract`, `highlights`, `keyword`, `equation` (3), `figure` (8), `table` (8), `tabular` (4),
  `tabularx` (4), `itemize` (3).
* **Citations** — all 23 BibTeX entries are cited, every `\cite` key exists in the `.bib`, no
  empty `\cite`, and **no leftover numeric citations** such as `[3]` or `[1,2]`.
* **Cross-references** — every `\ref`/`\eqref` resolves to a `\label`; no empty `\ref`; **no
  hard-coded equation numbers**; every figure and table label is referenced from the text.
* **Graphics** — 8 `\includegraphics`, all files present under `../11_Figures/`.
* **Tables** — 8 tables; in each, the declared column count matches every row (0 bad rows);
  booktabs rules paired.
* **Editorial limits** — abstract ≤250 words, 3–5 highlights each ≤85 characters.
* **Required content** — author placeholder, primary/exploratory model wording, MCV3 labelled
  exploratory, "no experimental validation", ">10× expansion uncertainty", continuum-validity
  caveat, AI declaration, data availability, `[PUBLIC REPOSITORY/DOI TO BE INSERTED]`,
  `elsarticle` class, `elsarticle-num`, `\bibliography{FINAL_REVISED_REFERENCES}`.
* **Number carry-over** — 22 carried numbers (0.854, 28.7, 29.9, 0.966, 1.322, 6.4, 1.4, 1.078,
  2.0213e-03, 5.291e-03, 6.19e-04, 5.39e-03, 3.959, 25.3, 7686, 0.0515, 0.040, 0.198, 0.792,
  1.16, 0.08, 2.6) are present in the `.tex`; five of them are cross-checked against the master
  `.md`; the table count matches the `.md` (8 = 8).

### Gate 2 — conversion unit tests (`tools/test_md_to_tex.py`): **26 tests, ALL PASSED**
The unicode → LaTeX conversion is the riskiest part of generating the source, so it is pinned by
expected-output tests covering every pattern that occurs in the manuscript and that an earlier
version got wrong: chemical formulae (`β-Ga₂O₃`), bare subscripts (`t_w (t_th)`), math that the
markdown left outside its delimiters (`$\gamma$_B`, `N_$\theta$`, `A_$\varphi$`), combining
accents (`κ̄`, `σ̂`, `s̄`), en/em dashes, `µm`, `Lamé`, degrees, ellipsis, integral, `\%`, and
identifiers that must **not** be converted (`MASTER_PROMPT`).

### Gate 3 — PDF verification (`tools/verify_pdf.py`): **5 checks, ALL PASSED**
`[1] text fidelity` 174 units and 79 table rows present, 0 missing · `[2] margins` 0 blocks
outside the 2 cm text column · `[3] figures` 8, on pages 3, 6–12 · `[4] equations` 3, on pages
2, 4, 5 · `[5] figure/caption` 0 figures without a caption on the same page.

### Gate 4 — manual editorial read-through
The repaired text was read against the brief's non-negotiables: primary vs exploratory labelling
consistent in the introduction, §2.1, §5.4 and Table 7; the abstract's claims matched to one
decimal place and qualified; `C̄` defined; every figure and table pointed to from the text; all
limitations retained in §6 and in the abstract; placeholders reduced to the two required tokens.

---

## 3. Defects found and fixed during this pass

| # | Defect | Fix |
|---|---|---|
| 1 | Abstract over-claimed (modulation rounded up, ablation stated without its qualifier, caveats buried) | quantified to 1 dp (28.7 % / 29.9 %), qualified, caveats last; 248 words |
| 2 | Highlights up to 100+ characters, one stated a result without its caveat | rewritten, 69–78 characters; the last item carries the verified-not-validated message |
| 3 | Reference [23] (Huang 2025) in the verified list but never cited | cited in the introduction |
| 4 | Fourier / Lord–Shulman vs the two-relaxation-time kernel not ranked | primary vs exploratory stated in the introduction and §2.1; MCV3 labelled exploratory in §5.4 and Table 7 |
| 5 | §2.1 missing the initial conditions, the boundary conditions and the pulse definition | all stated in §2.1 |
| 6 | `C̄` used in §2.2 without a definition | defined as `C₃₃` in §2.2 and in the nomenclature |
| 7 | §5.4 referred to `Eq. (3)` where `Eq. (2)` was meant | corrected |
| 8 | **Regression introduced by fix 6:** the `×10⁻³` of `δ = 1.078×10⁻³` was left stranded at the end of the sentence | restored; the value is unchanged |
| 9 | `ε` used for both strain and the small parameter | `ϵ` for strain (text, Voigt components, Eq. (1), nomenclature), `ε` for the parameter |
| 10 | Nomenclature incomplete (14 of the symbols used) | extended to 27 rows |
| 11 | Fig. 1, Fig. 2, Fig. 7, Table 1, Table 2, Table 6, Table 8 never referenced in the text | pointers added at the natural places (no new claims) |
| 12 | Conversion defect: `$\rho c_{p}$` emitted as `\rhoc_{p}` (undefined control sequence) | command names are now separated from a following letter |
| 13 | Conversion defects: `$$$t_{th}$$$`, escaped underscores inside math, `Ga_2O_3`, `$\beta$-Ga...` | rewritten conversion with protected math regions (see Gate 2) |
| 14 | Placeholders of three different shapes | standardised to `[AUTHOR INPUT REQUIRED: …]` and `[PUBLIC REPOSITORY/DOI TO BE INSERTED]` |

---

## 4. What this QA does **not** prove — read before submitting

1. **The `.tex` has never been compiled.** There is no TeX distribution in this environment and
   none could be installed (no root, no network access to CTAN/PyPI mirrors). The source passed
   66 static checks and 26 conversion tests, but **static checks cannot prove compilability**.
   The authors must run `pdflatex` + `bibtex` and read the log before submitting (see
   `AUTHOR_INPUT_REQUIRED.md` A7).
2. **The delivered PDF is not an elsarticle rendering.** It is produced by the project's own
   renderer (`tools/md_to_pdf.py`) from the *same* `manuscript_IJHMT.md`, so its text, numbers,
   tables and figures are identical to the LaTeX source's content — but its layout, page breaks
   and reference formatting are not Elsevier's. The authoritative submission artefact is the
   `.tex`; the PDF is a faithful content rendering for reading and checking.
3. **Citation numbers will differ between the PDF and the compiled `.tex`.** The `.md` (and hence
   the PDF) uses the fixed numbering of the verified reference list; `elsarticle-num` numbers in
   order of first citation. The key ↔ entry mapping is identical — only the printed numbers move.
4. **Float placement is left to LaTeX.** Figures and tables use `[htbp]`; where they land in the
   compiled PDF may differ from the delivered PDF. Check for figures that drift far from their
   first mention.
5. **Figures are PNGs** at the project's own resolution. Elsevier wants 300 dpi or better; see
   `AUTHOR_INPUT_REQUIRED.md` A8.
6. **Table 2 promises supplementary material** (the full verification table) that is not part of
   these four files — see A9.
7. **One verification test fails and one is exploratory** (metric consistency on the hand-off-style
   96×48 grid at χ = 2: 5.03×10⁻³ against a 5×10⁻³ threshold). This is reported in the paper, not
   hidden, and the number is unchanged by this revision.
8. **Placeholders remain by design.** `[AUTHOR INPUT REQUIRED: …]` and
   `[PUBLIC REPOSITORY/DOI TO BE INSERTED]` cannot be filled from the data package.

---

## 5. Claims and non-claims

* **Claimed:** the four deliverables are complete and internally consistent; every number in them
  comes from `manuscript_IJHMT.md`, which is generated from the data package; nothing was
  invented — no author, affiliation, funder, DOI, repository, reference or result was added.
* **Not claimed:** that the LaTeX source compiles (it was not compiled); that the study is
  experimentally validated (it is not, and says so); that the continuum model is valid at 5–50 nm
  (not established, and stated); that the relaxation times are measured (they are hypothetical);
  that the reported modulation is a measured material property (it is a property of a verified
  continuum model with expansion data that are uncertain by more than an order of magnitude).

---

## 6. Reproduce

```bash
cd /home/user/le
python3 PAPER_PROJECT/13_Manuscript/build_manuscript.py     # .md + .docx
python3 tools/refs_to_bib.py                                # .bib (23/23, 0 unparsed)
python3 tools/md_to_tex.py                                  # .tex
python3 tools/audit_tex.py                                  # 66 static checks   -> ALL CHECKS PASSED
python3 tools/test_md_to_tex.py                             # 26 conversion tests-> ALL PASSED
cd PAPER_PROJECT/13_Manuscript
python3 ../../tools/md_to_pdf.py -o FINAL_REVISED_MANUSCRIPT.pdf
python3 ../../tools/verify_pdf.py                           # 5 PDF checks       -> ALL CHECKS PASSED
```
