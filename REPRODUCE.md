# How this repository was made (Colorado)

This file is written by the build on 2026-11-02, the day the source data was retrieved.

## Sources

| Source | Address | Retrieved | Licence |
| --- | --- | --- | --- |
| Constitution of the State of Colorado (CRS 2022, OLLS bulk release r83.2023.06, ODT), Public.Resource.Org item gov.co.crs.bulk on the Internet Archive | <https://archive.org/download/gov.co.crs.bulk/r83.2023.06/gov.co.crs.constitution.co.odt> | 2026-11-02 | Public Domain Mark 1.0 (item licence); "These are edicts of government and are thus the property of the people and not subject to copyright." (Public.Resource.Org, item description). |
| Colorado Revised Statutes 2022, title 1 (OLLS bulk release r83.2023.06, ODT), Public.Resource.Org item gov.co.crs.bulk on the Internet Archive | <https://archive.org/download/gov.co.crs.bulk/r83.2023.06/gov.co.crs.title.01.odt> | 2026-11-02 | Public Domain Mark 1.0 (item licence); "These are edicts of government and are thus the property of the people and not subject to copyright." (Public.Resource.Org, item description). Statute text is not copyrightable (Georgia v. Public.Resource.Org, 590 U.S. 255 (2020)). |
| Colorado Revised Statutes 2022, title 2 (OLLS bulk release r83.2023.06, ODT), Public.Resource.Org item gov.co.crs.bulk on the Internet Archive | <https://archive.org/download/gov.co.crs.bulk/r83.2023.06/gov.co.crs.title.02.odt> | 2026-11-02 | Public Domain Mark 1.0 (item licence); "These are edicts of government and are thus the property of the people and not subject to copyright." (Public.Resource.Org, item description). Statute text is not copyrightable (Georgia v. Public.Resource.Org, 590 U.S. 255 (2020)). |
| Colorado Revised Statutes 2022, title 3 (OLLS bulk release r83.2023.06, ODT), Public.Resource.Org item gov.co.crs.bulk on the Internet Archive | <https://archive.org/download/gov.co.crs.bulk/r83.2023.06/gov.co.crs.title.03.odt> | 2026-11-02 | Public Domain Mark 1.0 (item licence); "These are edicts of government and are thus the property of the people and not subject to copyright." (Public.Resource.Org, item description). Statute text is not copyrightable (Georgia v. Public.Resource.Org, 590 U.S. 255 (2020)). |
| Colorado Revised Statutes 2022, title 4 (OLLS bulk release r83.2023.06, ODT), Public.Resource.Org item gov.co.crs.bulk on the Internet Archive | <https://archive.org/download/gov.co.crs.bulk/r83.2023.06/gov.co.crs.title.04.odt> | 2026-11-02 | Public Domain Mark 1.0 (item licence); "These are edicts of government and are thus the property of the people and not subject to copyright." (Public.Resource.Org, item description). Statute text is not copyrightable (Georgia v. Public.Resource.Org, 590 U.S. 255 (2020)). |
| Colorado Revised Statutes 2022, title 5 (OLLS bulk release r83.2023.06, ODT), Public.Resource.Org item gov.co.crs.bulk on the Internet Archive | <https://archive.org/download/gov.co.crs.bulk/r83.2023.06/gov.co.crs.title.05.odt> | 2026-11-02 | Public Domain Mark 1.0 (item licence); "These are edicts of government and are thus the property of the people and not subject to copyright." (Public.Resource.Org, item description). Statute text is not copyrightable (Georgia v. Public.Resource.Org, 590 U.S. 255 (2020)). |

Every word of law in this repository comes from these sources. Lexifina reads them and records each act's dated versions, and the laws that made each change, in one corpus file. This repository is built from that file.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| `constitution` | Constitution of the State of Colorado | 1 | 2022-08-10 to 2022-08-10 |
| `title-01` | Colorado Revised Statutes, Title 1: Elections | 1 | 2022-08-10 to 2022-08-10 |
| `title-02` | Colorado Revised Statutes, Title 2: Legislative | 1 | 2022-08-10 to 2022-08-10 |
| `title-03` | Colorado Revised Statutes, Title 3: United States | 1 | 2022-08-10 to 2022-08-10 |
| `title-04` | Colorado Revised Statutes, Title 4: Uniform Commercial Code | 1 | 2022-08-10 to 2022-08-10 |
| `title-05` | Colorado Revised Statutes, Title 5: Consumer Credit Code | 1 | 2022-08-10 to 2022-08-10 |

The build made 6 commits:

| Commits | Kind |
| ---: | --- |
| 6 | first version of an act |
| 0 | one law on its in-force day |
| 0 | changes no amendment note explains, credited to the publisher |

Other counts:
- 0 commits on the branch `future`: laws not yet in force on 2026-11-02.
- 0 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 0 laws in the record.
- 6 tags.

## Dates

Each commit is dated at noon (America/Denver) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: Colo. Const. art. V, sec. 19: an act without a safety clause takes effect 90 days after the General Assembly adjourns; in 2022 that day was 10 August 2022. https://archive.org/details/gov.co.crs.bulk

## How the history is built

`tools/build.py` turns the corpus into this history in one pass: one commit per law, on the day it took effect. The same corpus always gives the same commit hashes. `tools/check_repo.py` reads every version back from git and compares it with the corpus. `tools/on.py` shows the law as it stood on any date. The corpus format is described in `tools/SCHEMA.md`.

- Corpus: sha256 `407d62bb8884662da56579dcbf6755a3132e7f908acf9161ae113d387899999f` (4244633 bytes).
- Builder blob hashes (`git hash-object`): `build.py` `a4faa25af85facb64b956b372f6b528aafdd7ec1`, `check.py` `3d00541d258745461ab52b1b0cb4e1716a27a95d`, `on.py` `644a6c0857fbcc72562032b58d57aa113fee0641`.
- Python 3.12.10; git version 2.46.0.windows.1.

## Checks

6 versions of 6 acts read back from git on the day each took effect and on the day before: 0 mismatches. Trailers: 0 commits whose trailers git cannot parse. Health: 0 merge commits on main, 0 commit dates that go backwards, 0 commits dated after the build.

No second build of this corpus has been compared yet.

## Decisions made by hand

- The Colorado Revised Statutes are built one corpus.d part per title; see each part.
- Colorado Constitution: one version, as printed in the CRS 2022, dated 2022-08-10; units not in force that day are left out; repealed sections (no text) are left out.
- C.R.S. title 1: one version, the Colorado Revised Statutes 2022 as released by OLLS (release r83.2023.06), dated 2022-08-10, the general effective date of the 2022 session's acts; sections not in force on that day are left out.
- C.R.S. title 2: one version, the Colorado Revised Statutes 2022 as released by OLLS (release r83.2023.06), dated 2022-08-10, the general effective date of the 2022 session's acts; sections not in force on that day are left out.
- C.R.S. title 3: one version, the Colorado Revised Statutes 2022 as released by OLLS (release r83.2023.06), dated 2022-08-10, the general effective date of the 2022 session's acts; sections not in force on that day are left out.
- C.R.S. title 4: one version, the Colorado Revised Statutes 2022 as released by OLLS (release r83.2023.06), dated 2022-08-10, the general effective date of the 2022 session's acts; sections not in force on that day are left out.
- C.R.S. title 5: one version, the Colorado Revised Statutes 2022 as released by OLLS (release r83.2023.06), dated 2022-08-10, the general effective date of the 2022 session's acts; sections not in force on that day are left out.

## What AI did and did not do

The scripts that read the sources and build this repository were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- none
- none
- none
- none
- none
- none
- none
