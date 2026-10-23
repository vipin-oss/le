# V-B10c GK closure — Guyer–Krumhansl row re-confirmed against FINDINGS_03 (F10/F11), and the manuscript check

**Status:** closed against a document that now exists. The earlier version of this file recorded the
closure as resting on a supervisor instruction because `control/FULLTEXT_FINDINGS_03.md` was absent
from the remote; that file has since been pushed (`claude/control`, commit `d468ebd`) and has now
been read. Every row reference below is to that document.

---

## Task

1. Fetch `claude/control` explicitly, read `control/FULLTEXT_FINDINGS_03.md`, and re-confirm the
   Guyer–Krumhansl (GK) row in `verification/FULLTEXT_FACTS.csv` against findings **F10** and
   **F11**.
2. Replace the "basis is the supervisor's ruling" provenance with a reference to the document, and
   keep the status split: `PRIMARY-SOURCE-CHECKED` for the Boltzmann-derived structure and `λ²`;
   `UNVERIFIED` for any continuum form.
3. Check the manuscript's GK equation and its `τ_N` / `τ_R` notation against F10.

---

## Method

1. `git fetch origin +refs/heads/claude/control:refs/remotes/origin/claude/control` → moved
   `6569d60` → **`d468ebd`** ("Findings 03: Guyer-Krumhansl 1966 read from rendered pages").
2. Read the document in full (F10 = what the paper prints; F11 = what it does not print; plus the
   two orders addressed to Brave and to Arena).
3. Rewrote the `GuyerKrumhansl1966` row's five evidence-bearing fields against F10/F11, and replaced
   the provenance sentence in `read_level` with the document reference.
4. Re-ran the manuscript search for a GK equation and for `τ_N` / `τ_R` (unchanged result).
5. Re-ran `make_bibtex.py --check-only` after the base edits.

---

## Result

### R-1 — what F10 records, and how the row now reads

F10 states that the paper is kinetic theory (phonon Boltzmann), not a continuum-thermoelasticity
paper, and records:

* **(1a)/(1b)** — the resistive-fast regime: a Fourier-type limit, with the energy equation for the
  isotropic part and an algebraic relation for the flux-like amplitude involving the R operator.
* **(2a)/(2b)** — the normal-fast regime: the energy equation plus an evolution equation for the
  amplitude carrying the N* operator.
* **(4)** — the steady state: the operator acting on the flux amplitude is **`lap + 2 grad div`**,
  together with a term `−a₁/λ²`, and the length scale is **`λ² = c² τ_N τ_z / 5`**.
* **(6)/(8)/(10)** — the steady-state Poiseuille/effective-conductivity result with a Bessel-function
  correction, and its small-argument limit.
* **F11** — what is *not* printed: no single continuum flux law of the form
  `τ_R ∂q/∂t + q = −κ∇T + ℓ²(∇²q + 2∇∇·q)` as one displayed equation, and no thermoelastic coupling.
  Any such equation in the manuscript must cite a source that prints it, be tagged
  `SECONDARY-SOURCE`, and use `λ² = c²τ_Nτ_R/5` as the checkable constant.

The row in `FULLTEXT_FACTS.csv` now carries those equation numbers, the `lap + 2 grad div`
structure, the `λ²` expression, the two printed regime conditions (resistive-fast for 1a/1b,
normal-fast for 2a/2b), the Poiseuille result, and F11's prohibition in the conflict column. Its
status is *closed — PRIMARY-SOURCE-CHECKED (team level: the printed pages were read by the
supervisor and recorded as F10/F11) for the Boltzmann-derived structure and `λ²`; UNVERIFIED for any
continuum flux law and for a `τ_N`/`τ_R` ordering inequality*. Its `read_level` is
`SECONDARY-SOURCE (supervisor-read from rendered pages 2 and 4; recorded as F10/F11 in
control/FULLTEXT_FINDINGS_03.md, commit d468ebd)` — the honest split between what the team verified
and what this reader opened personally.

**One inconsistency inside the document, flagged not smoothed over:** F10's eq. (4) is recorded with
`τ_z` in the length scale (`λ² = c²τ_Nτ_z/5`) while F11's restatement writes `τ_R`. `τ_z` is
presumably the resistive (Umklapp) time and the two symbols are being used for the same quantity, but
that is an inference. Before the constant is quoted in the manuscript the printed page should settle
which symbol stands in eq. (4).

### R-2 — the manuscript check returns a negative result, and that is the finding

There is **no GK equation and no `τ_N` / `τ_R` notation in the manuscript** — neither in the frozen
17-section copy used for section mapping nor in the read-only master
(`origin/arena/40393d9f-le`, 93 `.tex` files). Searched: `Guyer`, `Krumhansl`, `Boltzmann`,
`umklapp`, `phonon`, `tau_N`, `tau_{N}`, `tau_R`, `tau_{\rm R}`, `lambda^2`, `second sound`,
`ballistic`. The manuscript's lag symbols are `τ_q`, `τ_T`, `τ_v`, `τ_0`, `τ_m`, `ω` — never
`τ_N`/`τ_R`, and its `λ²`-style symbols belong to the nonlocal length and to wavelengths.

So the notation check against F10 has **no object**. What the search does establish is the state of
the one place a GK anchor would sit: sec02's phase-II paragraph cites `\cite{Guyer1990}`
(Guyer & McCracken, *Phys. Rev. A* **41**, 6371), which `control/BRAVE_B6.md` records as
**FABRICATED / NOT FOUND** on four routes with logged response bodies, and which is absent from
`LITERATURE_BASE.csv`. Replacement anchors are already listed at `verification/CITATION_MAP.csv`
row CL-026. No manuscript prose was edited — this review never edits the paper.

**Consequence for anyone drafting a GK paragraph:** per F11 the paragraph must say "derived from the
phonon Boltzmann equation (Guyer & Krumhansl 1966)", may quote `λ² = c²τ_Nτ_R/5`, and must not
attribute a ready-made continuum flux law to the 1966 paper. The row now enforces that.

### R-3 — base records

`LITERATURE_BASE.csv`: LIT-0008 (1964) and LIT-0009 (1966) move to
`SECONDARY-SOURCE (supervisor-read … F10/F11 … d468ebd)`, and their `why` fields now state that the
printed object is the phonon-Boltzmann derivation with `lap + 2 grad div` and `λ² = c²τ_Nτ_z/5`, not
a continuum flux law. Base size unchanged at **466** by this task (it grows only through B05);
blank authors **307**; DOI-less **1**; bib re-checked clean.

---

## Evidence / Sources

* `git show origin/claude/control:control/FULLTEXT_FINDINGS_03.md` (commit `d468ebd`) — F10, F11 and
  the two orders.
* `git log origin/claude/control -1` — `d468ebd`, 2026-10-22.
* `control/BRAVE_B6.md`, `control/ARENA_NEXT.md` — the Guyer1990 fabrication finding and its
  acceptance.
* `git ls-tree -r origin/arena/40393d9f-le | grep '\.tex$'` → 93 files; the regex sweep above.
* `verification/CITATION_MAP.csv` row CL-026.
* Bibliographic facts: R. A. Guyer & J. A. Krumhansl, *Phys. Rev.* **148**, 778 (1966),
  doi:10.1103/PhysRev.148.778; and *Phys. Rev.* **133**, A1411 (1964),
  doi:10.1103/PhysRev.133.A1411 — LIT-0008 and LIT-0009.

## Checks done

1. **Fetch confirmation**: the remote branch moved `6569d60..d468ebd` and the file is now in the
   tree, so the earlier "missing document" finding is superseded rather than deleted — the history
   of why the row was once written differently is preserved in this file's status note.
2. **Field-by-field re-write**, not a text patch: the row's five evidence fields were regenerated
   from F10/F11 and then re-read in the CSV to confirm they saved.
3. **Two-copy manuscript search** with nine regex variants for the lag symbols, so a formatting
   difference could not hide an occurrence.
4. **Symbol-consistency check inside F10/F11** — the `τ_z` vs `τ_R` discrepancy was found by
   comparing eq. (4) with F11 line by line; it is reported, not silently normalised.
5. **Base/bib integrity** after the two `read_level`/`why` edits (`--check-only` passes).

## Confidence

* **HIGH** that the row now reflects F10/F11 as written, including the equation numbers and the
  λ² expression.
* **HIGH** that the manuscript contains no GK equation and no `τ_N`/`τ_R` (two copies, many
  variants).
* **HIGH** that the closure no longer rests on an undocumented instruction: the document is cited by
  commit hash.
* **MEDIUM** on the identification `τ_z ≡ τ_R`; flagged, not resolved.
* **NONE** on any physical content of the GK law beyond F10: this reader did not open the 1966
  paper, and the row says so.

## NOT verified / open issues

1. **The continuum GK flux law remains UNVERIFIED** — by F11 it is not in the 1966 paper at all.
   A manuscript equation of that form needs a printing source, tagged SECONDARY-SOURCE.
2. **`τ_z` vs `τ_R`** in eq. (4) of the paper: needs one look at the rendered page before the
   constant is quoted.
3. **`FULLTEXT_FINDINGS_02` still lists GK 1966 as OPEN**; FINDINGS_03 supersedes that row, but the
   earlier file was not edited (it is on the read-only control branch and is not mine to edit).
4. **The manuscript still carries the fabricated `Guyer1990`.** Fixing it is a manuscript-side
   action (CITATION_MAP CL-026); not done here and not this review's to do.
5. **LIT-0008 is typed "review"** in the base, which is wrong for a 1964 research paper. Left
   unchanged to keep the diff minimal; still flagged for the next base sweep.
