# Proposal (DRAFT, not sent) — Multiphysics Wave Mechanics in Generalized Continua

**Proposed section:** regular review (invited route). The manuscript is currently about 123 pages; the author must decide whether this proposal describes that full scope or a narrower one.

**Proposed editor:** [to be selected by the author from the journal's editorial board].

## 1. Motivation

Generalized continuum theories (relaxation and phase-lag heat conduction, memory-dependent and fractional operators, nonlocal and gradient elasticity, and coupled electrical, porous, and micropolar fields) are used for wave problems in thermoelastic and multiphysics media. The governing equations differ in their state variables, fluxes, and admissibility conditions, and a family label does not fix them. A review that compares these models without stating each one's balance laws and scope invites confusion about which claims hold.

## 2. Proposed scope

The review organizes representative models by constitutive mechanism, governing structure, predicted modes, and the questions they leave open. It separates three kinds of statement:

- statements checked against source equations or pages (class A in the internal ledger);
- statements established by a reproducible symbolic derivation or numerical check (class V); and
- statements that remain model-dependent, disputed, or open (class B or C).

## 3. What the verified core establishes

Each item below is limited to the model stated in the manuscript.

1. **Exact energy balance.** For the classical Eulerian balance, the outward total-energy flux is F_i = q_i − σ_ij v_j + E v_i. The reduced flux q_i − σ_ij v_j is used only for a stated first-order small-amplitude balance. The symbolic derivation is recorded as OCL-480.
2. **Reduction map.** Displayed substitutions between Lord–Shulman, dual- and triple-phase-lag, Moore–Gibson–Thompson candidate, fractional-endpoint, and nonlocal forms are checked symbolically, together with negative controls for the most plausible incorrect substitutions (OCL-470 to OCL-473, OCL-509).
3. **Interface energy partition.** For a one-dimensional welded lossless longitudinal interface, the reflected and transmitted fluxes, the interface loss, and the mode-count consistency are checked symbolically (OCL-465 to OCL-468).
4. **Nonlocal dispersion.** For the displayed Helmholtz-type nonlocal bar, the phase speed reduces to the local value at zero length scale and the frequency saturates at high wavenumber (OCL-520, OCL-521).
5. **Quasi-electrostatic branch.** Under the stated uniform dielectric closure, the electric-potential solution carries no propagating electromagnetic branch, while the full transverse Maxwell system does (OCL-522). Coupled piezoelectric mechanical terms are outside this check.
6. **Equation inventory.** Every equation environment in the build has a row with a status (verified, conditional, or withheld), so the remaining work is visible (OCL-501, OCL-534).

## 4. What is not claimed

- No universal energy flux or stability result is asserted for all generalized theories.
- No general well-posedness, finite-speed, or dissipation result is inferred from a theory name.
- Several primary sources are missing or not yet checked; these are listed in the internal register and are marked as limitations where they affect a statement.
- Some bibliography entries were uncited at the time of writing; the author decides on each.
- Figure source provenance is incomplete.

## 5. Why this venue

Physics Reports publishes reviews that are longer than a survey and aim to identify trends and open questions. The proposed review would be useful as a reference map if it is restricted to the statements above, with the open items stated plainly.

## 6. Plan if invited

- Confirm the scope against the regular-review length and reduce the manuscript if needed.
- Resolve the missing sources or mark them as limitations.
- Complete the equation audit for the conditional displays.
- Final visual review at print size and reference check.

## 7. Author decisions (not filled here)

Target section, editor, page limit, data statement, AI-use statement, and any conflicts or funding are for the author. The journal's terms were not read in this draft.
