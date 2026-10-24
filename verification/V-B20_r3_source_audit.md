# V-B20 — independent verification of Arena's R3 source audit

**Verifier:** Brave (independent), batch **B20**, 2026-10-24. Reported on branch `arena/04fdf32e-le`.
**Subject of the audit:** Arena's R3 source audit commit **`0a1eb01`** (`0a1eb018406fa3d41ee406912a9e1db4468b00a7`, "Record R3 source audit findings") on `origin/arena/b5e608f8-le`, with its report `phase5/reports/scientific-audit.md` §"R3 literature-source supplement (Arena audit; 2026-10-24)".
**Status of R3:** **NOT PASSED by this verifier and not marked passed.** Nothing here closes a gap, promotes a source, or edits the manuscript.

## 1. Task

Independently check six items of Arena's R3 audit without using Arena's notes as proof: (1) the Guyer–Krumhansl `.766` / `.778` split and the Eq. (59) reading; (2) the Povstenko 2011 `.511931` / `.511929` split and whether the supplied paper supports the manuscript's Γ-normalised equation; (3) whether the supplied Povstenko book and the local `Povstenko2016` entry are the same edition; (4) the actual evidence behind GAP-09, GAP-12, GAP-13, GAP-22 and GAP-23 against the current authoritative gap definitions; (5) Chester 1963's quoted equations, pages, assumptions and limitations; (6) the discrepancy between the audit / evidence matrix and the retrieved `R3_STATUS`. Preserve every disagreement for the supervisor. Do not touch the manuscript, the plan, `control/`, or the R3 branch.

## 2. Method

1. Read, at `origin/arena/b5e608f8-le`: `phase5/reports/scientific-audit.md` (both at `0a1eb01` and at the later `3b98180`; the R3 supplement is byte-identical), `phase5/reports/R3_STATUS.md`, `phase5/reports/literature-evidence-matrix.csv`, `phase5/reports/R3F_CITATION_MAP.csv`, `phase5/reports/CROSSREF_R3F_VERIFY.csv`, `phase5/reports/R3F_SECTION_COUNTS.csv`, `phase5/master/references_local.bib`, and the section files `phase5/master/sections/sec04,05,11,12*.tex`. The branch was **never fetched into the workspace**; every read used `git show origin/arena/b5e608f8-le:<path>`.
2. Read the authoritative verification records on my own branch at HEAD `9f121b7`: `verification/LITERATURE_BASE.csv`, `REFERENCE_PLAN.csv`, `REFERENCE_GAPS.csv`, `REFERENCE_READINESS.csv`.
3. **Live Crossref** (2026-10-24), not Arena's saved JSON, for the six bibliographic identities and the two ISBN questions — 13 checks, logged in `verification/api_log/B20_r3_crossref_checks.csv`. Two calls were deliberately completeness queries (an ISBN filter and a whole-volume author+year filter) rather than lookups of a DOI I already expected to exist.
4. **Live Open Library** for both Povstenko ISBNs, to get an independent catalogue opinion on the edition question rather than relying on Crossref alone.
5. APS abstract pages for the `.766`, `.778` and Chester records, to check content level without the paywalled PDFs.
6. Recomputed the R3f counts from the saved `CROSSREF_R3F_VERIFY.csv` (not from `R3_STATUS` prose).
7. Checked build evidence independently: `gh run list` for the branch, and the published PDF at `phase5/build_outputs/phase5-v1.1-master.pdf` was extracted and parsed locally (pypdf) for page count and for render artefacts.
8. Before writing any adverse verdict, grepped my own `verification/V-*.md` for each named paper, as required by the standing rule.

## 3. Result — item by item

### 3.1 Guyer–Krumhansl 1966: `.766` vs `.778`, and Eq. (59) — **VERIFIED (split) / MISMATCH (bib) / UNVERIFIED (Eq. 59)**

| | `.766` | `.778` |
|---|---|---|
| Crossref title | Solution of the Linearized Phonon Boltzmann Equation | Thermal Conductivity, Second Sound, and Phonon Hydrodynamic Phenomena in Nonmetallic Crystals |
| Authors | Guyer, R. A.; Krumhansl, J. A. | same |
| Journal, vol/issue, pages, year | Physical Review **148**(2):766–778, 1966-08-12 | Physical Review **148**(2):778–788, 1966-08-12 |
| APS abstract highlights (read 2026-10-24) | "…a set of macroscopic equations which describe second sound with damping and Poiseuille flow are obtained." | "…macroscopic equations developed from the solution of the linearized phonon Boltzmann equation … solved for a cylindrical sample in the limit λ_N ≪ R; λ_Nλ_R^z ≫ R²." |

**Result: the two are distinct papers, adjacent in the same issue, and Arena's direction of the split is correct** — `.766` is the theory paper that carries the macroscopic equations (Paper I); `.778` is the companion application (Paper II). Independent corroboration of the "z" in `τ_z`/`λ_R^z`: the APS abstract of `.778` itself prints `λ_R^z`, so the Ziman-superscript notation belongs to this pair and not to a later commentator.

**MISMATCH (bibliographic, unresolved in the manuscript).** `phase5/master/references_local.bib:204-216` entry `GuyerKrumhansl1966` carries the `.766` **title** with `doi = 10.1103/PhysRev.148.778` and `pages = {778--788}`. Section 4.5 (`sec04_thermoelastic.tex:194`) cites that key for `λ² = c²τ_Nτ_z/5`, a result of the `.766` paper. So the citation, as it stands, resolves to a paper that is not the source of the sentence. **Arena's audit flags the mismatch but the record is still wrong in the tree.**

**UNVERIFIED — Eq. (59), p. 773.** I could not open either paper: APS is paywalled, no copy exists in my workspace, and `R3/RP_2` archives are on the R3 branch, which I must not fetch. **Arena's "Eq. (59) visually checked, p. 773" is Arena's claim and is not evidence for me.** In particular the passage from Eq. (59) to `λ² = c²τ_Nτ_z/5` (the factor 1/5, and whether `τ_z` is Ziman-averaged *in that equation*) remains unchecked by this verifier. The APS abstracts are consistent with, but do not establish, that formula.

**Disagreement with Arena:** none on the split. On Eq. (59): Arena states PRIMARY-SOURCE-CHECKED; I can only reach **UNVERIFIED**, and under the standing rule a supervisor/Arena transcript cannot be promoted to a primary check on my side.

### 3.2 Povstenko 2011: `.511931` vs `.511929` and the Γ-normalised equation — **VERIFIED (split) / MISMATCH (citation key) / UNVERIFIED (exact equation)**

| DOI | Crossref record |
|---|---|
| `10.1080/01495739.2010.511931` | Povstenko, Y. Z., *Fractional Cattaneo-Type Equations and Generalized Thermoelasticity*, J. Thermal Stresses **34**(2):97–114, 2011 |
| `10.1080/01495739.2010.511929` | Povstenko, Y. Z., *Dirichlet Problem for Time-Fractional Radial Heat Conduction in a Sphere and Associated Thermal Stresses*, J. Thermal Stresses **34**(1):51–67, 2011 |

Both exist, are in the same volume, and are one issue apart. **Confirmed independently of Arena.**

**MISMATCH (citation key).** `references_local.bib:505-519` entry `Povstenko2011` is the `.511929` **Dirichlet** paper (title, pages 51–67, `verified = {YES}`), yet Section 11 (`sec11_advanced.tex:55-58`) attaches that key to the fractional Cattaneo flux law, Eq. (11.4) — a result of the `.511931` paper. The bibliography therefore points at a paper that cannot contain Eq. (11.4), while the bib simultaneously marks the record `verified = YES` from Crossref. The audit reaches the same conclusion; the defect is live in the tree.

**UNVERIFIED — does `.511931` print the Γ-normalised coefficient?** I have no copy. Arena says Eq. (29) does **not** print the manuscript's `Γ(1+α)` denominator. I can neither confirm nor refute that from the text; I record it as **UNVERIFIED**, and note that the manuscript already labels the attribution CONDITIONAL, which is the correct defensive posture. What is *not* in doubt is that the present key supports nothing: it points to a different paper.

**Disagreement with Arena:** none on identity or on the key mismatch. On "Eq. (29) lacks the Γ denominator" — Arena asserts, I record UNVERIFIED.

### 3.3 Povstenko 2015 vs `Povstenko2016` — **MISMATCH (edition), and the bib's `NO_DOI` is wrong**

- Live Crossref `filter=isbn:9783319296370` → **0 records**. Open Library `/isbn/9783319296370.json` → **404**.
- Live Crossref `10.1007/978-3-319-15335-3` → Povstenko, *Fractional Thermoelasticity*, Springer, series *Solid Mechanics and Its Applications*, **2015**, ISBN **9783319153346** (print) / **9783319153353** (eBook).
- Open Library `/isbn/9783319153346.json` → OL28306333M, Springer, **24 March 2015**, 265 pp, "Solid Mechanics and Its Applications (219)".

**Result:** the supplied copy (2015, DOI `10.1007/978-3-319-15335-3`) and the local entry (`Povstenko2016`, year 2016, `isbn = 9783319296370`, `verified = {NO_DOI}`) are **not demonstrated to be the same edition**, and on the ISBN they disagree. Two further defects, both independent of Arena: (a) the book demonstrably **has** a Crossref DOI, so `NO_DOI` is factually wrong for the work that was supplied; (b) the cited ISBN resolves nowhere in two independent catalogues.

**Disagreement with Arena:** Arena says "edition equivalence remains unresolved … the supplied copy's ISBN was not transcribed". I go one step further and record the ISBN that *is* recorded in the bib as unresolvable at Crossref and Open Library — so the entry cannot be repaired by inference; the printed copyright page is required. I make no substitution.

### 3.4 Gaps GAP-09 / GAP-12 / GAP-13 / GAP-22 / GAP-23 against the authoritative definitions

Authoritative rows: `verification/REFERENCE_GAPS.csv` (25 rows, HEAD `9f121b7`); readiness from `verification/REFERENCE_READINESS.csv`.

| gap | authoritative definition on my branch | audit's claim | my independent finding |
|---|---|---|---|
| **GAP-09** (s.4.11) | "Fractional-calculus primaries: Povstenko 2016 book, Gorenflo 1997, Luchko 2010"; status PARTLY CLOSED | "still open; two Povstenko files accessible; required fractional-calculus support still outstanding" | **Agree OPEN.** But the audit's wording is **stale**: Gorenflo–Mainardi 1997 (LIT-0528), Gorenflo et al. 2014 (LIT-0529) and Luchko 2010 (LIT-0535) are already in my base at *FULL-TEXT via supervisor transcription*, and Povstenko 2009 (LIT-0032) likewise; the book is PREFACE ONLY (LIT-0530). The one genuinely missing piece is the `.511931` paper, LIT-0536, still `metadata only`. **Disagreement: description, not verdict.** |
| **GAP-12** (s.9) | Achenbach 1973, *Wave Propagation in Elastic Solids*; HIGH, blocking | "not found; Auld 1973 is a different book" | **Agree OPEN.** Consistent with my 2026-10-23 Drive inventory: no Achenbach row. The audit's identification of `2015.148378.Accoustic-Fields-And-Waves-In-Solids-Vol-1_text.pdf` as **Auld 1973** is a useful negative result and does not close the gap. |
| **GAP-13** (s.10) | Nowacki 1975, *Dynamic problems of thermoelasticity*; MEDIUM, not blocking | "not found in the inspected archives" | **Agree OPEN, unchanged.** My record already warns that `10.1115/1.3424081` is a one-page 1977 pointer, not the book. |
| **GAP-22** (s.12) | s.12 plan defect; **3 of 6** read comparisons (LIT-0040, LIT-0307, LIT-0428); HIGH, blocking | "authoritative definition is the s.12 comparative-plan defect, 3/6; the B19 grouping of Chester/Guyer/Chandrasekharaiah conflicts with the plan" | **Split verdict — see 3.4.1.** |
| **GAP-23** (s.13) | six second-sound rows including Chester 1963; "Zero of six available" (2026-10-23); HIGH, blocking | "Chester is now source-checked in the supplied collection, but the remaining items and the six-source requirement are not" | **Agree OPEN.** The availability half of my GAP-23 status is now **superseded** (Chester is in the supervisor's `R3.zip`), and I accept that correction; the gap itself stays open. I did not verify Chester's equations myself (3.5). |

#### 3.4.1 GAP-22 and the s.12 count — the substantive disagreement

Authoritative plan rows with `plan_section = s.12` (my `REFERENCE_PLAN.csv`): **LIT-0026** (Askes 2011, comparative), **LIT-0040** (Shakeriaski 2021, comparative survey, SECONDARY), **LIT-0307** (Wang–Li 2025 IV, comparative), **LIT-0428** (van der Merwe 2021, comparative). Chester is **LIT-0010 → s.13**; Chandrasekharaiah 1998 is **LIT-0039 → s.4.1**; Guyer 1966 is **LIT-0009 → s.4.5**.

**Where Arena is right and I was wrong (B19):** my `PDF_REQUEST_LIST_5.md` Part E and `V-B19` §3 named Chester 1963, Guyer–Krumhansl 1966 and Chandrasekharaiah 1998 as "the three read comparisons GAP-22 needs". That inference came from the **supervisor's section tags in `control/EXTENDED_LIST.csv`** ("3, 12", "12", "1, 12"), **not** from the authoritative plan. Checked against the plan, all three sit elsewhere. **I withdraw that recommendation**; those three are candidate *additional* s.12 material only if the supervisor re-labels the plan rows, and they may not be counted toward the s.12 threshold as things stand.

**Where I disagree with Arena:** `R3_STATUS.md` §R3f/§R3g reports s.12 at **5 then 6** verified sources with **5 primary**. That number is reached by (i) treating supervisor transcripts F46–F49 as primary reads, and (ii) counting three single-model papers as s.12 comparisons. Independent check:

- `LITERATURE_BASE.csv` records LIT-0307 (F46), LIT-0428 (F47), LIT-0532 (F48), LIT-0533 and LIT-0534 (F49) as **"FULL-TEXT via supervisor transcription — not opened by this verifier"**. Under the standing rule those are **SECONDARY-SOURCE**, i.e. metadata-verified but not primary-read.
- Content, not metadata, decides comparative status: van der Merwe 2021 and Wang–Li 2025 (IV) are explicitly comparative (their titles say so); **Chiriţă–D'Apice–Zampoli 2016** is one model's thermodynamic compatibility, **Chen–Gurtin 1968** is a two-temperature constitutive theory, **Gurtin–Williams 1966** is a Clausius–Duhem paper. None of the three compares models side by side.

**Therefore s.12 is at 3 of 6** — the authoritative figure — not 6. Arena's "6 verified / 5 primary" and its "s.12=6, 10 eligible" cumulative line are not supported by the base. **This is a MISMATCH of counts, preserved for adjudication.** Consistent with the standing rule I am *not* issuing a WRONG verdict on any scientific claim; the disagreement is about counting and labelling.

### 3.5 Chester 1963 — **VERIFIED (bibliographic) / UNVERIFIED (equations, pages, assumptions)**

- Live Crossref: Chester, Marvin, *Second Sound in Solids*, Physical Review **131**(5):2013–2015, 1963-09-01. APS record adds **Received 29 April 1963**, published 1 September 1963, and an abstract stating that "a macroscopic point of view is used which relies upon a modification in the Fourier heat equation".
- **The manuscript quotes no Chester equation at all.** A grep of every file in `phase5/master/sections/` returns **zero** occurrences of "Chester", and `references_local.bib` has **no** Chester entry. So any "quoted equations / page references" that need checking exist only in Arena's audit text and in `literature-evidence-matrix.csv`, not in the manuscript.
- **UNVERIFIED:** Eqs. (5)–(8) and (11)–(12), the page anchors 2014–2015, the phonon-gas/dispersionless assumptions, and the "partly hypothetical" characterisation. No copy is reachable from my environment and I did not open the ZIPs.
- The audit's observation that the supplied PDF is a **mixed scan** (an unrelated X-ray article fragment above Chester's text) cannot be checked by me. If it is correct, it is a real caution worth keeping, because it widens the chance of mis-attributed quotations.
- **GAP-23 relevance:** even if every line of Arena's Chester reading is correct, one source out of six leaves GAP-23 open, and Chester is a *macroscopic-phenomenological* paper — it cannot on its own support an experimental-validation claim.

### 3.6 Discrepancies between the audit / evidence matrix and `R3_STATUS`

| # | Artefact A | Artefact B | Discrepancy |
|---|---|---|---|
| D1 | `R3_STATUS.md` §R3g: s.12 = 6 verified, 5 primary | `REFERENCE_READINESS.csv` s.12 = 3; base rows LIT-0307/0428/0532/0533/0534 all "supervisor transcription … not opened by this verifier" | **Numeric conflict, 6 vs 3.** See 3.4.1. Unreconciled in any file. |
| D2 | `literature-evidence-matrix.csv` **FW-013** (Guyer & Krumhansl `.778`): `primary_source_checked = YES`, `claim_supported = SUPPORTED` | `scientific-audit.md` supplement: only the `.766` paper was supplied; "do not transfer findings between them" | **The matrix asserts a primary check of a document no one holds.** FW-013's note also credits F10–F12, which are supervisor transcripts. |
| D3 | `R3_STATUS.md` §R3f narrative on Gurtin–Williams (`…non-linear elasticity with two temperatures`) | `references_local.bib:1977-1989`: title `On the Clausius-Duhem inequality`; live Crossref at ZAMP 17:626–633 confirms that title | **The R3_STATUS prose names a paper that does not exist at that DOI.** The bib was already corrected; the status text was not. Small, but it is exactly the kind of line a referee would quote. |
| D4 | `sec12_comparative.tex:22` attributes to `GurtinWilliams1966` the claim that "for a broad class that includes most materials with memory, the dual-temperature construction is inadmissible and reduces to Clausius–Duhem" | Live Crossref: the only 1966 Gurtin paper in ZAMP vol. 17 is *On the Clausius–Duhem inequality*; the only "two temperatures + non-simple" paper by these authors is **Chen–Gurtin–Williams 1969**, ZAMP 20:107–112, `10.1007/BF01591120` | **Possible attribution conflation — OPEN, not asserted as wrong.** The content of neither paper was read, so the sentence may well be supported by the 1966 paper; but the phrase "reduces to Clausius–Duhem" suggests the 1969 paper. Flagged for adjudication, no substitution made. |
| D5 | `sec12_comparative.tex:20`: "Chen and Gurtin's two-temperature theory **for non-simple materials**" | Live Crossref title of `10.1007/BF01594969`: *On a theory of heat conduction involving two temperatures* (no "non-simple") | **Descriptor mismatch — OPEN.** The relation θ = φ − a∇²φ is documented (my B18 facts from F49) and matches this paper; the "non-simple materials" wording belongs to the 1969 paper. |
| D6 | Audit: "the current evidence matrix has 97 data rows" | `literature-evidence-matrix.csv` = 98 lines including header = **97 data rows** | **No discrepancy** — arithmetic confirms the audit. Recorded because it was checked. |
| D7 | Supervisor's live report to me: run `39987191853` on `0f27630` **failed** the overfull gate; "R3f is not complete" | `R3_STATUS.md` now records the R3f **corrective** at `2d5dc6b`, run `39988876745`, passing, and two R3g passes; `gh run list` confirms both | **Version lag, not error.** The supervisor's report was accurate when written; the branch has since moved past it. The failing commit is superseded, so R3f *as delivered to me* reads as closed by `2d5dc6b`. |
| D8 | `R3_STATUS.md` "162 pages / 0 undefined" | My extraction of the **published PDF** at `phase5/build_outputs/phase5-v1.1-master.pdf`: **162 pages**, zero `??` render artefacts | **Agree** — independently confirmed on the artefact itself. |
| D9 | R3g inventory: process language recorded, "did not drive manuscript edits" | My extraction of the same PDF: **39** `PRIMARY-SOURCE-CHECKED`, **8** `SECONDARY-SOURCE`, **45** `UNVERIFIED`, **23** `GAP-`, **3** `eligible read` occurrences **in the rendered manuscript**, across 14 section files | **Agree there is process language; disagree that it is a non-issue.** It is visible to a referee in the submitted artefact. Editorial blocker, not a science error. |

### 3.7 Build / run evidence (independently obtained)

| run | commit | result | note |
|---|---|---|---|
| `39987191853` | `0f27630` | **failure** | the overfull-gate failure the supervisor reported; superseded |
| `39988876745` | `2d5dc6b` | success | R3f corrective |
| `40063975977` | `d81e99d` | success | after TeX-install fix |
| `40064319885` | `9d975ac` | success | report-only metrics |
| **`40072102450`** | **`0a1eb01`** | **success** | the audit commit's own strict run |

Published artefact parsed locally: `phase5/build_outputs/phase5-v1.1-master.pdf`, **162 pages**, title "Multiphysics Wave Mechanics in Generalized Continua: A Constructive Review of Theory, Energy Transport, and Interface Phenomena", 0 `??` occurrences. **I could not download the run logs** (`gh run view --log` returns an EOF from the results host in this environment), so the workflow's own `0 undefined references/citations` and the >1 pt overfull gate are **corroborated but not re-executed** by me. No local TeX build was possible: `latexmk`, `pdfinfo` are absent from my sandbox.

## 4. Evidence / sources

| source | used for | access level |
|---|---|---|
| `origin/arena/b5e608f8-le` @ `0a1eb01` / `3b98180`: `scientific-audit.md`, `R3_STATUS.md`, `literature-evidence-matrix.csv`, `R3F_CITATION_MAP.csv`, `CROSSREF_R3F_VERIFY.csv`, `R3F_SECTION_COUNTS.csv`, `references_local.bib`, `sections/*.tex`, `build_outputs/phase5-v1.1-master.pdf` | the audit's claims and the tree's actual state | files read via `git show`; branch **not** fetched into the workspace; **no PDF opened** |
| Crossref REST, live, 2026-10-24: 6 DOI lookups, 1 ISBN filter, 1 journal+author+year filter, 2 bibliographic searches | items 1, 2, 3, 5 and D3–D5 | metadata only |
| Open Library, live, 2026-10-24: ISBN 9783319296370 (404), ISBN 9783319153346 (OL28306333M) | item 3 | catalogue metadata only |
| APS abstract pages `link.aps.org/doi/10.1103/PhysRev.148.766`, `journals.aps.org/pr/abstract/10.1103/PhysRev.148.778`, `link.aps.org/doi/10.1103/PhysRev.131.2013` | items 1 and 5, content level | **abstract only — not full text** |
| `verification/{LITERATURE_BASE,REFERENCE_PLAN,REFERENCE_GAPS,REFERENCE_READINESS}.csv` @ `9f121b7` | item 4 and the s.12 count | local files |
| `gh run list`, published PDF parsed with pypdf | §3.7 | CI metadata + artefact |

## 5. Checks done

1. **Live, not cached.** Every bibliographic statement in §3 came from a request I issued in this batch; where I also used Arena's saved JSON I say so. `verification/api_log/B20_r3_crossref_checks.csv` holds all 13 checks.
2. **Completeness, not just existence.** For Gurtin–Williams I did not stop at "the DOI resolves": I queried the whole of ZAMP vol. 17, author=Gurtin, 1966 and got **exactly one** record. That closes the possibility of a second 1966 paper and is what turns D3/D5 from suspicion into a reportable discrepancy.
3. **Two independent catalogues for the edition question.** Crossref **and** Open Library both fail on ISBN 9783319296370 and both confirm 9783319153346 (2015, SMIA 219). One catalogue could be wrong; two agreeing is stronger.
4. **Counts recomputed, not quoted.** R3f 21 VERIFIED / 3 MISMATCH / 0 NOT-FOUND / 1 NO-DOI over 24 HTTP 200 requests and 1 NOT-REQUESTED, recomputed from `CROSSREF_R3F_VERIFY.csv`; it matches `R3_STATUS`.
5. **PDF parsed directly.** 162 pages and 0 `??` obtained from the artefact, not from the report; process-language counts likewise.
6. **Own-file grep before an adverse verdict.** Grepped `verification/V-*.md` and `FULLTEXT_FACTS.csv` for Guyer, Chester, Povstenko, Chen, Gurtin: confirmed that F43/F44/F46–F49/C3/C4 are supervisor transcripts, which is the basis for the SECONDARY-SOURCE reading in §3.4.1. Sub-system named: **R3 readiness counting and source labelling**, not the physics.
7. **Self-audit.** The B19 GAP-22 recommendation was re-checked against `REFERENCE_PLAN.csv` and withdrawn in §3.4.1.
8. **No branch pollution.** `git show origin/arena/b5e608f8-le:<path>` throughout; `arena/b5e608f8-le` was never checked out or merged. `git status` after writing shows only `verification/` additions.

## 6. Confidence

- **Guyer–Krumhansl split, Povstenko 2011 split, Chester bibliographic identity: HIGH.** Two independent sources each (Crossref + APS/Open Library), full field agreement.
- **Povstenko edition mismatch: HIGH on the defect, MEDIUM on the explanation.** The bib's ISBN resolves nowhere in two catalogues and the DOI-bearing book is dated 2015 — but whether 9783319296370 is a paperback reprint, a second printing, or a transcription error cannot be settled without the printed copyright page.
- **s.12 = 3 not 6: MEDIUM-HIGH.** The counting rules and the base's own `read_level` strings are unambiguous; the residual judgement is whether two-temperature constitutive papers "genuinely support" a comparative section, and I have argued they do not rather than proven it.
- **Chester equations, Guyer Eq. (59), Povstenko Eq. (29) content: no confidence — UNVERIFIED.** I did not see these texts. Any statement about them from me would be a guess.
- **D4/D5 attribution conflations: LOW-MEDIUM.** Titles and volume/page evidence are solid; the content of both candidate papers is unread, so this is a flag for adjudication, not a finding of error.

## 7. NOT verified / open issues

1. **No R3 paper was read by me.** Guyer–Krumhansl (either paper), Povstenko 2011/2015, Chester 1963, Chiriţă 2016, Chen–Gurtin 1968, Gurtin–Williams 1966, van der Merwe 2021 and Wang–Li 2025 are all unread here. Metadata and abstracts only.
2. **Eq. (59) p. 773, Chester's Eqs. (5)–(8)/(11)–(12) and pp. 2014–2015, Povstenko's Eq. (29) p. 101: UNVERIFIED.** No copy reachable; the ZIPs are on the R3 branch, which I may not fetch.
3. **The "mixed scan" and "40-page low-text Maxwell" document-integrity claims are Arena's**; I did not inspect those files.
4. **Run logs not downloadable**, so the >1 pt overfull gate and "0 undefined references" are corroborated by the artefact (162 pp, no `??`) but not re-run. No local TeX.
5. **GAP-09/12/13/23 remain open; GAP-22 remains open at 3/6.** No gap was closed or re-statused by this batch, and no ledger was edited.
6. **The `Povstenko2011` key, the `GuyerKrumhansl1966` entry and the `Povstenko2016` ISBN are still wrong in the manuscript tree.** I did not fix them — that is Arena's/supervisor's call, and fixing the bib is outside my scope.
7. **D4/D5 need the printed pages** of Gurtin–Williams 1966 and Chen–Gurtin–Williams 1969 before either the 1966 attribution is kept or the 1969 paper is substituted.
8. **R3 is not passed.** The build passes; the source-verification round does not, on the counting and labelling issues above.
