# P3-evidence batch 001 - inventory and summary

Mode: evidence extraction only. No manuscript editing, no derivations, no novelty claims.
Repository: vipin-oss/le. Working branch: arena/a7a306f6-le.
Base branch: review-paper-v2 (fetched from origin).
Base SHA (git merge-base HEAD origin/review-paper-v2): 69db6c4f82ce68660e3debc5573b93a2785342c3
Blueprint read before the work: paper_v2/BLUEPRINT_v3.1.md Sections 3 (wave framework and its conditions),
5 (evidence system, R0-R3, claim register) and 6 (verification and validation rules).

Files created in this batch (all new; nothing existing was modified):

- paper_v2/arena_deliverables/P3_evidence/claim_check_batch_001.csv
- paper_v2/arena_deliverables/P3_evidence/layered_dossier_batch_001.csv
- paper_v2/arena_deliverables/P3_evidence/benchmark_candidates_batch_001.csv
- paper_v2/arena_deliverables/P3_evidence/evidence_pages_batch_001.csv
- paper_v2/arena_deliverables/P3_evidence/inventory_and_summary_batch_001.md

## Headline result

Of the nine items requested, one was found in the Drive library and opened: Green and Naghdi 1993
(library file B13-029__bf00044969.pdf). RP7.zip does not exist in the Drive account, and eight of the
nine requested papers (Coleman and Gurtin 1967; Chen and Nunziato 1974; Rayleigh 1885; Love 1911;
Stoneley 1924; Scholte 1947; Barnett et al. 1985; Collet, Destrade, Maugin 2006) were not found.
Consequently the claim check has one supported statement, one partly supported statement and three
rows marked SOURCE NOT AVAILABLE, the layered dossier has no evidence rows, and the benchmark list is
empty. Nothing has been filled from memory, snippets or citing papers.

## Part A - inventory

| item | found | match on first page | file | note |
|---|---|---|---|---|
| RP7.zip (exact name) | no | - | - | see A1 below |
| Green and Naghdi 1993, J. Elasticity 31, 189-208 | yes | title, authors, year | B13-029__bf00044969.pdf | 807004 bytes; opened |
| Collet, Destrade, Maugin 2006 | no | - | - | see A3 below |

A1. RP7.zip is absent. Queries run (all returned 0 files): name contains 'RP7'; name = 'RP7.zip';
name contains 'RP7' and trashed = true. The archive series in the account is RP_!.zip (114048947 bytes),
RP_2.zip (12773333 bytes), RP_5.zip (13984955 bytes) and RP6.zip (18926682 bytes, modified
2026-10-31T06:35Z). RP6.zip is the latest archive, not RP7.zip, and it was not substituted. Its contents
were not listed: the archive is 18.9 MB and the available Drive tooling reads documents, not archive
members, without downloading the whole file into the session. Other archives present in the account and
likewise not opened: LE_PAPERS_P01.zip, LE_PAPERS_P02__was_R3.zip, Manuscript.zip, Beam.zip,
missing paper-23.zip, Flexo.rar, Lamb_Sumit_v2.zip.

A2. Green and Naghdi 1993 was matched on its first page: "Journal of Elasticity 31: 189-208, 1993",
title "Thermoelasticity without energy dissipation", authors "A.E. GREEN and P.M. NAGHDI". The DOI
recorded in the CSV is 10.1007/BF00044969, taken from the library filename suffix bf00044969; no DOI is
printed on the scanned page, so the DOI itself is not verified here.

A3. Collet, Destrade, Maugin 2006 was not found. Name search 'Collet': 0 files. Full-text search
'Collet': 17 files, all citing works or index tables; the four candidate PDFs inspected or identified
are later papers (for example B10-010__LAg_Nonlocal_WM-6 (1).pdf is Lazar and Agiasofitou 2022, Wave
Motion 114, 103038). Full-text search for the title string 'Bleustein-Gulyaev waves in some functionally
graded materials' returned only citing works. No substitute was used.

## Part B - claim check (5 rows, 4 statements)

| statement | cited source | verdict | level |
|---|---|---|---|
| S1 | Coleman and Gurtin 1967 | SOURCE NOT AVAILABLE | R0 |
| S1 | Chen and Nunziato 1974 | SOURCE NOT AVAILABLE | R0 |
| S2 | Chen and Nunziato 1974 | SOURCE NOT AVAILABLE | R0 |
| S3 | Green and Naghdi 1993 | SUPPORTED | R3 |
| S4 | Green and Naghdi 1993 | PARTLY SUPPORTED | R3 |

Verdict count per statement: S1 = 2 rows, both SOURCE NOT AVAILABLE (statement not verifiable from the
library as it stands); S2 = SOURCE NOT AVAILABLE; S3 = SUPPORTED; S4 = PARTLY SUPPORTED.

What the available source actually says (Green and Naghdi 1993):

- p.189, Abstract (a): the heat flow, unlike the Fourier-law case, "does not involve energy dissipation".
- p.190, footnote 2: both type II and type III accommodate finite wave speed, but "only type II involves
  no energy dissipation". This is the basis of the S3 verdict. The paper does not use the word
  "lossless", and in the pages read it performs no dispersion or attenuation calculation.
- p.189, Abstract (b): "a constitutive equation for an entropy flux vector is determined by the same
  potential function which also determines the stress".
- p.192, Section 2.1, eqs (2.15)-(2.17): the entropy flux is listed as a thermal variable with its own
  constitutive equation and the heat flux is related to it through multiplication by the temperature
  (OCR garbled; see the evidence row, manual check required). No sentence was read that states the
  entropy flux is "different from q/T0", and the paper does not define the entropy flux as q/T0 in the
  text read. Hence PARTLY SUPPORTED rather than SUPPORTED.
- p.193, end of Section 2.1: restrictions from the second law are explicitly not recorded in this paper
  ("will not be recorded here"), so this source cannot be used to check S1 or S2 even indirectly.

## Part C - layered and interface wave dossier

Rows: 6 requested, 6 present, 0 with content evidence. All six are marked "-" with verification level
R0 and the search evidence in the notes column. Papers opened for this part: none, because none of the
six was in the library. Papers requested and not found: Rayleigh 1885, Love 1911, Stoneley 1924,
Scholte 1947, Barnett et al. 1985, Collet et al. 2006.

Searches run for this part (navigation only, no keyword extraction of findings):

- filename searches: 'Rayleigh' (17 modern files), 'Love' (3 modern files), 'Stoneley' (0),
  'Scholte' (0), 'Barnett' (0), 'Collet' (0), 'B00' (0, so no separate classics series exists).
- full-text searches for the titles: 'plane surface of an elastic solid' (Rayleigh 1885),
  'Some Problems of Geodynamics' (Love 1911), 'surface of separation of two solids' (Stoneley 1924),
  'range of existence of Rayleigh and Stoneley' (Scholte 1947), 'Barnett', 'Collet',
  'Bleustein-Gulyaev waves in some functionally graded materials' (Collet et al. 2006).
  Every full-text hit was a later paper citing the work, or an index CSV of the library.

No cost was cut by reading a citing paper instead: the task forbids substitution, and a citing paper is
not the source.

## Part D - benchmark candidates

Rows: 0. No Part C paper was opened, therefore no printed value, unit or page could be recorded.
The CSV is header-only by design. Nothing was reconstructed from the Green and Naghdi 1993 paper
either, because that paper prints no benchmark speed, ratio or secular equation in the pages read.

## Evidence ledger

7 rows in evidence_pages_batch_001.csv, all for GreenNaghdi1993 / B13-029__bf00044969.pdf: title page,
abstract items (a) and (b), footnote 2, equations (2.15)-(2.17), the second-law scope sentence, and one
row recording the extraction limit (printed pp.195-205 not retrievable). Two rows carry
manual_check_required = yes: the OCR-garbled eq (2.17) and the unread pages. PDF page numbers were
derived as printed page minus 188, which is exact because pp.189-195 and 206-208 were all read with
their running heads visible.

## Method, limits and rules honoured

- Every statement in this batch comes from a page opened in this session, or is marked "-". No value,
  quote or equation was taken from memory, from an abstract database, or from a citing paper.
- R-levels used as defined in Blueprint Section 5.1: R3 only where an evidence row with an exact page
  and equation location exists; R0 where the source is unavailable.
- No derivations, no reconstruction of garbled equations (eq (2.17) is described in words and marked
  illegible in detail), no novelty claims, no citation sentences for main.tex.
- Source wording quoted is 25 words or fewer per quote.
- The extraction tool returns text from the start of a PDF only, and the platform truncates very large
  tool results at head and tail; that is why printed pp.195-205 of the Green and Naghdi 1993 paper could
  not be read. This is recorded as a limit, not worked around by inference.
- Absolute caveat on the "not found" results: Drive full-text search only sees PDFs that carry a text
  layer. An image-only scan stored under a B-code filename would be invisible to both the filename
  searches and the full-text searches used here. Within that limitation, the conclusion for each missing
  paper is that it is not present in the account.
- No .tex, .bib, script, PDF, zip, BLUEPRINT_v3.1.md or atlas_targets.csv file was modified; only the
  five new files listed at the top were added.
- ASCII only: all five files were scanned for bytes outside the printable ASCII range and for control
  characters after writing; result recorded below. No LaTeX build was run and none is claimed.

## Provenance

- Branch: arena/a7a306f6-le, created content-identically from origin/review-paper-v2 (fast-forward from
  the session branch tip, which was main's tip).
- Base SHA: 69db6c4f82ce68660e3debc5573b93a2785342c3 (git merge-base HEAD origin/review-paper-v2).
- Commit and ls-remote record: see "Provenance record" at the end of this file, added in a follow-up
  commit so that the line can quote a real SHA.
