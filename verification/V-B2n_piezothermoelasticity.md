# V-B2n — Piezothermoelasticity (Mindlin, Nowacki, Chandrasekharaiah; LS and GL versions)

**Revision task R3.** Access date 2026-10-22. ⚠ This is a **structure-level** file: no primary
full text was opened for any piezothermoelasticity source. Read §7 before printing anything.

---

## 1. Task

> **R3:** add `V-B2n` piezothermoelasticity — Mindlin 1961, Nowacki, Chandrasekharaiah's
> generalized piezothermoelasticity (LS and GL versions); governing equations (piezoelectric
> constitutive, pyroelectric coupling, electric field equations, quasi-static electric
> approximation), wave modes (3 elastic + thermal + quasi-static electric), what the quasi-static
> approximation neglects, usual mistakes.

## 2. Method

1. **Source layer.** Locate and verify bibliographic records (done, §4). Only **one** abstract was
   readable (Chandrasekharaiah 1988). Everything else is record-only or secondary.
2. **Derivation layer.** Because the equations themselves are standard continuum balance laws, I
   derive the system from (i) momentum balance, (ii) entropy/energy balance, (iii) Gauss's law,
   plus a stated linear constitutive ansatz, and then **test the consequences** by limits and by
   algebra I can check (e→0, p→0, quasi-static elimination). This is the same policy as the rest of
   the set: the *form* is standard-but-unverified; the *consequences of the form* are verified.
3. **Conventions.** Linear, infinitesimal strain $e_{ij}=\tfrac12(u_{i,j}+u_{j,i})$; small
   temperature difference $\theta=T-T_0$, $|\theta|\ll T_0$; $e^{i(kx-\omega t)}$ time convention;
   **e-form** piezoelectric constants (stress/electric), not d-form. Index order on the
   piezoelectric tensor follows the common solid-mechanics convention: $\sigma_{ij}$ couples to
   $E_k$ through $e_{kij}$, and $D_i$ couples to $e_{jk}$ through $e_{ijk}$. Authors differ; state
   one and keep it.

## 3. Result

### 3.1 The five ingredients

**(i) Momentum.** $\sigma_{ji,j}=\rho\ddot u_i$.

**(ii) Entropy balance.** $\rho T_0\dot\eta=-q_{i,i}$ (no heat supply), with the linearised
entropy density carrying the pyroelectric cross-term.

**(iii) Gauss's law.** $D_{i,i}=\rho_e$; with no free charge, $\boxed{D_{i,i}=0}$.

**(iv) Constitutive laws (linear, anisotropic, e-form).**
$$\sigma_{ij}=C_{ijkl}e_{kl}-e_{kij}E_k-\beta_{ij}\theta$$
$$D_i=\varepsilon_{ij}E_j+e_{ijk}e_{jk}+p_i\theta$$
$$\rho\eta=\frac{\rho c_v}{T_0}\theta+\beta_{ij}e_{ij}+p_iE_i$$
$$q_i=-k_{ij}\theta_{,j}\quad\text{(classical) or a generalised law (LS/GL/GN, see §3.5)}$$

**(v) Quasi-static electric field.** $E_i=-\varphi_{,i}$ with **no** $\partial^2\varphi/\partial t^2$
and no magnetic induction. Substituting into (iv)+(iii):
$$\nabla\!\cdot(\varepsilon\nabla\varphi)=\nabla\!\cdot\big(e:e\big)+\nabla\!\cdot(p\,\theta).$$
This is an **elliptic (Poisson-type) equation for $\varphi$** at each instant: the potential is a
*slave* field, determined by the mechanical and thermal fields with no dynamics of its own.

**Heat equation.** Eliminating $\eta$:
$$\rho c_v\dot\theta+T_0\beta_{ij}\dot e_{ij}=-q_{i,i}+T_0p_i\dot E_i .$$
The last term is the **pyroelectric source**: the rate of change of the electric field acts as a
heat source/sink. Dropping it while keeping $p_i$ in $D_i$ is the most common inconsistency in the
literature (see §3.6).

### 3.2 "Isotropic piezothermoelasticity" is impossible — the symmetry restriction

$e_{ijk}$ is a polar third-rank tensor. Any material with a centre of symmetry has $e_{ijk}=0$,
so **an isotropic medium cannot be piezoelectric**, and "isotropic piezothermoelasticity" is a
contradiction. The physically meaningful reduced symmetry used in almost all "2-D" papers is the
**poled ceramic** class ($6mm$, or transversely isotropic with a distinguished axis, usually $z$):

- elastic: $C_{11},C_{12},C_{13},C_{33},C_{44}$ (5)
- piezoelectric: $e_{31},e_{33},e_{15}$ (3)
- dielectric: $\varepsilon_{11},\varepsilon_{33}$ (2)
- pyroelectric: $p_3$ only (1)
- thermal expansion: $\beta_{11}=\beta_{22},\beta_{33}$ (2)
- heat conduction: $k_{11},k_{33}$ (2)

The brief's "isotropic linear" convention therefore **cannot** be carried over unchanged to this
model: the minimum admissible anisotropy is $6mm$. This is a manuscript-level warning, not a
nuisance: a review that prints "isotropic piezothermoelastic" equations is printing a theory with
no admissible material.

### 3.3 Quasi-static electric approximation: what it neglects

1. **Electric inertia / electromagnetic waves** — dropping $\partial^2\varphi/\partial t^2$ (or,
   in the full Maxwell system, the displacement-current feedback) removes the electromagnetic
   branch. Its natural speed is $c/\sqrt{\varepsilon_r\mu_r}\sim10^{8}$ m/s, i.e. 4–5 orders above
   any acoustic speed; retaining it would add a branch that no acoustic measurement resolves.
2. **Magnetic effects** — no $\partial\mathbf B/\partial t$, hence no piezomagnetic or
   magnetoelastic back-coupling; the electric field is curl-free.
3. **Retardation / finite signal speed of the electric field** — the potential responds
   instantaneously to a change in strain. This is a non-relativistic idealisation, harmless at
   acoustic time scales, but it means the model has an infinite-speed ingredient even when the
   thermal part is hyperbolic. Worth one sentence in a review that elsewhere criticises infinite
   thermal speed.
4. **It does *not* neglect the piezoelectric stiffening** — see §3.4. That is the point most often
   got wrong.

### 3.4 Consequences of the quasi-static elimination, derived and checked

**Piezoelectric stiffening.** In 1-D with $D=0$ (no free charge, $D$ constant $=0$ for a
shorted/open sample), $D=\varepsilon E+e\,e_{11}+p\theta=0$ gives $E=-(e\,e_{11}+p\theta)/\varepsilon$,
so
$$\sigma=\Big(C+\frac{e^2}{\varepsilon}\Big)e_{11}-\Big(\beta-\frac{ep}{\varepsilon}\Big)\theta .$$
Two effects, both derived by simple elimination and both **verified symbolically (sympy)**:

- the elastic modulus is **stiffened** by $e^2/\varepsilon$ (open-circuit / $c_D$ moduli);
- the thermoelastic coupling constant is **renormalised**, $\beta\to\beta-ep/\varepsilon$, by the
  pyroelectric path.

Numerical illustration with **synthetic** constants chosen purely for arithmetic ($C=100$ GPa,
$e=17$ C/m², $\varepsilon=1.3\times10^{-8}$ F/m, $\rho=7500$ kg/m³, $\beta=1.5\times10^{6}$ Pa/K,
$p=5\times10^{-4}$ C/(m²K) — **no real material is claimed**):

| quantity | value |
|---|---|
| $C$ (short-circuit, $E=0$) | $1.0000\times10^{11}$ Pa |
| $e^2/\varepsilon$ | $2.2231\times10^{10}$ Pa (**+22.2 %**) |
| $C+e^2/\varepsilon$ (open-circuit) | $1.2223\times10^{11}$ Pa |
| $c_E=\sqrt{C/\rho}$ | 3651.5 m/s |
| $c_D=\sqrt{(C+e^2/\varepsilon)/\rho}$ | 4037.0 m/s (**+10.6 %**) |
| $\beta\to\beta-ep/\varepsilon$ | $1.5\times10^{6}\to8.46\times10^{5}$ Pa/K |

**The single most consequential consequence for a review:** whether a quoted "piezothermoelastic
longitudinal speed" is $c_E$ or $c_D$ depends on the *electrical boundary condition*, not on the
material alone. Two papers can disagree by ~10 % here and both be right. A review that tabulates
speeds without stating the electric boundary condition is not tabulating a material property.

### 3.5 Wave modes — and why "quasi-static electric mode" is a misnomer

Count the field components: $u_i$ (3) + $\theta$ (1) + $\varphi$ (1) = 5. The quasi-static
$\varphi$ satisfies an **elliptic constraint**, not an evolution equation, so it carries **no
independent branch** and no initial data. What the dispersion relation contains is:

- **3 elastic/acoustic branches** (quasi-longitudinal, quasi-transverse, SH) — all three are
  piezoelectrically stiffened, and in the $6mm$ case SH couples to $\varphi$ (Bleustein–Gulyaev
  type surface waves are the standard consequence);
- **1 thermal branch** (parabolic for Fourier; hyperbolic with speed $\sqrt{\kappa/\tau_0}$ for a
  relaxation/generalised law);
- **0 electric branches** — the electric field is a **constraint mode** whose "frequency" is not
  defined; it appears in the eigenvectors (the potential moves with the mechanical wave) but not
  as a separate dispersion curve.

So the brief's "3 elastic + thermal + quasi-static electric" is right **as a count of fields** and
misleading **as a count of modes**: it is 4 propagating branches plus one constraint. If the
electric inertia is restored, the fifth branch appears at the electromagnetic speed — which is the
honest way to say what the approximation bought.

Branch labelling is asymptotic only: the quasi-longitudinal and thermal branches **hybridise**
(avoided crossing) near the coincidence of their speeds, so "elastic" and "thermal" are names for
the two ends of a continuous curve pair, not identities. This is the piezo analogue of the LS
thermal/elastic avoided crossing already recorded in `V-B2b`.

### 3.6 The LS and GL versions (Chandrasekharaiah)

- **LS-type (heat-flux-dependent) piezothermoelasticity — Chandrasekharaiah (1988).** His summary
  states that the theory "includes heat-flux among the independent constitutive variables" and that
  the linearised version "admits a finite speed for thermal signals", with "an equation of energy
  balance and a theorem on the uniqueness of solution". Structure: replace Fourier's law by
  $q_i+\tau_0\dot q_i=-k_{ij}\theta_{,j}$ and keep §3.1(i)–(v) otherwise unchanged; the thermal
  branch becomes hyperbolic with $c_h=\sqrt{\kappa/\tau_0}$, and the piezoelectric stiffening and
  pyroelectric source are untouched in form.
- **GL-type (temperature-rate-dependent) piezothermoelasticity — Chandrasekharaiah (1984)**,
  "A temperature-rate dependent thermo-piezoelectricity", *J. Thermal Stresses* **7**:293–306
  (verified only as a reference in Chandrasekharaiah 1988's list). Structure: keep Fourier's law
  but let the entropy carry $\dot\theta$, i.e. $\sigma_{ij}=C_{ijkl}e_{kl}-e_{kij}E_k-\beta_{ij}(\theta+\tau_1\dot\theta)$
  and $\rho c_v(\dot\theta+\tau_0\ddot\theta)+\dots$, with the same caveats as `V-B2c` §R7
  (**GL's own notation stands unverified; the same slot confusion applies**).

In both versions the **piezoelectric and pyroelectric constitutive content is unchanged** — only
the thermal operator changes. This is worth one sentence in the review: the "generalisation" is
purely in the heat-conduction half of the system, so all the §3.4 electric-boundary-condition
pitfalls survive it intact.

### 3.7 Usual mistakes (verified as *structural* pitfalls; not all attested in print)

1. **"Isotropic piezothermoelasticity"** — impossible by symmetry (§3.2).
2. **Pyroelectric term in $D_i$ but not in the heat equation** (or vice versa) — breaks the
   energy balance identity; the source $T_0p_i\dot E_i$ must be kept if $p_i$ is kept.
3. **Setting $D_i=0$ instead of $D_{i,i}=0$.** In 1-D with no free charge these coincide; in 2-D/3-D
   they do not, and the 1-D shortcut silently changes the problem.
4. **Counting the quasi-static electric field as a mode** (§3.5).
5. **Mixing e-form and d-form constants** when comparing speeds; $d=e\,s^E$, so a "piezoelectric
   constant" quoted without its form (and without the elastic compliances) is not a material
   constant in any usable sense.
6. **Quoting $c_E$ where the wave is open-circuit** (§3.4) — up to ~10 % error in the illustration.
7. **In generalised versions, putting the relaxation time on the potential instead of the
   temperature** — the electric field is quasi-static, so it cannot carry a relaxation time; a
   paper that writes $\tau$ on $\varphi$ has changed the electric model, not the thermal one.
8. **Labelling hybridised branches as "the elastic wave" and "the thermal wave"** beyond the
   asymptotic regime (§3.5).

## 4. Evidence / Sources

1. **Mindlin, R. D. (1961).** "On the equations of motion of piezoelectric crystals." In: *Problems
   of Continuum Mechanics* (J. Radok, ed.), pp. 282–290. Philadelphia: SIAM.
   **No DOI** (book chapter; not indexed in Crossref). Accessed 2026-10-22.
   **Access level: SECONDARY — bibliographic details taken from the reference list of source 4
   (Chandrasekharaiah 1988, ref. [8]), which gives author, title, editorship, pages and publisher.
   Not opened.**
2. **Mindlin, R. D. (1952).** "Forced thickness-shear and flexural vibrations of piezoelectric
   crystal plates." *Journal of Applied Physics* **23**(1): 83–88. DOI `10.1063/1.1701983`.
   Crossref 160. **Access level: record only.** *Different paper from the 1961 chapter* — do not
   conflate; a citation that attributes the piezoelectric equations of motion to Mindlin (1952) is
   citing the plate-vibration paper, not the chapter.
3. **Nowacki, W. (1978).** "Some general theorems of thermopiezoelectricity." *Journal of Thermal
   Stresses* **1**(2): 171–182. DOI `10.1080/01495737808926940`. Crossref 263.
   **Access level: record only.**
4. **Chandrasekharaiah, D. S. (1988).** "A generalized linear thermoelasticity theory for
   piezoelectric media." *Acta Mechanica* **71**(1–4): 39–49. DOI `10.1007/BF01173936`.
   Crossref 228. Accessed 2026-10-22. **Access level: SUMMARY/ABSTRACT read** (Springer page:
   "A theory of thermoelasticity for piezoelectric materials which includes heat-flux among the
   independent constitutive variables is formulated. It is found that the linearized version of the
   theory admits a finite speed for thermal signals. An equation of energy balance and a theorem on
   the uniqueness of solution are obtained."). Full text paywalled.
5. **Chandrasekharaiah, D. S. (1984).** "A temperature-rate dependent thermo-piezoelectricity."
   *Journal of Thermal Stresses* **7**: 293–306. Accessed 2026-10-22. **Access level: SECONDARY —
   reference [6] of source 4.** Not otherwise verified; no Crossref check performed.
6. **Nowacki, W. (1979).** "Foundations of linear piezoelectricity." In: *Electromagnetic
   Interactions in Elastic Solids* (H. Parkus, ed.), Springer, Wien. **Access level: SECONDARY —
   reference [9] of source 4.**

The equations in §3.1 are the standard linear piezothermoelastic system. **No source opened this
session states them.** They are reproduced here as the form implied by the balance laws plus the
stated constitutive ansatz, and every consequence I draw from them is checked algebraically in §5.

## 5. Checks done

1. **e→0 limit:** the elimination of §3.4 gives $\sigma=Ce_{11}-\beta\theta$ exactly, and
   $c_D\to c_E$; verified symbolically and numerically (the stiffening term vanishes identically
   when $e=0$).
2. **Two routes for the stiffening:** (a) hand elimination of $E$ from the two constitutive
   equations; (b) `sympy.solve` on $D=0$ substituted back into $\sigma$ — same result,
   $1.2223\times10^{11}$ Pa and $\beta_{\rm eff}=8.46\times10^{5}$ Pa/K.
3. **Dimensional analysis:** $e^2/\varepsilon$ = (C/m²)²·m/F = Pa ✓; $ep/\varepsilon$ =
   (C/m²)(C/(m²K))·m/F = Pa/K ✓ (the renormalised $\beta$).
4. **Ellipticity check:** the quasi-static equation for $\varphi$ has no time derivative of
   $\varphi$, hence no branch; consistent with the mode count in §3.5.
5. **Consistency of the heat equation:** with $p=0$ and $e=0$ it reduces to
   $\rho c_v\dot\theta=-q_{i,i}$, i.e. Biot/Fourier as in `V-B2a` ✓.
6. **LS limit:** $\tau_0\to0$ in the LS-type flux law returns Fourier and the parabolic thermal
   branch, as required.

## 6. Confidence

- **Structure of the linear piezothermoelastic system (§3.1): MEDIUM.** It is the standard form and
  is internally consistent, but **no primary source was read**; a transcription error in the sign
  or index order of $e_{kij}$ cannot be excluded from this file alone.
- **Impossibility of isotropic piezoelectricity (§3.2): HIGH.** This is a symmetry statement
  (centrosymmetry kills a polar third-rank tensor), independent of any source.
- **$6mm$ independent-constant count: MEDIUM** (standard, but not checked against a source here).
- **Stiffening/re normalisation result (§3.4): HIGH as algebra**, given the ansatz — verified two
  ways. **The numerical values are synthetic and mean nothing physically.**
- **Mode-count argument (§3.5): HIGH on the "constraint not a mode" claim** (it follows from
  ellipticity); **MEDIUM on "3 elastic branches"** (anisotropy can split into three genuinely
  coupled branches, which is what "quasi-P/quasi-SV/SH" means only in the sagittal-plane
  decoupling used by most papers).
- **Chandrasekharaiah 1988 finite-speed claim: HIGH as a quotation** from the accessible summary;
  the *derivation* in that paper is unverified.
- **GL-type piezo (1984) structure: LOW** — secondary reference only, and inherits `V-B2c`'s
  unverified GL notation.

## 7. NOT verified / open issues

1. **No primary full text opened** for any of the five sources. Mindlin 1961 is documented only
   through Chandrasekharaiah's reference list; Nowacki 1978/1979 likewise.
2. **The equations in §3.1 are unattributed.** Before printing, they must be matched to a page of
   Mindlin (1961) or Chandrasekharaiah (1988). The three things to check: the index convention on
   $e_{kij}$, the presence of the $T_0p_i\dot E_i$ term in the heat equation, and whether the
   entropy includes the $p_iE_i$ term (some formulations drop it, which is not equivalent).
3. **No coupled dispersion relation was computed.** §3.5's mode structure is argued from the
   constitutive structure and ellipticity, not from a determinant. The hybridisation/avoided
   crossing is asserted by analogy with the LS case, not computed for a $6mm$ crystal.
4. **No material constants verified.** No PZT/BaTiO₃/LiNbO₃ constant set is quoted; the numbers in
   §3.4 are synthetic and labelled as such. Do not lift them into the review.
5. **Chandrasekharaiah (1984)** — pages, existence and content all from a secondary reference [6] of
   source 4. No Crossref query was run for it; treat pages (7:293–306) as unconfirmed.
6. **Surface-wave consequences** (Bleustein–Gulyaev, Rayleigh-type) are mentioned only as the known
   consequence of SH–potential coupling; **not** derived or sourced here.
7. **Pyroelectricity vs flexoelectricity** is not discussed at all. A review paragraph claiming
   completeness on piezoelectric coupling should not be written from this file.
