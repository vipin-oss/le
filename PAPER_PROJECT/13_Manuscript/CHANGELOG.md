# CHANGELOG — BFS-FEM3 restructure and calculation companion

**Paper:** *Orientation-dependent wall stress around circular and elliptical cavities in monoclinic
β-Ga₂O₃ under a transient thermal pulse: a verified continuum study with thermal-memory and
mechanism ablations*
**Target journal:** International Journal of Heat and Mass Transfer (Elsevier, `elsarticle`)
**Branch:** `arena/01a0f67f-le` · **Dates:** 2026-10-01 (readiness pass, §1 ff. below) and
2026-10-02 (this restructure, §0)

> The entries below §0 record the 2026-10-01 publication-readiness pass. Their section numbers
> (`§2.1`, `§5.4`, `Table 7`, …) are the numbers of **that** version; the current numbering is
> given in §0. Nothing in either pass changes a number, a result, the physical model, the
> geometry, the boundary or initial conditions, the material parameters, or a limitation.

---

## 0. Restructure to the requested format, and the calculation companion (2026-10-02)

### 0.1 What the format asked for, and what was delivered

| Requested (BFS-FEM3 reference: 9 sections / 36 subsections / 93 equations / 8 figures / 5 tables / 54 references) | Delivered |
|---|---|
| ~9 sections | **9 sections**, 41 subsections |
| displayed equations throughout | **84** numbered equations (was 3) |
| 8 figures | **8** figures (unchanged) |
| tables | **11** tables (was 8) |
| ~54 references | **54** Crossref-verified references, all cited |
| ~15 printed pages | 32-page single-column preprint (≈ 15–18 pp two-column) |
| **a separate calculation file** | **`FINAL_REVISED_CALCULATIONS.tex`** — 11 sections, 37 subsections, 29 equations, 9 tables, ~4.9k words |

### 0.2 Section structure

| § | Title | § | Title |
|---|---|---|---|
| 1 | Introduction (1.1–1.4) | 6 | Results (6.1–6.5) |
| 2 | Governing equations and constitutive framework (2.1–2.9) | 7 | Discussion and limitations (7.1–7.3) |
| 3 | Analytical results (3.1–3.5) | 8 | Conclusions |
| 4 | Numerical method (4.1–4.8) | 9 | Code, data and reproducibility (9.1–9.3) |
| 5 | Verification and numerical uncertainty (5.1–5.4) | A | Nomenclature |

Sections 2–4 were expanded into their constituent steps (plane-strain reduction, crystal
rotation, conduction kernels, boundary and initial conditions, dimensionless groups, material
parameters, quantities of interest, grid, operators, boundary treatment, frequency-domain system,
Bromwich inversion, QoI definitions, numerical uncertainty); §5–§7 were renumbered; §9 is new.

### 0.3 The calculation companion

`FINAL_REVISED_CALCULATIONS.tex` (built by `build_calculations.py` → `calculations_IJHMT.md`) is
the worked arithmetic behind the manuscript. It computes every number **live** from the frozen
source (`PAPER_PROJECT/06_Source_Code/src/`) or reads it from
`PAPER_PROJECT/10_Processed_Data/ANALYSIS_V2.json`: term-by-term construction of β, the rotation
worked at φ = 30°, the closed-form circular cavity, the three dimensionless groups, the
grid metrics and contravariant coefficients, the Bromwich contour arithmetic (K, alias error,
round-off growth), the peak-extraction and modulation formulae, a step-by-step Richardson
extrapolation, the ablation arithmetic, and the reproduction commands. It runs no simulation and
adds no result. It carries the same declarations (author placeholder, competing interest, funding,
data availability, generative-AI statement) and the same limitation statements as the manuscript.

### 0.4 What was *not* changed

No number, result, parameter, figure, limitation or label was altered: not the peak stresses, the
modulation amplitudes, the memory deviations, the verification results, the >10× expansion
uncertainty, the hypothetical status of the relaxation time, the α₅ = 0 limitation, the
APPLICABLE — EVIDENCE_UNAVAILABLE physical-validation label, or the Fourier + Lord–Shulman
primary / two-relaxation-time exploratory split. No simulation was run for this pass.

One provenance item is new. The two code-freeze manifests were taken on 2026-10-01, and six of
the fifteen files they cover have been edited since (portability and reporting edits), so their
recorded digests no longer describe the code; the seven solver modules and the two convergence
drivers are still byte-identical. Section 9.1 of the manuscript and Section 11 of the companion
now say so, cite the end-to-end re-run that reproduces the archived results exactly
(`15_Audits/RERUN_COMPARISON.md`), and point at the refreshed manifest
`CODE_FREEZE_submission_2026_10_02.json` (27 files) as the one to deposit. No result was
recomputed for this: the re-run predates the restructure and is unchanged by it.

### 0.5 Tooling

| Tool | Change |
|---|---|
| `build_manuscript.py` | rebuilt: one central section map (`SEC_MAP`) numbers every heading and aborts on an unmapped one; `@@eq:/@@tab:/@@fig:` placeholders are resolved by order of appearance and fail loudly if unresolved |
| `build_calculations.py` (new) | builds the companion document from the frozen source and the data package |
| `tools/md_to_tex.py` | multi-digit `Eq. (n)` → `\eqref`; new `--companion` preamble; portable `\Vert`, prime and file-path handling; ASCII-only output |
| `tools/audit_tex.py` | 70 static checks on the manuscript `.tex`, 54 on the companion (`-c`); counts follow the expanded manuscript instead of being hard-coded |
| `tools/verify_pdf.py` | companion mode; generalised composite-glyph tolerance |
| `tools/check_crossrefs.py` (new) | validates every “Section x.y”, “Table n”, “Fig. n”, “Eq. (n)” against the built manuscript |
| `tools/renumber_crossrefs.py` | retired from a one-off migration to an idempotent guard |
| `tools/check_tex_commands.py` (new) | every `\\command` in the two `.tex` files must be provided by LaTeX, `elsarticle` or a loaded package; also catches a spacing command glued to the text after it (the `\\qquadc_k` class of error) |
| `.gitignore` | `13_Manuscript/equations/` (regenerated mathtext images) no longer tracked |
| `00_Project_Control/make_packages.py` | the submission package now also ships the `.tex`, `.bib` and `.pdf` deliverables |
| `06_Source_Code/make_code_freeze.py` | the frozen-file list now also covers the three manuscript scripts added by the restructure (`ms_derivation.py`, `ms_numerics.py`, `build_calculations.py`), so the manifest describes everything that generates the submission text |

### 0.6 Deliverables as they now stand

| File | What it is | Size |
|---|---|---|
| `FINAL_REVISED_MANUSCRIPT.tex` | elsarticle source, 9 sections / 41 subsections / 84 equations / 8 figures / 11 tables | 101,960 B |
| `FINAL_REVISED_REFERENCES.bib` | 54 BibTeX entries, all Crossref-verified, 0 unparsed | 20,377 B |
| `FINAL_REVISED_MANUSCRIPT.pdf` | 33-page preprint PDF (byte size varies: PDF metadata carries a timestamp) | ≈ 2.4 MB |
| `FINAL_REVISED_CALCULATIONS.tex` | companion calculation document | 48,209 B |
| `FINAL_REVISED_CALCULATIONS.pdf` | 13-page PDF of the companion | ≈ 0.6 MB |
| `manuscript_IJHMT.md` / `.docx` | single source of truth and its Office rendering | 98,956 B / 2,685,645 B |
| `MANUSCRIPT_STATS.json` | structure counts and editorial limits | — |
| `06_Source_Code/CODE_FREEZE_submission_2026_10_02.json` | refreshed code freeze: SHA-256 of the 27 solver, driver and manuscript scripts as submitted | 3,047 B |
| `15_Audits/RERUN_COMPARISON.md` | end-to-end re-run of the pipeline with the current code against the delivered results | — |

---


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
