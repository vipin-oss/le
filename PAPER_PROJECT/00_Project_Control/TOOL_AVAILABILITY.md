# TOOL_AVAILABILITY — Phase 0 (2026-10-01)

Measured in this session's sandbox (commands run 2026-10-01). Status labels per MASTER_PROMPT §8. Software integrity record per §83.

## 1. Compute environment (RUN_SUCCESS — measured)
| Item | Value |
|---|---|
| OS | Debian GNU/Linux 13 (trixie), Linux 6.1.158+ x86_64 |
| CPU | 2 cores, Intel Xeon @ 2.60 GHz |
| RAM | 1,984 MB total (≈1.4 GB free when measured) |
| Disk | 25 GB volume, ≈20 GB free |
| GPU | none (`nvidia-smi` absent) |
| Python | 3.13.14 (pip 26.1.2) |
| Libraries | numpy 2.3.5, scipy 1.17.1, matplotlib 3.10.9, pandas 2.2.3, sympy 1.14.0, mpmath 1.3.0, numba 0.66.0, Pillow 12.3.0, python-docx 1.1.2, openpyxl 3.1.5 |
| Other | gcc, gfortran, node, git |
| Match with the handoff | `data/ENVIRONMENT.json` records Python 3.13.14 / numpy 2.3.5 / scipy 1.17.1 / matplotlib 3.10.9 / Linux x86_64 — **identical versions**, so reproduction here is like-for-like (hardware differs; the handoff also used a 2-CPU sandbox). |
| Persistence | only `/home/user` is snapshotted; directories named `.cache`, `.venv`, `build`, `dist`, `node_modules`, `out`, `target` etc. are excluded; cap ≈128 MB / 10,000 files |

## 2. Not available here
| Tool | Status |
|---|---|
| pdflatex, xelatex, lualatex, latexmk, tectonic | not found → no LaTeX → no LaTeX→PDF. Downloading a tectonic binary is an UNTESTED alternative. |
| pandoc, libreoffice/soffice, unoconv | not found → no automatic md→docx/pdf or docx→pdf; `.docx` must be built with python-docx. |
| MATLAB, Octave, Julia | not found → the user's MATLAB FEM4/BFS code cannot be executed (NOT_RUN). |
| GPU | none. |
| Not installed (pip reachable, not tested) | e.g. reportlab / fpdf2 (PDF), python-pptx. |

## 3. Network and literature access
| Resource | Status |
|---|---|
| pip / PyPI | HTTP 200 |
| github.com | HTTP 200 (public-repo retrieval works) |
| sciencedirect.com (curl HEAD) | HTTP 403 → publisher full texts are not reachable by curl; not tested via `fetch_page` |
| `web_search` tool | AVAILABLE (live); used 2026-10-01 for MFP, Klimm and Adachi checks |
| `fetch_page` tool | AVAILABLE; an open-access Wiley page was read; PDFs are parsed up to 30 pages |
| Scopus / Web of Science / JCR | NO ACCESS → any quartile / impact-factor statement stays secondary evidence (public SCImago pages) and JCR is UNVERIFIED (§5, §53) |
| Google Scholar | not directly accessible (web search only) |

## 4. Output and viewing
The in-app viewer previews md, html, svg, png, pdf, csv, docx, xlsx, pptx. HTML previews have no network (inline assets only).

## 5. What was executed this session before Phase 0
| Action | Status |
|---|---|
| Download handoff + SHA-256 verification (303/303) | RUN_SUCCESS |
| Re-run of 4 production cases with the shipped code; stored values reproduced to ≤9e-11 | RUN_SUCCESS |
| Independent 3-D check of `rotate_Q_beta` (shipped vs patched); patched version agrees to 1.6e-16 | RUN_SUCCESS / ANALYTICALLY_CHECKED |
| 8-run circle test with patched code: identical peak for all φ (spread 3.2e-10) | RUN_SUCCESS |
| 12-run ellipse test with patched code: modulation 36.30% (shipped 36.56%) | RUN_SUCCESS |
| Window-length tests (8→64 t_th, quasi-static elasticity), H3 tests (inertia on/off, window scan, damping), steady-gradient test, V3b | RUN_SUCCESS — results in `/home/user/work/rerun/REVIEW_FINDINGS.md` |
| Patch applied to the project code | **NOT DONE** — exists as `rerun/rotate_Q_beta_fix.diff` and `rerun/fixed_src/cg_model.py`; the working copy `rerun/proj/` is still UNFIXED; handoff originals untouched |
| Full re-run of Blocks A–D with corrected code and an artifact-free single-pulse synthesis | NOT_RUN |
| Execution of the MATLAB FEM4 package | NOT_RUN |
