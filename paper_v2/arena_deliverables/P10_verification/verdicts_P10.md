# P10 — the "Wider material classes" section, read from `review-paper-v2`; verdict update

Date: 2026-11-02. Evidence only: no `.tex` file was edited, on this branch or any other.

## 1. Where the section actually is

The section is **not** in this branch. It is in `review-paper-v2`, commit `acea1fd`
("Add wider material-class section … 72 P8 refs; 171 pp"), inside the package at
`paper_v2/overleaf_package.zip`:

```
sections/s12b_wider.tex      41 lines, 8.6 kB
\section{Wider material classes: where the template reaches and where it stops}\label{sec:wider}
```

Five subsections: couple-stress/strain-gradient/microstructured; phononic crystals and
metamaterials; piezoelectric and piezo-semiconductor; graded/porous/laminated/magnetoelectric/
nano/tissue; summary map with one table.

**Citation check of that file:** it cites **72 keys, all 72 of which resolve** in the package's
`refs*.bib` (434 entries in total). Nothing dangles. Two things worth noting:

- `s12b_wider.tex` does **not** cite `Gupta2026HeatMap`, although that entry exists in the
  package's `refs.bib`. The piezo-semiconductor paragraph rests on Hutson 1962, White 1962,
  Palma 1987 and later works.
- Neither Oh et al. 2016 nor Hobiny/Abbas/Marin 2022 is in the package bibliography at all
  (their DOIs `10.1038/srep23630` and `10.3390/math10010121` occur nowhere in `refs*.bib`).

## 2. The three sentences, verbatim from `s12b_wider.tex`

**S1** (end of §2.1, after the list of gradient and couple-stress work):

> "These theories change the elastic operator, so they lie outside the kernel construction:
> $G(s)$ is not modified, while the modulus acquires a wavenumber dependence. **This statement
> follows from the structure of the models, not from a check of the cited papers.**"

and the table row: "Couple-stress, strain gradient | elastic operator, internal length | outside
($G$ unchanged, $m$ depends on $k$)".

**S2** (end of §2.2):

> "A locally resonant array is commonly described by a frequency-dependent effective mass or
> modulus, which is formally of the same kind as $m(s)$ in Section~\ref{sec:modulus}; that is the
> point of contact."

**S3** (end of §2.3, and the table row):

> "The relaxation kernel for the heat flux can still be inserted in each of them; the
> semiconductor coupling then adds its own relaxation times."

Table row: "Piezoelectric semiconductors | carrier and potential fields | outside; heat-flux
kernel can still be inserted".

## 3. Verdicts

### S1 — **PARTLY SUPPORTED** (unchanged in substance, now judged against the real text)

- *"These theories change the elastic operator"* — **verified**, Mindlin 1965, R3:
  energy `w = W(ε, ∇ε, ∇∇ε)` eq. (1) **p. 418**; quadratic form eq. (19) **p. 421**; equilibrium
  `∇·(τ − ∇·μ + ∇∇:χ) + f = 0` eq. (17) **p. 421**; stress modified by the strain gradient
  eq. (20a) **p. 422**; internal length fixed by `l² = a/μ`, **p. 422**.
- *"`G(s)` is not modified"* — **not verifiable from the cited work**: Mindlin 1965 has no
  temperature field at all, so it can neither modify nor preserve a heat kernel. The exclusion is
  an absence argument.
- *Couple-stress half* — **SOURCE NOT AVAILABLE**. Toupin 1962 (`10.1007/BF00253945`), Toupin 1964
  (`10.1007/BF00253050`), Green–Rivlin 1964 (`10.1007/BF00253051`) and Mindlin 1964
  (`10.1007/BF00248490`) are still not in the library — re-searched on 2026-11-02 by author
  name, by DOI-derived filename and by full-text title match; no new uploads.
- **The section's own hedge is accurate and should stay.** "This statement follows from the
  structure of the models, not from a check of the cited papers" is exactly what the evidence
  shows; the sentence is safe *because* it is written that way. If the hedge is ever removed, the
  sentence becomes unsupported.

### S2 — **SUPPORTED** for the wording used, **SOURCE NOT AVAILABLE** for the Liu attribution

- *"commonly described by a frequency-dependent effective mass or modulus"* — **verified at R3**
  by Oh, Kwon, Lee & Kim 2016: effective mass `m_eff = m1 + m3 ω²/(ω_x² − ω²)`, eq. (4a)
  **p. 4**, negative just above the local resonance; combined cell eq. (10) **p. 5**;
  `ρ_eff = m_eff/(d h²)` **p. 5**; dispersion eq. (1) **p. 3**, impedance eq. (2) **p. 3**.
- *Attribution to Liu 2000* — **SOURCE NOT AVAILABLE**. Liu et al. 2000
  (`10.1126/science.289.5485.1734`) is not in the library, so the original formula and its page
  numbers remain unverified. The sentence as written does not claim Liu for the formula
  (it cites Liu 2000 only for "gaps at wavelengths far larger than the lattice period"), so it is
  not wrong — but if a reader takes the final clause as Liu's result, that is still unverified.
- *Recommendation*: add `Oh2016` (this folder's `refs_P10.bib`) to the sentence, or leave it
  uncited and rely on the hedge-free reading above. Note also that Oh et al. is an **elastic**
  metamaterial (S0 Lamb mode), not a sonic crystal — the claim "locally resonant array" is
  therefore directly on point.

### S3 — **SUPPORTED**, and now at R3 for the piezo-semiconductor case

- **Gupta et al. 2026, heat-flux equation extracted from the PDF — R2 → R3.** The law is
  eq. **(2.15), p. 6**, "Nonlocal memory dependent TPL heat transfer law":

  ```
  (1 − ξ²∇² + τ² ∂²/∂t²) (1 + (τ_q/1!) D_μ + (τ_q²/2!) D_μ²) q̇*_i
      = − K_ij (∂/∂t)(1 + τ_θ D_μ) T_,i  − ∫ (E_g Ṅ/τ*) dx_i  − K*_ij (1 + τ_v D_μ) T_,i
  ```

  with the memory operator `D_μ` defined by eq. (1.1) **p. 3** and its kernels by eq. (1.2)
  **p. 3**. Eliminating the flux gives the temperature equation eq. **(2.16), p. 6**, and the
  carrier equation is eq. **(2.17), p. 6**:
  `∂N/∂t = D_Eij N_,ij − N/τ* + κ T`. Supporting structure: nonlocal operator eq. (2.7) **p. 5**,
  Klein–Gordon constitutive law eq. (2.8) **p. 5**, stress/potential/entropy eqs. (2.9)–(2.11)
  **p. 5**.
- **Hobiny, Abbas & Marin 2022, R3**: carrier eq. (2) **p. 3**, heat conduction with the
  relaxation operator `(1 + τ₀ ∂/∂t)` eq. (3) **p. 3**, and the same operator after
  non-dimensionalisation eq. (8) **p. 3** — the kernel is inserted without disturbing the carrier
  equation. (No piezoelectric term in this paper.)
- So the sentence "the relaxation kernel for the heat flux can still be inserted" is now
  demonstrated at equation level on a full piezo-semiconductor model, not merely asserted.
- *Recommendation*: cite `Gupta2026HeatMap` (already in the package bibliography, currently
  uncited) in that paragraph, and `Hobiny2022` (new) for the semiconductor + relaxation-law
  combination. Do not attribute to Hutson 1962 or White 1962 anything about relaxation kernels:
  those two are still unread.

## 4. New PDFs for step 3 of the task

**None arrived.** The eleven sources of `missing_pdfs_P9.csv` were searched again on 2026-11-02
(author-name filenames, DOI-derived filenames, and full-text title search) and are still absent:
Toupin 1962, Toupin 1964, Mindlin 1964, Green–Rivlin 1964, Hutson 1962, White 1962, Liu 2000,
Hussein 2014, Sigalas 1992, Kushwaha 1993, Zubko 2013. Their verdicts stay
**SOURCE NOT AVAILABLE** and nothing has been inferred about their contents.

## 5. Summary

| Item | Before P10 | After P10 |
|---|---|---|
| S1 operator change | R3 (Mindlin) | R3 (Mindlin), unchanged |
| S1 "`G` unchanged" | absence argument | absence argument; section's own hedge confirmed accurate |
| S1 couple-stress half | SOURCE NOT AVAILABLE | SOURCE NOT AVAILABLE (re-searched) |
| S2 effective mass | R3 (Oh 2016) | R3 (Oh 2016), now quoting the exact sentence |
| S2 Liu attribution | SOURCE NOT AVAILABLE | SOURCE NOT AVAILABLE (re-searched) |
| S3 kernel in piezo-semiconductor | R2 (Gupta 2026) | **R3 — eq. (2.15)/(2.16)/(2.17), p. 6** |
| Section located / citation integrity | not checked | found in `review-paper-v2` @ `acea1fd`; 72/72 cites resolve |

## Files in this folder

- `refs_P10.bib` — Oh 2016 and Hobiny 2022 as active entries, Gupta 2026 as a commented entry
  (already present in the package as `Gupta2026HeatMap`; duplicating the key would break the
  build). All three verified from the PDF title pages.
- `evidence_P10.csv` — the three sources with level, pages, equations and the sentence each
  supports.
- `check_p10.py` — gate; prints `PASS` and exits 0.
