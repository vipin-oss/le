# Step 19 - the four books, and the four claims the author waived

Date: 2026-11-01. Branch `arena/9b458c54-le`.

## 1. Four books came in, three matched their row

`batch5_2026-11-01.csv` - one row per file, with the title page as read:

| file as it arrived | what it turned out to be | verdict |
|---|---|---|
| Macro- to microscale heat transfer | Tzou, **second edition 2015** (Wiley) | accepted, with an edition caveat |
| Fractional Differential Equations | Podlubny, Academic Press 1999, vol. 198 | accepted |
| Theory of Thermal Stresses | Boley and Weiner, Dover reprint of the 1960 Wiley text | accepted, no page numbers (EPUB) |
| Thermoelasticity | **Parkus**, Springer 1976, DOI 10.1007/978-3-7091-8447-9 - **not Nowacki** | rejected, the Nowacki row stays |

The Parkus book was opened even though it was the wrong book: it has no treatment of reciprocity theorems and
the word "variational" occurs in it only inside its reference list, so it could not have carried the sentence
even if the author had been right about which book it was. This is the second time the Nowacki (1975) row has
defeated a batch - the fourth batch sent a two-page journal note for it.

## 2. Four claims closed

`SOURCE_READING_books_2026-11-01.csv`, four rows, each with a location and a quote of at most 27 words:

| claim | book | verdict | where | what was read |
|---|---|---|---|---|
| CR002 | Tzou | SUPPORTED | p.64 | the three instants of time of the DPL model: t+tau_T for the gradient, t+tau_q for the heat flow, t for the energy equation |
| CR112 | Tzou | SUPPORTED | p.62 | the heat flux and the gradient "are assumed to occur at different instants of time" |
| CR039 | Podlubny | SUPPORTED | p.79 | section 2.4.1 "Caputo's Fractional Derivative", and the sentence that introduces it |
| CR169 | Boley and Weiner | SUPPORTED | ch.9 | the plate under a "suddenly applied heat input" |

Three caveats are recorded on the rows themselves:

- **Tzou**: the copy is the 2015 second edition, the manuscript cites the 1997 first. Either the edition goes
  into the reference or the year is checked.
- **Podlubny**: the scan's text layer is rough and the definition display is an image, so the framing
  sentence was quoted, not the formula.
- **Boley and Weiner**: a reflowable EPUB has no page numbers, so the quote is cited by chapter. The exact
  phrase "thermal shock" occurs in the book only inside a reference title; its own wording is "suddenly
  applied".

## 3. Four claims waived by the author

The author said the four recent papers are not important and may be skipped. That is recorded as a decision,
not as evidence: `waived_by_author_2026-11-01.csv` lists CR209, CR210, CR177 and CR050 with the DOI of each
work and what has to happen to the sentence that cites it. The register still marks all four blocked, so the
manuscript has to drop those citations (or the sentences) rather than expect evidence later.

## 4. Where the 111 stand now

**78 closed + 6 to order (6 works) + 4 waived + 4 held, not read + 19 register-level = 111.**

The request list is down from 13 works / 14 claims to **6 works / 6 claims**: Cattaneo 1948, Nowacki 1975,
Carlson 1972, Danilovskaya 1950, Vernotte 1958, Born and von Karman 1912 - one attribution sentence each. The
one-page PDF is rebuilt from the same CSV, still one page.

## 5. Checks

- `check_pdfs_needed.py`: **PASS all checks (needed=1, library=34, findings=3)**, exit 0, with the ledger's
  arithmetic recomputed from the five records (78 + 6 + 4 + 4 + 19 = 111).
- New checks added: the fifth batch is four files with three matches and one named mismatch; the four book
  verdicts are SUPPORTED with a location and a quote and no quote over 27 words; the Tzou rows carry the
  edition caveat and the Boley row says the edition has no pages; the four waived claims are register claims,
  none of them is on the request list, and each says what to do with the sentence.
