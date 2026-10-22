# V-B14 — Green–Naghdi type II/III mapping, Moore–Gibson scope, Tzou 1995

**Batch:** B14 (items 1–5 of the post-B13 list). **Date:** 2026-10-22.
**Input read:** `control/FULLTEXT_FINDINGS_04.md` F13–F15, fetched from `origin/claude/control` at **`41adb03`** (`refs/heads/claude/control:refs/remotes/origin/claude/control --force`; a plain `git fetch --all` left the remote-tracking ref on the stale `6933a50`, so the explicit refspec was used and `git log --oneline -1` confirmed `41adb03`).
**Standing rule applied:** supervisor-relayed facts are `SECONDARY-SOURCE` in this repo unless I opened the document myself. I opened none of the three papers below.

---

## Task

Five corrections requested after F13–F15: (1) GAP-04 + LIT-0430 → GN **type III**; LIT-0005 → **type II**, with its equations made an explicit reading target; (2) add Tzou 1995 to the base as the supervisor-read DPL primary, tagged SECONDARY-SOURCE; (3) re-label Moore–Gibson 1960 per F14; (4) rewrite the Tzou 1997 row of `PDF_REQUEST_LIST_2.md` per F15; (5) sweep the two ledgers for every GN-II/III or 1992/1993 attribution and list each row whose disposition changes.

## Method

1. Fetched the control branch (explicit refspec) and read `FULLTEXT_FINDINGS_04.md` in full.
2. Grepped `EQUATION_LEDGER.csv` and `CLAIM_LEDGER.csv` case-insensitively for `GN.?II`, `GN.?III`, `type I`, `1992`, `1993`, `Tzou`, `Moore`, `MGT`, `Gibson`; opened every hit's full row and its note.
3. Checked before writing that the four papers were already in `LITERATURE_BASE.csv` (they were: LIT-0004, 0005, 0007, 0365, 0430) and that no Tzou 1995 row existed in `FULLTEXT_FACTS.csv` (it did not).
4. Applied all edits through Python `csv.DictReader`/`DictWriter` with the original header list, then re-read every file and compared row counts and column counts against `HEAD` to confirm nothing was reflowed.
5. Cross-check that no manuscript `.tex` exists in this repo, so every `file_line` anchor touched here is **annotated, not re-checked**.

## Result

### 1. The mapping (F13, PRIMARY-SOURCE-CHECKED for the labels only)

| type | paper | which label my earlier notes used |
|---|---|---|
| I | classical Fourier (in none of the three GN papers) | — |
| **II** | **Green & Naghdi 1993, *J. Elasticity* 31, 189–208**, "Thermoelasticity without energy dissipation" | I had called 1992 the II paper — **WRONG** |
| **III** | **Green & Naghdi 1992, *J. Thermal Stresses* 15, 253–264**, "On undamped heat waves in an elastic solid" | I had called 1993 the III paper — **WRONG** |

All three types are introduced in **GN 1991** (*Proc. R. Soc. A* **432**) — scanned, no text layer, **not read**; it stays `LIT-0004` with that stated.
F13's anchors: the 1993 paper prints "thermoelasticity type II, since it involves no dissipation of energy", and its integral identity (4.15) carries a `K*θ²`-type term; the 1992 paper's field equations (3.19)–(3.20) carry **both** the `K∇θ̇` and `K*∇·` terms, and its footnote says both types admit finite wave speed while only type II is dissipation-free. Undamped waves arise in type III only for small conductivity (`K ↔ K*/a₀`, their eq. 4.10).

### 2. Base-file edits (5 rows, `LITERATURE_BASE.csv`, 499 rows unchanged)

- `LIT-0005` → `sub_area` now **"GN type II (no dissipation) — PRIMARY for GN-II"**, with the F13 flags, the retraction of my GAP-04 wording, and the **explicit target**: transcribe the linearised type II flux `q = −k*∇α` and identity (4.15) *before* sec. 4.5 is written.
- `LIT-0430` → **"GN type III … PRIMARY for GN-III"**, with (3.19)–(3.20), the footnote, and the small-conductivity limit (4.10) named as the transcription target.
- `LIT-0007` (Tzou 1995) → `read_level` = **`SECONDARY-SOURCE (supervisor-read …)`**; `why` records that this is the DPL primary for sec. 4.7 and that the manuscript key `Tzou1997` conflates it with the book.
- `LIT-0365` (Moore & Gibson 1960) → `sub_area` = **"gas dynamics — third-order acoustic equation (NOT a heat-conduction law)"**, with F14's scope note and the "cite as the origin of the third-order acoustic equation only" instruction.
- `LIT-0004` (GN 1991) → notes that the three types were introduced there.

### 3. `FULLTEXT_FACTS.csv` — **102 rows** (was 101)

One new row, `Tzou1995DPL`, deliberately **identity-and-role only**: `status` and `read_level` both say `SECONDARY-SOURCE`, and the `law_or_model_as_printed` cell states in words that **nothing is claimed about what the paper prints**, because F15 relayed the identification, not an equation. It carries the citation (JHT **117**, 8–16, `10.1115/1.2822329`), the conflict (key `Tzou1997`, pp. 110–116), and the instruction to separate the paper from the book. No lag-ordering claim is recorded — I have no printed statement to support one.

### 4. Moore–Gibson per F14

`LIT-0365` and `EQ-173` now both say: *Propagation of Weak Disturbances in a Gas Subject to Relaxation Effects*, *J. Aerospace Sci.* **27**, 117–127, DOI `10.2514/8.8418`; third-order wave equation for sound in a relaxing gas, with attenuation, dispersion and discontinuous fronts. **No heat-conduction law.** "MGT thermoelasticity" is an **analogue**; the thermoelastic primaries are Quintanilla 2019 (`LIT-0041`, `10.1177/1081286…`) and its successors. Thompson 1972 **not found and not cited**.

### 5. Ledger sweep — every row whose disposition changes

**No verdict changes numerically, and that is the substantive finding:** the ledgers label models by *name* (`GN-II`, `GN-III`), never by year, so the F13 correction cannot flip a correct/incorrect cell. What changes is **attribution** — which paper each correct row must cite.

| row | file | printed/assumed model | verdict now | what changed |
|---|---|---|---|---|
| EQ-044 | EQUATION | GN-II | CORRECT (unchanged) | cite **1993**, not 1992 |
| EQ-045 | EQUATION | GN-II | CORRECT | cite 1993; `q=−k*∇α` is the printed II law |
| EQ-098 | EQUATION | GN-II (=EQ-044) | CORRECT | cite 1993 |
| EQ-120 | EQUATION | GN-II | CORRECT | cite 1993 |
| EQ-047 | EQUATION | GN-III | CORRECT | cite **1992**, not 1993 |
| EQ-099 | EQUATION | GN-III | CORRECT | cite 1992 |
| EQ-119 | EQUATION | GN (α̇ = T) | CORRECT | II = 1993 and III = 1992 only |
| EQ-050 | EQUATION | unstated (MGT-like) | **UNCLEAR** (unchanged) | `τ=0 ⇒ GN-III`, i.e. the **1992** paper; and F14 forbids rescuing this row by appeal to Moore–Gibson |
| EQ-165 | EQUATION | Table 12-A, GN-II/III flux cells | **WRONG (CONFIRMED)** (unchanged) | now additionally: the table attaches the years the wrong way round; F13 is the cited authority |
| EQ-173 | EQUATION | MGT year row | **WRONG (CONFIRMED)** (unchanged) | 1960 date is right; the **role wording** must read "acoustic equation 1960 → thermoelastic analogue 2019" |
| CL-007 | CLAIM | GN-II dissipation-free | CORRECT-CONDITIONAL (unchanged) | statement is *printed* in 1993; citation year fix |
| CL-008 | CLAIM | GN-II | CORRECT (unchanged) | cite 1993 |
| CL-009 | CLAIM | GN-III → GN-II limit | CORRECT-CONDITIONAL (unchanged) | **my supporting note was wrong**: the limit is `k→0`, not `k*→0` (which gives Fourier); the note is corrected in the row itself |
| CL-043 | CLAIM | type II energy identity | CORRECT (unchanged) | identity is GN 1993 (4.15) |

Unaffected, confirmed by the grep rather than assumed: EQ-017 (classical only), EQ-077/078/087 (GN-II, no year claim), CL-025 (family list), CL-040 (Povstenko ↔ LS/GN-II interpolation; verdict left as WRONG (PROBABLE), F13 does not bear on it).

### 6. `REFERENCE_GAPS.csv` (4 rows touched, no row added or removed)

GAP-04 → GN **1993** type II; GAP-05 → GN **1992** type III; GAP-06 → DPL primary is Tzou 1995 (book separated); GAP-08 → Moore–Gibson role corrected. GAP-04's old sentence is **deleted, not hedged**.

### 7. `PDF_REQUEST_LIST_2.md`

Row 2 replaced by **Tzou 1995, JHT 117:8–16, `10.1115/1.2822329`** and demoted from "request the document" to "confirm the printed equation numbers", since the supervisor has already read it. The 1997 book survives as row **2b**, explicitly marked *superseded row, kept for the record*, with no DOI and the 2014 Wiley edition `10.1002/9781118818275` as the only verifiable form. The note under the table and the "what I am asking for" list were rewritten to match.

## Evidence / Sources

- **Green & Naghdi 1993**, *J. Elasticity* **31**, 189–208 — **not opened**; relayed by `control/FULLTEXT_FINDINGS_04.md` F13 (supervisor-read), accessed 2026-10-22.
- **Green & Naghdi 1992**, *J. Thermal Stresses* **15**, 253–264 — **not opened**; same source.
- **Green & Naghdi 1991**, *Proc. R. Soc. A* **432** — scanned, no text layer, **not read** (control findings 02, item 8).
- **Moore & Gibson 1960**, *J. Aerospace Sci.* **27**, 117–127, `10.2514/8.8418` — Crossref record checked earlier this session; scope relayed by F14; **not opened**.
- **Tzou 1995**, *J. Heat Transfer* **117**, 8–16, `10.1115/1.2822329` — identifier from Crossref; **identification** relayed by F15 (supervisor opened `1.2822329.pdf`); **I did not open it**.
- **Tzou 1997** book, Taylor & Francis — **no Crossref record**; 2nd ed. Wiley 2014 `10.1002/9781118818275`.
- Local: `control/FULLTEXT_FINDINGS_04.md` at `origin/claude/control` `41adb03`; `verification/LITERATURE_BASE.csv`, `FULLTEXT_FACTS.csv`, `EQUATION_LEDGER.csv`, `CLAIM_LEDGER.csv`, `REFERENCE_GAPS.csv`, `PDF_REQUEST_LIST_2.md`.

## Checks done

- **Row/column integrity:** before/after via `csv.DictReader` against `HEAD` — LITERATURE_BASE 499→499 (5 changed), FULLTEXT_FACTS 101→102, EQUATION_LEDGER 176→176 (10 changed), CLAIM_LEDGER 53→53 (4 changed), REFERENCE_GAPS 16→16 (4 changed); column counts unchanged (12/10/9/9/9).
- **No duplicate insertion:** grepped for `Tzou` in the facts file first; `Tzou1995DPL` is the only Tzou row, and LIT-0007 was reused rather than re-added.
- **Own-group neutrality:** none of the five papers is own-group, so no `CONDITIONAL` rule applies here; CL-040's own-group-adjacent verdict was left untouched.
- **WRONG-verdict discipline:** the two new WRONG-adjacent statements are not new verdicts — EQ-165 and EQ-173 were already WRONG (CONFIRMED) and were re-verified against my own V-B2d/V-B2i notes by grep before annotating; sub-system named in each note (Table 12-A flux column; MGT order-in-space cell).
- **No fabricated transcription:** no equation from GN 1992/1993, Moore–Gibson or Tzou 1995 is reproduced; the only equations written are the flux laws already recorded in V-B2d, quoted from my own earlier check.
- **`file_line` honesty:** the repo holds no manuscript source, so sec04/sec12/sec10 anchors were **not** re-checked; the annotations say so.
- **Self-correction recorded:** CL-009's old note (`k*→0 ⇒ GN-II`) is wrong under the flux law `q = −(k*∇α + k∇θ)`; corrected in-row rather than quietly dropped.

## Confidence

- **HIGH** for the type II/III ↔ 1993/1992 mapping as *relayed* — F13 is explicit and quotes both papers' printed statements.
- **HIGH** that no ledger verdict flips: the ledgers carry no year strings for these models, checked by grep, not by memory.
- **MEDIUM** for the Tzou 1995 ↔ 1997 separation as a bibliographic fact — identifier verified at Crossref, role relayed by F15; the paper's contents remain unread by me.
- **MEDIUM** for the Moore–Gibson scope statement — F14 is specific, but I did not open the 1960 paper.
- **LOW** for anything about the actual printed equations, which remain untranscribed.

## NOT verified / open issues

1. **GN 1993 type II equations not transcribed** — no flux law, no (4.15) text. sec. 4.5 cannot be signed off until they are.
2. **GN 1992 type III equations not transcribed** — (3.19)–(3.20) and the small-conductivity limit (4.10) still pending.
3. **GN 1991 not read** (scanned). The "all three types originate here" statement is relayed only.
4. **Moore & Gibson 1960 not opened**; Thomson/Thompson 1972 remains **unfound** — do not cite it on the strength of F14 alone.
5. **Tzou 1995 not opened by me**; the facts row asserts identity and role only and says so in both `status` and `read_level`. Its equation numbers are still unknown, so the manuscript's DPL equation cannot yet be checked against print.
6. **The manuscript still has to be changed, and I cannot do it** (no `.tex` here): sec. 4.5/4.6 citation years, sec. 4.7 key `Tzou1997`, sec. 4.10 + Table 1 Moore–Gibson wording, Table 12-A cells. These are reports, not fixes.
7. **Existing incorrect string inside EQ-165's note** (`−k^*\x07lpha_{,i}`, an escaped `\a`) is a pre-existing encoding defect, left untouched in this batch to avoid reflowing an already-verified row; it should be fixed once, globally.
