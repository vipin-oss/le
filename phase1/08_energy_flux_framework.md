# Energy-Flux Framework — Phase 1

**Prepared:** 2026-10-21  
**Status:** Partially completed (framework sketched; derivations pending)  
**Evidence standard:** `VERIFIED` / `DERIVED` / `SCHEMATIC` / `HYPOTHESIS`

---

## 1. Central Challenge

The Phase 0 audit identified the energy-flux definition at interfaces as the central theoretical gap. Papers compute "energy ratios" but no shared definition of the energy flux functional exists across:

- Dissipative media (LS, DPL, MGT, MDD)
- Dissipationless media (GN II/III)
- Piezoelectric media (electrical flux channel)
- Porous media (pore-fluid energy channel)
- Nonlocal media (integral flux required)
- Memory-dependent media (hereditary flux required)
- Imperfectly bonded interfaces (interface storage/dissipation)

This document sketches the framework for investigating whether a unified energy-flux formulation is mathematically possible.

---

## 2. General Balance Representation (TENTATIVE)

\[
\frac{\partial \mathcal{E}}{\partial t} + \nabla \cdot \mathbf{J} = \mathcal{P} - \mathcal{D}
\]

where:
- `\mathcal{E}` = total stored energy density
- `\mathbf{J}` = total energy flux vector
- `\mathcal{P}` = supplied power density
- `\mathcal{D}` = dissipation density (non-negative)

**Status:** This is an initial organizational representation, NOT a proven universal law. Each theory must be tested individually.

---

## 3. Stored Energy Density by Theory

### 3.1 Classical coupled thermoelasticity (Fourier)

```
\mathcal{E} = (1/2) ρ v_i v_i + (1/2) c_ijkl ε_ij ε_kl - β_ij ε_ij (T - T0) + (ρ c_v / 2T0) (T - T0)²
```

### 3.2 Lord–Shulman (single relaxation time)

Additional relaxation energy term needed:

```
\mathcal{E}_LS = \mathcal{E}_classical + (τ / 2k) q_i q_i
```

The `q_i q_i` term represents energy stored in the heat-flux relaxation process.

### 3.3 Green–Naghdi Type II (dissipationless)

No dissipation; energy is conserved. The stored energy includes a thermal displacement gradient term:

```
\mathcal{E}_GN-II = \mathcal{E}_elastic + (ρ c_v / 2T0) T² + (k / 2T0) (∇T)² + ...
```

### 3.4 Green–Naghdi Type III

Similar to Type II but with temperature-rate coupling; different stored energy structure.

### 3.5 Dual-phase-lag

The two phase lags introduce two relaxation processes; stored energy includes both:

```
\mathcal{E}_DPL = \mathcal{E}_classical + (τ_q / 2k) q_i q_i + (τ_T ρ c_v / 2k T0) T_,i T_,i
```

### 3.6 Moore–Gibson–Thompson

Third-order-in-time; stored energy includes acceleration of heat flux:

```
\mathcal{E}_MGT = \mathcal{E}_classical + relaxation terms involving q˙_i q˙_i
```

### 3.7 Memory-dependent derivative

Stored energy is history-dependent:

```
\mathcal{E}_MDD(t) = \mathcal{E}_instantaneous(t) + ∫₀ᵗ K(t-ξ) [\mathcal{E}(ξ)] dξ
```

where `K` is a memory kernel related to the MDD kernel `M`.

### 3.8 Fractional-order

Stored energy involves fractional integrals of the state variables; physical interpretation of fractional energy is an open question.

---

## 4. Total Energy Flux by Theory

### 4.1 Mechanical flux

```
\mathbf{J}_mech = -σ · v  (stress power transmitted across surface)
```

More precisely, `J_i^mech = -σ_ji v_j` (power done by tractions on velocity).

### 4.2 Thermal flux (classical)

```
\mathbf{J}_thermal = q  (Fourier heat flux)
```

### 4.3 Thermal flux (hyperbolic theories)

For LS, DPL, TPL, MGT: `q` alone is NOT sufficient. Additional terms from relaxation processes contribute:

```
\mathbf{J}_thermal_hyperbolic = q + relaxation correction terms
```

The exact form of the correction terms is theory-dependent and not standardized.

### 4.4 Electrical flux (piezoelectric)

```
\mathbf{J}_electric = -E × H  (Poynting-like, for electromagnetic)
```

or for quasistatic piezoelectricity:

```
\mathbf{J}_electric = -φ ∂D/∂t · n  or  -D ∂φ/∂t · n
```

The precise form depends on the electrical formulation.

### 4.5 Nonlocal flux

For Eringen nonlocal elasticity, the divergence theorem argument fails:

```
∇ · σ ≠ local expression
```

The energy flux must be nonlocal (integral):

```
\mathbf{J}_nonlocal(x) = ∫ K(x-x') σ(x') · v(x') dx'
```

No standardized form exists in the corpus.

### 4.6 MDD/fractional flux

Convolution kernels require hereditary flux:

```
\mathbf{J}_MDD(t) = ∫₀ᵗ M(t-ξ) \mathbf{J}(ξ) dξ
```

The physical meaning of "instantaneous flux" is ill-defined.

---

## 5. Interface Energy Balance

At an interface between medium 1 (x_n < 0) and medium 2 (x_n > 0):

### 5.1 Perfect bonding

Continuity conditions:
- Displacement: `u_i^(1) = u_i^(2)`
- Traction: `σ_ji^(1) n_j = σ_ji^(2) n_j`
- Temperature: `T^(1) = T^(2)`
- Heat flux: `q_i^(1) n_i = q_i^(2) n_i`
- Electric potential: `φ^(1) = φ^(2)`
- Electric displacement: `D_i^(1) n_i = D_i^(2) n_i`

Energy conservation at interface:

```
[J_n] = 0  (jump in normal flux = 0)
```

or equivalently: `J_n^(1) = J_n^(2)` (no energy stored at interface).

### 5.2 Imperfect bonding (spring-type)

Interface can store and dissipate energy:

```
[J_n] = ∂\mathcal{E}_interface/∂t + \mathcal{D}_interface
```

where `\mathcal{E}_interface` is interface stored energy and `\mathcal{D}_interface` is interface dissipation.

### 5.3 Energy ratios

For an incident wave with normal flux `J_n^inc`:

```
R_j = |J_n^ref,j| / |J_n^inc|     (reflection ratio for mode j)
T_k = |J_n^trans,k| / |J_n^inc|   (transmission ratio for mode k)
```

Conservation check:

```
Σ_j R_j + Σ_k T_k + A = 1
```

where `A` is the absorption/loss fraction. This holds ONLY if:
- All fluxes are properly defined
- No interface storage
- No external sources
- Steady-state harmonic regime

---

## 6. Open Questions (Unresolved)

| Question | Status | Significance |
|----------|--------|--------------|
| What is the total energy flux in LS thermoelasticity? | UNRESOLVED | Needed for energy ratios |
| What is the total energy flux in MGT thermoelasticity? | UNRESOLVED | Needed for energy ratios |
| What is the total energy flux in nonlocal elasticity? | UNRESOLVED | Divergence theorem fails |
| What is the total energy flux in MDD media? | UNRESOLVED | Convolution makes instantaneous flux ill-defined |
| Is energy conserved at imperfectly bonded interfaces? | UNRESOLVED | Interface storage/dissipation unquantified |
| Can a unified flux expression cover all theories? | HYPOTHESIS | May be impossible; negative result is valuable |
| Do published energy ratios sum to unity? | UNVERIFIED | Never checked systematically |

---

## 7. Next Steps (Milestone E)

1. Derive total energy flux for LS theory from first principles
2. Derive total energy flux for MGT theory from first principles
3. Derive total energy flux for nonlocal elasticity (integral form)
4. Derive total energy flux for MDD media (hereditary form)
5. Test each derivation against 3-5 representative interface papers
6. Document where unification succeeds and where it fails
7. Prepare conservation audit table of corpus energy-ratio papers