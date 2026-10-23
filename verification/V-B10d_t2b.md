# V-B10d_t2b — Tier-2 batch T2-B (9 files: imperfect boundaries, flexo/piezo interfaces, one misfiled paper)

**Task.** Tier-2 batch T2-B per `verification/DRIVE_PRIORITY.md` §14: the imperfect-boundary pair, the two flexo papers, the nonlocal-interface paper, and the two `piezo` pairs. Same deliverables as T2-A: one `FULLTEXT_FACTS.csv` row per file, printed energy-ratio definition, printed interface-condition form, identity versus bound versus approximation, and section placement.

**Method.** `origin` fetched (no change; `claude/control` at `6933a50`). Nine files downloaded by id, md5 recorded, text extracted under `/tmp/gd/t2b`. Title page → identity; then pattern searches for *energy ratio*, *unity*, *conservation*, *interaction energy*, *stiffness*; then the surrounding equation windows read. DOIs read off the printed pages and deduplicated against the 485-row base before appending.

**Result.**

**The unity story has a third category, and it is the important one: printed BOUNDS.**

* **DRV-0090** (B. Singh & G. Gupta, flexoelectric free boundary) states that the **sum of the reflected energy ratios is less than or equal to unity at each incident angle**, and aligns that with Qi (2019).
* **DRV-0157** (De, Sarkar et al., *J. Heat Transfer* 2020) prints the same kind of bound — the modulus of the sum of the three energy ratios ≤ 1 — **and gives the reason**: surface waves are not involved in energy conservation, and the thermal and interaction contributions are negligibly small in that example but must be included when they are comparable.

That explanation is the missing link for the whole §9.7/§10.5 discussion. The literature contains three distinct printed statements, and they are not in conflict: an **identity** when every channel including the interaction energy is retained (DRV-0040 (6.14), DRV-0179 (80), DRV-0043 (6.9), DRV-0033 (7.6)); an **approximate unity** where the sum is evaluated numerically (DRV-0099, the own-group cluster); and a **bound** where a channel is deliberately dropped (DRV-0090, DRV-0157). The manuscript should say exactly this instead of choosing one phrasing — and DRV-0157 supplies the printed justification.

**Two papers that were expected to be energy-partition papers are not.**

* **DRV-0167** is filed as `reflection.pdf` in the `Reflection+piezo` folder, but it is **Biswas 2020, *Acta Mechanica*, "Surface waves in piezothermoelastic transversely isotropic layer lying over … half-space"** — a Rayleigh-wave study. It computes phase velocity, attenuation and specific loss, and no energy ratios. It is still useful: its eq (3) prints the **GN type-III** heat conduction equation with both the `K_ij ∂(T,ij)/∂t` and `K*_ij T,ij` groups, which is the equation-backed discriminator the B03 batch asked for.
* **DRV-0168** (`MMMS-03-2015-0012.pdf`) contains **only the Emerald article-information cover page** — about 2.4 thousand characters, no body. It is recorded as `UNVERIFIED (cover page only)`, and nothing whatsoever may be cited from it. This is a library defect, not a reading failure, and a full text is needed if the paper matters.

**Imperfect bonding is a four-parameter family, not a single "stiffness".** DRV-0094 (R. Kumar & N. Sharma 2008) prints **four** independent interface parameters — normal force stiffness, transverse force stiffness, transverse couple stiffness, thermal contact conductance — with perfect bonding as the infinite-stiffness limit; DRV-0158 (2009) is a second, independent stiffness-parameter study. Combined with DRV-0018's finite-stiffness fluid/solid interface from T2-A, §9.3/§9.8 can be written with printed parameter names rather than a hand-wave.

**Remaining files.** DRV-0093 (piezomagnetic + flexomagnetic) and DRV-0123 (graded piezoelectric microstructures) report dispersion and reflection with **no energy ratios**; DRV-0095 is a six-page conference paper on the micropolar imperfect interface, recorded at scope level only.

**Evidence / sources.** Nine files, Drive ids in `FULLTEXT_FACTS.csv`, read 2026-10-22, deleted from `/tmp` afterwards. DOIs: `10.1080/15397734.2020.1853566`, `10.1007/s00707-024-03940-z`, `10.1016/j.tafmec.2008.07.010`, `10.4028/www.scientific.net/AMR.803.419`, `10.1016/j.euromechsol.2020.103955`, `10.1115/1.4046924`, `10.12989/sem.2009.31.2.117`, `10.1007/s00707-020-02848-8`, `10.1108/MMMS-03-2015-0012`.

**Checks done.**
- Nine md5s distinct; no duplicate within the batch.
- Header equality asserted; `FULLTEXT_FACTS.csv` 79 → **88 rows**, 88 unique `inv_id`.
- DOI dedup against 485 rows: **four hits** (LIT-0352, LIT-0168, LIT-0268, LIT-0271), all upgraded in place with authors filled where blank and `read_level` raised; **five new rows** (LIT-0486–LIT-0490).
- Key-collision caught and fixed: the new Biswas row would have reused the key `Biswas2020ActaMech`, which belongs to the DRV-0106 row (a different Biswas paper, porous nonlocal GN-III). Renamed to `Biswas2020PTlayer`; the duplication would otherwise have silently merged two papers in any key-based lookup.
- Negative results obtained by full-text search, not sampling: no energy ratios in DRV-0093, DRV-0095, DRV-0123, DRV-0167, DRV-0158, DRV-0094.
- `/tmp/gd` removed; repository contains no paper text.

**Confidence.** HIGH for the two bound statements — both are quoted from the papers' own sentences about conservation, with the reason printed in DRV-0157. HIGH for the DRV-0168 diagnosis (the file's own content is only the cover page; the character count is decisive). HIGH for the DRV-0167 misfiling (the printed title and abstract are unambiguous). MEDIUM for DRV-0094/DRV-0158's parameter sets: the keyword lists and abstracts name the four parameters, but the equations were not transcribed.

**NOT verified / open issues.**
- Equation numbers were **not** transcribed for DRV-0090, DRV-0094, DRV-0095, DRV-0093, DRV-0123, DRV-0157, DRV-0158. Each row says so; nothing finer than a section-level statement may rest on them.
- DRV-0168 needs a re-download before use.
- DRV-0095 is a conference paper; its results should not be cited as peer-reviewed primary evidence.
- Citation counts not fetched; `citations` blank for the five new rows.
