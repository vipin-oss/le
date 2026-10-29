from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "master"
# The edits in this script were applied during the staged repair. Its final-tree
# guard prevents accidental reapplication to the already edited working copy.
if "No universal generalized-continuum flux is assumed" in (ROOT / "sections/sec10_energy.tex").read_text(encoding="utf-8"):
    print("phase5 repair patch already applied; no changes made")
    raise SystemExit(0)

def sub(rel, old, new, count=1):
    p = ROOT / rel
    s = p.read_text(encoding="utf-8")
    if old not in s:
        if new in s:
            print(f"already updated {rel}")
            return
        raise RuntimeError(f"pattern not found in {rel}: {old[:100]!r}")
    p.write_text(s.replace(old, new, count), encoding="utf-8")
    print(f"updated {rel}")

# Classical total energy and outward-positive flux, derived directly by adding
# (rho vdot_i = sigma_ji,j + rho f_i)*v_i to rho edot = sigma_ij epsdot_ij - q_i,i.
p = "sections/sec03_foundations.tex"
sub(p, r"\mathcal{E} = \frac{1}{2}\rho v_i v_i + e", r"\mathcal{E} = \frac{1}{2}\rho v_i v_i + \rho e")
sub(p,
    "Adding the mechanical power balance \\eqref{eq:3.12} and the internal energy balance \\eqref{eq:3.14} (with $r=0$), and defining the total energy density $\\mathcal{E} = \\frac{1}{2}\\rho v_i v_i + \\rho e$, we obtain:",
    "Adding the mechanical power balance \\eqref{eq:3.12} and the internal-energy balance \\eqref{eq:3.14} (with $r=0$), and defining total energy per unit volume as $\\mathcal{E}=\\frac12\\rho v_i v_i+\\rho e$, gives an outward-positive flux $J_j=q_j-\\sigma_{ji}v_i$:")
sub(p, r"\frac{\partial}{\partial x_j}\left(\sigma_{ji}v_i + q_i\right)", r"\frac{\partial}{\partial x_j}\left(q_j - \sigma_{ji}v_i\right)")
sub(p, r"J_i = \sigma_{ji}v_i + q_i.", r"J_i = q_i - \sigma_{ji}v_i.")
sub(p, r"\item $\sigma_{ji}v_i$: mechanical energy flux (stress power transmitted across a surface per unit area), and", r"\item $-\sigma_{ji}v_i$: mechanical contribution to the outward-positive flux, and")
sub(p, "The mechanical part $\\sigma_{ji}v_i$ represents the rate of work done by tractions on a surface, while the thermal part $q_i$ represents heat conduction.", "With the outward-positive convention, the mechanical contribution is $-\\sigma_{ji}v_i$ and the thermal contribution is $q_i$. Reversing the normal or defining inward-positive flux reverses the signs consistently.")
# Absolute temperature Θ versus increment T.
sub(p, "where $s$ is the specific entropy and $T$ is the absolute temperature. Using the internal energy balance", "where $s$ is specific entropy and $\\Theta$ is absolute temperature. In the linear constitutive equations below, $T=\\Theta-T_0$ denotes the temperature increment. Using the internal-energy balance")
sub(p, r"\rho \dot{s} \geq -\left(\frac{q_i}{T}\right)_{,i} + \frac{\rho r}{T},", r"\rho \dot{s} \geq -\left(\frac{q_i}{\Theta}\right)_{,i} + \frac{\rho r}{\Theta},")
sub(p, r"\sigma_{ij}\dot{\varepsilon}_{ij} - \rho\left(\dot{\psi} + s\dot{T}\right) - \frac{q_i T_{,i}}{T} \geq 0.", r"\sigma_{ij}\dot{\varepsilon}_{ij} - \rho\left(\dot{\psi} + s\dot{T}\right) - \frac{q_i \Theta_{,i}}{\Theta} \geq 0.")
sub(p, r"- \frac{c_v}{2\rho T_0}T^2", r"- \frac{c_v}{2 T_0}T^2")
sub(p, "For a linear isotropic thermoelastic material, the free energy is quadratic in strain and linear in temperature:", "For a linear isotropic thermoelastic material, with temperature increment $T=\\Theta-T_0$ and thermal-stress coefficient $\\beta$ in Pa K$^{-1}$, take the specific Helmholtz free energy:")
sub(p, "$T$ & Temperature increment & K & \\eqref{eq:3.13}", "$T$ & Temperature increment $\\Theta-T_0$ & K & \\eqref{eq:3.20}")
# Unit convention for beta is stated in the constitutive paragraph; the existing notation table has no beta row.

# Lord--Shulman correction and two-way classical coupling; Green--Lindsay is
# one-temperature, temperature-rate dependent, not Chen--Gurtin two-temperature.
p = "sections/sec04_thermoelastic.tex"
sub(p,
    "Equations \\eqref{eq:4.1}--\\eqref{eq:4.2} describe one-way coupling from mechanics to thermal (the $-\\beta T_0\\dot{u}_{i,i}$ term in the heat equation) and one-way coupling from thermal to mechanics (the $-\\beta T_{,i}$ term in the equation of motion). This coupling is the physical origin of thermoelastic wave propagation: mechanical deformation produces temperature changes, and temperature changes produce thermal stresses.",
    "Equations \\eqref{eq:4.1}--\\eqref{eq:4.2} are two-way coupled: volumetric strain rate sources temperature, while the temperature gradient contributes to mechanical stress. In the fully dynamic problem neither field can in general be solved independently; sequential treatments are approximations requiring explicit scale assumptions.")
sub(p,
    "= k\\nabla^2 T (1 + \\tau_0 \\partial_t)\n- \\beta T_0 (\\dot{u}_{i,i} + \\tau_0 \\ddot{u}_{i,i}).",
    "= k\\nabla^2 T\n- \\beta T_0 (\\dot{u}_{i,i} + \\tau_0 \\ddot{u}_{i,i}).")
sub(p, "Green and Lindsay (1972) introduced two relaxation times and two temperatures: the conductive temperature $T$ and the thermodynamic temperature $T^*$.", "Green and Lindsay (1972) introduced a temperature-rate-dependent thermoelastic theory with two relaxation times and a single temperature field. It is distinct from two-temperature thermoelasticity.")
sub(p, r"\rho c_v \dot{T}^* = k\nabla^2 T - \beta T_0 \dot{u}_{i,i},", r"\rho c_v (\dot{T} + \tau_0\ddot{T}) = k\nabla^2 T - \beta T_0(\dot{u}_{i,i}+\tau_0\ddot{u}_{i,i}),")
sub(p, r"\sigma_{ij} = \lambda\varepsilon_{kk}\delta_{ij} + 2\mu\varepsilon_{ij} - \beta T^*\delta_{ij}.", r"\sigma_{ij} = \lambda\varepsilon_{kk}\delta_{ij} + 2\mu\varepsilon_{ij} - \beta(T + \tau_1\dot{T})\delta_{ij}.")
sub(p,
    "\\subsubsection{Dissipationless wave propagation}\n\nFor centrally symmetric bodies, GL theory predicts finite-speed wave propagation without energy dissipation in the classical Fourier sense. The entropy production vanishes for appropriate parameter ranges, making GL theory suitable for modeling conservative thermoelastic waveguides and resonators.",
    "\\subsubsection{Thermal-rate coupling and admissibility}\n\nThe second relaxation time enters the stress through the temperature rate; it does not introduce a second temperature field. Green--Lindsay theory is distinct from Chen--Gurtin two-temperature thermoelasticity. Admissibility and stability restrictions depend on the constitutive convention and parameter regime; no universal dissipationless classification is asserted here without a primary-source derivation.")
sub(p, r"\caption{Historical evolution of thermoelasticity theories. Figure \ref{fig:theory_evolution}.", r"\caption{Historical evolution of thermoelastic theories, shown once in the manuscript.")

# Piezoelectric stiffening sign for the stated constitutive convention; the
# quasistatic electric equations do not support a propagating EM wave.
p = "sections/sec05_multiphysics.tex"
sub(p,
    "and an electromagnetic mode, which is a pure electrostatic oscillation of the potential with vanishing mechanical displacement and which travels at the speed of light in the material. The three speeds are separated by many orders of magnitude in most materials, and this separation is the reason that the electromagnetic mode can usually be separated from the mechanical ones by a modal truncation, whereas the separation of $qP$ from $qS$ is not.",
    "and a quasi-electrostatic potential solution. Under the assumptions used here, $E_i=-\\phi_{,i}$ and $D_{i,i}=0$, Maxwell's displacement-current equation is absent; this solution is not an electromagnetic wave and no speed-of-light mode is implied. A propagating electromagnetic branch requires the full Maxwell system and a stated frequency regime.")
sub(p, r"\bar{c}_{ijkl} = c_{ijkl} - \frac{e_{mij}e_{nkl}}{\kappa_{mn}},", r"\bar{c}_{ijkl} = c_{ijkl} + e_{aij}(\kappa^{-1})_{ab}e_{bkl},")
sub(p,
    "which is the quantity that appears in the coupled wave speeds of Section~\\ref{sec:methods}. The correction is small for weak piezoelectrics such as quartz and large for strong ones such as lead zirconate titanate, and it is the reason that a piezoelectric medium cannot be modelled accurately by adding a piezoelectric source term to an otherwise classical elastic wave calculation: the correction is to the stiffness, and therefore to the wave speed, and not to the amplitude of the excitation alone.",
    "which is the short-circuit/open-circuit stiffness correction after eliminating the quasistatic field under a specified electrical constraint. Its sign is positive for positive-definite permittivity with the stated tensor contraction. The effective modulus depends on the electrical boundary condition; it is not a universal scalar correction.")

# Nonlocal dispersion: frequency saturates; phase and group speeds tend to zero.
p = "sections/sec07_nonlocal.tex"
sub(p,
    "It is worth emphasising what Eq.~\\eqref{eq:7.4} does and does not say, because the corresponding statement in gradient elasticity differs in a way that is experimentally discriminating. The nonlocal dispersion relation \\emph{saturates}: as $k \\to \\infty$ the wave speed tends to zero like $1/k$, so that the high-wave-number branch of the dispersion curve is bounded. A gradient theory produces a dispersion relation in which the squared wave speed decreases \\emph{linearly} in $k^2$ over the range in which the gradient expansion is valid, and the two mechanisms therefore predict measurably different wave speeds at the same wave number even when they are fitted to agree in the long-wave limit.",
    "For Eq.~\\eqref{eq:7.4}, the phase speed tends to zero as $k\\to\\infty$, while the angular frequency $\\omega(k)=c_0 k/\\sqrt{1+\\xi^2k^2}$ approaches the finite limit $c_0/\\xi$; it is frequency, not phase speed, that saturates. The group velocity is $d\\omega/dk=c_0(1+\\xi^2k^2)^{-3/2}$ and tends to zero. By contrast, the positive strain-gradient law in Eq.~\\eqref{eq:7.3} gives $c_{\\rm ph}^2=c_0^2(1+\\ell^2 k^2)$ for a one-dimensional bar, so it stiffens and phase speed increases. Gradient-inertia variants can behave differently; the model form must accompany any comparison.")
sub(p,
    "A review that presented nonlocal elasticity purely as a remedy for the breakdown of classical elasticity would give a misleading impression, because the remedy has a well-documented cost. The differential form of Eq.~\\eqref{eq:7.2} raises the order of the governing equation, and the resulting initial-value problem is not well posed in the sense of Hadamard: the number of required initial conditions grows with the order of the equation, and the growth of the solution with the wave number is unbounded \\cite{Eringen1983}. In the frequency domain, the same statement appears as the unbounded increase of the wave number with frequency, so that the group velocity grows without bound and the causal cone is not preserved.",
    "The differential nonlocal model must be distinguished from the integral constitutive law from which it is sometimes obtained. Its boundary-value formulation can exhibit paradoxes under particular geometries and boundary conditions, including the cantilever-bending paradox discussed in the nonlocal-beam literature; that does not establish a bulk-wave group velocity that grows without bound. For Eq.~\\eqref{eq:7.4}, both frequency and group velocity are bounded. Well-posedness claims must specify operator, domain, boundary conditions and function space; no universal Hadamard-instability claim is made here.")
# The corrected paragraph already distinguishes strain-gradient stiffness from gradient-inertia variants.

# Energy: total energy uses rho e; outward flux is q - sigma v; remove a
# dimensionally incorrect universal internal-variable flux assertion.
p = "sections/sec10_energy.tex"
sub(p, r"\mathcal{E} = \frac{1}{2}\rho v_i v_i + e + \mathcal{E}_{\mathrm{coup}},", r"\mathcal{E} = \frac{1}{2}\rho v_i v_i + \rho e + \mathcal{E}_{\mathrm{coup}},")
sub(p, "For classical coupled thermoelasticity, adding the mechanical power balance and the internal energy balance yields", "For classical coupled thermoelasticity, adding the mechanical power and internal-energy balances yields the outward-positive flux")
sub(p, r"J_i = \sigma_{ji}v_i + q_i,", r"J_i = q_i - \sigma_{ji}v_i,")
sub(p,
    "For time-harmonic fields, the average energy flux is obtained from the time-average identity\n\n\\begin{equation}\n\\avg{J_i}_t = \\frac{1}{2}\\Re\\left[\\hat{\\sigma}_{ji}\\hat{v}_i^*\\right],\n\\label{eq:10.4}\n\\end{equation}\nin which the complex conjugate appears because the physical field is the real part of the complex amplitude.",
    "For time-harmonic mechanical fields, the outward-positive mean flux is $\\langle J_i\\rangle=q_{i,\\rm av}-\\frac12\\Re[\\hat{\\sigma}_{ji}\\hat{v}_i^*]$. The factor $1/2$ and complex conjugate follow from the time-average identity; $q_{i,\\rm av}$ is the separately evaluated mean heat flux (zero for a purely oscillatory perturbation about a uniform reference state).")
start="The systematic way to write the energy balance for a generalized theory is the internal-variable formulation."
end="\\subsubsection{Verified piezothermoelastic energy flux}"
s=(ROOT/p).read_text(encoding="utf-8")
if start in s:
    i=s.index(start); j=s.index(end,i)
    s=s[:i]+("The first-law balance retains the boundary power terms for a specified constitutive theory. What changes between generalized theories is the stored free energy and dissipation, which must be derived from that theory's state variables and evolution laws. There is no universal additional flux term $-\\sum_\\alpha Y^\\alpha\\dot z^\\alpha$: this has units of power per volume, not energy flux, unless an additional spatial transport structure is derived. We therefore do not use a generic internal-variable flux formula; family-specific identities are supplied only when the free energy, evolution law and boundary terms have been established, otherwise the result is marked conditional or open.\n\n")+s[j:]
(ROOT/p).write_text(s,encoding="utf-8")
sub(p,
    "The third is the most frequently violated in practice: evanescent modes carry a normal flux that is not zero, so omitting them from the modal sums produces an apparent deficit that is sometimes attributed to absorption \\cite{Gupta2026HeatMap}.",
    "For a single lossless, purely evanescent partial wave, the time-averaged normal flux is zero under the usual real-coefficient assumptions. Cross terms between partial waves can contribute to the total field flux; attenuating modes in dissipative media require separate treatment. Modal accounting must be performed on the complete field.")
sub(p,
    "All the generalized families considered here---Lord--Shulman, Green--Lindsay, Green--Naghdi types~II and~III, the dual and triple phase-lag theories, Moore--Gibson--Thompson, and the memory-dependent formulation---predict a finite thermal wave speed, and thereby address the infinite propagation speed paradox of classical Fourier heat conduction",
    "Thermal propagation depends on the constitutive family and parameters. Fourier conduction is parabolic with instantaneous mathematical support; Lord--Shulman and Green--Naghdi type II have hyperbolic thermal branches under their standard positive-parameter assumptions; Green--Naghdi type III is dissipative and its propagation/support properties depend on the selected equations; phase-lag, MGT, MDD and fractional models require their own stability and kernel conditions. “Finite thermal wave speed” is not applied uniformly to all generalized families")

# Sequential-solution description in Section 8: dynamic mechanical equation is hyperbolic.
p="sections/sec08_mathematical_methods.tex"
s=(ROOT/p).read_text(encoding="utf-8")
old="The classical problem is solved in two sequential stages: the mechanical problem is elliptic and the thermal problem is parabolic, and the two can be solved in sequence. The mechanical waves are unaffected by thermal coupling to leading order."
new="The fully dynamic classical thermoelastic initial-boundary-value problem is coupled: momentum balance is hyperbolic, heat conduction is parabolic, and thermoelastic coupling acts in both directions. Sequential solution is an approximation (for example, quasi-static mechanics, weak coupling or a separated-timescale limit), not the exact dynamic structure. In the harmonic longitudinal problem, eliminating temperature gives a frequency-dependent effective modulus and therefore thermoelastic dispersion and attenuation of the compressional branch. The coupling parameter is of order $\\epsilon=\\beta^2T_0/[\\rho c_v(\\lambda+2\\mu)]$ under the isotropic linear convention; quantitative claims require the geometry and parameter assumptions of the cited wave analyses."
if old in s:
    s=s.replace(old,new)
else:
    # locate likely exact subsection and replace the two known incorrect phrases independently
    if "solved in two sequential stages" in s:
        a=s.index("The classical problem is solved in two sequential stages")
        b=s.find("\n\\subsection",a)
        if b<0: b=len(s)
        s=s[:a]+new+s[b:]
    else:
        print("NOTE: sec08 alleged sentence not found")
(ROOT/p).write_text(s,encoding="utf-8")
print("phase5 source repairs done")
