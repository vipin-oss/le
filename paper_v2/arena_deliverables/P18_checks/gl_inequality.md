# Green–Lindsay: which relaxation time sits where, and which inequality the sources state

**Task.** P18, item 1. **Date.** 2 November 2026.
**Question.** In Green & Lindsay (1972), Ignaczak & Ostoja-Starzewski (2010), Hetnarski–Ignaczak (1999) and Chandrasekharaiah (1998): which relaxation time multiplies θ̇ in the stress and entropy relations, which multiplies θ̈ in the energy equation, and what inequality between the two is stated, with equation and page. Then map onto the review's notation and say which order the review must print.

---

## 0. What this deliverable is, and what it is not — read this first

**No copy of any of the four sources exists in this working environment.** The workspace contains the manuscript, the repository, and nothing else: a search of the workspace returns one PDF, the manuscript itself. The sources are held in the author's library, not here, and the repository is by rule free of PDFs.

Consequently **nothing in this file is a fresh read of a primary source.** Every statement below is one of two things, and each is labelled:

| Label | Meaning |
|---|---|
| **RECORDED** | A page-level read already recorded in this project's own evidence registers, with the file and row given so it can be checked. The quote and the page were obtained from the printed source in an earlier pass; they are not re-read here. |
| **EXTERNAL** | Verified in this session against a bibliographic registry (Crossref), with the query given. |
| **NOT RECORDED** | The source is held, but this particular item was never recorded, and it cannot be read here. |
| **NOT IN LIBRARY** | No copy is held at all. |

This distinction matters for the one question that the task exists to settle: the direction of the inequality is **NOT RECORDED** in every source, and it is therefore **not established** in this deliverable. Section 4 says exactly what that implies for the manuscript, and what one page settles it.

---

## 1. Green & Lindsay (1972), *Journal of Elasticity* 2, 1–7

**Held in the library:** yes (`green1972.pdf`, matched by title on the first page; library inventory v3, line 39). **Catalogue level:** R2 — bibliographic fields verified, not a full-text verification (`refs_catalogue_check.csv`, key `Green1972`, batch 1).

### 1.1 What is recorded

| Item | Recorded content | Where it is recorded | Status |
|---|---|---|---|
| Identity and scope | "an alternative generalization of classical thermoelasticity"; the linear heat-conduction tensor is symmetric; "the theory allows for second sound effects" | `claim_register.csv` row CR100; abstract, printed p. 1 | **RECORDED** |
| Constitutive development | homogeneous-body constitutive development and the symmetry result, Eqs. (3.12)–(3.19), **printed p. 4** | `reports/Q3_PRIMARY_SOURCE_CHECKS.md`, section "Green & Lindsay (1972)" | **RECORDED** (page and equation range; the equations themselves are not transcribed) |
| Linearisation and heat flux | small-field linearisation, constitutive and heat-flux equations, coefficient restrictions and the linearised field equation, Eqs. (4.1)–(4.13), **printed p. 5** | same file, same section | **RECORDED** (range only) |
| Coefficient restrictions | imposed "from the entropy inequality (Eqs. (4.8)–(4.10), (4.14))"; further positivity conditions at Eq. (4.14) | same file, same section | **RECORDED** (location only) |
| Additional conditions and uniqueness | "additional positivity conditions and uniqueness identity in Eqs. (4.14)–(4.17)", **printed p. 6**; the sufficient conditions are cited at Eq. (4.16) | same file; `R4B_SOURCE_FINDINGS.md` line 275 | **RECORDED** (location only) |
| **Which coefficient multiplies θ̇ in the stress** | "Two temperature-rate coefficients do enter the linear equations, **α in the stress** and **h in the energy equation**" | `PARTLY_SUPPORTED_EDIT_SHEET_2026-11-01.csv`, row CR100 | **RECORDED** |
| **Which coefficient multiplies θ̈ in the energy equation** | **h** — same row, "h in the energy equation" | as above | **RECORDED** |
| Naming | the word "relaxation" does not occur in printed pp. 1–7; the paper does not call α and h relaxation times | row CR100 | **RECORDED** |
| The heat-flux equation (4.11) | "includes a temperature-gradient term and **may include a temperature-rate term in the general form**; the source does not write a q̇ evolution law"; in a centrosymmetric body the vector coefficient multiplying the temperature rate vanishes | `R4B_SOURCE_FINDINGS.md` line 356; Q3 check, same section | **RECORDED** |
| **The inequality between α and h** | **nothing.** The restrictions are located (Eqs. (4.8)–(4.10) p. 5; Eq. (4.14) p. 6) but their content is nowhere transcribed, and the Q3 check states expressly that "the source's coefficient notation has **not been mapped** to the manuscript's … relaxation-time ordering" | `reports/Q3_PRIMARY_SOURCE_CHECKS.md`; `R4B_SOURCE_FINDINGS.md` line 275 | **NOT RECORDED** |

### 1.2 Consequence for the review's present text

The review says of GL (p. 13) that "the heat flux is taken in its Fourier form, as is usual for the isotropic case". The recorded source finding is narrower: (4.11) *may* carry a temperature-rate term in the general (non-centrosymmetric) case. The review's sentence is defensible as a statement about the isotropic case, and the qualifier is already in the text — but it should not be repeated elsewhere without the qualifier, and it should not be used to place GL outside the flux template without saying that the placement holds for the isotropic form.

---

## 2. Ignaczak & Ostoja-Starzewski (2010), *Thermoelasticity with Finite Wave Speeds*, OUP

**Held in the library:** yes — read in P13 with 24 evidence rows; the print/PDF offset is recorded as "printed page = PDF page − 19" (`books_status.csv`). **ISBN:** 978-0-19-954164-5.

### 2.1 What is recorded (all at **printed p. 21**)

| Item | Recorded content | Where | Status |
|---|---|---|---|
| **(1.3.30)** stress | `S_ij = C_ijkl E_kl + M_ij(ϑ + t1 ϑ̇)` — the temperature-rate term in the **stress carries t1** | `P13_books/evidence.csv` line 20 | **RECORDED** (equation transcribed) |
| **(1.3.31)** entropy | `θ0 η = −θ0 M_ij E_ij + C_E(ϑ + t0 ϑ̇)` — the temperature-rate term in the **entropy carries t0** | `P13_books/evidence.csv` line 21 | **RECORDED** (equation transcribed) |
| **(1.3.32)** | no row; content unknown | — | **NOT RECORDED** |
| **(1.3.33)** heat flux | "Equation (1.3.33) represents the classical Fourier law of heat conduction", with footnote 16 | `P13_books/evidence.csv` line 22 | **RECORDED** |
| **Inequality between t0 and t1** | nothing recorded, in any file | — | **NOT RECORDED** |

Note the placement: in this book **t1** is the stress coefficient and **t0** the entropy/energy coefficient — the opposite assignment to the one a reader of the review's Table 15 might assume, because the review calls the stress coefficient τ1 and the energy coefficient τ0. The two notations agree on *which* coefficient sits where; they differ in the *index* attached to each. That is the first of the two convention traps here.

### 2.2 The energy equation

The review writes the GL energy equation as `k θ,ii = ρc(θ̇ + τ0 θ̈) + T0 β_ij ε̇_ij` (Eq. (39), p. 26). Differentiating the recorded entropy relation (1.3.31) and using the energy balance turns the `t0 ϑ̇` of the entropy into a `t0 θ̈` in the energy equation, so **t0 is the coefficient of θ̈** and corresponds to the review's τ0. This is arithmetic on a recorded equation, not a further source claim; it is flagged as **DERIVED** wherever it is used below.

---

## 3. Hetnarski & Ignaczak (1999) and Chandrasekharaiah (1998)

| Source | Held? | What is recorded | Status for this task |
|---|---|---|---|
| **Hetnarski & Ignaczak (1999)**, *J. Thermal Stresses* 22 | Catalogue level R2 only (`refs_catalogue_check.csv`); one pass marked it SOURCE NOT AVAILABLE, another read **p. 2** for its survey role only, with the note that the copy's text layer is letter-spaced | no equation, no constitutive relation, no inequality | **NOT RECORDED** |
| **Hetnarski & Ignaczak (2000)**, *Int. J. Solids Struct.* | Yes (`hetnarski2000.pdf`, inventory v3 row 83) | inventory entry only; no content rows anywhere | **NOT RECORDED** |
| **Chandrasekharaiah (1998)**, *Appl. Mech. Rev.* 51 | Yes (`chandrasekharaiah1998.pdf`, inventory v3 row 88) | structural read only (P15: 8 unnumbered sections, 338 stated references, no figures, no tables) | **NOT RECORDED** at equation level |

So of the four sources named in the task, **two** contribute recorded equations (GL, and I&O 2010), and **none** contributes a recorded inequality.

---

## 4. The answer to the question asked, stated plainly

### 4.1 The mapping is established

| Quantity | Green & Lindsay 1972 | Ignaczak & Ostoja-Starzewski 2010 | The review (§4.2.3, Eq. (39), p. 26) |
|---|---|---|---|
| coefficient of θ̇ in the **stress** | **α** (recorded) | **t1** (recorded, (1.3.30)) | **τ1** |
| coefficient of θ̇ in the **entropy**, hence θ̈ in the **energy** | **h** (recorded) | **t0** (recorded, (1.3.31)); θ̈ form **derived** | **τ0** |
| heat flux | (4.11): gradient term, possibly a temperature-rate term in the general form; no q̇ law (recorded) | (1.3.33) classical Fourier (recorded) | "Fourier's here" |

Therefore:

* a source statement **t1 ≥ t0** converts to **τ1 ≥ τ0 ≥ 0** in the review's notation;
* a source statement **t0 ≥ t1** converts to **τ0 ≥ τ1 ≥ 0**;
* an GL statement **h ≥ α** converts to **τ0 ≥ τ1 ≥ 0**, and **α ≥ h** to **τ1 ≥ τ0 ≥ 0**.

Conversion is mechanical; there is no freedom in it. The only thing missing is which direction each source states.

### 4.2 What is not established, and why it is not guessed

**The direction is not established.** No file in this repository records it, no copy of GL 1972, I&O 2010, Hetnarski–Ignaczak 1999/2000 or Chandrasekharaiah 1998 exists in this environment, and the Q3 check that reviewed GL's printed pp. 4–6 says so in terms: the coefficient notation "has not been mapped … to their proposed **relaxation-time ordering**".

It would be easy to write "τ1 ≥ τ0 ≥ 0" here and be right half the time. That would be worse than useless, because the answer decides which of two printed tables in the manuscript is wrong, and because the manuscript is in a state where a referee has already been told (P17, finding R5) that the two tables disagree.

### 4.3 What the manuscript prints today — and the one thing that is certain

| Where | Statement | Cite for the inequality |
|---|---|---|
| §4.2.3, text under Eq. (39), **p. 26** | "with **τ0 ≥ τ1 ≥ 0**" | none |
| **Table 15**, p. 85, GL row, column "Well-posed when" | "**τ0 ≥ τ1 ≥ 0**" | none (table cites nothing) |
| **Table 22**, p. 114, row (39) | "**τ1 ≥ τ0 > 0**", basis: "Primary text (Green and Lindsay 1972); no τ0 term on the strain-rate coupling" | no page |

**Certain, without any source read:** the manuscript cannot be right in both places today. At least one of these three printed statements is wrong, and none of them carries a page or equation number from GL or from I&O. That is a defect independent of which ordering is correct.

**A second, separable defect in the same row of Table 22.** The register's basis note says "no τ0 term on the strain-rate coupling", which describes an energy equation whose coupling term carries **τ1**: `ρc(θ̇ + τ0θ̈) = kθ,ii + T0β(ε̇ + τ1ε̈)`. The review's Eq. (39) as printed carries **no relaxation time at all** on `T0 β_ij ε̇_ij`. So Eq. (39) and its own register entry describe two different equations. Whatever the correct GL form, one of the two must be corrected, and the register note is the more likely to be describing the source (the coupling term in the GL linear theory inherits a temperature-rate factor), while Eq. (39) is the simplification.

### 4.4 The page that settles it — and the rule for using it

Two readings, each a few minutes with the copies the author already holds:

1. **Green & Lindsay (1972), printed p. 5, Eqs. (4.8)–(4.10)**, and **printed p. 6, Eq. (4.14)**. The coefficient restrictions sit there. Read which of **h** and **α** is bounded by the other.
2. **Ignaczak & Ostoja-Starzewski (2010), printed p. 21**, the text immediately following Eqs. (1.3.30)–(1.3.33). The same restriction should be stated in the book's notation as a bound between **t0** and **t1**.

Then apply §4.1. Whichever way it comes out, the edit is mechanical:

* if the source reads `h ≥ α` (or `t1 ≥ t0`): the review must print **τ1 ≥ τ0 ≥ 0** and Table 15 must be corrected;
* if the source reads `α ≥ h` (or `t0 ≥ t1`): the review must print **τ0 ≥ τ1 ≥ 0** and Table 22 must be corrected.

**Until one of those pages is read, the recommendation is: print neither.** Replace the inequality in §4.2.3 and in Table 15 with a pointer rather than a condition — for example "the two coefficients are restricted by the entropy inequality (Green & Lindsay 1972, p. 5, Eqs. (4.8)–(4.10); Ignaczak & Ostoja-Starzewski 2010, p. 21, Eqs. (1.3.30)–(1.3.33))" — and mark Table 22's basis column as pending. A pointer is defensible in print; an unverified inequality is not, and the manuscript's own evidence protocol (Section 2.4, item 4) requires a page for a printed verification claim.

---

## 5. Two further notes for the manuscript

1. **The section number in the task does not match the compiled paper.** The task calls this "Section 4.2.2". In the compiled 157-page paper, **§4.2.2 is Lord–Shulman** (Eq. (37), p. 26) and **Green–Lindsay is §4.2.3** (Eq. (39), p. 26). Any cross-reference written as "Section 4.2.2" in the revision would point at the wrong theory.
2. **The naming point is already handled correctly and should be kept.** The review says the two coefficients "are the notation of the later literature" for GL's original coefficients (p. 13). The recorded source finding confirms it: the word "relaxation" does not occur in pp. 1–7. Do not "correct" this into a claim that GL named relaxation times.

---

*Provenance of every row in this file is repeated in `evidence.csv`, with the file and row of each recorded read and the exact Crossref query for each external check, so that a reader can verify or refute each one without trusting this summary.*
