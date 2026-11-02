# P9 — verification of three sentences of the planned section "Wider material classes"

Date: 2026-11-02. Evidence only: no `.tex` file and no pipeline script was touched.

## What was asked

Read the 35 PDFs listed in `pdfs_needed_P8.csv`, priority on twelve of them
(Toupin1962, Toupin1964, Mindlin1964, Mindlin1965, GreenRivlin1964, Hutson1962, White1962,
Hussein2014, Liu2000, Sigalas1992, Kushwaha1993, Zubko2013), verify abstract + energy/dispersion
equations with equation numbers and pages, then judge three sentences:

- **S1** — strain-gradient / couple-stress elasticity change the elastic operator, the heat-flux
  kernel `G(s)` is unchanged.
- **S2** — locally resonant arrays are described by a frequency-dependent effective mass
  (or modulus).
- **S3** — the heat-flux kernel can still be inserted in piezo-semiconductor models.

## Two facts that shape this report

1. **There is no section called "Wider material classes" in the repository.** A search of every
   text file (`grep -r "material classes"`, `grep -r "Wider"`, both zero hits) finds no such
   heading, in `paper_v2/manuscript_v2`, in `P7_language`, or anywhere else. The three sentences
   are therefore checked **as supplied in the task**, not against repository text; if the section
   is being drafted elsewhere, its final wording has not been seen here.
2. **Eleven of the twelve priority PDFs are not in the library.** The library was searched four
   ways: author-name filename match, DOI-derived filename match (the scans of Springer articles
   are stored under their DOI suffixes, e.g. `10.1007@bf01302942.pdf`), the inventory index, and
   full-text search. Only **Mindlin 1965** was found and read. The missing eleven are listed with
   DOIs in `missing_pdfs_P9.csv`. Nothing about them is inferred from other papers.

Four library PDFs were read for the sentences themselves, two of which are not in `refs_P8`
(they are marked as such and were *not* added to the bibliography).

## Sources actually read

| Key / short cite | Venue | Level | Pages read | Equations checked |
|---|---|---|---|---|
| Mindlin 1965 | Int. J. Solids Struct. **1**:417–438 | **R3** | 417–425 | (1) p. 418; (17) p. 421; (19) p. 421; (20a) p. 422; (35), (37) pp. 424–425 |
| Mindlin & Eshel 1968 (library, not in `refs_P8`) | Int. J. Solids Struct. **4**:109–124 | R1 | 109 (abstract) | none — abstract only |
| Oh, Kwon, Lee & Kim 2016 (library, not in `refs_P8`) | Sci. Rep. **6**:23630 | **R3** | 1–5 | (1) p. 3; (2) p. 3; (4a,b) p. 4; (10) p. 5 |
| Hobiny, Abbas & Marin 2022 (library, not in `refs_P8`) | Mathematics **10**:121 | **R3** | 1–6 | (1)–(5) p. 3; (8) p. 3 |
| Gupta, Hussain, Yaylacı & Das 2026 (library, not in `refs_P8`) | Contin. Mech. Thermodyn. **38**:41 | R2 | 1–4, 9, 13–14 | (1.1), (1.2) p. 3; (2.1) p. 4 |

Levels: R0 = metadata only, R1 = abstract read, R2 = text read but not all pages / not all
equations extracted, R3 = the equations were checked and their numbers and pages recorded.
All page numbers are the **journal page numbers printed in the article**, not PDF page indices.

---

## S1 — "strain-gradient / couple-stress change the elastic operator, `G` unchanged"

**Verdict: PARTLY SUPPORTED.**

*What is supported, with equations.* Mindlin 1965 takes the potential energy density to be a
function of the strain, its first and second gradients — **eq. (1), p. 418**:
`w = W(ε, ∇ε, ∇∇ε)`. The full quadratic form, with the two Lamé constants and the additional
constants `a1…a5`, `b1…b7`, `c1…c3`, is **eq. (19), p. 421** (the equation sits at the foot of
p. 421 in the scan). The higher-order stresses enter the equilibrium equation as
`∇·(τ − ∇·μ + ∇∇:χ) + f = 0`, **eq. (17), p. 421**, with the traction conditions (18a–c); the
stress itself is modified by the strain gradient in **eq. (20a), p. 422**:
`τ_pq = λδ_pq ε_ii + 2μ ε_pq + c1 ε_iij,j δ_pq + c2 ε_pqii + ½c3(ε_iipq + ε_iiqp)`.
So yes, the **elastic operator is changed**: a fourth-order term appears and the stress is no
longer a function of the strain alone.

*The internal length.* p. 422 fixes it explicitly: "suppose that `l²` is the ratio of one of the
constants `a_n` to `μ`; i.e. `l` is a material property with the dimension of length", together
with the order-of-magnitude assumptions `|∇u| ≪ 1`, `|l∇∇u| ≪ 1`, `l²|∇∇∇u| ≪ 1`. This is the
sentence a size-dependent section needs, and it is now verified at R3.

*What is not supported.* Mindlin 1965 contains **no temperature field at all** — not in the
energy (19), not in the stress (20a), not in the equilibrium equation (17). It therefore cannot
show that the heat-flux kernel `G(s)` is unchanged; it only shows that the mechanical theory is
built without one. "`G` unchanged" is an *absence* argument: nothing in the elastic enrichment
touches the heat law because the theory has no heat law. That is a defensible statement, but it
must be phrased that way, and it is not an equation-level verification.

*Couple-stress specifically.* Toupin 1962, Toupin 1964 and Green–Rivlin 1964 — the three papers
that would carry this half of the sentence — are **not available** (see
`missing_pdfs_P9.csv`). The only support at hand is Mindlin's own introduction, p. 417, which
describes Toupin's couple-stress theory as the case in which the energy depends on the
rotation-gradient, i.e. eight of the eighteen strain-gradient components. That is a secondary
statement about Toupin, not a reading of Toupin. Mindlin & Eshel 1968, p. 109 (abstract, R1)
confirms that three forms of the first strain-gradient theory exist and that the stresses and
boundary conditions differ between them — consistent with "the elastic operator changes", again
not an equation-level check of couple stress.

*Honest limitation.* The sentence as written cannot be upgraded to SUPPORTED on this evidence:
the first clause is verified at R3 for strain gradient, the second is an absence argument, and
the couple-stress clause has no primary source in the library.

---

## S2 — "locally resonant arrays are described by a frequency-dependent effective mass / modulus"

**Verdict: SUPPORTED (by a library source that is not in `refs_P8`).**

*Evidence with equations.* Oh, Kwon, Lee & Kim, *Sci. Rep.* **6**:23630 (2016), "Elastic
metamaterials for independent realization of negativity in density and stiffness":

- **eq. (1), p. 3** — dispersion of the periodic mass–spring chain,
  `-m^eff_x ω² = α^eff_x (e^{ikd} + e^{-ikd} − 2)`;
- **eq. (2), p. 3** — the characteristic impedance `Z = i α^eff_x (1 − e^{ikd})/(ωh)`, which is
  what makes the effective parameters identifiable rather than merely fitted;
- **eq. (4a), p. 4** — the effective mass of the resonating cell,
  `m^eff_x = m1 + m3 ω²/(ω_x² − ω²)` with `ω_x = √(δ/m3)`: frequency dependent, and **negative**
  just above the local resonance `ω_x`;
- **eq. (10), p. 5** — effective mass and stiffness of the combined cell, `ω_x` and `ω_y`
  independently tunable;
- **p. 5** — the passage to continuum properties, `ρ^eff_x = m^eff_x/(d h²)`,
  `C^eff_x = α^eff_x/h`.

That is exactly the content of S2: a locally resonant array is represented by an effective mass
(equivalently a modulus) that depends on frequency and changes sign near the resonance.

*Caveat that matters.* S2's natural citations are Liu et al. 2000, Sigalas–Economou 1992,
Kushwaha 1993 and the Hussein 2014 review — **none of them is in the library**, so the specific
formula and page that Liu et al. print have **not** been verified. If the sentence is to be
attached to Liu 2000 specifically, it stays unverified until that PDF is supplied; if it is
attached to the general statement, Oh et al. 2016 carries it at R3. Note also the sign of the
claim: negative effective mass is a *consequence* of local resonance, not a definition, and
eq. (4a) above shows where the sign change comes from.

---

## S3 — "the heat-flux kernel can still be inserted in piezo-semiconductor models"

**Verdict: SUPPORTED, with the equation-level check on the non-piezoelectric semiconductor case.**

*Semiconductor + relaxation kernel, equations checked.* Hobiny, Abbas & Marin, *Mathematics*
**10**:121 (2022):

- **eq. (1), p. 3** — motion with carrier and thermal coupling,
  `μu_i,jj + (μ+λ)u_j,ij − γ_n N_,i − γ_t T_,i = ρ ü_i`;
- **eq. (2), p. 3** — the carrier equation,
  `D_e N_,jj − N/τ + (k/τ) T = ∂N/∂t`, i.e. a diffusive branch that sits **beside** the thermal one;
- **eq. (3), p. 3** — the heat conduction equation carrying the relaxation operator,
  `K φ_,jj + (E_g/τ) N = (1 + τ₀ ∂/∂t)(ρ c_e ∂T/∂t + γ_t T₀ ∂u_j,j/∂t)`;
- **eq. (8), p. 3** — the same law after non-dimensionalisation, the operator `(1 + τ₀ ∂/∂t)`
  intact.

So the kernel is inserted without disturbing the carrier equation: the two fields keep their own
characters (parabolic carrier, relaxed thermal). This paper has **no** piezoelectric term.

*Piezo-semiconductor + kernel, text level.* Gupta, Hussain, Yaylacı & Das, *Contin. Mech.
Thermodyn.* **38**:41 (2026), title: "Heat map analysis of wave dynamics in nonlocal Kelvin–Voigt
piezo-semiconductors under memory-dependent heat flux". The abstract states that the governing
equations "combine a Klein–Gordon type nonlocal operator with three-phase-lag heat conduction,
semiconductor transport, and piezoelectric coupling"; **eq. (1.1), p. 3** defines the
memory-dependent operator with kernel `K(t − ζ)` over the sliding interval `[t − μ, t]`, and
**eq. (1.2), p. 3** lists three admissible kernels. The paper refers to its field equations as
(3.1)–(3.5) and compares five heat-conduction models (Biot, LS, DPL, TPL, TPL-WV) on the same
piezo-semiconductor fields, pp. 13–14. That is a piezo-semiconductor model with the kernel in it.
Level **R2**: the explicit heat-flux equation itself (sections 2–3) fell in a part of the text
that could not be extracted, so its equation number is *not* recorded and must not be quoted.

*Honest limitation.* The piezo case is R2, the equation-level (R3) case is the photothermal
semiconductor without piezoelectric coupling. If the sentence must be backed by one source at
R3, the Gupta et al. PDF has to be read in full.

---

## Summary table

| Sentence | Verdict | Strongest evidence | Level |
|---|---|---|---|
| S1 elastic operator changes | supported | Mindlin 1965, eqs. (1), (17), (19), (20a), pp. 418–422 | R3 |
| S1 kernel `G(s)` unchanged | **not demonstrated** (absence argument) | Mindlin 1965 has no thermal field | — |
| S1 couple-stress clause | **SOURCE NOT AVAILABLE** | Toupin 1962/1964, Green–Rivlin 1964 missing from the library | — |
| **S1 overall** | **PARTLY SUPPORTED** | | |
| S2 effective mass depends on frequency | supported | Oh et al. 2016, eqs. (1), (4a), (10), pp. 3–5 | R3 |
| S2 attributed to Liu 2000 / Hussein 2014 | **SOURCE NOT AVAILABLE** | four P8 sources missing from the library | — |
| **S2 overall** | **SUPPORTED** (different source) | | |
| S3 kernel + carriers | supported | Hobiny et al. 2022, eqs. (2), (3), p. 3 | R3 |
| S3 kernel + *piezo*-semiconductor | supported at text level | Gupta et al. 2026, eq. (1.1), p. 3 | R2 |
| **S3 overall** | **SUPPORTED** | | |

## Consequences for the text (not applied — no `.tex` edited)

1. S1 should be split into two sentences: the equation-level statement about the elastic operator
   (safe, R3), and the statement that the heat law is untouched (must be phrased as a
   structural remark, or supported by a gradient-thermoelasticity paper that does not exist in
   the library yet).
2. S2 is safe but its citation should be the source that was actually verified (Oh et al. 2016)
   or Liu 2000 once supplied. Do not attribute the formula to a paper that has not been opened.
3. S3 is safe; if the piezo attribution matters, read Gupta et al. 2026 in full first, otherwise
   cite the semiconductor paper for the kernel and the piezo paper for the coupling, separately.

## Files

- `evidence_P9.csv` — every verified item: citation, DOI, pages read, equations with numbers and
  pages, which sentence it bears on, level.
- `missing_pdfs_P9.csv` — the eleven priority PDFs that are not in the library, with DOIs.
- `check_p9.py` — gate for this folder; prints `PASS` and exits 0.
- `refs_P8.csv` (in `../P8_coverage/`) — the `verification` column now reads **R3** for
  Mindlin1965 and **R0** for the other 71, and a new `pdf_status` column records
  READ / NOT FOUND / NOT CHECKED.
