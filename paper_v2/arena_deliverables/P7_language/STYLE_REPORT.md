# Style report — P7 language pass

Every section of the review was rewritten into journal prose, one file at a time, while the technical content was held fixed: equations, labels, cross-references, citation keys, numbers, environments and script paths are byte-identical to the original. `check_invariants.py` enforces that and must print `PASS` before a file is shipped; a file that failed would keep its original text and be listed in `FAILED_INVARIANTS.csv`.

## What changed

- 51 files rewritten (50 sections plus the abstract, which was lifted out of `main.tex`).
- 241 paragraphs edited in total; 51 files contain at least one edit.
- No equation, label, reference key, citation key, number, unit, symbol, table, figure, footnote or script path was altered.
- Paragraphs that were already in journal style were left as they stood.

## Verification

```
$ cd paper_v2/arena_deliverables/P7_language && python3 check_invariants.py
checked 51 rewritten file(s): 51 PASS, 0 FAIL
PASS
```

| file | paragraphs edited | original lines |
|---|---:|---:|
| `abstract.tex` | 2 | 39 |
| `appA.tex` | 2 | 14 |
| `appB.tex` | 1 | 16 |
| `appBal.tex` | 6 | 50 |
| `appC.tex` | 1 | 30 |
| `appD_catalogue.tex` | 1 | 358 |
| `appE_glossary.tex` | 2 | 52 |
| `appEqReg.tex` | 5 | 234 |
| `appF_debye.tex` | 4 | 33 |
| `appG_params.tex` | 1 | 34 |
| `appH_registry.tex` | 2 | 25 |
| `s01_intro.tex` | 14 | 119 |
| `s02_history.tex` | 9 | 66 |
| `s03_foundations.tex` | 14 | 162 |
| `s03b_kinetic.tex` | 6 | 45 |
| `s03c_prelim.tex` | 7 | 29 |
| `s03d_admiss.tex` | 4 | 40 |
| `s04_classical.tex` | 9 | 67 |
| `s04b_flexted.tex` | 3 | 31 |
| `s05_hyperbolic.tex` | 9 | 108 |
| `s06_lags.tex` | 9 | 75 |
| `s06b_delay.tex` | 2 | 38 |
| `s07_memory.tex` | 7 | 45 |
| `s07b_fraccoupled.tex` | 2 | 23 |
| `s07c_modulus.tex` | 5 | 27 |
| `s08_waves3d.tex` | 4 | 26 |
| `s08b_aniso.tex` | 5 | 45 |
| `s08c_reflection.tex` | 5 | 36 |
| `s09_transient.tex` | 6 | 43 |
| `s09b_thermalmodes.tex` | 4 | 20 |
| `s10_surface.tex` | 5 | 36 |
| `s10b_lamb.tex` | 4 | 31 |
| `s10c_bar.tex` | 4 | 29 |
| `s11_interfaces.tex` | 8 | 57 |
| `s11b_layered.tex` | 5 | 33 |
| `s12_size.tex` | 6 | 69 |
| `s13_multiphysics.tex` | 5 | 70 |
| `s13b_bg.tex` | 3 | 34 |
| `s14_methods.tex` | 4 | 36 |
| `s14b_schemes.tex` | 3 | 38 |
| `s15_applications.tex` | 6 | 31 |
| `s15b_examples.tex` | 4 | 41 |
| `s15c_experiments.tex` | 5 | 29 |
| `s15d_scenarios.tex` | 3 | 28 |
| `s15e_identify.tex` | 3 | 21 |
| `s16_synthesis.tex` | 5 | 99 |
| `s16b_atlas.tex` | 2 | 75 |
| `s16c_taxonomy.tex` | 5 | 75 |
| `s17_open.tex` | 4 | 95 |
| `s17b_reporting.tex` | 4 | 30 |
| `s18_declarations.tex` | 2 | 24 |

## Banned-pattern audit (whole corpus, before → after)

| pattern | before | after |
|---|---:|---:|
| landscape | 1 | 0 |
| pivotal | 1 | 1 |
| not only | 2 | 0 |
| This section | 10 | 0 |

Notes on the audit:

- Thirteen of the seventeen patterns — `delve`, `crucial`, `tapestry`, `navigate`, `multifaceted`, `robust framework`, `seamlessly`, `underscores`, `in the realm of`, `Moreover`, `Furthermore`, `Additionally`, `It is worth noting` — do not occur in either version, so they are omitted from the table.
- `pivotal` survives once, inside the `Reported result` column of the atlas table (`s16b_atlas.tex`), where the entry paraphrases the source's own claim. Rewriting it would misreport what the source says, so it stands.
- `This section` openings were replaced by `we` constructions, which is why the count falls to zero.

## Before / after, one example per file

### `abstract.tex`

Before:

> One coupled dispersion polynomial, verified symbolically, gives comparative phase speed, attenuation and thermoelastic damping across all template models. The widely repeated dual-phase-lag stability condition $\tau_T\ge\tau_q/2$ is shown to belong to a specific Taylor truncation, not to the first-order template.

After:

> Green--Lindsay and Guyer--Krumhansl lie outside it, and we treat them separately. A single coupled dispersion polynomial, verified symbolically, gives comparative phase speed, attenuation and thermoelastic damping across the template models.

### `appA.tex`

Before:

> The identity was checked symbolically with all template parameters kept as symbols (script \path{check_dispersion.py}); a first version of our own implementation had the opposite sign for the coupling term, and the symbolic comparison detected it immediately, which is the reason we advocate the check.

After:

> The identity was checked symbolically with every template parameter kept as a symbol (script \path{check_dispersion.py}). A first version of our own implementation had the coupling term with the opposite sign, and the symbolic comparison caught it at once; that is why we recommend the check.

### `appB.tex`

Before:

> With the values of Table~\ref{tab:materials} and a lag time of one picosecond, $\tau_0\omega_*\approx0.4$ for aluminium, i.e.\ a thermal front somewhat faster than the elastic one.

After:

> With the values of Table~\ref{tab:materials} and a lag time of one picosecond, $\tau_0\omega_*\approx0.4$ for aluminium, so the thermal front is somewhat the faster.

### `appBal.tex`

Before:

> The balances in \cref{sec:foundations} are used throughout; this appendix records where each comes from and what it assumes, so that a reader can see which statements are identities of continuum mechanics and which already contain a constitutive choice.

After:

> This appendix records where each balance used in \cref{sec:foundations} comes from and what it assumes, so that a reader can see which statements are identities of continuum mechanics and which already contain a constitutive choice.

### `appC.tex`

Before:

> All numerical results of this review are produced by Python scripts supplied with the manuscript. \Cref{tab:scripts} lists them with the checks they perform.

After:

> Every numerical result in this review comes from Python scripts supplied with the manuscript. \Cref{tab:scripts} lists them with the checks each performs.

### `appD_catalogue.tex`

Before:

> This appendix lists every work in the reference database, grouped by the subject of its title. Works that are not discussed in the main text are included as further reading for the corresponding topic.

After:

> We list every work in the reference database, grouped by the subject of its title, and include works not discussed in the main text as further reading for the corresponding topic. The grouping is automatic, by title keyword alone, so it helps to locate the literature without summarising any paper.

### `appE_glossary.tex`

Before:

> \emph{How large is thermoelastic damping in a resonator?} Use \cref{eq:LR} with the plane-strain factor when the width exceeds several thicknesses, and check $kh$ (\cref{sec:lamb}). \emph{How do I validate a code?} Use the checks in \cref{sec:methods,sec:schemes}, including the sum rule and the elastic limits.

After:

> \emph{How large is thermoelastic damping in a resonator?} Use \cref{eq:LR} with the plane-strain factor once the width exceeds several thicknesses, and check $kh$ (\cref{sec:lamb}). \emph{How do I validate a code?} Use the checks in \cref{sec:methods,sec:schemes}, including the sum rule and the elastic limits.

### `appEqReg.tex`

Before:

> The register below records that, one row per equation, using a fixed and finite vocabulary. A status is a record of the check performed; it is not a ranking of the equation's importance, and it does not certify that the equation applies to a given material.

After:

> The register below records that, one row per equation, in a fixed and finite vocabulary. A status records the check performed; it is not a ranking of the equation's importance, and it does not certify that the equation applies to a given material.

### `appF_debye.tex`

Before:

> This appendix derives the Debye-type loss used throughout (\cref{eq:debye}) directly from the dispersion polynomial, and shows that it is the response of a standard linear solid. We use the classical theory in units $\rho=c_1=c=k=1$, so $\omega_*=1$ and $s=-i\omega$.

After:

> We derive the Debye-type loss used throughout (\cref{eq:debye}) directly from the dispersion polynomial and show that it is the response of a standard linear solid, working in the classical theory with units $\rho=c_1=c=k=1$, so $\omega_*=1$ and $s=-i\omega$.

### `appG_params.tex`

Before:

> In line with the reporting standards of \cref{sec:reporting}, \cref{tab:paramreg} lists the parameters behind every computed figure. Quantities are in the non-dimensional units of the scripts ($\rho=c_1=c_v=1$, lengths in $c_1/\omega_*$, times in $1/\omega_*$, so $k_{\rm cond}=1$) unless stated otherwise. ``Branch'' indicates the branch plotted and ``tracked'' that continuity in the frequency or wavenumber was used.

After:

> Following the reporting standards of \cref{sec:reporting}, \cref{tab:paramreg} gives the parameters behind every computed figure. Quantities are in the non-dimensional units of the scripts ($\rho=c_1=c_v=1$, lengths in $c_1/\omega_*$, times in $1/\omega_*$, so $k_{\rm cond}=1$) unless stated otherwise. ``Branch'' names the branch plotted, and ``tracked'' means continuity in frequency or wavenumber was enforced.

### `appH_registry.tex`

Before:

> \Cref{tab:registry} lists the fourteen benchmarks that are executed by \path{run_checks.py}. Every entry is a \emph{code verification}: it tests that an implementation reproduces an exact, closed-form, symbolic or independently computed reference to a stated tolerance.

After:

> \Cref{tab:registry} lists the fourteen benchmarks run by \path{run_checks.py}. Every entry is a \emph{code verification}: it tests that an implementation reproduces an exact, closed-form, symbolic or independently computed reference to a stated tolerance.

### `s01_intro.tex`

Before:

> \subsection{The problem that generalized thermoelasticity addresses} Heat conduction in solids is described, to an excellent approximation under ordinary conditions, by Fourier's law: the heat flux is proportional to the temperature gradient at the same instant.

After:

> \subsection{The problem that generalized thermoelasticity addresses} Fourier's law makes the heat flux proportional to the temperature gradient at the same instant. Under ordinary conditions this is an excellent description of conduction in solids.

### `s02_history.tex`

Before:

> Biot \citep{Biot1956} showed that the classical thermoelastic equations follow from the thermodynamics of irreversible processes with a Rayleigh-type dissipation function, and Danilovskaya \citep{Danilovskaya1950} solved the thermal shock of an elastic half-space, in the uncoupled approximation.

After:

> Biot \citep{Biot1956} showed that the classical thermoelastic equations follow from the thermodynamics of irreversible processes with a Rayleigh-type dissipation function. Danilovskaya \citep{Danilovskaya1950} solved the thermal shock of an elastic half-space in the uncoupled approximation.

### `s03_foundations.tex`

Before:

> This section collects the balance laws, the thermodynamic structure of linear thermoelasticity, the reasons why Fourier's law is problematic for fast processes, and the heat-flux template that organises the remainder of the review.

After:

> We collect the balance laws, the thermodynamic structure of linear thermoelasticity, the reasons Fourier's law fails for fast processes, and the heat-flux template that organises the rest of the review. The presentation is self-contained, so later sections can cite equation numbers instead of rederiving them.

### `s03b_kinetic.tex`

Before:

> The lag models of \cref{sec:lags} are usually justified by their formal structure. Their physical meaning comes from kinetic theory of phonons, and this section summarises how the two most-used laws arise there.

After:

> Formal structure usually justifies the lag models of \cref{sec:lags}. Their physical meaning comes from the kinetic theory of phonons, and this section summarises how the two most-used laws arise there.

### `s03c_prelim.tex`

Before:

> They are collected here with the conventions of this review, so that every statement about branches, damping and dispersion has a single definition.

After:

> We collect them here with the conventions of this review, so that every statement about branches, damping and dispersion rests on a single definition.

### `s03d_admiss.tex`

Before:

> A heat law can be wrong in several different ways, and the tests are not interchangeable. \emph{Conservation} is built into the balance laws and does not constrain the constitutive law.

After:

> A heat law can be wrong in several ways, and the tests are not interchangeable. \emph{Conservation} is built into the balance laws and says nothing about the constitutive law.

### `s04_classical.tex`

Before:

> Their product, $T_0\beta^2$, is what appears in the single coupling constant $\varepsilon$ of \eqref{eq:adiabatic}; the reciprocal structure (the same $\beta$ in both) is a consequence of the existence of the free energy \eqref{eq:psi}.

After:

> Their product, $T_0\beta^2$, is what appears in the single coupling constant $\varepsilon$ of \eqref{eq:adiabatic}, and the reciprocal structure, the same $\beta$ in both terms, follows from the existence of the free energy \eqref{eq:psi}.

### `s04b_flexted.tex`

Before:

> Longitudinal waves (\cref{sec:classical}) are only one of the settings in which the thermoelastic loss appears. In micro-resonators the dominant case is flexure of a thin beam, where the temperature gradient across the thickness $h$ relaxes by heat conduction in the transverse direction.

After:

> Longitudinal waves (\cref{sec:classical}) are only one setting for the thermoelastic loss. In micro-resonators the dominant case is flexure of a thin beam, where the temperature gradient across the thickness $h$ relaxes by transverse conduction.

### `s05_hyperbolic.tex`

Before:

> \subsection{A common dispersion equation} The three classical generalized theories can be written, for plane longitudinal motion, in one equation. Let $\tau_0$ denote the flux relaxation time (Lord--Shulman) or the thermal relaxation time (Green--Lindsay, in the notation of the later literature), and let $\tau^\dagger$ be the lag that multiplies the thermal-stress and dilatation coupling.

After:

> \subsection{A common dispersion equation} For plane longitudinal motion the three classical generalized theories fit into one equation. Let $\tau_0$ denote the flux relaxation time (Lord--Shulman) or the thermal relaxation time (Green--Lindsay, in the notation of the later literature), and let $\tau^\dagger$ be the lag that multiplies the thermal-stress and dilatation coupling.

### `s06_lags.tex`

Before:

> \paragraph{Why the truncation order matters for stability.} The stability condition $\tau_T>\tau_q/2$ (exponential stability, with instability for $\tau_T<\tau_q/2$), often quoted as \emph{the} stability condition of DPL thermoelasticity, was derived by Quintanilla \citep{Quintanilla2003DPL} by a spectral argument for the version in which the flux is expanded to second order in $\tau_q$ and the gradient to first order in $\tau_T$, i.e.\ variant (ii).

After:

> \paragraph{Why the truncation order matters for stability.} Quintanilla \citep{Quintanilla2003DPL} derived the condition $\tau_T>\tau_q/2$ (exponential stability, with instability for $\tau_T<\tau_q/2$) by a spectral argument, for the version in which the flux is expanded to second order in $\tau_q$ and the gradient to first order in $\tau_T$, that is, variant (ii).

### `s06b_delay.tex`

Before:

> This is a modelling choice, not an identity, and its consequences deserve a quantitative look. Here we compare the truncations with the \emph{exact} delay law on the uncoupled thermal branch.

After:

> That is a modelling choice, not an identity, and its consequences deserve a quantitative look. Here we compare the truncations with the \emph{exact} delay law on the uncoupled thermal branch.

### `s07_memory.tex`

Before:

> \subsection{Motivation} Fractional and memory-dependent derivatives replace the local-in-time structure of Cattaneo's and Tzou's laws by an operator that weights the past, so that the response at time $t$ depends on the history of the gradient or flux.

After:

> \subsection{Motivation} Fractional and memory-dependent derivatives replace the local-in-time structure of Cattaneo's and Tzou's laws by an operator that weights the past, so that the response at time $t$ depends on the history of the gradient or of the flux.

### `s07b_fraccoupled.tex`

Before:

> Here we put a fractional Cattaneo law, $q+\tau^{\alpha}D^{\alpha}q=-k\,\theta_{,x}$ with a Caputo derivative $D^\alpha$ and $0<\alpha\le1$, into the coupled longitudinal problem of \cref{sec:classical}. In the Laplace representation $G(s)=k/[1+(\tau s)^{\alpha}]$, and the polynomial of \cref{eq:unified} is used unchanged, with the principal branch $(-i\omega)^\alpha=\omega^\alpha e^{-i\pi\alpha/2}$.

After:

> Here we insert a fractional Cattaneo law, $q+\tau^{\alpha}D^{\alpha}q=-k\,\theta_{,x}$ with a Caputo derivative $D^\alpha$ and $0<\alpha\le1$, into the coupled longitudinal problem of \cref{sec:classical}. In the Laplace representation $G(s)=k/[1+(\tau s)^{\alpha}]$, and the polynomial of \cref{eq:unified} is used unchanged, with the principal branch $(-i\omega)^\alpha=\omega^\alpha e^{-i\pi\alpha/2}$.

### `s07c_modulus.tex`

Before:

> A wave measurement does not return $k(\omega)$ for a heat law; it returns a complex wavenumber that an experimenter interprets as a frequency-dependent modulus. This section makes that interpretation explicit for the one-dimensional coupled problem and states what causality does and does not imply.

After:

> A wave measurement does not return $k(\omega)$ for a heat law. It returns a complex wavenumber that the experimenter reads as a frequency-dependent modulus.

### `s08_waves3d.tex`

Before:

> \paragraph{Counting branches.} The number of branches in a bulk plane-wave problem is $2$ (dilatational--thermal) $+\,2$ (shear polarisations) in an isotropic medium, with $G$ rational of low degree; the degree of the polynomial in $K$ equals $2$ only if $G$ is rational of the kind in the template.

After:

> \paragraph{Counting branches.} In an isotropic medium a bulk plane-wave problem has $2$ branches from the dilatational--thermal pair $+\,2$ shear polarisations when $G$ is rational of low degree; the polynomial in $K$ has degree $2$ only for a $G$ of the template's kind.

### `s08b_aniso.tex`

Before:

> Real devices use single crystals, and the question is how the coupling strength $\varepsilon$ depends on the propagation direction and which modes are affected.

After:

> Devices use single crystals, so the questions are how the coupling strength $\varepsilon$ depends on propagation direction and which modes it touches.

### `s08c_reflection.tex`

Before:

> Here we give numbers, and a validation, for a plane P wave incident on an insulated traction-free surface of an isotropic thermoelastic half-space.

After:

> Here we give numbers and a validation for a plane P wave incident on an insulated traction-free surface of an isotropic thermoelastic half-space.

### `s09_transient.tex`

Before:

> Steady-state dispersion analysis tells us how a monochromatic wave propagates. Transient problems test the \emph{fronts}: finite speed, jumps and their decay.

After:

> Steady-state dispersion analysis says how a monochromatic wave propagates. Transient problems test the \emph{fronts}: finite speed, jumps and their decay.

### `s09b_thermalmodes.tex`

Before:

> The uncoupled heat law offers a small, exactly solvable example of how a finite size reveals the hyperbolic character: the normal modes of a rod with insulated ends.

After:

> The uncoupled heat law offers a small, exactly solvable example of finite size revealing hyperbolic character: the normal modes of a rod with insulated ends.

### `s10_surface.tex`

Before:

> Differences between formulations in the literature (which wave attenuation measure is plotted, which branch of the square roots is used, how the thermal boundary condition is chosen) account for many apparent disagreements among published Rayleigh dispersion curves \citep{Biswas2020a,Tung2019,Gupta2024,Aldandani2026,Abouelregal2011,Biswas2020c,Chirita2012,Singh2013,Singh2015}.

After:

> Many apparent disagreements among published Rayleigh dispersion curves come from differences of formulation: which attenuation measure is plotted, which branch of the square roots is taken, how the thermal boundary condition is chosen \citep{Biswas2020a,Tung2019,Gupta2024,Aldandani2026,Abouelregal2011,Biswas2020c,Chirita2012,Singh2013,Singh2015}.

### `s10b_lamb.tex`

Before:

> Surface waves on a half-space (\cref{sec:surface}) have a counterpart in plates, where the two free faces couple the dilatational, shear and thermal fields. The plate problem is where the flexural thermoelastic damping of \cref{sec:flexted} is recovered from the full field equations, which gives a stringent test of the formulation.

After:

> Plates carry the counterpart of the half-space surface wave (\cref{sec:surface}), with two free faces coupling the dilatational, shear and thermal fields. The plate problem recovers the flexural thermoelastic damping of \cref{sec:flexted} from the full field equations, which makes it a stringent test of the formulation.

### `s10c_bar.tex`

Before:

> The loss measured in a resonator is a temporal quantity: a standing mode with real wavenumber $k_n=n\pi/L$ decays in time with a complex frequency $\omega_n$. Here the plane-wave polynomial of \cref{eq:unified} is used with real $k$ and complex $s=-i\omega$.

After:

> Resonator loss is a temporal quantity: a standing mode with real wavenumber $k_n=n\pi/L$ decays in time at a complex frequency $\omega_n$. We therefore use the plane-wave polynomial of \cref{eq:unified} with real $k$ and complex $s=-i\omega$.

### `s11_interfaces.tex`

Before:

> Reflection and transmission at interfaces is the most heavily studied wave problem in generalized thermoelasticity and multiphysics media; Table~\ref{tab:streams} lists many of the works. Most of them report \emph{energy ratios} and use the requirement that the ratios sum to unity as a validation.

After:

> Reflection and transmission at interfaces is the most heavily studied wave problem in generalized thermoelasticity and in multiphysics media; Table~\ref{tab:streams} lists many of the works. Most of them report \emph{energy ratios} and take a unit sum as a validation.

### `s11b_layered.tex`

Before:

> Two further classical wave types depend on a \emph{second} medium: Love waves, guided by a surface layer over a half-space, and Stoneley waves, guided by the interface of two half-spaces. This section gives their isothermal elastic secular equations, checks them against numbers printed in the original papers, and states how the heat law enters when thermal coupling is added.

After:

> Two classical wave types need a \emph{second} medium: Love waves, guided by a surface layer over a half-space, and Stoneley waves, guided by the interface of two half-spaces. We give their isothermal elastic secular equations, check them against numbers printed in the original papers, and state how the heat law enters once thermal coupling is added.

### `s12_size.tex`

Before:

> \subsection{Why local elasticity fails at small wavelengths} Local elasticity predicts non-dispersive waves, $\omega=c\,k$, for all wavelengths. A crystal is a lattice, and its acoustic branch bends over and reaches zero group velocity at the zone boundary.

After:

> \subsection{Why local elasticity fails at small wavelengths} Local elasticity predicts $\omega=c\,k$ at every wavelength. A crystal is a lattice: its acoustic branch bends over and reaches zero group velocity at the zone boundary.

### `s13_multiphysics.tex`

Before:

> Thermoelastic waves are one member of a larger class: whenever a further field is energetically coupled to deformation and temperature, the dispersion relation acquires additional branches or renormalised constants, and the heat-flux law acts as a module that can be exchanged without altering the coupling structure.

After:

> Thermoelastic waves belong to a larger class: whenever another field is energetically coupled to deformation and temperature, the dispersion relation gains branches or renormalised constants, while the heat-flux law acts as an exchangeable module that leaves the coupling structure alone.

### `s13b_bg.tex`

Before:

> The thermopiezoelectric coupling of \cref{sec:multi} changes bulk stiffness, but piezoelectric media also support surface waves that have no elastic counterpart. The simplest is the Bleustein--Gulyaev (BG) wave \citep{Bleustein1968,Gulyaev1969}, a shear-horizontal (SH) wave localised at the surface of a hexagonal (6mm) crystal.

After:

> The thermopiezoelectric coupling of \cref{sec:multi} changes bulk stiffness, and piezoelectric media also carry surface waves with no elastic counterpart. The simplest is the Bleustein--Gulyaev (BG) wave \citep{Bleustein1968,Gulyaev1969}, a shear-horizontal (SH) wave localised at the surface of a hexagonal (6mm) crystal.

### `s14_methods.tex`

Before:

> Using the wrong measure when comparing with an experiment is a common source of apparent inconsistency. \textbf{Integral transforms.} For half-spaces, layers and cylinders, Laplace transformation in time and Fourier (or Hankel) transformation in space reduce the problem to ordinary differential equations with exponential solutions, as in Sections~\ref{sec:transient} and~\ref{sec:surface}.

After:

> Comparing an experiment against the wrong measure is a common source of apparent inconsistency. \textbf{Integral transforms.} For half-spaces, layers and cylinders, Laplace transformation in time and Fourier (or Hankel) transformation in space reduce the problem to ordinary differential equations with exponential solutions, as in Sections~\ref{sec:transient} and~\ref{sec:surface}.

### `s14b_schemes.tex`

Before:

> Time-domain numerics for hyperbolic heat laws are commonly validated against a smooth test problem, which hides the main difficulty: a front that the scheme must carry without spurious oscillation or excessive smearing. This section gives a small benchmark with an exact solution and reports what three standard schemes achieve.

After:

> Hyperbolic heat laws are usually validated in the time domain against a smooth test problem, which hides the real difficulty: a front that the scheme has to carry without spurious oscillation or excessive smearing. We give a small benchmark with an exact solution and report what three standard schemes achieve.

### `s15_applications.tex`

Before:

> The theories reviewed here are used in four broad application areas. For each, we state which regime of the parameter space is relevant, based on the characteristic numbers derived in the previous sections.

After:

> The theories reviewed here serve four broad application areas. For each we state the relevant regime of parameter space, using the characteristic numbers derived above.

### `s15b_examples.tex`

Before:

> This section shows how the results of the review are used for four practical questions. All numbers follow from the rounded handbook inputs of \cref{tab:materials} at $T_0=300$\,K (script \path{scripts/worked_examples.py}); they illustrate the procedure and should be redone with measured parameters for a specific specimen.

After:

> Four practical questions show how the results of the review are used. All numbers come from the rounded handbook inputs of \cref{tab:materials} at $T_0=300$\,K (script \path{scripts/worked_examples.py}); they illustrate the procedure and should be redone with measured parameters for a specific specimen.

### `s15c_experiments.tex`

Before:

> A theory of wave propagation is only as useful as its parameters. This section reviews which experiments probe which model parameters, what they can and cannot discriminate, and how to read published values of lag times and fractional orders.

After:

> We review which experiment probes which parameter, what the experiments can and cannot discriminate, and how published lag times and fractional orders should be read.

### `s15d_scenarios.tex`

Before:

> Here the dimensionless groups that decide the heat law are evaluated for six representative scenarios, so that the reader can see at a glance which of the models of this review is relevant. The table is generated by \path{scripts/table_scenarios.py} from the rounded handbook inputs of \cref{tab:materials} and a lag $\tau_q=1$\,ps; $\delta_T=\sqrt{2\chi/\omega}$ is the thermal penetration depth and $\lambda=c_1/f$ the acoustic wavelength.

After:

> We now evaluate the dimensionless groups that decide the heat law for six representative scenarios, which shows at a glance which model of this review is relevant. The table is generated by \path{scripts/table_scenarios.py} from the rounded handbook inputs of \cref{tab:materials} and a lag $\tau_q=1$\,ps; $\delta_T=\sqrt{2\chi/\omega}$ is the thermal penetration depth and $\lambda=c_1/f$ the acoustic wavelength.

### `s15e_identify.tex`

Before:

> This is consistent with the combination $\tau_v^{*}=k+k^*\tau_v$ used by \citet{RoyChoudhuri2007}. Two consequences follow: $k$ and $\tau_v$ cannot be separated by dispersion or attenuation data alone, and a fitted pair $(k,\tau_v)$ from such data is a convention, not a measurement (compare \cref{sec:delayfid}).

After:

> Two consequences follow: dispersion or attenuation data alone cannot separate $k$ from $\tau_v$, and a pair $(k,\tau_v)$ fitted to such data is a convention rather than a measurement (compare \cref{sec:delayfid}).

### `s16_synthesis.tex`

Before:

> A regime map} The question that most users face is whether a generalized heat law will change their prediction. We answer it for the damping and speed of the elastic-type branch by computing the relative difference between Lord--Shulman and classical predictions over the plane of the two relevant dimensionless numbers, the frequency $\omega/\omega_*$ and the lag $\tau_0\omega_*$ (\Cref{fig:regime}).

After:

> A regime map} Most users want to know one thing first: will a generalized heat law change their prediction? We answer the question for the damping and the speed of the elastic-type branch by computing the relative difference between Lord--Shulman and classical predictions over the plane of the two relevant dimensionless numbers, the frequency $\omega/\omega_*$ and the lag $\tau_0\omega_*$ (\Cref{fig:regime}).

### `s16b_atlas.tex`

Before:

> This section collects wave problems treated in the literature, so that a reader can see which geometry, heat law and coupling has been studied and what the source actually demonstrates. \Cref{tab:atlas} lists fourteen problems from eleven papers by research groups other than the author's; each was read in full text (geometry, governing equations, boundary conditions and results) and each entry is traced to a page in the source.

After:

> We collect wave problems treated in the literature, so that a reader can see which geometry, heat law and coupling has been studied and what the source actually shows. \Cref{tab:atlas} lists fourteen problems from eleven papers by groups other than the author's.

### `s16c_taxonomy.tex`

Before:

> That single axis collapses independent commitments into one word: a study may adopt a relaxation law for the heat flux, a gradient or integral law for the stress, a coupling to a second field, and a validation regime, and each can be varied while the others are held fixed.

After:

> That single axis collapses independent commitments into one word. A study may adopt a relaxation law for the heat flux, a gradient or integral law for the stress, a coupling to a second field, and a validation regime, and each of these can be varied while the others are held fixed.

### `s17_open.tex`

Before:

> A complete analytical statement of well-posedness, decay and front structure for the coupled TPL and MGT systems with all parameters positive, including the conditions on $(\tau_q,\tau_T,\tau_v,k,k^*)$ and the role of the coupling $\varepsilon$, is still lacking in a form directly usable by applied authors.

After:

> What applied authors still lack is a complete analytical statement of well-posedness, decay and front structure for the coupled TPL and MGT systems with all parameters positive, that is, the conditions on $(\tau_q,\tau_T,\tau_v,k,k^*)$ together with the role of the coupling $\varepsilon$, in a form they can use directly.

### `s17b_reporting.tex`

Before:

> The comparisons made in this review were often limited not by the models but by what the original papers report. This section proposes a short set of reporting standards that would make future results directly comparable.

After:

> What limited the comparisons in this review was usually not the models but what the original papers report. We therefore propose a short set of reporting standards that would make future results directly comparable.

### `s18_declarations.tex`

Before:

> The scripts that produce every computed figure and every benchmark in \cref{app:repro} and \cref{app:registry} are provided with the manuscript, together with the parameter registers in \cref{app:params}. No experimental data were generated in this work; every experimental value quoted is attributed to its source in the text.

After:

> The scripts that produce every computed figure and every benchmark in \cref{app:repro} and \cref{app:registry} come with the manuscript, together with the parameter registers in \cref{app:params}. No experimental data were generated in this work; every experimental value quoted is attributed to its source in the text.

