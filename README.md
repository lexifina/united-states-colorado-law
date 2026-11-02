# Colorado: law history in git

The Constitution of the State of Colorado and the Colorado Revised Statutes as a git repository: one file per section, one paragraph per line, so `git blame` works line by line. It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law).

**What is in it now**

| Folder | Act | Versions | History |
| --- | --- | ---: | --- |
| `constitution/` | Constitution of the State of Colorado (354 units) | 1 | As printed in the Colorado Revised Statutes 2022, dated 10 August 2022 (oldest version available) |
| `title-01/` | Colorado Revised Statutes, Title 1: Elections (748 sections) | 1 | As printed in the Colorado Revised Statutes 2022, dated 10 August 2022 (oldest version available) |
| `title-02/` | Colorado Revised Statutes, Title 2: Legislative (229 sections) | 1 | As printed in the Colorado Revised Statutes 2022, dated 10 August 2022 (oldest version available) |
| `title-03/` | Colorado Revised Statutes, Title 3: United States (41 sections) | 1 | As printed in the Colorado Revised Statutes 2022, dated 10 August 2022 (oldest version available) |
| `title-04/` | Colorado Revised Statutes, Title 4: Uniform Commercial Code (646 sections) | 1 | As printed in the Colorado Revised Statutes 2022, dated 10 August 2022 (oldest version available) |
| `title-05/` | Colorado Revised Statutes, Title 5: Consumer Credit Code (394 sections) | 1 | As printed in the Colorado Revised Statutes 2022, dated 10 August 2022 (oldest version available) |
| `title-06/` | Colorado Revised Statutes, Title 6: Consumer and Commercial Affairs (331 sections) | 1 | As printed in the Colorado Revised Statutes 2022, dated 10 August 2022 (oldest version available) |
| `title-07/` | Colorado Revised Statutes, Title 7: Corporations and Associations (1047 sections) | 1 | As printed in the Colorado Revised Statutes 2022, dated 10 August 2022 (oldest version available) |
| `title-08/` | Colorado Revised Statutes, Title 8: Labor and Industry (877 sections) | 1 | As printed in the Colorado Revised Statutes 2022, dated 10 August 2022 (oldest version available) |
| `title-09/` | Colorado Revised Statutes, Title 9: Safety - Industrial and Commercial (98 sections) | 1 | As printed in the Colorado Revised Statutes 2022, dated 10 August 2022 (oldest version available) |
| `title-10/` | Colorado Revised Statutes, Title 10: Insurance (1232 sections) | 1 | As printed in the Colorado Revised Statutes 2022, dated 10 August 2022 (oldest version available) |
| `title-11/` | Colorado Revised Statutes, Title 11: Financial Institutions (657 sections) | 1 | As printed in the Colorado Revised Statutes 2022, dated 10 August 2022 (oldest version available) |
| `title-12/` | Colorado Revised Statutes, Title 12: Professions and Occupations (1132 sections) | 1 | As printed in the Colorado Revised Statutes 2022, dated 10 August 2022 (oldest version available) |
| `title-13/` | Colorado Revised Statutes, Title 13: Courts and Court Procedure (1140 sections) | 1 | As printed in the Colorado Revised Statutes 2022, dated 10 August 2022 (oldest version available) |
| `title-14/` | Colorado Revised Statutes, Title 14: Domestic Matters (308 sections) | 1 | As printed in the Colorado Revised Statutes 2022, dated 10 August 2022 (oldest version available) |
| `title-15/` | Colorado Revised Statutes, Title 15: Probate, Trusts, and Fiduciaries (1034 sections) | 1 | As printed in the Colorado Revised Statutes 2022, dated 10 August 2022 (oldest version available) |
| `title-16/` | Colorado Revised Statutes, Title 16: Criminal Proceedings (493 sections) | 1 | As printed in the Colorado Revised Statutes 2022, dated 10 August 2022 (oldest version available) |
| `title-17/` | Colorado Revised Statutes, Title 17: Corrections (248 sections) | 1 | As printed in the Colorado Revised Statutes 2022, dated 10 August 2022 (oldest version available) |
| `title-18/` | Colorado Revised Statutes, Title 18: Criminal Code (850 sections) | 1 | As printed in the Colorado Revised Statutes 2022, dated 10 August 2022 (oldest version available) |
| `title-19/` | Colorado Revised Statutes, Title 19: Children's Code (374 sections) | 1 | As printed in the Colorado Revised Statutes 2022, dated 10 August 2022 (oldest version available) |
| `title-20/` | Colorado Revised Statutes, Title 20: District Attorneys (31 sections) | 1 | As printed in the Colorado Revised Statutes 2022, dated 10 August 2022 (oldest version available) |
| `title-21/` | Colorado Revised Statutes, Title 21: State Public Defender (15 sections) | 1 | As printed in the Colorado Revised Statutes 2022, dated 10 August 2022 (oldest version available) |
| `title-22/` | Colorado Revised Statutes, Title 22: Education (1104 sections) | 1 | As printed in the Colorado Revised Statutes 2022, dated 10 August 2022 (oldest version available) |
| `title-23/` | Colorado Revised Statutes, Title 23: Postsecondary Education (963 sections) | 1 | As printed in the Colorado Revised Statutes 2022, dated 10 August 2022 (oldest version available) |
| `title-24/` | Colorado Revised Statutes, Title 24: Government - State (2866 sections) | 1 | As printed in the Colorado Revised Statutes 2022, dated 10 August 2022 (oldest version available) |
| `title-25/` | Colorado Revised Statutes, Title 25: Public Health and Environment (1473 sections) | 1 | As printed in the Colorado Revised Statutes 2022, dated 10 August 2022 (oldest version available) |
| `title-25-5/` | Colorado Revised Statutes, Title 25.5: Health Care Policy and Financing (382 sections) | 1 | As printed in the Colorado Revised Statutes 2022, dated 10 August 2022 (oldest version available) |

19067 sections and constitutional units. That is all the law this repository holds today: any title not listed above, the session laws and the regulations are not in it yet, and it has no amendment history yet.

## Where the text comes from

The Office of Legislative Legal Services (OLLS) of the Colorado General Assembly publishes the Colorado Revised Statutes as downloadable files. Public.Resource.Org describes the item as "bulk data releases of the Colorado Revised Statutes ... These are edicts of government and are thus the property of the people and not subject to copyright. This law is your law." and marks it with the Public Domain Mark 1.0.

The Constitution of the State of Colorado is taken from the same release (the Colorado part of its constitution file; the Declaration of Independence and the United States Constitution printed with it are not used). Each section is taken from the paragraphs OLLS marks "Statute text": the section number and catchline, and its text. Left out:

- the source note (OLLS's "History" paragraph naming the session laws), and all annotations (editor's notes, cross references, case annotations);
- bracketed "[Editor's note: ...]" lines inside the statute text and catchlines;
- repealed sections (printed with no statute text);
- sections not in force on 10 August 2022 (see Dates), and sections printed in two versions both in force that day. Each title's commit names how many.

No annotation, case note, editor's note or other vendor material is included. The text is a text-layer source (no OCR): every section's letters and digits were compared with a second, independent reading of the same file, with no differences.

## Dates

- Release r83.2023.06 holds the Colorado Revised Statutes 2022: the laws through the 2022 regular session (no 2023 session law is cited in it).
- Each title is one version, dated **10 August 2022**, the day the 2022 session's acts without a safety clause took effect (90 days after the General Assembly adjourned on 11 May 2022), the latest general effective date the edition contains. It is credited to the publisher as "oldest version available".
- A section is left out when it was not yet in force that day: its editor's note gives a later effective date, its source note credits a change with a later effective date (the edition prints such text ahead of time), or a 2022 change takes effect on a governor's proclamation. Of two printed versions, the one "effective until" a later day is used.

## What it does not show

- Any history before the 2022 edition, and any change after it. Earlier OLLS releases (2020 to 2022) are in the same Internet Archive item and may be added as earlier history in a separate build.
- The source notes, annotations and editor's notes; the sections left out as above.
- Nothing here is an official publication or legal advice. For anything that matters, read the official text.

## How it is checked

- Every unit is read back from git on its day and compared with the corpus (`tools/check_repo.py`; results in `REPRODUCE.md`).
- Each source file is identified by its sha256, in `data/versions.json`.

## What "author" means

Each commit is authored by the publisher (the Office of Legislative Legal Services) because this build holds one version of each title, the oldest version available. The committer is always Lexifina.
