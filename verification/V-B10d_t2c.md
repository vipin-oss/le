# V-B10d_t2c — Tier-2 batch T2-C (8 files, the Mendeley / reference-transfer tail)

**Task.** Final tier-2 batch per `verification/DRIVE_PRIORITY.md` §14: the two `Mendeley` reflection papers (including the suspected duplicate pair), the `Used-in-P11` pair, the `R-Poonia-Sir` pre-proof, and the `Collected-from-My-Folders` cylindrical SH-wave paper. Deliverables as T2-A/T2-B.

**Method.** `origin` fetched (unchanged). Eight files downloaded by id; **two of them will not parse** (details below), which is itself a library finding. The six that do parse were extracted with `pypdf`, title page read, then pattern searches for the energy-ratio / unity / conservation / interaction / welded / imperfect vocabulary and reading of the surrounding equations. DOIs deduplicated against the 490-row base before appending.

**Result.**

**The equality claim is now printed by two independent groups, and the bound by two more. The manuscript can stop choosing and state the condition.** DRV-0223 (M. Kumar & X. Liu) prints an energy matrix at (30) — diagonal entries are the energy ratios, off-diagonals the interaction energies — and states at **(32)** that the total energy ratio equals unity. DRV-0181 (Sheokand, Kalkal & Deswal, *J. Ocean Eng. Sci.* 2021) states that the sum of the energy ratios is verified and **equals unity at each angle of incidence**, for a rotating, fibre-reinforced, orthotropic, TPL half-space. Against those, DRV-0090 and DRV-0157 (T2-B) print bounds. The resolution the manuscript should adopt: **equality when every channel including interaction energy is retained; a bound when a channel is dropped** — with DRV-0157 giving the printed reason.

**One paper prints the stiffness-to-welded degeneration explicitly, which none of the others does.** DRV-0146 (Kaur, Lata & Singh 2020) sets up the imperfect boundary between two transversely isotropic piezo-thermoelastic diffusive half-spaces with normal and transverse force stiffness and a thermal contact conductance, then prints the **welded contact as the limit in which those stiffnesses go to infinity**, giving the eight-equation system. That is exactly the degeneration §9.3 needs, and it is combined with a memory-dependent TPL law and a two-temperature description, so it also serves §11.3.

**Two of the eight files are unusable, and one of those may be a duplicate.**

* **DRV-0141** (`Kumar, Chawla - 2013 - Reflection and refractio.pdf`) is a **corrupt PDF**: `pypdf` reports "Incorrect startxref pointer" and "Invalid object in /Pages", and no page opens even in non-strict mode. Nothing is established beyond the file name, so the row is `UNREADABLE` and the paper is **not citable**.
* **DRV-0147** (`…refra(1).pdf`) is truncated — "Stream has ended unexpectedly" — so the DOI comparison that would confirm the duplicate could not be made. It is recorded as a **presumed** duplicate of DRV-0146 on the strength of the file name, identical authors and year, and a 1 % file-size difference consistent with two renderings. The row says "presumed", not "confirmed", and the duplicate is **not** counted as a second paper.

Both files also resisted three download attempts (the connector reported success while the file was intermittently absent from the workspace); the copies that did arrive are themselves damaged, so the defect is in the stored files. A re-download from the publisher is needed before either can be read.

**Other findings.** DRV-0224 (M. Kumar, X. Liu & Kalkal) prints open versus sealed surface-pore boundary conditions and an interaction-energy treatment — useful for §9.3 and §10.5. DRV-0341 (Kumawat & Vishwakarma 2023) is a second **cylindrical** imperfect-bond waveguide paper, so the manuscript can note that the imperfect-interface treatment recurs in cylindrical as well as planar geometry. DRV-0144 (R. Kumar, Sharma, Lata & Marin 2018) computes **no** energy ratios — amplitude ratios only — so it belongs to §9.6.

**Evidence / sources.** Eight files, Drive ids in `FULLTEXT_FACTS.csv`, read 2026-10-22, deleted from `/tmp` afterwards. DOIs: `10.12921/cmst.2016.0000069`, `10.1080/17455030.2020.1856451`, `10.1108/HFF-01-2022-0008`, `10.1108/HFF-04-2021-0279`, `10.1016/j.joes.2020.12.001`, `10.1016/j.apm.2023.06.034`; none for the two unreadable files.

**Checks done.**
- md5 computed as files arrived; the two Kaur files differ in size, so they are at least different byte streams — the duplicate judgement rests on name/authors/year, not on the hash, and the row says so.
- Parse attempts made in strict and non-strict mode on both damaged files before declaring them unreadable; the error strings are recorded.
- Header equality asserted; `FULLTEXT_FACTS.csv` 88 → **96 rows**, 96 unique `inv_id`.
- DOI dedup against 490 rows: **one hit** (LIT-0281, authors filled, upgraded); **five new rows** (LIT-0491–LIT-0495). No row added for the two unreadable files beyond the facts entries.
- Negative results by full-text search: no energy ratios in DRV-0144, DRV-0341.
- `/tmp/gd` removed. Tier-2 totals: 26 files, 96 facts rows overall, 495 base rows.

**Confidence.** HIGH for DRV-0223's and DRV-0181's printed equality statements (both quoted from the papers' own conservation sentences). HIGH that DRV-0141 and DRV-0147 are unusable — the parser errors are decisive and reproduce. MEDIUM for the DRV-0147 duplicate judgement, which is name-based and explicitly labelled presumed. MEDIUM for DRV-0146's energy-ratio closure status, where the ratios are printed but no unity sentence was located.

**NOT verified / open issues.**
- DRV-0141 and DRV-0147: identity and content **UNVERIFIED**; both need fresh copies. Until then the library contains two unreadable entries in tier 2.
- DRV-0146: whether a closure/unity statement is printed remains open; the row says UNVERIFIED rather than inferring from the presence of energy ratios.
- Equation numbers are transcribed only for DRV-0223 ((30), (32)) and DRV-0146 ((75), (77)); the other rows are section-level.
- DRV-0181 was read from a **journal pre-proof**; page numbers will change on publication and the bibliographic record must be refreshed before the reference list is frozen.
- Citation counts not fetched; `citations` blank for the five new rows.

---

**Correction added 2026-10-22, during T3-1.** The paragraph above says the defect is "in the stored files". A controlled re-download of DRV-0141 (and of the newly failing DRV-0056 in tier 3) returned files that are **byte-identical to the first copies** (same size, same md5) and truncated in the same place, so the transfer is reproducible and not a one-off glitch. What cannot be distinguished from here is whether the stored objects are themselves truncated or whether the download path truncates them deterministically. The corrected statement: **the copies that reach this workspace are reproducibly truncated; the site of the damage is undetermined.** The reading verdict — UNREADABLE, not citable, not guessed — is unchanged. DRV-0056 fails the same way (`root of pages tree has no /Kids array`).
