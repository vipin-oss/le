# V-B7a — PDF request list for the handler's institutional access

**Task item:** B7a of `control/BRAVE_B7.md` (`origin/claude/control` @ `fafb778`).
**Access date for everything cited here:** 2026-10-22. **Scope:** build a ranked, ≤40-row list of
the papers whose full text decides a claim, table cell or equation in the manuscript; mark which
are already open access.

---

## 1. Task

> Create `verification/PDF_REQUEST_LIST.md` and `.csv`: the papers whose FULL TEXT decides a dispute
> or a headline claim, ranked, max 40. For each: DOI, why full text is needed (which equation/claim/
> `file:line` depends on it), what exactly to check in it (page/section if known), legal access route,
> priority 1–3. Must include at least: [list]. Mark which ones are open access already (then you read
> them yourself FIRST and raise read_level to full).

## 2. Method

1. Started from the decision side, not the reading side: took the 17 rows of `CITATION_MAP.csv`
   (which already carry a risk level) plus the 17 WRONG-CONFIRMED / 4 WRONG-PROBABLE defects and the
   4 UNCLEAR items from `V-B6_summary.md`, and asked of each: *which single paper would settle this?*
   A paper entered the list only if it answers a question that is currently open in a V-sheet.
2. Read the open-issue sections of the V-sheets that own those claims (`V-B2p §7`,
   `V-B2d §7`, `V-B2e`, `V-B2f`, `V-B2h`, `V-B4 W1`, `V-B6a D1–D7`) and turned each open issue into a
   concrete "what to check" instruction with a page or equation number where one is known.
3. Located each paper's `file:line` anchor by grepping the read-only manuscript extraction
   (`/tmp/mstree/phase5/master`) — e.g. `sec09_interfaces.tex:140–200` for §9.7,
   `sec06_transport.tex:92–105` for the MDD operator and kernel, `sec12_comparative.tex:101,108` for
   the GN rows, `energy_flux_derivations.tex:317–344` for the OPEN piezoelectric-flux item.
4. Verified every DOI/venue/pages against `LITERATURE_BASE.csv`, Crossref, or the publisher page —
   never from the brief. Two results of that check are corrections (§4 below).
5. Determined OA status from OpenAlex `open_access`/`best_oa_location` (batched DOI queries) and, for
   six items, by actually opening the text. Anything marked OA that would not open stayed a request
   row.
6. Ranked: P1 if the item decides a HIGH-risk claim, a printed equation, or a bibliographic fact the
   manuscript's own numbering depends on; P2 if it decides a table cell or attribution; P3 if it is
   background needed to position the review.

## 3. Result

- **33 rows**, `verification/PDF_REQUEST_LIST.csv` (authoritative long fields) and
  `verification/PDF_REQUEST_LIST.md` (readable, with the coverage matrix for every mandatory item).
  Distribution: **10 × priority 1, 14 × priority 2, 9 × priority 3.** Under the cap of 40 by 7.
- **6 papers were already open access and are NOT request rows**; I read them this session and their
  `read_level` is now FULL (see `V-B7b_oa_fulltext_upgrade.md`):
  Sci Rep 2023 `10.1038/s41598-023-44339-5`; Chiriţă–Ciarletta–Tibullo 2017 `10.1016/j.ijheatmasstransfer.2017.06.071`
  (arXiv:2103.10068); Quintanilla 2019 `10.1177/1081286519862007` (UPC repository); Kovács & Ván
  `10.1007/s00161-017-0610-x` (arXiv:1709.06825) and `10.1016/j.ijheatmasstransfer.2017.10.041`
  (arXiv:1708.09770); Bongarti–Charoenphon–Lasiecka 2021 `10.1007/s00028-020-00654-2` (arXiv:2011.11141).
- **Two items marked OA would not open** and therefore remain request rows: Wang & Li 2011
  (`10.1016/j.camwa.2011.04.028`, bronze; the ScienceDirect PDF endpoint refused my session) and
  Kumar et al. 2023 Phys. Scr. (`10.1088/1402-4896/acfced`, hybrid CC-BY-NC-ND; the IOP page served
  the abstract with the banner "the computer you are using is not registered by an institution with a
  subscription to this article").
- **One mandatory brief item did not resolve** (Mindlin 1961) and **one base hole was found**
  (Green & Naghdi 1992 missing from the 428-record inventory). Both are stated, neither is papered
  over: §4 and `PDF_REQUEST_LIST.md §5`.

## 4. Evidence / sources

Every row of the CSV carries its own DOI and route. The load-bearing new verifications in this sheet:

1. **Quintanilla & Racke 2006** — `10.1016/j.ijheatmasstransfer.2005.10.016`, IJHMT 49(7–8):1209–1213.
   OpenAlex this session: `is_oa: false`, `oa_status: "closed"`, no repository copy. Access level
   available to me: **publisher preview only** (already recorded in V-B2p §4 item 1). Requested for
   the typeset.
2. **Green & Lindsay 1972** — `10.1007/BF00045689`, J. Elasticity 2(1):1–7. Closed. CL-006 (HIGH).
3. **Wang & Li 2011** — `10.1016/j.camwa.2011.04.028`, CMA 62(3):1562–1567. OpenAlex:
   `is_oa: true`, `oa_status: "bronze"`, `pdf_url: sciencedirect.com/science/article/pii/S0898122111003294/pdf`,
   `license: null`. Attempted: the PDF endpoint did not return text. **Read level: not opened.**
4. **Green & Naghdi 1992** — `10.1080/01495739208946136`, J. Thermal Stresses 15(2):253–264
   (bibliographic details from V-B2e, Crossref-confirmed there). **Absent from
   `LITERATURE_BASE.csv`** (verified by grep for "Naghdi": only 1991 `10.1098/rspa.1991.0012` and 1993
   `10.1007/BF00044969` are present).
5. **Green & Naghdi 1993** — `10.1007/BF00044969`, J. Elasticity 31(3):189–208. Closed. The
   type-II/III labelling conflict is documented in V-B7b §3.3.
6. **Lord & Shulman 1967** — `10.1016/0022-5096(67)90024-5`, JMPS 15(5):299–309. Closed.
7. **Guyer & Krumhansl 1964** — `10.1103/PhysRev.133.A1411`, Phys. Rev. 133(5A):A1411–A1417; and
   **1966** `10.1103/PhysRev.148.778`, Phys. Rev. 148(2):778–788. Both closed.
8. **Moore & Gibson 1960** — `10.2514/8.8418`, J. Aerospace Sciences 27. Closed.
9. **Sinha & Elsibai 1997** — `10.1080/01495739708956095`, J. Thermal Stresses 20(2):129–157. Closed.
   A bibliographic query for the name returns the **1996** half-space paper
   `10.1080/01495739608946205`; the interface paper is the 1997 one. Recorded so the wrong DOI is not
   substituted later.
10. **Chandrasekharaiah 1986 / 1998** — Crossref queried this session, one record each:
    `10.1115/1.3143705` = AMR **39**(3):355–376, published 1986-03-01, 835 citations;
    `10.1115/1.3098984` = AMR **51**(12):705–729, published 1998-12-01, 1149 citations, abstract
    states 338 references and calls itself a continuation of the 1986 review. **These two DOIs are
    correctly assigned in `LITERATURE_BASE.csv` (LIT-0038/LIT-0039)** — checked because a swapped pair
    would have been an invisible bibliographic defect.
11. **Roy Choudhuri 2007** — `10.1080/01495730601130919`, J. Thermal Stresses 30(3):231–238
    (Crossref bibliographic query this session). OpenAlex: `is_oa: false`, `closed`.
12. **Barak/Gupta §9.7 set** — six closed DOIs (`10.1080/01495739.2023.2253879`,
    `10.1007/s12648-022-02568-w`, `10.1108/MMMS-10-2022-0209`, `10.1108/hff-04-2022-0259`,
    `10.1108/hff-11-2022-0654`, `10.1088/1402-4896/acfced`); OA status per OpenAlex this session,
    with the IOP access banner read directly.
13. **Mindlin 1974** — `10.1016/0020-7683(74)90047-X`, IJSS 10(6):625–637. OpenAlex:
    `is_oa: false`, `closed`. Attributed this session from Barak et al. 2023 (Sci Rep, **FULL**) as
    the origin of the piezothermoelectricity equations.
14. **Quintanilla 2002** — `10.1515/jnetdy.2002.012`, JNET 27(3):217–227 (page range now confirmed by
    the Crossref record; V-B2p §4 item 4 previously had it incomplete). Closed.

## 5. Checks done

1. Every row's DOI cross-checked against `LITERATURE_BASE.csv` **or** a registrar/publisher record
   fetched this session; 0 rows carry a DOI from the brief alone.
2. The two AMR DOIs checked for correct year–DOI assignment (result: correct, item 10 above).
3. The Sinha & Elsibai 1996/1997 trap tested and resolved by DOI, not by name.
4. OA claims tested by opening: 6 open (read), 2 claimed-open but blocked (kept as request rows),
   25 closed. **No row was upgraded on OA metadata alone.**
5. Row count (33) and priority counts (10/14/9) computed from the CSV, not counted by eye.
6. Every mandatory item in the brief is mapped to a row in `PDF_REQUEST_LIST.md §3`; the two items
   that could not be mapped as asked are stated in §4 of that file.
7. `grep -c "Mindlin"` over every `.tex` in the manuscript tree: **0 hits outside the bibliography
   rows at §7** — this is what makes the "1961 anchor" correction in item 22 a finding rather than an
   opinion.

## 6. Confidence

- **That these 33 are the decision-carrying papers: MEDIUM–HIGH.** The top 10 are traced to specific
  open issues in named V-sheets; the tail (25–33) is judgement about what background the review needs,
  and the handler may reorder it.
- **DOI/venue/page facts: HIGH** for the 31 rows confirmed at a registrar or publisher this session;
  **MEDIUM** for Ackerman 1966 and Tzou's AIAA 1995 paper, whose DOIs are quoted from records I read
  but did not query (flagged in `PDF_REQUEST_LIST.md §7.1`).
- **OA/closed classification: HIGH** — each row names the check that produced it.
- **That the list is complete with respect to the brief's mandatory items: HIGH**, with the two
  documented exceptions (Mindlin 1961; the base hole for GN 1992).

## 7. NOT verified / open issues

1. **Mindlin 1961 not located.** No such record in the base, no citation in the manuscript. I did not
   go hunting for an uncited book chapter — asserting a 1961 Mindlin item without a record would be a
   guess. If Claude has a specific 1961 paper in mind, it must be named with a source, and I will look
   again.
2. **Green & Naghdi 1992 not added to the base.** Adding it would move the accepted count from 428 to
   429. That is Claude's call; I only report the hole.
3. **Subscription routes are inferred from the publisher**, not checked against the handler's library.
   If the institution lacks Emerald or De Gruyter, rows 18–20 and 23 need an interlibrary route.
4. **Page ranges in two rows are partial** (Barak et al. JTS; Roy Choudhuri's issue number). They do
   not affect ordering or identifiability.
5. **Whether any of these 33 would overturn a verdict rather than confirm it: unknown until read.**
   The list is built from open questions, and an open question can close the other way.
6. **No claim in this sheet about the manuscript's correctness.** B7a is a procurement list; verdicts
   stay in the V-sheets that own them, and no verdict was changed by this task.
