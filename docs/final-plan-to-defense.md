# Final plan to the defense

Written Nov 25, 2026, at the end of production week 10. The defense window is **Dec 2–9**, and our slot is not yet confirmed. **We plan as if the defense is Dec 2**, so everything is finished by Tue Dec 1 at 11 pm. Any days after that are buffer for more user sessions.

The required content comes from `docs/course/project-overview.md` (Final Defense, 7 points) and `docs/course/expert-review-03.md`. The success criteria are in `docs/impact-criteria-and-release.md`.

## Rules for these 7 days

- Every task leaves a file and a row in `docs/daily-log.md`, **committed from your own GitHub account the same day.** Grades drop when individual contribution is not visible.
- Every decision goes in `docs/decisions-log.md` with its evidence.
- Log your hours every day, in the `Notes` column as `h=2.5`. That is the cost data.
- Stand-up: 15 minutes, 9:30 pm daily on Teams. Each person says what they did, what is blocked, and what they do next. Abhinav writes 3 lines of minutes in the log.
- Blocked for more than 2 hours: post in the group chat right away. Don't wait for the stand-up.
- Raw interview and test data never goes into git, because the repo is public.

## Owners for the end phase

| Person | Owns until the defense | Defense section they present |
|---|---|---|
| **Abhinav** (lead) | Working release (code), cost and run log, decisions log, merging and integration, final slide deck | Points 2 and 3: intervention, then the live demo |
| **Shrijana** | Participants, consent, comprehension questions, M2 sessions, the student-voice evidence | Point 5: does it remove the problem (M2 results) |
| **Aakriti** | Impact criteria (frozen), requirements traceability, the M1 reference key facts, the results table, the team rubric | Points 1 and 7: problem is real, evidence-based reasoning |
| **Khemraj** | Hypotheses status, risks and limits, the Q1 quality checks, M3 and M4 measurements, the scaling strategy | Points 4 and 6: method, quality, resources, impact and scale |

## Day-by-day

### Wed Nov 26: freeze and prepare

| Who | Task | Output | Due |
|---|---|---|---|
| All | 30-min meeting at noon: read the impact criteria file together, agree on the numbers, then freeze | Decision row "Criteria frozen". Commit | 1 pm |
| Abhinav | Email the professor: (1) is REB clearance needed for user sessions, (2) confirm the defense slot | Sent. Note in log | 2 pm |
| Abhinav | Call or email CNIB Windsor and the SAS advisor: ask for 3–5 screen-reader users for a 30-min session, Dec 1–5 | `outreach/emails.md` updated | 5 pm |
| Aakriti | Choose 20 labelled-diagram slides: at least 10 from UWindsor course PDFs (ask classmates and instructors for public lecture PDFs), the rest from public courses | `research/test-set/slides.md` (file, page, source) | 9 pm |
| Shrijana | Write the consent form and session script (plain language, works with a screen reader) | `research/study/consent.md`, `research/study/session-script.md` | 9 pm |
| Khemraj | Write the anonymized SAS interview summary. Update question table A–K (A confirmed, K partly rejected) | `research/interviews/2026-11-24-sas.md` | 9 pm |
| Khemraj | Bring the decisions log up to date: Nov 13, ER03, Nov 24, and today's decisions | `docs/decisions-log.md` | 11 pm |
| All | **Back-fill the daily log from Sep 17**: one row per real past task, with hours, using git history, chats and reports. Mark these rows `backfilled` | `docs/daily-log.md` | 11 pm |

### Thu Nov 27: build and set the baseline

| Who | Task | Output | Due |
|---|---|---|---|
| Abhinav | Release items 1–2: accept any PDF, render pages, send each slide image to the vision model, get back the JSON (overview, parts, relationships, LaTeX, tables) | `prototype/` code. Commit | 9 pm |
| Aakriti + Khemraj | Each writes the **reference key facts** for all 20 slides independently, **before seeing any AI output**. Aakriti settles disagreements | `research/test-set/key-facts.md` | 9 pm |
| Shrijana | Write 4 comprehension questions for each slide in the two M2 slide sets (A and B, 3 slides each), with an answer key | `research/study/questions.md` | 9 pm |
| Shrijana | Book participants. Send the consent form | Bookings in the replies log (no names in git) | 9 pm |
| Khemraj | Run `research/pdf-scan/` on the UWindsor PDFs (this answers stress test question 9) | `research/pdf-scan/uwindsor-results.md` | 11 pm |

### Fri Nov 28: finish the release

| Who | Task | Output | Due |
|---|---|---|---|
| Abhinav | Release items 3–5: HTML output, one command (or a simple upload page), cost and time CSV per run. Remove the hand-written `slides.json` path | Working release, tag `v1.0-rc`. README with how to run it | 9 pm |
| Khemraj | Cost sheet: hours per person since Sep 17 (from the log) × CAD $25/h, API spend, free resources and who bears their cost | `docs/cost-tracking.md` | 9 pm |
| Aakriti | Requirements traceability table: problem → need → R1/R2 → release feature → test (M1–Q1) | `docs/traceability.md` | 9 pm |
| Shrijana | Dry-run the session script with a team member using VoiceOver with the screen off. Fix the script | Notes in the log | 9 pm |

### Sat Nov 29: measure the product (M1, M3, M4, Q1)

| Who | Task | Output | Due |
|---|---|---|---|
| Abhinav | Run the release on all 20 test slides and on 3 full UWindsor lectures | Outputs in `results/`, run CSV | 2 pm |
| Aakriti | Score M1: key-fact recall and critical errors per slide, against the frozen references | `results/m1-accuracy.md` | 9 pm |
| Khemraj | Q1: axe-core, then VoiceOver (Mac) and NVDA (Windows) walkthroughs. M3 and M4 from the run CSV | `results/q1-quality.md`, `results/m3-m4.md` | 9 pm |
| Abhinav | Fix the defects Q1 finds. Re-run. Tag `v1.0` | Release frozen for the user sessions | 11 pm |
| Shrijana | Confirm sessions. Send each participant the instructions | — | 9 pm |

### Sun Nov 30: first user sessions, report writing begins

| Who | Task | Output | Due |
|---|---|---|---|
| Shrijana + Abhinav | M2 sessions as booked (30 min each, on the participant's own device and screen reader, original PDF vs our HTML, order counterbalanced) | Anonymized scores in `results/m2-comprehension.md`. Raw data outside git | as booked |
| Aakriti | Results table: every measure against its threshold, marked met / not met / not measured | `results/summary.md` | 9 pm |
| Khemraj | Hypotheses H1–H11 final status (supported, partly, rejected, untested, with evidence). Risks and limits | `docs/hypotheses-final.md`, `docs/risks-and-limits.md` | 9 pm |
| All | Team rubric (weak, acceptable, strong for product and method), compared with the course rubric: where we agree, where we differ, and why | `docs/team-rubric.md` (Aakriti leads) | 11 pm |

### Mon Dec 1: final report, slides and rehearsal

| Who | Task | Output | Due |
|---|---|---|---|
| All | Final report (past tense, structured on the 7 defense points). Each person writes their own sections | `docs/Final Report.md` + PDF | 6 pm |
| Abhinav | Slide deck. Demo script with a recorded backup video of the demo | `docs/defense/` | 6 pm |
| Khemraj | Scaling strategy: what it would take to run at UWindsor through SAS and CTL (tech, people, data, policy, cost) | Section in the final report | 6 pm |
| All | **Individual reflective reports**, one per person: what you believed, evidence, alternatives, what you expected, what happened, what changed | `docs/reflections/<name>.md` | 11 pm |
| All | Full rehearsal at 8 pm, timed. Cut anything over time. Write AI-use disclosure | — | 10 pm |

### Dec 2 onward (buffer)

More M2 sessions if participants come later. Update `results/` and the slides. Rehearse again the day before our slot.

## Defense run sheet (planned for 20 minutes; adjust once the slot length is confirmed)

| Min | Point | Presenter | Content |
|---|---|---|---|
| 0–1 | — | Abhinav | Team, problem in one sentence |
| 1–4 | 1. Problem is real | Aakriti | For whom, objective, difficulty, why, consequence. Scan numbers, UWindsor scan, SAS interview, lawsuits, AODA |
| 4–6 | Project history | Abhinav | Timeline below. What we dropped and why |
| 6–8 | 2. Intervention fits | Abhinav | Value chain, why the description step is where the problem sits, why HTML rather than tagged PDF, no braille |
| 8–11 | 3. Product works | Abhinav | **Live demo:** upload a UWindsor PDF → accessible HTML → VoiceOver reads a diagram |
| 11–13 | 4. Method, quality, resources | Khemraj | Spiral rounds, decisions log, Q1 results, cost sheet |
| 13–16 | 5. Removes the problem | Shrijana | M1 and M2 against the thresholds, stated honestly |
| 16–18 | 6. Impact and scale | Khemraj | M3, M4, what it takes to scale, limits |
| 18–20 | 7. Evidence-based | Aakriti | Hypotheses status, team rubric compared with the course rubric, what we would do differently |
| after | Questions | All | Prepare from `docs/defense-stress-test.md` |

### Project history slide (Sep 17 → Dec)

| Week | Dates | What happened |
|---|---|---|
| 1–3 | Sep 17 – Oct 7 | GPU scaling plan for the fictional "LaunchCo". Dropped Oct 7 after the professor and GA said real evidence was not possible |
| 4–5 | Oct 10 – 25 | Compared 5 problems. Chose accessible lecture material after the CS231n test. Ruled out braille output and tagged PDF |
| 6 | Oct 26 – 28 | ER01 and ER02. Feedback: we were solution-first and responsibilities were unclear |
| 7 | Oct 29 – Nov 4 | Evidence before building. 27-PDF scan, sources. Claim 3 reframed |
| 8–9 | Nov 5 – 18 | Two-week plan, member-owned areas, survey and outreach. ER03: problem restated, 11 hypotheses, spiral model |
| 10 | Nov 19 – 25 | SAS interview (Nov 24). H11 partly rejected. Impact criteria drafted |
| — | Nov 26 – Dec 1 | Release built and measured. User sessions. Defense prepared |

## Risks to the plan

| Risk | Sign | Response, decided now |
|---|---|---|
| No participants by Dec 1 | No bookings by Nov 28 | Apply the rule in the impact criteria (section 4): claim only M1, M3, M4 and Q1, and present the January study |
| REB clearance needed | Professor's reply | No sessions until it is cleared. Same fallback |
| The vision model misses the M1 threshold | M1 scores on Nov 29 | Report the result honestly. Analyse which diagram types fail. Narrow the declared scope if the data supports it. Never re-score against changed criteria |
| Release not ready by Nov 28 | `v1.0-rc` missing | Khemraj joins the build. Drop R2 and the upload page, and use the CLI only |
| A member is unavailable | Missed stand-up | Their tasks go to the next person in the owners table the same night. Log it in the decisions log |
