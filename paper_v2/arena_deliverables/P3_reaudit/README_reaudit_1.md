# Task 2, re-run — the 20 flagged register rows, re-audited against the current `main.pdf`

`claim_register.csv` carries 20 rows marked PARTLY SUPPORTED (18) or NOT SUPPORTED (2).
`reaudit_1.csv` re-audits exactly those 20 against the **build in this repository**
(`paper_v2/main.pdf`, 145 pp), not against the wording they were originally flagged on.

## Result

| outcome | rows |
|---|---|
| resolved — the current wording matches the source | 19 |
| still partly supported | 1 (CR046) |
| wording changed, needs a fresh check | 0 |
| passage not located in the PDF | 0 |
| **total** | **20** |

The single remaining item is **CR046** (Gorenflo, Kilbas, Mainardi & Rogosin 2014): the
citation now covers the Mittag-Leffler functions only, which the monograph does support,
but the "heavy tails" assertion attached to it is not in the source as read. It needs either
a page reference into the monograph or a weaker sentence.

## How each row was decided (mechanically, not by impression)

1. **Locate.** The wording the earlier pass judged (`P1_audit/reaudit_flagged_20.csv`,
   column `current_text`) is matched against every page's extracted text on *content words
   of four or more letters*, order-free, with a three-page window to absorb page breaks.
   The measure is the recall of the earlier wording on that page.
2. **Still present?** recall ≥ 0.80 → `yes`; 0.50–0.80 → `partly`; otherwise `no`.
3. **Where does the register sentence sit now?** An independent word-sequence match of the
   register statement against the pages gives the page quoted in `manuscript_page`.
4. **Verdict.** `resolved` only where the earlier wording is still present *and* the earlier
   pass had found the current wording to match its source; `still partly supported` where
   that earlier judgement was itself negative; `wording changed` where the wording is gone
   or edited. The validator refuses a `resolved` row whose earlier wording is not present,
   so the verdict cannot drift away from its evidence.

Nothing here re-derives the *source* side from scratch: the judgement about what each cited
source says is the one recorded in the earlier pass (which names its basis per row), and it
is carried over only while the manuscript text it was made about is still the text in this
PDF. Where that is not the case the row says `wording changed - re-check` instead.

## Files

| file | content |
|---|---|
| `reaudit_1.csv` | 20 rows: claim id, register verdict, cited source, PDF page, whether located, the page text (600 chars), whether the earlier wording is still present and its recall, the re-audit verdict, the basis, a suggested wording where one exists, and a note |
| `make_reaudit_1.py` | rebuilds the CSV from `main.pdf` + `claim_register.csv` + the earlier re-audit |
| `check_reaudit_1.py` | validator: 20 flagged ids in register order, schema, page range, verdict vocabulary, the `resolved`-needs-evidence rule, no URLs/Drive ids |
| `check_reaudit_1_log.txt` | validator output (`PASS all checks (rows=20, resolved=19)`) |

```
python3 make_reaudit_1.py     # needs pypdf for the text extraction
python3 check_reaudit_1.py    # stdlib only
```

No `.tex` file was edited, and no judgement about a source was invented: where the earlier
pass had no evidence, the row keeps that status rather than upgrading it.
