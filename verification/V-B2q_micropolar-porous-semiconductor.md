# V-B2q — Micropolar, porous and semiconductor thermoelasticity

**Revision task R4 (second of two).** Access date 2026-10-22.

> **DEPTH MARKER — READ FIRST.** This is a **short, deliberately shallow** overview, as R4
> specifies ("only a short source-verified overview with governing-equation structure and which
> are covered by classical vs generalized theories"). **No primary full text was opened** for any
> of the three families. Two families have Crossref-verified bibliographic anchors; the
> semiconductor family has **no verified foundational source at all** and its section is marked
> **UNVERIFIED** throughout. Do not let this file stand in for a section of the review without
> the sources being opened first.

---

## 1. Task

Part of R4: `V-B2q` — micropolar / porous / semiconductor thermoelasticity, short, with
governing-equation structure and "which are covered by classical vs generalized theories",
depth marked honestly.

## 2. Method

1. Verify bibliographic anchors (§4): 4 verified by Crossref DOI, 4 secondary (reference lists),
   1 unverified.
2. State the governing structure at the level I can defend: **what field is added, which balance
   law it obeys, how the theory degenerates to the classical one, and what it does to the wave
   spectrum.** No attempt at a full constitutive listing for anisotropic cases.
3. Provide the **classification** the brief asks for (§3.4), which is the part that matters for a
   review: all three are *kinematic/transport enrichments*, not theories of heat conduction.
4. Mark every unverified statement.

**Conventions:** linear, small strain, isotropic where a form is given; $e^{i(kx-\omega t)}$.

## 3. Result

### 3.1 Micropolar (Cosserat) thermoelasticity

**Added field:** the microrotation $\varphi_i$ (3 components), independent of $u_i$. **Degrees of
freedom per point: 6** ($u_i$, $\varphi_i$), plus temperature = 7 field components.

**Balance laws:**
$$\sigma_{ji,j}=\rho\ddot u_i,\qquad m_{ji,j}+\varepsilon_{ijk}\sigma_{jk}=\rho J\ddot\varphi_i .$$
The second equation is what classical elasticity lacks: a couple-stress balance with a
**rotational inertia** $J$ (dimension m²).

**Isotropic constitutive structure** (Eringen's form, as cited in the literature):
$$\sigma_{ij}=\lambda e_{kk}\delta_{ij}+(\mu+\kappa)e_{ij}+\mu e_{ji}-\beta\theta\delta_{ij},
\qquad m_{ij}=\alpha\varphi_{k,k}\delta_{ij}+\beta_m\varphi_{i,j}+\gamma\varphi_{j,i},$$
with $\kappa$ the **micropolar (coupling) modulus** [Pa] and $\alpha,\beta_m,\gamma$ the
couple-stress constants [Pa·m²]. **The notation clash $\beta$ (thermal) vs $\beta_m$ (couple-stress)
is endemic in this literature** — fix one before printing.

**Length scale and dimensionless coupling.** $\gamma/\mu$ has dimension m², giving a material
length; and $\kappa/(\mu+\kappa)\in[0,1)$ is the standard dimensionless coupling number. Both
statements are structural (dimensional analysis); **the exact definitions differ between authors
and are not verified here.**

**Effect on the spectrum.** The microrotation adds **optic-type (band-limited) branches**: the
rotational part has a finite response frequency at $k=0$ set by the couple-stress constants and
$J$, and it does *not* propagate at long wavelength. The theory **degenerates to classical
elasticity as $\kappa,\alpha,\beta_m,\gamma\to0$** (all extra branches go to infinite frequency or
decouple). Hence micropolarity **adds branches with a cutoff**; it does **not** add a finite-speed
thermal wave.

**Positivity/admissibility:** a set of inequalities on
$(\lambda,\mu,\kappa,\alpha,\beta_m,\gamma,J)$ is required; **not reproduced here** (see §7).
Commonly quoted consequences: $\kappa\ge0$, $\mu+\kappa>0$, $J>0$, and inequalities among
$\alpha,\beta_m,\gamma$.

### 3.2 Porous (void) thermoelasticity — Cowin–Nunziato

**Added field:** the void volume fraction $\nu$ (1 component). **DOF: 3 + 1 + 1 = 5.**

**Balance laws:** $\sigma_{ji,j}=\rho\ddot u_i$ as usual, plus the **void balance**
$$h_{i,i}+g=\rho k\ddot\nu,$$
where $h_i$ is the equilibrated (void) stress vector and $k$ a micro-inertia coefficient
[dimension m²]. The constitutive structure adds $\xi\nu$ (a "void stiffness") to the stress and a
quadratic free energy in $\nabla\nu$ — i.e. **a gradient (length-scale) term**, which is the
reason the theory is sometimes (loosely) called "porous gradient thermoelasticity".

**Effect on the spectrum.** One extra **dilatational-type branch** coupling to the volumetric
strain (a "breathing" mode), band-limited like the micropolar rotational branch; the theory
degenerates to classical thermoelasticity as the void coupling $\to0$.

**Anchors (Crossref-verified):** Nunziato & Cowin (1979) *ARMA* **72**:175–201, DOI
`10.1007/BF00249363`; Cowin & Nunziato (1983) *J. Elasticity* **13**:125–147, DOI
`10.1007/BF00041230`. **Neither opened.**

### 3.3 Semiconductor thermoelasticity (photo-thermoelasticity)

**Added field:** the carrier (electron/hole) density $n$ (1 component). **DOF: 3 + 1 + 1 = 5.**

**Governing structure (as commonly written):** an ambipolar diffusion–recombination equation for
$n$,
$$D_E\nabla^2n=\frac{\partial n}{\partial t}+\frac{n-n_0}{\tau_R}+\text{(source from }\dot\theta\text{ and }\dot e_{kk}\text{)},$$
coupled to the heat equation through recombination/generation heat and to the momentum equation
through the **deformation potential** (carrier pressure contributes to stress). $D_E$ is the
ambipolar diffusivity [m²/s] and $\tau_R$ the carrier lifetime [s].

**Effect on the spectrum.** A **diffusive carrier-density-wave ("plasma") branch** with a cutoff
at $\omega\sim1/\tau_R$; it is **dissipative, has no finite-speed front**, and is the reason
semiconductor thermoelasticity is used to model laser-generated ultrasound and photothermal
deflection rather than second sound.

**Source status: UNVERIFIED.** No foundational primary paper was found or opened. The best anchor
located is a book chapter on carrier-density waves (Mandelis 2001, §4.5), record only. **Nothing in
this subsection should be printed without a source.**

### 3.4 The classification the review actually needs

The decisive point: **none of these three is a "generalized thermoelasticity" in the
LS/GL/GN/DPL sense.** Those theories change the **heat-conduction law** (they add relaxation
times, and their business is finite thermal speed and its admissibility). Micropolar, porous and
semiconductor theories change the **kinematics or the carrier transport** and leave the heat law
alone (or leave it interchangeable).

| family | what is added | where the length/time scale enters | composes with | finite *thermal* speed? |
|---|---|---|---|---|
| **micropolar** | microrotation $\varphi_i$ (3) | couple-stress constants ⇒ length; rotational inertia $J$ ⇒ time | **any** heat law: LS, GL, GN-II/III, DPL | **unchanged by micropolarity** — inherited from the heat law |
| **porous** | void fraction $\nu$ (1) | void stiffness + micro-inertia $k$ ⇒ length; $\rho k$ ⇒ time | any heat law | inherited from the heat law |
| **semiconductor** | carrier density $n$ (1) | ambipolar diffusivity ⇒ length; lifetime $\tau_R$ ⇒ time | any heat law | inherited, but the carrier branch is always diffusive |

Consequences worth one paragraph in the review:

1. **They are orthogonal to the relaxation theories.** "Micropolar LS thermoelasticity" and
   "micropolar GL thermoelasticity" are *compositions*, not rival theories. A review that lists
   them as further items in a single progression (Fourier → LS → GL → GN → … → micropolar) is
   conflating two independent axes.
2. **They do not solve the infinite-speed problem**, and papers that present them as doing so are
   mistaking a kinematic enrichment for a thermal one. The thermal branch keeps whatever speed the
   heat law gives it.
3. **They do add branches with a cutoff** (optic-type), which *is* a genuine qualitative change:
   the medium can store energy in a non-propagating mode. This is the legitimate reason to include
   them.
4. **Their length scales are not interchangeable with nonlocal/gradient ones** (`V-B2m`) even where
   the symbols coincide (both are often called $\ell$).

## 4. Evidence / Sources

1. **Nunziato, J. W.; Cowin, S. C. (1979).** "A nonlinear theory of elastic materials with voids."
   *Archive for Rational Mechanics and Analysis* **72**(2): 175–201. DOI `10.1007/BF00249363`.
   Crossref 790. **Record only.**
2. **Cowin, S. C.; Nunziato, J. W. (1983).** "Linear elastic materials with voids." *Journal of
   Elasticity* **13**(2): 125–147. DOI `10.1007/BF00041230`. Crossref 923. **Record only.**
3. **Eringen, A. C. (1999).** "Theory of micropolar elasticity." In: *Microcontinuum Field
   Theories I*, Springer, pp. 101–248. DOI `10.1007/978-1-4612-0555-5_5`. Crossref 92.
   **Record only.** The canonical 1966 *J. Math. Mech.* **15**:909–923 paper is the usual citation;
   **I could not find a Crossref record for it** (queries returned only DTIC reports:
   `10.21236/ad0473723`, 1965, and `10.21236/ad0664271`, 1967, and the 1999 chapter). **The 1966
   coordinates are therefore UNVERIFIED in this file.**
4. **Eringen, A. C. (1970).** "Formulation of problems of micropolar elasticity." In: *Foundations
   of Micropolar Thermoelasticity*, Springer, pp. 87–102. DOI `10.1007/978-3-7091-2904-3_4`.
   **Record only** — note this is a *thermoelasticity* source and thus more on-point than the
   elasticity papers usually cited.
5. **Boschi, E.; Iesan, D. (1972).** "A generalized theory of linear micropolar thermoelasticity."
   *Meccanica* **3**: 154–157. **Access level: SECONDARY — reference [4] of Chandrasekharaiah
   (1988), no DOI checked.**
6. **Dost, S.; Tabbarrok, B. (1978).** "Generalized micropolar thermoelasticity." *Int. J. Engng.
   Sci.* **16**: 173–183. **Access level: SECONDARY — reference [5] of Chandrasekharaiah (1988).**
7. **Chandrasekharaiah, D. S. (1986).** "Heat-flux dependent micropolar thermoelasticity."
   *Int. J. Engng. Sci.* **24**: 1389–1395. **Access level: SECONDARY — reference [7] of
   Chandrasekharaiah (1988).** This is the LS-composition source.
8. **Mandelis, A. (2001).** "Carrier-density-wave fields in electronic solids / semiconductors."
   In: *Diffusion-Wave Fields*, Springer, pp. 584–661. DOI `10.1007/978-1-4757-3548-2_10`.
   Crossref 2. **Record only** — the only anchor found for the carrier-density-wave branch.

**No equation in §3 is transcribed from any of these.** The structures given are the standard ones
and are justified only at the level of "what field is added, which balance law it obeys, how the
classical limit is recovered".

## 5. Checks done

1. **Degeneracy checks (structural):** each theory returns classical thermoelasticity as its new
   coupling constants vanish — micropolar as $\kappa,\alpha,\beta_m,\gamma\to0$; porous as the void
   coupling $\to0$; semiconductor as the deformation-potential and recombination couplings $\to0$.
   This is the defining requirement of an enrichment and is the basis of the "adds a branch with a
   cutoff" claim.
2. **Dimensional analysis:** $J$ [m²], $k$ (void) [m²], $\gamma/\mu$ [m²], $D_E$ [m²/s],
   $\tau_R$ [s] — all consistent with the stated roles (inertia, length, lifetime).
3. **DOF counting:** micropolar 6+1 = 7, porous 3+1+1 = 5, semiconductor 3+1+1 = 5 — arithmetic on
   the stated field content, not a claim about the number of *propagating* branches.
4. **Consistency with the rest of the set:** the "inherited thermal speed" statement follows
   directly from the fact that these enrichments do not touch $q_i$'s law — checkable by
   inspection of the structures in §3.1–§3.3.
5. **Cross-check against `V-B2m`:** the warning that micropolar/porous lengths and
   Eringen/Mindlin lengths are different objects is consistent with `V-B2m`'s finding that even
   *nonlocal* and *gradient* elasticity differ by a factor $10^{6}$ at the same nominal $\ell$.

## 6. Confidence

- **Classification in §3.4 (enrichment vs heat-law generalisation): HIGH.** It follows from the
  structure of the equations, not from a source, and it is the file's main deliverable.
- **Governing structure of micropolar/porous: MEDIUM.** Standard forms, no primary text read.
- **"Adds optic-type branches with a cutoff": MEDIUM.** Structurally right (rotational/void
  inertia with a restoring term gives a finite $k=0$ frequency); **the exact branch counts and
  cutoffs are not computed here.**
- **Semiconductor subsection: LOW/UNVERIFIED.** No foundational source, no equation verified.
- **Bibliographic coordinates: HIGH for sources 1, 2, 3, 4, 8 (Crossref); MEDIUM for 5, 6, 7
  (secondary).**
- **Eringen (1966) *J. Math. Mech.* coordinates: UNVERIFIED.**

## 7. NOT verified / open issues

1. **No primary full text opened** for any of the eight sources. This file is a map, not a survey.
2. **No dispersion relation was computed** for any of the three families. Branch counts, cutoffs
   and avoided crossings are described qualitatively only.
3. **Micropolar positivity inequalities** ($\alpha,\beta_m,\gamma$) are **not** reproduced — the
   sets quoted in the literature differ and I did not verify one. **Do not print a positivity set
   from this file.**
4. **Eringen (1966)** journal coordinates unverified (§4.3). A review citing "Eringen 1966, *J.
   Math. Mech.* 15:909" is citing something I could not confirm bibliographically.
5. **Semiconductor section needs replacing before use** — no source, no equations.
6. **Porous literature beyond Cowin–Nunziato** (e.g. later "porous thermoelasticity" with two
   relaxation times) is not covered.
7. **No coverage of micromorphic/microstretch** generalisations, which are the modern
   generalisation of this family and would be expected in a review of "generalized continua".
8. **Branch-count warning:** the DOF counts in §5.3 are *field components*, not propagating
   branches. If the review needs branch counts, they must be computed from the dispersion
   determinant per theory — this file does not supply them.
