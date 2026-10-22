# api_log — raw-response provenance for B5b / B5b-2

Purpose: every record in `../LITERATURE_BASE.csv` and every bibliographic assertion in
`../V-B5b_guyer1990.md` must be traceable to a request that was actually issued. This
directory holds that trail.

Files
-----
| File | What it is |
|---|---|
| `b5b_queries.csv` | One row per Crossref query issued for B5b/B5b-2: id, route, full URL, date, HTTP status, rows requested, rows returned. |
| `LITERATURE_ROW_INDEX.csv` | One row per record in `LITERATURE_BASE.csv`: record id, DOI, the query id that returned it, date, HTTP status, and an honesty note on how exact the attribution is. |
| `guyer1990.json` | The ten raw response bodies (Crossref / OpenAlex / Semantic Scholar, target + controls) behind the Guyer1990 tie-break, with a per-request HTTP status and status basis, plus the conclusion record. |

Status column
-------------
The sandbox `fetch_page` tool returns the response **body** but does **not** expose the
numeric HTTP status code. So `http_status` is recorded as one of:

* `200` — the body is a JSON document carrying `"status":"ok"`, `"message-type":"work"`,
  `"message-type":"work-list"`, or a numeric `"count"` / `"meta"` object. For these the 200
  is not inferred: a 4xx/5xx from these endpoints returns an error document instead.
* `404` — marked `status_basis: inferred`. The body is the endpoint's documented
  not-found document (`Resource not found.` for Crossref `/works/{doi}`; `{"error":
  "Paper with id ... not found"}` for Semantic Scholar).

No status in this log is guessed silently; where it is inferred, the JSON says so.

Attribution honesty
-------------------
`LITERATURE_ROW_INDEX.csv` distinguishes two levels of precision, in its `note` column:

* `exact query attributed` — 91 records added in the final B5b-2 batch, where the working
  list was kept in per-query blocks, so each DOI maps to one query id (Q9–Q14).
* `batch-level attribution` — the 149 earlier B5b records and the 133 records of the first
  B5b-2 batch. These were merged into the CSV from multi-query harvests without a per-row
  query pointer, and that pointer cannot now be reconstructed without re-querying. Rather
  than invent a plausible-looking query id for each of those 282 rows, they are labelled
  `PRE-B5b (Q1-Q7 batch)` and `BATCH-B5b2 (Q1-Q8 batch)`. The candidate query set for each
  batch is in `b5b_queries.csv`; the fact that the record came back from *one of* those
  queries is verified, the exact one is not.

What this log does **not** contain
----------------------------------
* No full raw JSON is stored for the 282 batch-level rows — only for the Guyer1990 case,
  where the order explicitly required raw bodies. Bulk storage of ~400 response documents
  was not attempted.
* No request was retried with a different URL until it succeeded. Every request in
  `guyer1990.json` is the first attempt, recorded with its outcome.
