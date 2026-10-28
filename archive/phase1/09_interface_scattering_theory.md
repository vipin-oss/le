# Interface Scattering Theory — Phase 1

**Prepared:** 2026-10-21  
**Status:** Partially completed (framework sketched; derivations pending)  
**Evidence standard:** `VERIFIED` / `DERIVED` / `SCHEMATIC` / `HYPOTHESIS`

---

## 1. Problem Statement

Consider an interface at x_n = 0 between two half-spaces:
- Medium 1 (x_n < 0): generalized thermoelastic/piezoelectric/poroelastic
- Medium 2 (x_n > 0): different multiphysics continuum

An incident wave from medium 1 generates reflected modes in medium 1 and transmitted modes in medium 2.

---

## 2. Wave Solution Ansatz

For each medium, substitute harmonic plane-wave form:

```
u_i = U_i exp[i(k_j x_j - ωt)]
T = Θ exp[i(k_j x_j - ωt)]
φ = Φ exp[i(k_j x_j - ωt)]
D_i = Δ_i exp[i(k_j x_j - ωt)]
```

where `k_j` is the complex wave vector, `ω` is angular frequency.

---

## 3. Secular Equation

Substitution into governing equations yields a Christoffel-type system:

```
Γ_ij(n, ω) U_j = ρ ω² U_i
```

where `Γ_ij` depends on propagation direction `n = k/|k|`, material properties, and thermal/electrical/porous coupling.

Nontrivial solutions require:

```
det[Γ_ij - ρ ω² δ_ij] = 0
```

This is a high-degree polynomial in complex slowness. Each root corresponds to a wave mode:
- **Propagating modes:** Real phase velocity, imaginary attenuation
- **Evanescent modes:** Imaginary phase velocity (decaying)
- **Attenuating modes:** Complex phase velocity (decaying while propagating)

---

## 4. Interface Conditions

### 4.1 Perfect bonding

| Quantity | Condition |
|----------|-----------|
| Displacement | u_i^(1) = u_i^(2) |
| Traction | σ_ji^(1) n_j = σ_ji^(2) n_j |
| Temperature | T^(1) = T^(2) |
| Heat flux | q_i^(1) n_i = q_i^(2) n_i |
| Electric potential | φ^(1) = φ^(2) |
| Electric displacement | D_i^(1) n_i = D_i^(2) n_i |
| Porosity | φ_vol^(1) = φ_vol^(2) (if applicable) |
| Pore pressure | p^(1) = p^(2) (if applicable) |

### 4.2 Imperfect bonding (spring-type)

```
u_i^(2) - u_i^(1) = K_i^u t_i  (displacement jump proportional to traction)
q^(2) - q^(1) = K^q (T^(2) - T^(1))  (thermal contact resistance)
φ^(2) - φ^(1) = K^φ (D^(2) - D^(1))  (electrical contact resistance)
```

where `K` are interface stiffness parameters.

---

## 5. Scattering Matrix Formulation

### 5.1 Amplitude system

The interface conditions yield a linear system:

```
M · [A_reflected, A_transmitted]^T = b · A_incident
```

where:
- `A_incident` = incident wave amplitude (known)
- `A_reflected` = reflected mode amplitudes (unknown)
- `A_transmitted` = transmitted mode amplitudes (unknown)
- `M` = interface condition matrix
- `b` = incident coupling vector

### 5.2 Reflection and transmission coefficients

```
r_j = A_reflected,j / A_incident      (amplitude ratio)
t_k = A_transmitted,k / A_incident    (amplitude ratio)
```

### 5.3 Critical distinction: amplitude vs energy

**Amplitude ratios are NOT energy ratios.** Energy flux for mode m:

```
J_n,m = (1/2) Re[σ_ji v_j* n_i + q_i n_i* + ...]
```

Energy ratios:

```
R_j = |J_n,ref,j| / |J_n,inc|
T_k = |J_n,trans,k| / |J_n,inc|
```

For complex modes, cross terms between modes can appear in the total flux. Modal separation requires orthogonality conditions that may not hold in dissipative/coupled systems.

---

## 6. Conservation Check

For steady-state harmonic waves at a passive interface:

```
Σ_j R_j + Σ_k T_k + A = 1
```

where `A` accounts for dissipation, interface storage, and mode conversion losses.

**This identity does NOT hold when:**
- The interface stores energy (imperfect bonding)
- External sources are present
- Nonlocal boundary work occurs
- Stored energy changes with time

**Correct alternative:**
```
Σ_j R_j + Σ_k T_k + A + ∂\mathcal{E}_interface/∂t = 1
```

---

## 7. Complex Wave Number Treatment

For complex slowness `s = s_r + i s_i`:
- Phase velocity: `v_phase = ω / Re(k)`
- Attenuation: `α = Im(k)`
- Energy velocity: `v_energy = J / \mathcal{E}` (may differ from phase and group velocity)

In dissipative media, phase velocity, group velocity, and energy velocity generally differ. This affects energy ratio definitions.

---

## 8. What Remains (Phase 1 Milestones E-F)

| Item | Status |
|------|--------|
| Derive secular equation for representative interface | NOT STARTED |
| Compute reflection/transmission coefficients | NOT STARTED |
| Derive energy flux for each mode | NOT STARTED |
| Test conservation: ΣR + ΣT + A = 1 | NOT STARTED |
| Handle complex modes (evanescent, attenuating) | NOT STARTED |
| Interface matrix for imperfect bonding | NOT STARTED |
| Symbolic verification of limiting cases | NOT STARTED |
