# Publishing this paper: the complete pending list

Written 2026-11-01, after step 24. This is the one page to read before promising a date.
It answers a single question: **what is still standing between the manuscript and a submitted
paper?** Every number here is recomputed by `check_publish_pending.py` from the registers,
except the ledger split (83 / 1 / 4 / 4 / 19), which `check_readiness.py` enforces.

The short answer: the blueprint's own submission gate, section 11b, stands at **0 of 6**
and all six boxes are still empty. The design gate, 11a, is at **8 of 9** — only "expert readers named by the author"
is open. So nothing is wrong with the plan; what is missing is all execution.

---

## 1. The six hard gates, as they stand

| # | gate (blueprint 11b) | state today | owner |
|---|---|---|---|
| G1 | P1 audit of the 134 pages, derivations and the 35 scripts complete | **not started** as an audit; 10 defects registered, **7 of the 10 defects are OPEN** | author + agent |
| G2 | no R0 entries; critical claims at R3 or independently derived | **7 are R0** (down from 32), catalogue check **238 entries** with **9 R0**, register covers **204 entries** of the bibliography's **323** | agent, plus print access |
| G3 | contribution map filled and checked against prior reviews | **no such file exists**; P0 has not started | author + agent |
| G4 | benchmark registry complete, independent implementations done | **14 benchmark records**, **42 comparisons**; atlas **40 cases planned**, **29 with a fully executable invariant** and **5 partial**, and **no case-level result for any of the 40** - the eight rows in the benchmark file are families, not cases | agent |
| G5 | two or three expert reviews received and resolved | **0 named, 0 invited, 0 received** | author (external people) |
| G6 | journal fit confirmed, template, declarations, archive DOI | **journal not chosen**; the Elsevier variant has never compiled; no archive DOI, no declaration wording, no cover letter | author + agent |

---

## 2. Gate by gate, item by item

### G1 — the audit (biggest single block of work)

What 11b literally asks for is an audit of the 134 pages, the derivations and the 35 scripts
(12 check/bench/table scripts plus 23 figure scripts). What exists:

- **neither the 134 pages nor the 35 scripts are in this repository.** It holds the registers,
  the deliverables and one summary `.tex`; the manuscript and the scripts live in the Overleaf
  project. So the audit cannot even start until the project has been pulled into
  `paper_v2/from_overleaf/` - and the pull has to run on the author's machine, because the
  Overleaf git host is not reachable from the agent's sandbox. `pull_from_overleaf.sh` is ready
  and does it in one command.

- the page-by-page audit: **0 of 134 pages**. Nothing in the repository walks the manuscript
  page by page. The nearest thing is 20 flagged claims re-audited and a 10-entry defect register.
- **9 of the 35 scripts** have no assertions or coded tolerances (D3). They print numbers and a
  human reads them, which means a check can fail silently. This is the defect most likely to
  embarrass the paper, because it makes every other number unverifiable in the same breath.
- **D2, the overbroad phrasing** "one coupled dispersion polynomial", is still in the abstract
  and in four other places. It is not true for exact delays, fractional powers or hereditary
  models, and a referee will find it in the first paragraph.
- **23 paper edits** are written and waiting, **5** of them mandatory; the author applies them in
  Overleaf. The 5 claims are NOT SUPPORTED verdicts, and all five are already covered by that sheet.
- **D4** (pinned environment) is partial: `requirements.txt` exists, a clean-environment run and
  archive checksums do not.
- **D6** (about 65 catalogue-only bib entries absent from the text), **D8** (the Elsevier variant
  never compiled) and **D9** (an unexplained TeX message line) are open.
- the clean build has to happen where the manuscript lives, i.e. on the author's side.

### G2 — the evidence side

- **7 rows are still R0**: Chadwick 1960 (Progress in Solid Mechanics 1), Auld 1973 (Wiley),
  Duhamel 1837 (J. Ecole Polytechnique 15), Scruby 1990 (Adam Hilger) and Gulyaev 1969 (JETP
  Letters). Each needs a printed page, not a search: this is a library or a purchase, not an
  analysis job.
- **9 catalogue rows are R0** in the separate 238-entry catalogue check.
- the register holds **204 entries** against the bibliography's **323**. That 323 is the
  blueprint's count of the manuscript's own bibliography (section 10, P2), and the three `.bib`
  files in this repository carry only **199 unique keys** between them, so the register cannot be
  finished here either: it needs the manuscript's bibliography file from Overleaf. Filling the
  remaining 119 works is still the longest single thread in P2, though 85 rows were verified in the
  coverage extension of 2026-11-01 and only the keys the repository does not hold are left.
- **4 held sources are unread** (CR127 Muller and Ruggeri; CR152 Gurtin and Williams; CR166 Li et
  al.; CR196 Eringen). Their citations are verified; two of them can be closed by rewording
  (proposals are in `P2_verification/HELD_SOURCES_2026-11-01.csv`), two need a copy.
- **1 claim still waits on one work**: CR181, Born and von Karman 1912. The author is supplying
  Born and Huang as the substitute; it has not arrived yet.
- **111 claims** still carry SOURCE NOT AVAILABLE; the four buckets below are what is left of
  them after the closed ones are removed.
- **4 claims were waived** by the author, which means two sentences citing them must be rewritten
  before submission, not after.
- **19 claims are register-level**: they need a register row, not a reading, and each is a
  twenty-minute job.
- the register carries **198 distinct bibkeys** over 204 rows: six bibkeys are duplicated across
  batches 003 and 004 and need the author's sign-off to be de-duplicated. Cosmetic, but a referee
  who counts will notice.

### G3 — the contribution map

Nothing exists. 11b wants a map of what this review claims as new, checked line by line against
the prior reviews (the bibliography's 323 entries include them). This is the gate that decides
whether the paper is a review or a contribution, and it is the cheapest of the six to start and
the most expensive to do badly. It needs the author's judgement, not a machine reading.

### G4 — benchmarks and the atlas

- **14 benchmark records**; the registry is published in the repository, but "complete" is not yet
  defined against the paper's own schemes.
- **42 comparisons** in the second implementation.
- the atlas is the visible hole, and it is smaller than it looked. Of the **40 cases planned**, **29 have a
  fully executable invariant** and **5 more a partial one**; **6 have none**, and all six are coupled multifield
  cases waiting on BK-15. Steps 29 and 30 wrote the invariants for the plate, layer, interface and thermoelastic
  surface families (BK-12, BK-13, BK-14, BK-10), each validated against a classical closed form rather than
  against itself. What is still missing: a branch-count invariant for m > 2 (BK-11, the five porous cases) and the
  coupled-field one (BK-15). And no case has a case-level result today - none can have one until the papers are
  read past their titles.
- experiment extraction stands at **13 rows** and can be extended as sources allow.

### G5 — expert readers

Zero. 11b wants two or three. This is also the item holding 11a at 8 of 9. The blueprint names
three complementary specialities (continuum thermodynamics, guided waves, numerics or experiment)
and says names are fixed in P0 and do not delay P0-P2 — that has not happened, so an invitation
that should have gone out weeks ago has not gone out. Reviews take four to six weeks to come back.
**Nothing else in this list is paced by other people; this one is.** It should start first.

### G6 — the package

- **journal not confirmed**: the strategy is an AMR inquiry first with a Physics Reports proposal
  as the alternative, and P0 asks for both to be drafted; neither exists.
- **the Elsevier variant (`main_els.tex`) has never compiled** (D8) — the template work is paused
  until a journal is chosen, so the choice unblocks it.
- no **archive DOI** (a Zenodo or equivalent deposit of code, data and the check scripts),
  no **AI-use declaration** wording, no **cover letter**, no **data and code availability
  statement**, and no author, funding or competing-interest block in the repository.
- the AI declaration wording is explicitly deferred until the journal is known.

---

## 3. What only the author can do, what only a machine can do, what needs money

| owner | items |
|---|---|
| **author only** | the 23 paper edits in Overleaf (5 mandatory); the 4 waived-citation sentences; the 34 PARTLY SUPPORTED claims that need a wording hedge or a better source; naming and inviting the 3 expert readers; choosing the journal; the declarations and cover letter; signing off the de-duplication of 6 register rows |
| **agent only** | assertions and tolerances in the 9 scripts (D3); D6 catalogue-only entries; the register 204 towards 323; the porous branch-count invariant (BK-11) and the coupled-field one (BK-15); the model-selection guide and the controversy table once the author approves the shape |
| **needs the Overleaf project first** | the page-by-page audit of the 134 pages; the assertions in the 9 scripts; D6, D8, D9; the final clean build. All of it is blocked until the project is pulled into `paper_v2/from_overleaf/` |
| **needs money or a library** | the 7 R0 works (Chadwick 1960, Auld 1973, Duhamel 1837, Scruby 1990, Gulyaev 1969 — five distinct works); Muller and Ruggeri 1998; a readable Polizzotto 2001 for CR195 |
| **needs other people** | G5, the three expert reviews; and the journal editor's own response |

---

## 4. The order that actually works

The dependencies, not the effort, set the order. Expert readers must be invited in week 1 because
their reply is the longest lead time; the journal must be chosen before the template can be made
to compile; the atlas must be finished before the synthesis can be written, because the synthesis
is built on it.

| when | what | who |
|---|---|---|
| week 0 | run `pull_from_overleaf.sh` on the author's machine so the manuscript and the 35 scripts are in the repository: four later items are blocked on it | author |
| week 1 | apply the 23 edits, rewrite the 5 NOT SUPPORTED sentences, hedge the 34 PARTLY SUPPORTED ones; **invite the three expert readers**; pick the journal and send the AMR inquiry | author |
| week 1-2 | assertions in the 9 scripts; 19 register-level claims; 9 catalogue R0 rows; chase the 5 print-only works | agent |
| week 2-3 | the page-by-page audit of the 134 pages, defect by defect, with the 7 open defects closed as it goes | author + agent |
| week 3-6 | BK-11 (porous, m > 2) and BK-15 (coupled multifield), then reading the 40 papers so the cases can carry numbers | agent |
| week 4-6 | P5 synthesis: model-selection guide, controversy table, atlas rebuild, the 17-row atlas replaced (D7) | author + agent |
| week 4-8 | expert reviews arrive, are answered in writing, and the answers are folded into the text | author |
| week 6-7 | contribution map and the comparison against prior reviews (G3) | author + agent |
| week 7-8 | template compiles, declarations written, archive deposited with a DOI, cover letter, final clean build, final audit, submit | author + agent |

**Honest estimate: 6 to 8 weeks** if the expert invitations go out in week 1 and the author's edits
do not slip a week. If the readers take the usual six weeks to reply, **8 to 12 weeks**. The
existing readiness note estimated 2-3 weeks for the audit and script work and 1-2 months for the
atlas; nothing in step 24 changed that, it only removed 25 reference rows from the critical path.

---

## 5. Definition of done, gate by gate

Concrete, so that no gate can be declared passed by good intentions:

- **G1** — every one of the 134 pages has an audit line; all 35 scripts raise on failure; D1-D10
  are all FIXED or explicitly closed; the manuscript compiles in a clean environment with the
  pinned versions; the 23 edits are applied.
- **G2** — the verification register has no R0 row that is not explicitly excluded with a written
  reason; the bibliography's 323 entries each have a row or an exclusion; the catalogue's 9 R0
  rows are resolved; no claim cites a paper nobody has opened.
- **G3** — a contribution map exists, each claim in it points at a manuscript section, and each is
  checked against at least one prior review in the bibliography.
- **G4** — every atlas case that appears in the paper has a results record; every benchmark in the
  registry reproduces from versioned code inside the stated tolerance.
- **G5** — three written reviews are in the repository, each with a numbered response and either a
  change or a recorded decision not to change.
- **G6** — a chosen journal, a compiling template for it, the declarations, an archive DOI that
  resolves, and a cover letter.

---

## 6. What could still go wrong

1. **The experts say no, or say nothing.** Two refusals turn three readers into one; that is a
   two-week recovery, not a one-day one. Invite five to get three.
2. **The 5 print-only works stay unfindable.** Then the honest move is exclusion with a written
   reason, which blueprint §12.1 already permits — never a forced promotion to R1.
3. **The atlas does not finish.** Then the paper must be described as covering 8 of 40 cases with
   the rest scheduled, and the claim of full coverage in the manuscript comes out. That is a
   writing decision the author has to make before submission, not after review.
4. **The journal choice slips.** It blocks the template, the declarations and the AI wording all at
   once, and it is a one-afternoon decision.
