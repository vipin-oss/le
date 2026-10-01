# Full-source review search/access log

Date:30 September2026. User supplied https://github.com/vipin-oss/BFS-FEM-MATLAB/blob/main/alit.zip after the assistant requested B01/B02/B03.

## Input retrieval

- GitHub contents API returned200; archive size1,274,111bytes; blob70586950b70674a0f5365341cb2f2f1fc7929a9d.
- Raw download returned200; actualZIP safely inventoried/extracted.
- Archive contains3PDFs only,1,544,618uncompressedbytes.
- Titles/frontmatterDOIs matched all3requested sources.
- PDF pages:B01=18,B02=11,B03=15.
- Native page-marked text extracted. Relevant equations/BCs/ICs/material/method/case/benchmark sections read; key Table1/Table2/Eq36–37 and cylinder/table pages inspected as rendered images.
- No external upload of PDFs or unpublished material; no scientific solver run.

## Exact new searches

1. `"10.1007/s10483-025-3280-7" correction erratum`
   Returned unrelated erratum records; excluded. No verified relevant correction was identified in this query. This does not prove that no publisher update/correction exists. The observed Eq36 inconsistency is our source-algebra observation, not an official erratum claim.
2. `"Fractional thermoelasticity revisited with new definitions of fractional derivative" "104043"`
   Confirmed metadata/DOI10.1016/j.euromechsol.2020.104043 via published citation records. This is B01Ref52, used for its Figure4 theoretical comparison. Its full text was not obtained/inspected here; not required for first explicitly specified Figure5 case.

## Source inspection level

B01:fullPDFavailable; relevant model equations, Table1, Eqs44–66, Table2/Figs4–8 and conclusions/references inspected; rendered pages7/9/11read. Complete proof/admissibility/correction audit not performed.
B02:fullPDFavailable; formulation/normalization/initial conditions/solution/Eqs54–57 and results inspected; rendered pages4/6read. Complete proof/correction audit not performed.
B03:fullPDFavailable; diffusion/boundary/integral/algorithm/example/Table1–2 and conclusions inspected; rendered pages10–11read; appendix coefficient passages inspected as support, not all independently re-derived. Complete proof/correction audit not performed.

## Outcome / exclusions

- Former full-source access blockers B01–B03resolved by user-provided files; original historical review retained.
- All three numerical-reference tracks are mathematical/source verification, not experimental validation.
- Do not use B01Fig4 as a fully reconstructed case without Ref52/settings.
- Use B02LS case for the immediate common-law curved route, not direct GL/GNII overlays.
- Do not impose cold finite-boundary steady conditions as though they equal B03's unbounded problem.
- Formal novelty/closest-five/current scooping not completed; no gap confirmed.

Exact conditions, operator identities and remaining issues are in FULL_SOURCE_REVIEW.md and ANALYTICAL_SOURCE_CHECKS.md. No agreement/runtime/convergence outcome is reported.
