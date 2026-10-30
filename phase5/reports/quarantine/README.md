# Quarantined Crossref files

This directory holds Crossref response files that were removed from `crossref_raw_*`
directories because they could not be authenticated against a request-log entry
or because the DOI does not exist in Crossref.

## 10.1016_0020-7222(92)90072-Z.json

**Removed from:** `phase5/reports/crossref_raw_r3d/`

**Reason:** No matching entry in `CROSSREF_R3D_REQUEST_LOG.csv`; the DOI
`10.1016/0020-7222(92)90072-Z` does not exist in Crossref (the real DOI for
Aifantis's "On the role of gradients in the localization of deformation and
fracture", Int. J. Engng Sci. 30 (1992) 1279-1299, is `10.1016/0020-7225(92)90141-3`).
The file contained a fabricated `http_status: 200` response and was not produced
by the fetch command.

**Replacement:** `phase5/reports/crossref_raw_r3d/10.1016_0020-7225_92_90141-3.json`
with matching request-log entry in `CROSSREF_R3D_REQUEST_LOG.csv`.

**Bib correction:** `Aifantis1992` DOI changed from `10.1016/0020-7222(92)90072-Z`
to `10.1016/0020-7225(92)90141-3` in `phase5/master/references_local.bib`.
