# AUTHOR INPUT FORM — 5 answers and the paper is ready to submit

Sabse aasan tarika: is file ke blanks bhar do, **ya** bas chat me in 5 cheezon ka jawab bhej do
(`1) ... 2) ...`) — main manuscript `.md`, `.tex`, `.docx`, cover letter aur checklist me ye values
khud daal dunga, aur dobara compile-ready package bana dunga. Ye 5 ke al kuch bhi bache hue
submission blocker nahi hai.

Answer format: English me, plain text. Jo applicable na ho us jagah `none` likh dena — khaali mat
chhorna, kyunki journal ko har statement chahiye (blank = desk rejection risk).

---

## 1) Authors — naam, order, affiliation, e-mail, ORCID

Required: har author ka full name, unki order (jis tarah print hona chahiye), affiliation (department,
institution, city, country), corresponding author ka e-mail, aur ORCID iD (if any).

```
Author 1: <Full name> | <Dept, Institution, City, Country> | <email> | <ORCID or none>   [corresponding? yes/no]
Author 2: <Full name> | <Dept, Institution, City, Country> | <email or same> | <ORCID or none>
Author 3: ...
```

Example (format ke liye, nakal mat karna):

```
Author 1: Vipin Kumar | Department of Mechanical Engineering, XYZ Institute of Technology,
Kaithal, Haryana 132001, India | vipin.kumar@xyz.edu.in | 0000-0002-1825-0097   [corresponding: yes]
Author 2: Anil Sharma | Department of Physics, ABC University, Panipat, India | none
```

## 2) CRediT — kisne kya kiya (per author, ek line each)

Roles the journal recognises: Conceptualization, Methodology, Software, Validation, Formal analysis,
Investigation, Data curation, Writing – original draft, Writing – review & editing, Visualization,
Supervision, Project administration, Funding acquisition.

```
Vipin Kumar: Conceptualization, Methodology, Software, Validation, Writing – original draft
Anil Sharma: Formal analysis, Writing – review & editing, Supervision
```

(Beta version already in the manuscript's Declarations is a placeholder — is list se replace ho jaayega.)

## 3) Competing interest — ek line

Either exactly this:

```
The authors declare that they have no known competing financial interests or personal relationships
that could have appeared to influence the work reported in this paper.
```

…ya apna interest likh do. Answer: `standard` (upar wala line use kar lo) ya `<aap ka text>`.

## 4) Funding — grant numbers ya "no funding"

```
Funding: <"none"  OR  "This work was supported by the XYZ Scheme (grant ABC-1234)." OR "No funding was received.">
Also needed: <agar kisi agency ne compute/data diya to Acknowledgements me line>   (else "none")
```

## 5) Data & code deposit — repository URL + DOI, aur licence

Data aur code ka poora package (603 files, 43.65 MB, sha256 `de9cfb1a4369c444…`) download-ready hai;
usko Zenodo ya Figshare pe daalne ke baad mujhe do:

```
Repository URL: <https://doi.org/10.xxxx/yyyy or https://github.com/...>
DOI:            <10.xxxx/yyyy  (or "not yet deposited" - tab main placeholder chhod dunga)>
Licence:        <CC BY 4.0 / CC0 / MIT for code / GPL / "same as repository default">
Version label:  <e.g. v1.0-submission-2026-10-03>
```

Ya: bolo to main tumhare liye **GitHub Release** bana dunga (public repo already hai, isliye koi naya
data expose nahi hoga) — usse ek permanent download link bhi mil jaata hai jo sandbox resets se nahi
taoota, aur phir Zenodo/Figshare us release ko hi DOI de sakta hai.

---

## Optional but useful (submit karne se pehle journal maangta hai)

```
Suggested reviewers:   <name, institution, e-mail> x 2-3   (or "none")
Opposed reviewers:     <name + reason>                       (or "none")
Editor's name:         <IJHMT editor, if you know>           (or "unknown")
Run-as-title / article type: <Research paper>                (default rakha hai)
Word-count / abstract limit check: <already within limits - 249 words abstract, 5 highlights>
```

## Aur do cheezein jo sirf aap kar sakte ho (main kar nahi sakta)

1. **LaTeX compile** — is environment me TeX engine nahi hai, isliye `.tex` kabhi compile nahi hua;
   static gates sab green hain. Apne machine pe: `bash PAPER_PROJECT/../Phase_10_Submission_Package/compile_check.sh`
   (ya 4 commands: pdflatex → bibtex → pdflatex → pdflatex). Warning aaye to log bhej dena, main fix kar dunga.
2. **AI declaration padh lo** (manuscript me References se pehle) — jo likha hai wahi actually hua ho,
   usme confirm karna author ka kaam hai; galat disclosure Ethics issue ban jaata hai.
