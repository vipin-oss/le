# Interface Energy Balance — Phase 2 Milestone E

**Prepared:** 2026-10-21  
**Status:** Completed (framework derived; critical findings documented)  
**Evidence standard:** DERIVED / VERIFIED (RG-003 full text)  
**Source:** Independent derivation; verified against RG-003 full text (Eqs. 45-58)

---

## 1. General Interface Energy Balance

### 1.1 Control volume approach

Consider a pillbox control volume straddling the interface at $x_3 = 0$, with height $\epsilon \to 0$ and area $A$.

**Rate of change of stored energy in pillbox:**
$$\frac{d}{dt}\int_{-\epsilon/2}^{\epsilon/2} \mathcal{E} A \, dx_3 \to 0 \quad \text{as } \epsilon \to 0 \text{ (if no interface energy storage)}$$

**Energy flux balance:**
$$J_n^{(1)} A - J_n^{(2)} A + P_{interface} A = \frac{d\mathcal{E}_{interface}}{dt} A$$

where:
- $J_n^{(1)}$ = energy flux from medium 1 toward interface
- $J_n^{(2)}$ = energy flux from medium 2 away from interface
- $P_{interface}$ = power supplied to interface (external sources)
- $\mathcal{E}_{interface}$ = energy stored at interface

### 1.2 Jump condition

$$[J_n] = J_n^{(2)} - J_n^{(1)} = P_{interface} - \frac{\partial\mathcal{E}_{interface}}{\partial t}$$

For a passive interface with no storage and no external sources:
$$[J_n] = 0 \quad \Rightarrow \quad J_n^{(1)} = J_n^{(2)}$$

---

## 2. Classical Energy Flux at Interface

### 2.1 Flux definition

From `07_continuum_balance_derivations.md`:
$$J_i = \sigma_{ji}v_i + q_i$$

Normal component:
$$J_n = \sigma_{3j}v_j + q_3 = \sigma_{31}v_1 + \sigma_{32}v_2 + \sigma_{33}v_3 + q_3$$

### 2.2 Interface continuity conditions

For perfect bonding:
- $v_1^{(1)} = v_1^{(2)}$, $v_2^{(1)} = v_2^{(2)}$, $v_3^{(1)} = v_3^{(2)}$
- $\sigma_{31}^{(1)} = \sigma_{31}^{(2)}$, $\sigma_{32}^{(1)} = \sigma_{32}^{(2)}$, $\sigma_{33}^{(1)} = \sigma_{33}^{(2)}$
- $T^{(1)} = T^{(2)}$
- $q_3^{(1)} = q_3^{(2)}$ (classical heat flux continuity)

With these conditions:
$$J_n^{(1)} = \sigma_{31}^{(1)}v_1^{(1)} + \sigma_{32}^{(1)}v_2^{(1)} + \sigma_{33}^{(1)}v_3^{(1)} + q_3^{(1)}$$
$$J_n^{(2)} = \sigma_{31}^{(2)}v_1^{(2)} + \sigma_{32}^{(2)}v_2^{(2)} + \sigma_{33}^{(2)}v_3^{(2)} + q_3^{(2)}$$

Since all terms match: $J_n^{(1)} = J_n^{(2)}$. ✓

### 2.3 Energy conservation

For harmonic waves at a passive interface:
$$\sum_j R_j + \sum_k T_k + A = 1$$

where $A \geq 0$ is the absorption fraction.

---

## 3. Generalized Theory Energy Flux — Interface Complications

### 3.1 Lord–Shulman

The LS heat equation $q_i + \tau_0\dot{q}_i = -kT_{,i}$ introduces a relaxation term. The classical flux $q_i$ alone may not represent total energy transport.

**Interface condition question:** Should $q_3^{(1)} = q_3^{(2)}$ or should a modified flux condition be used?

**Status:** UNRESOLVED.

### 3.2 Green–Naghdi Type II/III

No dissipation; energy is conserved. The flux includes thermal displacement gradient terms.

**Interface condition question:** What is the appropriate heat flux condition for GN theories?

**Status:** UNRESOLVED.

### 3.3 Piezoelectric

Electrical energy flux must be included:
$$J_i^{elec} = -\phi\dot{D}_i \quad \text{or} \quad J_i^{elec} = -D_i\dot{\phi}$$

Interface conditions:
- $\phi^{(1)} = \phi^{(2)}$ (perfect electrical contact) or $D_3^{(1)} = D_3^{(2)}$ (charge continuity)
- Or $D_3 = 0$ (insulated interface, as in RG-003)

**Status:** PARTIALLY VERIFIED (RG-003 uses $D_3 = 0$).

### 3.4 Nonlocal

The divergence theorem fails for nonlocal stress. Interface energy balance requires integral-form flux.

**Status:** UNRESOLVED.

---

## 4. RG-003 Interface Energy Balance — Verified from Full Text

### 4.1 Energy flux definitions

**HPS side** (Eq. 45):
$$P = -\text{Re}\left(\sigma_{13}\overline{\dot{u}}_1 + \sigma_{33}\overline{\dot{u}}_3 - \phi\overline{\dot{D}}_3 + K_3\overline{T}_{,3}\frac{T}{T_0}\right)$$

**TS side** (Eq. 46):
$$P^e = -\text{Re}\left(\sigma_{31}^e\overline{\dot{u}}_1^e + \sigma_{33}^e\overline{\dot{u}}_3^e\right)$$

### 4.2 Asymmetry finding

The HPS side includes 4 terms: tangential mechanical, normal mechanical, electrical, thermal.
The TS side includes 2 terms: tangential mechanical, normal mechanical only.

**Missing:** Thermal conduction term ($q_3^e$) on the TS side.

### 4.3 Interface conditions (Eq. 38)

$$\sigma_{33} = \sigma_{33}^e, \quad \sigma_{31} = \sigma_{31}^e, \quad u_1 = u_1^e, \quad u_3 = u_3^e, \quad T = T^e$$
$$\left[K_3\frac{\partial}{\partial t}(\cdots) + K_3^*(\cdots)\right]\frac{\partial T}{\partial x_3} = K_e^*\frac{\partial T^e}{\partial x_3}, \quad D_3 = 0$$

The heat flux continuity condition includes MDD operators on the HPS side but not on the TS side — another asymmetry.

### 4.4 Conservation claim (Eq. 58)

$$\sum_{s=1}^{4}(ES_s + E_{int} + E_{RP} + E_{RT} + E_{RS}) = 1$$

**Authors' claim:** "the total of the energy ratios is almost equal to one at each angle of incidence"

**Independent assessment:** This claim is for the specific energy flux definitions used. Given the asymmetric flux (TS side missing thermal term), this conservation law does NOT represent total energy conservation. It represents conservation of mechanical + electrical (HPS only) + thermal (HPS only) energy.

---

## 5. Energy Partitioning Verification

### 5.1 Conservation identity

For steady-state harmonic waves at a passive interface:

$$\sum_j R_j + \sum_k T_k + A = 1$$

where:
- $R_j = |\langle J_n^{\text{ref},j}\rangle_t| / |\langle J_n^{\text{inc}}\rangle_t|$
- $T_k = |\langle J_n^{\text{trans},k}\rangle_t| / |\langle J_n^{\text{inc}}\rangle_t|$
- $A$ = absorption/dissipation fraction

### 5.2 Conditions for validity

| Condition | Required? | RG-003 compliance |
|-----------|-----------|-------------------|
| All fluxes properly defined | YES | PARTIAL (TS side missing thermal flux) |
| No interface storage | YES | YES (pillbox limit $\epsilon \to 0$) |
| No external sources | YES | YES |
| Steady-state harmonic regime | YES | YES |
| Symmetric flux definitions | YES | NO (asymmetric between media) |

### 5.3 What "almost equal to one" means

The RG-003 authors claim energy conservation but their flux definition is incomplete on one side. This means:
- The conservation law holds for a **subset** of energy channels
- Thermal energy transported on the TS side is unaccounted for
- The "missing" energy may appear as numerical error or be attributed to the interaction terms $E_{int}$

---

## 6. Open Questions

| Question | Status | Significance |
|----------|--------|--------------|
| What is the complete energy flux for TS thermoelasticity including thermal transport? | UNRESOLVED | Needed for total energy conservation |
| Does $\sum R + \sum T + A = 1$ hold with symmetric flux definitions? | UNRESOLVED | Tests GAP-002 |
| How does interface storage affect energy balance? | UNRESOLVED | Relevant for imperfect bonding |
| What is the energy flux for nonlocal media at interfaces? | UNRESOLVED | Divergence theorem fails |
| What is the energy flux for MDD media? | UNRESOLVED | Convolution makes instantaneous flux ambiguous |

---

## 7. Next Steps

1. Derive complete energy flux for classical thermoelasticity including thermal term on both sides
2. Test conservation identity $\sum R + \sum T + A = 1$ for BM-1 benchmark
3. Verify RG-003 conservation claim with corrected flux definitions
4. Derive interface energy balance for imperfect bonding
5. Document where conservation succeeds and where it fails
