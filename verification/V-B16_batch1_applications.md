# V-B16 batch 1 — reading pass for the thin sections (10 papers + availability audit)

**Batch:** B16-1. **Date:** 2026-10-23. **Input:** `arena/b5e608f8-le` @ `3092fa3` (`phase5/reports/R3_STATUS.md`, read-only); `claude/control` @ `22b5339` (checked, no new findings file).
**Manuscript:** not touched — this verifier does not edit it, and the repo holds no `.tex`.
**Batches of ten; this is batch 1 of the programme.**

---

## Task

R3 leaves these sections short of evidence-ready sources: 5 (3), 8 (1), 11 (2), 12 (0), 13 (1), 10, and 4.1 / 4.2 / 4.9 / 4.11 (0). Read the `must_read_first=YES` rows for those sections in priority order, from the Drive inventory or open access, until each section has at least six sources at FULL or PARTIAL read **where documents genuinely exist**; where they do not, write "source not available" in `REFERENCE_GAPS.csv` and invent nothing. Then update `FULLTEXT_FACTS`, `LITERATURE_BASE.read_level`, and `REFERENCE_PLAN.technical_claim_eligible` for rows where an equation or statement was actually seen.

## Method

1. **Availability audit first, before reading anything.** Every `must_read_first=YES` row in the ten target sections was matched against the whole library: title-token overlap against the `title` and `file_name` of all 370 `DRIVE_INVENTORY.csv` rows, plus the parsed titles in `DRIVE_TIER3_METADATA.csv` (274 rows). A row counts as *available* only if the overlap is with the same paper (author and year agreeing), not merely the same words.
2. **Read only what exists**, from the Drive PDF, in one pass per paper; identity taken from the title page (not from the filename and not from the metadata row).
3. **Level discipline:** a paper read only to the end of its introduction is `PARTIAL - abstract and introduction`, never `FULL`. `technical_claim_eligible` was set only where a statement was actually read.
4. No PDF, no extracted text and no long quotation enters the repo.

## Result

### A. What the audit found (the uncomfortable part)

**None of the must-read rows for sections 4.1, 5, 8, 10, 11, 13 is in the library** — with exactly one exception, Chandrasekharaiah's 1998 *Applied Mechanics Reviews* review (Drive `DRV-0063`). The highest-scoring "matches" are different papers that share generic phrases: "plane waves in generalized thermoelasticity" matched a 2022 paper on rotating double-porous media; "thermoelastic materials with voids" matched a 2023 orthotropic piezo paper. Those are not matches and were not treated as such.

The library is not a theory collection. It is 370 files of which ~300 are recent applied papers, two-thirds of them metadata-only in earlier passes. That is why section 13 can be fed and sections 5, 8 and 10 cannot.

**Consequence:** this batch could not deliver six sources for nine of the ten target sections. It delivered six-plus for **section 13**, one for **section 4.1/4.2**, one for **section 11**, and recorded exactly why the rest cannot be delivered.

### B. Papers read in this batch (12 reads, 11 new base rows, 1 new facts row for an existing base row)

| Drive | identity as read from the title page | journal | read to | serves |
|---|---|---|---|---|
| DRV-0063 | D. S. Chandrasekharaiah, *Hyperbolic thermoelasticity: a review of recent literature* | Appl. Mech. Rev. **51**(12) part 1, 705– (1998) | **Section 2**, printed eqs (2.1)–(2.6) | 4.1, 4.2 |
| DRV-0254 | F. Shakeriaski, F. Salehi, M. Ghodrat, *Modified G-L thermoelasticity theory for nonlinear longitudinal wave in a porous thermoelastic medium* | Phys. Scr. **96**, 125206 (2021), `10.1088/1402-4896/ac1aff` | abstract + intro | 5 |
| DRV-0229 | J.-L. Wang, H.-F. Li, *Memory-dependent derivative versus fractional derivative (II): Remodelling diffusion process* | Appl. Math. Comput. **391**, 125627 (2021), `10.1016/j.amc.2020.125627` | definitions (1)–(3) | 11 |
| DRV-0305 | Y. Sun, M. Saka, *Thermoelastic damping in micro-scale circular plate resonators* | JSV (2010), `10.1016/j.jsv.2009.09.014` | abstract + intro | 13 |
| DRV-0306 | Y. Sun, H. Tohmyoh, *Thermoelastic damping of the axisymmetric vibration of circular plate resonators* | JSV **319**, 392–405 (2009) | abstract + intro | 13 |
| DRV-0307 | J. N. Sharma, R. Sharma, *Damping in micro-scale generalized thermoelastic circular plate resonators* | Ultrasonics (2011), `10.1016/j.ultras.2010.10.009` | abstract + intro | 13 |
| DRV-0343 | R. Kumar, S. Devi, V. Sharma, *Damping in microscale modified couple stress thermoelastic circular Kirchhoff plate resonators* | Appl. Appl. Math. **12**(2) Art. 19, 924– (2017) | abstract | 13 |
| DRV-0302 | T. Wang et al., *A phase-field model of thermo-elastic coupled brittle fracture with explicit time integration* | Comput. Mech. (2020), `10.1007/s00466-020-01820-6` | abstract + intro | 13 |
| DRV-0368 | T. Wang et al., *Phase field modeling of crack propagation in three-dimensional quasi-brittle materials under thermal shock* | EFM **302**, 110070 (2024) | abstract | 13 |
| DRV-0369 | T. Wang et al., *Simulation of crack patterns in quasi-brittle materials under thermal shock using phase field and cohesive zone models* | EFM **276**, 108889 (2022) | abstract | 13 |
| DRV-0370 | H.-Y. Kuo, S.-H. Yu, *Effect of the imperfect interface on the scattering of SH wave in a piezoelectric cylinder in a piezomagnetic matrix* | Int. J. Eng. Sci. (2015), `10.1016/j.ijengsci.2014.08.006` | abstract + intro | 13 |
| DRV-0365 | A. Almuneef, I. Abbas, A. A. El-Bary, *Finite element analysis in an unbounded fiber-reinforced medium containing spherical cavities caused by pulse heat flux* | Results Eng. (2025) 105059 | abstract + intro | 13 |

### C. Section coverage after batch 1

| section | eligible before (R3) | added at read level | eligible now | status |
|---|---:|---|---:|---|
| **13** | 1 | **9** (abstract/intro level, grade B) | **10** | **meets the six-source bar at abstract level** — equation-level still open |
| **11** | 2 | 1 (definitions (1)–(3) seen) | 3 | short; see GAP-21 |
| **4.1 / 4.2** | 0 / 0 | 1 (equations (2.1)–(2.6) seen) | 1 / 1 | the one source that prints the CV law; Cattaneo/Vernotte originals still missing |
| 5 | 3 | 0 (+1 citing source) | 3 | **no document available** — GAP-18 |
| 8 | 1 | 0 | 1 | **no document available** — GAP-19 |
| 10 | 0 | 0 | 0 | **no document available** — GAP-20 |
| 12 | 0 | 0 | 0 | no plan rows exist at all — GAP-22 |
| 4.9 / 4.11 | 0 / 0 | 0 | 0 | no plan rows / no document — GAP-24, GAP-25 |

The "eligible now" column counts only what this verifier has seen; nine of the section-13 additions rest on abstract-level statements and are labelled `evidence_grade B` with that limitation in `evidence_quality`. They support "what the paper did", not "what value it got".

### D. The one substantive find for 4.1/4.2

Chandrasekharaiah 1998 prints the **Cattaneo–Vernotte equation as (2.1)**, `q + τ ∂q/∂t = −k∇T`, the transport equation (2.2), the energy balance (2.3), the finite speed (2.4) `v = √(k/ρcτ)`, and the τ = 0 reduction to Fourier (2.5) and to the parabolic equation (2.6). Since neither Cattaneo 1948 nor Vernotte 1958 is obtainable here, this is the only defensible way to support the CV sentence in sec. 4.2 **as a SECONDARY citation**, and the facts row says so in both `status` and `read_level`.
The same review independently states that GN 1992/1993 formulated two hyperbolic theories, the second a limiting case of the first and free of energy dissipation — a third, independent corroboration of the type II/III reading in `V-B15`.

### E. Two bibliographic errors found while reading

1. **`DRIVE_TIER3_METADATA` row `DRV-0229` was wrong.** It recorded Part **(I)** *"Memory-dependent derivative versus fractional derivative (I): Difference in temporal modeling"*, `10.1016/j.cam.2020.112923`. The file is Part **(II)**: *"… (II): Remodelling diffusion process"*, Appl. Math. Comput. **391**, 125627, `10.1016/j.amc.2020.125627`. Title, venue, volume and DOI replaced from the article page and the old values recorded in `notes`. Had this gone unchecked, sec. 11 would have cited a paper nobody read.
2. **A filename is not an identity.** `Shakeriaski_2021_Phys._Scr._96_125206.pdf` was assumed (in my own first pass) to be LIT-0040, *"Recent advances in generalized thermoelasticity theory and its applications"*. It is not: it is *"Modified G-L thermoelasticity theory for nonlinear longitudinal wave in a porous thermoelastic medium"*. **`LIT-0040` therefore remains unread and unavailable.** This is exactly the failure mode the "identity from the title page" rule exists to catch.

### F. Gap records written (9 new, 1 updated)

`GAP-17` (Cattaneo/Vernotte originals, s.4.2, partly mitigated), `GAP-18` (s.5, all six rows), `GAP-19` (s.8, all seven), `GAP-20` (s.10, all twelve), `GAP-21` (s.11 Caputo/Povstenko/Gorenflo–Luchko), `GAP-22` (s.12 has no plan rows), `GAP-23` (s.13's six second-sound rows), `GAP-24` (s.4.9 has no plan rows), `GAP-25` (s.4.11 Caputo 1967); `GAP-09` extended. Every entry states the check that was done, not merely that something is missing.

## Evidence / Sources

All twelve documents were read by the verifier from the Google Drive library on 2026-10-23; access level is recorded per row (`PARTIAL - title page, abstract and introduction`, or `PARTIAL - Section 2` for DRV-0063). Identities from title pages; DOIs recorded only where printed on the page seen, otherwise the field says "file metadata; not seen on the page read" or is left empty. Bibliographic framing for the R3 counts: `phase5/reports/R3_STATUS.md` at `arena/b5e608f8-le` `3092fa3`.

## Checks done

- **Availability checked before reading** — the audit table was produced first, so no time was spent pretending a missing paper was readable.
- **Negative matches rejected:** every ≥0.5 title-overlap was opened and identified; all were different papers. Recorded in `GAP-19`/`GAP-20` wording.
- **Identity from title page, twice** — this caught the Shakeriaski and the Wang–Li Part I/II errors.
- **Level honesty:** 11 of 12 reads are `PARTIAL`; only DRV-0063 reached printed equations. No `FULL` claim anywhere.
- **No fabrication:** no equation, number or page is quoted that was not in the extracted text I read; DOIs absent from the page are left blank rather than filled from memory.
- **Integrity:** LITERATURE_BASE 499 → 510 (11 new, no duplicate ids), FULLTEXT_FACTS 104 → 116 (12 new, no duplicate keys), REFERENCE_PLAN 193 → 204 (11 new rows, 1 updated), REFERENCE_GAPS 16 → 25, DRIVE_PRIORITY 11 read levels updated, DRIVE_TIER3_METADATA 12 read levels + 1 identity correction. Column counts unchanged in every file.

## Confidence

- **HIGH** that the nine target sections' must-read rows are absent from the library: the check was title-token overlap against every inventory row with manual confirmation of every high score.
- **HIGH** for the twelve identities and their printed venue/volume where recorded.
- **HIGH** for Chandrasekharaiah (2.1)–(2.6): the equations were in the text I read.
- **MEDIUM** for what the nine section-13 papers *claim*: abstract-level, unverified against their body text or figures.
- **LOW** for any use of these papers as numerical evidence — no numbers were read.

## NOT verified / open issues

1. **Sections 5, 8, 10, 4.9, 4.11 and the second-sound half of 13 cannot be made evidence-ready from this library.** They need documents, not more reading. GAP-18/19/20/23/24/25 are the shopping list.
2. **Section 12 still has no plan rows.** Its candidates have to be labelled first (GAP-22); comparative papers do exist in the library.
3. **Nine section-13 sources are abstract-level.** If sec. 13 needs numbers (damping values, crack densities, scattering cross-sections), each of those papers needs a second pass to its results section.
4. **`LIT-0040` (Shakeriaski 2021 review) is still unread** — the file that looked like it is a different paper.
5. **No equation-level check of any section-13 paper** was possible in this pass, so nothing here corroborates or contradicts the manuscript.
6. **Open-access harvesting was not attempted** for the missing analysis papers (s.10); the sandbox can reach arXiv and publisher landing pages through the page fetcher, but PDF ingestion needs a document in Drive. That is the next lever if the library cannot be extended.
