# R3f Crossref mismatch and title checks

Rows with Crossref metadata that did not pass all mapped identity checks.

- `ChadwickSneddon1958` DOI=10.1016/0022-5096(58)90027-9; author mismatch; base title=(not supplied); Crossref title=Plane waves in an elastic solid conducting heat
- `HetnarskiIgnaczak1999` DOI=10.1080/014957399280832; author mismatch; base title=(not supplied); Crossref title=GENERALIZED THERMOELASTICITY
- `Gorenflo1997` DOI=10.1007/978-3-7091-2664-6_5; venue mismatch; base title=Fractional calculus: integral and differential equations of fractional calculus; Crossref title=Fractional Calculus

## R3g supervisor arbitration (Crossref rules unchanged)

The original registry outcomes remain recorded as `MISMATCH` in `CROSSREF_R3F_VERIFY.csv`. Following supervisor arbitration against the supplied PDFs and printed first pages, the Chadwick–Sneddon and Gorenflo records are separately designated `VERIFIED-BY-ARBITRATION`. The prior printed-page arbitration for the 1999 Hetnarski–Ignaczak record is withdrawn: the held paper is the distinct 2000 IJSS article, not the 1999 JTS item. No Crossref matching threshold or verification rule was changed.

- `ChadwickSneddon1958`, DOI `10.1016/0022-5096(58)90027-9` — `VERIFIED-BY-ARBITRATION`. The printed first page names P. Chadwick and I. N. Sneddon. Crossref's `Snedon` is a spelling typo; the DOI, title, journal, year, volume, and pages identify the printed paper. The bibliography uses `Sneddon`.
- `HetnarskiIgnaczak1999`, DOI `10.1080/014957399280832` — Crossref metadata identifies the 1999 *Journal of Thermal Stresses* article *Generalized thermoelasticity*, but primary-source identity is **not verified**. The previously associated printed page belongs to the distinct 2000 *International Journal of Solids and Structures* article *Nonclassical dynamical thermoelasticity* (now keyed `HetnarskiIgnaczak2000`). Keep the 1999 record metadata-only and do not use the 2000 source to support the 1999 survey claims.
- `Gorenflo1997`, DOI `10.1007/978-3-7091-2664-6_5` — `VERIFIED-BY-ARBITRATION`. The printed chapter title is “Fractional calculus: integral and differential equations of fractional order,” in *Fractals and Fractional Calculus in Continuum Mechanics*, CISM Courses and Lectures 378, Springer, Wien, pp. 223–276. The earlier manuscript title “...of fractional calculus” was incorrect; the bibliography now follows the printed chapter/volume details and retains the Crossref DOI.
