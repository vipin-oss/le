# V-B6a — Equation and claim audit of the sections not previously covered

| field | content |
|---|---|
| **Task** | B6a: apply the same EQUATION_LEDGER / CLAIM_LEDGER procedure to the sections and artefacts not yet audited — sec05, sec08, sec11, sec12, sec13, sec14, sec15, sec16, sec17, appendices appC, appD, appE, appF and tables T1–T5, T8. Same columns, same process rule (grep my own earlier V-files first; state which sub-system a check covers). |
| **Manuscript read** | branch `arena/40393d9f-le`, commit **`d116771`** ("Improve build warning context"), tree `phase5/master`, read-only, extracted with `git archive` to `/tmp/mstree`. All line numbers below are line numbers in that commit. |
| **Rows added** | `EQUATION_LEDGER.csv` **EQ-131 … EQ-176** (46 rows, total 176). `CLAIM_LEDGER.csv` **CL-030 … CL-053** (24 rows, total 53). |
| **Result** | 10 CONFIRMED-WRONG equations, 2 duplicate displays, 7 CONFIRMED-WRONG claims, 4 PROBABLE-WRONG claims, 3 unverifiable claims, 2 arithmetic errors in a table, and 3 artefact claims verified exactly. Two of the wrong items are citation-level (an overclaim of priority, and a family-dating error of 59 years), one is a physics inversion in the applications section. |
| **Confidence** | **HIGH** on every row marked CONFIRMED, because each is either internal to the read commit (duplication, dimension, arithmetic on a table I can recount) or checked against a source fetched in this session. **MEDIUM** on the four PROBABLE rows, which turn on how a phrase is read. |
| **NOT verified** | sec13, sec15, sec16 and sec17 are prose-heavy and I audited only the checkable assertions in them; sec16 yielded no ledgered row at all. I did not compile the LaTeX, did not check cross-references mechanically beyond the one recorded in CL-049, and did not read any cited paper's full text. |

## 1. Coverage after B6a

| unit | new rows | verdicts |
|---|---|---|
| sec05 multiphysics | 18 eq, 5 claim | 1 WRONG, 1 notation collision, 2 CONDITIONAL, rest CORRECT |
| sec08 mathematical methods | 8 eq, 5 claim | no WRONG equations; 2 unverifiable claims; the transform conventions are internally consistent |
| sec11 advanced | 8 eq, 3 claim | 3 WRONG (two confirmed, one probable) |
| sec12 comparative | 4 eq, 2 claim | 3 WRONG table cells |
| sec13 applications | 0 eq, 2 claim | 1 WRONG, 1 UNVERIFIED |
| sec14 taxonomy | 2 eq, 4 claim | 1 arithmetic WRONG, 1 count WRONG, 2 CORRECT |
| sec15 challenges | 0 eq, 1 claim | 1 UNCLEAR cross-reference |
| sec17 conclusions | 0 eq, 1 claim | 1 CORRECT-CONDITIONAL |
| appC / appD / appE / appF | 4 rows | 3 CORRECT (verified against binaries), 1 CORRECT |
| T1 / T4 | 3 rows | 1 WRONG (family date), 1 WRONG (Rayleigh constant), 1 CONDITIONAL |
| sec16 future | 0 | prose only; nothing with a truth value that could be checked |

## 2. The confirmed defects, ranked by cost to the paper

**D1 — eq:5.17 is a verbatim copy of eq:5.14, and its symbol is undefined** (`sec05:176`). Five lines earlier the section defines `φ_i` as the microrotation *vector*; the copied constitutive law then contains `d_{ijk}φ_{,k}`, the gradient of a *scalar*. Whatever is meant, the display as printed is not a micropolar constitutive law, and it duplicates the porous one exactly. A referee who reads §5.4 and §5.5 in sequence will see the same equation twice with two different physical readings. This is the most damaging single item in the section, because the two theories it conflates are supposed to be the section's content.

**D2 — `φ` appears twice in the Section 5 notation table** (`sec05:265` and `sec05:269`): once as electric potential [V], once as void volume fraction [dimensionless]. Twelve rows apart in one table. Every equation in the section containing `φ` — eq:5.3, 5.8, 5.14, 5.16, 5.17 — is ambiguous in the table's own terms. This and D1 are the same defect seen twice.

**D3 — eq:11.1 is dimensionally inconsistent** (`sec11:19`): `{}^CD_t^α T = a∇²T` balances only if `a` carries units m²/s^α. My own V-B2k line 87 flagged this as a defect class in this literature, and here it is in the manuscript. It is worse for being self-noticed: twelve lines later (`sec11:54`) the text warns that "the dimension of the relaxation parameter changes with the order … a common source of error", and commits the identical error for the diffusivity. Fix: write `a_α`.

**D4 — the fractional/MDD kernel statement is wrong** (`sec11:41`). The text identifies the memory kernel of eq:11.3 as `τ^{-α}t^{α-1}/Γ(α)`. The kernel of eq:11.3 is `(t-τ)^{α-1}/Γ(α)` — a function of the elapsed time only. The printed expression has a stray `τ^{-α}` and a `t` that cannot sit inside a `τ`-integral. This matters because the sentence is the one that establishes the section's central structural claim, that fractional and memory-dependent descriptions are two representations of one object.

**D5 — the nonlocal column of Table 12-B has the wrong physics** (`sec12:49`): thermal law "Cattaneo", characteristic time "τ (kernel)", sourced to `\cite{Eringen1972}`. That source's Crossref title, verified this session, is *"Linear theory of nonlocal elasticity and dispersion of plane waves"* — an isothermal theory with no heat conduction. The MDD and nonlocal rows also appear transposed: memory-dependence is nonlocality in **time**, Eringen nonlocality is nonlocality in **space**, yet both rows list `τ (kernel)` and both list a length `ℓ`. The table exists to separate exactly these two mechanisms.

**D6 — MGT "order in space = 3"** (`sec12:55`). MGT is third order in **time**, second in **space** (`τθ_{ttt}+θ_{tt}=c²∇²θ+…`; my V-B2i line 20). Single-cell error, but it is the cell that carries the "higher-order" characterisation.

**D7 — GN thermal laws mislabelled** (`sec12:25`): GN-II as "Fourier", GN-III as "Cattaneo". My V-B2d records all three laws explicitly — I: `q=-kθ_{,i}`; II: `q=-k*α_{,i}`; III: `q=-(k*α_{,i}+kθ_{,i})`. Type II contains no Fourier term at all, and neither type is Cattaneo. Sub-system covered: the Green–Naghdi flux-law table in `V-B2d_green-naghdi-I.md` lines 29–31 only.

**D8 — Table 14.3 sums to 96 over a corpus of 95** and the percentages use 96 in the denominator (24/96 = 25.0%, 15/96 = 15.6%, 13/96 = 13.5% — all exact). The inventory label column shows the cause: `ls_mdd_piezo` and `mgt_mdd_piezo` each satisfy two rows, so two records are counted twice. Needs either a "counted in more than one family" note or a corpus of 96.

**D9 — "seventeen more fall in the 1970s"** (`sec14:89`). Counted from the inventory year column: 1970s = **9**. The neighbouring figures are right (pre-1970 = 17, 2010s+2020s = 39), which makes the error harder to spot and it is the number that supports the "bimodal" reading.

**D10 — the Rayleigh constant** (`T4:19`): `c_R ≈ 0.87 c_s (Poisson solid)`. Recomputed by bisection on `η³-8η²+(24-16ξ)η-16(1-ξ)=0`: **0.9194** at ν = 0.25 (Poisson solid), 0.9274 at ν = 0.30, 0.9320 at ν = 0.33. The value 0.874 is the ν = 0 limit. Right number, wrong material — low by 5% for the case named.

**D11 — "Moore–Gibson–Thompson, 2019 onward"** (`T1:17`). A milestone table dates the family 59 years late; the equation is Moore & Gibson 1960 (`10.2514/8.8418`, Crossref-verified this session, 132 citations) and Thompson 1972. 2019 is the date of Quintanilla's analysis, which is the cell's own source lead.

**D12 — the overclaim of priority** (`sec05:181`): Tauchert–Claus–Ariman 1968 as "the earliest of the micropolar-thermoelastic formulations". The cited paper's own reference list — fetched this session via Crossref — contains Nowacki 1966 (*Couple stress in the theory of thermoelasticity*, Bull. Acad. Pol. Sci. 14:97), Ieşan 1968, and Eringen 1970 (*Foundations of Micropolar Thermoelasticity*, Springer). All precede 1968. Access level: secondary source, which suffices to falsify "earliest" but not to name the true first paper.

**D13 — a physics inversion in the applications section** (`sec13:38`): thermal-wave inspection said to require a finite propagation speed because an infinite one "makes the depth resolution unphysical". Fourier diffusion supplies a finite thermal diffusion length `μ = √(α/πf)`, which *is* the standard depth-resolution metric of photothermal imaging. A parabolic equation does not give unlimited resolution depth; it gives exponential decay with a defined 1/e depth. This is the one place where a generalized theory is called "a requirement" rather than a refinement, so the error is load-bearing, not cosmetic.

**D14 — "all limiting procedures … are parameter substitutions, not rigorous limit theorems"** (`sec11:122`). False as an absolute: Crossref returned singular-limit theorems for MGT this session (Bongarti–Charoenphon–Lasiecka, *J. Evol. Equ.* 2021, 32 cites; M3AS 2019, 58 cites), both now in my base. The defensible version is narrower: such theorems exist for MGT and for classical↔LS, but not across every family.

## 3. What checked out — including three artefact claims verified against binaries

Recorded because an audit that only reports failures is not an audit.

* **appF's PDF metadata is exactly right.** Decompressing the object streams of `phase5/master/v1.0-baseline.pdf`: `/Producer = pdfTeX-1.40.25`, `/CreationDate = D:20231114221320Z`, 161 page objects, `/Count 161`. All three asserted numbers match.
* **appD's figure inventory is right**: 18 `.svg` and 18 `.pdf` in `figures/source/`, 18 `.svg` in `figures/rendered/`. **appE's table inventory is right**: 8 files, T1–T8.
* **sec14's metadata counts are four for four**: 95 records, 48 non-blank DOIs, 13 open-access flags, 12 full-text plus 1 methodology.
* **The transform conventions are consistent** (eq:8.1 `e^{-iωt}` with eq:8.6 `e^{+iωt}` forward) — the most common sign trap in this literature is avoided, and the section says why.
* **eq:8.77's evanescent-flux statement is correct and non-trivial**, and agrees with my independent V-B3a conclusion.
* **Sec 11's Caputo Laplace rule, Caputo definition, hereditary form, two-temperature relation** are all correct.
* **appC's "no benchmark was executed"** is consistent with every BM status line in the same appendix. That is honest labelling, and it is recorded as such.

## 4. Checks done

1. Read all nine sections and four appendices at commit `d116771`; grepped for display equations first (`sec12`, `sec13`, `sec15`, `sec16`, `sec17` and appC–appF contain **no** `equation` environments — sec14 has two, so the "equation audit" for those units is necessarily a claim audit).
2. Re-derived or re-computed rather than eyeballed: the Rayleigh cubic (bisection, three Poisson ratios), every dimensional balance flagged in §2, and the fractional kernel of eq:11.3.
3. Recounted the taxonomy table and the inventory metadata directly from `phase4/literature/expanded_literature_database.csv` at the read commit.
4. Grepped my own earlier V-files before calling anything wrong (B4 arbitration rule): `V-B2k:87` (fractional dimension), `V-B2d:29-31` (GN flux laws), `V-B2i:20` (MGT time order), `V-B2m:78` (gradient sign/well-posedness), `V-B3a` (evanescent flux). Where a verdict rests on one of those, the ledger note names the file and line and states the sub-system covered.
5. Verified three artefact claims against the actual binaries/counts rather than against the prose.
6. Fetched two Crossref records this session to settle two of the items: `10.1007/s00707-022-03399-w` (Sherief & Hussein — reference list supplies Nowacki 1966, Ieşan 1968, Eringen 1970) and `10.1016/0020-7225(68)90037-2` (Tauchert, Claus Jr., Ariman, IJES 6(1):37–47, 99 citations — confirms the bib entry is correctly corrected and confirms the 1968 date).

## 5. Confidence and what would overturn it

The arithmetic items (D8, D9, D10, appF/appD/appE, sec14:57) are reproducible by anyone with the same two files and six lines of Python; they are as certain as the read commit. The table-cell items (D5–D7) are certain modulo my reading of the manuscript's intended column identity. D12 and D13 are certain as statements but their *importance* is a judgement. D14 depends on whether "limiting procedures" is read as covering the MGT singular limits — I read it as covering them, and said so.

Nothing here re-opens a B4 verdict. The B4 results (GL ordering τ₁ ≥ τ₀ > 0, degree 8, W3 MDD symbol CONFIRMED-WRONG, no piezo-stiffened SH branch in the 6mm sagittal plane) stand unchanged.
