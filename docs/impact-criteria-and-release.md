# Impact criteria and working release definition

Status: **DRAFT for team agreement.** Written Nov 25, 2026. It must be committed and frozen **before** any test result is collected. The course requires success criteria to be fixed in advance (`docs/course/project-overview.md`, "Define Success Before You Claim It"). After freezing, any change is logged in `docs/decisions-log.md` with its reason, and the old version stays in git history.

## 1. Declared scope

| | In scope | Out of scope (stated limits) |
|---|---|---|
| Users | Blind and low vision university students who use a screen reader | Braille display output (R3), deafblind users, instructors as users |
| Material | Lecture slide PDFs. Visuals: **labelled diagrams** (Round 1), plus formulas already in the slide | Charts, video, lab equipment, textbooks, handwritten material |
| Requirement | **R1** (learn the information in the visual). **R2** (follow-up questions) only if time allows, as a stretch goal | R3 braille |
| Context | Real course PDFs, including UWindsor ones, read on the student's own device and screen reader | LMS integration, SAS workflow integration |

**Operational definition of the problem.** When a student opens a lecture PDF containing a labelled diagram, the student cannot answer questions about what the diagram shows without sighted help.

## 2. Working release (what must actually run)

The release counts as operationally complete only if all of these hold, on real files and not hand-prepared ones:

1. **Input:** any lecture slide PDF uploaded by a user, not a preset file.
2. **Description step automated:** each slide image goes to a vision model, which returns the existing JSON structure (overview, parts, relationships, LaTeX, tables). No hand-written descriptions.
3. **Output:** one accessible HTML page per lecture. It has headings for each slide, layered descriptions, MathML and real tables, as in the current `make_accessible.py`.
4. **Runs end to end** from one command or a simple web page, without a team member editing anything in between.
5. **Logged cost and time** for every run, written to a CSV.

Not required for the release: a polished UI, accounts or hosting at scale.

## 3. Impact criteria (fixed before testing)

| # | Claim | Measure | Baseline | Success threshold |
|---|---|---|---|---|
| **M1** Accuracy (product works) | Descriptions are correct | Key-fact recall and factual errors, on a test set of **20 labelled-diagram slides** (at least 10 from UWindsor courses). Two team members write a reference list of key facts for each slide **independently and before** seeing AI output. Disagreements are settled by a third member | Original PDFs: 0 key facts available to a screen reader (our scan: 3% of tagged images described, most files untagged) | Mean key-fact recall **≥ 80%**. **≥ 90%** of slides have no critical error (a wrong label, value or relationship that would teach something false) |
| **M2** Comprehension (impact) | Students learn the diagram information on their own | Comprehension questions (4 per slide, written before testing) answered by blind or low vision participants on their own screen reader. Within-subject design: each person gets one slide set as the original PDF and one as our HTML, with the order counterbalanced | Each participant's own score on the original PDF | Score with our HTML **≥ 70%** correct **and** at least **30 percentage points higher** than their original-PDF score. **No sighted help** needed |
| **M3** Independence and time | Access without waiting for a person | Time from receiving the PDF to having an accessible version | Published SAS turnaround of 2–10 business days, with a person in the loop (evidence register) | **≤ 10 minutes** per lecture with no person involved |
| **M4** Cost | Affordable for one institution | API cost per lecture, from the run log | Scribe or GA time per lecture. Estimate in the cost sheet | **≤ CAD $2** per 50-slide lecture |
| **Q1** Quality | Output is usable with a screen reader | Automated check (axe-core: 0 serious violations). Manual run with VoiceOver and NVDA: navigate by heading, read the math and tables | Original PDFs in our scan | All checks pass on every test lecture |

**What counts as the problem being reduced:** M1 and M2 met within the scope above. M3, M4 and Q1 support the claim but cannot replace M2.

## 4. If we cannot reach enough users (the main risk)

The defense is Dec 2–9, and SAS can only reach students in January. These rules are fixed in advance:

- **Target:** 5 participants. Sources: CNIB, SAS advisor contacts, `outreach/study.html` responses, and online blind communities.
- **1–4 participants:** report M2 as case studies, giving each person's result against the threshold. No general claim.
- **0 participants:** M2 is **not met**, and we say so. We claim only M1, M3, M4 and Q1 (the product works), and present the January study with SAS as the validation plan. Sighted team members using a screen reader with the screen off may be reported as a **usability check only, never as impact evidence**.

## 5. Ethics

Testing with people needs a consent form, voluntary participation, no names in the repo, and the raw data kept out of git, as for the SAS interview. **Ask the professor whether this needs research ethics (REB) clearance before the first session.**

## 6. Schedule to the defense

| Date | Output | Owner (proposed) |
|---|---|---|
| Nov 26 | This file agreed and committed (frozen). Test slides chosen. Reference key facts written | All. Aakriti owns the criteria |
| Nov 26–29 | Release items 1–5 built | Abhinav |
| Nov 27–29 | Comprehension questions and consent form. Participants booked | Shrijana |
| Nov 30 | M1, M3, M4 and Q1 measured. Results logged | Khemraj |
| Dec 1–5 | M2 sessions | Shrijana, Abhinav |
| Before defense | Results compared with the thresholds. Decisions logged. Scaling strategy written | All |

## 7. Cost tracking

Every member logs their hours in `docs/daily-log.md`. Hours are valued at a stated student rate, for example CAD $25/h, and the reason for that rate is recorded. API spend comes from the run log. Free resources (university licences, Claude, and SAS staff time for the interview) are listed with who bears their cost.
