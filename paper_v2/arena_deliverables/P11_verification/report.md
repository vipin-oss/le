# P11 — the eleven added PDFs: identity, equations read, verdict update

Date: 2026-11-02. Evidence only. No `.tex` file and no pipeline script was edited; no PDF was
copied into the repository; no folder identifier, sharing link or download link appears in this
folder or in `refs_P8.csv`.

Supersedes the two "SOURCE NOT AVAILABLE" halves of P10: the couple-stress half of **S1** and the
Liu 2000 attribution inside **S2** now rest on the papers themselves.

## 1. What arrived

Eleven PDFs were present in the library and all eleven are the papers recorded in
`refs_P8.csv`. Every one has a real text layer, so no page had to be read as an image and no page
was skipped. Identity was checked against the title page (authors, journal, volume, page range,
year) and, for the two Journal of Applied Physics items, against the article's own citation line.

| Key | Printed pages in the PDF | Title-page identity | Text layer |
|---|---|---|---|
| Toupin1962 | 385–414 (30 pp) | *Elastic Materials with Couple-stresses*, R. A. Toupin, Arch. Ration. Mech. Anal. 11 | yes |
| Toupin1964 | 85–112 (28 pp) | *Theories of Elasticity with Couple-stress*, R. A. Toupin, Arch. Ration. Mech. Anal. 17 | yes |
| Mindlin1964 | 51–78 (28 pp) | *Micro-structure in Linear Elasticity*, R. D. Mindlin, Arch. Ration. Mech. Anal. 16 | yes |
| GreenRivlin1964 | 113–147 (35 pp) | *Multipolar Continuum Mechanics*, A. E. Green & R. S. Rivlin, Arch. Ration. Mech. Anal. 17 | yes |
| Hutson1962 | 40–47 (9 pp incl. cover) | *Elastic Wave Propagation in Piezoelectric Semiconductors*, Hutson & White, J. Appl. Phys. 33, 40 (1962) | yes |
| White1962 | 2547–2554 (9 pp incl. cover) | *Amplification of Ultrasonic Waves in Piezoelectric Semiconductors*, D. L. White, J. Appl. Phys. 33, 2547 (1962) | yes |
| Liu2000 | 1734–1736 (4 pp incl. cover) | *Locally Resonant Sonic Materials*, Liu, Zhang, Mao, Zhu, Yang, Chan, Sheng, Science 289 | yes |
| Sigalas1992 | 377–382 (6 pp) | *Elastic and Acoustic Wave Band Structure*, Sigalas & Economou, J. Sound Vib. 158(2) | yes |
| Kushwaha1993 | 2022–2025 (4 pp) | *Acoustic Band Structure of Periodic Elastic Composites*, Kushwaha, Halevi, Dobrzynski, Djafari-Rouhani, Phys. Rev. Lett. 71(13) | yes |
| Hussein2014 | 040802-1…040802-38 (38 pp) | *Dynamics of Phononic Materials and Structures*, Hussein, Leamy, Ruzzene, Appl. Mech. Rev. 66 | yes |
| Zubko2013 | 387–421 (37 pp) | *Flexoelectric Effect in Solids*, Zubko, Catalan, Tagantsev, Annu. Rev. Mater. Res. 43 | yes |

Two scanning notes, both harmless: the JAP items carry the publisher cover page as p. 1 (page
numbers therefore run one ahead of the printed folio), and the last page of the White PDF is
p. 2554, where White's text ends and the first column of the next article in the same issue
begins. Nothing from that next article was used.

## 2. What was actually read, paper by paper

Quotes and page numbers in full are in `evidence_P11.csv` (42 rows, every quote checked to be a
verbatim substring of the cited page). Equation transcriptions there are marked "(normalized)":
the text layer renders many symbols as OCR debris, so those rows give the reading, not a
character-exact quotation.

### Toupin 1962 — couple-stress, and a classical thermal sector

- Energy function: eq. **(5.1)**, **p. 394** — the internal energy depends on the nine components
  of the deformation gradient, the eighteen independent components of its material gradient, and
  the entropy density.
- Constitutive relations: eqs. **(5.6)–(5.8)**, **p. 395** — symmetric stress, the couple-stress
  part `μ^(p(q)r)`, and temperature `θ = ∂ε/∂η` are all derivatives of that energy function.
- **Temperature does appear.** A heat equation is written as eq. **(5.4)**, **p. 394**, and the
  paper says it is taken "as in classical elasticity theory". A classical flux, no kernel.
- Internal length: eq. **(9.4)**, **p. 408** — a modulus `μ` of dimension stress and a second
  parameter "having the physical dimension of length".
- Dispersion: eqs. **(9.29)–(9.32)**, **p. 413**, with `K = lk`, plus Theorem 9.2 on the same page
  (the longitudinal speed is frequency-independent if and only if a coefficient vanishes). This is
  the wavenumber-dependent modulus the review's S1 refers to, in the paper itself.

### Toupin 1964 — grade-2 theory and the natural length

- Constitutive law: eq. **(12.8)**, **p. 107** — stress and hyperstress are the derivatives of
  `W` with respect to strain and to the second gradient.
- Internal length: eqs. **(14.1)–(14.4)**, **p. 109** — "a natural length" defined as
  `l² = |F|/|C|` from the moduli of the grade-2 energy.
- **No thermal sector:** the word "temperature" does not occur in the 28 pages. Isothermal.

### Mindlin 1964 — microstructure

- Potential energy: eq. **(2.5)**, **p. 55** — `W = W(e_ij, γ_ij, κ_ijk)`, forty-two variables.
- The length is the cell: eq. **(2.4)**, **p. 55** (edges `2d`), and the micro-inertia term in the
  kinetic energy carries `d²`.
- Constitutive equations: eqs. **(5.3)–(5.5)**, **p. 58**; isotropic quadratic energy with
  eighteen independent coefficients.
- **No thermal sector** (no occurrence of "temperature").

### Green–Rivlin 1964 — multipolar, with a thermal sector

- Entropy-production inequality: eq. **(8.3)**, **p. 124**; temperature `T`, entropy `S`, heat
  supply `r` and heat flux are all part of the framework.
- Heat flux has its own constitutive law: eqs. **(10.1)–(10.8)**, **p. 129**, with
  `q_K` depending on the temperature gradients; the conduction inequality (10.10) is on the same
  page. Classical conduction, no relaxation.
- Infinitesimal theory: eqs. **(15.9)–(15.10)**, **p. 138**, with the explicit footnote
  "the temperature T is constant" (or, alternatively, `S` constant).
- This is the one paper in the batch left at **R2**: the tensor equations are partly destroyed by
  the text layer, so only the scalar/statement-level equations above were read.

### Hutson & White 1962 — the coupled piezo-carrier problem

- Equations of state: eqs. **(II.2)–(II.3)**, **p. 41** — `T = cS − eE`, `D = eS + εE`.
- Field equations: Poisson **(II.5)**, continuity **(II.6)**, and a current with a drift term and
  a diffusion term, **(II.7)**, all **p. 41**; combined into **(II.10)**.
- Result: a complex, frequency-dependent elastic constant, eqs. **(II.15)–(II.18)**, **p. 42**,
  giving "dispersion and loss of the usual relaxation type with relaxation frequency" `ω_c = σ/ε`,
  plus the diffusion frequency `ω_D`.
- **No amplification and no gain:** neither word occurs in the nine pages. The review's split of
  the two 1962 papers is correct as written and must not be merged.
- **No heat flux:** "heat" does not occur; the two hits for "temperature" are the ambient
  laboratory condition.

### White 1962 — gain

- Abstract, **p. 2547**: "Amplification occurs when the drift velocity of the electrons exceeds
  the velocity of sound".
- Ratio `γ = 1 − μE₀/v_s` and the modified elastic constant, **(12)**, **p. 2548**; the
  conductivity frequency is "often called the dielectric relaxation frequency", same page.
- eq. **(16)**, **p. 2549**: `c' = c[1 + K²(γ + jω/ω_D)/(γ + j(ω_c/ω + ω/ω_D))]`, with the
  sentence that negative attenuation means a growing wave and that amplification needs
  `v_drift > v_sound`. Eqs. (17)–(18) are images in the text layer; only their statement is used.
- **No heat-flux law:** the "heat" hits are Joule heating and device power.

### Liu 2000 — locally resonant gap

- Structure, **p. 1734**: lead core, 2.5 mm silicone-rubber coating, epoxy matrix, simple cubic,
  lattice constant 1.55 cm; a 2 cm slab "break[s] the conventional mass-density law" at 400 Hz,
  with the lattice constant two orders below the wavelength.
- Numbers, **p. 1735**: dips at 380 and 1350 Hz; at 500 Hz the lattice constant is 300 times the
  longitudinal wavelength in epoxy. Eq. **(1)** (transmission coefficient) and eq. **(2)**
  (mass-density law) are on p. 1735.
- Effective modulus, **p. 1736**: `k_e` obtained by inverting Eq. (1); "close to the resonances the
  modulus actually turns negative", with 180° phase jumps at the zero crossings.
- **No effective-mass formula.** The phrase "effective mass" never occurs; the inverted quantity
  is an effective modulus and it has no equation number of its own. The paper also reports
  negative **elastic constants**, not a negative density.

### Sigalas 1992 — method and gap sizes

- Method, **p. 378**: Bloch's theorem plus a Fourier expansion of `λ`, `μ`, `ρ⁻¹`, truncated to a
  `3N × 3N` matrix eigenvalue problem (the scalar case gives `N × N`).
- Scalar (acoustic) result, **p. 378**: a first gap for volume fraction about 14 % and velocity
  contrast about 2 (fcc, bcc); lower fractions for sc at higher contrast.
- Full elastic result, **p. 380**: with `ρ_i/ρ_o = 1` and `x = 14.4 %`, "a rather narrow gap does
  appear. The ratio of the gap to mid-gap is about 5 %".

### Kushwaha 1993 — method and result

- Abstract, **p. 2022**: first full band-structure calculation for periodic elastic composites; a
  phononic gap "for transverse polarization of the vibrations ... throughout the Brillouin zone".
- Method, **p. 2024**: Bloch theorem with a plane-wave expansion, eqs. (3)–(6), square lattice,
  441 plane waves; Ni rods in Al (`f = 0.1`) and Al rods in Ni (`f = 0.75`).
- Caveat, **p. 2025**: "the gaps found are not 'complete' or independent of polarization",
  because the mixed longitudinal–transverse mode was not computed.

### Hussein 2014 — the taxonomy, and what it does not give

- §1.4.1 "Configurations of Locally Resonant Metamaterials", **p. 040802-5**: the Liu 2000 design;
  a gap "at a wavelength well below the regime corresponding to bandgap generation" by spatial
  periodicity, i.e. Bragg scattering.
- §1.4.2 "Effective Properties", **p. 040802-6**: monopolar resonance ↔ negative modulus, dipolar
  resonance ↔ negative density; effective properties are computed by unit-cell analysis or from
  reflection/transmission.
- §4.1.3, **p. 040802-11**: the condensed resonator, eqs. (22)–(24); eq. (23) contains the
  frequency-dependent term `k_R²/(k_R − ω²m_R)` that acts as the effective mass.
- **No closed-form effective-mass equation** and no symbol `m_eff` is defined anywhere in the
  38 pages.

### Zubko 2013 — flexoelectric constitutive law

- Coefficient, eq. **(1)**, **p. 390**: `μ_klij = (∂P_i/∂(∂u_kl/∂x_j))_{E=0}`, a fourth-rank
  flexoelectric tensor.
- Constitutive equations, eqs. **(7)–(9)**, **p. 391**: `P = χE + μ ∂u/∂x`,
  `σ = cu + (μ/χ) ∂P/∂x`, `μ ≡ χf`; one coefficient `f = f₁ − f₂` for direct and converse effect.
- Thermodynamic potential, eqs. (2)–(6), pp. 390–391.

## 3. Verdicts on the three sentences of the "Wider material classes" section

Sentence text is quoted from `s12b_wider.tex` as recorded in P10 §2.

### S1 — **PARTLY SUPPORTED** (was PARTLY with the couple-stress half unavailable)

> "These theories change the elastic operator, so they lie outside the kernel construction:
> `G(s)` is not modified, while the modulus acquires a wavenumber dependence."

- *"These theories change the elastic operator"* — **SUPPORTED, now R3 on primary sources**:
  Toupin 1962 eq. (5.1) p. 394 and eqs. (9.29)–(9.32) p. 413; Toupin 1964 eq. (12.8) p. 107;
  Mindlin 1964 eq. (2.5) p. 55; Green–Rivlin 1964 eq. (10.1) p. 129. With Mindlin 1965 from P9,
  all five cited papers are now equation-checked.
- *"the modulus acquires a wavenumber dependence"* — **SUPPORTED**: Toupin 1962 gives the
  dispersion relations explicitly, eqs. (9.31)–(9.32) p. 413, and proves when the longitudinal
  speed is *not* frequency dependent (Theorem 9.2, same page).
- *"`G(s)` is not modified"* — **PARTLY, and only as an absence argument**. None of the five
  papers multiplies a heat flux by a kernel. But two of them are not thermally empty:
  Toupin 1962 states a heat equation, eq. (5.4) p. 394; Green–Rivlin 1964 carries temperature,
  entropy, a heat-flux constitutive law with temperature gradients, eqs. (10.1)–(10.8) p. 129,
  and the conduction inequality (10.10), plus (15.9)–(15.10) p. 138. So the honest wording is
  "no relaxation kernel is present", not "there is no thermal sector".
  Toupin 1964 and Mindlin 1964 genuinely have no thermal field.
- The section's own hedge — "This statement follows from the structure of the models, not from a
  check of the cited papers" — is now partly obsolete: the operator and dispersion halves *were*
  checked. It can be narrowed to the `G(s)` clause only.

### S2 — **SUPPORTED** (was SUPPORTED with the Liu attribution unavailable)

> "A locally resonant array is commonly described by a frequency-dependent effective mass or
> modulus, which is formally of the same kind as `m(s)` ..."

- *Liu 2000 attribution* — **SUPPORTED at R3**: core/coating/matrix design and the 400 Hz
  subwavelength gap, p. 1734; a frequency-dependent effective modulus `k_e` that turns negative
  near resonance, p. 1736. That is exactly a frequency-dependent modulus of the `m(s)` kind.
- *"effective mass or modulus"* — the "modulus" word is the one Liu 2000 supports. Liu 2000 has
  **no effective-mass formula**; the effective-mass language in this literature comes from later
  work, and Hussein 2014 only carries it implicitly, eq. (23) p. 040802-11, without a symbol.
- *"commonly described"* — **SUPPORTED**: Hussein 2014 §1.4.2 p. 040802-6 (negative modulus from a
  monopolar resonance, negative density from a dipolar one); Oh et al. 2016 from P10.

### S3 — **PARTLY SUPPORTED** (was SUPPORTED via other classes; the piezo pair is now checked)

> "The relaxation kernel for the heat flux can still be inserted in each of them; the
> semiconductor coupling then adds its own relaxation times."

- *"Interaction of acoustic waves with carriers in piezoelectric semiconductors was described
  early [Hutson 1962]"* — **SUPPORTED at R3**: Hutson & White 1962, eqs. (II.2)–(II.3) and
  (II.5)–(II.10) p. 41, complex modulus and dispersion/loss, eqs. (II.15)–(II.18) p. 42.
- *"together with ultrasonic amplification [White 1962]"* — **SUPPORTED at R3**: gain criterion in
  the abstract p. 2547 and body p. 2549, `γ = 1 − μE₀/v_s` p. 2548, eq. (16) p. 2549. The
  attribution is exactly right: amplification is White's paper, not Hutson & White's.
- *"the semiconductor coupling then adds its own relaxation times"* — **SUPPORTED at R3**:
  the conductivity frequency `ω_c = σ/ε` ("often called the dielectric relaxation frequency",
  White p. 2548) and the diffusion frequency `ω_D` are the extra relaxation scales, and they enter
  the same complex-modulus form as a viscoelastic kernel would, Hutson eq. (II.15) p. 42.
- *"the relaxation kernel for the heat flux can still be inserted in each of them"* —
  **NOT DEMONSTRATED by the cited papers**: Hutson & White 1962 has no heat-flux field at all
  ("heat" 0 hits) and neither does White 1962 (the "heat" hits are Joule heating). Insertion is an
  inference from the fact that the thermal balance law is independent of the carrier equations —
  plausible, but it is not something these two papers show. The clause should stay flagged as
  structural, as P10 already flagged it.

## 4. Points where the review text must be careful

1. **Toupin 1962 is not thermally empty.** Any sentence of the form "the couple-stress papers
   contain no temperature" would be false: eq. (5.4) p. 394 is a heat equation and eq. (5.8)
   p. 395 makes temperature a constitutive output.
2. **Green–Rivlin 1964 has a thermal sector** — temperature, entropy, a heat-flux constitutive
   law with temperature gradients (10.8) p. 129 and the conduction inequality (10.10). It is
   classical conduction without relaxation, but it is not absent.
3. **Liu 2000 gives an effective modulus, not an effective mass.** Any later text that attributes
   a negative effective mass or an effective-mass formula to Liu 2000 would be wrong.
4. **Kushwaha 1993 does not claim a complete gap.** Its gaps hold "for transverse polarization"
   and the paper says so explicitly, p. 2025. Cite it for a polarization-specific gap.
5. **Do not merge Hutson 1962 and White 1962.** Hutson & White has no amplification statement at
   all; White is the amplification paper. The review currently gets this right.
6. **Sigalas 1992's numbers** (14 %, contrast ≈2, 5 % gap) come from OCR of a two-column letter;
   the values are consistent with the surrounding text but the glyphs are degraded, so quote the
   5 % figure from p. 380 and not the garbled threshold line.

## 5. Still missing or wrong

Nothing. 11 of 11 target PDFs were found, opened and confirmed to be the right papers; none was
scanned-only; `missing_P11.csv` therefore records zero outstanding items. No wrong paper was
used and no content was inferred from a title.

## 6. Bookkeeping

- `refs_P8.csv`: the eleven rows moved from `R0 / NOT FOUND` to **R3 × 10 and R2 × 1**
  (Green–Rivlin 1964), `pdf_status = READ` for all eleven, and the `notes` column now carries the
  equations and page numbers read in this phase.
- **Known state, deliberate:** `build_p8.py` (`PDF_STATUS`) and `refs_data.py` (`ver`, `note`) were
  *not* edited, because this phase is evidence-only. `refs_P8.csv` is therefore the source of
  truth for these eleven rows; anyone who re-runs the P8 builder must first set `READ` in its
  status map and `R3`/`R2` plus the new notes in the data module, or the builder will silently
  revert these cells.
- Verdicts and evidence are additive to P10: `P10_verification/verdicts_P10.md` carries a banner
  pointing here, and nothing in P10 was rewritten.
- One gate line had to be relaxed, and it is disclosed here: `P9_verification/check_p9.py` asserted
  the exact P9 snapshot of the P8 register ("1 x R3 and 71 x R0") and therefore failed as soon as
  P11 read ten more papers. It now asserts the substance — Mindlin1965 sits at R3 and carries its
  P9 note, and every level is in R0–R3 — instead of the snapshot. No other gate was touched, and
  no check was weakened: `check_p11.py` is stricter about these eleven rows than `check_p9.py`
  ever was.
- Gates at the end of this phase: `check_p8.py`, `check_p9.py`, `check_p10.py`, `check_p11.py`,
  `check_readme_paths.py --root .` — all PASS.
