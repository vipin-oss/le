# Scope brief — theories and materials in the review

`REVIEW_SCOPE_BRIEF_2026-11-02.pdf` (4 pages, A4) answers one question in plain terms: what does the
review actually cover, in theories and in materials, and which theory applies to which material and
frequency? It is written for a reader who has the 164-page paper in front of them and wants the map
before the territory.

## What is inside

| section | content |
|---|---|
| 1 | the organising idea: one heat-flux template `G(s) = [k(1+τ_T s) + k*(1+τ_v s)/s]/(1+τ_q s)` and one dispersion polynomial in `K = k²`, with Green–Lindsay and Guyer–Krumhansl treated outside it |
| 2 | **the theories**: thirteen heat-conduction laws in one table — position in the template, free parameters, and whether the law gives a finite thermal front; then the elastic enrichments (Eringen nonlocal in both forms, strain gradient, couple stress, micropolar, Klein–Gordon, viscoelastic), the coupled fields (piezoelectric and thermopiezoelectric, magnetic, diffusion, microstructure and two-temperature), and eleven wave and damping problems with the numbers the review reports for each |
| 3 | **the materials**: the five materials that carry computed numbers (aluminium, copper, silicon, carbon steel, fused silica) with `c₁`, `ε`, `f_*` and `α`; the cubic anisotropy of the coupling for Cu, Al and Si; and the materials discussed without numbers (solid helium, NaF, graphite, 6mm piezoelectrics, layered pairs, porous solids, tissue, water-like media) |
| 4 | which theory for which material and frequency: six scenarios at `τ_q = 1 ps`, with `ω/ω_*`, `ωτ_q`, the penetration depth, the wavelength and the assessment; then the decision rule as the paper states it |
| 5 | map of the review: six parts, sections 1–38 and Appendices A–H |
| 6 | what the brief and the paper do not claim |

## Provenance

Every number in the PDF is copied from a file inside `paper_v2/overleaf_package.zip`:

- the template and the parameter assignments — §3 (parameter table), §33 (comparative table), §8;
- the materials and their constants — §3 (materials table);
- the cubic anisotropy — §14;
- the six scenarios and their assessment — §30, with the decision thresholds of §33.5;
- the Rayleigh and Lamb figures quoted in Table 2 — §18 and §19;
- the page, section, equation, table, figure and reference counts — the paper's own build and gate log.

No claim, reference or number is added, and nothing is taken from memory. Where the paper labels a
value as a rounded handbook number for illustration at 300 K, the brief says so.

## Rebuilding the PDF

The brief is generated, not hand-drawn, so it can be regenerated after any change to the paper:

```sh
python3 -m pip install --break-system-packages reportlab   # only dependency
cd paper_v2/arena_deliverables/BRIEF_2026-11-02
python3 make_brief_pdf.py
```

`make_brief_pdf.py` is self-contained: it holds the text and the tables inline, typesets A4 with
DejaVu Serif and DejaVu Sans (both present on the system), and writes
`REVIEW_SCOPE_BRIEF_2026-11-02.pdf`. No LaTeX engine is involved — there is none in this sandbox; see
`../TEX_ENGINE_STATUS_2026-11-01.md`. The Greek symbols, the superscripts and the `≈`, `≥`, `→`
arrows are Unicode glyphs in those fonts, not images.

If the paper's numbers change, change them here as well: the two dozen figures in Table 1 and Table 5
are the only places where the brief can drift from the paper.
