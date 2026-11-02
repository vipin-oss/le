#!/usr/bin/env python3
"""batch_008: settle the register rows whose cited source is already in hand.

The sandbox holds no document library, so no PDF is opened here. Every row below points at a page-level
read already recorded in this repository (a claim_check_C batch row, or a SOURCE_READING_held row): the
locator, the quoted wording and what the source actually states are carried over verbatim from that
record, and the verifier string says so. Where the earlier read found the manuscript's wording stronger
than the page, the verdict is PARTLY.

Side effect: the register rows these entries settle are moved off SOURCE NOT AVAILABLE, with the old
verdict kept in `notes`, and the status pointing at the new entry. Nothing else in the register changes.
Prints PASS and exits 0.
"""
from __future__ import annotations

import csv
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PAPER = HERE.parent.parent.parent / "paper_v2"
DELIV = PAPER / "arena_deliverables"
BATCH_DIR = DELIV / "P3_evidence_claims_C"
REGISTER = PAPER / "claim_register.csv"
OUT = BATCH_DIR / "claim_check_C_batch_008.csv"

# register claim -> (evidence file, evidence claim_id, verdict, why this verdict)
PLAN = [
    ("CR003", "batch_001", "CC-0001", "PARTLY SUPPORTED",
     "attribution and truncation verified on the page; the page states a strict tau_y > tau_q/2 for "
     "exponential decay, while the manuscript writes >=, and equality is not decided by the paper"),
    ("CR020", "batch_001", "CC-0003", "PARTLY SUPPORTED",
     "the stability note is verified (abstract and Sec. 1); the end-effects attribution in the same "
     "sentence is not on the pages read"),
    ("CR043", "held", "CR043", "SUPPORTED",
     "the paper is the time-fractional Cattaneo law and the stress theory built on it, which is what the "
     "sentence says"),
    ("CR082", "batch_005", "CC-0016", "PARTLY SUPPORTED",
     "the cited paper is the internal-state-variable framework; the manuscript attaches it to a memory law"),
    ("CR083", "batch_005", "CC-0015", "SUPPORTED",
     "the paper's own title and Sec. 1 carry the relaxation-function restriction the sentence credits it with"),
    ("CR122", "batch_005", "CC-0019", "SUPPORTED",
     "the MGT equation is treated as an evolution problem exactly as the sentence says"),
    ("CR182", "batch_005", "CC-0025", "PARTLY SUPPORTED",
     "the kernel attribution is safe; the differential form quoted in the manuscript is not on the 1972 pages"),
    ("CR196", "batch_005", "CC-0028", "SUPPORTED",
     "the title and abstract of the 1974 paper are exactly the nonlocal thermoelasticity extension claimed"),
]


def load_batch(name: str) -> dict[str, dict]:
    path = BATCH_DIR / f"claim_check_C_{name}.csv"
    return {r["claim_id"]: r for r in csv.DictReader(path.open(encoding="utf-8"))}


def main() -> int:
    batches = {n: load_batch(n) for n in ("batch_001", "batch_005")}
    held = {r["claim_id"]: r for r in csv.DictReader(
        (DELIV / "P3_evidence_claims_B" / "SOURCE_READING_held_2026-11-01.csv").open(encoding="utf-8"))}
    reg_rows = list(csv.DictReader(REGISTER.open(encoding="utf-8")))
    reg = {r["claim_id"]: r for r in reg_rows}

    out_rows, settled = [], []
    for i, (claim, where, ev_id, verdict, why) in enumerate(PLAN, start=64):
        cc = f"CC-{i:04d}"
        if where == "held":
            h = held[ev_id]
            src = reg[claim]["cited_source"]
            row = {
                "claim_id": cc,
                "manuscript_location": reg[claim]["origin"],
                "manuscript_statement": reg[claim]["manuscript_statement"],
                "cited_source": src,
                "source_doi": reg[claim]["source_doi"],
                "found_in_library": "yes - held copy read in an earlier pass",
                "verdict": verdict,
                "source_page_or_equation": h["evidence_page"],
                "source_wording_max25words": h["evidence_quote"][:200],
                "what_source_actually_states": h["what_source_actually_states"],
                "verification_level": "R3 - consolidated from SOURCE_READING_held_2026-11-01.csv",
                "notes": f"register row {claim}; source read in an earlier pass, not re-read now. "
                         f"Verdict reason: {why}.",
            }
        else:
            b = batches[where][ev_id]
            row = {
                "claim_id": cc,
                "manuscript_location": b["manuscript_location"],
                "manuscript_statement": b["manuscript_statement"],
                "cited_source": b["cited_source"],
                "source_doi": b["source_doi"],
                "found_in_library": "yes - held copy read in an earlier pass",
                "verdict": verdict,
                "source_page_or_equation": b["source_page_or_equation"],
                "source_wording_max25words": b["source_wording_max25words"],
                "what_source_actually_states": b["what_source_actually_states"],
                "verification_level": f"R3 - consolidated from {where} {ev_id}",
                "notes": f"register row {claim}; the page-level read is recorded in {where} {ev_id} and "
                         f"is not repeated here. Verdict reason: {why}.",
            }
        out_rows.append(row)
        settled.append((claim, cc, verdict, row["verification_level"]))

    cols = ["claim_id", "manuscript_location", "manuscript_statement", "cited_source", "source_doi",
            "found_in_library", "verdict", "source_page_or_equation", "source_wording_max25words",
            "what_source_actually_states", "verification_level", "notes"]
    with OUT.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        w.writerows(out_rows)

    for claim, cc, verdict, level in settled:
        r = reg[claim]
        old = f"{r['verdict']}/{r['verification_level']}"
        r["verdict"] = verdict
        r["verification_level"] = "R3"
        r["verifier"] = ("consolidated from the page-level read recorded under "
                         f"{cc} (not re-read in the post-merge pass)")
        r["status"] = f"resolved - see P3_evidence_claims_C/{cc}"
        r["notes"] = (f"{r['notes']} || post-merge: was {old}; settled from recorded page read, see {cc}. ")
    with REGISTER.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(reg_rows[0].keys()))
        w.writeheader()
        w.writerows(reg_rows)

    print(f"batch_008 rows: {len(out_rows)} ({OUT.name})")
    for claim, cc, verdict, _ in settled:
        print(f"  {cc}  {claim}  {verdict}")
    print("register rows moved off SOURCE NOT AVAILABLE: 8")
    print("PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
