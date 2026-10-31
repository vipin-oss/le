# Gurtin & Pipkin 1968 — the landmark the manuscript is missing

`gurtin_pipkin_1968.csv` (one row, `GP-1968`) records what can honestly be recorded about

> Gurtin, M. E. and Pipkin, A. C., **A general theory of heat conduction with finite wave
> speeds**, *Archive for Rational Mechanics and Analysis* **31**, 113–126 (1968),
> DOI `10.1007/BF00281373`.

## What was and was not verified

* **Now read:** the library copy `gurtin1968.pdf` (561 kB) was opened. Page 113 shows the
  title, the author line *MORTON E. GURTIN & A. C. PIPKIN* and the Introduction; page 114
  carries the running head *114 M. E. GURTIN & A. C. PIPKIN*, the sentence "We call the
  function a(s) the heat-flux relaxation function" and Eq. (1.2). Eq. (1.1) on p. 113 is
  the linearized flux as a history functional, `q(t) = -∫₀^∞ a(s) g(t-s) ds`.
* **Still not verified:** the journal name, volume 31 and the end page 126 are **not
  printed** on those pages, and the ARMA article carries **no DOI**. Those values rest on
  the two identical bibliography entries (`refs_atlas.bib`, `refs_landmark_candidates.bib`)
  and `doi_status` in the CSV says so explicitly. The DOI must be confirmed on a DOI page
  before it is quoted anywhere.

## Why it matters

Gurtin and Pipkin's flux is a functional of the entire temperature-gradient history
through a relaxation kernel. That is the *origin* of the memory/hereditary branch of heat
conduction — finite propagation speed without any relaxation time — of which the
fractional laws, the memory-dependent derivative and the Chen–Nunziato memory theory used
in this manuscript are descendants. The manuscript uses the descendants and never cites
the origin.

## Where it should be cited (four anchors, all checked in the sources)

| # | file, line | manuscript page | why here |
|---|---|---|---|
| 1 | `sections/s03d_admiss.tex`, line 2 | p. 23 | the admissibility paragraph says "for heat conduction with memory it restricts the relaxation functions", and currently leans on Chen–Nunziato 1974 alone; add `\citep{GurtinPipkin1968,ChenNunziato1974}` |
| 2 | `sections/s02_history.tex`, line 11 | p. 14 | the paragraph "Nonlocal, fractional and memory-dependent extensions" starts the memory line at Caputo 1967; Gurtin–Pipkin 1968 is the missing origin |
| 3 | `sections/s03c_prelim.tex`, line 9 | p. 21 | "hereditary kernels" are admitted as a coefficient class in the dispersion polynomial and branch-cut rules are stated — a class should not be introduced without its source |
| 4 | `sections/s16_synthesis.tex`, line 97 | p. 90 | the synthesis sentence contrasting rational heat laws with hereditary kernels repeats the same claim |

Anchor 1 is the strongest: it is the only place where a *thermodynamic* reading of a
memory kernel is asserted, and the citation there is currently doing all its work with a
1968 follower (Chen–Nunziato) rather than the paper that introduced the formulation.

`in_paper_status` in the CSV records that the manuscript cites `GurtinPipkin1968`
**nowhere**; the validator checks that against the `.tex` sources themselves.

## Validator

`python3 check_gurtin_pipkin_1968.py`
→ `PASS all checks (rows=1, anchors=4, values_read=0)` (`check_gurtin_pipkin_1968_log.txt`).
It fails if the DOI is ever presented as verified, if `verified_from` stops recording that
the copy was read, if the quoted page evidence loses its page/equation tokens, if the manuscript starts citing the key without the row being
updated, or if any anchor stops naming a real file, line and page.
