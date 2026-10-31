# P3 evidence and claim check, batch A-002

Scope: the eight claim-bearing sentences that batch 001 deferred (six in section 7,
two in section 6), plus the separate check of Quintanilla (2003) requested for claim A2.

Batch 001 is unchanged: `claim_check_A_batch_001.csv`, `missing_sources_A.csv` and
`README_batch_001.md` were neither edited nor regenerated.

## Deliverables

| File | Rows | Columns |
|---|---|---|
| `claim_check_A_batch_002.csv` | 25 | 11 (header byte-identical to batch 001) |
| `missing_sources_A_batch_002.csv` | 11 | 7 (new missing works only) |

Encoding: ASCII, CRLF, every field on one line. Claim quotes are capped at 25 words.

## Claim identifiers

| Id | Section | Sentence, in short |
|---|---|---|
| A31 | 6 (lags) | thermodynamic compatibility and continuous dependence of the TPL model are studied in Chirita (2016) |
| A32 | 6 (lags) | stability and plane-wave characterization in the hyperbolic two-temperature theory are in Prasad (2020) |
| A33 | 7 (memory) | memory-dependent derivative modelling was introduced by Wang and Li (2011) |
| A34 | 7 (memory) | reviews and critical discussions of the logic of fractional thermoelasticity, six works |
| A35 | 7 (memory) | MDD versions of lag models replace the first-order derivatives in the DPL or TPL law by D_tau, eleven works |
| A36 | 7 (memory) | fractional order generalized thermoelasticity was developed by Youssef (2010), with a variational principle by Youssef and Al-Lehaibi (2010) |
| A37 | 7 (memory) | fractional Cattaneo-type thermoelasticity with new fractional derivatives was introduced by Yu and Deng (2020) |
| A38 | 7 (memory) | thermoelasticity as wave hierarchies (Scott) and generalized thermoelasticity with MDD (Shaw) |

## Method

1. Each cited work was looked up by first author, by distinctive title phrase and,
   where available, by its printed DOI string.
2. Where a copy is held, page 1 (title block, abstract, and the first equations when
   they fall on that page) was read as text and the wording recorded verbatim, trimmed
   to 25 words. Body pages and full derivations were not read.
3. Where no copy is held, the row is `SOURCE NOT AVAILABLE` at level `V0` and the notes
   record the terms actually searched for that item.
4. No bibliographic field was edited; a DOI is recorded only in the source columns.

## Results

Claims: 8. Source rows: 25. Distinct works: 25.

| Verdict | Rows |
|---|---|
| SUPPORTED | 6 |
| PARTLY SUPPORTED | 2 |
| NOT SUPPORTED | 1 |
| SOURCE NOT AVAILABLE | 16 |

Verification level: `V2` 1, `V1` 8, `V0` 16.

### By claim

- A31: not verifiable. Chirita (2016) is not held (already recorded in batch 001).
- A32: not verifiable. Prasad (2020) is not held (already recorded in batch 001).
- A33: supported, level `V2`. The abstract of Wang and Li (2011) presents the
  memory-dependent derivative as something the authors "bring forth", defined in an
  integral form of a common derivative with a kernel on a slipping interval. The paper
  does not use the word "introduce", so the manuscript's "was introduced by" is a
  paraphrase of the authors' own claim of origination. Definition 2.1 and eq. (5) are
  on p. 1563.
- A34: one supported, one not supported, four unavailable. Yu (2024) supports the
  reinterpretation half of the bracket. Gorenflo and Mainardi (1997) is a review of
  fractional calculus, not of fractional thermoelasticity: its abstract lists
  Riemann-Liouville operators with Laplace transforms, Abel equations and
  relaxation-oscillation equations, and no thermoelastic topic. Povstenko (2016) is a
  book that is not held; Povstenko (2004, 2007, 2009) are not held either.
- A35: five supported, two partly supported, four unavailable. The three-phase-lag
  plus MDD combination is confirmed for Singh (2019), Singh (2020a) and Biswas (2019)
  (verified in batch 001), and for Sur et al. (2019), whose abstract describes a TPL
  model "defined in an integral form of a common derivative on a slipping interval" with
  memory-dependent heat transfer incorporated. Sur et al. (2025) confirms higher-order
  memory-driven heat transfer but its abstract page prints no lag law. Ezzat et al.
  (2015) confirms MDD in the heat-conduction law but builds a one-relaxation-time
  (Lord-Shulman type) theory, not a DPL or TPL model. Abouelregal (2023), Hamza (2014),
  Sur and Kanoria (2012), Yu (2014) and Sherief and Raslan (2018) are not held.
- A36: not verifiable. Neither Youssef (2010) paper is held; the author sweep returned
  only a 2006 journal paper, a conference-file copy and a 2018 hyperbolic
  two-temperature paper.
- A37: not verifiable. Yu and Deng (2020) is not held.
- A38: not verifiable. Scott (2008) and Shaw (2019) are not held.

## Quintanilla (2003), the A2 attribution

The requested question was whether the paper states the condition tau_T >= tau_q/2,
with equation, page and a quote of at most 25 words.

Outcome: **not identified from its own first page in this batch. No verdict is offered
and no wording is quoted.** The paper is cited in the bibliography as
Quintanilla, R. (2003), A condition on the delay parameters in the one-dimensional
dual-phase-lag thermoelastic theory, Journal of Thermal Stresses 26:713-721,
DOI 10.1080/713855996.

Searches made, all of which failed to return the paper itself:

- author-name sweep for the surname;
- distinctive title-phrase sweep;
- DOI string sweep in its printed form, and the alternative DOI that the bibliography
  does not carry;
- journal-style and "thermal stresses" filename probes;
- full-text phrase sweeps for the title and for the phrase "delay parameters";
- listing of the library's top-level folders and of the two folders whose names suggest
  reference material, which contain index and ledger files rather than article PDFs.

Every object that mentions the paper is one of the author's own index, ledger or review
notes, or a later paper that cites it. None is the 2003 article, so its first page could
not be read and the condition it states cannot be reported. One prior internal review
note in the same library records the abstract as concluding decay for tau_T > tau_q/2
and unstable solutions for tau_T < tau_q/2 with equality untreated (printed p. 714);
that note is a secondary record, was not used for any verdict, and is flagged here only
so that the author knows where the belief may have come from.

Consequence for the manuscript: claim A2 remains unverified, as in batch 001, and the
inequality should either be attributed to a held source that prints it, or rephrased as
a statement about the literature without the specific attribution. Supplying the PDF
(or attaching the archive member that contains it) would settle it in one page read.

## Limits

- Only title blocks, abstracts and first-page equations were read; body derivations and
  numerical results were not checked.
- Two rows (A33, and the Singh/Biswas rows reused from batch 001) rest on abstracts; the
  explicit algebraic replacement of a first-order derivative by D_tau happens in the
  body of those papers and was not read.
- Sur et al. (2025) is written by three authors on the review group's own list; the row
  is recorded for completeness and is not independent evidence.
- No LaTeX build was attempted or claimed, and no review-author script exists or was run.
