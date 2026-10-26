# Harmonic Energy Transport — Phase 2 Milestone D

**Prepared:** 2026-10-21  
**Status:** Completed (framework established; theory-specific derivations pending)  
**Evidence standard:** DERIVED / SCHEMATIC  
**Source:** Independent derivation; verified against RG-003 full text (Eqs. 45-58)

---

## 1. Harmonic Convention

For real-valued harmonic quantities:
$$f(\mathbf{x},t) = \operatorname{Re}[\widehat{f}(\mathbf{x}) e^{-i\omega t}]$$

where $\omega$ is angular frequency and $i = \sqrt{-1}$.

### 1.1 Time-average product identity

For two real harmonic quantities $a(t) = \operatorname{Re}[\widehat{a}e^{-i\omega t}]$ and $b(t) = \operatorname{Re}[\widehat{b}e^{-i\omega t}]$:

$$\langle a b \rangle_t = \frac{1}{T}\int_0^T a(t)b(t)\,dt = \frac{1}{2}\operatorname{Re}[\widehat{a}\widehat{b}^*]$$

where $^*$ denotes complex conjugation and $T = 2\pi/\omega$.

### 1.2 Sign convention check

With $e^{-i\omega t}$ convention:
- $\dot{f} = -i\omega\widehat{f}e^{-i\omega t}$
- $\overline{\dot{f}} = i\omega\widehat{f}^*e^{i\omega t}$ (complex conjugate)
- $\langle f\dot{g}\rangle_t = \frac{1}{2}\operatorname{Re}[\widehat{f}(i\omega\widehat{g}^*)] = \frac{\omega}{2}\operatorname{Re}[i\widehat{f}\widehat{g}^*] = -\frac{\omega}{2}\operatorname{Im}[\widehat{f}\widehat{g}^*]$

---

## 2. Classical Energy Flux for Harmonic Waves

### 2.1 Mechanical power

For harmonic displacement $u_i = \operatorname{Re}[\widehat{u}_i e^{-i\omega t}]$ and stress $\sigma_{ij} = \operatorname{Re}[\widehat{\sigma}_{ij} e^{-i\omega t}]$:

$$\langle \sigma_{ij}\dot{u}_i \rangle_t = \frac{1}{2}\operatorname{Re}[\widehat{\sigma}_{ij}(-i\omega\widehat{u}_i^*)] = -\frac{\omega}{2}\operatorname{Im}[\widehat{\sigma}_{ij}\widehat{u}_i^*]$$

### 2.2 Heat flux power

$$\langle q_i T_{,i}/T \rangle_t = \frac{1}{2T}\operatorname{Re}[\widehat{q}_i(\widehat{T}_{,i})^*]$$

For Fourier conduction $q_i = -k T_{,i}$:
$$\langle q_i T_{,i}/T \rangle_t = -\frac{k}{2T}|\widehat{T}_{,i}|^2 \leq 0$$

This represents heat dissipation (entropy production).

### 2.3 Total energy flux (harmonic, time-averaged)

$$\langle J_i \rangle_t = \langle \sigma_{ji}v_i + q_i \rangle_t = -\frac{\omega}{2}\operatorname{Im}[\widehat{\sigma}_{ji}\widehat{v}_i^*] + \widehat{q}_i$$

For the normal component at an interface with normal $n_j$:
$$\langle J_n \rangle_t = n_j\langle J_j \rangle_t$$

---

## 3. Energy Flux in RG-003 (Verified from Full Text)

### 3.1 HPS side (piezothermoelastic with MDD+TPL)

From RG-003 Eq. (45), the instantaneous power is:

$$P = -\text{Re}\left(\sigma_{13}\overline{\dot{u}}_1 + \sigma_{33}\overline{\dot{u}}_3 - \phi\overline{\dot{D}}_3 + K_3\overline{T}_{,3}\frac{T}{T_0}\right)$$

For harmonic fields, the time-averaged normal power flux at $x_3 = 0$ is:

$$\langle P \rangle_t = -\frac{1}{2}\text{Re}\left[\widehat{\sigma}_{13}(-i\omega\widehat{u}_1^*) + \widehat{\sigma}_{33}(-i\omega\widehat{u}_3^*) - \widehat{\phi}(-i\omega\widehat{D}_3^*) + \widehat{K_3T}_{,3}\frac{\widehat{T}}{T_0}\right]$$

$$= \frac{\omega}{2}\text{Im}\left[\widehat{\sigma}_{13}\widehat{u}_1^* + \widehat{\sigma}_{33}\widehat{u}_3^* - \widehat{\phi}\widehat{D}_3^*\right] - \frac{1}{2}\text{Re}\left[\widehat{K_3T}_{,3}\frac{\widehat{T}}{T_0}\right]$$

### 3.2 TS side (elastic thermoelastic)

From RG-003 Eq. (46):

$$P^e = -\text{Re}\left(\sigma_{31}^e\overline{\dot{u}}_1^e + \sigma_{33}^e\overline{\dot{u}}_3^e\right)$$

Time-averaged:
$$\langle P^e \rangle_t = \frac{\omega}{2}\text{Im}\left[\widehat{\sigma}_{31}^e\widehat{u}_1^{e*} + \widehat{\sigma}_{33}^e\widehat{u}_3^{e*}\right]$$

### 3.3 CRITICAL: Missing thermal term on TS side

The TS side energy flux $\langle P^e \rangle_t$ contains NO thermal conduction term. For a thermoelastic medium with heat flux $q_i^e$, the complete flux should include $q_i^e n_i$. The omission means:

1. **Thermal energy transport at the interface is not accounted for on the TS side**
2. **The claimed conservation law (Eq. 58) cannot represent total energy conservation**
3. **This is an instance of GAP-001 (no consensus on energy flux definition)**

---

## 4. Energy Ratios for Harmonic Waves

### 4.1 Definition

For an incident wave with normal energy flux $\langle J_n^{\text{inc}}\rangle_t$:

$$R_j = \frac{|\langle J_n^{\text{ref},j}\rangle_t|}{|\langle J_n^{\text{inc}}\rangle_t|}, \quad T_k = \frac{|\langle J_n^{\text{trans},k}\rangle_t|}{|\langle J_n^{\text{inc}}\rangle_t|}$$

### 4.2 RG-003 energy ratios

From RG-003 Eqs. (47)-(53):

Incident P wave energy flux:
$$\langle P_{IP}^e \rangle_t = \frac{1}{2}\left(\alpha_1^{e2}\rho^e k_1^2 + C_T\zeta_1\right)k_1\omega\text{Re}(\cos\theta_0)\|A_0^e\|^2$$

Reflected P wave:
$$\langle P_{RP}^e \rangle_t = -\frac{1}{2}\left(\alpha_1^{e2}\rho^e k_1^2 + C_T\zeta_1\right)k_1\omega\text{Re}(\cos\theta_1)\|A_1^e\|^2$$

Energy ratio:
$$E_{RP} = \frac{\langle P_{RP}^e \rangle_t}{\langle P_{IP}^e \rangle_t}$$

Similar expressions for T, SV, and transmitted waves.

### 4.3 Sign convention

The negative signs in reflected wave energy fluxes (Eqs. 50-52) account for the opposite direction of propagation (negative $x_3$ component).

---

## 5. Complex Wave Modes

### 5.1 Evanescent modes

For complex slowness $q = q_r + i q_i$ with $q_i > 0$:
- Wave decays as $e^{-\omega q_i x_3}$
- Phase velocity: $v_p = \omega/\text{Re}(k)$
- Attenuation: $\alpha = \omega\text{Im}(k)$

### 5.2 Energy flux for evanescent modes

For purely evanescent modes (no net energy propagation in the decay direction):
$$\langle J_n \rangle_t = 0 \quad \text{(for lossless media)}$$

For dissipative media, evanescent modes can transport energy laterally while decaying normally.

### 5.3 Modal orthogonality

In non-self-adjoint systems (dissipative/coupled), conventional modal orthogonality fails. Energy flux inner products must use biorthogonal modes.

**Status:** SCHEMATIC — not independently derived for specific theories.

---

## 6. Cross-Mode Interference

### 6.1 Interaction energy

RG-003 Eq. (57) defines interaction energy between refracted waves $s$ and $t$:

$$\langle P_{st} \rangle_t = \frac{1}{2}\omega^2\text{Re}\left(\Delta_{2s}H_s\overline{H}_t + \Delta_{1s}\overline{W}_t H_s\overline{H}_t + \overline{\Delta}_{7s}\Phi_t H_t\overline{H}_s + \frac{i}{\omega}\frac{K_3}{T_0}\overline{\Delta}_{5s}\Theta_s\overline{H}_s H_t\right)$$

This cross-term accounts for interference between different refracted modes.

### 6.2 Conservation with interaction terms

RG-003 Eq. (58):
$$\sum_{s=1}^{4}\left(ES_s + E_{int} + E_{RP} + E_{RT} + E_{RS}\right) = 1$$

where $E_{int} = \sum_{s,t=1,s\neq t}^{4} E_{st}$.

**Status:** Claimed by RG-003 authors; NOT independently verified. The asymmetric flux definition (TS side missing thermal term) casts doubt on whether this holds for total energy.

---

## 7. Theory-Specific Harmonic Flux Derivations Needed

| Theory | Additional flux terms | Complex mode treatment | Status |
|--------|---------------------|----------------------|--------|
| Classical | None | Standard | DERIVED |
| LS | Relaxation correction | Attenuating modes | SCHEMATIC |
| GN II | Thermal displacement | No dissipation | SCHEMATIC |
| DPL | Two relaxation corrections | Wave + diffusion | SCHEMATIC |
| TPL | Three relaxation corrections | Complex dispersion | SCHEMATIC |
| MGT | $\dot{q}$ acceleration terms | Third-order dispersion | SCHEMATIC |
| MDD | Hereditary convolution | Memory-dependent attenuation | SCHEMATIC |
| Nonlocal | Integral form | Nonlocal dispersion | SCHEMATIC |

---

## 8. Next Steps

1. Derive LS harmonic energy flux from relaxation equation
2. Derive MGT harmonic energy flux
3. Derive nonlocal harmonic energy flux (integral form)
4. Derive MDD hereditary harmonic flux
5. Test conservation identity $\sum R + \sum T + A = 1$ for BM-1 benchmark
6. Verify RG-003 conservation claim with corrected (symmetric) flux definitions
