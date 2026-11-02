# Where the evidence work stands after Step 7 - short summary

Written 2026-11-01, after the author supplied the reference set. Every number below is read off the
deliverable CSVs in this folder and in `../P3_evidence_claims_C`, not from memory.

## 1. What changed in one line

Nineteen of the twenty sources that were still owed have arrived, been identified from their own first
pages and read; **the list of sources still missing is down from 20 to 1** (Tzou 1997, the book).

## 2. The claim-check-B series (667 rows)

| level | before Step 7 | now |
|---|---|---|
| R3 - a page or equation was read | 113 | **120** |
| R2 - seen indirectly | 17 | 17 |
| R1 - only a title page or catalogue record | 325 | 325 |
| R0 - nothing of the source seen | 212 | 205 |

By verdict: **SUPPORTED 425** (was 420), **PARTLY SUPPORTED 29** (was 28), **NOT SUPPORTED 1** (was 0),
**SOURCE NOT AVAILABLE 212** (was 219).

The seven B rows carried by the new files: CB-0082, CB-0084, CB-0089, CB-0242, CB-0253, CB-0282 went to
SUPPORTED at R3, and CB-0112 went to NOT SUPPORTED.

## 3. The claim-check-C series (63 rows in seven batches)

**SUPPORTED 35, PARTLY SUPPORTED 23, NOT SUPPORTED 3, SOURCE NOT AVAILABLE 2.**

The two that remain unavailable are CR044 (Sherief, El-Sayed and Abd El-Latief 2010 - not in the set)
and CR210 (Singh, Sarkar and Pal 2020 - genuinely absent from every search).

Batch 007 is the Step-7 batch: 32 rows, CC-0032 to CC-0063, one per register row that the nineteen new
sources could speak to.

## 4. The register (224 rows)

**SUPPORTED 74, PARTLY SUPPORTED 34, NOT SUPPORTED 5, SOURCE NOT AVAILABLE 111.** 26 rows now carry a
`resolved - see P3_evidence_claims_C/CC-xxxx` status.

The register is the authority: each of the 32 rows touched this pass was written with the page locator,
the quoted wording (25 words or fewer) and what the source actually says, exactly as the B rows were.

## 5. The correction to Steps 3-5

Step 5 closed CR019 as unavailable on the strength of a name match: the library's `quintanilla2008.pdf`
is the Quintanilla-Racke stability note, not the end-effects paper. **That closing is withdrawn.** The
supplied set contains the real paper - Quintanilla (2008), "End effects in three-phase-lag heat
conduction", Applicable Analysis 87:8, 943-955 - and its abstract (pp. 943-944) does exactly what the
manuscript says. CR019 is SUPPORTED at R3, CC-0036, and the withdrawal is written into
`step5_source_not_available_final.md` so the file cannot be read as if the old conclusion still stood.

## 6. Four things the author has to decide, not the verifier

1. **CR200 / CB-0112** - Mindlin and Tiersten (1962) is couple-stress elasticity; the word
   "piezoelectric" does not occur in its 34 pages. The piezoelectric bar should rest on Yang (2018)
   alone.
2. **CR134** - Chirita, D'Apice and Zampoli (2016) construct no energy functional ("functional" and
   "entropy" do not occur in the paper). Keep Quintanilla 2003 if it carries the sentence, drop the
   Chirita paper from it.
3. **CR129 / CR130** - the "no admissible entropy functional unless parameter restrictions hold"
   wording is not in either Chirita paper; what they give is restrictions on the delay times (and, in
   the 2017 paper, on the conductivities). Reword, or cite whoever states the functional result.
4. **Chirita2017 as cited** - the bibliography says three authors, Int. J. Heat Mass Transfer; the file
   is a single-author Journal of Thermal Stresses paper. One of the two is wrong.

Lower-stakes wording notes, all recorded in the batch-007 rows: Rukolaine (2014) is a critique of the
DPL model, not a stability result (CR007); Zener's paper is about a reed, not a plane wave (CR140), and
its `h^2/(pi^2 alpha)` display could not be read from the extracted text (CR141); Moore and Gibson do
not use the name "Moore-Gibson-Thompson" (CR024); the Povstenko papers do not treat fractional DPL or
TPL (CR063-CR065).

## 7. State of the deliverables

* `pdfs_needed_from_author.csv` - **1 row** (Tzou1997), and the checker enforces that reduction.
* `library_available_sources.csv` - 34 rows; the nineteen new works are listed there with their claims.
* `step7_reference_set_pass.md` - the file-by-file account of what arrived and what it settled.
* Checkers: `check_claim_check_B.py` PASS (667 rows), `check_claim_check_C.py` PASS (63 rows),
  `check_pdfs_needed.py` PASS (needed=1), `check_library_inventory_v3.py` PASS (unchanged).

No `.tex` file was touched, no PDF or zip was committed, and no Drive identifier appears in any file.
