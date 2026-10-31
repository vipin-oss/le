# `pdfs_needed_from_author.csv` - Step 3 rewrite

The file was rewritten for the current step. It now carries **only the sources that are still not
held**, and only the **top 20** of them. Everything that was resolved in Steps 1-2 has left the list.

## What changed

| change | detail |
|---|---|
| dropped, source read | `Quintanilla2003DPL` (CR003) - read this step, batch 006 |
| dropped, source read | `Fabrizio2014` (CR006), `DellOroPata2016Viscoelasticity` (CR028), `ChenGurtin1968` (CR033) - read in batches 001-004 |
| dropped, no blocked claim left | `SecondSound1970review` (CR098 was already resolved) |
| moved out of the list | `Quintanilla2008a`, `Jackson1970`, `Huberman2019`, `Cahill2003` - all four are **in** the library, inside over-cap archive bundles; they are now recorded in `pdfs_held_in_archives.csv` as custody records |
| trimmed | `ChenNunziato1974` keeps only CR084; CR083 was checked on p. 1 of the paper (batch 005) |
| cut | ranks 21 onwards of the still-missing sources (25 remain; the top 20 are listed) |

`pdfs_needed_by_bundle.csv` is retired: it grouped the old 34-row list, which no longer exists. Its
useful part - which over-cap member sits in which bundle - survives as `pdfs_held_in_archives.csv`.
`check_pdfs_needed.py` was updated to the new scope, and it now cross-checks the needed list against
the `P3_evidence_claims_C` batches so that a claim already read from a held source cannot linger here.

## The DOI column is now almost entirely `NOT FOUND`, on purpose

The instruction is that a DOI is written only when it is printed on the page. **None of these
sources is held**, so there is no page to read, and asserting a DOI from a bibliography would be
exactly the kind of guess the project forbids. Where the manuscript bibliography does carry a DOI,
it is preserved as prose in the `availability` column - "the bibliography carries DOI ..., but no
page of this work was read, so the DOI is not asserted here" - so the author still sees it while the
`doi` column stays honest. That is why the six rows that used to show a DOI now show `NOT FOUND`
with the DOI spelled out one column over.

## The 20 rows, in order

| rank | key | blocked claims | why it matters |
|---|---|---|---|
| 1 | Chirita2016 | CR115 CR129 CR134 | three-phase-lag thermodynamic compatibility; three claims at once |
| 2 | Zener1937 | CR140 CR141 | the original thermoelastic-damping paper |
| 3 | MindlinTiersten1962 | CR190 CR200 | the piezoelectric plate/bar model |
| 4 | Eringen1983 | CR183 CR185 | the differential form of nonlocal elasticity |
| 5 | Chandrasekharaiah1996 | CR138 CR155 | the DPL review that fixed the notation |
| 6-8 | Povstenko2004, 2007, 2009 | CR040/041/042, CR063/064/065 | fractional heat conduction and its thermal stresses |
| 9 | Chirita2017 | CR116 CR130 | the TPL model, second paper |
| 10 | Prasad2020 | CR035 CR058 | hyperbolic two-temperature plane waves |
| 11 | MooreGibson1960 | CR024 | the MGT origin |
| 12 | ChenNunziato1974 | CR084 | the remaining half of the ZAMP paper, after CR083 |
| 13 | Tzou1997 | CR002 | the DPL paper itself |
| 14 | Antaki2000 | CR022 | damping in thermoelastic resonators |
| 15 | Quintanilla2002b | CR004 | the DPL existence/uniqueness paper |
| 16 | Quintanilla2006 | CR005 | stability in type III |
| 17 | Quintanilla2008 | CR019 | TPL end effects (see Step 5: still absent from the folder) |
| 18 | Quintanilla2009 | CR021 | exponential decay in TPL |
| 19 | MarchandMcDevittTriggiani2012 | CR025 | the MGT semigroup paper |
| 20 | Rukolaine2014 | CR007 | the critique of the Cattaneo/DPL finite-speed claim |

Nine of the twenty are Quintanilla or Povstenko items, so a single request to the author for those two
authors' papers would clear most of the list.
