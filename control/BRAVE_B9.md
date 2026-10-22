# BRAVE B9 (supervisor audit of B8a ff1c472: ACCEPTED)
Accepted: dimensional check (tau_nu/2 fails s^-1), no-Taylor-order check, two legitimate second-order forms (Barak secondary; Abouelregal 2020 primary), scoped correction of V-B2h/V-B2z.
Tasks:
1. YES, build a SEPARATE APPA_LEDGER.csv covering every appA row (EQ-xxx, EQ-10.x, appA sec 6/7/9 rows) with the same status tags. Do NOT change EQUATION_LEDGER (176) or CLAIM_LEDGER (53).
2. Resolve the T0/T vs T/T0 thermal-channel factor in EQ-10.12 from the rendered page of Sci Rep 2023 eq 45 (page render, not text layer) and derive which is dimensionally/thermodynamically right for q_total = sigma v + q with q=-K grad T and entropy-flux convention. State sub-system.
3. Add Abouelregal 2020 (Sci Rep) and Green-Naghdi 1992 to LITERATURE_BASE with read_level.
4. Sec 9.7 claim that the identity "survives": test F9's point (E_int cross terms) on one concrete case from V-B3d; report whether sum with cross terms = 1 is automatic or only enforced by lumping.
Rules unchanged: execution evidence; grep own V-files before any WRONG; scope every verdict. Push to arena/04fdf32e-le, report commit hash.
