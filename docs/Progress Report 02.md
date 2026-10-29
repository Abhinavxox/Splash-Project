**SPLASH Team Progress Report 02**

COMP 8117 Expert Review 02

Team members Abhinav Pandey, Shrijana Karki, Aakriti Mainali and Khemraj Adhikari

Date October 29, 2026

Repository https://github.com/Abhinavxox/Splash-Project

**Executive summary**

Since Expert Review 01 we focused on one question. Is the problem real and how big is it? We wrote a research plan, collected 60 sources across seven kinds of evidence and scanned 27 real lecture PDFs ourselves. The evidence confirms that lecture material loses most of its meaning for screen reader users. It does not yet support our earlier claim that students wait a long time, and we still have almost no first hand voices of blind students.

We are behind the plan we set in Review 01. We have not contacted Student Accessibility Services or instructors, we have not run Adobe as a baseline and the automatic description step is not built. We chose to secure the problem evidence first because the professor's main concern was evidence, and building the solution before proving the problem would repeat the mistake of our first project.

**Development progress**

| Planned in Review 01 | Status | Evidence |
|---|---|---|
| Contact Student Accessibility Services and instructors | Not started | none |
| Collect real lecture files | Done differently. Public lectures instead of instructor files | 27 PDFs from 7 university courses, list in research/pdf-scan |
| Adobe auto tagging baseline | Not started | none |
| Research existing work | Done and extended | 60 sources in research/evidence-register.md |
| Automate the description step | Not started | prototype still uses hand written descriptions |
| Screen reader recording with Guidepup | Not started | none |
| Decide team roles | Not done | none |

New work that was not in the plan

- A research plan that lists seven claims we must prove and where to look for each, in research/problem-evidence-plan.md
- A scan of 27 public lecture PDFs with 1852 pages, using scripts that anyone can rerun, in research/pdf-scan

**What the evidence shows**

Our own scan gave the strongest result. 12 of 27 lecture files have no tags at all. 376 pages carry their main content in images. Of 7293 tagged images only 237 have a description, about 3 percent. The 27 files contain only 6 formula tags and none has a description.

Published research agrees. A study of about 20,000 scholarly PDFs found fewer than 3.2 percent pass basic accessibility checks, and another found 2.4 percent of 11,397.

The problem has real consequences. In 2025 blind students and the NFB sued West Virginia University over course PDFs that screen readers could not read, and Oregon State University settled a similar claim for 475,000 dollars in 2026. Ontario law (AODA section 15) requires colleges and universities to provide accessible course materials, and the US ADA Title II rule now sets compliance dates in 2027 and 2028.

Every tool we reviewed, including Adobe, CommonLook, Equidox and Mathpix, still needs a person for reading order, tables, descriptions and math.

Some evidence goes against us. Published turnaround times are shorter than we assumed. Stanford converts lecture slides in at least 2 business days, the University of the Fraser Valley takes 5 and Maryland 10. The WebAIM screen reader survey says nothing about documents. Most PDF studies measure research papers, not lecture slides.

**Verdict**

The problem is real and measurable. Lecture PDFs routinely lose their formulas, tables and diagrams for screen reader users, institutions are legally required to fix this, and the tools that exist still depend on manual work. This part of our case is well supported.

The claim that students wait a long time is not supported yet. The published waits are days, not weeks, and they apply to universities with dedicated teams. We now frame the problem as quality and completeness. Even after conversion, formulas and diagrams are the hardest parts and depend on skilled people. We still need first hand evidence from blind students and from our own university before we can say how much this matters to them.

We therefore keep the project and adjust the claim, not the direction.

**Planning drift and causes**

We planned about four outcomes for weeks 6 and 7 and completed one, the research, while adding the PDF scan.

The causes were these. Reading week and exams reduced our time. Roles were left undecided, so outreach had no owner. And after the professor's feedback we decided problem evidence had to come before building, which moved the description step later.

The consequence is that user sessions and the full before and after comparison now have less time. Outreach replies are still unknown, so the user evidence is the biggest risk.

**Corrective actions and revised plan**

- Send emails to Student Accessibility Services, two or three instructors and CNIB this week, and post a short survey for screen reader users. Owner to be set when roles are decided.
- Decide roles at the next team meeting and record them in the decisions log.
- Keep the public lecture set as our test data instead of waiting for instructor files.
- Change claim 3 from long waits to quality and completeness of conversions.

| Week | Goal |
|---|---|
| 8 (Nov 5 to 11) | Outreach replies collected, roles set, automatic description step built, Adobe or free checker baseline on the test set |
| 9 (Nov 12 to 18) | Screen reader recording with Guidepup, accuracy check of descriptions, question test before and after |
| 10 (Nov 19 to 25) | User sessions if possible, fix biggest errors, final measurement |
| 11 to 12 | Analysis, reports and defense |

**Quality management**

Our scan scripts are in the repository and produce the same numbers when rerun. Each source in the register links to where it came from. We marked each source as strong, medium or weak and kept sources that contradict us. We have not yet tested the prototype beyond three slides and have no automated tests. Adding a test that runs the pipeline on every change is part of week 8.

**Risk management**

| Risk from Review 01 | Now |
|---|---|
| Accessibility office does not reply | Still open because we have not contacted them yet |
| Few real users available | Has become our main risk since we found almost no first hand user voices |
| AI writes wrong descriptions | Still open, to be measured in week 9 |
| Scope too big | Reduced by focusing on evidence first |

New risk. Some figures we found, such as the ADA compliance dates, differ between sources. We will check each one at the official source before citing it.

**Engineering process and team**

We did not keep the weekly rhythm we planned. Work happened in bursts on October 24 and 25 and on October 29. The decisions log and the repository worked well and gave us a clear record. Leaving roles open slowed us down more than expected.

**Lessons learned and next steps**

Measuring the problem ourselves gave stronger evidence than any single source. Writing down the claims first showed us exactly which ones were weak. Our next priorities are outreach, roles and the automatic description step.

Questions for the teaching team. Is reframing claim 3 from waiting time to conversion quality acceptable? How much first hand user evidence is enough if blind students are hard to reach?

**Supporting artifacts**

- research/problem-evidence-plan.md
- research/evidence-register.md with 60 sources
- research/pdf-scan with scripts and results
- research/candidates with rough notes for each source
- docs/decisions-log.md
- Progress Report 01 as the baseline

**Use of AI tools**

We used Claude to help search for and summarise sources, write the scan scripts and draft this report. The team remains responsible for every claim, and we will confirm key figures at their original source before the final report.
