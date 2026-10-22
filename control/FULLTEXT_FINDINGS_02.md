# FULLTEXT FINDINGS 02 (supervisor, claude/control)
Source: second batch of PDFs opened by Claude from the handler's Downloads. PDFs are NOT in the repo (public repo, copyright). Facts and short statements only.

| # | Paper | Read? | Status |
|---|-------|-------|--------|
| 1 | Roy Choudhuri 2007, J. Thermal Stresses 30, 231-238 (TPL) | YES, eqs 1-9 | PRIMARY-SOURCE-CHECKED |
| 2 | Quintanilla 2002, J. Non-Equilib. Thermodyn. 27, 217-227 (DPL stability) | YES, cond (4.1) | PRIMARY-SOURCE-CHECKED |
| 3 | Tzou 1995, J. Heat Transfer (unified macro-micro) | partial, text layer | SECONDARY until eqs checked |
| 4 | Eringen 1983, J. Appl. Phys. 54, 4703 (differential nonlocal) | partial | OPEN |
| 5 | Chandrasekharaiah 1986 (AMR) and 1998 (AMR) reviews | text extracted, not yet analysed | OPEN (structure/length benchmark) |
| 6 | Guyer-Krumhansl 1966 (Phys Rev 148, 778) | extracted, not analysed | OPEN |
| 7 | Mindlin 1974 (IJSS 10) | extracted, not analysed | OPEN |
| 8 | Green-Naghdi 1991 (Proc R Soc A 432) | SCANNED PDF, no text layer; NOT READ | UNVERIFIED |

## F6 TPL law (Roy Choudhuri 2007)
- Eq (3): q(P,t+tau_q) = -[ k grad T(P,t+tau_T) + k* grad v(P,t+tau_v) ], with vdot = T, k*>0, and ordering 0 <= tau_v < tau_T < tau_q assumed.
- Eq (4) is FIRST-order Taylor in all three lags: q + tau_q dq/dt = -[ k*_v grad T + k tau_T d/dt grad T + k* grad v ], k*_v = k + k* tau_v.
- Eq (9): (1 + tau_q d/dt)[rho c_v Tddot + T0 beta uddot_kk,...] = k*_v lap Tdot + k tau_T lap Tddot + k* lap T. No 1/2 tau_v^2 term anywhere in this paper.
- The thermal-displacement gradient k* grad v is the point of TPL. It reduces to Jeffreys-type for k*=0, to Fourier for k*=0 and tau_T=tau_q, to LS for tau_T=0,k*=0.

## F7 Manuscript conflict (EQ-019, appA)
- Manuscript EQ-019 reads q(t+tau_q) = -k[T,i(t+tau_T) + (tau_nu/2) d_t^2 T,i(t+tau_nu)], tagged VERIFIED, "Tzou 1997".
- This is NOT Roy Choudhuri's law: it drops k* grad v, replaces it with a second-time-derivative of grad T, and attributes to Tzou 1997. Status VERIFIED is unsupported. Correct status: CONFLICT. Required: restate with k* and grad v, cite Roy Choudhuri 2007 as the origin, and label any (tau^2/2) second-order variant as a later development with its own primary source (Arena/Brave to find; do not guess).
- Also Eq 10.12 "TPL+MDD flux, confirmed across 8 full-text sources" needs the same re-check: which of the 8 actually state the second-order form.

## F8 DPL stability (Quintanilla 2002)
- Condition (4.1) is tau_T > tau_q/2 -> exponential stability; if it fails there are growing solutions. Matches Brave and my derivation (second order in tau_q, first in tau_T).

## Orders arising
BRAVE: (1) re-audit EQ-019 and EQUATION_LEDGER rows for TPL against F6; (2) find the primary source of any second-order TPL form used in the manuscript, report status tag.
ARENA: hold EQ-019 and ef:tpl:* until Brave reports; then fix per F7. Do not edit TPL on your own reading.
SUPERVISOR: OCR GN 1991; analyse AMR 1986/1998 reviews, GK 1966, Mindlin 1974, Eringen 1983 in FINDINGS_03.

## ADDENDUM F9 - Barak et al. 2023 (J. Thermal Stresses; read in full from Drive, text layer OK)
- Heat law (their eq 2.5): (1+tau_v D_s) K*_ij u_{,ij} + (1+tau_T D_s) K_ij Tdot_{,ij} = (1 + tau_q D_s + (tau_q^2/2) D_s^2)[ rho C_E Tddot + T0 beta_ij uddot_{i,j} - ... ], D_s = MDD operator. They state they follow Roy Choudhuri [19] and Gupta et al. [37].
- So the SECOND-ORDER term is (tau_q^2/2) on the flux-lag side, NOT (tau_nu/2) d_t^2 on the temperature-gradient side. Manuscript EQ-019 puts the 1/2 term on the wrong lag and with wrong power. Roy Choudhuri 2007 itself is first order only; the second-order-in-tau_q form is Barak/Gupta's own extension (secondary source, CONDITIONAL on Quintanilla-Racke stability).
- Parameters used: tau_v=0.02, tau_q=0.05, tau_T=0.03 (tau_v<tau_T<tau_q; they cite Quintanilla-Racke condition).
- Energy ratios (eqs 6.9-6.14): sum_s E_Ss + E_int + E_RP + E_RT + E_RS = 1, with E_int = sum of cross terms s != t between refracted waves. This is the R_mode/cross-term bookkeeping we flagged: the unity result holds only because cross terms are lumped into E_int, which can be negative or non-physical per mode. The review must state this explicitly in 9.7.
- Normal acoustic flux is cited from Kumar-Sharma [9] and Guha-Singh [41], not derived there.
ORDER (Brave): re-tag EQ-019 with F9 as the correct reference form; check manuscript 9.7 attributions against F9 (what Barak actually does vs what review says).
