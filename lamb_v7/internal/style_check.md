# v7 style and source check

Run on the three masters after the depth pass. No LaTeX engine here, so this is a
source-level check: environment balance, math balance, citation coverage, forbidden
vocabulary, and line length in displayed equations.

deliver/v7/Anu/Lamb_Anu.tex: 821 lines, 48038 bytes, 36 worked blocks, 15 display blocks, 14 citations, 0 em-dashes
deliver/v7/Neha/Lamb_Neha.tex: 836 lines, 48175 bytes, 36 worked blocks, 16 display blocks, 20 citations, 0 em-dashes
deliver/v7/Sumit/Lamb_Sumit.tex: 1168 lines, 69305 bytes, 42 worked blocks, 22 display blocks, 19 citations, 0 em-dashes

Checks: every begin/end pair balanced; $ even in every file; every citation key present
in the matching bib and no unused bib entry; no use of the forbidden list (delve,
moreover, furthermore, tapestry, landscape, leverage, robust, seamless, pivotal, realm,
audit, internal log, earlier version); no displayed line longer than 90 characters;
no bold in running text; no sentence opening repeated more than three times running.
Not checkable here without a compile: page counts, overfull boxes, both-flag builds.
