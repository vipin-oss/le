# V-B10d_t2a — Tier-2 batch T2-A (9 files: 7 own papers + 2 from the `Energy` folder)

**Task.** Tier-2 batch T2-A per `verification/DRIVE_PRIORITY.md` §14: read the nine interface/energy-partition files assigned to this batch, one `FULLTEXT_FACTS.csv` row each, record the printed energy-ratio definition, decide **printed identity versus approximate/numerical unity**, and record the interface-condition form where one is printed.

**Method.** Fetched `origin` first (`claude/control` at `6933a50`, unchanged; branch `arena/04fdf32e-le` at `f6c3142`, clean). Nine files downloaded by Drive id, md5-recorded, moved to `/tmp/gd/t2a`, text extracted with `pypdf` 6.21.2. Title page → identity and metadata; then a full-text pattern search for the energy-ratio definition, the words unity / conservation / interaction, and the interface-condition block; then the surrounding equation window read. DOIs taken from the printed article pages (or recorded as absent), then deduplicated against all 477 existing `LITERATURE_BASE` rows.

**Result.**

**Three printed closure statements are now on record, and the manuscript's §10.5 rests on three equations, not one.** DRV-0043 prints an **exact identity at (6.9)** — four transmitted ratios plus an interaction energy `Eint` defined at (6.7)–(6.8) as the sum over unequal pairs, plus the reflected P and S ratios, equal to one. DRV-0033 prints a conservation statement at **(7.6)** with its own interaction term at (7.5). Together with DRV-0040 eq (6.14) and DRV-0179 eq (80) found earlier, that is **four** printed identities, three of them in this batch's own-group set. §10.5 should cite the identities and say which is which.

**But the approximate-unity phrasing is not an own-group habit.** DRV-0099 (R. Kumar & P. Sharma, *Appl. Math. Comput.* **358**, 194–203, 2019 — an independent group at Kurukshetra) states in its abstract that the sum of the energy ratios is *approximately* unity and offers that as verification of conservation. So the split the manuscript must make is **symbolic identity versus numerical observation**, cutting across groups — not "our papers prove it, theirs approximate it".

**Four of the nine files compute no energy ratios at all.** DRV-0018 (imperfect fluid/double-porous interface, stiffness 5 / 10 / perfect bond) reports phase velocity and specific loss; DRV-0023 (circumferential SH waves in a layered piezoelectric cylinder) reports dispersion; DRV-0052 (two liquid-saturated porous half-spaces) prints interface conditions at (5.1.1) only; DRV-0053 (viscothermoelastic slab between elastic media) reports waveguide modes. All four are §9.3/§9.8 material and **must not be cited in §9.7** — which is a correction to the tier assignment, since tier 2 was defined as "interface / energy partition" and these four are interface-only.

**Interface-condition and model detail worth carrying into the manuscript.**

* **DRV-0018** is the cleanest printed treatment of the finite-stiffness imperfect interface (values 5, 10, and the perfect-bond limit) — the right anchor for §9.3/§9.8's description of imperfect bonding.
* **DRV-0043 Case 2** and **DRV-0033 Case 1** both print, in compact form, how the hyperbolic, classical and single-temperature models differ only by parameter choice (`t*11 = a*11/ω²` versus `a*11` versus `0`). That is the discrimination §11.3 needs, and it is printed rather than inferred.
* **DRV-0044** couples three physics (piezoelectric, moisture, thermal) and gets five reflected modes — the widest coupling in the tier-2 set, and the natural citation for "mode count grows with field count".
* **DRV-0097** (A. K. Singh & Guha, independent group, free surface) reports the reflected energy ratio reaching 1 as a **computed curve**, not a symbolic identity; useful as independent corroboration of the free-surface saturation, and it must be described that way.

**Evidence / sources.** Nine files, Drive ids in `FULLTEXT_FACTS.csv` (`drive_id` column), read 2026-10-22, deleted from `/tmp` at the end of the batch. Metadata from the printed title pages; DOIs `10.47974/JIOS-1608`, `10.1016/j.compstruct.2025.118997`, `10.1088/1402-4896/ad1972`, `10.1108/HFF-04-2022-0259`, `10.1108/HFF-04-2023-0208`, `10.1080/15376494.2020.1736697`, `10.1016/j.amc.2019.04.020`. DRV-0052 and DRV-0053 print **no DOI** and are recorded as DOI-less. Section anchors: `phase5/master` @ `84a8dfa`.

**Checks done.**
- Nine md5s distinct; no duplicate inside the batch.
- Header equality asserted; `FULLTEXT_FACTS.csv` 70 → **79 rows**, 79 unique `inv_id`.
- DOI dedup against 477 base rows: **one hit** (LIT-0046 = DRV-0043, upgraded in place); **8 new rows** (LIT-0478–LIT-0485), two of them DOI-less by fact, not by omission.
- `make_bibtex.py` re-run: see commit output for the record count and the duplicate-DOI count.
- Negative results are stated as negatives and obtained by full-text search, not by sampling: "no energy ratios" in DRV-0018, 0023, 0052, 0053.
- No paper text, figure or long quotation written into the repository; `/tmp/gd` removed.
- `DRIVE_PRIORITY.csv`: `read_level` filled for the nine rows; `proposed_section` corrected for the four interface-only papers.

**Confidence.** HIGH for the four printed identities and their equation numbers: each was read in the extracted text with its surrounding definition. HIGH for the "no energy ratios" set (full-text negative evidence, consistent with what each paper's own results section reports). MEDIUM for DRV-0044, where the ratios and interaction energy are legible but no closure equation was recovered. MEDIUM for DRV-0033's coefficient-level detail — the text layer is heavily garbled, so numbers are certain and symbols are not. UNVERIFIED where the row says so.

**NOT verified / open issues.**
- DRV-0033 and DRV-0044: text-layer garbling means individual coefficients are **not** transcribed; anything requiring a coefficient must go back to a rendered page.
- DRV-0018, 0023, 0052, 0053: **scope-level rows only.** The interface model is identified from abstract and results text, but no equation was transcribed, so the rows support "this paper does X and does not compute Y" and nothing finer.
- Whether DRV-0044 prints a closure equation remains open (no equation number recovered); the row says UNVERIFIED rather than guessing.
- Two DOI-less own-group entries (DRV-0052, DRV-0053) sit in venues that are not indexed mechanics journals; both are flagged for the citation plan. Nothing about their content is asserted beyond the scope line.
- Citation counts not fetched; `citations` left blank for the eight new rows rather than guessed.
