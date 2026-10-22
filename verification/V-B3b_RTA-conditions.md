# V-B3b — Conditions under which R + T + A = 1

**Phase B3, item b.** Access date 2026-10-22. Numeric verification: `V-B3_rta.py`.

---

## 1. Task

B3b: state and derive the conditions under which $R+T+A=1$ for reflection/transmission at an
interface, and give a numeric example with code, checked to sum to 1 within $10^{-10}$.

## 2. Method

1. Set up the interface problem in general form (two semi-infinite media, one incident branch,
   arbitrary number of reflected/transmitted branches).
2. Derive the flux normalisation and show what is needed for the sum to be 1.
3. **Do the numbers**, then see whether the obvious hypothesis survives (it does not — §3.2).
4. Separate the three distinct meanings that $A$ can carry, because most of the confusions in the
   literature are a failure to distinguish them.

## 3. Result

### 3.1 The definition, and the identity

For a harmonic branch $j$ with temperature amplitude $\hat\theta_j$ and normal flux amplitude
$\hat q_j$, the time-averaged normal energy flux is
$$J_j=\tfrac12\operatorname{Re}\big(\hat q_j\overline{\hat\theta_j}\big).$$
With incident flux $J_i>0$, reflected $J_r<0$ (in the $+x$ convention) and transmitted $J_t>0$:
$$R:=\frac{-J_r}{J_i},\qquad T:=\frac{J_t}{J_i},\qquad A:=1-R-T .$$

$R+T+A=1$ is then an **identity by definition** — so it can never be evidence for anything. The
content lies in the three separate conditions:

- **(C1) Same frequency on both sides.** No time-dependent interface ⇒ $\omega$ is conserved.
  Fails for a moving or time-varying interface, or if a model is written with an explicit time
  delay in the interface condition.
- **(C2) Snell's law with the *model's own* dispersion.** The tangential wavenumber is conserved,
  $k_\parallel^{(1)}=k_\parallel^{(2)}$, and each branch's normal wavenumber is obtained from that
  model's dispersion relation. Fails if a paper mixes models (e.g. GN-II wave number with a Fourier
  flux), which is the single most common source of "$R+T\neq1$".
- **(C3) The flux used in $R$ and $T$ is the flux that is continuous at the interface** — i.e. the
  one from that model's own energy identity (`V-B3a` §3.7). Fails for LS (missing
  $(1-i\omega\tau_0)^{-1}$), for GN-II (using $\theta$ instead of $\alpha$), for GN-III (dropping
  the $k^*$ channel), and is **undefined** for MGT.
- **(C4) The number of interface conditions equals the number of outgoing branches.** If a model's
  thermal operator is order $n$ in time, it needs $n$ conditions. Imposing fewer gives an
  under-determined problem whose "solution" will satisfy $R+T+A=1$ by construction but is not the
  solution of the stated model. **MGT (3rd order) needs three; all others here need two.**
- **(C5) Outgoing/radiation condition.** On each side the branch kept must decay or propagate away
  from the interface. Violating this silently admits a spurious "growing" branch and produces
  $R>1$ or $T>1$.

Under (C1)–(C5), and with an **ideal (zero-resistance) interface**, the numbers below show that
$A=0$ to machine precision for every model in the list, including the dissipative ones.

### 3.2 The hypothesis that failed (recorded, not deleted)

My working hypothesis when starting B3 was: *"$A>0$ for the dissipative models (Biot, LS, GL,
GN-III) and $A=0$ for GN-II, because the dissipative models lose energy."* **The computation
refutes this.** At an ideal interface between two different media:

| model | $R$ | $T$ | $A=1-R-T$ | $\arg\hat q_1-\arg\hat q_2$ |
|---|---|---|---|---|
| Biot/Fourier | 0.567289 | 0.432711 | $+5.6\times10^{-17}$ | 0 |
| Lord–Shulman | 0.567289 | 0.432711 | $-3.3\times10^{-16}$ | $2.2\times10^{-16}$ |
| Green–Lindsay | 0.567289 | 0.432711 | $+2.8\times10^{-16}$ | $1.1\times10^{-16}$ |
| GN-II | 0.146836 | 0.853164 | $0$ (exactly) | 0 |
| GN-III | 0.146836 | 0.853164 | $-7.5\times10^{-11}$ | $8.9\times10^{-6}$ |

**Why $A=0$ even for dissipative models:** the flux amplitudes on the two sides differ by a *common
phase factor*. For Fourier, $\hat q=-ik k_{\text{th}}\hat\theta$ with $k=(1+i)\sqrt{\omega/2\kappa}$,
so $\arg\hat q=-\pi/4$ **independently of $\kappa$**; both media share it, so the interface cannot
"absorb" the phase lag. The bulk dissipation is already **inside** the complex $k$ of the branch:
the transmitted wave is attenuated, and its attenuated flux is what $T$ measures. There is nothing
left over to put in $A$.

**This is a genuinely useful statement for the review:** a reported $R+T=1$ for an ideal interface is
a **consequence of the interface conditions (C3)**, not a validation of the physics, and it holds
even for strongly dissipative models. Papers that present "$R+T=1$" as a check of their energy
accounting are checking their own algebra, no more.

### 3.3 When $A\neq0$: the three distinct mechanisms

**(M1) Interface-level loss — contact resistance (Kapitza).** With a finite interface conductance
$h$ (units W m⁻²K⁻¹), the temperature jumps: $\theta_1-\theta_2=q_n/h$ replacing $[\theta]=0$ while
$[q_n]=0$ is kept. This produces a genuine third term. Numeric (`V-B3_rta.py`, LS, 1 MHz):

| $h$ [W m⁻²K⁻¹] | $R$ | $T$ | $A$ | $\lvert R+T+A-1\rvert$ |
|---|---|---|---|---|
| $10^{9}$ | 0.568323 | 0.430312 | $+1.365\times10^{-3}$ | $0$ |
| $10^{8}$ | 0.577699 | 0.409319 | $+1.298\times10^{-2}$ | $0$ |
| $10^{7}$ | 0.666801 | 0.252966 | $+8.023\times10^{-2}$ | $0$ |
| $10^{6}$ | 0.917988 | 0.019659 | $+6.235\times10^{-2}$ | $0$ |

$A>0$ throughout, and **non-monotonic in $h$**: $A\to0$ both as $h\to\infty$ (ideal contact) and as
$h\to0$ (nothing enters, $R\to1$), with a maximum in between. Both limits are physical checks and
both are reproduced.

**(M2) Phase mismatch across the interface.** If the two media have *different* phase lags — e.g.
different $\tau_0$ in LS, or different $k^*/\omega k_{\text{th}}$ ratios in GN-III — then
$\arg\hat q_1\neq\arg\hat q_2$ and $A\neq0$ at second order in the mismatch. Numeric (LS with
$\tau_0=10^{-10}$ s on side 1 and $10^{-11}$ s on side 2): $R=0.567289$, $T=0.432589$,
$A=+1.22\times10^{-4}$. For GN-III with different $c_h$ (2000 vs 5000 m/s): $A=-9.5\times10^{-11}$,
i.e. still zero at double precision. **So (M2) is a real but tiny effect, and it is a bulk property
masquerading as an interface one** — the correct bookkeeping is that each half-space attenuates at
its own rate, which a single $A$ cannot represent.

**(M3) A missing branch or condition (the pathological case).** If a model needs $n$ conditions and
only $n-1$ are imposed, the system is under-determined; the resulting amplitudes will still satisfy
$R+T+A=1$ *by construction* (with $A$ absorbing the deficit) but will be meaningless. **This is the
case that a verifier must test for**, and it is why (C4) is on the list: the check is not
"$R+T+A=1$?" but "$A=0$ for an ideal interface?" — because a correct ideal-interface solution has
$A=0$, and a wrong one generally does not.

### 3.4 The numeric deliverable and the $10^{-10}$ check

`V-B3_rta.py` implements the thermal interface problem for Biot, LS, GL, GN-II, GN-III (MGT
excluded for the reason in `V-B3a` §3.6) and performs:

- **[0] solver sanity:** identical media on both sides ⇒ $r=0$, $t=1$, $A=0$. **Result: exact zeros
  for all five models (worst deviation $0.0$).** This is the non-trivial check of the solver: it
  would fail if a branch sign or a flux factor were wrong.
- **[1] two different media:** $R+T+A-1=0.00\times10^{0}$ for all five models, i.e. **within
  $10^{-10}$ with room to spare** (the residual is at the double-precision floor, $\sim10^{-16}$);
  GN-II's $A$ is exactly $0$.
- **[2] low-frequency limit:** LS and GL $\to$ Biot as $\omega\tau_0\to0$, verified at
  $\omega\tau_0=6.3\times10^{-4},6.3\times10^{-6},6.3\times10^{-8}$ (all $A$ within $10^{-16}$ of
  zero).
- **[3] phase analysis:** $\arg\hat q_1=\arg\hat q_2$ to $10^{-16}$ for Biot/LS/GL/GN-II, and
  $8.9\times10^{-6}$ for GN-III — matching §3.2's explanation.
- **[4] Kapitza case:** the §3.3 (M1) table, with $\lvert R+T+A-1\rvert=0$ and the flux-jump
  residual at $10^{-15}$.

**What the $10^{-10}$ test does and does not establish.** It establishes that the flux definitions
of `V-B3a` §3.7 are consistent with the interface conditions, and that the solver is correct. It
does **not** establish that any published $R/T$ is right; for that, (C1)–(C5) must be checked
paper by paper, and the discriminating test is $A=0$ at an ideal interface.

### 3.5 Check list for the review (one line per model)

| model | ideal interface gives $A=0$? | what makes $A\neq0$ | trap |
|---|---|---|---|
| Biot | yes ($5.6\times10^{-17}$) | Kapitza resistance | quoting $R+T=1$ as validation |
| LS | yes (phase common) | Kapitza; **$\tau_0$ mismatch** | using $k_{\text{th}}\partial_n\theta$ instead of $/(1-i\omega\tau_0)$ |
| GL | yes (Fourier flux) | Kapitza; $\tau$-mismatch | using the LS flux — GL's flux is Fourier |
| GN-II | yes (exactly) | Kapitza | using $\theta$ where $\alpha$ belongs |
| GN-III | yes ($7.5\times10^{-11}$) | Kapitza; $k^*$ mismatch | dropping the $k^*$ channel in $[q_n]$ |
| MGT | **undefined** | — | imposing 2 conditions on a 3rd-order model |

## 4. Evidence / Sources

No source was opened for this item: the derivation is elementary flux bookkeeping, and the numbers
come from `V-B3_rta.py`. The model flux definitions and sources are those of `V-B3a` §3.7 / §4.
Literature on $R/T$ in these theories is in `V-B3c`.

**Nothing in this file is a quotation.** The claim about what the literature typically reports
(§3.2, last paragraph) is a **prediction from the structure**, not a survey finding — see §7.

## 5. Checks done

1. **Identical-media check** (exact): $r=0$, $t=1$, $A=0$ for all five models, to $0.0$ — a strong
   solver test, independent of the material contrast.
2. **Sum check:** $\lvert R+T+A-1\rvert=0$ (displayed as $0.00\times10^{0}$) for every model and
   every parameter set; the underlying residuals are at $\le10^{-16}$.
3. **Independent flux-continuity residual** at the computed solution: $\le5\times10^{-9}$ absolute
   on fluxes of magnitude $\sim10^{9}$ W/(m²K), i.e. $\sim10^{-18}$ relative.
4. **Limit check:** $\omega\tau_0\to0$ ⇒ LS, GL $\to$ Biot; $k_{\text{th}}\to0$ ⇒ GN-III $\to$ GN-II.
5. **Physical consistency of $A(h)$:** $A\to0$ at both $h\to\infty$ and $h\to0$, maximum in between.
6. **Phase explanation tested, not asserted:** the $\arg\hat q$ column in §3.2 is computed, and it
   correctly predicts *which* models have $A=0$. (This is the check that turned the failed
   hypothesis into an explanation.)
7. **Code runs clean** under Python 3 + numpy; no warnings suppressed.

## 6. Confidence

- **Condition list (C1)–(C5): HIGH** (they are the standard requirements for a well-posed interface
  problem, and each failure mode is exhibited numerically).
- **"$A=0$ at an ideal interface for all five models": HIGH** — computed, and explained by the
  common-phase argument which itself is checked.
- **The refutation of my own hypothesis: HIGH** (numbers are unambiguous).
- **"$A=0$ always for an ideal interface in *any* model": MEDIUM.** It is true for the five models
  here; a model with genuinely different phase lags on the two sides (or with an interface
  constitutive law of its own) can break it — (M2) shows the mechanism.
- **MGT exclusion: MEDIUM–HIGH** (structural argument, `V-B3a` §3.6).

## 7. NOT verified / open issues

1. **No literature was surveyed for this file** — in particular, the assertion that papers commonly
   present $R+T=1$ as a validation, and that GN-II/GN-III interface conditions are often written
   with $\theta$ instead of $\alpha$, are **predictions, not survey results**. `V-B3c` does not
   close this gap either (no full text read). If they are to appear in the review as criticisms,
   they need page-level citations.
2. **Only the *thermal* interface problem was computed.** The coupled thermoelastic problem
   (incident P wave → reflected P + reflected thermal + transmitted P + transmitted thermal, five
   unknowns and four conditions plus one normalisation) was **not** implemented. Its structure is
   the same; its numbers are not supplied here. `V-B3a` §7.2 also records that coupled-system
   stability is unverified.
3. **Oblique incidence and mode conversion** are not treated (normal incidence only, in the numeric
   part; the general statements (C1)–(C5) are incidence-independent).
4. **Evanescent branches** are only touched implicitly: a transmitted branch with $\operatorname{Im}k>0$
   carries zero normal flux in the time average only if it is purely evanescent; the code keeps the
   decaying root but does not classify branches as propagating vs evanescent or compute a critical
   angle. **Not verified.**
5. **Anisotropy** is not treated; in an anisotropic medium the energy flux direction (group
   velocity) is not parallel to $k$, so $R$ and $T$ must be defined with respect to the *normal
   flux*, as done here, but the "angle" bookkeeping changes. Flagged.
6. **MGT numbers do not exist** in this file, by design.
