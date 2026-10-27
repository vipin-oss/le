# B23b — Adjudication of Arena's dispute of B23 P1-2, plus OCL-513 and flux re-derivation

Prepared 2026-10-27. Target head: `arena/b5e608f8-le` @ `d9bf722` (read-only extraction in
`/home/user/b23b_src`). This report is written **only** under `verification/B23b_*` in
`vipin-oss/le`; nothing in the target head was modified.

## P0

**None.** No wrong statement was found in the four disputed rows or in the new material.

## P1

**None outstanding.** Two items need explaining rather than fixing.

### P1-1 — my own B23 disposition was wrong for one of the four rows; I withdraw it

B23's item-1 tally was `CONFIRMED 16, WRONG 0, OVERSTATED 0, NOT-CHECKABLE 4`. **One of those
four NOT-CHECKABLE dispositions was my error.** Mindlin (1974) is in the library — file
`B13-021__0020-76832990047-x.pdf`, batch `B13`, 0.80 MB, 13 pp. I could not find it in B23
because (a) the library inventory records `key = unknown` for that row, so no bibliographic key
exists to search on, and (b) it carries a batch-renamed filename, so title keywords fail. Arena's
claim that the paper is in the library was correct; my "source not located" was a search failure,
not a source absence, and B23 should have said so in those words.

**Corrected tally for the four disputed rows: CONFIRMED 4, WRONG 0, OVERSTATED 0,
NOT-CHECKABLE 0.** All four sources were opened, on the cited pages, in this pass.

### P1-2 — Arena's substantive claim is confirmed; only the *record* remains thin (downgraded to P2)

B23 P1-2 said the remediation's fresh-read claim was unsupported because only 4 ledger rows carry
a `2026-10-27` date. At `d9bf722` the count is **5** rows (`OCL-195`, `OCL-207`, `OCL-404`,
`OCL-405`, `OCL-513`) — the fifth was added with OCL-513 in this remediation. I re-read every one
of the five anchors myself, and all five check out (verdicts below and in
`B23b_OCL513_CHECK.md`). Arena did not need to prove its claim by artifact: the claim is true.

What is still not in the ledger: of **40** rows whose `evidence_mode` starts with `FRESH-READ`,
only **11** carry any date (6 × `2026-10-26`, 5 × `2026-10-27`); the other 29 carry a fresh-read
label with no date and no page-level record. That is a traceability gap, not a truth defect — it
makes an auditor unable to distinguish a fresh read from a carried one without redoing the work.
Downgraded to **P2-1**; the fix is one `date` column, not a re-read.

## Verdict table — the four disputed rows

Full detail, including the exact equations seen, is in `B23b_SOURCE_VERDICTS.csv`.

| row | manuscript claim (current text) | source + page actually seen | verdict |
|---|---|---|---|
| **OCL-195** | Mindlin 1974 gives the 3-D linear thermopiezoelectric balances, `h_i = -K_ij theta_,j`, and Gibbs-function constitutive laws, as the starting point of the plate reduction | Mindlin, IJSS 10 (1974) 625–637, `B13-021`: **printed p.625 Eq. (1)** `T_ij,i = rho u_ddot_j`, `D_i,i = 0`, `h_i,i = -Theta_0 eta_dot`; **printed p.626 Eq. (2)** `h_i = -K_ij theta_,j`; **Eqs. (3)–(5)** `T_ij = dG/dS_ij`, `D_i = -dG/dE_i`, `eta = -dG/dtheta` | **CONFIRMED** |
| **OCL-207** | Kumar et al. 2023 is a dual-porous thermoelastic interface study reporting a total energy-ratio sum that *approximates* unity, kept as a numerical observation, not an identity | Kumar, Gupta, Pathania, Barak, Phys. Scr. 98:115211, `B01-009`: **printed p.1** (elastic vs doubly porous thermoelastic half-spaces, DPL + MDD + two-temperature); **printed p.17, Sec. 9 final bullet** — the sum "approximates unity", offered as validation of energy conservation | **CONFIRMED** |
| **OCL-404** | table row: classical thermoelasticity supplies thermal-stress coupling and the conductivity-based heat equation (the explicit `q_i = -k T_,i` wording was correctly withdrawn) | Biot, J. Appl. Phys. 27:240, `1.1722351.pdf` (inside `LE_PAPERS_P01.zip`): **printed p.241 Eq. (2.2)** `sigma_xx = 2 mu e_xx + lambda e - beta theta`; (2.14)–(2.15); **printed p.242 Eqs. (3.3)–(3.4)** `k lap theta = c theta_dot + T beta e_dot` | **CONFIRMED** |
| **OCL-405** | table row: piezothermal moduli and pyroelectric constants, in the source's own terminology, no `e_kij` tensor attributed | Barak et al., Sci Rep 13:17170, `(2023)Barak_et_al-2023-Scientific_Reports.pdf`: **printed p.3 Eq. (6)** `D_i = eps_ij E_j + eta_ijr e_jr + p_i T`; Eq. (7) `D_i,i = 0`; Eq. (8) memory-dependent DPL heat equation; **Nomenclature on the same page**: "eta_ijr, eps_ij = piezothermal moduli tensors", "p_i = pyroelectric constants" | **CONFIRMED** (anchor needs Eq. (6), see P2-2) |

Method note on OCL-195: because a text extractor can garble `rho u_ddot_j`, I also rendered the
printed p.625 equation block as a page image and read it there. The image and the extract agree.

## Arena's provenance claims, checked one by one

| Arena said | reality | verdict on the provenance claim |
|---|---|---|
| Biot = `1.1722351.pdf` in the split archive | `LE_SOURCES/04_SPLIT_ZIP_PARTS/LE_PAPERS_P01.zip!/1.1722351.pdf` (and `01_ZIP_ARCHIVES_ORIGINAL/1.1722351.zip`) | **SUPPORTED** |
| Kumar 2023 is in the batches | `02_PAPERS_PDF_BATCHES/B01/B01-009__P09_2023_PhysScr_…pdf` | **SUPPORTED** |
| Mindlin 1974 is in the library | `02_PAPERS_PDF_BATCHES/B13/B13-021__0020-76832990047-x.pdf` | **SUPPORTED** — and this is the claim B23 got wrong |
| Barak = "the Indian J. Phys. file in B14" | no Indian Journal of Physics file exists anywhere in the library (name search: 0 hits); the row cites `Barak2023` = **Sci Rep 13:17170**, whose PDF exists but is **not** in the 19 inventoried batches | **WRONG** (mislabel; does not affect the row, which I verified against the correct paper) |

## New claims checked

### OCL-513 — `rho c_v T_dot = k lap T - beta T_0 u_dot_{i,i}` vs Biot p.242 (3.3)–(3.4)

**CONFIRMED.** Biot (3.4) rearranges to Eq. (4.2) exactly under `theta -> T`, `c -> rho c_v`
(Biot's `c` is defined on p.241 as the specific heat *of the unit volume*), `e -> u_{i,i}`, with no
source term. My independent sympy check (`verification/B23b_verify_biot.py`, rc=0) verifies the
residual is 0, that the printed stress sign is the negative one, that Biot's heat route (2.15)
and the manuscript's entropy route (3.22) agree identically, that the discarded terms are genuinely
`O(eps^2)`, that the negative controls (`beta=0`, `k=0`) behave, and that all three terms carry the
same SI dimension `M L^-1 T^-3`. Details: `B23b_OCL513_CHECK.md`.

### `phase5/verification/verify_classical_thermoelastic.py`

Executed at `d9bf722`: `rc = 0`. The symbolic content is substantive and duplicates my steps
independently. Caveat for the ledger: its **final block only asserts LaTeX substrings** of
`sec04_thermoelastic.tex`; it is a transcription guard, not a derivation. It does work as a guard
— flipping the sign inside that string kills the script (mutation 3).

### `phase5/scripts/verify_classical_flux.py` + independent flux re-derivation

Executed at `d9bf722`: `rc = 0`. My own derivation (`verification/B23b_verify_eulerian.py`, rc=0)
independently yields

    F_i = q_i - sigma_ij v_j + E v_i ,  E = rho(1/2|v|^2 + e)

from the material balances plus mass conservation, shows the reduced `q - sigma·v` fails by exactly
`-div(E v)`, and exhibits a **steady solution** where that residual is `-4` at `x=2` (not merely a
formal difference). Cycle-mean results: the advective mean vanishes identically for a lossless
elastic wave and for an adiabatic thermoelastic wave, but not for a general phase-lagged field —
which is precisely the caveat Section 10.2 now prints. Details:
`B23b_EULERIAN_REDERIVATION.md`.

Mutation evidence that the two scripts are not tautological
(`verification/B23b_mutation_test.py`, rc=0): dropping `E v` **killed**, flipping its sign
**killed**, flipping the `beta T_0 du/dt` sign **killed**, deleting the quadratic-remainder
assertion **survived** (expected, since deleting a check cannot fail a script).

**B23 P1-1 status: upheld against the head it was written for, FIXED at `d9bf722`.** The Section 3
equations now carry `E v_i`, say explicitly that omitting it is not an identity, and Section 10.2
isolates the reduced flux with the correct order-of-magnitude caveat.

## P2

1. **Ledger traceability.** 40 `FRESH-READ` rows, 11 dated, 29 undated; no page-level record per
   row. Add `read_date` and `page_seen` columns; the five disputed rows already show the pattern.
2. **OCL-405 anchor is one equation short.** Eqs. (7)–(8) do not display `eta_ijr` or `p_i`;
   Eq. (6) does. Change the anchor to "Eqs. (6)–(8) and Nomenclature" so a later auditor does not
   have to hunt for the moduli.
3. **Library inventory gaps.** 354 of 500 `INVENTORY.csv` rows carry `key = unknown`, including
   Biot (`1.1722351.pdf`), Kumar (`B01-009`) and Mindlin (`B13-021`) — the exact three files B23
   failed to locate. Separately, the Barak Sci Rep PDF is in the library but absent from
   `INVENTORY.csv`/`MOVE_MANIFEST.csv` entirely, so the "19 batches" are not a complete index.
   Populating `key` from the Crossref DOI (batch filenames already contain the DOI-ish suffixes)
   would have prevented the whole dispute.
4. **Notation gloss.** Eq. (4.2) uses `rho c_v` where Biot uses `c` per unit volume, and `E` is
   total energy density in Section 3 but a symbol reused elsewhere; one-line glosses would remove
   the ambiguity. Editorial only.

## What I could not check, and what I did not attempt

* No check of any claim in `sec05` beyond the two disputed rows; no re-audit of the other 35
  `FRESH-READ` rows — that would require re-reading ~35 sources, and is not what was disputed.
* `mindlin1965.pdf` / `mindlin1968.pdf` in `LE_PAPERS_P03__was_R4.zip` were not opened; they are
  not anchor sources for any disputed row.
* No manuscript `.tex` edit was made and none is requested by this report.

## Deliverables and reproduction

| file | content |
|---|---|
| `verification/B23b_REPORT.md` | this report |
| `verification/B23b_SOURCE_VERDICTS.csv` | 4 rows: verdict, page seen, equation seen, library file, batch, Arena-provenance verdict |
| `verification/B23b_OCL513_CHECK.md` | Biot p.241–242 vs Eq. (4.2), plus script audit |
| `verification/B23b_EULERIAN_REDERIVATION.md` | exact flux derivation, steady counterexample, cycle means, P1-1 verdict |
| `verification/B23b_verify_biot.py` | OCL-513 symbolic check (sympy only) |
| `verification/B23b_verify_eulerian.py` | independent flux derivation + counterexample + cycle means |
| `verification/B23b_mutation_test.py` | mutation harness for the two phase5 scripts under dispute |

    python3 verification/B23b_verify_biot.py
    python3 verification/B23b_verify_eulerian.py
    python3 verification/B23b_mutation_test.py /path/to/phase5-head
    # all three: rc = 0

## Bottom line

Arena was right on the facts and B23 was wrong on one row: all four sources are in the library and
all four anchors check out — **4/4 CONFIRMED, 0 WRONG, 0 OVERSTATED, 0 NOT-CHECKABLE**. OCL-513's
Biot anchor is exact, the linearization script is substantive, and the Eulerian flux is now derived
correctly with a real negative control. Remaining work is record-keeping (dated roster, one anchor
fix, inventory keys), not physics.
