# V-B19 — the 69-paper EXTENDED_LIST: DOI verification and access triage

**Verifier:** independent verification agent (Arena), batch **B19**, 2026-10-23. This file reports only; it edits no paper text and ingests no source as read.

## 1. Task

Acting for a planned ASME AMR review, verify **every DOI** in the supervisor's new `control/EXTENDED_LIST.csv` (69 wish-list papers, DOIs written from memory and explicitly marked unverified), confirm title, authors, journal, volume/pages and year at Crossref, and — where a listed DOI is wrong — find the correct one or print **NO DOI**; never guess. Then give an **open-access verdict** (OpenAlex, plus targeted Unpaywall) and turn the result into an acquisition sheet split into **Part A (OA) / Part B (paywalled) / Part C (no DOI)**, with papers already in `LITERATURE_BASE` appearing **only as a map**. Also: move the B18 API log into `verification/api_log/`, and state **which three further read comparisons s.12 (GAP-22) needs and whether they are in this list**.

## 2. Method

1. `git fetch origin refs/heads/claude/control:refs/remotes/origin/claude/control --force` → `f95cf21..e09a127`; `git show origin/claude/control:control/EXTENDED_LIST.csv` → 69 rows (the file that B18 reported absent from Drive; it was never a Drive file).
2. Lower-cased, DOI-normalised join of the 69 against `verification/LITERATURE_BASE.csv` (done earlier in this session; **not recomputed** to avoid a second, drifting match): 18 in base, 51 new, of which 2 carry no DOI field.
3. Crossref: `api.crossref.org/works?filter=doi:<up to ten DOIs>&select=DOI,title,author,container-title,volume,issue,page,issued` — seven batched calls covering all 49 DOIs. Each returned record was compared field by field with the citation in the list.
4. Where a DOI was **not returned** (n13, n47) or **returned a different paper** (n12, n14, n35): `query.bibliographic` with the list's title + author + year, then a candidate accepted only when title, author, journal, volume and pages all matched. Five corrections, no guesses.
5. Books n42/n43: `query.author` + `query.title` + `filter=type:book`, and `query.title` + `filter=type:book`. Both returned no book-level record → **NO DOI**.
6. OpenAlex: `api.openalex.org/works?filter=doi:…|…&select=doi,open_access`, four calls covering all 49 DOIs; `per-page=50` honoured.
7. Unpaywall `api.unpaywall.org/v2/<doi>?email=…` for the four items where the verdict mattered: n13, n18, n44, n47 — all four `closed`, agreeing with OpenAlex.
8. Outputs written; B18 log moved with `git mv` (history preserved).

## 3. Result

- **51 new papers verified.** 41 DOIs correct as supplied and metadata matching; **5 DOIs corrected** (n12, n13, n14, n35, n47 — full table in `PDF_REQUEST_LIST_5.md` Part F); 1 title-verified but author-less Crossref record (n28 book); 1 end-page discrepancy (n51: Crossref 129–145, list 129–146); 1 short author list (n58: Crossref omits Casas-Vázquez); **2 with NO DOI** (n42 Podlubny 1999, n43 Kilbas et al. 2006).
- **Access:** 9 open access (2 diamond, 2 green, 1 gold, 3 bronze, 1 hybrid), 40 paywalled, 2 books to be got from a library.
- **Tier split of the 51:** 17 Must (16 paywalled + n60 Quintanilla–Racke 2003 green) and 34 Good.
- **Supervisor's own flags resolved:** n13 "year/DOI uncertain" → 2003, `10.1080/713855996`; n44 "Brave could not resolve" → `10.1007/BF01173936` resolves normally; n35 "(DOI to verify)" → list DOI was a different paper, corrected; n28/n58/n59/n45 books → catalogue-level records found; n3 "(re-confirm?)" → no fetch needed, GL 1972 counts as read under B11 #2.
- **GAP-22 / s.12:** all three missing read comparisons **are** in the extended list; two need only a PDF (n17 Chester 1963 = LIT-0010; n8 Chandrasekharaiah 1998 = LIT-0039), one needs a PDF *and* a new base row (n18 Guyer–Krumhansl 1966). None of the three is open access.
- **No ledger was modified.** `LITERATURE_BASE` (536), `FULLTEXT_FACTS` (152), `REFERENCE_PLAN` (232), `REFERENCE_GAPS` (25), `REFERENCE_READINESS` (20 + TOTAL) are unchanged by B19. Reason: the extended list is an acquisition sheet, and adding 51 unread papers to the base would pad it — the exact thing this verifier exists to prevent. If the supervisor wants these rows created up front at `metadata only`, that is a separate order.
- **Hygiene:** `api_log/B18_crossref_checks.csv` → `verification/api_log/B18_crossref_checks.csv` (`git mv`); new `verification/api_log/B19_extended_doi_checks.csv` (51 rows) in the same directory; repo-root `api_log/` removed.

## 4. Evidence / sources

| source | what it gave | date | access level |
|---|---|---|---|
| `origin/claude/control` @ `e09a127`, `control/EXTENDED_LIST.csv` | the 69 citations, tiers, section tags, unverified DOIs | commit read 2026-10-23 | file read in full (once); values re-quoted from the working copy in `/tmp/ext.csv` |
| Crossref REST `works?filter=doi:` (7 calls) | title/authors/container/volume/issue/pages/year for 49 DOIs | 2026-10-23 | metadata only — **not** full text |
| Crossref `query.bibliographic`, `query.author/title` + `filter=type:book` (6 calls) | correct DOIs for n12/n13/n14/n35/n47; absence of book records for n42/n43 | 2026-10-23 | metadata only |
| OpenAlex `works?filter=doi:…&select=doi,open_access` (4 calls) | `oa_status` + `oa_url` for all 49 | 2026-10-23 | metadata only |
| Unpaywall `v2/<doi>` (4 calls: n13, n18, n44, n47) | independent OA cross-check — all `closed` | 2026-10-23 | metadata only |
| `verification/LITERATURE_BASE.csv` | the 18 in-base matches and their current `read_level` | local, HEAD `2f86331` | local file |

## 5. Checks done

1. **Arithmetic reconciliation:** 18 (in base) + 51 (new) = 69 ✓. Of the 51: 41 + 5 + 2 + 1 + 1 + 1 = 51 ✓. Of the 51: 9 OA + 40 paywalled + 2 no-DOI = 51 ✓. Paywalled 40 = 16 Must + 24 Good ✓; Must 17 = 16 + n60 (OA) ✓.
2. **Wrong-DOI detection, not just resolution:** the three "resolves but wrong paper" cases were caught only because the returned title was compared with the list — a resolver that merely tested "does this DOI exist" would have passed all three. Recorded in the CSV as `DOI-CORRECTED` with the wrong paper named.
3. **No-guess check:** every corrected DOI came back from Crossref with a matching title *and* author *and* volume/pages; no DOI was constructed from a pattern, and the two books were left without a DOI.
4. **OA cross-check:** OpenAlex and Unpaywall agree on all four items sampled; no case of OpenAlex "closed" contradicted by an Unpaywall location.
5. **No double counting:** n41 has two OpenAlex records for one DOI (one green, one gold); counted once, noted.
6. **In-base discipline:** the 18 mapped rows were re-read from `LITERATURE_BASE` to confirm their `read_level` before writing the map — none was re-described, none given a new id.
7. **Scope check:** `git status` after writing shows only `verification/` additions plus the `git mv`; no file outside `verification/` was touched.

## 6. Confidence

- **DOI identity for the 43 papers whose metadata matches exactly: HIGH.** Title + authors + journal + volume/pages/year agree with the list, in some cases letter for letter including publisher caps.
- **The 5 corrections: HIGH.** Each correct record matches the list's title, authors, journal, volume and pages simultaneously, and the wrong DOI is identified as a different, nameable paper.
- **OA verdicts: MEDIUM.** A single-day snapshot of OpenAlex, cross-checked on only four items; repository copies and publisher free-access windows change. Nothing here was fetched to confirm a file actually downloads.
- **Book metadata (n28, n45, n58, n59, n42, n43): LOW.** Crossref book records carry title and year only; authorship, edition and ISBN are unverified.
- **s.12/GAP-22 recommendation: MEDIUM-HIGH.** The three papers are the right ones and all three are in the list, but whether reading them will actually lift s.12 to six *read* comparisons depends on what they say — that is a judgement for after reading, not now.

## 7. NOT verified / open issues

1. **Nothing in this batch was read.** No PDF was opened; all 51 remain unknown as sources. Crossref/OpenAlex/Unpaywall confirm identity and access, never a technical claim.
2. **n28** — Crossref's book record has no author field. That the book is Eringen's is asserted by the list, not confirmed here.
3. **n58** — Crossref lists two of three authors; Casas-Vázquez's co-authorship is unconfirmed (not contradicted).
4. **n51** — end page 145 (Crossref) vs 146 (list). Unresolved; must be settled from the printed article.
5. **n42 / n43** — "NO DOI" means Crossref returns no book-level record, not that no DOI exists anywhere. Edition/ISBN also unverified.
6. **No OA link was tested.** The 9 Part A URLs are what OpenAlex reports; n68's points at the retired `aip.scitation.org` host and is suspected stale. None was downloaded or opened.
7. **The 18 in-base DOIs were not re-verified** in this batch (order 3: map only). Any of them that a later citation depends on still needs its own Crossref pass.
8. **GAP-22 remains open** at 3/6 and stays HIGH severity and blocking for s.12.
9. **No base/plan/facts ingestion** — deliberate, stated in §3; the 51 verified papers exist only in the acquisition sheet until a PDF arrives and is read.
10. **This ends B19.** Per the order, the batch stops here.
