# Phase 5 — Literature audit and introduction repositioning

Scope: verify what the manuscript cites and what it cites it for; add only what can be verified; reposition the
introduction so that each framework claim sits on a primary source rather than on a review. 54 references went
in, 55 come out, and one classical pair stays uncited for a stated reason.

## 1. Reference verification

Every entry in `01_Literature/REFERENCES_VERIFIED.json` carries a verification level. Before this phase: 23
entries metadata-verified against Crossref on 2026-10-01 and 31 on 2026-10-02 — metadata-verified means the
title, authors, journal, volume, pages and year returned by Crossref match the entry as printed. It does not
mean the paper was read. The two exceptions, unchanged and still the only ones, are Klimm et al. (open access,
read in the first session) and Adachi et al. (the values checked against the open-access version). The literature
README says the same; nothing in this phase upgraded that claim, and no entry's level was softened either.

The Crossref API is reachable from here through the agent's fetch path (not through the shell), so the
verification in this phase was done live against `api.crossref.org`, and the queries plus their raw outcomes are
in `SEARCH_NOTES.md`.

## 2. What the audit found, and what was done about it

1. **The passivity restriction was carried by reviews only (A13).** The claim "the Cattaneo–Vernotte law meets
   this for every τ > 0 because it is a positive-real (passive) kernel" is a statement about a theorem in the
   general theory of heat conduction with finite wave speeds. Added, DOI-verified: Gurtin & Pipkin, *Arch. Ration.
   Mech. Anal.* 31(2), 113–126 (1968), doi 10.1007/BF00281373 → reference [55]. The sentence now says what that
   source states (the restriction is for a memory kernel) and what it does not (τ > 0 is its instance here, not
   its subject). The companion's parallel sentence points to the same reference, so the two documents have the
   same support for the same claim.
2. **The Richardson extrapolation was flagged as uncited (B19).** Checked in the generated text: it is cited, to
   Richardson and Gaunt [52]. No addition. A second verified candidate (Ferziger & Peri ć) was found and left out
   deliberately — adding a textbook to a statement that already carries its methodological citation is padding.
3. **Claim ↔ citation matrix (B21).** `verification/lit_B_claims_matrix.py` extracts every citation instance
   with its sentence, joins it to the reference's verification level, and flags strong-verb assertions resting on
   a metadata-only record in the framing and theory sections. Result: 139 citation instances, **55 of 55 entries
   cited (no orphan), 0 flagged**. So the introduction and model sections do not currently over-claim against
   their sources; the numbers are in `verification/claims_matrix.json`.
4. **The classical papers named in the body could not be verified (A13, stays open).** For Cattaneo 1948, the
   nearest records are either unrelated or a 2011 Springer chapter carrying the title on a single page — citing
   that as the 1948 paper would misdate the source; secondary references disagree on venue and pagination
   (Treccani: Modena, *Atti del Seminario matematico e fisico*, III [1948–49]; elsewhere Milan *Rendiconti*,
   29–36). For Vernotte 1958 there is no Crossref record at all. Both therefore remain **named, not cited**, and
   the item is recorded as open for the authors with the exact follow-up spelled out (`SEARCH_NOTES.md`). The
   project rule — no reference without verification, never invent a DOI — was kept over the temptation to close
   the item cosmetically.

## 3. Introduction repositioning

The introduction needed one structural change rather than a rewrite: its framework sentence grouped the
memory-kernel literature through the reviews ([13], [14], [23]) and the primary theory was absent. Section 1.2 now
reads "…the Lord–Shulman theory with one relaxation time [11] and its extension to anisotropic media with a
uniqueness theorem [12]; the general theory of heat conduction with a memory kernel and finite wave speeds is due
to Gurtin and Pipkin [55]; dual-phase-lag formulations [13]…", which puts the model actually used in Section 2 on
a primary source.

What was deliberately **not** touched: the gap statement in Section 1.1 stays as verified in earlier phases —
"Within the bounded literature search described in the data package we found no study that combines … (this is a
statement about our search, not a claim of priority)". No "first", no "novel", no "no previous study exists"; the
scope sentence in 1.3 ("verified continuum parametric study … not compared with experiments, which are not
available") is unchanged, since the audit found no citation in the list that would license saying more.

## 4. Consequences for the deliverables

Reference count 55 in both the reference list and `.bib`; structure otherwise unchanged (9 sections, 41
subsections, 84 equations, 8 figures, 11 tables; abstract 249/250; companion 11/37/29/9, ≈5268 words). All
document gates green after the rebuild. Freeze moved additively to `submission_2026_10_03d` (27 files) and both
documents quote its digest as it stands on disk — the Phase 4 ordering rule (freeze regenerated before the last
build) was followed, and the guard in `build_calculations.py` aborted the first attempt when the manifest lagged
the edited builders, which is the mechanism working as designed.

## 5. What later phases inherit

- **P5-1 (open, authors):** pagination for the two classical papers, obtainable from a library catalogue, after
  which [56]/[57] can be appended and cited at the three mentions.
- **Phase 6 (restructuring):** the reference list is thematic (numbers follow the list order, not
  first-appearance order: [6] is cited after [7] in 1.1, and [48]–[51] appear before [10]). If IJHMT is to be
  strictly sequential-numeric, that is a mechanical renumbering best done once, in the restructuring phase.
- **Phase 7 (language):** nothing in this phase changed wording outside Sections 1.2 and 2.2 and the companion's
  kernel paragraph.
- No numerical code changed, so the verification record from Phase 4 (27 PASS / 0 FAIL / 1 exploratory) still
  describes the code; the suite is re-run for the release record in Phase 8.
