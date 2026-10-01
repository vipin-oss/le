# Analytical source checks — not numerical validation

Date:30 September2026. Sources: user-supplied B01/B02 PDFs in alit.zip. Scope: source consistency/common-law checks before any implementation. No new research model, solver or first-discovery novelty is claimed.

## Conventions

D=d/dt; s is the Laplace variable; tau>0. For the source's causal compatible/zero-history interpretation,

```text
q_hat = -k * [N(s)/M(s)] * grad(theta_hat).
```

Cancelling a common differential factor does NOT preserve every arbitrary higher-order initial-value problem. An extra homogeneous mode can occur if the written higher-order equation is supplied with incompatible ICs. The identities below concern compatible source histories/constitutive-network states.

## A01 — MCV5 equal-unit reduction

B01 Eq28/Table1:

```text
M=(1+tau*s)^2
N=2*(1+tau*s)
k*N/M=2*k/(1+tau*s).
```

Thus the equal-unit source law has the observable CV kernel with effective conductivity2k. In time-domain terms, the second-order expression is (1+tau*D) applied to the first-order CV(2k) residual. A nonzero initial residual would add a decaying homogeneous mode; do not infer unconditional equivalence for arbitrary independently assigned heat-flux-rate data.

**Status: ANALYTICALLY_CHECKED — algebra, not numerical reproduction or a new equivalence discovery.** Unequal component relaxation times in the general network need not reduce the same way.

## A02 — MGN3 equal-unit reduction

B01 Eq40/Table1:

```text
M=2*tau*s*(1+tau*s)
N=(1+tau*s)^2
k*N/M=(k/2)*(1+tau*s)/(tau*s).
```

This is the source GN structure with conductivity parameter k/2, under compatible histories. Its zero-frequency thermal-displacement pole remains; it is not ordinary static Fourier conduction.

**Status: ANALYTICALLY_CHECKED — stated restricted parameter/history case only.**

## A03 — MCV1/MCV2 physical reparameterization

MCV1 physical kernel:
`k_a*(1+tau_a*s)/(1+2*tau_a*s)`.

MCV2 physical kernel:
`k_b*(2+tau_b*s)/(1+tau_b*s)`.

Putting `k_a=2*k_b`, `tau_a=tau_b/2` makes the kernels equal. This is a restricted first-order relaxation family (also expressible in first-order phase-lag form), not two independent observable laws merely because the labels differ.

Coordinate/time normalizations involving k must also be converted consistently; this is not permission to overlay source dimensionless plots at unchanged axes/parameters.

**Status: ANALYTICALLY_CHECKED. No current novelty claim.**

## A04 — DC conductivity normalization

Directly from B01 Table1:

- CV,MCV1,MCV3,MCV6: `lim(s->0) k*N/M=k`.
- MCV2,MCV4,MCV5: `lim(s->0) k*N/M=2*k`.
- GN and MGN rows: M(0)=0 while N(0) is nonzero; the transfer has a zero-frequency pole rather than a finite static conductivity.

Reproduce the published equal-component comparison as such. A new mechanism study that intends equal measured static conductivity must set the effective coefficient consistently and label this as a separate control. Do not silently change source inputs to improve an apparent match.

**Status: ANALYTICALLY_CHECKED — transfer limits, not a complete thermodynamic-admissibility proof.**

## A05 — MGN2 internal equation inconsistency

B01 p7 Eq36, with equal component parameters, gives:

```text
q+3*tau*q_t+tau^2*q_tt = -k*grad(T)-k*tau*grad(T_t).
```

This is not the printed Eq37/Table1 MGN2 law:

```text
tau*q_t+tau^2*q_tt = -k*grad(T)-2*k*tau*grad(T_t).
```

Independent elimination of Eq35, using the source definition k1*=k1/tau1 and omega_t=grad(T), gives for compatible histories:

```text
tau1*q_t+tau1*tau2*q_tt
 = -k1*grad(T) -(k1*tau2+k2*tau1)*grad(T_t).
```

Equal k1=k2=k,tau1=tau2=tau gives Eq37, not Eq36. This is an **independently derived source-consistency relation**, not an official published correction/new research law.

**Status: ANALYTICALLY_CHECKED internal mismatch; ACTION_REQUIRED before selecting/implementing MGN2.** Original PDFs remain unchanged. The derivation does not certify all source equations or results. Human domain-expert review is recommended before model adoption/publication.

## A06 — Thermal expansion header/unit

Source sigma=C_L*epsilon-gamma*theta with gamma=(3lambda+2mu)*alpha_theta requires gamma[Pa/K], hence alpha_theta[1/K]. The m/K-style Table2 header is dimensionally inconsistent with that use. Proposed source-case disposition: use the same reported numeric coefficient1.78e-5 as1/K, explicitly logged, not a new measurement or silent source edit.

**Status: ANALYTICALLY_CHECKED dimensional requirement; implementation disposition pending.**

## A07 — Dimensionless coupling does not require untabulated k

B01 defines n2=rho*cE/k and g=gamma/(k*n2). Substitution gives g=gamma/(rho*cE). Therefore dimensionless Figure5 reconstruction can use the reported elastic/expansion/density/capacity/T0 inputs without guessing k. The physical x/time/tau conversions still require k; no dimensional operating prediction is certified.

**Status: ANALYTICALLY_CHECKED algebra.**

## A08 — Eq66 boundary amplitudes

Let z_i=k_i^2 and Delta=z1-z2. B01 Eq66 has:

```text
theta1=(z1-s^2)/(s*Delta)
theta2=(z2-s^2)/(-s*Delta)
sigma1=b*s/Delta
sigma2=-b*s/Delta.
```

Thus `theta1+theta2=1/s` and `sigma1+sigma2=0`. Multiplying by decaying exp(-k_i*x) gives the required heated free-end values at x=0 and decay at infinity when Re(k_i)>0.

This checks the stated boundary-amplitude identity, not an implemented inversion, every PDE residual or a computed transient curve. Degenerate roots need a separate limiting treatment.

**Status: ANALYTICALLY_CHECKED — limited identity only.**

## A09 — CV / LS common law

B01 CV:
`q+tau*q_t=-k*grad(theta)` and
`-div(q)=rho*cE*theta_t+T0*beta:epsilon_t`, with classical thermoelastic stress.

Applying (1+tau*D) to the energy balance yields the coupled LS-type heat equation. B02 obtains LS with eta=1, t1=t2=t3=0, its GL material vector zero, and scalar isotropic relaxation tau0=tau. With matching isotropic C,beta,K,c/temperature conventions, the constitutive/energy laws coincide.

This does NOT make a semi-infinite 1D step case identical to a finite cylindrical heat-flux case. In the radial cylinder epsilon_trace includes u_r+u/r and BCs/scaling differ.

**Status: ANALYTICALLY_CHECKED common constitutive/energy structure; no numerical case comparison.**

## A10 — GNIII versus GNII / GL limitation

B01 GN Eq8 implies:
`q_t=-k*grad(theta_t)-(k/tau)*grad(theta)`.

This has B02 GNIII structure with k*=k/tau. B02's displayed numerical GN curves use typeII, with dissipative k=0. Setting k->0 at fixed tau in the tied B01 law also eliminates k*=k/tau; it is not that nontrivial typeII limit. A joint/independent-parameter limiting map and compatible nondimensionalization are needed.

B02 GL also introduces temperature-rate terms in stress/entropy not present in B01's native classical-stress equations. Do not claim the GL curves are an unmodified B01 benchmark by heat-law naming alone.

**Status: ANALYTICALLY_CHECKED law comparison / benchmark boundary.**

## Claims explicitly not made

No source curve was numerically reproduced. No code/pilot/production was executed. No full existence/uniqueness, stability, thermodynamic proof, tensor extension, physical validation, literature novelty or journal readiness is established by these checks.
