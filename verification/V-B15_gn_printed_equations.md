# V-B15 — printed GN and Tzou equations; ledger re-check; GK sourcing

**Batch:** B15. **Date:** 2026-10-22. **Input:** `control/FULLTEXT_FINDINGS_05.md` F16–F18, fetched from `origin/claude/control` at **`94f1813`** (explicit refspec `refs/heads/claude/control:refs/remotes/origin/claude/control --force`, confirmed with `git log --oneline -1`).
**Manuscript side:** the frozen section copy at `/tmp/ms403` (17 `sec*.tex` files), used read-only; `sec04_thermoelastic.tex:117-175` and `sec03_foundations.tex:178-186`. This repo still holds no `.tex`.
**Standing rule:** supervisor-transcribed equations are `PRIMARY-SOURCE-CHECKED` at team level but **not read by this verifier**; both `status` and `read_level` say so in every row written below.

---

## Task

1. Record the printed equations — GN 1992 (3.19)–(3.20), GN 1993 (3.15)–(3.17), Tzou 1995 (15)–(17) — in `FULLTEXT_FACTS.csv`, tagged `PRIMARY-SOURCE-CHECKED` (supervisor-transcribed from render), and close the B14 "untranscribed" items **except** GN 1993 (4.15).
2. Re-check EQ-044 / EQ-045 / EQ-098 / EQ-120 (type II) and EQ-047 / EQ-099 (type III) against those printed forms; list every row whose verdict changes. Give EQ-016 evidence on both routes (derivation + primary source).
3. For Green–Kubo: record Tzou (15) as the **SECONDARY** continuum source and GK 1966 as the **Boltzmann-structure primary**, with the `ell^2 = c^2 tau_N tau_R/5` consistency.

## Method

- Read F16–F18 in full; transcribed each printed equation into the facts row verbatim in ASCII (short, no page images retained).
- For each ledger row: (a) locate the manuscript display in the frozen copy, (b) compare term by term with the printed equation, (c) run a **derivative-count** check (how many time derivatives sit on each term, given `alpha-dot = theta`) and a **dimensional** check (each term reduced to base SI using the units that the printed equation itself forces), (d) state which sub-system was checked.
- For the type-II coupling, two independent routes: integrate the printed (3.16) once in time, and read the printed equation as it stands. A third, dimensional route was added afterwards.
- For GK: multiply Tzou (15) by `tau_R` and substitute `alpha = tau_R c^2/3` from (17) to test the two expressions for `ell^2` against each other.
- CSV writes via `DictReader`/`DictWriter` with the original header; before/after row and column counts compared against `HEAD`.

## Result

### 1. Facts rows (102 → 104; two new, two updated)

| key | source | printed content | status / read_level |
|---|---|---|---|
| `GreenNaghdi1993TypeII` | GN 1993, *J. Elasticity* **31**, pp. 202 | (3.15) momentum; (3.16) `c theta-ddot + [E beta* theta0/(3(1-2nu))] div u-ddot = rho0 r + kappa* lap theta`; (3.17) `c>0, kappa*>=0, lambda+2mu>=0` + "harmonic waves without damping" | PRIMARY-SOURCE-CHECKED (supervisor-transcribed) / not read by me |
| `GreenNaghdi1992TypeIII` | GN 1992, *J. Thermal Stresses* **15**, p. 261 | (3.19) momentum; (3.20) `rho0 c theta-ddot + [E beta* theta0/(3(1-2nu))] div u-ddot = rho0 r-dot + kappa lap theta-dot + kappa* lap theta`; (3.18) restrictions; (4.1),(4.2) 1-D | same |
| `Tzou1995DPL` *(updated)* | *JHT* **117**, p. 10 | (15) GK continuum law `dq/dt + (c^2 C_p/3) grad T + (1/tau_R) q = (tau_N c^2/5)[lap q + 2 grad div q]`; (16) hyperbolic temperature equation; (17) `alpha = tau_R c^2/3, tau_T = 9 tau_N/5, tau_q = tau_R` | same (was identity-only) |
| `GuyerKrumhansl1966` *(updated)* | *Phys. Rev.* **148**, 778 | unchanged Boltzmann structure; F18 block added: continuum law now sourced SECONDARY via Tzou (15), `ell^2` consistency, roles fixed | CLOSED - PRIMARY (team level) for structure, SECONDARY for the continuum law |

`LITERATURE_BASE.csv` read levels for LIT-0005, LIT-0430, LIT-0007 moved from "metadata only"/"secondary" to `PRIMARY-SOURCE-CHECKED (supervisor-transcribed from render; this verifier did not open the paper)`. `REFERENCE_GAPS.csv` GAP-04/05 marked **CLOSED for the equations**, GAP-06 extended. `V-B14_gn_mapping.md` got an append-only closure note: its items 1, 2, 5 closed; **item 6 — GN 1993 identity (4.15) — stays open by instruction**.

### 2. Ledger re-check — the verdicts that change

| row | display | verdict before | verdict now | why |
|---|---|---|---|---|
| **EQ-044** | sec04:124, `k lap alpha_GN = rho c_e alpha-ddot_GN + beta T0 u-ddot_{i,i}` | CORRECT | **WRONG (CONFIRMED)** | one time derivative too many on the coupling term |
| **EQ-098** | energy_flux:130, identical display | CORRECT | **WRONG (CONFIRMED)** | same defect (duplicate) |
| EQ-045 | sec04:131, `p_i = k_ij alpha_{,j}` | CORRECT | CORRECT | structure untouched; **evidence caveat**: the flux law is not printed on the transcribed pages |
| EQ-120 | energy_flux:137, same as EQ-045 | CORRECT | CORRECT | same caveat |
| EQ-047 | sec04:156, `K T_{,ii} + k* T-dot_{,ii} - rho C_e T-ddot = ...` | CORRECT | CORRECT | structure matches (3.20); **letters exchanged** vs GN (`K = kappa*`, `k* = kappa`) |
| EQ-099 | energy_flux:165, identical to EQ-047 | CORRECT | CORRECT | same |
| EQ-119 | `alpha-dot = T` | CORRECT | CORRECT | not printed on these pages (implied) |
| EQ-016 | sec03:182, Clausius–Duhem | CORRECT | CORRECT | untouched; **ID-collision note only** |

**The two flips are EQ-044 and EQ-098, and nothing else moves.**

### 2a. Why EQ-044/EQ-098 flip — three routes

The manuscript sets `alpha-dot_GN = T` (its own eq:4.12 area, `sec04:120`).

- **Route (a), derivation from the printed (3.16).** Printed: `c theta-ddot + C div u-ddot = kappa* lap theta`. This is the once-differentiated energy balance; integrating once, and using `lap theta = lap alpha-dot`, gives `c alpha-ddot + C div u-dot = kappa* lap alpha`. The coupling carries **one** dot against `alpha-ddot`. The manuscript has `div u-ddot`.
- **Route (b), primary source as printed.** The printed equation pairs the coupling with `theta`/`alpha` terms carrying the *same* number of derivatives (two on `theta-ddot`, none on `lap theta` once integrated). The manuscript pairs `div u-ddot` (two dots) with `lap alpha` (no dots) and `alpha-ddot` — a mixture of the differentiated and the integrated form.
- **Route (c), dimensions.** With `kappa*` taking the units forced by (3.16) itself (`J m^-1 s^-2 K^-1`), `k lap alpha` and `rho c_e alpha-ddot` are both `J m^-3 s^-1`, while `beta T0 div u-ddot` is `J m^-3 s^-2`. The manuscript display is internally inconsistent by one inverse time — exactly the term that route (a) says is over-differentiated.

Same conclusion as the BRAVE B9 verdict. Scope: **one term of one display** (and its duplicate); the `alpha-ddot` and `lap alpha` terms are correct. The surrounding text does not repeat the error.

### 2b. EQ-047/EQ-099 — correct, but the letters are GN's in the wrong slots

Term by term against printed (3.20) — `kappa lap theta-dot + kappa* lap theta`:

- manuscript `K T_{,ii}` ↔ GN `kappa* lap theta` ⇒ `K = kappa*`;
- manuscript `k* T-dot_{,ii}` ↔ GN `kappa lap theta-dot` ⇒ `k* = kappa`.

Dimensionally consistent (`K` must be `J m^-1 s^-2 K^-1`, `k*` must be `W m^-1 K^-1`), so the structure is right and the verdict stands. The defect is presentational and cross-display: the manuscript writes lower-case `k` for the type II constant (`GN kappa*`) in eq.(4.11) and upper-case `K` for the same role in eq.(4.14), while the symbol `k*` means GN's `kappa`, not GN's `kappa*`. Anyone comparing to GN will read the conductivities as exchanged. **One sentence or a symbol table fixes it.**

### 2c. EQ-016 — both routes, and an identifier collision

- **Derivation route:** the display `sigma_ij eps-dot_ij - rho(psi-dot + s Theta-dot) - q_i Theta_,i/Theta >= 0` is the standard Clausius–Duhem inequality obtained from the internal-energy balance `eq:3.13` with `psi = e - Theta s`; the substitution is standard and the sign is right (verified in `sec03_foundations.tex:180-186`).
- **Primary-source route:** Green & Lindsay 1972's own entropy production (relayed, F1) has the same structure with their `psi`; no term in the manuscript display diverges.
- **Collision:** F17 writes "manuscript EQ-016" while quoting `k lap alpha = rho c alpha-ddot + beta T0 u-ddot`. That display is **sec04 eq.(4.11) = ledger EQ-044/EQ-098**, not ledger EQ-016, which is `eq:3.16` at `sec03:182` (checked: `\label{eq:3.16}` is on line 185 there). The note of both routes was therefore written on **EQ-044**, and EQ-016 carries a cross-reference saying so. Treating F17's "EQ-016" as the Clausius–Duhem row would have been wrong.

### 3. Green–Kubo sourcing and the `ell^2` consistency

- **Roles.** GK 1966 (*Phys. Rev.* **148**, 778) stays the **primary for the Boltzmann-derived structure** — eqs (1a)/(1b), (2a)/(2b), (4), (6)/(8)/(10) and `lambda^2 = c^2 tau_N tau_z/5`. **Tzou 1995 (15) is the `SECONDARY` continuum source**: it is GK's law *as quoted by Tzou*, and a paper citing the continuum form must cite Tzou (15) and tag it `SECONDARY-SOURCE`, not attribute a ready-made flux law to 1966.
- **`ell^2` consistency (my algebra on the printed equations).** Multiplying (15) by `tau_R`:

  `tau_R dq/dt + q = -(c^2 C_p tau_R/3) grad T + ell^2 [ lap q + 2 grad div q ]`, with `ell^2 = c^2 tau_N tau_R/5`.

  Tzou (17) prints `alpha = tau_R c^2/3`, so `ell^2 = (3 alpha/tau_R) * tau_N tau_R/5 = 3 alpha tau_N/5`. The two expressions are algebraically identical, which is the check that Tzou's `tau_R` and GK's `tau_z` are the **same quantity** (Ziman-averaged R-process time). **The `tau_z`-vs-`tau_R` flag stays CLOSED** (`control/FULLTEXT_FINDINGS_03.md`) and is not reopened here.
- **Derived, not printed:** DPL admissibility `tau_q > tau_T` combined with (17) gives `tau_R > 9 tau_N/5`. That inequality is **mine**, and the facts row labels it as such.
- **Consequence for the review:** in the phonon case DPL is a stretched-time image of the GK law (`tau_T = 9 tau_N/5`), not an independent postulate. Any sentence claiming DPL is independent of kinetic theory must be hedged to the non-phonon setting.

### 4. New claim rows (53 → 55)

`CL-054` at `sec04:117` — heading "Green–Naghdi type II theory (1991)" — **WRONG (CONFIRMED)**: the type II primary is 1993.
`CL-055` at `sec04:151` — heading "Green–Naghdi type III theory (1993)" — **WRONG (CONFIRMED)**: the type III primary is 1992.
Both are year attributions in headings that propagate to the bibliography; the equations in those subsections are separate rows above.

## Evidence / Sources

- **GN 1992**, *J. Thermal Stresses* **15**, 253–264, `10.1080/01495739208946136` — printed (3.18)–(3.20), (4.1),(4.2) relayed by F16 (supervisor, page renders); **I have not opened it**.
- **GN 1993**, *J. Elasticity* **31**, 189–208, `10.1007/BF00044969` — printed (3.15)–(3.17) relayed by F17; **not opened by me**. The identity (4.15) remains untranscribed.
- **Tzou 1995**, *J. Heat Transfer* **117**, 8–16, `10.1115/1.2822329` — printed (15)–(17), p. 10, relayed by F18; **not opened by me**.
- **Guyer & Krumhansl 1966**, *Phys. Rev.* **148**, 778 — structure and `lambda^2` from F10–F12; **not in the library, not opened by me**.
- Manuscript: frozen copy `/tmp/ms403`, `sec04_thermoelastic.tex` lines 117–175 (`eq:4.11` on 127, `eq:4.14` on 159, `eq:4.15` on 172), `sec03_foundations.tex` lines 178–186 (`eq:3.16` on 185). Access 2026-10-22, read-only, not part of this repo.
- Local: `verification/FULLTEXT_FACTS.csv`, `EQUATION_LEDGER.csv`, `CLAIM_LEDGER.csv`, `LITERATURE_BASE.csv`, `REFERENCE_GAPS.csv`, `V-B14_gn_mapping.md`.

## Checks done

- **Two independent routes** for the type-II coupling (integration of the printed equation; reading the printed equation as it stands), plus a **third** dimensional route that flagged the same term independently.
- **Second-method check** for `ell^2`: two algebraic expressions (`c^2 tau_N tau_R/5` and `3 alpha tau_N/5`) agree identically; the substitution used is Tzou's own (17), not an assumption.
- **Term-by-term mapping** of the type III display against (3.20), including the dimensional units forced by each printed equation, which is what distinguishes "structure wrong" from "letters exchanged".
- **Anchor honesty:** the display anchors (`sec04:124`, `sec04:156`) point at the introducing line, matching the ledger's convention; the equations themselves sit on lines 127 and 159. The `energy_flux:*` duplicate anchors are **not** in the frozen copy — those rows were verified as *identical displays* by content, not by opening that file, and the rows say so.
- **Self-correction:** my own B14 note on EQ-047 restated the equation with `k` on `lap T-dot` and `k*` on `lap T` (GN's letters) while the manuscript's LaTeX is the other way round; the new note records that the *manuscript's* letters are exchanged relative to GN, so the earlier restatement is not to be quoted as the manuscript's form.
- **No invented transcription:** every equation quoted is either from F16–F18 or from the frozen manuscript copy; no page image, PDF or long passage entered the repo.
- **Integrity:** FULLTEXT_FACTS 102→104 (2 new, 2 updated), EQUATION_LEDGER 176→176 (8 rows), CLAIM_LEDGER 53→55, LITERATURE_BASE 499→499 (3 read levels), REFERENCE_GAPS 16→16 (3 rows); no duplicate keys; column counts unchanged.

## Confidence

- **HIGH** that EQ-044/EQ-098 are wrong on the coupling term: three routes agree and one of them is dimensional.
- **HIGH** that EQ-047/EQ-099 are structurally right and only mis-lettered — the units force each symbol's slot.
- **HIGH** for the `ell^2` identity as algebra on Tzou (17).
- **MEDIUM** for anything depending on the transcription itself (e.g. whether (3.16)'s source term is `r` or `r-dot`, whether the bare `c` carries `rho0`): I have not seen the render.
- **MEDIUM** that the manuscript's `k` (eq. 4.11) and `K` (eq. 4.14) are meant to be one constant — that is a reading of intent, flagged as a question for the authors, not a verdict.

## NOT verified / open issues

1. **GN 1993 identity (4.15)** — still untranscribed **by instruction**; no energy-identity claim can be signed off.
2. **The flux laws** `q = -kappa* grad alpha` / `p_i = k_ij alpha_{,j}` are **not** on the transcribed pages, so EQ-045/EQ-120 still rest on my earlier V-B2d/V-B3d reading. A one-line transcription from the GN 1993 constitutive section would close them.
3. **`alpha-dot = T`** is not printed in F16/F17 either; standard, but the row says so.
4. **Transcription uncertainties not resolved:** (3.16) prints `c theta-ddot` with a bare `c` (does `rho0` multiply it?), and prints `rho0 r` against a twice-differentiated left side (is `r` a rate?). Neither is used in any verdict.
5. **GN 1991 still unread** (scanned); the "all three types introduced there" statement is relayed.
6. **Everything here is a report, not a fix** — sec.4.5/4.6 equation error, the two heading years, the symbol clash and the `Tzou1997` key must be changed by the authors; this verifier cannot edit the manuscript (no `.tex` in this repo).
7. **The manuscript build used for line anchors is a frozen copy**; if the current build renumbers subsections, `sec04:117` / `sec04:151` must be re-derived, not assumed.
