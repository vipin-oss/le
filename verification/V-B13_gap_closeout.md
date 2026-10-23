# V-B13 — Closing GAP-03/04/05/08 from the supervisor's findings, and the request list for the rest

| field | content |
|---|---|
| **Task** | (1) Read `control/FULLTEXT_FINDINGS_01.md` and `02.md` and move whatever they establish into `LITERATURE_BASE.csv` and `FULLTEXT_FACTS.csv`, tagged **SECONDARY-SOURCE**, for GAP-03 (GL 1972), GAP-04 (GN 1992), GAP-05 (GN 1993) and GAP-08 (Moore & Gibson 1960); anything the findings do not contain stays UNVERIFIED. (2) Build `PDF_REQUEST_LIST_2.md` for the remaining eleven gaps with Crossref-verified DOIs. |
| **Deliverable** | `FULLTEXT_FACTS.csv` 100 → **101** rows (`GreenLindsay1972`); four base rows re-tagged (`LIT-0003`, `LIT-0005`, `LIT-0430`, `LIT-0365`); four `REFERENCE_GAPS.csv` rows updated; **`PDF_REQUEST_LIST_2.md`** (11 rows). |
| **Method** | `git fetch --all`; read `control/FULLTEXT_FINDINGS_01.md` and `_02.md` at `origin/claude/control` @ `6933a50`. Nothing was added to the base that is not printed in those two files. DOIs in the request list were resolved live against the Crossref REST API and Unpaywall on 2026-10-22. |
| **Result** | **GAP-03 is closed at secondary level and it overturns a manuscript equation.** GAP-04 and GAP-08 gain a base record but no content; GAP-05 gains nothing and stays open. |
| **Confidence** | HIGH that the GL facts are transcribed faithfully from the findings (they are quoted, not paraphrased, and the equations are unambiguous). **MEDIUM** as *evidence*: the status is SECONDARY-SOURCE because I did not open the paper. HIGH on every DOI below (resolved, not remembered). |

## 1. What the findings actually contain

`FULLTEXT_FINDINGS_01.md` records nine papers opened by the supervisor, of which five were analysed: **GL 1972, LS 1967, Quintanilla & Racke 2006, Wang & Li 2011, Sinha & Elsibai 1997**. GN 1992, GN 1993, Guyer & Krumhansl 1964 and Moore & Gibson 1960 are listed as *opened but available for a later batch* — i.e. **no facts exist for them**, only bibliographic identity.

`FULLTEXT_FINDINGS_02.md` adds Roy Choudhuri 2007, Quintanilla 2002, Tzou 1995 (partial), Eringen 1983 (partial), the two Chandrasekharaiah reviews, GK 1966 and Mindlin 1974 (extracted, not analysed), and records **GN 1991 as a scanned PDF with no text layer, NOT READ**.

So of the four gaps I was asked to close, **only GAP-03 could actually be closed.** That is the whole finding of this file.

## 2. GAP-03 — GL 1972: what the paper prints, and why it matters

Recorded as `FULLTEXT_FACTS.GreenLindsay1972`, status `SECONDARY-SOURCE`, from F1:

* **Stress (4.11)** carries the relaxation: `t_ik = k_iklrs e_rs + a_ik(θ + α θ̇)`.
* **Flux is Fourier.** `q_i = −θ_0(b_i θ̇ + k_ij θ_,j)`; with a centre of symmetry `b_i = 0`. **GL has no flux relaxation.**
* **Energy (4.13)**, source-free: `k_ij θ_,ij − d θ̇ − h θ̈ + a_ij ė_ij = 0`. The temperature carries `(θ̇ + (h/d)θ̈)`, i.e. `τ_0 = h/d`, but **the strain-rate coupling `a_ij ė_ij` carries no relaxation time**.
* **Ordering (4.9)/(4.14):** `dα − h ≥ 0`, i.e. `τ_1 ≥ τ_0`; **(4.16)** adds `d, h, α > 0`. The ordering is therefore *printed and sourced*, not "commonly imposed".

**The consequence is a manuscript defect, and it is the same one B4 raised from the other direction.** The manuscript's eq. (4.9) writes `βT₀(u̇_i,i + τ_0 ü_i,i)` — a uniform LS-style operator on the strain-rate term. LS 1967 eq. (23) does carry `τ_0` on `ë_kk` (already recorded as `LordShulman1967`, and F2 independently confirms that existing row slot-for-slot), whereas GL (4.13) does not. **The manuscript equation is the LS energy balance glued to the GL stress law** — a hybrid that exists in the literature but is not Green–Lindsay 1972. Three things follow, and all three are consequences the paper owner must act on, not me:

1. §4.4 must print (4.13) as printed and, beside it, GL's Fourier flux law.
2. Any GL dispersion, secular equation or GL interface number computed from the manuscript coupling has to be recomputed.
3. The hybrid itself now needs a source of its own. F1 says it is "a later hybrid used in parts of the literature" but names no paper, so **the hybrid remains unsourced** — recorded as an open item, not filled in.

## 3. GAP-04/05/08 — the three that could not be closed

| gap | what the findings give | what is still missing |
|---|---|---|
| **GAP-04** GN 1992 | bibliographic identity and DOI `10.1080/01495739208946136`, *JTS* **15**(2), 253–264. The row already existed in the base as **LIT-0430** — no new row was needed; I re-tagged it rather than duplicating it. | **no equation, no statement.** The "opened but not analysed" status is recorded in the row. The GN II/III numbering conflict with `DRV-0185` is therefore **still open**: the findings do not settle which paper is which model. |
| **GAP-05** GN 1993 | nothing new; LIT-0005 keeps `metadata only`. | the `k*` term and the dissipation statement as printed. |
| **GAP-08** Moore & Gibson 1960 | identity and DOI `10.2514/8.8418`, *J. Aerospace Sci.* — already in the base as **LIT-0365**. | nothing read: §4.10 still cannot quote an MGT equation. |

Adding GN 1992 and Moore & Gibson to the base, as instructed, therefore turned out to be **already done**: both records exist (LIT-0430, LIT-0365). I verified this before writing and changed only `read_level` and `why`, so the base stays at **499** rather than gaining two duplicate rows. The alternative — appending them again — would have been an invisible duplicate.

## 4. Two cross-links the findings opened

* **F9 (Barak et al. 2023) bears directly on the manuscript's EQ-019.** The second-order term in the TPL flux law is `(τ_q²/2)` on the **flux-lag** side, while EQ-019 places a `(τ_ν/2)∂_t²` term on the **temperature-gradient** side and attributes it to Tzou 1997. FINDINGS_02 F7 marks that attribution `CONFLICT`.
* **And that is exactly the item I could not verify in `PDF_REQUEST_LIST_2.md` row 2:** Crossref has no 1997 record for Tzou's book and no 1997 Tzou paper on lagging conduction. The attribution cannot be checked until the 1997 text is in hand — and if the authors meant the 2014 Wiley edition, the equation numbering differs and the attribution has to be re-made against *that* edition.

## 5. Checks done

1. Both findings files read in full at the fetched `origin/claude/control`; commit hash recorded (`6933a50`).
2. Before adding anything to the base I checked whether a record already existed — the two instructed additions were already there, which is why the base did not grow.
3. `FULLTEXT_FACTS` key uniqueness asserted; one row added, no duplicates.
4. Every DOI in `PDF_REQUEST_LIST_2.md` resolved live this session; the five that do not resolve are printed as **NO DOI** rather than filled in with a plausible string.
5. OA status from Unpaywall, not from publisher page appearance.
6. Row widths asserted equal to header on all four CSVs touched.

## 6. NOT verified / open issues

* **GL 1972 has not been opened by me.** The equation numbers are the supervisor's; the primary-source check is one phone call away (p. 5 of the paper) and should be made before §4.4 is rewritten.
* GN 1992, GN 1993, Moore & Gibson 1960, GN 1991: **no content at all**. GN 1991 has no text layer at all per FINDINGS_02, so OCR is needed before anything can be said about it.
* The GL/LS hybrid used in the manuscript has no primary source yet.
* Five of the eleven requested items have **no DOI anywhere** (Cattaneo 1948, Vernotte 1958, Tzou 1997, Achenbach 1973, Nowacki 1975). For those, a stable identifier has to come from the library record, not from me.
* `Luchko2010` in the manuscript cannot be pinned to one record; two candidates verify and the request list says so.
