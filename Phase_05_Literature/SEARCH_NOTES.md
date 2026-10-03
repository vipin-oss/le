# Phase 5 — reference verification notes (2026-10-03)

How verification was done here. The sandbox shell has no network, but the agent's web fetch does, so the Crossref
REST API (`api.crossref.org/works?query.bibliographic=…&select=DOI,title,author,issued,container-title,volume,page`)
was queried directly and the raw JSON responses were read. This updates the environment note in the programme
state, which records the API as unreachable from the code's side: it is unreachable from the shell, reachable
through the fetch path, and every claim below rests on the returned record, not on recollection.

Project rule applied throughout: a reference is added only if it can be verified to a record that carries the
bibliographic details used; no DOI is ever invented.

## A13 — the classical papers named in the text

**Carlo Cattaneo, 1948.** Query: `Cattaneo equazione del calore tipo iperbolico 1948` → the five nearest
records were Pascucci's book chapter (2008), Dellavalle (1975), Picone (1910), a UNITEXT chapter, and
`10.1007/978-3-642-11051-1_5` — "Sulla Conduzione Del Calore", C. Cattaneo, in *Some Aspects of Diffusion
Theory* (Springer, 2011), page 485. The last is a Springer chapter carrying Cattaneo's title, but it is a
2011 reprint of one page, and nothing in the returned metadata identifies it as the 1948 paper or gives its
pagination; citing it as "Cattaneo (1948)" would misdate the source and citing it as the 2011 chapter would
not be the primary paper.

Secondary sources disagree on the details, which is precisely why the primary is not added without a record:
the Treccani *Dizionario Biografico* (vol. 34, 1988) gives the 1948 paper as *Sulla conduzione del calore*,
Atti del Seminario matematico e fisico dell'Università di Modena, III [1948–49]; the literature variously
cites a Milan *Rendiconti* venue and pages 29–36. Wikipedia states the model was developed in 1948 and that
the relation is now called the Maxwell–Cattaneo law. A query for an English translation in a DOI-bearing
journal (`Cattaneo Sulla conduzione del calore translation Journal of Thermal Stresses`) returned no
translation record.

**Pierre Vernotte, 1958.** Query: `Vernotte Les paradoxes de la chaleur non stationnaire` → nothing related
in Crossref (the returned items were a 2008 C. R. Mathématique note on a heat-kernel bound, theses, and
unrelated 1998/2021 items). The venue where the paradoxes paper appeared is not DOI-registered, so no record
with verifiable pagination could be retrieved from here.

**Decision (rule-conformant).** Neither original is added to the list. The manuscript already cites the
DOI-verified Lord–Shulman paper [11] (1967) and the anisotropic extension with its uniqueness theorem [12] at
the point where the finite-wave-speed framework is introduced, and it attributes the law by name in the body,
which is what a reader needs to find the origin. The general theory that actually carries the restriction the
paper relies on is now cited (see below). What remains is a library task, not a computing task: if the authors
can obtain the Modena (or Milan) 1948 pagination and the 1958 Revue de Mécanique Appliquée pages from the
originals or a catalogue record, two entries can be appended and the two mentions in Sections 1.2/1.3 and 2.2
carry citations. This is recorded as open item P5-1 rather than quietly resolved.

## B19 — methodological and constitutive-theory references

* Richardson extrapolation: **already cited.** Section 5 attributes the extrapolation to Richardson and Gaunt
  [52], which is in the DOI-verified list, so no addition was needed (the audit's own suspicion that the method
  carried no reference was checked and found not to hold).
* Passivity / positive-real restriction: **one addition.** `Gurtin Pipkin general theory heat conduction memory`
  → exact hit: M. E. Gurtin and A. C. Pipkin, *A general theory of heat conduction with finite wave speeds*,
  Archive for Rational Mechanics and Analysis **31**(2), 113–126 (1968), DOI `10.1007/BF00281373`, returned with
  title, both authors, journal, volume and pages by Crossref. Added as [55] and cited at the two places where the
  restriction is used (manuscript Section 2.2, and the companion's kernel section by pointer). The wording states
  what the source does and does not say: the restriction there is stated for a memory kernel, and τ > 0 is its
  instance here.
* A second methodological candidate was verified and deliberately **not** added: Ferziger, Peri ċ,
  *Computational Methods for Fluid Dynamics*, Springer, DOI `10.1007/978-3-642-56026-2` (2002 printing, record
  confirmed) — it exists and is relevant to apparent-order/Richardson practice, but the extrapolation already
  has its citation at [52] and adding a textbook for the same statement is padding. B19 asked for at most two
  additions; one was made.

## B21 — claim ↔ citation matrix

Produced by `verification/lit_B_claims_matrix.py` (mechanical, from the generated Markdown and the verification
levels in `01_Literature/REFERENCES_VERIFIED.json`): 139 citation instances across the manuscript, 55 of 55
list entries cited (no orphan entry), and **0** sentences in the framing or theory sections that assert with a
strong verb on top of a citation whose record here is metadata-only. The two levels present are therefore
stated as such in the ledger rather than being described as "all sources read": 23 entries are
metadata-verified from 2026-10-01, 31 from 2026-10-02, 1 from today; the only works whose content was actually
read in this environment remain Klimm et al. (open access) and the Adachi et al. values, as the literature
README has always said.
