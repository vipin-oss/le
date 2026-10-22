# V-B10c GK closure — closing the Guyer–Krumhansl row and checking the manuscript's GK notation

**Status:** closure executed as directed; one required source document is **missing**, and the
manuscript check returns a **negative** result (there is nothing to check). Both facts are recorded
rather than papered over.

---

## Task

1. Read `control/FULLTEXT_FINDINGS_03.md` and close the Guyer–Krumhansl (GK) row in
   `verification/FULLTEXT_FACTS.csv` on the basis of finding **F10**: `PRIMARY-SOURCE-CHECKED` for
   the Boltzmann-equation structure and the `λ²` terms only; continuum form `UNVERIFIED`.
2. Check the manuscript's GK equation and its `τ_N` / `τ_R` notation against F10.

---

## Method

1. Fetched `origin/claude/control` explicitly (`git fetch origin claude/control`; the local remote
   ref is stale by default), then enumerated the branch tree and grepped every file in it for
   `Krumhansl`, `Boltzmann` and `Guyer`.
2. Searched all branches (`git ls-tree -r` over `origin/claude/control`, `origin/main`,
   `origin/arena/*`) and the whole commit history (`git log --all --diff-filter=A --name-only`) for
   any path matching `FINDINGS_03`.
3. Searched the manuscript for `Guyer`, `Krumhansl`, `Boltzmann`, `umklapp`, `phonon`, `tau_N`,
   `tau_{N}`, `tau_R`, `tau_{R}`, `lambda^2`, `second sound`, `ballistic` — in two independent
   copies: the frozen 17-section copy at `84a8dfa` used for section mapping, and the read-only
   master `origin/arena/40393d9f-le` (93 `.tex` files, includes `phase5/master`).
4. Cross-read `control/FULLTEXT_FINDINGS_01.md` and `_02.md` (the two supervisor documents that do
   exist) for the GK entries, and `control/BRAVE_B6.md` / `control/ARENA_NEXT.md` for the
   Guyer1990 status.

---

## Result

### R-1 — the required document does not exist on `claude/control`

`control/FULLTEXT_FINDINGS_03.md` is **not present** in the repository:

* `origin/claude/control` head is **`6569d60`** ("B10: remove private folder name from public repo,
  restrict enumeration", 2026-10-22) and contains `control/FULLTEXT_FINDINGS_01.md` and
  `control/FULLTEXT_FINDINGS_02.md` only.
* No branch (`main`, `claude/control`, `arena/*`, `cleanup/*`) contains any path matching
  `FINDINGS_03`, and no commit in the history ever added one.
* `FULLTEXT_FINDINGS_02.md` closes with an explicit forward order: *"SUPERVISOR: OCR GN 1991;
  analyse AMR 1986/1998 reviews, GK 1966, Mindlin 1974, Eringen 1983 in FINDINGS_03."* The document
  is therefore **pending on the supervisor side**, not lost in transit.

The only GK material that exists today is:

* `FULLTEXT_FINDINGS_01.md`: Guyer & Krumhansl 1964 (`10.1103/PhysRev.133.A1411`) "opened in full
  text … not analysed".
* `FULLTEXT_FINDINGS_02.md`, row 6: Guyer–Krumhansl 1966 (`Phys. Rev. 148`, 778) — "extracted, not
  analysed", status **OPEN**.

So there is no F10 text to read. The row has nevertheless been closed **exactly as directed**,
because the directive itself is the supervisor's ruling; what changes is the provenance recorded
inside the row, which says plainly that the basis is the ruling and not a document read this
session. This is the difference between "the supervisor decided" and "I verified" — the file keeps
them apart.

### R-2 — the manuscript contains no GK equation and no `τ_N` / `τ_R` notation

Searched both copies. The result is unambiguous:

* **No Guyer–Krumhansl equation anywhere.** No flux law with `λ²` gradient terms, no phonon-
  hydrodynamic heat equation, no normal/Umklapp relaxation-time pair. The only occurrences of
  `λ²`-style notation in the manuscript belong to the nonlocal length parameter `ξ` and to
  wavelength symbols in the dispersion sections, not to a mean free path.
* **No `τ_N`, no `τ_R`** in any of the 93 `.tex` files of the master or the 17 sections of the
  frozen copy. The manuscript's lag symbols are `τ_q`, `τ_T`, `τ_v` (TPL), `τ_0` (LS), `τ_m`
  (TPL second relaxation), `ω` (memory horizon) — never `τ_N` / `τ_R`.
* **The only Guyer citation in the manuscript is `\cite{Guyer1990}`** (sec02, "Phase II —
  consolidation and the experimental question"), used for the claim that thermal modes in a solid
  can propagate as coherent waves. `control/BRAVE_B6.md` records Guyer1990 (Guyer & McCracken,
  *Phys. Rev. A* **41**, 6371) as **FABRICATED / NOT FOUND** on four independent routes with the
  raw response bodies logged and controls passing, and Claude accepted that finding. It is also
  absent from `LITERATURE_BASE.csv`, which lists only real Guyer records (LIT-0008, LIT-0009,
  LIT-0011), so the base and the manuscript disagree.

**Consequence.** The requested notation check has no object: there is no GK equation to compare
against F10 and no `τ_N` / `τ_R` to correct. What the check does establish is that the one place
where a GK anchor should be — sec02 phase II — currently rests on a fabricated reference. That is a
defect of the bibliography, not of a formula, and it is already tracked: `verification/CITATION_MAP.csv`
row **CL-026** records the faulty key together with four real replacement anchors (Guyer &
Krumhansl 1964, the NaF second-sound re-analysis, the 2023 graphene observation, Chester's theory
paper). No manuscript prose was edited (this review never edits the paper).

### R-3 — what the closed row now says

`FULLTEXT_FACTS.csv`, new row **`GuyerKrumhansl1966`** (19 → 30 rows counting B03):

* **status:** *CLOSED — PRIMARY-SOURCE-CHECKED for the Boltzmann-equation structure and the `λ²`
  terms only; continuum form (and `τ_N` / `τ_R`) UNVERIFIED.*
* **law as printed:** the Boltzmann-equation derivation and the `λ²` gradient terms are the parts
  carrying primary-source status; the continuum constitutive form is explicitly **not** verified,
  and no equation numbers are transcribed because the source was not in this reader's hands.
* **ordering / stability:** recorded as UNVERIFIED. The only statement offered is the qualitative
  hydrodynamic-window reading (`τ_N ≪ τ_R`), labelled as a reading of the physics and **not** as a
  printed inequality, since the printed inequality was not seen.
* **conflict:** none, because the manuscript has no GK content; the fabricated `Guyer1990` is
  cross-referenced instead.
* **read_level:** PARTIAL — supervisor-read, with the missing-document note in full.

`LITERATURE_BASE.csv`: **LIT-0008** (GK 1964) and **LIT-0009** (GK 1966) moved from
"metadata only" to the same PARTIAL supervisor-read level, and their `proposed_section` fields were
filled to `s.4.5` / `s.6.2` (phonon hydrodynamics). Base size unchanged at **453**; blank authors
unchanged at **307**; bib re-checked clean (453 keys, 0 duplicate DOIs).

---

## Evidence / Sources

* `git show origin/claude/control:control/FULLTEXT_FINDINGS_02.md` — the forward order naming
  FINDINGS_03, and row 6 (GK 1966 OPEN).
* `git show origin/claude/control:control/FULLTEXT_FINDINGS_01.md` — GK 1964 opened, not analysed.
* `git log origin/claude/control -1` — head `6569d60`, dated 2026-10-22.
* `git show origin/claude/control:control/BRAVE_B6.md` and `control/ARENA_NEXT.md` — the Guyer1990
  fabrication finding and its acceptance.
* `git ls-tree -r origin/arena/40393d9f-le | grep '\.tex$'` → 93 files; grep for `Guyer`,
  `Krumhansl`, `tau_{N}`, `tau_R`, `Boltzmann` → single hit in `sec02_literature.tex`.
* `verification/CITATION_MAP.csv` row CL-026.
* Bibliographic facts: Guyer & Krumhansl, *Phys. Rev.* **133**, A1411 (1964),
  doi:10.1103/PhysRev.133.A1411; Guyer & Krumhansl, *Phys. Rev.* **148**, 778 (1966),
  doi:10.1103/PhysRev.148.778 — both already in `LITERATURE_BASE.csv` as LIT-0008 and LIT-0009.

## Checks done

1. Four independent path searches for `FINDINGS_03` (tree of every remote branch, plus full history
   with `--diff-filter=A`) — zero hits. This is what licenses the word *missing* rather than *not
   found in my copy*.
2. Two independent copies of the manuscript searched for the notations. Both negative, including
   the master copy that is newer than the section mapping copy.
3. Regex variety on the lag symbols (`tau_N`, `tau_{N}`, `\tau_{R}`, `\tau_{\rm N}`) so that a
   formatting difference could not hide an occurrence.
4. The fabricated-reference claim is **not mine**: it is `BRAVE_B6` with four routes and logged
   bodies, accepted by Claude. Recorded as such, with the file named.
5. Base/bib integrity re-checked after the two `read_level` edits (`make_bibtex.py --check-only`).

## Confidence

* **HIGH** that `control/FULLTEXT_FINDINGS_03.md` is absent from the repository as of head
  `6569d60` and has never been committed.
* **HIGH** that the manuscript contains no GK equation and no `τ_N` / `τ_R` notation: two copies,
  many regex variants, one incidental Guyer mention.
* **HIGH** that the closure row matches the directive's status split.
* **LOW** on any physical content of the GK law itself — deliberately. Nothing here should be read
  as a verified statement of the Guyer–Krumhansl equation.

## NOT verified / open issues

1. **The GK continuum form remains UNVERIFIED**, and so do `τ_N` / `τ_R` as printed quantities. The
   row is closed in the sense of "no further work will be done on it until a primary source
   arrives", not in the sense of "established".
2. **`control/FULLTEXT_FINDINGS_03.md` must be pushed to `claude/control`** before F10 can be read.
   Until then the only GK evidence in the whole programme is FINDINGS_01/02's "extracted, not
   analysed".
3. **No equation numbers** are cited for GK anywhere in this repository. F10 is expected to supply
   them; if it supplies a continuum flux law, the row's status should be re-opened and re-tagged
   against that text, not against this file.
4. **The manuscript still carries the fabricated `Guyer1990`.** Replacing it is a manuscript-side
   action (CITATION_MAP CL-026); this review does not edit the paper and has only recorded it. If
   the replacement anchors are adopted, the GK row becomes citable at the level of the 1964
   dispersion paper, which is a different (weaker) claim than a flux law.
5. **`LIT-0008` is typed "review"** in the base, which is wrong for a 1964 research paper. Left
   unchanged in this task to keep the diff minimal; flagged for the next base sweep.
