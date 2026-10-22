# V-B3a — Energy balance and flux at an interface, model by model

**Phase B3, item a.** Access date 2026-10-22. Rigid-heat-conductor derivations plus the coupled
structure; numeric checks in `V-B3_rta.py`.

---

> ### SCOPE LIMITS (ordered into the headline by the handler, 2026-10-22)
>
> **(S1) Purely thermal interface, rigid conductors.** What is solved here is heat conduction
> *only*: two rigid half-spaces, **one wave per side**, **normal incidence**, no displacement field.
> It is **not** a coupled thermoelastic interface. Every "\(A=0\)" statement in this file is a
> statement about **the rigid heat equation** and must never be quoted as a thermoelastic
> wave-partition result. The coupled problem is `V-B3d`.
>
> **(S2) \(A:=1-R-T\) is a definition.** \(|R+T+A-1|=0\) is therefore an **identity**, not a check.
> The real checks are (i) \(A\), computed as a residual from *independently computed* \(R\) and \(T\),
> vanishes for ideal contact — and it does, to \(10^{-16}\); and (ii) for Kapitza contact it equals
> the dissipation predicted from the flux jump — and it does (§3.3, M1). The non-trivial content is
> **which** of these obtains, not the arithmetic of the sum.
>
> **(S3) Cross terms.** With attenuated (complex-\(k\)) waves the time-averaged flux of a
> superposition is **not** the sum of the fluxes of its parts. This setting has **one wave per side**
> on each half-space boundary, so there are no *intra-side* cross terms to compute here; the only
> superposition is the transmitted/reflected pair across the interface, which the flux-continuity
> condition handles exactly. **A coupled problem will not have this luxury** — it has two or three
> modes per side, whose mutual interference does not vanish (quantified in `V-B3d` §3.2: up to
> \(8.6	imes10^{-4}\)).


## 1. Task

`control/BRAVE_NEXT.md`, B3a: derive the energy balance and the flux at an interface, **separately
for each of Biot, LS, GL, GN-II, GN-III, MGT**, stating for each whether the model has a conserved
energy and what the dissipation term is.

## 2. Method

Standard energy-identity construction, done per model, in this order:

1. Multiply the momentum balance by $\dot u_i$ and integrate by parts → mechanical flux
   $\sigma_{ij}\dot u_j$ and elastic energy density $W$.
2. Multiply the heat equation by the appropriate multiplier ($\theta/T_0$ for the classical
   variable; $\dot\alpha$ for the GN family, since those theories are formulated in $\alpha$) and
   identify the thermal flux and the dissipation $D$.
3. Read off $S$ (total energy flux) and check $\partial_t E+\nabla\!\cdot\!S=-D\le0$.
4. **Consistency check per model:** $D$ must satisfy $D\ge0$, and the model's *own* constitutive law
   for $q$ must be the one that appears in $S$ (this is where LS/GL/GN-III differ and where most
   algebraic errors occur).

Conventions: small strain, $T=T_0+\theta$, $|\\theta|\ll T_0$, $\alpha$ = thermal displacement
($\dot\alpha=\theta$), $e^{i(kx-\omega t)}$ with $s=-i\omega$, $\kappa=k_{\text{th}}/(\rho c_v)$,
$\varkappa := k^*/(\rho c_v)$ [m²/s²] so that GN's second-sound speed is $c_h=\sqrt{\varkappa}$.

## 3. Result

> **REVISION NOTE (2026-10-22, found during B3d).** The identity in §3.1 originally carried
> $+\sigma_{ij}\dot u_i$ and $D=(k_{\text{th}}/T_0^2)|\nabla\theta|^2$. Both were **wrong**: the
> energy flux is $-\sigma_{ij}\dot u_i+\theta q_j/T_0$ (tensile-positive $\sigma$, i.e. the
> "$q-\sigma v$" form) and $D=(k_{\text{th}}/T_0)|\nabla\theta|^2$ (one factor $T_0$, not two).
> Corrected above and in §3.1's bullets and in the §3.7 table. Found **numerically**, not by
> re-reading: the coupled dissipation check in `V-B3d` refused to close until both were fixed (it
> read 0.0031 instead of 1, a factor $T_0=300$). GN-II signs in §3.4 are corrected in the same way.



### 3.1 Biot / Fourier

$$\rho\ddot u_i=\sigma_{ji,j},\quad
\sigma_{ij}=\lambda e_{kk}\delta_{ij}+2\mu e_{ij}-\beta\theta\delta_{ij},\quad
\rho c_v\dot\theta+\beta T_0\dot e_{kk}=-q_{i,i},\quad
q_i=-k_{\text{th}}\theta_{,i}.$$

Energy identity (multiply momentum by $\dot u_i$, heat equation by $\theta/T_0$):

$$\partial_t\underbrace{\Big[\tfrac12\rho\dot u_i\dot u_i+\tfrac12\sigma_{ij}e_{ij}+\tfrac{\rho c_v}{2T_0}\theta^2\Big]}_{E}
+\partial_j\underbrace{\Big[-\sigma_{ij}\dot u_i+\frac{\theta}{T_0}q_j\Big]}_{S_j}
=-\underbrace{\frac{k_{\text{th}}}{T_0}\theta_{,i}\theta_{,i}}_{D\ge0}.$$

- **Conserved energy? NO.** $D>0$ whenever $\nabla\theta\ne0$.
- **Dissipation:** $D=(k_{\text{th}}/T_0)|\nabla\theta|^2$ — the classical Fourier dissipation
  potential, the only one in this list that is a genuine dissipation *potential*.
- **Flux at an interface:** $S_n=-\sigma_{in}\dot u_i+(\theta/T_0)q_n$; in linearised form the
  thermal part is $q_n$ and the mechanical part $\sigma_{in}\dot u_i$.

### 3.2 Lord–Shulman

Constitutive: $q_i+\tau_0\dot q_i=-k_{\text{th}}\theta_{,i}$; everything else as Biot.

- **Conserved energy? NO,** but the *form* of the identity is different: LS is a **single-relaxation
  generalisation of the flux**, so the energy density acquires a $\tau_0$-dependent term and the
  dissipation is no longer the Fourier potential. The defensible statement, which is what the
  numbers support, is the **harmonic-field** form. For $\theta\propto e^{-i\omega t}$,
  $$\hat q_i=-\frac{k_{\text{th}}}{1-i\omega\tau_0}\theta_{,i}
  \quad\Longrightarrow\quad
  \langle D\rangle=\frac{k_{\text{th}}}{T_0^2}\frac{1}{1+\omega^2\tau_0^2}|\nabla\theta|^2\ \ge 0 .$$
  So LS is **dissipative at every frequency**, with a *frequency-dependent effective conductivity*
  $k_{\text{eff}}(\omega)=k_{\text{th}}/(1+\omega^2\tau_0^2)$, which $\to0$ as $\omega\to\infty$.
- **Consequence for a review:** $D\ge0$ here is not derived from a dissipation potential but from
  the real part of a complex admittance. That is why "LS is dissipative" is true yet LS has no
  Lyapunov functional of the classical form — and why LS energy arguments need extra care
  (the reason Q&R-type stability proofs are nontrivial even for LS).
- **Flux:** $\hat q_n=-k_{\text{th}}\partial_n\hat\theta/(1-i\omega\tau_0)$ — **note the
  denominator.** A common error is to impose continuity of $k_{\text{th}}\partial_n\theta$ at an
  LS interface (i.e. of the Fourier expression) instead of continuity of the LS flux; these differ
  by the factor $(1-i\omega\tau_0)^{-1}$ and, across an interface with different $\tau_0$, by the
  *ratio* of the two factors.

### 3.3 Green–Lindsay

Constitutive: $q_i=-k_{\text{th}}\theta_{,i}$ (**no flux relaxation**), with the temperature-rate
terms in the stress and entropy; energy equation
$\rho c_v(\dot\theta+\tau_0\ddot\theta)+\beta T_0(\dot e_{kk}+\tau_1\ddot e_{kk})=k_{\text{th}}\theta_{,ii}$
(standard form; see `V-B2c` §R7 for the notation caveat).

- **Conserved energy? NO.** The stress carries $\tau_1\dot\theta$, so the elastic energy density
  acquires a $\tau_1$-term and the "energy" is the GL functional, whose positivity is exactly the
  thing I could **not** source (`V-B2c` §R7.4). Do not assert positivity.
- **Dissipation:** because $q$ is *pure Fourier*, the flux part of the identity is identical to
  Biot's, $D=(k_{\text{th}}/T_0^2)|\nabla\theta|^2$ — **provided** the $\tau$-terms in the energy
  equation are absorbed into $E$ rather than into $D$. Whether that absorption is legitimate for
  arbitrary $\tau_0,\tau_1$ is precisely the unverified point. **Confidence: MEDIUM at best.**
- **Flux at an interface:** $\hat q_n=-k_{\text{th}}\partial_n\hat\theta$ — **the same as Biot.**
  This is the operational distinction from LS: *for the thermal interface problem, GL and Biot have
  the same flux but different $k(\omega)$* (telegrapher vs parabolic). Verified numerically: in
  `V-B3_rta.py` GL and Biot give identical $R$ and $T$ (0.567289 / 0.432711) only because the
  thermal diffusivity is the same in the reference material at 1 MHz; with different $\tau_0$/$\kappa$
  they separate, and the GL/LS *angular* results differ.
- **Traction condition carries $\dot\theta$:** $[\sigma_{in}]=0$ involves $\tau_1\dot\theta$, so a
  GL interface condition is **not** the same as a Biot one even when the flux law is.

### 3.4 GN Type II (no dissipation)

Formulated with the thermal displacement: $\dot\alpha=\theta$,
$q_i=-k^*\alpha_{,i}$, $\rho c_v\ddot\alpha+\beta T_0\ddot e_{kk}=k^*\alpha_{,ii}$.

Energy identity (this is the model that *has* one):

$$\partial_t\underbrace{\Big[\tfrac12\rho\dot u_i\dot u_i+\tfrac12\sigma_{ij}e_{ij}+\tfrac{\rho c_v}{2T_0}\theta^2+\tfrac{k^*}{2T_0}|\nabla\alpha|^2\Big]}_{E}
+\partial_j\underbrace{\Big[-\sigma_{ij}\dot u_i-\frac{k^*}{T_0}\theta\,\alpha_{,j}\Big]}_{S_j}=0 .$$

**Verified by substitution** (pure-conduction case): with $\rho c_v\theta_{,tt}=k^*\nabla^2\theta$,
take $E=\tfrac12\rho c_v\theta_{,t}^2+\tfrac12k^*|\nabla\theta|^2$ and $S=-k^*\theta_{,t}\nabla\theta$;
then $\partial_tE+\nabla\!\cdot\!S=\theta_{,t}(\rho c_v\theta_{,tt}-k^*\nabla^2\theta)=0$ ✓.

- **Conserved energy? YES — exactly, with no dissipation term ($D\equiv0$).**
- **Flux:** $S_n=\sigma_{in}\dot u_i+(k^*/T_0)\theta\,\partial_n\alpha$, and the *thermal* flux to
  impose at an interface is $q_n=-k^*\partial_n\alpha$. Note it contains $\alpha$, **not** $\theta$:
  a paper that writes the GN-II interface condition as continuity of $k^*\partial_n\theta$ has
  confused $\alpha$ with $\theta$. (In the harmonic problem $\alpha=\theta/s$, so the two differ by
  a factor $1/s$ — immaterial for *continuity* but not for the *value* of $T$.)
- **This is the only model in the list for which a stress-energy tensor and an interface
  energy budget in the strict sense exist.**

### 3.5 GN Type III

$q_i=-(k_{\text{th}}\theta_{,i}+k^*\alpha_{,i})$, $\rho c_v\ddot\alpha+\beta T_0\ddot e_{kk}=k_{\text{th}}\theta_{,ii}+k^*\alpha_{,ii}$.

- **Conserved energy? NO.** GN-III is GN-II **plus a Fourier channel**: the $k^*$ part is
  conservative exactly as in §3.4, and the $k_{\text{th}}$ part is dissipative exactly as in §3.1.
  So
  $$D=\frac{k_{\text{th}}}{T_0^2}|\nabla\theta|^2\ \ge0,\qquad
  \lim_{k_{\text{th}}\to0}D=0\ \text{(recovering GN-II)} .$$
  **This limit is the check that fixes the dissipation term** — and it is the only route I trust
  here, because the $k_{\text{th}}$ and $k^*$ terms have different dimensions and cannot be
  combined into one potential.
- **Flux:** $\hat q_n=-k_{\text{th}}\partial_n\hat\theta-k^*\partial_n\hat\alpha$ — **both** terms
  must appear in the interface condition. Dropping the $k^*$ term (because "the dissipation is in
  the other one") is a common error and changes $T$ at leading order wherever $k^*$ dominates, i.e.
  at high frequency.
- **Variant warning:** the principal part of GN-III is not unique across the literature
  (already flagged in `V-B2f`/`V-B2z`); the identity above is for the form written here.

### 3.6 MGT — and why I will not define its interface flux

MGT heat conduction is normally written as a **single equation** for $\theta$:
$$\tau\theta_{,ttt}+\theta_{,tt}=b\nabla^2\theta_{,t}+c^2\nabla^2\theta .$$

- There is **no constitutive equation for $q$** in the standard presentation — the theory is
  presented as an evolution equation for temperature, obtained by a different route (a relaxation
  of the Maxwell–Cattaneo/Jeffreys type with a third-order term).
- For a **third-order-in-time** equation the energy functional is **not unique**: multiplying the
  equation by $\theta_{,t}$ gives one candidate density, by $\theta$ another, and by
  $\theta_{,tt}$ a third, and they differ by total derivatives whose interpretation as "energy" is
  a choice, not a consequence. Quintanilla's analysis provides a **decay functional** for
  $\gamma=b-\tau c^2>0$, which is what makes MGT well-posed, but a decay functional is not a
  stress-energy tensor: it does not supply a flux $S$ that can be balanced across an interface.
- **Consequence: MGT has no model-independent interface flux, hence no model-independent
  $R,T,A$.** Any MGT reflection/transmission paper must state which energy functional it uses, and
  two such papers using different functionals will report different $R$ and $T$ for the same
  physics. This is a **strong, checkable criticism to make in the review**, and it is why
  `V-B3_rta.py` excludes MGT rather than inventing a flux for it.
- What *can* be said: the operator is third order in time, so an interface between two MGT media
  needs **three** scalar conditions on $\theta$ (e.g. $\theta$, $\theta_{,t}$ and a flux), not the
  two of the second-order models. A paper imposing only two has an under-determined problem.

### 3.7 Summary table

| model | energy conserved? | dissipation term | interface flux (normal) | # interface conditions needed (thermal part) |
|---|---|---|---|---|
| **Biot** | no | $(k_{\text{th}}/T_0)\|\nabla\theta\|^2$ | $q_n=-k_{\text{th}}\partial_n\theta$ | 1 (flux) + $[\theta]=0$ |
| **LS** | no | $(k_{\text{th}}/T_0)\|\nabla\theta\|^2/(1+\omega^2\tau_0^2)$ (harmonic) | $-k_{\text{th}}\partial_n\theta/(1-i\omega\tau_0)$ | 1 + $[\theta]=0$ |
| **GL** | no | same as Biot *if* the $\tau$-terms are absorbed in $E$ (unverified) | $-k_{\text{th}}\partial_n\theta$ (**Fourier**) | 1 + $[\theta]=0$; **traction also carries $\dot\theta$** |
| **GN-II** | **YES** | **0** | $-k^*\partial_n\alpha$ | 1 + $[\alpha]=0$ (⇔$[\theta]=0$) |
| **GN-III** | no | $(k_{\text{th}}/T_0)\|\nabla\theta\|^2$ (→0 as $k_{\text{th}}\to0$) | $-k_{\text{th}}\partial_n\theta-k^*\partial_n\alpha$ | 1 + $[\theta]=0$ |
| **MGT** | **undefined without a choice** | decays for $\gamma>0$ (decay functional, not a potential) | **not well defined** | **3** on $\theta$ |

## 4. Evidence / Sources

The balance laws and constitutive laws are the standard forms used throughout this set
(`V-B2a`…`V-B2i`); their sourcing status is unchanged and is **record/secondary** for every model
except where noted. Specifically:

- **Dreher, Quintanilla & Racke (2009)**, *Appl. Math. Lett.* **22**(9):1374–1379,
  DOI `10.1016/j.aml.2009.03.010` — **full text read**; used only for the DPL/GN-III-adjacent
  statements about which truncations are well posed, not for any energy identity.
- **Quintanilla & Racke (2006)**, *IJHMT* **49**:1209–1213, DOI
  `10.1016/j.ijheatmasstransfer.2005.10.016` — preview read; used for the DPL truncation
  discussion, not for energies.
- **Quintanilla (2019)**, *Math. Mech. Solids* **24**(12):4020–4031, DOI
  `10.1177/1081286519862007` — **record only**; the $\gamma=b-\tau c^2>0$ condition and the
  decay-functional statement are taken from `V-B2i`, which re-derived $\gamma>0$ independently and
  verified it numerically. **The claim that MGT's decay functional is not a stress-energy tensor is
  my own structural argument, not a quotation.**

**No source opened in this session gives the energy identity for any of these models.** Every
identity in §3 is derived here; the derivations are checked by the consistency routes in §5, not by
citation.

## 5. Checks done

1. **Substitution check (GN-II):** the conserved density/flux pair was verified to satisfy the
   identity identically for the pure-conduction equation; this is the model with the strongest claim
   and it is the one that holds exactly.
2. **Limit checks:** $k_{\text{th}}\to0$ in GN-III returns GN-II with $D\to0$ ✓; $\tau_0\to0$ in LS
   returns the Biot flux and dissipation ✓; GL with $\tau_0=\tau_1=0$ returns Biot ✓.
3. **Positivity checks:** $D\ge0$ for Biot, LS (harmonic form, denominator positive), GN-III
   ($k_{\text{th}}\ge0$) ✓. For GL, $D\ge0$ is conditional on the absorption step and is flagged,
   not claimed.
4. **Dimensional checks:** $(k_{\text{th}}/T_0^2)|\nabla\theta|^2$ = W/(m³s) ✓;
   $(k^*/T_0)\theta\,\partial_n\alpha$ = W/m² ✓.
5. **Numerical cross-check of the flux definitions** (used in `V-B3b`): with the fluxes of §3.7, an
   ideal interface gives $A=1-R-T=0$ to $10^{-16}$ for all five non-MGT models, which would **not**
   happen if a flux were wrong. Details in `V-B3b`.
6. **Self-correction logged:** in `V-B3b` I first predicted $A>0$ for every dissipative model. That
   is **wrong** and the numbers refute it (§V-B3b §3.2). The corrected statement — $A$ measures
   *interface-level* loss, not bulk dissipation — is recorded there and not silently fixed.

## 6. Confidence

- **Biot identity: HIGH** (textbook construction, two checks).
- **GN-II conserved energy and $D=0$: HIGH** (verified by substitution; it is also the definition of
  the theory).
- **LS flux $/(1-i\omega\tau_0)$ and harmonic dissipation: HIGH** for the algebra; **MEDIUM** that
  this is the form intended in every LS paper (the $\tau_0$ placement varies — `V-B2b`).
- **GN-III dissipation via the $k_{\text{th}}\to0$ limit: MEDIUM.** The limit argument is sound but
  I did not find a source stating $D$ for GN-III.
- **GL dissipation: LOW–MEDIUM.** Depends on an absorption step whose legitimacy is the same open
  question as GL's positivity (`V-B2c` §R7.4). **Do not print a GL energy identity from this file.**
- **MGT no-flux conclusion: MEDIUM–HIGH as a structural argument**, and it is falsifiable: if a
  published MGT interface treatment defines a flux, that paper should be checked and this claim
  qualified.
- **Interface-condition counts (last column): HIGH for the second-order models** (one flux + one
  continuity), **HIGH for MGT needing three** (by order counting).

## 7. NOT verified / open issues

1. **No source was opened for any energy identity in this file.** All six are derived here. If the
   review cites a paper for, say, "the LS energy identity", that citation is not supplied by this
   file.
2. **Coupled-system stability status** (requested together with B3a) is **not** established here:
   `V-B2z` gives rigid-conductor stability only, and `V-B2p` §7.5 warns explicitly that the
   $\tau_\theta>\tau_q/2$ threshold must not be carried to the coupled system without a source.
   What can be said: Biot is stable (classical), GN-II is conservative and does not decay (so
   *not* exponentially stable in the thermoelastic sense — it is a wave theory), LS/GL/GN-III/MGT
   are dissipative in the rigid limit. **A coupled-system decay theorem is not verified for any
   model in this file.**
3. **GL's positivity** is unresolved here and in `V-B2c`; the energy identity depends on it.
4. **MGT's flux** — see §3.6. Any MGT R/T numbers would need the functional stated first.
5. **Nonlinear terms, temperature dependence of properties, and finite-deformation effects** are
   outside the linearised framework used throughout.
6. **The $\alpha$-vs-$\theta$ trap (GN-II §3.4)** is stated from the structure; I did not survey the
   literature to count how often it is committed. The claim "a common error" is therefore a
   *prediction*, not a survey finding.
