# AUTHOR INPUT REQUIRED

Everything in this file is something **the authors must supply, decide or confirm** before the
paper can be submitted. None of it can be produced from the data package, and none of it may be
invented on the authors' behalf. Items are grouped as **blocking** (the submission is incomplete
without them), **decisions** (judgement calls the authors should make) and **open scientific
items** (things that are genuinely unknown and are already disclosed in the paper).

Every placeholder in the deliverables uses one of two exact tokens:

* `[AUTHOR INPUT REQUIRED: …]`
* `[PUBLIC REPOSITORY/DOI TO BE INSERTED]`

---

## A. Blocking — the submission cannot go out without these

### A1. Authors, affiliations, ORCID, corresponding author
`FINAL_REVISED_MANUSCRIPT.tex` currently contains

```latex
\author{[AUTHOR INPUT REQUIRED: author names, affiliations, ORCID iDs and corresponding author]}
```

with a commented template directly above it. Replace it with, for example:

```latex
\author{Firstname Lastname\corref{cor1}}
\ead{author@institution}
\affiliation{organization={Institution},addressline={Street},city={City},country={Country}}
\cortext[cor1]{Corresponding author.}
```

Needed: full names in the order the authors want them, one `\affiliation` block per affiliation,
ORCID iDs if the journal's submission system does not collect them separately, and the
corresponding author's e-mail. The same information must be filled into the author line of
`manuscript_IJHMT.md` / `.docx`.

### A2. CRediT authorship contribution statement
Currently `[AUTHOR INPUT REQUIRED]` (in **Declarations**). The journal asks for a contribution
statement per author; this cannot be written from the data package because it is a statement about
who did what.

### A3. Declaration of competing interest
Currently `[AUTHOR INPUT REQUIRED]`. Must state either that the authors have no competing
interests, or list them.

### A4. Funding
Currently `[AUTHOR INPUT REQUIRED]`. Either name the grants, or state that the work received no
funding. Do not leave it blank.

### A5. Data availability — deposit and DOI
The text states that the code, verification suite, raw outputs, analysis scripts and the
production matrix are in the project data package, whose contents are fixed by the SHA-256 code
freeze `06_Source_Code/CODE_FREEZE_submission_2026_10_03j.json` (27 files) — the archived
`CODE_FREEZE_v2_gate.json` is named alongside it as history — **to be deposited at
`[PUBLIC REPOSITORY/DOI TO BE INSERTED]`.** Deposit the package under a licence and replace the
placeholder with the repository URL and DOI. `tools/connection_audit.py` re-derives the manifest
from the repository, so the placeholder is the only thing missing.

### A6. Declaration on generative AI and AI-assisted technologies
The declaration above the references now follows Elsevier's own wording and covers only the
**writing** process (drafting and revising the text and captions, and checking internal
consistency), with the statement that the authors reviewed and edited the content and take full
responsibility. The **research**-process use — reviewing and extending the numerical code and its
verification suite, and running the simulations — is disclosed in the numerical-methods section,
as the policy directs; the two are deliberately kept apart. The template marker has been removed,
so the text reads as final: **the authors must still read it, confirm that it matches what
happened, and edit anything that does not.** Do not submit a disclosure you have not checked.

### A7. Compile the LaTeX source
No TeX engine exists in the environment where this revision was produced, so
`FINAL_REVISED_MANUSCRIPT.tex` has **never been compiled** — it was checked statically only (see
`FINAL_QA_REPORT.md`). Before submission run

```bash
pdflatex FINAL_REVISED_MANUSCRIPT
bibtex   FINAL_REVISED_MANUSCRIPT
pdflatex FINAL_REVISED_MANUSCRIPT
pdflatex FINAL_REVISED_MANUSCRIPT
```

and check the log for warnings (overfull boxes, float placement, missing figures). `compile_check.sh`
in `Phase_10_Submission_Package/` runs exactly these commands and triages the log into
`COMPILE_CHECK.txt`. The `.tex` loads the vector figures through `\graphicspath{{figures/}}`, so keep
`13_Manuscript/figures/` next to the source; if that set is absent the converter falls back to
`../11_Figures/*.png`, in which case both directories must stay together.

### A8. Figure formats — prepared, needs your confirmation only
Done in Phases 9 and 10: every figure exists in all three renditions at 300 dpi or better, verified by
`11_Figures/export_submission_figures.py` (8 vector PDFs in `13_Manuscript/figures/`, which is what the
`.tex` uses; 600-dpi PNGs; LZW-compressed 600-dpi TIFFs in `11_Figures/submission/`, which is what a
journal that insists on raster TIFF should receive). **Nothing to produce here** - only confirm against
the journal's art guide which format it wants, and note that the TIFFs and PNGs are gitignored
regenerated artifacts, so rebuild them with that exporter if the working copy lacks them.

### A9. Supplementary material
Table 2 is captioned “Summary of the verification suite (full table: supplementary material)”.
The full tables are supplied: `13_Manuscript/SUPPLEMENTARY_TABLES.xlsx` carries eight sheets
(README, Verification, PhiSweep_ellipse, Convergence_6phi, D_lambda_eps, Ablations, Parameters,
Production_runs), built by `13_Manuscript/build_supplement.py` from the same analysis outputs as
the manuscript, so the caption is satisfied. Supply the workbook as the supplementary file and
check that the journal's submission system preserves its sheet order; the per-run npz/json
outputs belong to the data package, not to the supplementary file.

### A10. Cover letter
A complete draft is at `13_Manuscript/cover_letter.md`, refreshed on 2026-10-03 so that its
figures match the manuscript (55 numbered references, the 28.7% modulation, the 2026-10-03j
freeze, the 28-case suite, the Cattaneo/Vernotte citation note). It already states the position
honestly — a verified continuum study, not experimentally validated — and carries bracketed
fields the authors must complete: the editor's name if known, suggested reviewers, the
corresponding author, and confirmation of the declarations. Nothing has been sent.

---

## B. Decisions the authors should make

| # | Decision | Current state in the files |
|---|---|---|
| B1 | `preprint` (1-column, 12 pt) vs `review` (double-spaced) vs `5p` | source uses `preprint,12pt` |
| B2 | Keep the exploratory two-relaxation-time (MCV3) kernel in the main text, or move it to supplementary material | kept, labelled **exploratory** wherever it appears (§1.3, §2.5, §6.4, Table 9) |
| B3 | Keep the nomenclature as Appendix A, or move it into the main text | Appendix A, as Table 11 |
| B4 | Reference style | `elsarticle-num` (numbers in order of first citation). Note that this renumbers the citations relative to the fixed `[1]`–`[54]` numbering used in the `.md`/PDF: the mapping key ↔ number is preserved, only the printed numbers change |
| B5 | Whether the abstract should carry the ablation numbers or only the headline modulation | abstract carries 28.7 % (extrapolated) and 29.9 % (grid) and states that ablations attribute the modulation to expansion and stiffness anisotropy |
| B6 | Whether to report the 298 K-like expansion sensitivity in the abstract | currently not in the abstract (it is in §6.5 and Table 9) |
| B7 | Where to state the licence of the deposited data package | in Data availability, next to the DOI |
| B8 | Whether the calculation companion (`FINAL_REVISED_CALCULATIONS.tex`) is submitted as supplementary material, as an appendix, or hosted with the code | provided as a separate document; not yet attached to any submission route |
| B9 | Whether the 9-section / 84-equation expansion stays as-is for the target journal, or is compressed for a shorter article-type | kept as-is (32-page preprint; ≈ 15–18 pp in the journal's two-column layout) |

---

## C. Open scientific items — already disclosed, cannot be closed here

These are **not** defects to be fixed; they are limits of what the study can support, and each is
stated in the paper. They are listed so that the authors do not accidentally over-claim in the
cover letter or in responses to reviewers.

1. **No physical validation.** No transient cavity measurements for β-Ga₂O₃ are available to the
   authors; every comparison in the paper is against an exact solution or an independent
   implementation of the same mathematical model. Status: `APPLICABLE — EVIDENCE_UNAVAILABLE`.
2. **Relaxation times are hypothetical** (τ = 1, 5, 20 ps; order-of-magnitude estimates only:
   grey τ ≈ 0.9 ps, long-MFP phonons τ ≈ 0.2 ns). The memory results are sensitivities, not
   measurements.
3. **Continuum validity at 5–50 nm is not established.** Grey MFP ≈ 3 nm, while heat-carrying
   phonons with MFPs up to about 0.7–1 µm exist in β-Ga₂O₃.
4. **Thermal-expansion data are uncertain by more than an order of magnitude** between the two
   cited data sets; this moves the absolute stress scale (the mean peak changes by a factor
   ≈0.063), while the orientation modulation is relative and much less affected.
5. **`c_p` = 560 J/(kg K) is assumed**, against reported values of 485–537 J/(kg K).
6. **`α₅ = 0` is assumed**, and the b-axis expansion enters only through `C₁₂`, `C₂₃`, `C₂₅`.
7. **Coverage is partial by design:** the thermal-memory and feedback runs were made for the
   circular cavity only, and the elliptical cavity was run with Fourier conduction.
8. **`R = 80a` with a clamped cold outer boundary** means elastic echoes are model features for
   `a ≥ 20 nm`; the quantity-of-interest window (`t ≤ 6 t_th`) is echo-free only for
   `a ≤ 10 nm`. (Doubling R changed the peak by ≤0.3 % and D by ≤5.4 %.)
9. **A 192×192 grid could not be run** within the 2 GB memory available; the reported uncertainty
   comes from the extrapolated sweep, not from that grid.
10. **One verification test fails**: metric consistency (linear field) on the hand-off-style
    96×48 grid at χ = 2 (5.03×10⁻³ against a 5×10⁻³ threshold), dominated by angular resolution.
    It is reported as a failure, not hidden. One further test is marked exploratory.
11. **AI assistance** was used for code review, simulation runs and drafting (see A6), including a
    past rotation-tensor sign error, the earlier periodic-pulse synthesis, and the under-resolved
    wall mesh — all of which are disclosed in the paper's AI declaration and AI-error section.

---

## D. Checklist before submission

```
[ ] A1  authors, affiliations, ORCID, corresponding author filled in (.tex and .md)
[ ] A2  CRediT statement written
[ ] A3  competing-interest statement written
[ ] A4  funding statement written
[ ] A5  data package deposited; DOI inserted in Data availability
[ ] A6  AI declaration reviewed, edited and confirmed by the authors
[ ] A7  .tex compiled cleanly with pdflatex + bibtex; log checked
[ ] A8  figure formats/resolution acceptable to the journal
[ ] A9  supplementary material (full verification table) prepared
[ ] A10 cover letter written
[ ] A11 re-run `python3 PAPER_PROJECT/06_Source_Code/make_code_freeze.py <label>` and deposit the
        refreshed manifest with the data package (the 2026-10-01 manifests no longer describe
        six edited files; see manuscript §9.1 and 15_Audits/RERUN_COMPARISON.md)
[ ] B   decisions B1–B7 taken
[ ]     every [AUTHOR INPUT REQUIRED] and [PUBLIC REPOSITORY/DOI TO BE INSERTED] gone
[ ]     numbers in the text re-checked against the data package by the authors
```

The last item matters most: the authors, not the tooling, are responsible for the scientific
content. Everything the tooling produced came from `manuscript_IJHMT.md`, and every number in
that file comes from the data package.
