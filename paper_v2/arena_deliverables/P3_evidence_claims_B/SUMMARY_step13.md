# Step 13 — the author-supplied sources read against the claims they free

Date: 2026-11-01. Scope: evidence only. No `.tex` file was touched and nothing in `scripts/` was run.
This step does not change the request list (39 works); it settles what the 40 already-supplied
sources actually say about the 40 claims those works were blocking.

## What was done

Every page of each supplied source was opened, and the sentence that bears on the claim was read
on a page and copied word for word with that page's number. Page 1 alone was not accepted as proof
for a claim about a specific model, equation or result; in those cases the text inside the paper was
searched and the page carrying the relevant sentence is the one cited. Nothing was paraphrased into a
quote, and no quote was reconstructed from memory.

Result: `source_reading_2026-11-01.csv`, one row per claim, 40 rows.
Checker: `check_pdfs_needed.py` — `PASS all checks (needed=1, library=34, findings=3)`, exit 0.

## Verdicts

| verdict | rows | meaning |
|---|---|---|
| SUPPORTED | 31 | the cited work says what the sentence attributes to it; quote + page recorded |
| PARTLY SUPPORTED | 6 | the work is in the right family but does not carry the specific statement |
| NOT SUPPORTED | 2 | the work is real but does not contain the attributed claim |
| NOT READ | 1 | copy held, no text could be extracted, verdict withheld |

## The six findings the author should look at

1. **CR161 — NOT SUPPORTED.** The sentence puts "stability and decay results for Green–Naghdi type III"
   on Suh and Burger (1998). That paper is a spectral study of the Lord–Shulman and Green–Lindsay
   models; Green–Naghdi type III does not appear in it. A different citation is needed, or the
   sentence must be relocated.
2. **CR047 — NOT SUPPORTED.** Luchko (2010) is a uniqueness/existence study of the time-fractional
   diffusion problem. It does not assert the α < 1 stretched Mittag-Leffler decay with heavy tails that the
   sentence cites it for; the claim needs a source that actually states the asymptotic form.
3. **CR128 — PARTLY SUPPORTED.** Müller (1967) removes the assumption that the entropy flux equals
   heat flux over temperature and makes the entropy flux an independent constitutive quantity
   (eq. 2.9). It does not put the heat flux `q_i` into the state space of the entropy; that is the
   EIT step of Jou et al. and Müller–Ruggeri, which are cited in the same sentence. The sentence is
   safe as long as the `q_i` part is attached to those two, not to Müller (1967).
4. **CR075, CR073, CR072 — PARTLY SUPPORTED.** These three sit in the list of memory-dependent-derivative
   (MDD) versions of the lag models, but all three are fractional-order models (new Caputo definition,
   fractional order, fractional two-relaxation-time theory). They replace the first-order derivative by a
   fractional derivative, not by `D_τ`. The list mixes two mechanisms; either split it or say
   "fractional and memory-dependent versions".
5. **CR044 — PARTLY SUPPORTED.** The attribution itself is sound (the paper derives the theory from a
   fractional-order heat transport law), but the equation form printed in the sentence was not read off a
   page of this copy, so no quote backs it. Worth one line of confirmation while the file is at hand.
6. **CR195 — NOT READ.** Polizzotto (2001) is held as a copy whose text layer is glyph-encoded on all
   22 pages; not one word can be extracted. The claim ("nonlocal variational principles are discussed by
   Polizzotto (2001)") stays unverified until a text-readable copy arrives. Recorded as SOURCE NOT
   AVAILABLE in spirit, not as supported.

Two smaller notes, both recorded in the CSV: McNelly et al. (1970) describe **incipient** second sound,
not fully developed second sound, so the word "observed" should keep that qualifier; and the
Joseph–Preziosi item cited as 1990 is the addendum to the 1989 review, so the volume/year pair in the
bibliography should be checked once.

## What this does not do

It does not change the 39-work list, does not touch the 667-row and 63-row claim-check batches, and does
not edit the manuscript. It only records, claim by claim, what the supplied sources say and on which page.
