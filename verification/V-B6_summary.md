# V-B6 — Round summary: whole-manuscript verdict counts, ranked defects, safe/unsafe map

| field | content |
|---|---|
| **Task** | B6d: merge the B6 audit with B4, give counts per verdict, rank the top defects across **all** sections, and state which parts of the manuscript are safe to build on and which are not. |
| **Manuscript** | `arena/40393d9f-le` @ **`d116771`** for B6a–B6d; the B4 rows refer to the commit B4 read (`a4a3961` baseline, re-audited under `24421c8`). Where a B4 verdict was re-tested in B6 it is marked so. |
| **Ledger state** | `EQUATION_LEDGER.csv` **176 rows**; `CLAIM_LEDGER.csv` **53 rows**. Combined: 229 statements adjudicated. |
| **Verdict** | The manuscript is **not ready for R2 sign-off**. 21 statements are wrong (13 confirmed, 4 probable, 14 unpublishable-but-unverifiable), 3 of them in the equations that carry the review's own results. The reference layer is repaired; the mathematics layer is not. |
| **Confidence** | HIGH on counts (they are a script over my own CSV). HIGH on each individual CONFIRMED item, for the reasons given per row. MEDIUM on the *ranking*, which is a judgement about consequence, not fact. |

## 1. Counts per verdict, whole manuscript

| verdict | equations (176) | claims (53) | total |
|---|---|---|---|
| CORRECT | 127 | 25 | **152** |
| CORRECT-CONDITIONAL | 34 | 10 | **44** |
| WRONG (CONFIRMED) | 10 | 7 | **17** |
| WRONG (PROBABLE) | 0 | 4 | **4** |
| DUPLICATE-DISPLAY | 2 | 0 | **2** |
| UNCLEAR | 2 | 2 | **4** |
| UNVERIFIED | 1 | 3 | **4** |
| NOT-CHECKABLE | 0 | 2 | **2** |

Read the wrong-count carefully: **17 CONFIRMED + 4 PROBABLE = 21 wrong statements out of 229**,
about 9%. That is not a catastrophic rate for a draft of this length. What matters is *where* the
21 sit.

## 2. Ranked defects across all sections

Ranked by the cost of leaving them in, not by how hard they are to fix.

| # | location | defect | verdict | source of the verdict |
|---|---|---|---|---|
| 1 | s.9.5, `sec09:117` eq. (9.9) | the secular equation for the coupled thermo-piezoelastic interface: order 16 printed where 8 is correct, and the two statements coexist in the draft | CONFIRMED-WRONG | B4 (W2), unchanged |
| 2 | `energy_flux_derivations.tex:270` | Fourier transform of the finite-horizon memory-dependent operator — the W3 symbol error | CONFIRMED-WRONG | B4 (W3), unchanged by the B4 recheck |
| 3 | s.4.4, `sec04:101` eq. (4.9) | Green–Lindsay energy equation printed with the wrong terms | CONFIRMED-WRONG | B4 (W1) |
| 4 | s.5.4–5.5, `sec05:176` eq. (5.17) | micropolar constitutive law is a **verbatim copy** of the porous one (5.14) and contains `φ_{,k}` where `φ` was just defined as a vector | CONFIRMED-WRONG | new in B6a (D1) |
| 5 | s.9.7, eq. (9.10) + per-mode numerators | absorption coefficient `A = D/|J_inc|` with `D` never scoped; reflected-mode vs total-field numerators | UNCLEAR / NOT-CHECKABLE | B4 items 4–5 |
| 6 | s.12, Tables 12-A/12-B | four wrong cells: GN-II labelled Fourier, GN-III labelled Cattaneo, MGT "order in space 3" (it is third in time), and the nonlocal column given a Cattaneo law plus a time kernel though its own source is isothermal | CONFIRMED-WRONG | new in B6a (D5–D7) |
| 7 | s.11.1, `sec11:19` eq. (11.1) | fractional heat equation dimensionally inconsistent (`a` must be `a_α`, units m²/s^α); the section warns about this error elsewhere | CONFIRMED-WRONG | new in B6a (D3); my own V-B2k:87 had flagged the class |
| 8 | s.11.1, `sec11:41` | memory kernel mis-stated as `τ^{-α}t^{α-1}/Γ(α)`; the kernel of (11.3) is `(t-τ)^{α-1}/Γ(α)` | CONFIRMED-WRONG | new in B6a (D4) |
| 9 | s.14.3, Table 14.3 + text | table sums to 96 over a corpus of 95 (two records double-counted); "seventeen more in the 1970s" where the inventory has 9 | CONFIRMED-WRONG | new in B6a (D8–D9), recounted from `phase4/literature/expanded_literature_database.csv` |
| 10 | s.13.2 | thermal-wave imaging said to *require* finite propagation speed because Fourier "makes depth resolution unphysical" — the opposite of standard practice (diffusion length `√(α/πf)` is the resolution metric) | CONFIRMED-WRONG | new in B6a (D13) |
| 11 | s.5, notation table | `φ` used for both electric potential [V] and void fraction [dimensionless], twelve rows apart | CONFIRMED-WRONG | new in B6a (D2) |
| 12 | s.5.5, `sec05:181` | Tauchert–Claus–Ariman 1968 called "the earliest" micropolar-thermoelastic formulation; Nowacki 1966, Ieşan 1968 and Eringen 1970 precede it, per the cited paper's own bibliography | CONFIRMED-WRONG | new in B6a (D12) |
| 13 | T4, `T4:19` | Rayleigh speed "0.87 c_s (Poisson solid)"; recomputed value at ν = 0.25 is **0.9194**; 0.874 is ν = 0 | CONFIRMED-WRONG | new in B6a (D10) |
| 14 | T1, `T1:17` | Moore–Gibson–Thompson dated "2019 onward"; the equation is Moore & Gibson 1960 plus Thompson 1972 | CONFIRMED-WRONG | new in B6a (D11) |
| 15 | s.11.1, `sec11:47` | fractional Cattaneo claimed to interpolate LS↔GN-II; as α→0 it gives Fourier, not GN-II | WRONG-PROBABLE | new in B6a (D14 row CL-036) |
| 16 | s.11.5 | "all limiting procedures are parameter substitutions, not rigorous limit theorems" — singular-limit theorems exist for MGT (M3AS 2019; J. Evol. Equ. 2021) | WRONG-PROBABLE | new in B6a |

**What did not change.** The B4 verdicts stand exactly: GL ordering τ₁ ≥ τ₀ > 0, secular degree 8,
W3 MDD symbol CONFIRMED-WRONG, no piezo-stiffened SH branch in the 6 mm sagittal plane. B6 found
nothing that reopens them and nothing that contradicts them.

## 3. Safe / unsafe map

**Safe to build on (audited, no defect found):**
§3.1–3.4 kinematics, stress power and the free-energy route (EQ-001…016, all CORRECT); Appendix B
(15 of 16 rows CORRECT); §10 energy balance in the classical local case (25 of 27 CORRECT); §6
transport laws apart from one unverifiable claim; §7 nonlocal formulations; §8 transforms,
Christoffel equation and root classification — **the conventions in §8 are internally consistent,
which is rarer than it should be**; §5.1–5.3 piezoelectric and piezothermoelastic constitutive
laws; the artefact appendices (appC, appD, appE, appF all verified, three of them against the
binaries).

**Unsafe — do not cite these as settled:**
§4.4 Green–Lindsay (defect 3 and CL-006); §9.5 secular equation (defect 1); §9.7 energy ratios
(defects 5 and CL-015); §5.4–5.5 constitutive laws and notation (defects 4, 11); §11.1 fractional
operator (defects 7, 8, 15); §12 and §14 tables (defects 6, 9); §13 applications evidence claims
(defect 10 and CL-046).

**Mixed:** §4.7–4.8 DPL — the equations audited CORRECT-CONDITIONAL, but the family is where the
literature itself disagrees (Quintanilla vs Rukolaine vs Kovács–Ván), so the *review's* paragraph
must present that disagreement rather than a settled law.

## 4. The honest one-paragraph assessment

The reference layer is now in better shape than the mathematics layer. After B5b the fabricated
citation is gone, 44 of 48 DOI'd references were shown to match, and the base has grown from 149 to
428 real records with the named author holes mostly closed. But B6a turned up **eleven confirmed
wrong statements in sections that B4 never read**, including two transcription errors in table
cells that carry a family's whole characterisation, an arithmetic error in the review's own corpus
statistics, and one physics inversion in the applications section. Several of these look like
copy-paste and carry-over faults rather than conceptual failures — eq. (5.17) is eq. (5.14) verbatim;
GN-II is labelled Fourier in a table whose source in my own notes says otherwise. That is
encouraging for repair: they are the kind of defects that a careful pass fixes. It is not
encouraging for the *gate*: they survived R1, R2 and a B4 audit, which means the current audit
process samples sections rather than covering them, and the coverage numbers in §1 are the first
whole-manuscript counts anyone has.

## 5. What is still not verified

1. **Read level.** No claim in this review is source-verified at full-text level. Every proposed
   citation in `CITATION_MAP.csv` is metadata or abstract only. The R2 gate's "verified by someone
   other than its writer" is satisfied for *derivations I re-derived*; it is not satisfied for
   *sources*.
2. **Author lists.** 308 of 428 base records still have a blank author field (`--enrich` blocked by
   the sandbox; Claude has ordered Arena to run it in CI). Until then no key is stable.
3. **Sections 13, 15, 16, 17** were audited only for checkable assertions; sec16 yielded nothing
   ledgerable. These are prose sections and a hostile referee will read them for overclaim, which is
   a different test from the one I applied.
4. **Figures.** All 18 are counted and present; none has been inspected at final size. appD says so
   itself, and I did not do better.
5. **The compiled PDF.** I have not compiled v1.1; the build gate remains Arena/Claude's.
6. **Thompson 1972** is still missing from the base, and **Hetnarski** is still absent as an author.

## 6. What I would fix first

1. eq. (5.17) and the `φ` collision in §5 — one afternoon, and it removes the section's worst look.
2. The four table cells in §12 and the two table cells in §14 — factual, checkable, embarrassing if
   a referee catches them first.
3. eq. (11.1) and the kernel sentence at `sec11:41` — the fractional section's structural claim
   currently rests on a mis-stated kernel.
4. The §13 thermal-imaging sentence — it is the only place where the review asserts that a
   generalized theory is *required*, and it is currently backwards.
5. Then the three carried-over B4 defects (W1, W2, W3), which are harder and already known.
