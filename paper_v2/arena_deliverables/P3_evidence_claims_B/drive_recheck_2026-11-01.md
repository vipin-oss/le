# Drive swept again, 2026-11-01: is any work still on the request list already in Drive?

Question put to this pass: the request list is only worth sending if nothing on it is already sitting in
Drive. So all 39 works that were on the list at the start of the sweep were searched against the Drive
file index, and every file that came back was opened and identified before being accepted or rejected.

Verdict: **one** of the 39 was already in Drive. It has been struck off, the list now stands at **38 works
(39 blocked claims)**, and the work is recorded in `drive_held_sources_2026-11-01.csv` like every other
work that has been found in Drive before.

## The one find

**Kumar, Devi and Sharma 2017**, cited as "Appl. Appl. Math. Int. J." with no title in the register and no
DOI to match on. Held as a PDF; its cover page was read and it prints:

> Kumar, Rajneesh; Devi, Shaloo; and Sharma, Veena (2017). Damping in microscale modified couple stress
> thermoelastic circular Kirchhoff plate resonators, Applications and Applied Mathematics: An
> International Journal (AAM), Vol. 12, Iss. 2, Article 19.

That is the cited work, and the article carries **no DOI**, which is exactly why the earlier
name-plus-DOI passes walked past it. The claim it frees (CR144, "generalized and nonlocal corrections to
the classical thermoelastic-damping result ... for plates and beams") now has its source in hand.

## How the sweep was run

Name-index queries over the whole Drive, eight of them, covering every surname on the list and every
distinctive title word of the works that a surname query could miss (a book with no article title, a paper
whose file is named after its subject):

| query group | files returned |
|---|---|
| Podlubny, Abouelregal, Ackerman, Alzahrani, Askes, Bem, Biswas | 13 |
| Boley, Born, Brorson, Caputo, Carlson, Cattaneo, Chandrasekharaiah | 2 |
| Chirita, Ciarletta, Danilovskaya, de Hoog, Dubner, Durbin | 0 |
| Eringen, Ezzat, Nowacki, Tzou, Vernotte | 24 |
| Kumar, Singh, Wang | 86 |
| Tomar, von Karman, lagging, Podlubny | 2 |
| Das, Thermal Stresses, Thermoelasticity | 22 |
| phase lag, Complete solutions, Domain of influence, Microcontinuum | 24 |
| Rayleigh, Temperature-rate, fractional differential equations | 18 |

Every file that could plausibly have been one of the 39 was then named exactly and its first page read.
Twelve exact-name hits came back, covering eleven distinct files (two pairs were duplicate copies):

| file as it sits in Drive | what the first page actually is | one of the 39? |
|---|---|---|
| Kumar2017 | AAM 12(2) Art. 19, Kumar-Devi-Sharma, couple-stress plate damping | **YES - the find above** |
| Kumar2017, second copy | same article, duplicate | yes, same work |
| Kumar-2017 (Coupled Systems Mechanics) | Kumar and Sharma, fractional energy ratios at an elastic-piezothermoelastic boundary | no |
| abouelregal2020 | higher-order time-derivatives and three-phase lags, Multidiscipline Modeling in Materials and Structures | no - the list wants the four-phase-lag EPJ Plus paper and the Sci Rep paper |
| Biswas 2020, state-space approach | MDD solved by a state-space method | no - the list wants the surface-wave paper in Acta Mechanica 232 |
| singh2020 | Singh and Gupta, wave reflection at a flexoelectric half-space, Mechanics Based Design | no - the list wants Singh, Sarkar and Pal in J. Heat Transfer 142 |
| chandrasekharaiah1998 | "Hyperbolic thermoelasticity: a review of recent literature" | no - the list wants the 1984 and 1997 papers |
| chandrasekharaiah1988 | Acta Mechanica 71, 39-49, generalized theory for piezoelectric media | no |
| wang2020 (ZAMM) | thermo-electric response in 2D hexagonal quasicrystals | no |
| wang2020 (Computational Mechanics) | phase-field model of thermo-elastic brittle fracture | no |

The rest of the hits were identified from their own titles and are other papers by the same authors:
Megahid/Abouelregal/Sedighi 2023 (bioheat), Abouelregal/Ahmad/Yao 2020, Tiwari/Kumar/Abouelregal 2021,
Biswas 2018 and 2024, Biswas-Mukhopadhyay 2018, the Kaur/Lata/Singh papers, Kumar-Chawla 2013,
Kumar-Sharma 2017 and 2021, Kumar et al. 2018/2021/2022, Singh-Gupta 2020 and 2023, Singh-Guha 2021,
Guha/Singh/Das 2021, Wang and Li 2011 and their part (I) of 2021, Tzou 1995 and Tzou-Bao 1995, Eringen
1966/1972/1978, Ezzat 2011, 2015, 2016 (thermoelectric MHD), 2019 and 2020, Nowacki's absence noted below.
None of these is a work on the list.

## What is simply not there

No file at all came back for: Podlubny 1999, Ackerman et al. 1966, Alzahrani and Abbas 2020, Askes and
Aifantis 2006 and 2011, Bem 1982 and 1983, Boley and Weiner 1960, Born and von Karman 1912, Brorson et
al. 1987, Caputo 1967, Carlson 1972, Cattaneo 1948, Chirita/Ciarletta/Tibullo 2017, Ciarletta 1999,
Danilovskaya 1950, Das et al. 2008, de Hoog/Knight/Stokes, Dubner and Abate 1968, Durbin 1974, Eringen
1999, Nowacki 1975, Vernotte 1958, Kumar and Tomar 2024, Kumar/Gupta/Pathania/Barak 2025, and the 2025
Wang and Li part (IV).

## The limit of a name search, stated plainly

A file whose name carries neither an author surname nor a title word - a publisher's PII number, a
serial number, an internal batch code - cannot be caught by this method. Those files are covered two
other ways: the library inventory was built by opening every file in the archive bundles, and each of the
three uploads the author made today was read page by page before anything was accepted. Nothing in this
record comes from a file name alone: every acceptance and every rejection above is based on a page that
was read.
