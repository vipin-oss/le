# Job C — what the library already gives me, and what has to come from the author

Source list: `paper_v2/missing_sources_priority.csv` — 141 cited works, ordered by
`claims_blocked`. The question this job answers is not "which citations are weak" but
"which of these 141 can I actually open, and which do I have to ask for".

## Did I actually look in the Drive folders?

Yes — every paper folder was listed file by file this pass (B01 … B14_NEW), and the result is
`library_folder_inventory.csv`: **320 PDFs** across B03–B14_NEW. B01 and B02 were listed too;
they hold the author's own papers (P01–P54), not cited literature.

What the scan shows is that the blocked sources really are not among those 320 files: I read
the file names against the 141 keys by DOI suffix, by author name and by title, and only four
of the 141 have a standalone PDF. The classical works the manuscript leans on (Chirita,
Povstenko, Zener, Chen & Nunziato, Coleman & Gurtin, Moore & Gibson, …) are not in any
batch folder — they live inside the three archive bundles:

| bundle | size | can be extracted here? |
|---|---|---|
| `LE_PAPERS_P01.zip` | 15.5 MB | yes, it is under the cap |
| `LE_PAPERS_P02__was_R3.zip` | 51.8 MB | no — over the 25 MB extraction cap |
| `LE_PAPERS_P03__was_R4.zip` | 62.3 MB | no — over the 25 MB extraction cap |

Seven of the seven largest blocked items sit in P02/P03. So "sab PDF hai" is right about the
library as a whole — 320 loose PDFs plus three bundles — but the specific works that block
the claims are either inside P02/P03 or genuinely absent, and this is the list of them.

## The split

| bucket | works |
|---|---|
| held by the library (ledger says FOUND) | 4 |
| not held: ledger says MISSING | 62 |
| not held: the held file is a *different* paper (mismatch) | 4 |
| not held as a loose PDF, held inside a capped archive bundle | 1 |
| not held: no ledger record at all | 71 |
| **total** | **141** |

Only four of the 141 are in the library. `library_available_sources.csv` lists them;
`pdfs_needed_from_author.csv` lists the rest, highest claims-blocked first.

## `pdfs_needed_from_author.csv` (34 rows)

Columns: `rank, bib_key, authors, year, title, doi, claims_blocked, claim_ids,
availability, library_ledger_status, cited_as_in_priority_list`.

* 30 rows are the top of the blocked list, in descending `claims_blocked`.
* 5 further rows are PDFs that **are** in the library but only inside an archive bundle
  (Quintanilla & Racke 2008 is in `LE_PAPERS_P01.zip`, which is small enough to extract —
  its first page was read in an earlier pass and prints DOI
  `10.1016/j.ijheatmasstransfer.2007.04.045`)
  that this environment cannot extract (the bundle is over the 25 MB download cap). They
  are appended after the cut so they cannot fall off it, and each names both the bundle
  and the member file, e.g.

  | bib_key | bundle | member |
  |---|---|---|
  | Huberman2019 | `LE_PAPERS_P03__was_R4.zip` | `huberman2019.pdf` |
  | Jackson1970 | `LE_PAPERS_P03__was_R4.zip` | `jackson1970.pdf` |
  | Cahill2003 | `LE_PAPERS_P02__was_R3.zip` | `cahill2003.pdf` |
  | SecondSound1970review | `LE_PAPERS_P02__was_R3.zip` | `2ndSoundSolids.pdf` |

  Extract those four members from the two bundles and the second-sound evidence base is
  complete without the author having to send anything.

**DOI policy.** A DOI appears only where the project's own record says it was verified —
`verification_register.csv` with a "verified" status, or the Task-4 survey
(`P3_experiments/experiments_1.csv`), whose `doi_source` column states where each one was
seen. Everything else is the literal `NOT FOUND`. No DOI was typed from memory and none was
inferred from a title. Titles come from the register, else from the manuscript's own
classified catalogue; where neither has one the field says so instead of guessing.

## `library_read_findings.csv` (3 rows, Task-1 format)

The four in-library works were opened; three claims could be judged from them.

| claim | page | source read | verdict |
|---|---|---|---|
| CR196 | p. 67 | Eringen 1974, p. 1063 (title + abstract) | **SUPPORTED** — the paper *is* the extension of nonlocality to thermoelasticity |
| CR182 | p. 66 | Eringen 1972, pp. 425–426 | **PARTLY SUPPORTED** — the linearised nonlocal theory and the plane-wave fit are there, but the Yukawa kernel / `(1 − ξ²∇²)σ = C:ε` form is not on the pages read, and Eringen 1983 has no ledger record |
| CR043 | p. 39 | Ezzat & El Karamany 2011, pp. 937–939 | **PARTLY SUPPORTED** — a fractional heat-conduction law with the modified Riemann–Liouville derivative is used, but the explicit flux equation is not on the pages read and the other two cited works were not opened |

The fourth in-library work (Li2019) could not be located among the library's files in this
pass, so no claim of its own is marked.

Nothing was upgraded on the strength of a title, an abstract line, or a filename: each
verdict records the page range actually read, and the notes say what would be needed to
raise it.

## Reproduce

```
python3 make_pdfs_needed.py     # rebuilds both lists from the register + priority CSV
python3 check_pdfs_needed.py    # stdlib only; prints PASS all checks and exits 0
```

`make_pdfs_needed.py` carries the library-status map transcribed from the library's own
ledger (`SOURCE_LEDGER.csv`, status + evidence columns). Where the ledger records that the
held file is a different paper, the work is treated as **not held** — that is the whole
point of the mismatch rows.

## Grouping by bundle — `pdfs_needed_by_bundle.csv`

The 34 rows, sorted into the three bundles plus a fourth group that needs a fresh download.

| group | bundle | rows | files to pull out |
|---|---|---|---|
| **P01** | `LE_PAPERS_P01.zip` (15.5 MB) | 1 | `quintanilla2008.pdf` |
| **P02** | `LE_PAPERS_P02__was_R3.zip` (51.8 MB) | 2 | `cahill2003.pdf`, `2ndSoundSolids.pdf` |
| **P03** | `LE_PAPERS_P03__was_R4.zip` (62.3 MB) | 2 | `huberman2019.pdf`, `jackson1970.pdf` |
| **separate** | — | 29 | nothing to extract; these have to be downloaded |

Why so few in the bundles: the library ledger records, for almost every one of the 29, that
the bundle *was* searched and the member found there is a different paper. Two cases are
written into the `note` column so they are not re-tried:

* `ChenGurtin1968` — P03 holds `gurtin1968.pdf`, but that is Gurtin & Pipkin 1968, not Chen & Gurtin.
* `vanDerMerwe2021` — P01 holds `quintanilla2008.pdf`, which is Quintanilla & Racke 2008.

That last member is also why `Quintanilla2008` (the Applicable Analysis paper, DOI
`10.1080/00036810802428938`) carries a warning: it must not be confused with the P01 member
of the same name, which belongs to `Quintanilla2008a`.

For the 29 separate rows, `suggested_save_as` gives a name to save the download under
(`chirita2016.pdf`, `zener1937.pdf`, …). It is only a naming suggestion — it is not
something read out of the library.
