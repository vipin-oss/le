# Foundational Theory — Phase 1

**Prepared:** 2026-10-21  
**Status:** Partially completed (lineage and schematic equations documented; full derivations pending)  
**Evidence standard:** `VERIFIED` (Crossref/OpenAlex source) / `DERIVED` (analyst derivation) / `SCHEMATIC` (representative form, not source-extracted)

---

## 1. Historical Lineage of Thermoelastic Theories

Verified foundational contributions (DOIs Crossref-verified, 2026-10-21):

| Year | Authors | Title | Journal | DOI | Core Contribution | Verified Citations |
|------|---------|-------|---------|-----|-------------------|-------------------|
| 1956 | Biot, M. A. | Thermoelasticity and Irreversible Thermodynamics | J. Appl. Phys. 27, 240–253 | 10.1063/1.1722351 | Coupled thermoelasticity via irreversible thermodynamics | 2854 |
| 1967 | Lord, H. W.; Shulman, Y. | A generalized dynamical theory of thermoelasticity | J. Mech. Phys. Solids 15, 299–309 | 10.1016/0022-5096(67)90024-5 | First hyperbolic (single-relaxation-time) model | 4068 |
| 1972 | Green, A. E.; Lindsay, K. A. | Thermoelasticity | J. Elasticity 2, 1–7 | 10.1007/bf00045689 | Temperature-rate (two-temperature) theory | 2929 |
| 1972 | Eringen, A. C. | Linear theory of nonlocal elasticity | IJES 10, 425–435 | 10.1016/0020-7225(72)90050-x | Nonlocal elasticity; plane wave dispersion | 1272 |
| 1979 | Nunziato, J. W.; Cowin, S. C. | Nonlinear theory of elastic materials with voids | Arch. Rat. Mech. Anal. 72, 175–201 | 10.1007/bf00249363 | Volume fraction as independent field | 790 |
| 1991 | Green, A. E.; Naghdi, P. M. | Re-examination of thermomechanics postulates | Proc. R. Soc. A 432, 171–194 | 10.1098/rspa.1991.0012 | Types II & III: dissipationless wave heat propagation | 1097 |
| 1995 | Tzou, D. Y. | Unified field approach for heat conduction | J. Heat Transfer 117, 8–16 | 10.1115/1.2822329 | Dual-phase-lag model | 1995 |
| 2007 | Roy Choudhuri, S. K. | On a thermoelastic three-phase-lag model | J. Thermal Stresses 30, 231–238 | 10.1080/01495730601130919 | Three-phase-lag extension | 766 |
| 2019 | Quintanilla, R. | Moore–Gibson–Thompson thermoelasticity | Math. Mech. Solids 24(12), 4020–4031 | 10.1177/1081286519862007 | Third-order-in-time hyperbolic thermoelasticity | 409 |

**Audit note:** All DOIs verified via Crossref exact bibliographic match. Citation counts are OpenAlex snapshots (2026-10-21), not cross-checked against Scopus/WoS.

---

## 2. Balance Principles (SCHEMATIC)

The following balance equations represent the continuum-mechanics foundation. They are **schematic** — representative of the model family, not extracted from any single source.

### 2.1 Conservation of mass

```
∂ρ/∂t + ∂(ρ v_i)/∂x_i = 0
```

### 2.2 Balance of linear momentum

```
ρ ∂²u_i/∂t² = ∂σ_ji/∂x_j + ρ f_i
```

### 2.3 Balance of angular momentum

```
σ_ij = σ_ji  (in the absence of couple stresses)
```

### 2.4 First law of thermodynamics (energy balance)

```
∂/∂t (ρ e) = σ_ij ∂v_i/∂x_j - ∂q_i/∂x_i + ρ r
```

where `e` is internal energy density, `q_i` is heat flux, `r` is heat supply.

### 2.5 Second law of thermodynamics (entropy inequality)

```
∂/∂t (ρ s) + ∂J_i^s/∂x_i ≥ ρ r / T
```

where `s` is entropy density, `J_i^s` is entropy flux, `T` is absolute temperature.

### 2.6 Entropy production

```
σ_s = ∂/∂t (ρ s) + ∂J_i^s/∂x_i - ρ r / T ≥ 0
```

---

## 3. Constitutive Thermodynamics (SCHEMATIC)

### 3.1 Free energy potential

For a generalized thermoelastic medium:

```
ψ = ψ(ε_ij, T, T_,i, φ, φ_,i, E_i, D_i, ...)
```

where `ε_ij` is strain, `T` is temperature, `φ` is porosity volume fraction, `E_i` is electric field.

### 3.2 Thermodynamic conjugates

| Variable | Conjugate | Physical meaning |
|----------|-----------|------------------|
| ε_ij | σ_ij | Stress |
| T | -ρ s / T | Negative entropy scaled |
| T_,i | -q_i / T² | Negative heat flux scaled |
| φ | η | Equilibrated stress |
| φ_,i | τ_i | Microstress |
| E_i | D_i | Electric displacement |

### 3.3 Dissipation inequality (Coleman-Noll form)

```
σ_ij ∂ε_ij/∂t - ρ ∂ψ/∂t - ρ s ∂T/∂t - q_i ∂(1/T)/∂x_i - η ∂φ/∂t - τ_i ∂φ_,i/∂x_i - ... ≥ 0
```

### 3.4 Constitutive restrictions

For thermodynamic admissibility:
- **Free energy convexity:** Hessian of ψ positive semi-definite
- **Dissipation non-negativity:** All dissipative fluxes satisfy Onsager relations
- **Positive-definiteness:** Stiffness, thermal conductivity, dielectric permittivity tensors positive definite

---

## 4. Heat-Conduction Model Hierarchy

| Model | Flux law | Verified source | Dissipative? | Finite heat speed? |
|-------|----------|-----------------|--------------|--------------------|
| Fourier | `q_i = -k T_,i` | Classical | Yes | No (infinite) |
| Lord–Shulman | `q_i + τ q_i˙ = -k T_,i` | [`10.1016/0022-5096(67)90024-5`](https://doi.org/10.1016/0022-5096(67)90024-5) | Yes | Yes |
| Green–Lindsay | `q_i + ...` coupled to `T˙` | [`10.1007/bf00045689`](https://doi.org/10.1007/bf00045689) | Yes | Yes |
| Green–Naghdi II | No dissipation; `τ₀² T¨ + ...` | [`10.1098/rspa.1991.0012`](https://doi.org/10.1098/rspa.1991.0012) | No | Yes |
| Green–Naghdi III | No dissipation; temperature rate | [`10.1098/rspa.1991.0012`](https://doi.org/10.1098/rspa.1991.0012) | No | Yes |
| Dual-phase-lag | `q_i(t+τ_q) = -k T_,i(t+τ_T)` | [`10.1115/1.2822329`](https://doi.org/10.1115/1.2822329) | Depends | Yes |
| Three-phase-lag | Adds gradient phase lag | [`10.1080/01495730601130919`](https://doi.org/10.1080/01495730601130919) | Depends | Yes |
| Moore–Gibson–Thompson | `τ q¨ + q˙ = -k ∇²T - ...` | [`10.1177/1081286519862007`](https://doi.org/10.1177/1081286519862007) | Yes | Yes |
| Memory-dependent derivative | `D^α_MDD f = ∫ M(ξ) f^(α)(t-ξ) dξ` | [`10.1016/j.camwa.2011.04.028`](https://doi.org/10.1016/j.camwa.2011.04.028) | Depends on kernel | Depends |
| Fractional-order | Caputo/Riemann–Liouville derivative | Not individually verified | Depends | Depends |

**Critical observation:** The energy flux `q_i` in the entropy production term `q_i ∂(1/T)/∂x_i` is not the same as the total energy flux when heat conduction is hyperbolic. The total energy flux must include additional terms (inertial, relaxation, etc.) that are not consistently defined across theories.

---

## 5. Piezoelectric Coupling (SCHEMATIC)

### 5.1 Constitutive relations

```
σ_ij = c_ijkl ε_kl - β_ij (T - T0) - e_kij E_k
D_i = e_ijk ε_jk + κ_ij E_j
E_i = -∂φ/∂x_i
∂D_i/∂x_i = 0  (no free charge)
```

### 5.2 Electrical energy flux

The electrical contribution to energy flux is `E_i ∂D_i/∂t` (or equivalently `D_i ∂E_i/∂t` under appropriate conditions), but the precise form depends on whether the electric field is treated as a state variable or a derived potential.

---

## 6. Porosity / Voids (SCHEMATIC)

### 6.1 Single porosity (Cowin–Nunziato)

Additional balance equation for equilibrated inertia:

```
ρ κ ∂²φ/∂t² = ∂τ_i/∂x_i - η + ρ g
```

where `φ` is porosity volume fraction, `τ_i` is microstress, `η` is equilibrated stress.

### 6.2 Double porosity

Two interacting pore networks with exchange terms. No foundational double-porosity DOI verified in Phase 0; the corpus invokes it without a single canonical reference.

---

## 7. Nonlocal Elasticity (SCHEMATIC)

### 7.1 Eringen stress-based nonlocal

```
σ_ij(x) - (e₀a)² ∇²σ_ij(x) = C_ijkl ε_kl(x)
```

where `e₀a` is the nonlocal length scale parameter.

### 7.2 Energy implication

The divergence theorem used to derive local energy flux breaks down for nonlocal stress. The energy flux must be expressed as an integral (nonlocal) form, which is not consistently handled in the corpus.

---

## 8. Memory-Dependent Derivative (SCHEMATIC)

### 8.1 MDD operator

```
D^α_MDD f(t) = ∫₀ᵗ M(ξ) f^(α)(t-ξ) dξ
```

where `M(ξ)` is a memory kernel.

### 8.2 Energy implication

For convolution-based constitutive laws, "instantaneous" energy flux is not physically meaningful. The energy flux must account for the hereditary (history-dependent) nature of the response.

---

## 9. Dispersion Relations (SCHEMATIC)

For a harmonic plane wave `exp(i(k·x - ωt))`, the secular equation is:

```
det[Γ_ij(n, ω, k) - ρ v² δ_ij] = 0
```

where `Γ` is the Christoffel-type matrix, `n` is propagation direction, `v` is phase velocity.

**Audit note:** The dispersion relation is generally a high-degree polynomial in complex slowness. Closed-form interface solutions exist only for simplified geometries.

---

## 10. What Remains to Be Derived (Phase 1 Milestone E)

| Item | Status | Required for |
|------|--------|--------------|
| Full balance-law derivation for each thermal model | NOT STARTED | Energy-flux framework |
| Total energy flux expression for LS, GL, GN II/III, DPL, TPL, MGT, MDD | NOT STARTED | RQ1, RQ4 |
| Piezoelectric electrical energy flux | NOT STARTED | RQ1 |
| Porosity energy flux (voids, double porosity) | NOT STARTED | RQ1 |
| Nonlocal energy flux (integral form) | NOT STARTED | RQ4 |
| MDD/fractional energy flux (hereditary form) | NOT STARTED | RQ4 |
| Interface energy balance with all coupling channels | NOT STARTED | RQ2, RQ6 |
| Complex-mode reflection/transmission coefficients | NOT STARTED | RQ5 |
| Conservation check: sum of R + T + A = 1 | NOT STARTED | RQ6, RQ7 |
