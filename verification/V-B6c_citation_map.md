# V-B6c — Citation map (claim → proposed primary citations)

| field | content |
|---|---|
| **Task** | B6c: an appendix-style deliverable mapping manuscript claims to the best available citations in `LITERATURE_BASE.csv`, with the read level of each and a risk rating. |
| **Deliverable** | `verification/CITATION_MAP.csv` — 17 rows, columns `claim_id, section, claim_short, proposed_citations, read_level, risk`. |
| **Result** | 17 claims mapped, 44 distinct citation keys proposed, every key machine-verified to resolve in `literature_base.bib`. Three rows are rated HIGH risk: the claims for which **no record in the 428-record base may be able to support the claim as written**. |
| **Confidence** | **HIGH** that the mapping is internally consistent (keys resolve, sections are correct, claims are quoted from the ledgers). **LOW** on whether each proposed citation actually supports its claim — see the read-level column, which is "metadata only" or "abstract only" for every row. |
| **NOT verified** | That any proposed citation's text contains the result the manuscript needs. This map is a reading list with priorities, not a citation audit. |

## 1. How to read the risk column

* **LOW** — the claim is standard and at least two independent records in the base are on point. A
  human reading two of the proposed papers will be able to close the claim.
* **MEDIUM** — the claim is specific enough that the papers must be checked equation by equation,
  and the base contains the right *kind* of paper but not necessarily the right *statement*.
* **HIGH** — I could not identify, inside the 428-record base, a record that carries the needed
  statement. Either the manuscript's claim is wrong, or the base must grow before the claim can be
  sourced. **These are the rows the authors should look at first.**

## 2. The three HIGH-risk rows, spelled out

**CL-006 / W1 (Green–Lindsay energy equation).** The base has the GL paper and the two
Green–Naghdi postulates papers, but no record that prints the GL energy balance in a form I could
compare against the manuscript's eq. (4.9). Since V-B4 found that equation wrong, the citation
cannot be "fixed" by pointing at a paper; the equation has to be re-derived and *then* sourced.

**CL-015 / item 6 (attribution of a closed energy-balance identity).** The manuscript attributes a
conservation identity to specific papers. `V-B4` showed the identity does not close automatically.
Proposing `Anon2003Reflection`, `Barak2023Behavior` and `Racke2002Thermoelasticity` is the right
move *if* the identity is true; if it is not, citing them would propagate the error. The risk is
not "wrong citation" but "citation used to launder an unproven identity".

**CL-018 / item 11 (isothermal vs adiabatic Lamé modulus in `c_p`).** This is a standard correction
and yet the base cannot supply it: not one of the 428 records prints both moduli side by side. The
manuscript needs a textbook (Achenbach or Nowacki — both in the reference list, both DOI-less) or a
new primary source. **This is the clearest case in the whole review where a metadata-only strategy
fails**: the claim is easy, and the base still cannot source it.

## 3. Where the base is strong enough to close a claim outright

* **CL-024 (DPL well-posedness and truncation order)** — four sources that disagree informatively:
  Quintanilla 2002 (exponential stability for a parameter range), Rukolaine 2014 (115 cites,
  unphysical effects), Kovács & Ván 2018 (thermodynamic consistency), Chiriţă et al. 2017 (second
  route to the same constraints). This is what a well-posedness paragraph should look like, and the
  disagreement is the content.
* **CL-025 (MGT limits)** — Moore & Gibson 1960, a 2021 analytical solution, and two singular-limit
  theorems (M3AS 2019; *J. Evol. Equ.* 2021). The one family in the review where a rigorous
  statement is already available in the literature.
* **CL-026 (second sound was measured)** — the four real anchors that replace the fabricated
  `Guyer1990`: Guyer & Krumhansl 1964, Chester 1963, the NaF-experiment re-analysis (2018), and the
  2023 graphene observation. This row is the direct repair of the B5 defect.

## 4. Structural problem the map exposes

The read-level column is "metadata only" or "abstract only" for **all 17 rows**. That is not a
cautious hedge; it is the state of the evidence base. The review therefore cannot yet claim that any
core claim is PRIMARY-SOURCE-CHECKED in the sense the blueprint's R2/R3 gates require, and the
`risk` column is doing the work that the read-level column should be doing.

**308 of 428 bib keys are `Anon…` placeholders** because the author field is empty (see
`V-B6b_holes_and_citations.md` §5). Every key proposed here resolves *today*, but will change when
`--enrich` finally runs. Any manuscript built on these keys before then will have to be re-keyed.

## 5. Checks done

1. All 44 distinct keys machine-checked against `literature_base.bib` — all resolve. One earlier
   error (`LIT-0010 (Chester1963)`) was caught by this check and replaced by `Chester1963Second`.
2. Section column cross-checked against the labels in the read commit (`sec04` → s.4.x, `sec09` →
   s.9.x, `appA`, `T6`).
3. Claim ids cross-checked against `CLAIM_LEDGER.csv` and `V-B4_summary.md` item numbering; no
   invented claim ids.
4. Risk ratings assigned by asking, for each row, whether the base contains a record that could
   plausibly carry the statement — and marking HIGH when the answer was no.
