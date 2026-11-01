# Publication readiness - blueprint status and what is left

Updated 2026-11-01, step 23. Short answer: **the blueprint is frozen and its design checklist is
8 of 9 complete; the manuscript is not at submission level yet.** The blueprint's own
submission checklist (Section 11b) is **0 of 6 items passed**, and every number below is recomputed from the
CSVs in this repository, not remembered.

## 1. Blueprint freeze (design level) - essentially done

| checklist | passed | open |
|---|---|---|
| 11a Blueprint freeze | **8 of 9** | expert readers named by the author (three complementary specialists) |
| 11b Manuscript submission approval | **0 of 6** | all six: P1 audit, R0-free reference register, contribution map, benchmark registry and independent implementations, expert reviews, journal package |

So the answer to "blueprint pura ho gaya?" is: **the design is frozen and the plan is good; the work it describes is
about one third executed.** Freezing the blueprint was never the same thing as finishing the paper - the document
says so itself.

## 2. Phase by phase, against what is in this repository

| phase | exit condition (blueprint) | what exists | status |
|---|---|---|---|
| P0 scope and originality | Section 9 answered; originality matrix done; AMR inquiry and Physics Reports proposal drafted | no originality-matrix or contribution-map file anywhere in the repository; Section 9 items still open (title, journal, expert readers, AI wording, code release) | **not started** |
| P1 integrity audit | audit report; fixes merged; clean build | defect register with 10 entries: 1 fixed, 1 partial, 7 open, 1 observed; 20 claims re-audited; the page-by-page audit of the 134 pages has not been done | **partial** |
| P2 evidence registers | no R0 entries; critical claims at R3 | verification register holds **204 entries** against the blueprint's 323, of which **7 are R0** (62 R2, 127 R1, 4 R3, 4 R1-noDOI); the catalogue check covers **238 entries** with **9 R0**; claim register: 224 rows | **partial** |
| P3 full-coverage expansions | each topic with equations, verified checks, sources, evidence classes | atlas **40 cases planned**, **40 with a fully executable invariant** and **none partial**, and **no case-level result for any of the 40** - the eight rows in the benchmark file are families, not cases; experiment extraction **13 rows**; landmark work done | **partial** |
| P4 integration | registry published in repository | **14 benchmark records**; second implementation with **42 comparisons** | **partial** |
| P5 critical synthesis | tables complete | the old 17-row atlas is still in the manuscript (defect D7); no model-selection guide, no controversy table | **not started** |
| P6 expert reviews | responses logged | none: no reader named, no review received | **not started** |
| P7 submission package | submitted | journal not confirmed, the Elsevier variant has never compiled (D8), no archive DOI, no declaration wording, no cover letter | **not started** |

## 3. Where the evidence stands

The claim register has **224 rows**: 74 supported, 34 partly supported, 5 not supported,
111 carrying `SOURCE NOT AVAILABLE`. Those 111 split, after this week's reading, into
**83 closed** by reading a source, **1 to order**, **4 waived** by the author,
**4 held but unread**, and **19 register-level** rows that need no file.

That is the strongest part of the project: 83 claims now have a page and a quote behind them, and the
5 not-supported rows plus the 34 partly-supported rows have been turned into
**23 paper edits** (5 mandatory, 5 soften-or-re-cite, 9 bibliography, 4 pending).

## 4. What is genuinely done and should not be redone

- The evidence system exists and runs: registers, checkers that print `PASS` and exit 0, a ledger that reconciles
  every blocked claim, a one-page request list, a paper edit sheet.
- 83 claims read at page-and-quote level, including four books and a whole 49-page handbook chapter.
- 10 defects found in the existing manuscript and scripts, 1 already fixed, with the rest specified
  precisely enough to fix.
- A 40-case atlas plan, 14 benchmark records with tolerances, and a second implementation with
  42 comparisons - the skeleton of the reproducibility the blueprint demands.
- 20 flagged claims re-audited, and every wrong bibliography line found so far carries a verified fix.

## 5. What stands between here and a submission

Ordered by what blocks the most. "Agent" means it can be done here without the author.

| # | gap | why it blocks | owner | size |
|---|---|---|---|---|
| A | **23 paper edits**, 5 of them mandatory | the manuscript still says things its own sources contradict | author, in Overleaf | 1-2 days |
| B | **one source still missing** (Born and von Karman 1912, CR181) and four held sources unread | the last blocked claim, plus four free wins | agent + one book | 1 day |
| C | **P1: page-by-page audit of the 134 pages**, and the 7 open defects - above all the overbroad dispersion-polynomial wording (D2) and the 9 scripts with no assertions (D3) | the blueprint forbids new chapters before this passes, and a referee will hit D2 in the abstract | author + agent | 1-2 weeks |
| D | **P2: 7 R0 references remain of the original 32** (the other 25 were repaired on 2026-11-01: 8 completed, 8 replaced, 4 already read, 2 level-aligned, 1 memory entry confirmed, 2 confirmed), **and the register covers 204 entries where the bibliography has 323**; its 204 rows carry 198 distinct bibkeys | "no R0 entries" is a hard exit condition, and an unverifiable reference is not admissible at submission | agent | the remaining 7 need printed copies; extending coverage is 1-2 weeks |
| E | **P3/P4: the atlas has 8 of 40 cases carried through, and 14 benchmark records** | the paper's claim to be verifiable rests on these | agent | 2-4 weeks |
| F | **P5: model-selection guide, controversy table, atlas rebuild** | this is the paper's actual contribution - without it the review is a catalogue | author + agent | 2-3 weeks |
| G | **P6: three expert readers** (continuum thermodynamics, guided waves, numerics or experiment) | blueprint checklist, and the unique way to catch what a machine reading cannot | author | 2-6 weeks, parallel |
| H | **P7: journal confirmed, template compiled, archive DOI, AI declaration, cover letter** | nothing can be submitted without them | author + agent | 3-5 days |

## 6. Honest estimate

- **Two to three weeks of agent work plus the author's edit pass** gets the evidence layer complete and the
  manuscript self-consistent: blocks A, B, D and the script part of C.
- **One to two months** gets the atlas and benchmark registry to the density the blueprint asks for (E).
- **The synthesis (F) and the expert reviews (G) are the real critical path** - a month each, and they cannot be
  shortened by working harder, only by starting earlier.
- Nothing here is a writing problem. What is missing is *checked* content: audit, reproduction, synthesis.

## 7. What can move without the author

1. Finish B: the last book, the four held sources, the readable Polizzotto copy.
2. Continue D: the 32 R0 entries were re-audited on 2026-11-01 and 7 remain, each with a named next action (see `P2_verification/`); the next step is the printed copies, then extending the register from 204 towards 323 (85 rows were added in the coverage extension of 2026-11-01).
3. Start C: add assertions and tolerances to the 9 check and bench scripts so a failure cannot pass silently.
4. Start E: carry the remaining atlas cases from plan to results, one record at a time.
