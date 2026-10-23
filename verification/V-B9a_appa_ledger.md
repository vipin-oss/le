# V-B9a — Separate `APPA_LEDGER.csv` for the Appendix A equation register

**Order:** `control/BRAVE_B9.md` item 1 @ `origin/claude/control` `79999f7`, base `ff1c472`
(ACCEPTED). **Access date:** 2026-10-22.
**Files created:** `APPA_LEDGER.csv` (84 rows), `V-B9a_build_ledger.py`, `V-B9a_checks.py`.
**Files NOT touched:** `EQUATION_LEDGER.csv` (176 rows), `CLAIM_LEDGER.csv` (53 rows) — verified
unchanged by `git status` before commit. No manuscript file edited; the manuscript was read only to
establish what each row asserts, never for wording.

---

## 1. Task

Build a **separate** ledger covering every Appendix A register row (the supervisor's list: `EQ-xxx`,
`EQ-10.x`, and the "appA §6/§7/§9 rows"), carrying the register's own status tags, without altering the
frozen `EQUATION_LEDGER` (176) or `CLAIM_LEDGER` (53). B8a left appA outside the 229-statement audit by
construction, so appA is a **separately frozen count**.

## 2. Method

1. `git archive origin/arena/40393d9f-le | tar -x -C /tmp/ms`; parsed the tabular rows of both
   versions of `appendices/appA_equation_register.tex` with a strict `' & '`-field split
   (`V-B9a_build_ledger.py`). Rows whose first field does not match `^EQ-` are skipped, so the
   four-row "Verification Summary" table (DERIVED / CONDITIONAL / UNVERIFIED / OPEN) is not
   mis-parsed as equations.
2. Fields kept **verbatim** from the register: `row_id`, printed equation (truncated at 200 chars only
   for CSV readability), `status_in_register`, `register_note`. Nothing was re-tagged.
3. Added four audit columns: `b9_check` (`re-checked` / `not re-checked` / `frozen in B8a`),
   `b9_verdict`, `evidence`, `scope`. **13 of the 84 rows are `CARRIED`** — no B9 evidence, legacy
   verdict unchanged, explicitly not re-audited here.
4. Execution checks for the rows I did re-check: `V-B9a_checks.py` (stdlib dimension vectors
   `(kg,m,s,K,C)`, plus the thermal-factor algebra and the source's own sum rule) and the frozen
   `V-B3d_coupled_interface.py` results.
5. **Notation for verdicts** follows my earlier V-files: `CORRECT`, `CORRECT-CONDITIONAL`,
   `WRONG-CONFIRMED`, `CARRIED` (no new evidence).

## 3. Result

### 3.1 Coverage — and one correction to the order

| version | §3 Layer I | §4 Layer II | §5 Layer III | §10 Layer VI | total |
|---|---|---|---|---|---|
| LEGACY (`phase4/manuscript/appendices/…`) | 10 | 12 | 7 | 16 | **45** |
| LIVE (`phase5/master/appendices/…`) | 10 | 13 | 7 | 9 | **39** |
| total CSV rows | 20 | 25 | 14 | 25 | **84** |

**There are no appA §6/§7/§9 rows.** Neither version contains a register table for Sections 6, 7 or 9;
the only tables are Layer I (§3), II (§4), III (§5), VI (§10), plus the status-class summary. I searched
both appendices trees and the only other equation-bearing appendix is `appB_balance_derivations.tex`
(no `EQ-` IDs). So item 1's "§6/§7/§9 rows" describes a register that does not exist in this manuscript;
I recorded the gap instead of inventing rows. **Consequence:** the equations of §6 (transport), §7
(nonlocal) and §9 (interfaces) are *not* under any equation-register audit at all. That is a coverage
hole in the manuscript, not in my ledger.

### 3.2 Status tags as printed (unchanged by me)

| version | tags present |
|---|---|
| LEGACY | VERIFIED 38, PARTIAL 2, UNCERTAIN 5 |
| LIVE | UNVERIFIED 22, CONDITIONAL 9, DERIVED 5, OPEN 3 |

The live revision converted 38 unqualified `VERIFIED` rows into 5 `DERIVED` + 9 `CONDITIONAL` + 22
`UNVERIFIED` and withdrew three rows (EQ-019, EQ-022, EQ-029 → asserted equations removed). On the
evidence below, **that downgrade was justified**: of the 7 legacy rows I can falsify, all 7 were
tagged `VERIFIED`.

### 3.3 My verdicts (84 rows)

`CORRECT` 38 · `CORRECT-CONDITIONAL` 24 · `WRONG-CONFIRMED` 9 · `CARRIED` 13.

The nine `WRONG-CONFIRMED` rows:

| row | version(s) | defect | evidence |
|---|---|---|---|
| EQ-016 | **BOTH** | GN-II in the thermal-displacement variable off by one time derivative in the coupling term | `V-B9a_checks.py` CHECK 1; Barak et al. 2023 eq (10) integrated once in time |
| EQ-017 | **BOTH** | "entropy flux" `p_i = k_ij α_,j` is short one factor `1/T` | CHECK 2 |
| EQ-022 | LEGACY | MGT row: LHS `kg s⁻⁴`, RHS `m K s⁻²` | CHECK 3 (live withdrawal correct) |
| EQ-019 | LEGACY | the `(τ_ν/2)∂_t²T_,i` TPL form | frozen `V-B8a` §3.8 (no re-run) |
| EQ-10.3 | LEGACY | index mismatch `σ̂_ji v̂_i*` + mean of a harmonic `q̂` is zero | CHECK 6 / `V-B3d` §2.4 |
| EQ-10.12 | LEGACY | `(T₀/T)` where the source prints `T/T₀` → sign of the second-order thermal flux inverts | `V-B9b` |
| EQ-10.14 | LEGACY | same factor | `V-B9b` |

The two that survive into the **live** register are **EQ-016 and EQ-017**, both still tagged
`UNVERIFIED` — i.e. the live register does not claim them, but it also still prints them, and both are
dimensionally impossible as printed. Those two are the actionable live items.

### 3.4 Version-to-version drift worth recording

* **EQ-007 / EQ-10.2 sign.** Legacy: `J_i = σ_ji v_i + q_i`. Live: `J_i = q_i − σ_ij v_j`, with
  "outward-positive convention" stated. Same physical object, opposite mechanical sign, and only the
  live row states its convention. `V-B3d` §2.4 (verified against a dissipation integral) gives
  `J = −σu̇ + θq/T₀` with tensile-positive stress, i.e. the **live** sign with an explicit convention;
  the legacy row is admissible only under a compressive-positive convention it never states.
* **EQ-10.12 / EQ-10.14** exist only in the legacy register; the live register's §10 is
  `10.1–10.6, 10.11–10.13`. Live §10 of the manuscript likewise no longer prints the three-channel
  flux. So the `T₀/T` defect is confined to the legacy tree (`V-B9b` §3.4).
* **Definitions tagged `UNVERIFIED`.** Live marks `v_i = u̇_i`, `ε_ij`, `ω_ij` as `UNVERIFIED`. They
  are definitions; a definition cannot be unverified, only non-standard. Over-conservative, not wrong.

## 4. Evidence / sources

* Registers: `phase4/manuscript/appendices/appA_equation_register.tex` (147 lines) and
  `phase5/master/appendices/appA_equation_register.tex`, at `origin/arena/40393d9f-le`, extracted
  2026-10-22 (`git archive`, no working-tree writes).
* Barak, Ahmad, R. Kumar, R. Kumar, Gupta, Awwad, Ismail (2023), *Sci. Rep.* **13** (article number not captured in my page reads),
  DOI `10.1038/s41598-023-44339-5`, gold OA: eqs (1)–(10), (45), (53)–(58) read from the publisher PDF
  (11 chunks, all fetched this session). Access level: **FULL** for the parts cited.
* `V-B3d_coupled-interface-rta.md` (frozen), `V-B8a_tpl_F6_F9_audit.md` (frozen).
* Classification basis for `[k]`, `[k*]`, `[β]`: standard SI; the register itself uses `β_ij T` in
  EQ-027, which fixes `[β] = Pa/K`.

## 5. Checks done

1. Row count reconciliation: 45 + 39 = 84; every `^EQ-` line of both files is in the CSV
   (`rows with no explicit verdict: []` printed by the builder).
2. Parse robustness: the four status-class summary rows and all `\bottomrule` lines are excluded by the
   `^EQ-` filter; the builder reports any row that does not split into exactly 4 fields (none).
3. Dimensional checks are unit-vector arithmetic, not numerical round-off; printed with exponents so
   they can be re-derived by hand (CHECK 1–3).
4. Both versions read separately, so "same in both" is a computed fact, not an assumption.
5. `git status` confirms `EQUATION_LEDGER.csv` and `CLAIM_LEDGER.csv` unmodified (see §7).

## 6. Confidence

* Coverage counts, tag preservation, §6/§7/§9 absence: **HIGH** (mechanical, reproducible).
* EQ-016, EQ-017, EQ-022 dimensional verdicts: **HIGH** as dimensional statements; **MEDIUM** as
  defect reports, because a reader could rescue EQ-016 by declaring that its `k` is `k*` and its `α` is
  `∂_tα` — but then the row is a different equation from the one printed. Both readings were checked
  and both fail.
* EQ-10.12/10.14: **HIGH** that the printed source factor is `T/T₀` (two independent renderings);
  **HIGH** that `T₀/T` inverts the second-order mean under the source's own overall minus sign.
* EQ-10.3 legacy: **HIGH** on the index mismatch (arithmetic), **MEDIUM** on the "harmonic mean" part
  in isolation (it depends on the intended use as a time average, which the row claims by its `⟨·⟩`).

## 7. NOT verified / open issues

* **13 `CARRIED` rows** have no B9 evidence: legacy EQ-005, EQ-006, EQ-015, EQ-021; legacy
  EQ-10.9/10.10/10.11/10.13/10.15; live EQ-005, EQ-006, EQ-015, EQ-021, EQ-10.13 (live EQ-10.13 also
  carried). They remain at their register status; I did not read the free-energy/GL/GN-III/MGT
  primaries, and `PDF_REQUEST_LIST.csv` still lists the closed sources.
* **Green–Lindsay (1972)** is not read (no DOI/PDF obtained), so legacy EQ-015 — the "two temperatures"
  set — is recorded as `CARRIED`, not WRONG, even though as printed it is the classical heat equation
  with `T*` for `T` and therefore cannot encode GL relaxation. The live register's withdrawal of the
  attribution is appropriate; I cannot adjudicate the original attribution.
* **EQ-019** is frozen at its B8a verdict; the B8a scope (1-D, constitutive flux axis) still applies and
  is repeated in the CSV `scope` column.
* **EQ-023–EQ-028** are checked as *standard forms* and, for 027/028, against Barak et al. eqs (3)/(6).
  The original piezothermoelastic primary (Mindlin / Nowacki) was not opened; the check is
  "consistent with the source the register names", not "matches the originator".
* **No row of this ledger was added to `EQUATION_LEDGER.csv`**, by order. appA therefore remains a
  separate frozen count: **84 rows, this file only**.
* If any downstream table quotes "appA has N rows", the correct numbers are 45 (legacy) / 39 (live) /
  84 (both, this ledger) — and **zero** rows for §6, §7, §9.
