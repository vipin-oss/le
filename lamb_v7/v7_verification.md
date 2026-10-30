# v7 internal verification record

Internal only. No number here goes into a scholar file.

## What was checked, with the script that did it

`internal/verify_v7.py` builds each $5\times5$ matrix from the entries written in the master (placeholder
constants, only $\eta$ symbolic) and tests two things: whether $\det M(\eta)=\det M(-\eta)$, and how the
determinant scales with $\eta$. Tolerance for "even" is a relative difference below $10^{-25}$ at 90 digits;
the observed noise floor of the test itself is about $10^{-12}$ because the matrix is badly scaled
(entries from $10^{-19}$ to $10^{8}$).

## Parity, which is the result that changed

| case | $\max|\det(\eta)-\det(-\eta)|/|\det|$ | verdict |
|---|---|---|
| Sumit, full ($\beta_{\rm th}\ne0$, $\Pi_{\rm th}\ne0$, $p_3\ne0$) | $2.0\times10^{-4}$ | not even |
| Sumit, $\beta_{\rm th}=0$, $\Pi_{\rm th}=0$, $p_3\ne0$ | $2.0\times10^{-4}$ | not even |
| Sumit, $p_3=0$, all couplings else on | $1.7\times10^{-12}$ | noise floor: even |
| Sumit, $p_3=10^{-6}$ | $1.2\times10^{-9}$ | breaking term linear in $p_3$ |
| Sumit, $p_3=0.9$ | $2.0\times10^{-4}$ | not even |
| Neha, full | $0.0$ | even for every setting |
| Anu, full | $0.0$ | even for every setting |

The sweep of $k$ over 1000, 1234.5 and 5000 gave the same numbers, so the verdict is not an artefact of one
wavenumber.

**Consequence for the text.** The parity break in Paper A is caused by the pyroelectric constant $p_3$
acting together with the carrier field, not by the Sorbet and Peltier coefficients. Setting
$\beta_{\rm th}=\Pi_{\rm th}=0$ leaves the polynomial odd. The handoff note that named
$(\beta_{\rm th},\Pi_{\rm th})$ is corrected in the master, and the master says so in words rather than by
pointing at any earlier statement. Papers B and C split into symmetric and antisymmetric families for every
setting, which is also stated in the masters.

## Degree

The degree is 14 in $\eta$ with $l_g\ne0$ and 10 with $l_g=0$, by the row-by-row counting written in
Calculation D of each master; the diagonal product reaches the bound and no permutation exceeds it. A
numerical confirmation by Fourier fitting was attempted and is **not trustworthy** at this conditioning
(coefficients span 60 orders of magnitude and the fit reports the k-dominated term as the leading one), so
it is recorded as open rather than quoted. The counting argument itself is reproducible on paper.

## Not done

No LaTeX engine exists in this environment, so neither variant of any of the three masters has been
compiled; the page counts and the "both settings compile" check are therefore open. No numerical
dispersion run was made against the reference solver in this round.

## Constant placeholders used

Paper A: $c_{11}=209.7$, $c_{13}=121.1$, $c_{33}=211.2$, $c_{44}=42.4$ GPa; $e=(1.1,2.2,3.3)$ C/m$^2$;
$\rho=5680$; $n_0=10^{21}$ m$^{-3}$; $b_n=0.02$; $D_n=10^{-6}$; $\tau_R=10^{-9}$ s.
Paper B: $C=(150,60,130,40)$, $K_1=30$, $K_2=20$, $R=(1.1,2.2,3.3)$ GPa, $\gamma=10^8$, $\rho_p=12$.
Paper C: $C=(220,110,215,45)$ GPa, $\alpha_{11}=1.2\times10^{-9}$, $\alpha_{33}=3.4\times10^{-9}$ s/m,
$\mu_{11}=2.5\times10^{-6}$, $\mu_{33}=1.9\times10^{-6}$ N/A$^2$.
