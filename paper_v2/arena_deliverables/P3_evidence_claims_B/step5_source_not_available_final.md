# Step 5 - the two sources that are not in the folder: final wording

Checked again in the folder this pass, by filename search and by title search.

## 1. `Sherief2010Fractional` - Sherief, El-Sayed and Abd El-Latief (2010)

* The paper: **Sherief, H. H., El-Sayed, A. M. A. and Abd El-Latief, A. M. (2010), "Fractional order
  theory of thermoelasticity for a half-space", International Journal of Solids and Structures 47,
  585-590**, register DOI `10.1016/j.ijsolstr.2009.09.034`.
* Search result: **no file in the folder carries "Sherief" in its name** - a name search over the whole
  folder returns zero files, and the 100-name folder list has no entry for this paper or for any other
  Sherief paper.
* Affected register row: **CR044**, verdict `SOURCE NOT AVAILABLE`.

Final wording for CR044:

> The paper is not held: a full search of the source folder, by author name and by title, returns no
> copy of Sherief, El-Sayed and Abd El-Latief (2010), and none of the 100 files in the folder is it
> under another name. Its claim therefore cannot be checked at any level, and the manuscript's
> attribution is recorded here as unverified rather than supported. Nothing in this report rests on
> this paper. Note that a different Sherief item (Dhaliwal and Sherief 1980) is cited elsewhere in the
> manuscript and is held and verified; it must not be confused with this one.

## 2. `Quintanilla2008` - Quintanilla, "End effects in three-phase-lag heat conduction"

* The paper: **Quintanilla, R. (2008), "End effects in three-phase-lag heat conduction", Applicable
  Analysis 87**, register DOI `10.1080/00036810802428938`.
* Search result: the folder does contain a file called `quintanilla2008.pdf`, but it is **a different
  paper**. Its first page reads: "A note on stability in three-phase-lag heat conduction, Ramon
  Quintanilla and Reinhard Racke" - two authors, and the subject is Lyapunov functions and exponential
  stability of three-phase-lag heat conduction, not end effects. So the file is a **name match with a
  content mismatch**, not a copy of the cited paper.
* Affected register row: **CR019**, verdict `SOURCE NOT AVAILABLE`. This is the row whose claim
  ("the end effects of three-phase-lag heat conduction were studied by Quintanilla") is cited in
  Section 6, p. 35.

Final wording for CR019:

> The paper is not held. The only Quintanilla file of that year in the folder - `quintanilla2008.pdf` -
> is a different work: its first page identifies it as "A note on stability in three-phase-lag heat
> conduction" by Quintanilla and Racke, a two-author paper on Lyapunov functions, exponential stability
> and instability of the three-phase-lag heat equation, not a paper about end effects. Citing that file
> for an end-effects statement would be a citation error, so the claim stays unverified. A copy of
> "End effects in three-phase-lag heat conduction" (Applicable Analysis 87, DOI
> 10.1080/00036810802428938) is needed before the sentence can be checked.

## Where this leaves the register

**CR044 keeps `verdict = SOURCE NOT AVAILABLE`.** It is the one row this series has had to leave at
that verdict after a search; the other SNA rows were never in scope of a claim-check batch. Its DOI is
the one the register carries and was not verified against a printed page, because no page of the paper
was seen.

**CR019 no longer stands at that verdict - see the correction below.**

---

## CORRECTION (Step 7, 2026-11-01): CR019 is supplied and verified

The two paragraphs about `Quintanilla2008` above are **superseded**. The author supplied a complete
reference set on 2026-11-01, and it contains the correct paper. The copy in it is

> R. Quintanilla (2008), "End effects in three-phase-lag heat conduction", Applicable Analysis: An
> International Journal 87:8, 943-955, DOI 10.1080/00036810802428938

- the citation line printed on the first page of the file, i.e. exactly the work the bibliography names.

What that page establishes (read on pp. 943-944):

* the paper studies the spatial evolution of solutions of an initial-boundary-value problem in a
  semi-infinite cylinder;
* under null initial data a **Phragmen-Lindelof alternative** is obtained, plus an upper bound for the
  amplitude term in terms of the boundary data;
* for decay solutions the decay is shown to be controlled by the exponential of a second-degree
  polynomial in the distance from the finite end of the cylinder.

That is what "end effects" means in this literature, so **CR019 is SUPPORTED at R3** (register row
updated, deliverable `../P3_evidence_claims_C/claim_check_C_batch_007.csv`, row CC-0036).

One point of the old wording survives and should not be lost: the file named `quintanilla2008.pdf` in
the *library* folder really does hold the Quintanilla-Racke note on stability, not this paper. The
name-match/content-mismatch was real. What was wrong was the conclusion drawn from it - that the cited
paper could not be had. There were two different files with the same name, and the author's copy is the
right one. The library copy must still not be used for the end-effects sentence.
