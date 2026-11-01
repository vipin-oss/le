# Re-audit of the 20 flagged claims (Task 2)

Arena task: `HANDOFF_FOR_ARENA.md`, section 6, **Task 2**. Branch `arena/9b458c54-le`, 31 Oct 2026.
`main.tex` and `sections/*.tex` were not touched.

## What was checked

All 20 rows of `claim_register.csv` whose verdict is PARTLY SUPPORTED (18) or NOT SUPPORTED (2) were re-read
**against the current `main.pdf`**, not against the text that was audited in the earlier batches.
`current_text` is quoted from the build in this repo (145 pp., reference numbering [1]-[337]).

Judgement rule: a row is `yes` only if the *current* sentence states no more than the source passage recorded in
the claim register says, `partly` if the citation is now correctly scoped but some assertion in the same sentence
is still unsupported, `no` if the old mismatch is still there. No new source text was read for this task; the
source evidence is the recorded `source_wording_max25words` / `what_source_actually_states` / page of
`claim_register.csv`, which is why every row cites the page or equation it rests on.

## Result

| matches_source | rows |
|---|---|
| yes | 19 |
| partly | 1 |
| no | 0 |

The one `partly` is **CR046** (Gorenflo, Kilbas, Mainardi and Rogosin 2014): the citation now covers only the
Mittag-Leffler functions, which the monograph does support, but the "heavy tails" clause in the same sentence is
no longer attributed to any source and was not found in the pages that were read. Suggested wording in the CSV
drops that clause.

What changed in the manuscript (page numbers from the current build):

| claim | source | what the current text does |
|---|---|---|
| CR032 | Aldandani2026 [85] | MGT now credited to [84] only; [85] carries fractional, nonlocal (Klein-Gordon) and three-phase-lag, p. 36 |
| CR034, CR037 | Youssef2006 [62], Bassiouny2020 [65] | Laplacian relation marked as "the form commonly used"; Youssef's own definition given; Bassiouny moved out of the LS/GN group to "two relaxation times", p. 36 |
| CR045 | Ezzat2011 [58] | modified Riemann-Liouville vs Caputo stated explicitly, p. 39 |
| CR046 | Gorenflo et al. 2014 [167] | citation narrowed to the functions; heavy-tail clause still unsourced, p. 39 |
| CR062 | Gorenflo1997 [166] | cited for fractional calculus only, p. 39 |
| CR071, CR076 | Sur2025 [114], Ezzat2015 [173] | placed with higher-order memory-driven nano-beams and with Lord-Shulman-type MDD, p. 39 |
| CR086, CR091, CR104, CR105 | Green and Naghdi [36-38] | entropy balance now a joint attribution; the q/T0 comparison moved to a p. 23 parenthetical; the sentence itself is on p. 14 |
| CR087, CR088 | Coleman and Gurtin [138], Chen and Nunziato [139] | entropy-flux clause removed; internal-state-variable restriction and relaxation-function inequalities separated, pp. 23-24 |
| CR099, CR100 | Lord and Shulman [32], Green and Lindsay [33] | "Cattaneo form" kept as a description of the law; GL coefficients described as named relaxation times only "in the later literature", p. 14 |
| CR118 | Moore and Gibson [66] | "nonlinear" dropped; only "acoustics of a gas with relaxation", p. 14 |
| CR135 | Marotti de Sciarra [131] | cited for GN type-II mixed variational formulations; reciprocity theorems carried by [22, 23], p. 27 |
| CR143 | Yang et al. 2021 [121] | "beams" replaced by nanoplates and plate resonators, p. 29 |
| CR206 | Nunziato and Cowin [75] | volume-fraction field [75-77]; extra dilatational wave to [76]; thermal coupling to [77], p. 72 |

## Files

| file | content |
|---|---|
| `reaudit_flagged_20.csv` | 20 rows: `claim_id, current_text, matches_source, suggested_wording, page_or_equation, cited_source, manuscript_page, basis_for_judgement` |
| `check_reaudit_flagged_20.py` | validator (20 rows, ids match the register's flagged set, verdict values, 30-word limit); prints PASS, exit 0 |

## Limits

- Judgements are made against the evidence recorded in `claim_register.csv`, not against freshly opened PDFs.
  If a recorded `what_source_actually_states` is itself wrong, this re-audit inherits the error.
- Reference numbers in square brackets are the current build's numbering; the key is given in `cited_source`.
- This is a wording audit. It does not re-derive any result and does not certify that the sources exist.
