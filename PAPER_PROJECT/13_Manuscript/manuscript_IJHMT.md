# Orientation-dependent wall stress around circular and elliptical cavities in monoclinic β-Ga₂O₃ under a transient thermal pulse: a verified continuum study with thermal-memory and mechanism ablations

*[AUTHOR INPUT REQUIRED: author names, affiliations, ORCID iDs and corresponding author]*


## Abstract

Thermal stresses around cavities in low-symmetry crystals depend on crystal orientation, cavity shape and heat-conduction law, yet transient studies treat isotropic or highly symmetric media. We study monoclinic β-Ga₂O₃ with a circular and an equal-area elliptical cavity (axis ratio 2) under a Gaussian wall-temperature pulse in plane strain, with Fourier and Lord–Shulman conduction as the primary models and a two-relaxation-time kernel as exploratory variant. The single-pulse response is obtained from a frequency-domain finite-difference solver by Bromwich inversion on a shifted contour, verified against exact and independent solutions (peak error 0.08% at the finest grid, second order). The peak wall stress is orientation-invariant to round-off: 0.854 MPa/K for the circle. The ellipse converts crystal orientation into a peak-stress modulation of 28.7% on the extrapolated sweep (29.9% on the production grid) with numerical uncertainty 1.3 percentage points; single-parameter ablations on the production grid attribute the modulation to competing expansion and stiffness anisotropy, conductivity anisotropy being minor. Thermal memory (hypothetical relaxation times to 20 ps) changes the circular-cavity wall-stress history by at most 6.4% (1.6% at 10 nm and larger) and the peak (dynamic and quasi-static variants) by at most 1.4% (1.0% among dynamic runs); the residual size dependence is a quasi-static collapse plus an O(ε²) inertia correction. Thermoelastic feedback stays below the bound 5δ. Results are properties of a verified continuum model: no experimental validation exists, relaxation times are hypothetical, the expansion data are uncertain by more than an order of magnitude, and continuum validity at 5–50 nm is not established.

**Keywords:** thermoelasticity; cavity; monoclinic crystal; β-Ga₂O₃; Lord–Shulman theory; Bromwich inversion


## Highlights

- Bromwich inversion gives a verified single-pulse thermoelastic cavity response
- Circular-cavity peak wall stress is orientation-invariant to round-off
- Ellipse turns crystal orientation into a 28.7% peak-stress modulation
- Thermal memory shifts the peak wall stress by under 1.4% for τ up to 20 ps
- Verified, not validated: expansion data set the absolute stress scale


## 1. Introduction


### 1.1 Cavities, thermal stress and crystal anisotropy

Classical analyses of thermal stresses around holes and cavities in uniform heat flow are given in [1,2], and anisotropic plates with elliptic boundaries have been treated by complex-variable (Stroh-type) methods under steady conditions [3]. Transient cavity problems with a finite heat-wave speed have been solved for a fibre-reinforced anisotropic medium with a circular hole [4], for spherical cavities [5], for an orthotropic cylindrical cavity [6], and hole-shape effects have been studied in perforated composite plates [7]; boundary-element methods treat holes in general anisotropic discs and planes [8,9]; coated elliptic holes in uniform heat flow have been analysed by complex-variable methods [10] and dual-phase-lag boundary-element formulations for anisotropic media have been developed [11]. The generalized-thermoelasticity studies [4,5,6] concern isotropic or highly symmetric (fibre-reinforced, orthotropic) media and circular or spherical geometry, whereas the studies of general anisotropy and non-circular holes [3,8,9] are steady or quasi-static with Fourier conduction. Within the bounded literature search described in the data package we found no study that combines a low-symmetry crystal, a non-circular cavity, a systematic crystal-orientation sweep and a thermal-memory parameter in a transient coupled analysis (this is a statement about our search, not a claim of priority).


### 1.2 Transient loading, thermal memory and non-Fourier conduction

Coupled thermoelasticity [12] and its generalizations to a finite heat-wave speed are the framework for transient problems: the Lord–Shulman theory with one relaxation time [13] and its extension to anisotropic media with a uniqueness theorem [14]; the general theory of heat conduction with a memory kernel and finite wave speeds is due to Gurtin and Pipkin [15]; dual-phase-lag formulations [16], and later classifications of generalized heat-conduction and thermoelastic-coupling models [17,18]. Monoclinic β-Ga₂O₃ is an ultra-wide-band-gap semiconductor whose elastic [19], thermal-conductivity [20] and thermal-expansion [21,22] tensors are all strongly anisotropic; its room-temperature elastic constants are well characterised [19] and its conductivity tensor has an off-diagonal component in the a–c plane [20], so that crystal orientation, cavity shape and heat-conduction law can interact. The device context and the growth of bulk single crystals of the material are reviewed in [23,24]. Whether this interaction is large enough to matter, and which observable is sensitive to it, is the question addressed here.


### 1.3 Scope of the study and what is claimed

We study the transient coupled thermoelastic response of a circular and of an equal-area elliptical cavity (axis ratio 2) in a monoclinic crystal loaded in plane strain in the a–c plane by a Gaussian wall-temperature pulse. Two conduction laws are treated as primary models — Fourier and Cattaneo–Vernotte (Lord–Shulman) — and a two-relaxation-time kernel is carried along as an exploratory sensitivity variant only (Section 2.5). The study is a **verified continuum parametric study**: the numerical results are verified against exact and independent solutions and their numerical uncertainty is quantified, but they are not compared with experiments, which are not available; the relaxation times are hypothetical and the continuum description is not claimed to hold at the nanometre scale (Section 7).


### 1.4 Contributions and structure of the paper

The contributions are: (i) a verified time-domain method that returns the response of a quiescent medium to a single pulse from a frequency-domain solver by Bromwich inversion on a shifted contour, with the verification chain and the numerical uncertainty reported; (ii) the orientation dependence of the peak wall stress for a circular and an elliptical cavity, including an ablation that separates the contributions of stiffness, thermal-expansion and conductivity anisotropy; (iii) an analytical scaling identity and a local-response result for the circular cavity that explain why thermal memory has a bounded, small effect on the wall stress and what the residual dependence on the cavity size is; (iv) a bound on the thermoelastic feedback. Section 2 states the governing equations and the constitutive framework, Section 3 the analytical results, Section 4 the numerical method, Section 5 the verification, Section 6 the results, and Section 7 the discussion, the limitations and the scope of what can be claimed from them. Section 8 concludes and Section 9 gives the code, the data package and the reproduction procedure.


## 2. Governing equations and constitutive framework


### 2.1 Governing equations

Linear, small-strain thermoelasticity in plane strain is considered in the a–c plane of a monoclinic crystal, with the unique axis b normal to the plane and coordinates (x_{1}, x_{3}) along the crystal a and c axes at zero rotation. With temperature rise θ above the reference temperature T_{0} = 293 K, displacement u = (u_{1}, u_{3}) and Voigt strain ϵ = (ϵ_{11}, ϵ_{33}, γ_{13}), the constitutive law is σ = Qϵ − βθ (Biot [12]); Q is the 3×3 plane-strain block of the stiffness (only C_{11}, C_{13}, C_{15}, C_{33}, C_{35}, C_{55} enter) and β = Cα the thermal-stress vector, which also involves C_{12}, C_{23}, C_{25} through the b-axis expansion. The crystal is rotated by φ about b: the rank-four stiffness and the rank-two conductivity and expansion tensors are rotated by the same angle, and the rotation is cross-checked against an independent three-dimensional rank-four implementation (Section 5.1). Momentum balance and the heat equation with one relaxation time τ (Cattaneo–Vernotte flux law with energy balance, i.e. the Lord–Shulman equation [13,14]) read


$$ \nabla\cdot\boldsymbol{\sigma}=\rho\,\ddot{\mathbf{u}},\qquad \nabla\cdot(\mathbf{K}\nabla\theta)=\left(1+\tau\,\partial_t\right)\left(\rho c_p\,\dot\theta+T_0\,\boldsymbol{\beta}:\dot{\boldsymbol{\epsilon}}\right) \qquad (1) $$

In the Laplace domain (variable s) the heat equation becomes ∇·(K g(s) ∇θ) = s(ρc_{p}θ + T_{0}β:ϵ) with g = 1 for Fourier conduction and g = 1/(1 + sτ) for the relaxation-time law; these two are the primary conduction models of the study. A two-relaxation-time kernel g = ½/(1 + ½sτ) + ½/(1 + 2sτ) is used as an exploratory sensitivity kernel only (it is positive real, hence passive, but is not derived from a free energy) and is labelled exploratory wherever it appears. The medium is quiescent before the pulse (u = θ = 0 and ∂u/∂t = 0 for t < 0). The cavity wall is traction-free and held at the prescribed temperature θ = p(t) = exp(−((t − t_{0})/t_{w})²) with t_{0} = 2.5 t_{th} and t_{w} = 1.2 t_{th}; the outer boundary at R = 80a is clamped (u = 0) and cold (θ = 0). The cavity is a circle of radius a or an ellipse of semi-axes a√χ and a/√χ (equal area, χ = 2) whose major axis is parallel to the crystal a-axis at rotation φ = 0 (Fig. 1). The quantities of interest are defined in Section 2.9 and their discrete forms in Section 4.7.

The class is the kinematic plane strain: the fields are independent of x_2 and u_2 = 0. For a monoclinic crystal with the unique axis normal to the plane the out-of-plane shear stresses σ₁₂ and σ₂₃ vanish identically for every in-plane strain, so no relaxation step is needed to make the constraint admissible and σ₂₂ enters as a reaction, not as a boundary condition. The distinction is stated because the alternative convention — generalised plane strain, σ₂₂ = 0 — is not equivalent here: it would change the plane-strain block Q by 13.7% and the thermal-stress vector β by 37.2% at the parameters of Table 4, so the class is stated explicitly and the solver is built on the constraint, not on the stress.


![Fig. 1](../11_Figures/fig1_setup.png)

**Fig. 1.** Problem set-up: (a) circular and (b) equal-area elliptical cavity in the a–c plane of the crystal (crystal rotated by φ); (c) wall-temperature pulse and quantity-of-interest window.


### 2.2 Kinematics, balance laws and the heat equation

The formulation is written in the laboratory frame; the crystal frame is introduced in Section 2.4 and the two frames coincide at rotation φ = 0. With displacement u = (u_{1}, u_{3}) and temperature rise θ = T − T_{0}, the small-strain tensor in the plane has the three independent components


$$ \epsilon_{11}=\frac{\partial u_1}{\partial x_1},\qquad \epsilon_{33}=\frac{\partial u_3}{\partial x_3},\qquad \gamma_{13}=\frac{\partial u_1}{\partial x_3}+\frac{\partial u_3}{\partial x_1} \qquad (2) $$

written in Voigt form ϵ = (ϵ_{11}, ϵ_{33}, γ_{13}) with the engineering shear γ_{13} = 2ϵ_{13}, so that the stress–strain contraction σ:ϵ = σ_{11}ϵ_{11} + σ_{33}ϵ_{33} + σ_{13}γ_{13} is the mechanical work per unit volume. The strain components satisfy the two-dimensional compatibility relation


$$ \frac{\partial^2\epsilon_{11}}{\partial x_3^2}+\frac{\partial^2\epsilon_{33}}{\partial x_1^2}=\frac{\partial^2\gamma_{13}}{\partial x_1\partial x_3} \qquad (3) $$

which is what allows the displacement form used below. Balance of linear momentum and the first law, in the absence of body heating and internal heat sources, give


$$ \frac{\partial\sigma_{11}}{\partial x_1}+\frac{\partial\sigma_{13}}{\partial x_3}=\rho\,\ddot u_1,\qquad \frac{\partial\sigma_{13}}{\partial x_1}+\frac{\partial\sigma_{33}}{\partial x_3}=\rho\,\ddot u_3 \qquad (4) $$


$$ \rho c_p\,\dot\theta+T_0\,\boldsymbol{\beta}:\dot{\boldsymbol{\epsilon}}=-\nabla\cdot\mathbf{q} \qquad (5) $$

where q is the heat-flux vector and the coupling term T_{0}β:ϵ̇ is the rate at which mechanical work is converted into heat (the Thomson term of linear thermoelasticity [12]). With the Cattaneo–Vernotte flux law with a single relaxation time τ,


$$ \mathbf{q}+\tau\,\frac{\partial\mathbf{q}}{\partial t}=-\mathbf{K}\nabla\theta \qquad (6) $$

eliminating q between the flux law and the energy balance gives the heat equation that is discretised in Section 4,


$$ \nabla\cdot\left(\mathbf{K}\nabla\theta\right)=\left(1+\tau\,\frac{\partial}{\partial t}\right)\left(\rho c_p\,\dot\theta+T_0\,\boldsymbol{\beta}:\dot{\boldsymbol{\epsilon}}\right) \qquad (7) $$

of which Eq. (1) of Section 2.1 is the compact form. The Fourier model is recovered at τ = 0. For τ > 0 the law is hyperbolic: temperature disturbances propagate at the finite speed


$$ v_T=\sqrt{\frac{\bar\kappa}{\tau}},\qquad \bar\kappa=\frac{\sqrt{\det\mathbf{K}}}{\rho c_p} \qquad (8) $$

For the parameters of Table 4, κ̄ = 3.959×10^{−6} m²/s, so that v_{T} = √(κ̄/τ) = 1990 m/s at τ = 1 ps and 445 m/s at τ = 20 ps, against the longitudinal wave speed c_{ref} = (C_{33}/ρ)^{1/2} = 7686 m/s. The second law is satisfied in the form


$$ -\frac{\mathbf{q}\cdot\nabla\theta}{T_0}\geq 0 \qquad (9) $$

which the Cattaneo–Vernotte law meets for every τ > 0 because it is a positive-real (passive) kernel [15], a restriction stated there for a memory kernel rather than for a single relaxation time; the two-relaxation-time kernel of Section 2.5 is positive-real for the same reason but is not derived from a free energy, which is why it is carried as an exploratory variant only. Theories with two relaxation times [25,26,27] and the reviews of hyperbolic and generalized conduction [17,18,28,29,30,31] locate the single-relaxation-time law used here within that literature.


### 2.3 Plane-strain reduction of the monoclinic law

Monoclinic β-Ga₂O₃ has point group 2/m with the twofold axis along the crystallographic b direction. With the b axis taken as x_{2} and Voigt indices 1 = 11, 2 = 22, 3 = 33, 4 = 23, 5 = 13, 6 = 12, the stiffness has thirteen independent constants and the form of Table 1; the four constants C_{15}, C_{25}, C_{35} and C_{46} are the monoclinic couplings, and the thermal expansion is diagonal in the crystal frame, α = (α_{a}, α_{b}, α_{c}, 0, 0, 0), so that


$$ \sigma_I=\sum_{J=1}^{6}C_{IJ}\left(\epsilon_J-\alpha_J\theta\right),\qquad \beta_I=\sum_{J=1}^{6}C_{IJ}\alpha_J \qquad (10) $$

with I = 1, …, 6 (Voigt conventions and the Stroh and Lekhnitskii formalisms for such media are described in [32,33,34]). Plane strain in the a–c plane imposes ϵ_{22} = ϵ_{23} = ϵ_{12} = 0, so the six-dimensional law collapses onto the three in-plane components and


$$ \sigma_{11}=C_{11}\epsilon_{11}+C_{13}\epsilon_{33}+C_{15}\gamma_{13}-\beta_1\theta \qquad (11) $$


$$ \sigma_{33}=C_{13}\epsilon_{11}+C_{33}\epsilon_{33}+C_{35}\gamma_{13}-\beta_3\theta \qquad (12) $$


$$ \sigma_{13}=C_{15}\epsilon_{11}+C_{35}\epsilon_{33}+C_{55}\gamma_{13}-\beta_5\theta \qquad (13) $$

i.e. σ = Qϵ − βθ with the 3×3 block Q of Table 2. The thermal-stress vector β = Σ_{J} C_{IJ}α_{J} involves the b-axis expansion α_{b} through the constants C_{12}, C_{23}, C_{25} that couple the in-plane normal strains to ϵ_{22}:


$$ \beta_1=C_{11}\alpha_a+C_{12}\alpha_b+C_{13}\alpha_c+C_{15}\alpha_5 \qquad (14) $$


$$ \beta_3=C_{13}\alpha_a+C_{23}\alpha_b+C_{33}\alpha_c+C_{35}\alpha_5 \qquad (15) $$


$$ \beta_5=C_{15}\alpha_a+C_{25}\alpha_b+C_{35}\alpha_c+C_{55}\alpha_5 \qquad (16) $$

where α_{5} = 2ϵ_{13}^{th} is the thermal shear, set to zero (a limitation of the available data, Section 7.2). With the parameters of Table 4 this gives β = (1.3093, 1.5796, 0.0018)×10^{6} Pa/K and ‖β‖ = 2.0517 MPa/K; the eigenvalues of Q are 88.51, 126.86 and 463.43 GPa, so the block is positive definite and the elastic problem is elliptic. The out-of-plane stress does not enter the equilibrium equations but is recovered afterwards from


$$ \sigma_{22}=C_{12}\epsilon_{11}+C_{23}\epsilon_{33}+C_{25}\gamma_{13}-\beta_2\theta,\qquad \beta_2=C_{12}\alpha_a+C_{22}\alpha_b+C_{23}\alpha_c+C_{25}\alpha_5 \qquad (17) $$

and does no work because ϵ_{22} = 0 by construction. Table 2 collects the numerical values of the reduced block and of the thermal-stress vector.


**Table 1.** Independent stiffness constants of monoclinic β-Ga₂O₃ used in this study (GPa; literature values [19] transcribed and checked against the source).

| C_{11} | C_{22} | C_{33} | C_{44} | C_{55} | C_{66} | C_{12} | C_{13} | C_{23} | C_{15} | C_{25} | C_{35} | C_{46} |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 242.8 | 343.8 | 347.4 | 47.8 | 88.6 | 104.0 | 128.0 | 160.0 | 70.9 | -1.62 | 0.36 | 0.97 | 5.59 |


**Table 2.** Plane-strain stiffness block Q (GPa, Eq. (11)) and thermal-stress vector β (MPa/K, Eq. (14)) in the crystal frame, computed from Table 4.

| Q_{11} | Q_{13} | Q_{15} | Q_{33} | Q_{35} | Q_{55} | β_{1} | β_{3} | β_{5} | ‖β‖ |
|---|---|---|---|---|---|---|---|---|---|
| 242.8 | 160.0 | -1.62 | 347.4 | 0.97 | 88.6 | 1.3093 | 1.5796 | 0.0018 | 2.0517 |


### 2.4 Rotation of the crystal

Rotating the crystal about the b axis by φ (equivalently, rotating the loading frame by −φ) transforms the material tensors but not the cavity: the cavity geometry is fixed in the laboratory frame and the crystal is turned underneath it. With


$$ \mathbf{R}(\phi)=\left[\cos\phi,\,-\sin\phi;\;\sin\phi,\,\cos\phi\right] \qquad (18) $$

acting on in-plane vectors as v_{lab} = R v_{crys}, the fourth-order stiffness, the conductivity and the in-plane expansion transform as


$$ C^{\prime}_{ijkl}=R_{ip}R_{jq}R_{kr}R_{ls}\,C_{pqrs},\qquad \mathbf{K}^{\prime}=\mathbf{R}\mathbf{K}\mathbf{R}^{T},\qquad \boldsymbol{\alpha}^{\prime}_{(2)}=\mathbf{R}\,\mathrm{diag}(\alpha_a,\alpha_c)\,\mathbf{R}^{T} \qquad (19) $$

and the rotated plane-strain block Q′ is read off from C′ by the same assembly rules as in Eq. (11),


$$ Q^{\prime}_{11}=C^{\prime}_{1111},\quad Q^{\prime}_{13}=C^{\prime}_{1133},\quad Q^{\prime}_{15}=C^{\prime}_{1113},\quad Q^{\prime}_{33}=C^{\prime}_{3333},\quad Q^{\prime}_{35}=C^{\prime}_{3313},\quad Q^{\prime}_{55}=C^{\prime}_{1313} \qquad (20) $$

which is the operation verified in test U1 against an independent three-dimensional rank-four implementation (Section 5.1). The b-axis expansion is not touched by the rotation about b, but the constants that carry it into the plane are: the symmetric 2×2 block S = [[C_{12}, C_{25}], [C_{25}, C_{23}]] transforms as S′ = R S R^{T}, i.e. with c = cos φ and s = sin φ,


$$ C^{\prime}_{12}=c^2C_{12}+s^2C_{23}-2cs\,C_{25} \qquad (21) $$


$$ C^{\prime}_{23}=s^2C_{12}+c^2C_{23}+2sc\,C_{25} \qquad (22) $$


$$ C^{\prime}_{25}=cs\left(C_{12}-C_{23}\right)+\left(c^2-s^2\right)C_{25} \qquad (23) $$

so that the thermal-stress vector in the laboratory frame is


$$ \boldsymbol{\beta}^{\prime}(\phi)=\mathbf{Q}^{\prime}(\phi)\,\left(\alpha^{\prime}_{11},\,\alpha^{\prime}_{33},\,2\alpha^{\prime}_{13}\right)+\alpha_b\left(C^{\prime}_{12},\,C^{\prime}_{23},\,C^{\prime}_{25}\right) \qquad (24) $$

the factor 2 in the third slot being the engineering-shear convention. Two consequences are worth noting. First, the thermal shear β′_{5} does not vanish after rotation even though α_{5} = 0 in the crystal frame (Table 3): the rotated in-plane expansion acquires the off-diagonal component α′_{13} = (c² − s²)· 0 + cs(α_{c} − α_{a}) ≠ 0 whenever α_{a} ≠ α_{c}. Second, all three components of S′ enter through the cross term − 2cs C_{25} = -0.312 GPa at φ = 30°, and an error in the sign of that term is invisible at φ = 0 and φ = 90° (where cs = 0) but not at intermediate angles: this is precisely the defect carried by a superseded version of this analysis, which tests U1 and V3 now exclude (Section 5.1).


**Table 3.** Thermal-stress vector in the laboratory frame at four crystal rotations (computed from Table 4 with Eq. (24)).

| φ | β′_{1} (MPa/K) | β′_{3} (MPa/K) | β′_{5} (MPa/K) | ‖β′‖ (MPa/K) |
|---|---|---|---|---|
| 0° | +1.3093 | +1.5796 | +0.0018 | 2.0517 |
| 30° | +1.3753 | +1.5136 | -0.1162 | 2.0484 |
| 45° | +1.4427 | +1.4462 | -0.1352 | 2.0472 |
| 90° | +1.5796 | +1.3093 | -0.0018 | 2.0517 |


### 2.5 Conduction kernels in the Laplace domain

In the Laplace domain (variable s, Re s > 0) all three conduction models used here are the same diffusion operator with a scalar, frequency-dependent conductivity factor, so that the heat equation reads


$$ \nabla\cdot\left(\mathbf{K}\,g(s)\,\nabla\hat\theta\right)=s\left(\rho c_p\,\hat\theta+T_0\,\boldsymbol{\beta}:\hat{\boldsymbol{\epsilon}}\right) \qquad (25) $$

and the momentum equation is unchanged apart from the transform of the inertia term,


$$ \nabla\cdot\boldsymbol{\hat\sigma}=\rho s^2\mathbf{\hat u},\qquad \boldsymbol{\hat\sigma}=\mathbf{Q}\hat{\boldsymbol{\epsilon}}-\boldsymbol{\beta}\hat\theta \qquad (26) $$

with the kernel


$$ g(s)=1\quad\text{(Fourier)},\qquad g(s)=\frac{1}{1+s\tau}\quad\text{(Cattaneo--Vernotte)},\qquad g(s)=\frac{1/2}{1+s\tau_a}+\frac{1/2}{1+s\tau_b}\quad\text{(two-relaxation-time, exploratory)} \qquad (27) $$

the last with τ_{a} = τ/2 and τ_{b} = 2τ, i.e. an effective relaxation time τ_{eff} = ½(τ_{a} + τ_{b}) = 1.25τ. Both non-Fourier kernels are positive real, so the models are passive; the two-relaxation-time kernel is a sensitivity device for asking how much of the thermal-memory effect depends on the shape of the kernel, and it is labelled exploratory wherever it appears because it does not follow from a free-energy functional. In the Fourier limit sτ → 0 all three kernels tend to one, and the small-s expansion


$$ g(s)=1-s\tau_{\mathrm{eff}}+O\left((s\tau)^2\right) \qquad (28) $$

shows that the leading effect of thermal memory is a frequency-dependent reduction of the effective conductivity; in the time domain the same statement is that the flux lags the gradient. The physical motivation for such laws comes from heat conduction at small scales [35,36,37,38], the two-relaxation-time form is the two-term version of the multi-phase-lag kernels [39], and general presentations of the theories are given in [28,40,41].


### 2.6 Boundary and initial conditions

The cavity wall Γ_{c} is traction-free and held at a prescribed temperature; the outer boundary Γ_{R} at R = 80a is clamped and cold:


$$ \boldsymbol{\sigma}\mathbf{n}=\mathbf{0}\;\text{and}\;\theta=p(t)\;\text{on}\;\Gamma_c,\qquad \mathbf{u}=\mathbf{0}\;\text{and}\;\theta=0\;\text{on}\;\Gamma_R \qquad (29) $$

with the outward normal n of the cavity wall (pointing into the solid). The wall temperature is the Gaussian pulse


$$ p(t)=\exp\left[-\left(\frac{t-t_0}{t_w}\right)^2\right],\qquad t_0=2.5\,t_{th},\quad t_w=1.2\,t_{th} \qquad (30) $$

and the medium is quiescent before it: u = θ = 0 and ∂u/∂t = 0 for t < 0. The response computed in Section 6 is therefore the response to a single pulse, not the periodic steady state of a pulse train; the distinction is quantitative, not cosmetic (Section 4.6). Because the wall temperature is a Dirichlet condition, the wall itself shows no thermoelastic feedback by construction, and the finite domain with a clamped outer boundary supports elastic echoes: the first return of the longitudinal wave to the wall occurs at


$$ t_{\mathrm{echo}}=2\left(\frac{R}{a}-1\right)\frac{a}{c_{ref}}=2\left(\frac{R}{a}-1\right)\epsilon\,t_{th} \qquad (31) $$

which is 8.14 t_{th} at a = 10 nm and 1.63 t_{th} at a = 50 nm; the quantity-of-interest window 0 ≤ t ≤ 6 t_{th} is echo-free for a ≤ 10 nm only (Section 7.2).


### 2.7 Dimensionless groups

The thermal time is t_{th} = a²/κ̄ with κ̄ = (det K)^{1/2}/(ρc_{p}) = 3.959×10^{−6} m²/s (t_{th} = 25.3 ps at a = 10 nm). The memory number is Λ = τ/t_{th} = τκ̄/a² (Λ = 0.040, 0.198, 0.792 for τ = 1, 5, 20 ps at 10 nm); the elastic number is ε = κ̄/(c_{ref}a) with c_{ref} = (C_{33}/ρ)^{1/2} = 7686 m/s (ε = 0.0515 at 10 nm); the feedback number is δ = T_{0}‖β‖^{2}/(ρc_{p}C̄) = 1.078×10^{−3}, where C̄ = C_{33} is the stiffness scale of the plane-strain block and the norm in 33 is formed from the in-plane triple (β₁₁, β₃₃, β₁₃) with the shear slot weighted by 2, the same triple that enters the thermal-stress scale γ_T of Section 3; the full tensor contraction β:β would give 1.717×10^{−3}, a factor 1.59 larger, because it also counts the out-of-plane component β₂₂ that the plane-strain class never uses. The triple norm is the in-plane part of the tensor contraction and is therefore invariant under in-plane rotation of the crystal (relative spread 2e-15 over the 360-orientation lattice), so δ is a material constant of this model and not a directional statistic; it is still only an order-of-magnitude criterion for Section 3.4, and the convention is stated for that reason. With the outer boundary at R = 80a the first return of the longitudinal wave to the wall occurs at t_{echo} = 2(R/a − 1)ε t_{th} = 16.3, 8.14, 4.07 and 1.63 t_{th} for a = 5, 10, 20, 50 nm. All stresses are reported per kelvin of wall-temperature amplitude (MPa/K).


$$ t_{th}=\frac{a^2}{\bar\kappa},\qquad \bar\kappa=\frac{\sqrt{\det\mathbf{K}}}{\rho c_p} \qquad (32) $$


$$ \Lambda=\frac{\tau}{t_{th}}=\frac{\tau\bar\kappa}{a^2},\qquad \epsilon=\frac{\bar\kappa}{c_{ref}a},\qquad \delta=\frac{T_0\,\Vert\boldsymbol{\beta}\Vert^{2}}{\rho c_p\bar C} \qquad (33) $$

with c_{ref} = (C_{33}/ρ)^{1/2} = 7686 m/s and C̄ = C_{33} = 347.4 GPa. The three groups have direct physical readings: Λ compares the relaxation time with the time heat takes to diffuse across the cavity, ε compares the thermal diffusion speed κ̄/a with the elastic wave speed (it is the Mach number of diffusion), and δ measures the heat released by the mechanical deformation against the heat stored by the temperature rise, i.e. the strength of the thermoelastic feedback. Numerically κ̄ = 3.959×10^{−6} m²/s, δ = 1.078×10^{−3} and, at the reference size a = 10 nm, ε = 0.0515. The conductivity tensor has eigenvalues 11.72 and 14.50 W/(m K) with the off-diagonal component -0.992 W/(m K), so the conduction is anisotropic by a factor 1.24 and its principal axes are not aligned with the crystallographic a and c axes.


$$ v_T=\frac{\bar\kappa}{a\sqrt{\Lambda}}=\frac{\epsilon\,c_{ref}}{\sqrt{\Lambda}} \qquad (34) $$

which expresses the second-sound speed of Eq. (8) in the dimensionless groups: at fixed ε the thermal wave slows as Λ^{−1/2} when the relaxation time is increased.


### 2.8 Material parameters

The parameters of the study, their values and their status (literature, assumed, hypothetical or design) are collected in Table 4.


**Table 4.** Parameters of the study and their status (classification: literature / assumed / hypothetical / design).

| Parameter | Value | Class | Source |
|---|---|---|---|
| C_{ij} (13 constants) | C11 242.8, C22 343.8, C33 347.4, C44 47.8, C55 88.6, C66 104.0, C12 128.0, C13 160.0, C23 70.9, C15 −1.62, C25 0.36, C35 0.97, C46 5.59 GPa | literature | Adachi et al. [19] (values checked against the paper) |
| K (a–c block) | [[12.13, −0.992], [−0.992, 14.09]] W/(m K); eigenvalues 11.72, 14.50 | literature | Klimm et al. [20] |
| α (a, b, c) | (1.54, 3.37, 3.15)×10^{−6} 1/K; α_{5} = 0 | literature (secondary-quoted); uncertain | Orlandi et al. [21]; at 298 K the synchrotron data [22] give values ≈10× smaller |
| ρ | 5880 kg/m³ | literature | compilations; Klimm et al. [20] use 5.961 g/cm³ at 20 °C |
| c_{p} | 560 J/(kg K) | assumed | reported values 485–537 J/(kg K) [42]; enters only t_{th}, δ and the dimensional labels |
| τ | 1, 5, 20 ps (Λ = 0.04–0.8 at 10 nm) | hypothetical (sensitivity-only) | order-of-magnitude estimates (κ ≈ 15 W/(m K), ρc_{p} = 3.3 MJ/(m³ K), v ≈ 4 km/s): gray τ = 3κ/(ρc_{p}v²) ≈ 0.9 ps; phonons with the longest mean free path (≈ 0.7 µm [43]) τ ≈ 0.2 ns |
| R/a, pulse | 80; t_{0} = 2.5, t_{w} = 1.2 t_{th} | design | fixed in the design note before the production runs |
| a | 5–50 nm (10 nm reference) | design | continuum validity not established (Section 7) |


### 2.9 Quantities of interest

The primary observable is the peak of the absolute wall hoop stress |σ_{θθ}| over the wall and over 0 ≤ t ≤ 6 t_{th} (the window ends before the first elastic echo for a ≤ 10 nm). Two versions are reported: the nodal maximum over the wall nodes and the maximum of the spectrally (trigonometrically) interpolated wall profile; the latter removes the nodal quantisation of the angular maximum, which is of order (Δϑ)² and not negligible on coarse grids. The orientation modulation of the ellipse is A_{φ} = (max_{φ}σ̂ − min_{φ}σ̂)/mean_{φ}σ̂. The thermal-memory deviation is D = max|σ_{CV} − σ_{F}|/max|σ_{F}| over the wall and 0 ≤ t ≤ 6 t_{th} for the same grid and the same inversion plan.


## 3. Analytical results

Three analytical results are used to interpret the computations: a non-dimensionalisation that fixes which dimensionless groups the answer can depend on, a closed-form local-response solution for the circular cavity in an isotropic solid, and an order-of-magnitude bound on the thermoelastic feedback. None of them is a substitute for the computations; they say what the computations must show if the interpretation is right, and they provide two of the reference solutions of Section 5.


### 3.1 Non-dimensionalisation

Let Θ be the amplitude of the wall pulse and choose the expansion scale α_{0} = ‖β‖/C̄, so that the natural stress scale is C̄α_{0}Θ = ‖β‖Θ. With


$$ \mathbf{x}=a\hat{\mathbf{x}},\qquad t=\frac{a^2}{\bar\kappa}\hat t,\qquad \theta=\Theta\hat\theta,\qquad \mathbf{u}=a\alpha_0\Theta\,\hat{\mathbf{u}},\qquad \boldsymbol{\sigma}=\|\boldsymbol{\beta}\|\Theta\,\hat{\boldsymbol{\sigma}} \qquad (35) $$

the strain is ϵ = α_{0}Θϵ̂ with ϵ̂ = ½(∇̂û + ∇̂û^{T}), the constitutive law keeps its form,


$$ \hat{\boldsymbol{\sigma}}=\hat{\mathbf{Q}}\hat{\boldsymbol{\epsilon}}-\hat{\mathbf{b}}\hat\theta,\qquad \hat{\mathbf{Q}}=\frac{\mathbf{Q}}{\bar C},\qquad \hat{\mathbf{b}}=\frac{\boldsymbol{\beta}}{\|\boldsymbol{\beta}\|} \qquad (36) $$

and the two field equations become, using κ̄ = √(det K)/(ρc_{p}) and c_{ref}² = C̄/ρ,


$$ \hat\nabla\cdot\hat{\boldsymbol{\sigma}}=\epsilon^2\,\ddot{\hat{\mathbf{u}}} \qquad (37) $$


$$ \hat\nabla\cdot\left(\hat{\mathbf{K}}\,g\,\hat\nabla\hat\theta\right)=\left(1+\Lambda\frac{\partial}{\partial\hat t}\right)\left(\frac{\partial\hat\theta}{\partial\hat t}+\delta\,\hat{\mathbf{b}}:\dot{\hat{\boldsymbol{\epsilon}}}\right) \qquad (38) $$

with Λ, ε and δ the groups of Eq. (33) and K̂ = K/√(det K). The dimensionless problem therefore depends on the cavity size a only through ε, and the stress per unit wall-temperature amplitude is


$$ \frac{\boldsymbol{\sigma}}{\Theta}=\|\boldsymbol{\beta}\|\,\hat{\boldsymbol{\sigma}}\left(\hat{\mathbf{x}};\,\phi,\chi,\frac{R}{a},\Lambda,\epsilon,\delta,t_0,t_w\right) \qquad (39) $$

so that ‖β‖ = 2.0517 MPa/K is the only material quantity that sets the absolute stress scale; every other material parameter enters through the dimensionless groups, the orientation φ and the shape χ. This is the sense in which the results below are relative statements: the dimensionless response σ̂ is what the computations determine, and the dimensional stress per kelvin is Eq. (39) multiplied by ‖β‖, whose uncertainty is discussed in Section 6.5.


### 3.2 The collapse identity and its two corrections

**Scaling.** For ρ → 0 (quasi-static elasticity) and δ → 0 (no thermoelastic feedback) the temperature problem in the variables (r/a, t/t_{th}) depends only on Λ, the geometry, the crystal orientation and R/a, and the stress per unit wall temperature is a linear functional of θ with no further length scale. The thermal-memory deviation D therefore depends on Λ alone (“collapse”), and any dependence on the cavity size at fixed Λ measures elastic inertia (ε) or feedback (δ).

Setting ε = 0 (quasi-static elasticity) and δ = 0 (no thermoelastic feedback) removes a from the problem entirely: the dimensionless temperature depends on Λ, the geometry and the pulse parameters alone, and the stress is a linear functional of the temperature. Consequently the thermal-memory deviation D of Eq. (80), which is a ratio of two stress histories computed with the same geometry and pulse, depends on Λ alone in that limit,


$$ D=D\left(\Lambda;\,\phi,\chi,\frac{R}{a},t_0,t_w\right)\qquad (\epsilon=0,\;\delta=0) \qquad (40) $$

a statement we call the collapse identity. For the full model the identity can fail only through the two terms that were dropped, and the failure is expected to be small because both ε and δ are small:


$$ D=D_{\mathrm{collapse}}(\Lambda)+c_1(\Lambda)\,\epsilon^{2}+c_2(\Lambda)\,\delta+O(\epsilon^4,\delta^2) \qquad (41) $$

the inertia correction entering as ε² because ε appears squared in Eq. (37). Two runs with the same α = τκ̄/a² but different a test Eq. (40) directly: their D values must agree to within the corrections of Eq. (41). The pair used below is (a = 10 nm, τ = 5 ps) and (a = 20 nm, τ = 20 ps), which have the same Λ = 0.198.


### 3.3 Local response of the circular cavity in an isotropic solid

**Local response of the isotropic circle.** For an isotropic body in quasi-static plane strain with a free wall and a clamped outer boundary, with Lamé constants λ, μ, m = λ + 2μ and γ_{T} = (3λ + 2μ)α, the wall hoop stress is

For an isotropic solid in quasi-static plane strain the circular cavity can be solved in closed form, and the solution shows why the wall stress is insensitive to the conduction law. With radial displacement u(r, t), Lamé constants λ, μ, m = λ + 2μ and γ_{T} = (3λ + 2μ)α, the strains are ϵ_{rr} = u′ and ϵ_{θθ} = u/r, the stresses are


$$ \sigma_{rr}=m\,u^{\prime}+\lambda\frac{u}{r}-\gamma_T\theta,\qquad \sigma_{\theta\theta}=m\frac{u}{r}+\lambda\,u^{\prime}-\gamma_T\theta \qquad (42) $$

and radial equilibrium dσ_{rr}/dr + (σ_{rr} − σ_{θθ})/r = 0 becomes


$$ m\left(u^{\prime\prime}+\frac{u^{\prime}}{r}-\frac{u}{r^2}\right)=\gamma_T\,\theta^{\prime},\qquad \text{i.e.}\qquad m\frac{\mathrm{d}}{\mathrm{d}r}\left[\frac{1}{r}\frac{\mathrm{d}(ru)}{\mathrm{d}r}\right]=\gamma_T\,\theta^{\prime} \qquad (43) $$

Integrating once, with g_{T} = γ_{T}/m and G(r) = ∫_{a}^{r} r′θ(r′, t) dr′,


$$ \frac{1}{r}\frac{\mathrm{d}(ru)}{\mathrm{d}r}=g_T\,\theta+\frac{C_1}{m}\quad\Longrightarrow\quad u(r)=\frac{g_T}{r}G(r)+\frac{C_1}{2m}\frac{r^2-a^2}{r}+\frac{C_2}{r} \qquad (44) $$

where C_{1} and C_{2} are functions of time alone. Substituting Eq. (44) into the first of Eq. (42) gives


$$ \sigma_{rr}=\frac{m+\lambda}{2m}C_1+\frac{m-\lambda}{r^2}\left[-\left(g_T G+C_2\right)+\frac{C_1a^2}{2m}\right] \qquad (45) $$

and the two boundary conditions σ_{rr}(a) = 0 (traction-free wall, where G(a) = 0) and u(R) = 0 (clamped outer boundary) fix the constants:


$$ C_2=\frac{C_1a^2}{m-\lambda},\qquad C_1=-\,g_T\,F(t)\left[\frac{R^2-a^2}{2m}+\frac{a^2}{m-\lambda}\right]^{-1},\qquad F(t)=\int_a^R r\,\theta(r,t)\,\mathrm{d}r \qquad (46) $$

Finally, substituting Eqs. (44) and (46) into the second of Eq. (42) and using m − λ = 2μ and m − μ = λ + μ gives the wall hoop stress


$$ \sigma_{\theta\theta}(a,t)=-\,2\mu\,g_T\,p(t)\;-\;\frac{2(\lambda+m)\,g_T\,F(t)}{R^{2}+(\lambda+m)\,a^{2}/(2\mu)} \qquad (47) $$

which is the closed form used as the isotropic reference in Sections 5 and 6. The first term is local and instantaneous: it is the stress produced by constraining the thermal strain of the material at the wall, and it does not depend on the temperature field away from the wall at all, hence not on the conduction law. The conduction law enters only through F(t), and the ratio of the second term to the first is


$$ \frac{\lambda+m}{\mu}\,\frac{F(t)}{p(t)\,R^{2}}\;\lesssim\;\frac{\lambda+m}{\mu}\,\frac{\delta_{th}}{a}\left(\frac{a}{R}\right)^{2} \qquad (48) $$

where δ_{th} is the thickness of the heated layer; for δ_{th} of order a, R = 80a and the Lamé constants of the isotropic control (λ = 128 GPa, μ = 104 GPa) the prefactor (λ+m)/μ = 4.46 and (a/R)² = 1.6×10^{−4}, so the far-field term is below 10^{−3} of the local term — the wall stress is a local response to 0.1%. For the same constants γ_{T} = 1.5905 MPa/K, g_{T} = 4.734e-06 1/K and


$$ -\,2\mu\,g_T=-\,0.985\;\mathrm{MPa/K} \qquad (49) $$

the number used as the isotropic reference in Sections 5 and 6. The same expression shows what to expect for the anisotropic crystal. There the closed form is not available, because the tangential stiffness at a point of the wall depends on the direction of the tangent, so the wall hoop stress is not a single scalar multiple of p(t); but Eqs. (39) and (47) together say that the wall stress is ‖β‖ times a dimensionless factor of order unity that depends on the stiffness anisotropy and on the angle. That is the form in which the elliptical-cavity results are reported in Section 6.

with F ≲ a², so the second (far-field) term is of order (a/R)² ≈ 10^{−3} of the first: the peak wall stress is, to 0.1%, the local constraint response −2μ g_{T} p(t) (0.985 MPa/K for the Lamé constants of the isotropic control), whatever the heat-conduction law in the bulk. The expression follows from the radial equilibrium equation integrated once and the two boundary conditions; it is used here as an independent reference (Section 5) and as the basis of the interpretation in Section 6.


### 3.4 Bound on the thermoelastic feedback

The coupling term of Eq. (5) is the only nonlinearity-free but still two-way link between the fields: the temperature drives the stress and the strain rate feeds back into the heat equation. Its size relative to the storage term ρc_{p}θ̇ is, from Eq. (38), of order δ times the ratio of the strain rate to the temperature rate in dimensionless units, i.e. of order δ when the two evolve on the same time scale. This motivates the criterion used in Section 6.4: the feedback is negligible if the relative change of the temperature field when the coupling term is removed satisfies


$$ \frac{|\Delta\theta|}{|\theta|}\;\leq\;5\delta \qquad (50) $$

with the factor five a margin chosen before the runs, not fitted to them. For the parameters of Table 4, δ = 1.078e-03 and 5δ = 5.391e-03. A bound of this kind is an order-of-magnitude statement, not a theorem: it is used to decide whether the coupling has to be resolved, and the decision is then checked numerically by switching the coupling off (Section 6.4).


### 3.5 What these results do and do not establish

Equation (39) is exact within the model and fixes the parameter dependence of every number reported below; Eq. (40) is exact in the ε = δ = 0 limit and is used as the null hypothesis for the thermal-memory runs; Eq. (47) is exact for the isotropic circle and is used both as a reference solution and as the interpretation of the wall-stress peak. None of the three is a prediction about β-Ga₂O₃: Eq. (47) is derived for an isotropic solid, Eq. (40) for the quasi-static uncoupled limit, and Eq. (50) is an order-of-magnitude criterion. Their role is to make the numerical experiment interpretable, and to say in advance which outcome would be surprising.


## 4. Numerical method


### 4.1 Spatial discretisation and frequency-domain solver

A body-fitted mapped polar grid with exponential radial clustering towards the cavity (parameter γ = 5) and a uniform periodic parametric angle is used; first derivatives are second-order finite differences with analytic metrics (one-sided at the two boundaries), and the heat and momentum operators are assembled in conservative flux form. For a complex frequency the system A(s) = A_{0} − s²A_{in} + sA_{d} + g(s)A_{lap} is solved by sparse LU with row equilibration and two steps of iterative refinement; the refinement lowers the forward-error floor of the stress from about 10^{−8} to 10^{−14}. Grids are labelled N_{r}×N_{θ}: R48 = 48×96, T48 = 96×48, M = 96×96 (production), R192 = 192×96 and T144 = 96×144.


### 4.2 Body-fitted mapped grid

The annular domain between the cavity and the outer circle R = 80a is mapped from the unit square (ξ, η) ∈ [0, 1] × [0, 2π) by a transfinite map that is radial in the parameter but not in physical space, so that the grid is body-fitted to the ellipse for every χ. The radial coordinate is clustered towards the cavity with the exponential map


$$ \rho(\xi)=\frac{\exp(\gamma\xi)-1}{\exp(\gamma)-1},\qquad \xi\in[0,1],\qquad \frac{\mathrm{d}\rho}{\mathrm{d}\xi}=\frac{\gamma\exp(\gamma\xi)}{\exp(\gamma)-1} \qquad (51) $$

and the physical coordinates are


$$ x=A(\rho)\cos\eta,\qquad y=B(\rho)\sin\eta,\qquad A=a_e+(R-a_e)\rho,\qquad B=b_e+(R-b_e)\rho \qquad (52) $$


$$ a_e=a\sqrt{\chi},\qquad b_e=\frac{a}{\sqrt{\chi}} \qquad (53) $$

so that π a_{e}b_{e} = π a² for every χ: the circle and the ellipse have the same area, which is what makes the comparison of Section 6 a comparison of shape alone. The grid is uniform in ξ and η and periodic in η; with γ = 5 the ratio of the largest to the smallest radial spacing is (147)/5 ≈ 29 for the grids used, i.e. the near-wall layer carries most of the radial resolution. All metric terms are evaluated analytically from the map,


$$ x_\xi=\frac{\mathrm{d}A}{\mathrm{d}\xi}\cos\eta,\quad x_\eta=-A\sin\eta,\quad y_\xi=\frac{\mathrm{d}B}{\mathrm{d}\xi}\sin\eta,\quad y_\eta=B\cos\eta,\quad J=x_\xi y_\eta-x_\eta y_\xi \qquad (54) $$

and physical derivatives follow from the chain rule by inverting


$$ f_x=\frac{y_\eta f_\xi-y_\xi f_\eta}{J},\qquad f_y=\frac{-x_\eta f_\xi+x_\xi f_\eta}{J} \qquad (55) $$

Derivatives in ξ and η are second-order central differences, replaced at the two radial boundaries by the one-sided three-point formulas


$$ \left.\frac{\partial f}{\partial\xi}\right|_{0}=\frac{-3f_0+4f_1-f_2}{2h},\qquad \left.\frac{\partial f}{\partial\xi}\right|_{N_r-1}=\frac{3f_{N_r-1}-4f_{N_r-2}+f_{N_r-3}}{2h} \qquad (56) $$

and central periodic differences in η. The operators D_{x} and D_{y} are assembled as sparse matrices from Eq. (55); the discrete metric identities ∂_{ξ}y_{η} = ∂_{η}y_{ξ} and ∂_{ξ}x_{η} = ∂_{η}x_{ξ} hold exactly at interior nodes, which is what makes a uniform-stress field have exactly zero discrete divergence (the patch test of Section 5.1).


### 4.3 Conservative discretisation of the two operators

The heat and momentum operators are written in contravariant flux form rather than as compositions of first derivatives, because the composition D_{x}D_{x} has a 2h stencil with odd–even decoupling: it possesses spurious null modes that a narrow conservative stencil does not. For any vector field v the identity


$$ J\,\nabla\cdot\mathbf{v}=\frac{\partial}{\partial\xi}\left(v_xy_\eta-v_yx_\eta\right)+\frac{\partial}{\partial\eta}\left(-v_xy_\xi+v_yx_\xi\right) \qquad (57) $$

is exact for analytic metrics, and discretely exact for the discrete metrics of Section 4.1. Applying it to v = −K∇θ gives the thermal operator


$$ J\,\nabla\cdot\left(\mathbf{K}\nabla\theta\right)=\frac{\partial}{\partial\xi}\left(\mathcal{A}\theta_\xi+\mathcal{B}\theta_\eta\right)+\frac{\partial}{\partial\eta}\left(\mathcal{B}\theta_\xi+\mathcal{D}\theta_\eta\right) \qquad (58) $$


$$ \mathcal{A}=\frac{K_{11}y_\eta^2-2K_{13}x_\eta y_\eta+K_{33}x_\eta^2}{J},\qquad \mathcal{D}=\frac{K_{11}y_\xi^2-2K_{13}x_\xi y_\xi+K_{33}x_\xi^2}{J}, \qquad (59) $$


$$ \mathcal{B}=\frac{K_{13}\left(x_\xi y_\eta+x_\eta y_\xi\right)-K_{11}y_\xi y_\eta-K_{33}x_\xi x_\eta}{J} \qquad (60) $$

with the coefficients evaluated at half points as arithmetic averages of the nodal values, and the fluxes differentiated with the same stencils as in Eq. (56); the resulting matrix has the narrow (i ± 1, j ± 1) stencil. The momentum operator is built the same way from the contravariant fluxes


$$ \mathcal{P}_1=y_\eta\sigma_{11}-x_\eta\sigma_{13},\qquad \mathcal{P}_2=y_\eta\sigma_{13}-x_\eta\sigma_{33},\qquad \mathcal{R}_1=-y_\xi\sigma_{11}+x_\xi\sigma_{13},\qquad \mathcal{R}_2=-y_\xi\sigma_{13}+x_\xi\sigma_{33} \qquad (61) $$

through the same identity, with the stresses of Eq. (11) evaluated from the strain components


$$ \epsilon_{11}=u_{1,x},\qquad \epsilon_{33}=u_{3,y},\qquad \gamma_{13}=u_{1,y}+u_{3,x} \qquad (62) $$

computed with Eq. (55). The thermal-stress term is deliberately kept out of the flux: it is assembled as the first-derivative operator


$$ \mathcal{G}_1=\beta_1\frac{\partial}{\partial x}+\beta_5\frac{\partial}{\partial y},\qquad \mathcal{G}_2=\beta_5\frac{\partial}{\partial x}+\beta_3\frac{\partial}{\partial y} \qquad (63) $$

so that a uniform temperature field produces exactly zero body force, which is the V7 patch test of Section 5.1; putting βθ into the flux and differentiating it would leave a residual of the order of the metric-identity error and would destroy that property.


### 4.4 Boundary conditions and extraction of the wall stress

Boundary conditions are imposed by row replacement, not by elimination. On the cavity wall the temperature row is the Dirichlet condition θ = 1 (unit transfer amplitude) and the two momentum rows are the traction conditions built from the first-derivative stress operators


$$ \mathcal{S}_{11}=-\beta_1+Q_{11}\frac{\partial}{\partial x}+Q_{15}\frac{\partial}{\partial y},\qquad \mathcal{S}_{13}=-\beta_5+Q_{15}\frac{\partial}{\partial x}+Q_{55}\frac{\partial}{\partial y},\qquad \mathcal{S}_{33}=-\beta_3+Q_{35}\frac{\partial}{\partial x}+Q_{13}\frac{\partial}{\partial y} \qquad (64) $$

acting on (θ, u_{1}, u_{3}), and combined with the wall normal of the ellipse,


$$ n_x\propto b_e\cos\eta,\qquad n_y\propto a_e\sin\eta,\qquad t_x\propto-a_e\sin\eta,\qquad t_y\propto b_e\cos\eta \qquad (65) $$

into the two traction rows


$$ n_x\mathcal{S}_{11}+n_y\mathcal{S}_{13}=0,\qquad n_x\mathcal{S}_{13}+n_y\mathcal{S}_{33}=0 \qquad (66) $$

On the outer boundary Γ_{R} all three rows are Dirichlet (θ = 0, u_{1} = u_{3} = 0). The wall hoop stress reported throughout the paper is the tangential component of the same stress operators,


$$ \sigma_{\theta\theta}=t_x^2\,\mathcal{S}_{11}+2t_xt_y\,\mathcal{S}_{13}+t_y^2\,\mathcal{S}_{33} \qquad (67) $$

evaluated at the wall nodes; the two traction components of Eq. (66) are monitored in every run and are zero to the solver’s backward error, so the wall is traction-free by construction rather than approximately.


### 4.5 Frequency-domain system

For a single complex frequency the coupled system is solved in one linear system for the vector U = (θ, u_{1}, u_{3}) of 3N_{r}N_{θ} unknowns. With the harmonic convention fields ∝ exp(+iωt) the semi-discrete equations of Section 2.5 read


$$ \mathbf{A}(\omega)\,\mathbf{U}=\mathbf{f},\qquad \mathbf{A}(\omega)=\mathbf{A}_0+\omega^2\mathbf{A}_{in}+i\omega\mathbf{A}_d+g(\omega)\mathbf{A}_{lap} \qquad (68) $$

whose blocks (rows: momentum-1, momentum-2, energy) are


$$ \mathbf{A}_0=\left[-\mathcal{G}_1,\;\mathbf{M}_1,\;\mathbf{M}_2;\;-\mathcal{G}_2,\;\mathbf{M}_2^{\prime},\;\mathbf{M}_3;\;\mathbf{0},\;\mathbf{0},\;\mathbf{0}\right],\qquad \mathbf{A}_{in}=\rho\,\mathrm{diag}(0,1,1) \qquad (69) $$


$$ \mathbf{A}_d=\left[\mathbf{0},\;\mathbf{0},\;\mathbf{0};\;-\rho c_p\mathbf{I},\;-T_0\mathcal{G}_1,\;-T_0\mathcal{G}_2\right],\qquad \mathbf{A}_{lap}=\left[\mathbf{0},\;\mathbf{0},\;\mathbf{0};\;\mathbf{L},\;\mathbf{0},\;\mathbf{0}\right] \qquad (70) $$

with M the conservative momentum operator of Eq. (61), L the conservative thermal operator of Eq. (58) and A the row-replaced boundary rows of Section 4.3; the right-hand side f is nonzero only on the Dirichlet rows of the wall. The complex frequency is the Laplace variable of the inversion plan,


$$ \omega=-\,i\,\frac{s}{t_{th}},\qquad g(\omega)=\frac{1}{1+i\omega\tau} \qquad (71) $$

so that iω = s/t_{th} and ω² = −s²/t_{th}² as required by Eq. (25). Two steps control round-off. First, interior rows are multiplied by the nodal Jacobian J (of order a² in SI units), which brings the PDE rows from O(10^{20}) to O(10^{5}) relative to the unit boundary rows; then each row is scaled to unit maximum modulus. The system is complex symmetric but not Hermitian; it is factorised by sparse LU and improved by two steps of iterative refinement,


$$ \mathbf{U}^{(k+1)}=\mathbf{U}^{(k)}+\mathbf{A}^{-1}\left(\mathbf{f}-\mathbf{A}\mathbf{U}^{(k)}\right),\qquad \eta=\frac{\|\mathbf{f}-\mathbf{A}\mathbf{U}\|_{\infty}}{\left(\|\mathbf{A}\|_{\infty}\|\mathbf{U}\|_{\infty}\right)} \qquad (72) $$

with the backward error η recorded for every solve (frequency-domain formulations of dynamic coupled thermoelasticity with relaxation times go back to [44] and are reviewed in [45]): refinement lowers the floor of the wall stress from about 10^{−8} to 10^{−14} relative, which matters because the quantities of interest in Section 6 are differences of nearly equal stresses.


### 4.6 Single-pulse response by Bromwich inversion

The time-domain response of the quiescent medium to one pulse is obtained from the transfer function H(s) (unit wall amplitude) evaluated on the vertical line Re s = γ_{B} > 0 and inverted with the trapezoidal Bromwich sum [46,47]. With the two-sided Laplace transform of the pulse, P(s) = √π t_{w} exp((s t_{w}/2)² − s t_{0}), and Y = H P,


$$ P(s)=\int_{-\infty}^{\infty}p(t)\,e^{-st}\,\mathrm{d}t=\sqrt{\pi}\,t_w\exp\left[\left(\frac{st_w}{2}\right)^2-s\,t_0\right],\qquad Y(s)=H(s)P(s) \qquad (73) $$

and the response is the Bromwich integral evaluated by the trapezoidal rule on the vertical line Re s = γ_{B},


$$ y(t)=\frac{e^{\gamma_B t}}{T}\left[Y(\gamma_B)+2\,\mathrm{Re}\sum_{k=1}^{K}Y(\gamma_B+i\omega_k)\,e^{i\omega_k t}\right],\qquad \omega_k=\frac{2\pi k}{T} \qquad (74) $$

with T = 20 t_{th}, γ_{B} = 0.9/t_{th}: the alias error is e^{−γ_{B}T} = 1.5×10^{−8}, the Gaussian spectrum is truncated at 10^{−10} (K = 26, i.e. 27 solves per run), and the result is valid for 0 ≤ t ≤ 14.5 t_{th}. The real symmetry H(s̄) = conj H(s) of the undamped real system is used. Because the evaluation line lies at distance γ_{B} from the resonances of the finite undamped domain, no artificial damping is needed. The reconstruction of the wall temperature returns the Gaussian to better than 10^{−8} (10^{−10} for t ≤ 6 t_{th}), a check carried out in every run. A periodic discrete-Fourier synthesis over a window of a few thermal times must not be used for this purpose: it returns the periodic steady state of a pulse train, whose mean wall temperature is t_{w}√π/T = 0.106 of the peak for the parameters above; that mean drives a steady temperature profile out to the outer boundary and adds a static clamped-boundary stress, so the answer is not the single-pulse response this study asks about.

which is Eq. (74) with the plan made explicit. Three errors enter and all three are controlled: (i) the trapezoidal rule periodises the integrand, so the result is the response of a train of pulses of period T plus the alias error e^{−γ_{B}T} = e^{-18} = 1.5e-08 for the plan used; (ii) the sum is truncated at K terms, where K is fixed by requiring the pulse spectrum to have fallen to 1e-10 of its value at s = γ_{B},


$$ K=\left\lceil\frac{T}{2\pi}\sqrt{\gamma_B^2+\frac{4}{t_w^2}\ln\frac{1}{\varepsilon}}\;\right\rceil\;=\;26 \qquad (75) $$

giving 27 solves per run; and (iii) round-off of the inversion grows like e^{γ_{B}t}, which is 221.4 at t = 6t_{th} and 49020.8 at t = 12t_{th}. With T = 20 t_{th} and γ_{B} = 0.9/t_{th} the reconstruction is therefore valid for 0 ≤ t ≤ 14.5 t_{th} for the baseline pulse width t_{w} = 1.2 t_{th}, comfortably beyond the window 0 ≤ t ≤ 6 t_{th} of the quantities of interest. The bound is checked against the stored series of every production run, not only estimated: the reconstructed wall temperature deviates from the imposed Gaussian by at most 1.0e-10 anywhere in 0 ≤ t ≤ 6 t_{th}; over the whole stored window 0 ≤ t ≤ 12 t_{th} the worst case for t_{w} = 1.2 is 3.2e-01, while the widest pulse used in the locality test (t_{w} = 2.4 t_{th}) is the one case whose image term enters inside the stored window (3.2e-01 at t = 12 t_{th}), so that test is read only for peak values, which lie well inside the reported window. The real symmetry H(s̄) = conj H(s) of the undamped real system halves nothing but is used as a consistency check, and because the contour lies at distance γ_{B} from the resonances of the finite undamped domain, no artificial damping is needed. The wall temperature reconstructed from H is compared with the Gaussian in every run (Section 5.1).

Substituting a discrete Fourier synthesis over a window of a few thermal times for Eq. (74) is the mistake this plan replaces: the DFT synthesis returns the periodic steady state of a pulse train of period T: the imposed wall temperature is then not a single pulse but a train with a nonzero mean of t_{w}√π/T = 0.106 of its peak, a steady temperature profile reaches the outer boundary, and the clamped boundary adds a static stress. The question posed in Section 1 is the response to one isolated pulse, which is why the inversion of Eq. (74) is used instead of a windowed Fourier synthesis of the sampled history.

Peaks in time are located on the sampled history and refined by the three-point parabola through the sample maximum,


$$ t_\star=t_i+\frac{\Delta t}{2}\,\frac{y_{i-1}-y_{i+1}}{y_{i-1}-2y_i+y_{i+1}},\qquad y_\star=y_i-\frac{1}{4}\left(y_{i-1}-y_{i+1}\right)\frac{t_\star-t_i}{\Delta t} \qquad (76) $$

which removes the sampling bias of the peak time and amplitude at negligible cost. The alternative inversion algorithms surveyed in [48,49,50,51,52] were not needed here: the Gaussian spectrum decays fast enough for the plain trapezoidal sum on a shifted contour to reach the tolerance above.


### 4.7 Definitions of the quantities of interest

Let σ_{θθ}(η_{j}, t) be the wall hoop stress of Eq. (67) at wall node j. The primary observable is the peak of its modulus over the wall and over the window 0 ≤ t ≤ 6t_{th},


$$ \hat\sigma_{\mathrm{nodal}}=\max_{j}\max_{0\leq t\leq 6t_{th}}|\sigma_{\theta\theta}(\eta_j,t)| \qquad (77) $$

and, to remove the nodal quantisation of the angular maximum — a bias of order (Δη)² that is not negligible on the coarse grids — the same maximum taken over the trigonometric interpolant of the nodal wall profile,


$$ \sigma_{\theta\theta}(\eta,t)=\sum_{k=-N_\theta/2}^{N_\theta/2-1}c_k(t)\,e^{ik\eta},\qquad c_k=\frac{1}{N_\theta}\sum_{j=0}^{N_\theta-1}\sigma_{\theta\theta}(\eta_j,t)\,e^{-ik\eta_j},\qquad \hat\sigma=\max_{\eta}\max_{0\leq t\leq 6t_{th}}|\sigma_{\theta\theta}(\eta,t)| \qquad (78) $$

Both are reported per kelvin of wall-temperature amplitude. The orientation modulation of the ellipse and the thermal-memory deviation of the circle are


$$ A_\phi=\frac{\max_\phi\hat\sigma-\min_\phi\hat\sigma}{\mathrm{mean}_\phi\,\hat\sigma} \qquad (79) $$


$$ D=\frac{\max_{\eta,t}|\sigma_{\theta\theta}^{\mathrm{CV}}-\sigma_{\theta\theta}^{\mathrm{F}}|}{\max_{\eta,t}|\sigma_{\theta\theta}^{\mathrm{F}}|},\qquad 0\leq t\leq 6t_{th} \qquad (80) $$

the latter evaluated on the same grid and with the same inversion plan for the two conduction laws, so that D is a property of the model pair and not of the discretisation. The two-point modulation A_{2} used in the pulse-width test of Section 6.2 is Eq. (79) restricted to two orientations. Because D is a small difference of two nearly equal histories, its numerical accuracy is assessed separately (Section 5.1).


### 4.8 Numerical uncertainty

Grid convergence is assessed with two refinement families at fixed other direction: radial (R48, M, R192; N_{θ} = 96) and angular (T48, M, T144; N_{r} = 96). For each orientation the observed order is obtained from the three levels, the Richardson-extrapolated value is formed with the observed order bounded to [1,3], and the extrapolated value is M + (radial correction) + (angular correction). The numerical uncertainty of the orientation modulation is the largest of the differences between the amplitude on grid M and the amplitudes on R192, T144 and the extrapolated values. The radial clustering parameter was chosen from a mesh-direction study (Section 5.2).

Grid convergence is assessed on two refinement families that vary one direction at a time: radial (R48 = 48×96, M = 96×96, R192 = 192×96) and angular (T48 = 96×48, M = 96×96, T144 = 96×144). For three values f_{1}, f_{2}, f_{3} on meshes with N_{1} < N_{2} < N_{3} directions, the observed order p solves


$$ \frac{f_1-f_2}{f_2-f_3}=\frac{N_1^{-p}-N_2^{-p}}{N_2^{-p}-N_3^{-p}} \qquad (81) $$

(a root is sought numerically; if the differences are not monotone the order is undefined and no extrapolation is made). The order is then clipped to the interval [1,3] — below 1 the observed convergence is not trustworthy, above 3 it is not credible for a second-order scheme — and the error model


$$ f(N)=f_\infty+c\,N^{-p},\qquad c=\frac{f_2-f_3}{N_2^{-p}-N_3^{-p}},\qquad f_\infty=f_3-c\,N_3^{-p} \qquad (82) $$

is calibrated on the two finest levels. The extrapolated value quoted in Section 6 is the production grid M corrected additively by the two one-directional corrections,


$$ f_{\mathrm{ext}}=f_M+\left(f_\infty^{\mathrm{radial}}-f_M\right)+\left(f_\infty^{\mathrm{angular}}-f_M\right) \qquad (83) $$

which assumes the two error components are additive — an assumption, not a result. The numerical uncertainty of the orientation modulation is then


$$ u_{\mathrm{num}}=\max\left(|A_\phi(M)-A_\phi(R192)|,\;|A_\phi(M)-A_\phi(T144)|,\;|A_\phi(M)-A_\phi(\mathrm{ext})|\right) \qquad (84) $$

i.e. the largest of the differences between the production value and the finer or extrapolated estimates, and the detection criterion for the modulation, fixed before the production runs, is A_{φ} > max(5u_{num}, 2%). Following the extrapolation of Eq. (82) goes back to Richardson and Gaunt [53], and in the standard terminology of the verification literature [54,55], these are solution-verification quantities: they bound the discretisation error of the computed solution of the stated model, and say nothing about model error.

Software and AI assistance (Methods disclosure): the finite-difference solver of the preliminary analysis was reviewed, corrected where noted, extended and verified with the assistance of generative-AI coding tools; this is the research-process use referred to in the declaration before the references (Section 5 lists the tests; code, tests and raw data are in the data package). All numbers in this paper are produced by the analysis scripts from stored raw outputs.


## 5. Verification and numerical uncertainty

Verification is separated from validation: every comparison below is against an exact solution or an independent implementation of the same mathematical model (a 1-D axisymmetric Chebyshev solver in the Laplace domain and a time-domain Crank–Nicolson heat solver with the closed-form Lamé stress); none is a comparison with measurements. The suite has 28 tests (27 passed, 0 failed, 1 exploratory). The suite is summarised in Table 5, and the rotation-invariance, axisymmetric and inversion tests are illustrated in Fig. 2. One inherited absolute threshold is exceeded on a grid that is not used for any reported result: at 96×48 with χ = 2 the metric error is 5.028e-03 against the threshold 5e-03 (a 0.6% exceedance of a bound calibrated on that demonstration grid), while the same sequence converges at the expected second order and satisfies the threshold at the production grid; the coarse-grid value is reported in Table 5 rather than suppressed, and the convergence order is asserted as its own case (V0b).


### 5.1 Component and reference tests


**Table 5.** Summary of the verification suite (full table: supplementary material).

| Quantity | Reference | Result |
|---|---|---|
| Rotation of the stiffness/expansion tensors (27 angles) | independent 3-D rank-4 rotation | 1.6e-16 (a sign error in one cross-term would give 1.7e-03) |
| Rotation covariance of the circle (θ, u, wall hoop stress; all lattice φ, complex s) | exact discrete identity | 6.5e-14; peak-stress spread 3.6e-15; a test at φ = 90° alone is blind to the sign error (6e-14 vs 3.0e-03 at 45°) |
| Bromwich inversion: identity / damped oscillator / contour independence | exact / ODE integration / (T, γ_B) change | 6.3e-09 / 5.0e-09 / 4.7e-09 |
| Laplace-domain 1-D solution + inversion vs time-domain solution (quasi-static, uncoupled) | Crank–Nicolson + Lamé | 6.5e-07 |
| Steady log temperature profile; uniform-θ annulus; steady gradient load (wall hoop) | closed forms | V6 3.6e-06 (θ, 192×96); V7 0.11%; V8 0.16% (96×48), 0.04% (192×96), order 1.97 |
| Single pulse, isotropic circle (quasi-static, uncoupled): peak | time-domain reference | 1.16%, 0.27%, 0.07% (48×24, 96×48, 192×96), orders 2.08, 2.05 |
| Dynamic coupled problem (inertia + feedback): wall-hoop peak, Fourier / CV / MCV3 | 1-D spectral + same inversion | 1.21%, 0.29%, 0.07% (Fourier; 48×24, 96×48, 192×96); worst of the four conduction laws at 192×96: 0.08% |
| Quasi-static switch; a = 50 nm (echo-dominated) | 1-D reference | 0.29%; 0.27% (96×48) |
| Metric consistency of the mapped grid (linear field) | order ≥ 1.9 and ≤ 5×10^{−3} at 192×96 | production grid 192×96: ≤ 1.3e-03; observed order 1.96–2.00 on refinement (asserted separately as V0b); the inherited absolute threshold 5e-03 is exceeded by 0.6% at the demonstration grid 96×48 with χ = 2 (5.028e-03); that grid is not used for any reported result |


![Fig. 2](../11_Figures/fig4_verification.png)

**Fig. 2.** (a) Rotation invariance of the circular-cavity peak stress: earlier analysis (rotation-tensor sign error) versus this work; (b) errors of the axisymmetric verification tests versus mesh size; (c) wall-temperature reconstruction by the Bromwich inversion.

The thermal-memory deviation D is a small difference of two nearly equal series, so its accuracy was tested separately: relative to the 1-D reference the error of D is +10.3%, +2.6%, +0.7% (τ = 5 ps) and +21.9%, +5.2%, +1.3% (τ = 20 ps) on the 48×24, 96×48 and 192×96 grids. On the grid used for the circle thermal-memory runs (96×48) D is therefore accurate to a few percent; D changes by +0.6%, +2.3% between that grid and the production grid M for the two members of the equal-Λ pair.


### 5.2 Choice of the radial clustering

The sharp tip of the ellipse (radius of curvature 0.35a at the ends of the major axis) is the most demanding location. A mesh-direction study for the ellipse at φ = 30° (Table 6, Fig. 3) shows that the near-wall radial resolution, not the angular resolution, controls the tip stress: with the clustering of the earlier 96×48 grid (γ = 3.5) doubling N_{r} changes the peak by -8.7% while doubling N_{θ} changes it by +3.0%; increasing the clustering to γ = 5 at fixed 96×48 changes the peak by -11.9%, and γ = 6.5 changes it by only a further -0.7%. The clustering γ = 5 with N_{θ} = 96 was therefore adopted (grid M = 96×96).


![Fig. 3](../11_Figures/fig6a_mesh.png)

**Fig. 3.** Mesh-direction study for the ellipse at φ = 30°: peak wall stress for different meshes and radial clusterings γ (labels: N_r×N_θ).


**Table 6.** Peak wall hoop stress of the ellipse at φ = 30° (MPa/K) for different meshes and radial clusterings γ (interpolated maximum).

| γ | 96×48 | 192×48 | 96×96 | 96×144 | 192×96 |
|---|---|---|---|---|---|
| 3.5 | 1.412 | 1.289 | 1.454 | 1.459 | 1.316 |
| 5.0 | 1.245 | — | 1.262 | — | — |
| 6.5 | 1.236 | — | — | — | — |


### 5.3 Grid convergence of the production quantities


**Table 7.** Peak wall hoop stress of the ellipse (MPa/K, interpolated maximum) on the grid families and the extrapolated value M + radial + angular correction (corrections relative to M).

| φ (deg) | R48 | M | R192 | T48 | T144 | extrapolated | radial corr. | angular corr. |
|---|---|---|---|---|---|---|---|---|
| 0 | 1.1522 | 1.1496 | 1.1490 | 1.1345 | 1.1525 | 1.1543 | -0.07% | 0.48% |
| 30 | 1.3053 | 1.2617 | 1.2455 | 1.2447 | 1.2645 | 1.2409 | -2.04% | 0.39% |
| 60 | 1.1920 | 1.1595 | 1.1476 | 1.1487 | 1.1612 | 1.1439 | -1.60% | 0.26% |
| 90 | 0.9700 | 0.9659 | 0.9642 | 0.9617 | 0.9666 | 0.9640 | -0.32% | 0.12% |
| 120 | 1.2896 | 1.2481 | 1.2334 | 1.2333 | 1.2506 | 1.2299 | -1.82% | 0.36% |
| 150 | 1.3694 | 1.3220 | 1.3048 | 1.3012 | 1.3254 | 1.3010 | -2.03% | 0.44% |

Changing the inversion plan from (T, γ_B) = (20, 0.9) to (32, 0.6) and (16, 1.1) changes the peak stress by 2.9e-10 and 3.5e-10 (series: 4.1e-10, 7.2e-10), i.e. the inversion is not a source of uncertainty at the level of interest.

Because the model is undamped and the outer boundary is finite, elastic echoes are features of the model. Doubling the outer radius (R = 160a, with N_{r} adjusted to keep the near-wall spacing) changes the peak wall stress by 0.29% for a = 10 nm (first echo at 8.1 t_{th}, outside the window) and by 0.18% for a = 50 nm (echo at 1.6 t_{th}, inside the window); the thermal-memory deviation D changes by -5.4% and -3.6%, which is of the size of the grid uncertainty of D (Section 5.1). The finite outer radius is therefore not a significant source of uncertainty for these observables.


### 5.4 What the verification covers and what it does not

The tests of Sections 5.1-5.3 are code-verification and solution-verification tests in the usual sense [54]: they compare the implementation with exact solutions of the same equations (patch tests, steady and 1-D reference solutions, the closed form of Section 3.3) and with independent implementations of the same model (an independent three-dimensional tensor rotation, a 1-D spectral solver, a time-domain Crank-Nicolson integration), and they quantify the discretisation error by grid refinement. What they do not do is check the model itself. The constitutive law, the plane-strain reduction, the relaxation-time kernel, the parameter values of Table 4 and the continuum description at 5-50 nm are inputs, not outputs, of the verification: an error in any of them would leave every test above passing. No comparison with measurements is made anywhere in this paper, so the study is verified and not validated; the physical status of the model is discussed in Section 7.2.


## 6. Results


### 6.1 Circular cavity: orientation-invariant peak and local response

For the circular cavity the peak wall stress is 0.854 MPa/K on grid M, 0.854 MPa/K after radial extrapolation (the error of grid M is 0.03%). It does not depend on the crystal orientation: over the 12 orientations (R48) and the six lattice orientations on grid M the relative spread of the nodal peak is 6.7e-15 and 4.6e-15, against the criterion 10^{−8} (T1: PASS). The invariance is an exact property of the discrete problem for rotations that map the polar grid onto itself, and it is the one place where an implementation error in the rotation of the material tensors shows up unambiguously (Section 5.1).

The stress follows the wall temperature near the peak: at the peak node the ratio σ_{θθ}(t)/p(t) deviates from its value at the peak by at most 1.6% (circle) and 4.3% (ellipse) for 2 ≤ t/t_{th} ≤ 3, and by 1.6% and 15.2% at t = 3.5 t_{th} where p has fallen to 0.5 (Fig. 4b): the delayed, non-local contribution grows after the peak and is larger for the ellipse. This is the signature of the local response derived in Section 3: for the isotropic circle in quasi-static plane strain the Lamé solution gives σ_{θθ}(a,t) = −2μ(γ_{T}/m)p(t) − 2(λ+m)(γ_{T}/m)F(t)/(R² + (λ+m)a²/2μ) with F = ∫ rθ dr, in which the second, far-field term is O((a/R)²) ≈ 10^{−3} of the first. The isotropic control gives 0.981 MPa/K on the 96×48 grid, compared with 0.986 MPa/K from the independent time-domain solution (0.985 MPa/K for its first term).


![Fig. 4](../11_Figures/fig3_wall_profiles.png)

**Fig. 4.** Wall hoop stress of the circular and elliptical cavity. (a) Distribution around the wall at the time of the peak (grid R192, interpolated). (b) Time history at the peak node compared with the wall temperature p(t).


### 6.2 Elliptical cavity: crystal orientation modulates the peak wall stress

For the equal-area ellipse the peak wall stress depends strongly on the crystal orientation (Fig. 5a). On grid M the peak ranges from 0.966 MPa/K (φ = 90°) to 1.322 MPa/K (φ = 150°): an orientation modulation A_{φ} = 29.9%; after radial and angular extrapolation the six-orientation sweep gives A_{φ} = 28.7% with extremes 0.964–1.301 MPa/K. The numerical uncertainty of the amplitude is u_{num} = 1.31% (largest difference between grid M and the finer or extrapolated estimates), the detection threshold max(5u_{num}, 2%) = 6.56%, and the modulation is therefore resolvable (T4). At matched grids the mean ellipse peak on grid M is 1.396 of the circle peak on the same grid (0.854 MPa/K), and the extremes of the 12-orientation sweep are 1.132 and 1.549 of it; comparing the two extrapolated sequences gives 1.373. The orientation of the crystal changes the ellipse peak by a factor of 1.369 between the most and the least favourable orientation.


![Fig. 5](../11_Figures/fig2_phi_sweep.png)

**Fig. 5.** Peak wall hoop stress per kelvin versus crystal rotation φ. (a) Ellipse on the three radial grids and Richardson-extrapolated; circle (horizontal lines, three grids). (b) Same orientations: a superseded version of the analysis (periodic-pulse synthesis, rotation-tensor sign error, coarser wall mesh) compared with this work, kept to show what the recomputation changed.

With isotropic stiffness, conductivity and expansion the ellipse is orientation-independent by symmetry and its peak is 1.494 MPa/K (extrapolated; 1.501 on grid M), 1.530 times the isotropic circle (both on grid 96×96): the shape alone raises the peak by the curvature at the ends of the major axis, and the crystal orientation then modulates the response by the amount given above.

Is the modulation a local effect? If the heated layer were thin compared with the radius of curvature, the response at each wall point would depend only on the local tangent direction; every tangent direction occurs on any convex wall, so the peak over the wall would be orientation-independent for the ellipse as well, and the modulation would vanish. In the present problem the heated layer is not thin: its thickness scales with t_{w}^{1/2} and is comparable to the cavity radius, and the isotropic ellipse already has a peak 1.53 times that of the isotropic circle (both on grid 96×96), which a purely local response could not produce. A pulse-width test (t_{w} = 0.3–2.4 t_{th}; Table 8, Fig. 6) shows that the two-point modulation A_{2} = (σ̂(150°) − σ̂(90°))/mean rises monotonically but only weakly with the pulse width, from 24.8% to 32.0%, while the circle peak varies by 5.3% (peak to peak, relative to the mean; the narrowest pulse is the outlier). The trend is in the direction expected for a growing non-local contribution, but the accessible layer thicknesses (still thicker than the tip radius of curvature, 0.35a) do not reach the thin-layer limit, so the test neither confirms nor excludes a vanishing modulation in that limit; within the studied range the orientation dependence of the ellipse is a non-local effect of the interaction between the heated region and the cavity shape.


**Table 8.** Pulse-width test (grid 96×48, interpolated peaks). t_w = 1.2 is the baseline.

| t_w (t_th) | circle (MPa/K) | ellipse φ=90° (MPa/K) | ellipse φ=150° (MPa/K) | A_2 |
|---|---|---|---|---|
| 0.3 | 0.8990 | 0.9779 | 1.2552 | 24.8% |
| 0.6 | 0.8570 | 0.9488 | 1.2535 | 27.7% |
| 1.2 | 0.8527 | 0.9617 | 1.3012 | 30.0% |
| 2.4 | 0.8579 | 0.9886 | 1.3649 | 32.0% |


![Fig. 6](../11_Figures/fig7_pulse_width.png)

**Fig. 6.** Pulse-width test of the local-response interpretation (96×48). (a) Peak wall stress of the circle and of the ellipse at the baseline minimum and maximum orientations; (b) two-point orientation modulation.


### 6.3 Which anisotropy drives the modulation

To separate the contributions of the three anisotropic tensors the ellipse sweep was repeated with one tensor at a time made isotropic (stiffness from the same Lamé constants as the isotropic control; conductivity equal to the mean eigenvalue; expansion equal to the mean of the three axes) (Table 9, Fig. Fig. 7), and with an expansion set representing the 298 K measurements [22] (α = (0.10, 0.20, 0.20)×10^{−6} 1/K, a sensitivity-only set constructed from the abstract-level statement that α_{b} and α_{c} are about twice α_{a}). The ablations are exploratory and use the 96×48 grid (six orientations; the angular error common to all variants cancels in the comparison).

Removing the expansion anisotropy lowers the modulation to 70% of the baseline, removing the stiffness anisotropy changes it to 152% of the baseline, and removing the conductivity anisotropy changes it to 94%. The orientation modulation therefore results from the competition of the expansion and stiffness anisotropies — the expansion anisotropy alone (isotropic stiffness) would give a larger modulation than the full crystal, the stiffness anisotropy partially compensates it — while the conductivity anisotropy is a minor modifier.


**Table 9.** Mechanism ablations and expansion-set sensitivity for the ellipse at six orientations φ = 0, 30, …, 150°. The unlabelled rows are on grid 96×96 (production); rows labelled (grid 96×48) are the coarser set retained from the earlier design, kept for continuity. A variant is always compared with the baseline of the same grid.

| Variant | Modulation A_φ | Mean peak (MPa/K) | Mean / baseline |
|---|---|---|---|
| full anisotropy (baseline) | 30.1% | 1.1845 | 1.000 |
| full anisotropy (baseline, grid 96×48) | 29.0% | 1.1707 | 1.000 |
| isotropic conductivity | 28.1% | 1.1746 | 0.992 |
| isotropic conductivity (grid 96×48) | 27.2% | 1.1613 | 0.992 |
| isotropic stiffness | 45.6% | 1.4989 | 1.266 |
| isotropic stiffness (grid 96×48) | 45.6% | 1.4869 | 1.270 |
| isotropic expansion (mean α) | 21.0% | 1.2113 | 1.023 |
| isotropic expansion (mean α) (grid 96×48) | 20.8% | 1.1973 | 1.023 |
| expansion set of the 298 K-like data [22] | 31.0% | 0.0746 | 0.063 |
| expansion set of the 298 K-like data [22] (grid 96×48) | 29.9% | 0.0737 | 0.063 |


![Fig. 7](../11_Figures/fig6b_ablation.png)

**Fig. 7.** Orientation modulation of the ellipse peak stress for the baseline and with one anisotropic tensor made isotropic, and for the 298 K-like expansion set (96×48, six orientations).


### 6.4 Thermal memory and thermoelastic feedback

The relaxation-time law changes the wall stress only slightly. Over the studied range (Λ up to 3.2) the thermal-memory deviation of the full stress history is D ≤ 6.4% (largest at a = 5 nm, Λ = 3.2); for a = 10 nm it is 0.11%–1.6% for τ = 1–20 ps, and the peak value itself shifts by at most 1.4% (Table 10, Fig. 8a). The two-relaxation-time kernel (MCV3 in Table 10) is an exploratory variant and is not used in any of the statements below. For a prescribed wall temperature the conduction law enters the wall stress of the isotropic circle only through the weak far-field term of Eq. (47); the anisotropic results are consistent with this. The scaling identity of Section 3 is confirmed to round-off: in the quasi-static, uncoupled limit D depends on Λ alone, and the equal-Λ pair (a = 10 nm, τ = 5 ps) and (a = 20 nm, τ = 20 ps) (Λ = 0.198) gives D = 2.0213e-03 and 2.0213e-03 (residual below 1e-12, T2 quasi-static: SUPPORTED). With elastodynamics the same pair gives 5.291e-03 and 2.562e-03 (residual 52%; T2 dynamic: NOT-SUPPORTED). The collapse in Λ alone therefore fails for the full model at the 25% level, but the failure is entirely due to elastic inertia (including, for a ≥ 20 nm, echoes): the quasi-static runs differ from the dynamic ones only by the inertia term, and the correction is O(ε²), of the same order (10^{−3}) as the thermal-memory effect itself; for Λ ≤ 0.8 the excess of the dynamic over the quasi-static D falls with ε roughly as ε^{1.8–1.9} (5→10 nm) to ε^{2.5–2.7} (10→20 nm), consistent with an O(ε²) leading correction (steeper, ε^{2.7}–ε^{4.5}, at Λ = 3.2). For a = 20 nm and 50 nm the elastic echo returns inside the window, so those dynamic values are properties of the finite domain.


**Table 10.** Thermal-memory deviation D of the circular cavity (anisotropic, φ = 0; grid 96×48, t ≤ 6 t_{th}) and the relative shift of the peak stress for the dynamic runs. MCV3 = two-relaxation-time kernel (exploratory).

| a (nm) | τ (ps) | Λ | ε | D (dynamic) | D (quasi-static) | peak shift |
|---|---|---|---|---|---|---|
| 5 | 20 | 3.167 | 0.1030 | 6.38e-02 | 1.81e-02 | -0.96% |
| 10 | 1 | 0.040 | 0.0515 | 1.09e-03 | 4.01e-04 | +0.09% |
| 10 | 5 | 0.198 | 0.0515 | 5.29e-03 | 2.02e-03 | +0.38% |
| 10 | 20 | 0.792 | 0.0515 | 1.57e-02 | 7.07e-03 | +0.53% |
| 20 | 20 | 0.198 | 0.0258 | 2.56e-03 | 2.02e-03 | +0.12% |
| 50 | 20 | 0.032 | 0.0103 | 2.93e-04 | 3.21e-04 | +0.00% |
| 10 | 5 (MCV3) | 0.198 | 0.0515 | 5.93e-03 | — | +0.36% |
| 10 | 20 (MCV3) | 0.792 | 0.0515 | 1.37e-02 | — | +0.34% |


![Fig. 8](../11_Figures/fig5_memory.png)

**Fig. 8.** Thermal-memory deviation. (a) D versus Λ for dynamic (markers by cavity size) and quasi-static (crosses) runs; (b) wall hoop stress at the peak node for Fourier and CV (τ = 20 ps) conduction and their difference.

Thermoelastic feedback is negligible: with δ = 1.078e-03 the largest relative change of the temperature at the probes r/a ≈ 1.5, 2.0, 3.1 when the energy coupling is removed is 6.19e-04, against the criterion 5δ = 5.39e-03, which the measurement satisfies by a factor 8.7; the peak stress changes by -0.001%. The cavity-wall temperature is Dirichlet-prescribed and shows no feedback by construction.


### 6.5 Sensitivity to the expansion data

Stress per kelvin is proportional to the thermal-stress vector β = Cα. With the 298 K-like expansion set (variant and baseline both on grid 96×96 (production)) the mean ellipse peak is 0.063 of the baseline value (0.0746 MPa/K) while the orientation modulation is 31.0% (baseline 30.1%). The absolute stress scale therefore carries a parameter uncertainty of more than an order of magnitude (a factor 16 between the two expansion sets) through α, whereas the modulation depends on the anisotropy ratios of β and is almost unchanged; only the relative statements of this paper should be used quantitatively.


## 7. Discussion and limitations


### 7.1 What the study shows

- For a prescribed wall temperature the peak wall stress of a circular cavity is, to about 10^{−3} for the isotropic circle (closed form) and to a few percent for the anisotropic crystal (stress/temperature ratio within the window near the peak, pulse-width test), a local, instantaneous constraint response, and it is orientation-invariant. The ellipse breaks this locality: its peak is 1.53 times that of the isotropic circle, and in the crystal it depends on orientation by 29%. The pulse-width test shows only a weak dependence of this modulation on the heated-layer thickness (24.8%–32.0%), so within the accessible range it is a non-local effect of the interaction between the heated region and the cavity shape; whether it vanishes in the thin-layer limit is not tested. Every statement above concerns a relative quantity (a ratio or a modulation); the absolute stress scale carries the parameter uncertainty quantified in Section 6.5.
- Heat-conduction physics (Fourier versus relaxation-time laws) has a bounded and small influence on this observable (evaluated for the circular cavity). Wall hoop stress under a prescribed wall temperature is therefore a poor discriminator of conduction laws; interior stresses, wall heat flux or a prescribed heat flux are the observables to examine.
- The scaling identity (Section 3) turns the hypothesis of collapse in Λ, fixed before the runs, into a statement about the size of two corrections (elastic inertia/echo, thermoelastic feedback); the numerical results quantify both.


### 7.2 Limitations

- **No physical validation.** No transient cavity measurements for β-Ga₂O₃ are known to us; the study is verified, not validated (APPLICABLE — EVIDENCE_UNAVAILABLE).
- **Continuum validity.** Fourier and Cattaneo–Vernotte conduction are continuum models. In β-Ga₂O₃ the gray mean free path is of the order of 3 nm, but heat-carrying phonons with mean free paths up to about 0.7–1 µm exist [43]; cavities of 5–50 nm are therefore outside the demonstrated range of validity of these laws. The dimensionless results (Λ, ε, φ, χ) should be read as properties of the continuum model.
- **Parameters.** The relaxation times are hypothetical (order-of-magnitude estimates: gray ≈ 0.9 ps, longest-mean-free-path phonons ≈ 0.2 ns); c_{p} is assumed (485–540 J/(kg K) reported [42], 560 used) and enters only the time scale; the thermal-expansion coefficients are uncertain by more than an order of magnitude at 298 K [21,22]; α_{5} is set to zero; the b-axis expansion enters through C_{12}, C_{23}, C_{25}.
- **Scope of the runs.** Thermal-memory (relaxation-time) runs and the feedback test were made for the circular cavity; the elliptical cavity was run with Fourier conduction; the mechanism ablations are exploratory.
- **Model scope.** Linear, small-strain, plane strain in the a–c plane; temperature-independent properties; prescribed (Dirichlet) wall temperature; finite undamped domain (R = 80a) with a clamped cold boundary, so elastic echoes are model features for a ≥ 20 nm and the QoI window t ≤ 6 t_{th} is echo-free only for a ≤ 10 nm (doubling R changed the peak by ≤ 0.3% and D by ≤ 5.4%); no thermal boundary resistance, no surface or size effects on the elastic constants.
- **Numerics.** The sharp ends of the ellipse converge slowly: the extrapolation corrections of Table 7 and u_{num} quantify this; a 192×192 grid could not be run within the 2 GB memory of the environment. The mechanism ablations use the 96×48 grid and are exploratory.
- **Method of analysis.** The code and the analysis were developed with AI assistance and verified as described in Section 5; a superseded preliminary version of the analysis from which this study started contained a rotation-tensor sign error, a periodic-pulse-train synthesis and an under-resolved wall mesh; all affected results were recomputed. Independent expert review of the formulation and the claims has not been carried out.


### 7.3 Outlook

Natural extensions are prescribed heat-flux loading, interior-stress and wall-heat-flux observables, three-dimensional and finite-strain effects, temperature-dependent properties, and a comparison with time-resolved thermoreflectance or X-ray measurements of strain around engineered cavities if such data become available.


## 8. Conclusions

- The response of a quiescent medium to one pulse can be obtained from a frequency-domain solver by Bromwich inversion on a shifted contour; it was verified against exact and independent solutions (peak error 0.08% at 192×96 for the axisymmetric dynamic problem, second order), whereas a periodic synthesis over a few thermal times returns a pulse-train steady state.
- The peak wall stress of a circular cavity in monoclinic β-Ga₂O₃ is orientation-invariant to round-off (4.6e-15) and equals 0.854 MPa/K (extrapolated) for the parameters used.
- An equal-area ellipse (axis ratio 2) converts crystal orientation into a peak-stress modulation of 28.7% (grid M: 29.9%; numerical uncertainty 1.3 percentage points), resolvable against the criterion.
- Thermal memory changes the wall-stress history of the circular cavity by at most 6.4% (≤ 1.6% for a ≥ 10 nm) and the peak by at most 1.4% for Λ up to 3.2; D collapses in Λ in the quasi-static limit (residual below 1e-12) and the elastodynamic residual (52%) is an O(ε²) inertia correction to an already small effect; thermoelastic feedback is bounded by 5δ (WITHIN-BOUND).
- The absolute stress scale depends on the thermal-expansion data by more than an order of magnitude and on hypothetical relaxation times; the continuum description is not claimed at the nanometre scale; no experimental validation exists. Results are properties of the verified continuum model.


## 9. Code, data and reproducibility


### 9.1 Code and provenance

The solver, the test suite, the experiment drivers and the analysis scripts are frozen: SHA-256 digests of every file are recorded in `CODE_FREEZE_v2_gate.json` (feab48880c3c1359 for the file itself) and `CODE_FREEZE_v2_blockF.json` (9345b5d402e02f16), and the material model alone is identified by `cg_model.py` (f15578152b6374c1). Every production run records the code version, a checksum of its input configuration, the environment and a digest of its own output in `10_Processed_Data/PRODUCTION_PROVENANCE.csv`, so each number in this paper can be traced to the run that produced it and to the code state that produced the run.

**Code state and re-checks.** The two archived manifests date from 2026-10-01; since they were taken, 7 of the 15 entries of `CODE_FREEZE_v2_gate.json` (cg_bromwich.py, cg_pipeline.py, run_tests.py, analyze_v2.py, make_figures.py, production_matrix.py and run_production_v2.py) have been edited, so the digests recorded for them no longer describe the code. The pipeline was re-run end to end with the code as it now stands and compared with the archived results (`15_Audits/RERUN_COMPARISON.md`): every production run reproduces its archived quantity of interest to zero relative difference and only wall-clock timings differ. On 2026-10-03 the analysis layer was re-run over all 175 stored runs: every pre-existing quantity of `ANALYSIS_V2.json` came out identical (the only value that moves is the number of runs audited), the eight figures and the five archived CSV tables are byte-identical to the archived files, and one further CSV (the ablation set at the production grid) is added. A full production job re-solved in a different build — Python 3.11.2 with NumPy 2.4.6 instead of 3.13.14/2.3.5 — reproduces its stored peak wall stress to 2.7×10⁻¹⁶ relative, i.e. one unit in the last place; the reconstruction of the wall temperature stays within 1.0×10⁻¹⁰ of the imposed pulse over the reported window for every run. Two refreshed manifests record the current code: `CODE_FREEZE_submission_2026_10_03f.json` (27 files, taken before this verification pass) and `CODE_FREEZE_submission_2026_10_03g.json` (05342056f31a8f64, 27 files, all 27 byte-identical to the code as submitted); the second is the one to deposit with the data package, and the earlier manifests are kept unchanged as history.


### 9.2 Data package

The package contains the frozen source (06_Source_Code), the test suite and its machine-readable results (07_Tests), the experiment drivers (08_Experiments), the per-run raw outputs (175 production runs as .npz/.json pairs under 09_Raw_Data, together with the convergence and pulse-width runs), the processed analysis (10_Processed_Data: ANALYSIS_V2.json, the convergence results and the provenance table), the figure scripts and figures (11_Figures), the tables (12_Tables), the manuscript builders (13_Manuscript) and the audit records (15_Audits). The raw outputs store the frequency-domain transfer values as well as the inverted histories, so the quantities of interest can be recomputed without re-solving.


### 9.3 Reproduction

`python3 08_Experiments/reproduce.py` reruns the pipeline end to end (tests, production matrix, convergence runs, analysis, figures, manuscript builders) in the order used here; the individual stages are `07_Tests/run_tests.py`, `08_Experiments/run_production_v2.py`, `run_convergence.py`, `analyze_v2.py`, `make_figures.py`, `13_Manuscript/build_manuscript.py` and `tools/md_to_tex.py`. The environment is recorded in the code-freeze files; the memory required by the finest grid (192×192) exceeded the 2 GB available here, which is why that grid is absent from the convergence families (Section 7.2).


## Acknowledgements

[AUTHOR INPUT REQUIRED: acknowledge any funding, technical help or computing facilities not already named in the Funding statement; omit this section if there is nothing to acknowledge.]


## Declarations

**CRediT authorship contribution statement:** [AUTHOR INPUT REQUIRED].

**Declaration of competing interest:** [AUTHOR INPUT REQUIRED].

**Funding:** [AUTHOR INPUT REQUIRED: name the grant, or state that no funding was received].

**Data availability:** the Python source code, verification suite, per-run raw outputs (npz/json, including the frequency-domain transfer values), analysis and figure scripts and the production matrix are provided in the project data package, whose contents are fixed by the SHA-256 code freeze `CODE_FREEZE_submission_2026_10_03g.json` described in Section 9.1; the package will be deposited in a public repository under the persistent identifier to be deposited at [PUBLIC REPOSITORY/DOI TO BE INSERTED].

**Declaration of Generative AI and AI-assisted technologies in the writing process.** During the preparation of this work the author(s) used a generative-AI assistant (Arena.ai Agent Mode) in order to draft and revise the text and the figure captions, and to check the internal consistency of the manuscript, the calculation companion and the tables. After using this tool the author(s) reviewed and edited the content as needed and take(s) full responsibility for the content of the publication. The research-process use of the same class of tool - reviewing and extending the numerical code and the verification suite, and running the simulations - is recorded with the numerical-methods section, as the journal policy directs. No AI tool generated a physical result and no AI tool produced or selected any number reported here; no AI tool acted without the author(s)' review, and no AI tool is an author or is cited as a source.


## Appendix A. Nomenclature

The symbols used in this paper are listed in Table 11.


**Table 11.** Nomenclature.

| Symbol | Meaning | Unit |
|---|---|---|
| a | cavity radius (circle) / reference length | m |
| χ | ellipse aspect parameter (semi-axes a√χ, a/√χ) | — |
| φ | rotation of the crystal about the b-axis | deg |
| Q, C_{ij} | plane-strain stiffness block, stiffness constants | Pa |
| β = Cα | thermal-stress vector | Pa/K |
| K | conductivity tensor (a–c block) | W/(m K) |
| ρ, c_{p} | density, specific heat | kg/m³, J/(kg K) |
| τ | relaxation time | s |
| τ_{a}, τ_{b}, τ_{eff} | two-relaxation-time kernel parameters (τ/2, 2τ, 1.25τ) | s |
| κ̄, t_{th} | thermal diffusivity, a²/κ̄ | m²/s, s |
| v_{T} | thermal wave speed (κ̄/τ)^{1/2} | m/s |
| Λ = τ/t_{th} | memory number | — |
| ε = κ̄/(c_{ref}a) | elastic number | — |
| δ | thermoelastic coupling number | — |
| c_{ref}, C̄ | wave-speed scale (C̄/ρ)^{1/2}, stiffness scale C_{33} | m/s, Pa |
| α_{0}, Θ | expansion scale ‖β‖/C̄, wall-temperature amplitude | 1/K, K |
| x, t, θ, u, σ, ε | dimensionless counterparts (hats in the text) of the variables of Section 3.1 | — |
| b, Q | normalised thermal-stress vector β/‖β‖ and stiffness Q/C̄ | —, — |
| s, γ_{B}, T | Laplace variable, Bromwich abscissa and period | 1/s, 1/t_{th}, t_{th} |
| K, ω_{k}, ε_{tr} | number of Bromwich terms, their frequencies, spectrum tolerance | —, 1/t_{th}, — |
| H(s), P(s), Y(s) | transfer function, pulse transform, response transform | —, s, — |
| σ̂ | peak wall hoop stress per kelvin | Pa/K |
| A_{φ}, A_{2} | orientation modulation (max − min)/mean, two-point version | — |
| D | thermal-memory deviation | — |
| u_{num}, f₂ | numerical uncertainty, Richardson-extrapolated value | — |
| θ, T_{0} | temperature rise; reference temperature (293 K) | K, K |
| u | displacement in the a–c plane | m |
| ϵ | small-strain tensor (Voigt ϵ_{11}, ϵ_{33}, γ_{13}) | — |
| σ | stress tensor | Pa |
| α | thermal-expansion vector | 1/K |
| R | outer radius of the finite domain (R = 80a) | m |
| p(t), t_{0}, t_{w} | wall-temperature pulse, its centre and width | K, t_{th}, t_{th} |
| F(t), G(r) | radial integrals of θ (a to R, a to r) in Eq. (47) | K m² |
| λ, μ, m, γ_{T}, g_{T} | Lamé constants of the isotropic control; m = λ + 2μ; γ_{T} = (3λ + 2μ)α; g_{T} = γ_{T}/m | Pa, Pa, Pa, Pa/K, 1/K |
| C_{1}, C_{2} | integration constants of Eq. (44) | Pa, Pa m |
| ξ, η, ρ | computational coordinates and the radial map | —, rad, — |
| A, B, J | map functions and Jacobian | m, m, m² |
| A, B, D | contravariant thermal-operator coefficients | W/(m K) |
| γ | radial clustering parameter of the grid | — |
| N_{r} × N_{θ} | grid size (radial × angular) | — |
| ω, g(ω) | angular frequency, conduction kernel | 1/s, — |
| η | backward error of the linear solve | — |


## References

[1] Florence, A.L., Goodier, J.N. Thermal Stress at Spherical Cavities and Circular Holes in Uniform Heat Flow. Journal of Applied Mechanics, 26(2), 293-294 (1959). https://doi.org/10.1115/1.4011999
[2] Florence, A.L., Goodier, J.N. Thermal Stresses Due to Disturbance of Uniform Heat Flow by an Insulated Ovaloid Hole. Journal of Applied Mechanics, 27(4), 635-639 (1960). https://doi.org/10.1115/1.3644074
[3] Chao, C.K., Gao, B. Mixed boundary-value problems of two-dimensional anisotropic thermoelasticity with elliptic boundaries. International Journal of Solids and Structures, 38(34-35), 5975-5994 (2001). https://doi.org/10.1016/s0020-7683(00)00403-0
[4] Abbas, I.A. A Dual Phase Lag Model on Thermoelastic Interaction in an Infinite Fiber-Reinforced Anisotropic Medium with a Circular Hole. Mechanics Based Design of Structures and Machines, 43(4), 501-513 (2015). https://doi.org/10.1080/15397734.2015.1029589
[5] Karmakar, R., Sur, A., Kanoria, M. Generalized thermoelastic problem of an infinite body with a spherical cavity under dual-phase-lags. Journal of Applied Mechanics and Technical Physics, 57(4), 652-665 (2016). https://doi.org/10.1134/s002189441604009x
[6] Abbas, I., Marin, M., Hobiny, A., Vlase, S. Thermal Conductivity Study of an Orthotropic Medium Containing a Cylindrical Cavity. Symmetry, 14(11), 2387 (2022). https://doi.org/10.3390/sym14112387
[7] Jafari, M. Effect of hole geometry on the thermal stress analysis of perforated composite plate under uniform heat flux. Journal of Composite Materials, 53(8), 1079-1095 (2019). https://doi.org/10.1177/0021998318795279
[8] Fahmy, M.A., Alsulami, M.O. Boundary Element and Sensitivity Analysis of Anisotropic Thermoelastic Metal and Alloy Discs with Holes. Materials, 15(5), 1828 (2022). https://doi.org/10.3390/ma15051828
[9] Shiah, Y.C., Liu, T.L. Boundary element analysis of thermal stresses on voids/holes in an infinite/semi-infinite anisotropic plane. Journal of Thermal Stresses, 49(1), 129-145 (2026). https://doi.org/10.1080/01495739.2025.2566326
[10] Chen, F.M., Chao, C.K. Stress Analysis of an Infinite Plate with a Coated Elliptic Hole Under a Remote Uniform Heat Flow. Journal of Thermal Stresses, 31(7), 599-613 (2008). https://doi.org/10.1080/01495730801978547
[11] Fahmy, M.A. Boundary Element Algorithm for Modeling and Simulation of Dual-Phase Lag Bioheat Transfer and Biomechanics of Anisotropic Soft Tissues. International Journal of Applied Mechanics, 10(10), 1850108 (2018). https://doi.org/10.1142/S1758825118501089
[12] Biot, M.A. Thermoelasticity and Irreversible Thermodynamics. Journal of Applied Physics, 27(3), 240-253 (1956). https://doi.org/10.1063/1.1722351
[13] Lord, H.W., Shulman, Y. A generalized dynamical theory of thermoelasticity. Journal of the Mechanics and Physics of Solids, 15(5), 299-309 (1967). https://doi.org/10.1016/0022-5096(67)90024-5
[14] Dhaliwal, R.S., Sherief, H.H. Generalized thermoelasticity for anisotropic media. Quarterly of Applied Mathematics, 38(1), 1-8 (1980). https://doi.org/10.1090/qam/575828
[15] Gurtin, M.E., Pipkin, A.C. A general theory of heat conduction with finite wave speeds. Archive for Rational Mechanics and Analysis, 31(2), 113-126 (1968). https://doi.org/10.1007/BF00281373
[16] Tzou, D.Y. A Unified Field Approach for Heat Conduction From Macro- to Micro-Scales. Journal of Heat Transfer, 117(1), 8-16 (1995). https://doi.org/10.1115/1.2822329
[17] Chandrasekharaiah, D.S. Hyperbolic Thermoelasticity: A Review of Recent Literature. Applied Mechanics Reviews, 51(12), 705-729 (1998). https://doi.org/10.1115/1.3098984
[18] Huang, Y., Yan, L., Wu, H., Yu, Y. New insights on generalized heat conduction and thermoelastic coupling models. Applied Mathematics and Mechanics, 46(8), 1533-1550 (2025). https://doi.org/10.1007/s10483-025-3280-7
[19] Adachi, K., Ogi, H., Takeuchi, N., Nakamura, N., Watanabe, H., Ito, T., et al. Unusual elasticity of monoclinic β-Ga2O3. Journal of Applied Physics, 124(8), 085102 (2018). https://doi.org/10.1063/1.5047017
[20] Klimm, D., Amgalan, B., Ganschow, S., Kwasniewski, A., Galazka, Z., Bickermann, M. The Thermal Conductivity Tensor of β-Ga2O3 from 300 to 1275 K. Crystal Research and Technology, 58(2), 2200204 (2023). https://doi.org/10.1002/crat.202200204
[21] Orlandi, F., Mezzadri, F., Calestani, G., Boschi, F., Fornari, R. Thermal expansion coefficients of β-Ga2O3 single crystals. Applied Physics Express, 8(11), 111101 (2015). https://doi.org/10.7567/apex.8.111101
[22] Cheng, Z., Hanke, M., Galazka, Z., Trampert, A. Thermal expansion of single-crystalline β-Ga2O3 from RT to 1200 K studied by synchrotron-based high resolution x-ray diffraction. Applied Physics Letters, 113(18), 182102 (2018). https://doi.org/10.1063/1.5054265
[23] Pearton, S.J., Yang, J., Cary, P.H., Ren, F., Kim, J., Tadjer, M.J., et al. A review of Ga2O3 materials, processing, and devices. Applied Physics Reviews, 5(1), 011301 (2018). https://doi.org/10.1063/1.5006941
[24] Galazka, Z. Growth of bulk β-Ga2O3 single crystals by the Czochralski method. Journal of Applied Physics, 131(3), 031103 (2022). https://doi.org/10.1063/5.0076962
[25] Green, A.E., Lindsay, K.A. Thermoelasticity. Journal of Elasticity, 2(1), 1-7 (1972). https://doi.org/10.1007/BF00045689
[26] Green, A.E., Naghdi, P.M. Thermoelasticity without energy dissipation. Journal of Elasticity, 31(3), 189-208 (1993). https://doi.org/10.1007/BF00044969
[27] Hetnarski, R.B., Ignaczak, J. GENERALIZED THERMOELASTICITY: CLOSED-FORM SOLUTIONS. Journal of Thermal Stresses, 16(4), 473-498 (1993). https://doi.org/10.1080/01495739308946241
[28] Ignaczak, J., Ostoja-Starzewski, M. Thermoelasticity with Finite Wave Speeds. Oxford University Press (2009). https://doi.org/10.1093/acprof:oso/9780199541645.001.0001
[29] Straughan, B. Heat Waves. Springer, Applied Mathematical Sciences (2011). https://doi.org/10.1007/978-1-4614-0493-4
[30] Chandrasekharaiah, D.S. Thermoelasticity with Second Sound: A Review. Applied Mechanics Reviews, 39(3), 355-376 (1986). https://doi.org/10.1115/1.3143705
[31] Joseph, D.D., Preziosi, L. Heat waves. Reviews of Modern Physics, 61(1), 41-73 (1989). https://doi.org/10.1103/RevModPhys.61.41
[32] Ting, T.T.C. Anisotropic Elasticity. Oxford University Press (1996). https://doi.org/10.1093/oso/9780195074475.001.0001
[33] Hwu, C. Anisotropic Elastic Plates. Springer (2010). https://doi.org/10.1007/978-1-4419-5915-7
[34] Stroh, A.N. Dislocations and Cracks in Anisotropic Elasticity. Philosophical Magazine, 3(30), 625-646 (1958). https://doi.org/10.1080/14786435808565804
[35] Kaminski, W. Hyperbolic Heat Conduction Equation for Materials With a Nonhomogeneous Inner Structure. Journal of Heat Transfer, 112(3), 555-560 (1990). https://doi.org/10.1115/1.2910422
[36] Chen, G. Ballistic-Diffusive Heat-Conduction Equations. Physical Review Letters, 86(11), 2297-2300 (2001). https://doi.org/10.1103/PhysRevLett.86.2297
[37] Majumdar, A. Microscale Heat Conduction in Dielectric Thin Films. Journal of Heat Transfer, 115(1), 7-16 (1993). https://doi.org/10.1115/1.2910673
[38] Tzou, D.Y. Macro- to Microscale Heat Transfer. Wiley (2014). https://doi.org/10.1002/9781118818275
[39] Roy Choudhuri, S.K. On A Thermoelastic Three-Phase-Lag Model. Journal of Thermal Stresses, 30(3), 231-238 (2007). https://doi.org/10.1080/01495730601130919
[40] Hetnarski, R.B., Eslami, M.R. Thermal Stresses—Advanced Theory and Applications. Springer, Solid Mechanics and Its Applications (2019). https://doi.org/10.1007/978-3-030-10436-8
[41] Eslami, M.R., Hetnarski, R.B., Ignaczak, J., Noda, N., Sumi, N., Tanigawa, Y. Theory of Elasticity and Thermal Stresses. Springer, Solid Mechanics and Its Applications (2013). https://doi.org/10.1007/978-94-007-6356-2
[42] Handwerg, M., Mitdank, R., Galazka, Z., Fischer, S.F. Temperature-dependent thermal conductivity and diffusivity of a Mg-doped insulating β-Ga2O3 single crystal along [100], [010] and [001]. Semiconductor Science and Technology, 31(12), 125006 (2016). https://doi.org/10.1088/0268-1242/31/12/125006
[43] Yang, J., Xu, Y., Wang, X., Zhang, X., He, Y., Sun, H. Lattice thermal conductivity of β-, α- and κ- Ga2O3: a first-principles computational study. Applied Physics Express, 17(1), 011001 (2023). https://doi.org/10.35848/1882-0786/ad0ba8
[44] Prevost, J.H., Tao, D. Finite Element Analysis of Dynamic Coupled Thermoelasticity Problems With Relaxation Times. Journal of Applied Mechanics, 50(4), 817-822 (1983). https://doi.org/10.1115/1.3167151
[45] Narayanan, G.V., Beskos, D.E. Numerical operational methods for time-dependent linear problems. International Journal for Numerical Methods in Engineering, 18(12), 1829-1854 (1982). https://doi.org/10.1002/nme.1620181207
[46] Durbin, F. Numerical Inversion of Laplace Transforms: An Efficient Improvement to Dubner and Abate's Method. The Computer Journal, 17(4), 371-376 (1974). https://doi.org/10.1093/comjnl/17.4.371
[47] Crump, K.S. Numerical Inversion of Laplace Transforms Using a Fourier Series Approximation. Journal of the ACM, 23(1), 89-96 (1976). https://doi.org/10.1145/321921.321931
[48] Davies, B., Martin, B. Numerical inversion of the laplace transform: a survey and comparison of methods. Journal of Computational Physics, 33(1), 1-32 (1979). https://doi.org/10.1016/0021-9991(79)90025-1
[49] Weeks, W.T. Numerical Inversion of Laplace Transforms Using Laguerre Functions. Journal of the ACM, 13(3), 419-429 (1966). https://doi.org/10.1145/321341.321351
[50] Talbot, A. The Accurate Numerical Inversion of Laplace Transforms. IMA Journal of Applied Mathematics, 23(1), 97-120 (1979). https://doi.org/10.1093/imamat/23.1.97
[51] Abate, J., Whitt, W. A Unified Framework for Numerically Inverting Laplace Transforms. INFORMS Journal on Computing, 18(4), 408-421 (2006). https://doi.org/10.1287/ijoc.1050.0137
[52] de Hoog, F.R., Knight, J.H., Stokes, A.N. An Improved Method for Numerical Inversion of Laplace Transforms. SIAM Journal on Scientific and Statistical Computing, 3(3), 357-366 (1982). https://doi.org/10.1137/0903022
[53] Richardson, L.F., Gaunt, J.A. VIII. The deferred approach to the limit. Philosophical Transactions of the Royal Society of London Series A, 226, 299-361 (1927). https://doi.org/10.1098/rsta.1927.0008
[54] Oberkampf, W.L., Roy, C.J. Verification and Validation in Scientific Computing. Cambridge University Press (2010). https://doi.org/10.1017/CBO9780511760396
[55] Pelletier, D., Roache, P.J. Verification and Validation of Computational Heat Transfer. In Handbook of Numerical Heat Transfer, 417-442 (2000). https://doi.org/10.1002/9780470172599.ch13
