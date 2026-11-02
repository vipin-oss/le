# P8 coverage extension — what to add, per area

Evidence-only document. Nothing here is applied to `s*.tex`; each block is a plan for a
future edit, with the references that would carry it (`refs_P8.bib`), the equations that would
have to be stated, how the addition attaches to the review's template kernel `G(s)` and
effective modulus `m(s)`, whether it sits inside or outside that template, and one honest
limitation per area.

**Verification status of everything below: R0.** All 72 references were matched to a Crossref
record (title, venue, volume, pages, DOI) on 2026-11-02. No abstract was read, no full text was
read, and **no equation number is verified**. Where an equation number would be cited in a
future draft, it is marked `[eq. no. NOT VERIFIED]` and must be filled from the PDF before the
sentence is written. Reference-level statements are therefore statements about *what a paper is
about*, taken from its title and venue, not about what its equations say.

Template vocabulary used throughout: the review writes every non-Fourier heat law as a
relaxation kernel `G(s)` multiplying the Fourier flux in the Laplace/frequency domain, and it
writes every elastic enrichment as an effective modulus `m(s)` (or `m(ω)`); thermoelastic
damping follows from putting the two together. An addition is *inside* the template when it
enters through `G(s)` or through a frequency-dependent `m`, and *outside* when it changes the
elastic operator itself, the field list, or the geometry in a way the kernel cannot absorb.

---

## Area (a) — Strain-gradient, couple-stress, dipolar and gradient-thermoelastic continua

Current coverage in the rewritten text: `Toupin` 0 mentions, `Mindlin` 9 (almost all in
"Mindlin–Tiersten"), `couple-stress` 12, `strain gradient` 6, `gradient elasticity` 10. The
concepts are present as vocabulary in §24 (`s12_size`) but there is no section that states a
gradient elastic energy and connects it to the dispersion relation.

### What to add (proposed: a subsection in `s12_size`, before "other enrichments")

1. **One paragraph on the second-grade (strain-gradient) energy.** State
   `W = ½ ε:C:ε + ½ ∇ε ⋮ D ⋮ ∇ε` with a single internal length `ℓ`, defined by `ℓ² = D/C`
   (ratio of the higher-order to the ordinary modulus). This is the Toupin–Mindlin form; the
   energy itself is in Toupin 1964 and Mindlin 1965 `[eq. no. NOT VERIFIED]`.
2. **One paragraph on couple stress.** Same energy plus an independent rotation field
   (Toupin 1962; Green–Rivlin 1964 as the modern statement), with the length `l` appearing in
   the ratio of the couple modulus to the shear modulus. State explicitly that couple-stress
   and strain-gradient theories give the *same* leading correction to the long-wave speed and
   differ at the next order — this is the sentence the review does not currently have.
3. **The dispersion consequence, in the review's own variables.** Show that to `O(ℓ²k²)` both
   theories replace the elastic stiffness by an effective modulus
   `m_ℓ(k) = ρc₁²(1 + ℓ²k²)` (a *stiffening*, opposite in sign to the Eringen nonlocal
   softening already in §24). Then the thermal branch of the dispersion polynomial is
   untouched: the kernel `G(s)` still enters multiplicatively, and the elastic branch merely
   gains `ℓ²k²`. The observable statement is that thermoelastic damping acquires an `O(ℓ²k²)`
   correction while retaining its Debye shape.
4. **One paragraph on dipolar/micropolar thermoelasticity** (Mindlin's dipolar theory;
   Eringen's micropolar with a temperature field): the extra balance law for the couple stress
   adds one more branch, so the same `G(s)` now multiplies a 2×2 elastic block.
5. **Gradient thermoelasticity.** Say that placing the gradient in the *heat* side instead
   (a gradient-dependent internal energy) produces a `G(s)` of the Guyer–Krumhansl type, i.e. it
   is already covered — this is the honest way to keep the section from claiming novelty.

### Inside / outside the template

| Theory | Status | Why |
|---|---|---|
| Strain-gradient / couple-stress elasticity | **outside** | changes the elastic operator; `G(s)` unchanged, `m` becomes `m(k)` |
| Mindlin dipolar, Eringen micropolar | **outside** | extra balance law, larger elastic block |
| Gradient-dependent free energy on the heat side | **inside** | reproduces a Guyer–Krumhansl-type kernel |
| Second-sound / GK already in text | inside | reference point |

### Where it lands
`s12_size` (main), one sentence each in `s16c_taxonomy` (new row: "higher-grade elasticity")
and `s17_open` (parameter values for `ℓ` are material-specific and unsettled).

### Honest limitation
Every `ℓ` quoted in this literature is fitted, not measured independently: a strain-gradient
fit and a surface-energy fit can reproduce the same size effect, so the review must not present
`ℓ` as a physical property without saying which experiment fixed it.

---

## Area (b) — Phononic crystals, elastic/acoustic metamaterials, thermal metamaterials

Current coverage in the rewritten text: `metamaterial` **0**, `phononic` **0**, `band gap`
**0**, `locally resonant` 0. This is the largest single gap in the paper.

### What to add (proposed: a new short section after `s13b_bg`, cross-referenced from `s16c_taxonomy`)

1. **Two mechanisms, one paragraph each.** Bragg scattering (periodicity `a`, gap near
   `ω ≈ c/a`; Sigalas–Economou 1992, Kushwaha 1993) versus local resonance (Liu et al. 2000,
   a heavy core in a soft shell, gap far below the Bragg scale, set by an internal resonance
   `ω₀ = √(k_eff/m_eff)`).
2. **The effective-medium statement that connects to the review's `m(s)`.** A locally resonant
   array is described by a frequency-dependent effective mass
   `ρ_eff(ω) = ρ [1 − ω₀²/ω²]^{-1}` (or the analogous `m_eff`), which is *negative* between
   `ω₀` and the gap edge. This is formally the same object as the review's effective modulus
   `m(s)`: it is analytic in `s` away from the resonance and is the natural place to say that
   the paper's `m(s)` machinery covers metamaterial dispersion without new formalism
   `[eq. no. NOT VERIFIED — see Hussein 2014 review]`.
3. **Thermoelastic damping inside a metamaterial.** One paragraph: each resonator is a Zener
   beam in its own right, so the damping peak sits at the resonator's `ω₀` and the *band gap*
   can hide or expose that peak. This is the point no review currently makes and is the
   review's plausible novelty here — but it must be phrased as a question, because no
   reference found supports it directly.
4. **Thermal metamaterials.** Transformation thermodynamics / thermal cloaking (Li et al. 2021,
   *Nat. Rev. Mater.* **6**:488–507 — note: **not** a 2012 *Nature Materials* paper, a citation
   trap). State that these are steady or Fourier-transient designs: the effective conductivity
   is real and `G(s) = 1`, so the review's finite-speed criterion marks the boundary of that
   whole literature. This is a strong, honest framing sentence.
5. **Thermally driven metamaterials / thermal wave crystals** (second-sound in periodic
   structures): the periodic version of the GK kernel; mark as open.

### Inside / outside the template

| Item | Status | Why |
|---|---|---|
| Bragg / local-resonance band structure | **outside** | new geometry; needs Bloch analysis, not a kernel |
| `ρ_eff(ω)`, `m_eff(ω)` of a resonant array | **inside** | same analytic-in-`s` object as `m(s)` |
| Transformation thermodynamics / cloaking | **inside, degenerate** | `G(s)=1`; finite-speed criterion is violated by construction |
| TED of a single resonator | **inside** | ordinary Zener applied to the element |
| TED *of the array* including band structure | **outside / open** | no published treatment found |

### Where it lands
New section (call it `s13c_metamaterials` in a future draft) + one row in `s16c_taxonomy` +
two items in `s17_open` (band-gap–damping interaction; second-sound in periodic media).

### Honest limitation
No band structure is reproduced here and no gap width or frequency is quoted: the four
review references (Hussein 2014; Ma–Sheng 2016; Cummer 2016; Vasileiadis 2021) are R0, so the
proposed text must be written from them only after reading, or written without numbers.

---

## Area (c) — Piezoelectric and piezo-semiconductor waves: carriers, acoustoelectric effect, quasicrystals

Current coverage: `piezoelectric` 88 mentions, `semiconductor` 26, `flexoelectric` 11, but
`quasicrystal` **0** and no statement of the carrier–wave coupling beyond a name-check in
`s13_multiphysics`.

### What to add (proposed: extend `s13_multiphysics`'s "coupling to further fields" subsection)

1. **The field list, stated once.** Elastic displacement + electric potential + carrier density
   `ñ`. The carrier equation is drift–diffusion (continuity + Poisson), so the linearised system
   has a *diffusive* branch with diffusivity `D_n`, in addition to the elastic and thermal
   branches. Cite Hutson–White 1962 and White 1962 for the acoustoelectric coupling
   `[eq. no. NOT VERIFIED]`.
2. **The acoustoelectric effect as a gain/loss condition.** When the carrier drift velocity
   exceeds the sound speed, the wave gains energy; below it, it loses. State this as a
   threshold condition, not as a number.
3. **The link to the template — the sentence worth writing.** The carrier branch is
   mathematically the *Fourier* limit of the review's kernel: `G(s) → 1` with a diffusive pole.
   Hence the paper's finite-front argument applies to the thermal field but **not** to the
   carrier field; a piezo-semiconductor wave therefore has one hyperbolic-ish and one
   parabolic field at the same time. This is a clean, defensible generalisation and it costs
   two sentences.
4. **Photo-thermo-elastic / plasma coupling.** One paragraph: illumination creates carriers,
   carriers heat the lattice, the lattice strains — a three-field chain in which the thermal
   kernel of the review appears in the middle. Cite the plasma-wave papers at R0 only.
5. **Flexoelectric semiconductors.** One paragraph: strain gradients (Area a) produce
   polarisation without a centre of symmetry, so flexoelectricity couples Areas (a) and (c).
6. **Quasicrystals.** One paragraph: two displacement fields (phonon and phason), hence two
   elastic branches; the heat law still enters through `G(s)`. Cite Shechtman 1984 and
   Levine–Steinhardt 1984 for the structure, and one wave paper for the dynamics.

### Inside / outside the template

| Item | Status | Why |
|---|---|---|
| Piezoelectric stiffening (already in text) | inside | effective modulus renormalisation |
| Carrier drift–diffusion branch | **outside** | a second, parabolic field |
| Acoustoelectric gain threshold | **outside** | non-Hermitian coupling, not a relaxation kernel |
| Photo-thermal chain | inside (thermal link) + outside (source term) | kernel survives, forcing is new |
| Flexoelectric polarisation | **inside** | `m(s)` with an extra `k²` term |
| Quasicrystal phason branch | **outside** | second displacement field |

### Where it lands
`s13_multiphysics` (main), `s16c_taxonomy` (rows: piezo-semiconductor; quasicrystal),
`s17_open` (carrier–thermal competition time scales).

### Honest limitation
The review would be listing phenomena, not results: no gain coefficient, no threshold field and
no material constant is quoted, because none of the carrier papers has been read beyond R0 and
because the numbers depend on doping, which the review does not model.

---

## Area (d) — Graded, porous, magneto-electro-elastic, laminated, nanostructured and biological media

Current coverage: `porous` 32, `micropolar` 32, `tissue` 12, `FGM` 8, `magnetoelectric` 4,
`laminated` 1, `graphene`/`nanotube`/`CNT` **0**.

### What to add (proposed: three short paragraphs in `s15_applications` plus one table row)

1. **Functionally graded media.** Material functions `c₁(x)`, `ρ(x)`, `k(x)`: the dispersion
   relation acquires `x`-dependent coefficients and the review's constant-coefficient kernel
   becomes a local statement. Say plainly that the layered analysis of `s11_interfaces` is the
   piecewise-constant limit of this, so the review already covers the graded case in the limit
   that matters for damping estimates.
2. **Porous and double-porous media.** Two diffusing fields (pore pressure and temperature)
   plus elasticity: three fields, one relaxation kernel each. Cite Biot 1941 for the
   poroelastic skeleton and the micropolar/porous thermoelastic papers for the coupling.
3. **Magneto-electro-elastic continua.** The renormalised modulus of the piezoelectric
   discussion, extended by a second coupling constant (magnetostrictive); the algebra is
   identical, so one equation with `e` and `h` side by side suffices.
4. **Laminates and composites.** Zener damping per layer, energy partition at interfaces; the
   Vengallatore 2005 treatment is the reference for a laminated beam, not a homogenised one.
5. **Nanostructures.** Nonlocal elasticity (already §24) + surface energy (§22) + `ℓ` from
   Area (a): the three length scales that compete at the nanoscale, with the review's damping
   estimate as the observable.
6. **Biological tissue.** Bioheat (Pennes) with perfusion: state that the perfusion term is a
   *sink*, not a relaxation, so `G(s)` does not describe it, and that the review's `ω*`
   argument already shows thermoelastic coupling is negligible in tissue at physiological
   frequencies.

### Inside / outside the template

| Item | Status | Why |
|---|---|---|
| Graded properties | inside piecewise / outside continuously | `m` and `G` become `x`-dependent |
| Poroelastic double diffusion | **outside** | extra field (pore pressure) |
| Magneto-electro-elastic | **inside** | modulus renormalisation only |
| Laminated TED | **inside** | per-layer Zener, interface bookkeeping |
| Nonlocal + surface + gradient nanostructure | inside (each) / open (together) | three length scales, no unified model found |
| Perfused tissue | **outside** | volumetric sink, not a memory kernel |

### Where it lands
`s15_applications` (main), `s16c_taxonomy` (two rows), `s17_open` (which length scale wins at
the nanoscale; perfusion vs relaxation in tissue).

### Honest limitation
These are application sketches: no geometry is solved and no parameter is taken from the cited
papers, so the added text must stay at the level of "which template term changes", not
"how much the damping changes".

---

## Cross-cutting note on how to cite this file

`refs_P8.csv` carries, for every entry, the target section id and whether it is inside or
outside the template, so an editing pass can pull the list per section without re-reading this
document. `coverage_gaps.md` records what is *still* missing after this batch, and
`pdfs_needed_P8.csv` records which PDFs must be obtained before any of the "what it shows"
sentences can be upgraded from R0 to R2/R3.
