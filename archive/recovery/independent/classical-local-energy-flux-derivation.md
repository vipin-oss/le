# Independent classical local-energy-flux derivation

**Scope:** a conditional balance-law derivation, not a check of the absent R3 manuscript and not evidence for a generalized/nonlocal/piezoelectric flux formula.

## Assumptions and sign convention

Use a local Cauchy continuum with mass density \(\rho\), velocity \(v_i\), symmetric tension-positive Cauchy stress \(\sigma_{ij}\), specific internal energy \(e\), specific kinetic energy \(k=\tfrac12 v_i v_i\), body force per unit mass \(b_i\), heat supply per unit mass \(r\), and heat flux \(q_j\) positive in the outward direction. Assume no mass diffusion, couple stresses, independent microstructure, electromagnetic power, gradient/nonlocal interactions, or singular bulk sources. The balances are

\[
\rho\dot v_i=\sigma_{ij,j}+\rho b_i,
\qquad
\rho\dot e=\sigma_{ij}D_{ij}-q_{j,j}+\rho r,
\]

where \(D_{ij}=\tfrac12(v_{i,j}+v_{j,i})\). Stress symmetry gives \(\sigma_{ij}D_{ij}=\sigma_{ij}v_{i,j}\).

## Derivation

Multiply momentum balance by \(v_i\). Since \(\rho\dot k=\rho v_i\dot v_i\), the product rule yields

\[
\rho\dot k
=v_i\sigma_{ij,j}+\rho b_i v_i
=(v_i\sigma_{ij})_{,j}-\sigma_{ij}v_{i,j}+\rho b_i v_i.
\]

Add the internal-energy balance. The stress-power terms cancel:

\[
\rho\dot{(e+k)}=(v_i\sigma_{ij}-q_j)_{,j}+\rho(b_i v_i+r).
\]

Thus, in conservative form,

\[
\rho\dot E+F_{j,j}=\rho(b_i v_i+r),
\qquad E=e+k,
\qquad \boxed{F_j=q_j-v_i\sigma_{ij}}.
\]

With symmetric stress this is often written \(F=q-\sigma v\). The sign follows from the stated momentum equation, tension-positive stress, and outward-positive \(q\); changing traction/stress conventions changes the displayed sign accordingly. This \(F\) is the **total** local energy flux. It is not the same object as the conductive heat flux \(q\).

## Fixed-interface consequence

Let a stationary internal interface have unit normal \(n\) directed from the minus side to the plus side. If there is no surface storage, surface energy flux, or surface source, the pillbox balance gives

\[
\llbracket F\cdot n\rrbracket=0,
\quad\text{so}\quad
\llbracket q\cdot n\rrbracket=\llbracket v_i\sigma_{ij}n_j\rrbracket.
\]

Only if velocity and traction are continuous (for example, a perfectly bonded interface satisfying \(\llbracket v\rrbracket=0\) and \(\llbracket\sigma n\rrbracket=0\)) does the mechanical-power jump vanish and reduce this to \(\llbracket q\cdot n\rrbracket=0\). Slip, imperfect contact, interfacial dissipation/storage, moving interfaces, or singular surface sources require their own surface balance; the simple continuity statement must not be carried over without those terms.

## Dimensional check and limits

- \(q\) and \(\sigma v\) both have units \(\mathrm{W\,m^{-2}}\).
- \(F_{j,j}\) and \(\rho\dot E\) both have units \(\mathrm{W\,m^{-3}}\).
- The derivation is classical/local only. Gradient or nonlocal continua can have higher-order stress power and additional energetic fluxes. Piezoelectric/electromagnetic formulations can include field energy and electrical/polarization power. No generalized or interface-partition formula is inferred here.

## Verification status

Derived directly from the two stated balances and the product rule. No manuscript equation was available for comparison; no primary-source equation was inspected for this derivation. No symbolic software check was run. This note must not be entered as a claim mapping or used to change a protected equation, status, or interface convention.
