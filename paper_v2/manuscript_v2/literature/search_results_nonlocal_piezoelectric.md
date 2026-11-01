# Literature Search Results — Nonlocal and Piezoelectric Energy Flux

**Search date:** 2026-10-21

---

## Nonlocal Elasticity — Eringen

**Foundational:**
- Eringen, A.C. (1972). Nonlocal polar elastic fields. *Int. J. Eng. Sci.*
- Eringen, A.C. (1983). On differential equations of nonlocal elasticity and solutions of screw dislocation and surface waves. *J. Appl. Phys.*
- Eringen, A.C. (1974). Theory of nonlocal thermoelasticity. *Int. J. Eng. Sci.* 12:389-404. — **333 citations**, nonlocal stress, entropy, heat flux as integrals of local ones

**Key results from search:**
- [1] ScienceDirect: Theory of nonlocal thermoelasticity (Eringen 1974) — nonlocal stress, entropy, heat flux all integral forms
- [3] MDPI J 2025: Thermodynamics and Nonlocality in Continuum Physics — energy balance ρ ε̇ = T:D − ∇·q + ρr
- [4] ScienceDirect 2016: Eringen nonlocal integral stress model — differential form (1−(e₀a)²∇²)σ = τ
- [6] NSF review: Nonlocal elasticity and boundary condition paradoxes — Eringen 1983 differential model
- [7] IJSS 2014: Eringen nonlocal beams — differential model equivalent
- [8] Springer 2021: Nonlocal elasticity boundary condition paradoxes review
- [10] arXiv 1806.03906: From nonlocal Eringen model to fractional elasticity — σ = ∫A(x,x′)Cε(x′)dx′
- [12] Mathematics 2022: Two-phase integral model nanobeams
- [13] Utah notes: Basic Thermoelasticity Banerjee — divergence theorem derivations
- [14] Continuum Mech. Therm. 2021: Nonlocal MGT magneto-thermoelastic — (1−ξ²∇²)τ = σ
- [15] PMC 8814213: Nonlocal nanobeam gradient heating — σkl = ∫α|r−r′| τkl(r′) dVr′
- [17] Nature Scientific Reports 2025: Nonlocal thermoelastic nanobeams 3PHL — (1−ξ²∇²)tij = σij
- [19] IJSS 2025: Rayleigh waves Eringen nonlocal modified kernels
- [20] Boundary Value Problems 2019: Micropolar bodies with voids energy solutions
- [21] HAL 2016: On nonconservativeness of Eringen's nonlocal elasticity — σ − lc²σ′′ = Eε

## Piezoelectric Constitutive and Energy

**Key results from search:**
- [3] PMC 7559475: FGP medium MDD — constitutive equations σij = Cijklεkl − eijkEk − βijθ; ρS = ρCE T0 θ + βijεij + piEi
- [9] ScienceDirect 2023: Energy flow model piezoelectric harvesters — Di = eijESj + εiiσEi
- [15] Johns Hopkins thesis 2017: Computational Analysis of Piezoelectric Systems — electric enthalpy density Ḣ = S:J K ĖJK − ĖI DI
- [17] ScienceDirect 2008: Crack energy density piezoelectric — energy density dW/dV = ½σijεij + ½DiEi
- [19] ScienceDirect 2020: Piezo response temperature/humidity — Di = ∈ijTEj + dimTm

## Nonlocal Piezo-Thermoelastic with MDD/MGT

- [6] Springer 2026: Analysis of nonlocal piezo-thermoelastic media MGT MDD — three coupled equations heat/motion/Maxwell
- [11] Springer 2026: Heat map analysis nonlocal Kelvin-Voigt piezo-semiconductors MDD — KG nonlocal operator + 3PHL + semiconductor + piezoelectric

---

## Energy Flux Derivation — Primary Source Mapping

| Flux Type | Governing Law | Primary Source | Status |
|-----------|--------------|----------------|--------|
| Classical | Jᵢ = σⱼᵢvᵢ + qᵢ | Derived (EQ-007) | VERIFIED |
| LS | qi + τ₀q̇ᵢ = −kT,ᵢ | Lord & Shulman 1967 | NEEDS DERIVATION |
| DPL | q(t+τq) = −k∇T(t+τT) | Tzou 1995 | NEEDS DERIVATION |
| TPL | q(t+τq) = −[k∇T(t+τT) + k*∇ν(t+τν)] | Tzou 1996/97 | NEEDS DERIVATION |
| MGT | τq̈ + q̇ = −(k/ρc)∇(Ṫ + τṪ̈) | Guyer & Krumhansl | NEEDS DERIVATION |
| MDD | Convolution kernel heat flux | Wang & Li 2011 | NEEDS DERIVATION |
| GN-II | Entropy flux h = ∂ψ/∂∇α | Green & Naghdi 1991 | NEEDS DERIVATION |
| GN-III | Mixed type I/II flux | Green & Naghdi 1993 | NEEDS DERIVATION |
| Nonlocal | Integral-form flux | Eringen 1974 | NEEDS DERIVATION |
| Electrical | Jᵢᵉˡᵉᶜ = −φḊᵢ or equivalent | Piezoelectric literature | NEEDS DERIVATION |

---

**Next steps:** Build expanded literature database CSV (target 500+ records), then begin Section 3 drafting and energy flux derivations.