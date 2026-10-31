# P3_evidence_claims_C — blocked claims re-checked against the paper now in the library

Same format as `P3_evidence_claims_B` (identical 13-column header, at most 40 rows per
batch). Each row takes one `claim_register.csv` row whose status was *open: source not
available to verifier* and gives it a verdict from the source itself:

`SUPPORTED` / `PARTLY SUPPORTED` / `NOT SUPPORTED` / `SOURCE NOT AVAILABLE`,
always with `source_page_or_equation` pointing at a page (and equation, theorem or
section) that was actually read.

## Scope actually available

`missing_sources_priority.csv` ranks 141 sources by the number of claims they block. Of
those, **only three** correspond to a file in the unzipped library folder:

| rank | key | blocked claim | result |
|---|---|---|---|
| 14 | `Quintanilla2003DPL` | CR003 | **PARTLY SUPPORTED** — CC-0001 |
| 23 | `Quintanilla2008` | CR019 | **SOURCE NOT AVAILABLE** — CC-0002 (the file of that name is the 2008a paper) |
| 24 | `Quintanilla2008a` | CR020 | **SUPPORTED** — CC-0003 |

No other blocked claim in the register cites a paper that the folder supplies, so
`claim_check_C_batch_001.csv` is the whole of what can be decided today. Batches 002+
are **not** written, because writing them would mean inventing evidence: the papers that
the other 138 priority sources need are inside the two archives that are still zipped
(52 MB and 62 MB, above the 25 MB per-file read limit) and are not readable.

## What changed in the paper's favour, and what did not

* **CR003 (CC-0001)** is the single most load-bearing attribution in the manuscript, and
  it now rests on the page: Quintanilla (2003) keeps terms *to second order in τ_q and
  first order in τ_γ* (p. 714, Eq. (4)) — variant (ii), as the manuscript says — and
  proves exponential stability for τ_γ > τ_q/2 (p. 716, Eq. (11)) with instability for
  τ_γ < τ_q/2. The verdict is nevertheless **PARTLY SUPPORTED**, not SUPPORTED, because
  the source proves the *strict* inequality and never treats τ_γ = τ_q/2, whereas the
  manuscript writes τ_T ≥ τ_q/2. The sentence needs either `>` or an explicit "commonly
  quoted, not proved at equality" qualifier.
* **CR020 (CC-0003)** is supported: the abstract of Quintanilla and Racke (p. 24) states
  that conditions on the material parameters are obtained that guarantee exponential
  stability, with instability for suitable domains when they fail.
* **CR019 (CC-0002)** stays blocked. The library file called `quintanilla2008.pdf` is the
  2008a paper; the Applicable Analysis paper on end effects is still missing and must not
  be replaced by the 2008a file.

## Caution raised while doing this

`CR001` is marked *supported* at level V2 and cites `Tzou1995`, but the only library file
under the name `tzou1995.pdf` is the *other* 1995 Tzou paper (*Experimental support for the
lagging behavior in heat propagation*, J. Thermophys. Heat Transfer 9(4)) and not
*"A unified field approach for heat conduction from macro- to micro-scales"*. The register
verdict is left untouched here (it was reached from a different copy), but if the standing
check is repeated, that row must be re-read from the correct paper.

## Files

| file | contents |
|---|---|
| `claim_check_C_batch_001.csv` | 3 rows: CC-0001, CC-0002, CC-0003 |
| `check_claim_check_C.py` | validator; prints `PASS ...` and exits 0 |

Run: `python3 check_claim_check_C.py` →
`PASS all checks (batches=1, rows=3, PARTLY SUPPORTED=1, SOURCE NOT AVAILABLE=1, SUPPORTED=1)`
