# CHANGELOG — publication-readiness repair

**Paper:** *Orientation-dependent wall stress around circular and elliptical cavities in monoclinic
β-Ga₂O₃ under a transient thermal pulse: a verified continuum study with thermal-memory and
mechanism ablations*
**Target journal:** International Journal of Heat and Mass Transfer (Elsevier, `elsarticle`)
**Branch:** `arena/01a0f67f-le` · **Date:** 2026-10-01

This file records **every** change made to the manuscript during the publication-readiness pass.
Nothing here changes a number, a result, the physical model, the geometry, the boundary or initial
conditions, the material parameters, or any limitation. The scientific content of the submitted
work is unchanged; what changed is how completely and how carefully it is stated, plus the
submission-format artefacts.

The single source of truth is `PAPER_PROJECT/13_Manuscript/manuscript_IJHMT.md`, which is built by
`build_manuscript.py` from `ms_static.py` / `ms_results.py` / `docbuilder.py`. The `.docx`, the
PDF and the LaTeX source are all generated from it, so they cannot drift apart.

---

## 1. Deliverables added

| File | What it is | Size |
|---|---|---|
| `FINAL_REVISED_MANUSCRIPT.tex` | elsarticle submission source (`preprint,12pt`, `elsarticle-num`) | 50,635 B |
| `FINAL_REVISED_REFERENCES.bib` | 23 BibTeX entries, all Crossref-verified | 9,663 B |
| `FINAL_REVISED_MANUSCRIPT.pdf` | 16-page PDF of the final revised manuscript | 1,268,113 B |
| `CHANGELOG.md` | this file | — |
| `AUTHOR_INPUT_REQUIRED.md` | everything the authors must supply or decide | — |
| `FINAL_QA_REPORT.md` | what was checked, how, and what is still open | — |

New tooling (persisted in `tools/`, so the artefacts can be regenerated):

| Tool | Purpose |
|---|---|
| `tools/refs_to_bib.py` | builds the `.bib` from `01_Literature/REFERENCES_VERIFIED.json` (no hand-typed entries) |
| `tools/md_to_tex.py` | builds the `.tex` from `manuscript_IJHMT.md` (unicode → LaTeX math, booktabs/tabularx tables, `\eqref` / `\ref` / `\cite`) |
| `tools/audit_tex.py` | 66 static checks on the `.tex` (exit 0 = all pass) |
| `tools/test_md_to_tex.py` | 26 unit tests pinning the unicode → LaTeX conversion |

---

## 2. Changes to the manuscript text

Each item was made in the **builder** (never by hand-editing the generated `.md`), and each was
re-verified after the rebuild.

### Abstract and highlights
1. **Abstract de-overclaimed and quantified.** The modulation is now quoted to one decimal place
   (28.7 % on the extrapolated sweep, 29.9 % on the production grid) instead of being rounded up;
   the ablation statement carries its exploratory qualifier; and the closing sentence states
   plainly that the results are properties of a verified continuum model — no experimental
   validation, hypothetical relaxation times, >10× expansion uncertainty, continuum validity at
   5–50 nm not established. **248 words (limit 250).**
2. **Highlights tightened** to 5 items of 69–78 characters (Elsevier limit 85); the last item
   carries the verified-not-validated message rather than a result claim.

### Scope and labelling
3. **Fourier + Lord–Shulman declared the primary conduction models**, in both the introduction and
   §2.1; the two-relaxation-time kernel is labelled an **exploratory sensitivity variant** in the
   introduction, in §2.1, in §5.4 and in Table 7. Previously the manuscript introduced the models
   without saying which were primary, which let the exploratory kernel look like a co-equal result.
4. **Reference [23] (Huang 2025) is now cited** in the introduction. It was in the verified
   reference list but appeared nowhere in the text.
5. **§2.1 completed.** Coordinates and rotation convention, initial conditions
   (`u = θ = 0`, `∂u/∂t = 0` for `t < 0`), traction-free cavity wall with the prescribed wall
   temperature, the pulse (`t₀ = 2.5 t_th`, `t_w = 1.2 t_th`), and the outer boundary
   (`R = 80a`, clamped and cold) are now stated where the model is defined rather than being
   scattered or implicit.

### Definitions, symbols and cross-references
6. **`C̄` is defined** as `C₃₃` where it is first used (§2.2) and in the nomenclature. It was
   previously used in the feedback number without a definition.
7. **Wrong equation reference corrected** in §5.4: `Eq. (3)` → `Eq. (2)`.
8. **Exponent restored in §2.2.** The sentence now reads `δ = T₀β·β/(ρc_pC̄) = 1.078×10⁻³, where
   C̄ = C₃₃ …`. While the `C̄` definition was being added, the `×10⁻³` had been left stranded at the
   end of the sentence; it is back on the number. The value is unchanged (1.078×10⁻³).
9. **Strain symbol split.** `ϵ` is used consistently for strain (text, Voigt components
   `ϵ₁₁, ϵ₃₃, γ₁₃`, Eq. (1), nomenclature) and `ε` for the small elastic-inertia parameter.
10. **Nomenclature extended** from 14 to 27 symbols: `θ, T₀`, `u`, `ϵ`, `σ`, `α`, `R`,
    `p(t), t₀, t_w`, `F(t)`, `λ, μ, m, γ_T`, `C̄ = C₃₃`, `g(s)`, `N_r × N_θ`.
11. **Every figure and table is now referenced in the text.** Fig. 1, Fig. 2, Fig. 7, Table 1,
    Table 2, Table 6 and Table 8 were previously never pointed to from the prose. Pointers were
    added at the natural places (§2.1 for Fig. 1, a new lead sentence in §2.3 for Table 1, §4 for
    Table 2 and Fig. 2, §5.3 for Table 6 and Fig. 7, the appendix for Table 8). No claim, number
    or result was added — only the pointers.
12. **§6.1 states the relative-vs-absolute distinction explicitly**: the >10× uncertainty in the
    expansion data moves the whole absolute stress scale, while the orientation modulation is a
    relative quantity and does not.

### Placeholders
13. **Placeholders standardised** to the two required forms:
    `[AUTHOR INPUT REQUIRED: author names, affiliations, ORCID iDs and corresponding author]` and
    `[PUBLIC REPOSITORY/DOI TO BE INSERTED]`.

---

## 3. Changes to the submission format

14. **LaTeX source generated** (`FINAL_REVISED_MANUSCRIPT.tex`): `elsarticle` with
    `bibliographystyle{elsarticle-num}`, front matter with title / author placeholder / abstract /
    `highlights` / `keyword`, 7 numbered sections + unnumbered Declarations + appendix, 3 numbered
    `equation` environments, 8 `figure` environments, 8 booktabs/tabularx tables, and
    `\eqref` / `\ref` / `\cite` instead of hard-coded numbers.
15. **Bibliography generated** from the Crossref-verified metadata (`REFERENCES_VERIFIED.json`):
    23 entries, 0 unparsed, every entry carrying author, title, journal, volume, number, pages,
    year and DOI. Nothing was typed by hand and nothing was invented.
16. **PDF regenerated** from the repaired manuscript and re-verified (`tools/verify_pdf.py`):
    16 pages, 8 figures, 3 equations, 174 units and 79 table rows present, 0 blocks outside the
    text column, 0 figures without a caption on the same page.

---

## 4. What was deliberately NOT changed

* every numerical result, table value, figure and uncertainty estimate;
* the physical model (plane-strain anisotropic thermoelasticity), the geometry, the boundary and
  initial conditions, and the material parameters;
* the verification suite verdicts, including the one reported failure (metric consistency on the
  hand-off-style 96×48 grid) and the one exploratory test;
* every limitation and every scope statement — none was deleted or softened;
* the relaxation times remain explicitly hypothetical;
* the classification of the study remains **verified, not validated**
  (`APPLICABLE — EVIDENCE_UNAVAILABLE`);
* the reference list content (only its format changed, from a numbered markdown list to BibTeX).

---

## 5. How to reproduce

```bash
cd /home/user/le
python3 PAPER_PROJECT/13_Manuscript/build_manuscript.py     # .md + .docx from the builders
python3 tools/refs_to_bib.py                                # FINAL_REVISED_REFERENCES.bib
python3 tools/md_to_tex.py                                  # FINAL_REVISED_MANUSCRIPT.tex
python3 tools/audit_tex.py                                  # 66 static checks (exit 0 = pass)
python3 tools/test_md_to_tex.py                             # 26 conversion unit tests
cd PAPER_PROJECT/13_Manuscript
python3 ../../tools/md_to_pdf.py -o FINAL_REVISED_MANUSCRIPT.pdf
python3 ../../tools/verify_pdf.py                           # 5 PDF checks (exit 0 = pass)
```
