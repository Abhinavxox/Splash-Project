# Design rationale: from the goal to the engineering requirements to the design

Written Nov 25, 2026. This is the chain we defend at the final defense: **goal → users and how they differ → needs (with evidence) → engineering requirements (measurable) → design decisions (with alternatives) → tests.** Every row points to its source, so a reviewer can check it.

Sources used here:
- `[SAS]` is the SAS advisor interview of Nov 24, 2026. The raw transcript is not in git; the anonymized summary is in `research/interviews/`.
- `[ER03]` is the ER03 problem statement and draft requirements (`docs/Expert Review 03.md`).
- `[SCAN]` is our 27-PDF scan (`research/pdf-scan/`).
- `[EV]` is the evidence register (`research/evidence-register.md`).
- `[TOOLS]` is the review of 16 existing tools.

## 1. Goal

A blind or low vision university student learns **the same information** as classmates from **the same lecture material**, **without depending on a sighted person**, and **in time to use it** (before or during the lecture). `[ER03]`, `[SAS]`

The independence part comes straight from SAS: relying on people (scribes, often GAs) is "where bottlenecks happen and that's where barriers come." `[SAS]`

## 1b. The struggle: what getting the information costs a student today

The problem is not only that information is missing. Getting it takes work, time and other people, and sighted classmates pay none of that.

| What the student goes through | Evidence |
|---|---|
| **Has to depend on another person.** A scribe or GA must understand the material and must not give answers. Every such dependency is where "bottlenecks happen and… barriers come" | `[SAS]` |
| **Arrives at the lecture unprepared.** The ideal is to have the material in digital form before the lecture to follow along. When the professor's format is wrong, that doesn't happen | `[SAS]` |
| **Waits.** If a textbook isn't available digitally, SAS contacts the publisher, proves the purchase, and may cut the spine off and scan the book. How long this takes depends on the original format | `[SAS]`, `[EV]` (2–10 business days published) |
| **Gets material that a scan can't fix.** Old photocopied handouts defeat OCR | `[SAS]` |
| **Spends extra hours.** For example, 30 minutes for a 5-minute video, and 12 hours a week for statistics | `research/research-questions.md` J |
| **Finds even the help is made for sighted people.** A blind student found screen-reader tutorials "made for sighted teachers" | `[EV]` #5 |
| **Is shut out of the course content.** Blind graduate students at WVU could not read their course PDFs, which led to a complaint | `[EV]` #37 |
| **Every student differs, and some find any new software a burden.** So a fix that adds learning effort adds to the struggle | `[SAS]` |

What this means for the design: the release must reduce **effort** and **dependence**, not only accuracy. So the tests record effort, confidence and "would need sighted help" (see `results/sim/summary.md` and M2), alongside correct answers.

## 2. Who the users are, and how they differ

SAS was clear that there is no single "blind student." Solutions "are all very, very tuned to that person," and a fix that works for one person may not help the next. `[SAS]` So we do not design for one average student. We name the dimensions on which students differ and make the design handle each one.

| Dimension | Range | Why it matters for the design | Source |
|---|---|---|---|
| **D1 Vision** | Low vision → legally blind with some vision → no vision | Low vision students may still use the image with zoom or contrast. Blind students need everything in words | `[SAS]` |
| **D2 Onset** | Born blind → lost vision later | Born-blind students "have no comparison for things": a description that says "looks like a tree" or uses colour does not help them. It must describe structure and relationships | `[SAS]` |
| **D3 Technology skill** | Expert screen reader user → new to software | It must work with the student's *own* screen reader and habits, with nothing new to learn. A new app is a barrier for some | `[SAS]` |
| **D4 Reading mode** | Speech (screen reader) → refreshable braille → paper braille | Braille users need correct braille, especially for math | `[SAS]`, `[ER03]` R3 |
| **D5 Subject** | Text-heavy (history, sociology) → math and science | Text is "pretty straightforward nowadays." Formulas, charts, graphs and pictures are "the most difficult" | `[SAS]`, `[SCAN]` |
| **D6 Depth needed** | Wants the gist → wants every value | One fixed description is either too long or too short for a given student. Sources show students turn to tutors and friends for follow-up | `[ER03]` R2 |

**What we can defend:** these six dimensions come from SAS and the published sources. **What we cannot defend yet:** which dimensions matter *most*, because we have heard from no student directly. That is why M2 records each participant's profile (section 6).

## 3. Needs: what students must be able to do

| Need | Statement | Evidence |
|---|---|---|
| N1 | Get the information in visual content (diagrams, charts, formulas, labelled pictures), not just the text around it | `[SAS]`: visuals are the hardest part. `[SCAN]`: 3% of tagged images described, 0 formulas described, 12 of 27 files untagged |
| N2 | Get it **before** the lecture, so they can follow along | `[SAS]`: ideally the student has it in digital form before the lecture "so they know what the heck's going on." `[EV]`: published turnaround of 2–10 business days |
| N3 | Get it **without a person** in the loop | `[SAS]`: get rid of relying on people |
| N4 | Use their **own tools** (screen reader, zoom, braille display) | `[SAS]`, D3 |
| N5 | Read math in a form blind students already use (LaTeX, or MathML their screen reader speaks) | `[SAS]`: LaTeX matters for blind students' math |
| N6 | Control the depth: overview first, then detail, then ask questions | `[ER03]` R2, D6 |
| N7 | Not be the only one it is built for. It should help many kinds of users (universal design) | `[SAS]`: the automatic door opener example, and screen readers now used by people with learning disabilities |

## 4. Engineering requirements (measurable, traced)

User requirements R1–R3 `[ER03]` say what the student needs. The engineering requirements (ERQ) say what the software must do, written so they can be **tested**.

| ID | Engineering requirement | From | Test (see `impact-criteria-and-release.md`) | In release? |
|---|---|---|---|---|
| ERQ1 | For every slide containing a labelled diagram, produce a text description with three layers: **overview, parts, how the parts relate** | R1, N1, N6 | M1 key-fact recall ≥ 80% | Yes |
| ERQ2 | Descriptions state structure, position and relationships, and **never rely on visual comparison or colour alone** (if colour carries meaning, name what it encodes) | N1, D2 | M1 scoring rule: a description that depends on colour or appearance counts as a missed fact | Yes |
| ERQ3 | Every formula is output as **MathML** (spoken by screen readers) **and** its **LaTeX source** is available | N5, D4, D5 | Q1: VoiceOver and NVDA speak the math. LaTeX present | Yes |
| ERQ4 | Data tables are output as real HTML tables with header cells | N1 | Q1: navigable by row and column in a screen reader | Yes |
| ERQ5 | Output is plain semantic HTML: one heading per slide, works in any browser and screen reader, **no plugin or account** | N4, D3, N7 | Q1: axe-core has 0 serious violations. Heading navigation works | Yes |
| ERQ6 | The original slide image stays in the page, with zoom and high-contrast support, for low vision readers | D1, N7 | Q1: image present, zoom to 400% without loss | Yes |
| ERQ7 | Any lecture PDF is processed end to end **with no person involved** | N3 | M3: ≤ 10 min per lecture. The run log shows no manual step | Yes |
| ERQ8 | Processing finishes before the lecture: a whole lecture in minutes, not days | N2 | M3 | Yes |
| ERQ9 | Cost per lecture low enough for an institution to run on every course | Scale | M4 ≤ CAD $2 | Yes |
| ERQ10 | **Depth setting:** the student chooses *brief* (overview only) or *full* (all layers), and can jump between layers by heading | N6, D6 | Q1 check, and M2 participant feedback | Yes (simple setting) |
| ERQ11 | Follow-up questions about one slide, answered from that slide's content | R2, N6 | M2 feedback | Stretch only |
| ERQ12 | Braille output, including math | R3, D4 | — | **No.** Out of scope: existing tools (Liblouis, MathCAT) produce braille from the MathML and HTML we output. Decision of Oct 25 |

## 5. Design decisions and the alternatives we rejected

| Decision | Why | Alternatives considered, and why rejected |
|---|---|---|
| **Work on the material, not on the student's device** | The mechanism we found is upstream: files are made without described visuals `[SCAN]`. Screen readers work when content is structured `[EV]`, so the gap is in the content | *A new screen reader or app:* SAS says some students struggle to learn new software (D3), and screen readers already exist. *Training instructors only:* SAS already encourages this. It's slow and doesn't fix existing files |
| **Automatic description using a vision model** | It removes the person from the loop (N3) and finishes in minutes (N2) | *Human describers or scribes:* they are the bottleneck SAS described. *Existing remediation tools (Adobe, CommonLook, Equidox):* all 16 tools reviewed still need a person for descriptions `[TOOLS]`. *Alt text only:* one line is not enough for a diagram (D6) |
| **Layered description (overview → parts → relationships)** | It serves both gist and detail readers (D6). Screen reader users can skip by heading | *One paragraph:* too long for some students, too short for others |
| **No visual analogies or colour-only statements** | Born-blind students have no visual reference (D2) | *Conventional alt text style:* often says what something "looks like" |
| **HTML output, not tagged PDF** | Our tagged PDF test lost the meaning of formulas. HTML with MathML kept it. HTML works in every browser and screen reader (D3) | *Tagged PDF:* tested on Oct 25 and failed for math. *EPUB:* reader support varies |
| **MathML plus LaTeX** | Screen readers speak MathML. Blind students who use LaTeX can read the source (D4, D5) | *Images of formulas:* unreadable. *Spoken text only:* ambiguous for complex math |
| **Keep the original image** | Low vision students may still use it (D1). Universal design (N7) | *Text only:* excludes low vision users |
| **A linear pipeline, not an agent** | Same steps for every slide, so it is measurable and has fewer failure points under a one-week deadline | *Agentic pipeline:* more complex, harder to verify, and no evidence it improves the result |
| **Labelled diagrams first (Round 1)** | The riskiest and most common unsolved type. Math already has partial tools `[TOOLS]` | *Video and labs first:* bigger scope, can't be done by Dec 1 |
| **No braille output** | Liblouis and MathCAT already do it from structured content. SAS warned against recreating what exists | *Build braille ourselves:* would duplicate mature tools |

## 6. How "every student is different" is handled in practice

1. **In the design:** the student's own tools are used (ERQ5). Depth is chosen by the student (ERQ10). Descriptions work for born-blind readers (ERQ2). The image is kept for low vision readers (ERQ6). Math comes in two forms (ERQ3).
2. **In the test:** each M2 participant gives a short profile: vision (D1), onset (D2), screen reader and skill (D3), braille use (D4), field of study (D5). It is stored anonymized. **Results are reported per participant, not only as an average**, so we can see where the design works and where it does not.
3. **In the claims:** with a few participants we cannot claim the design works for all students. We claim results for the profiles we tested, and we list the profiles we did not test.
4. **After the course:** the January SAS study, the CTL assistive technology specialist and CNIB are the route to wider profiles.

## 6b. Testing ladder: from cheap checks to real users

| Step | What | What it can show | What it cannot show |
|---|---|---|---|
| 1 | **Simulated personas** (`prototype/simulate.py`): AI students with different profiles try variants P0–P3 | Which variant is stronger; broken questions; obvious gaps. Cheap and repeatable | Anything about real students. The personas barely differed from each other |
| 2 | Team members use VoiceOver and NVDA with the screen off (Q1) | Navigation, how the math is spoken, real screen reader behaviour | Real blind users' skills, habits and needs |
| 3 | Real blind and low vision participants (M2) | **Impact**: comprehension, effort, independence | Generalisation beyond the profiles we tested |

The first simulation (Nov 25) favoured full mode (92% vs 35% for the original PDF). It found a flawed draft question and a possible braille-reading issue with raw LaTeX. Full results: `results/sim/summary.md`.

## 7. Questions we must be able to answer at the defense

| Question | Answer, and where the evidence is |
|---|---|
| Why this problem? | Section 3, N1–N3. Scan, SAS and lawsuits |
| Why software, and why at this point in the system? | Section 5, row 1. The gap is in the content, not the screen reader |
| How did user needs become engineering requirements? | Section 4. Each ERQ has a source and a test |
| Every student is different. How did you account for that? | Sections 2 and 6 |
| Did you talk to the users? | SAS, yes. Students: give the M2 numbers honestly, plus the January plan |
| Doesn't this already exist? | `[TOOLS]`: all 16 need a person for descriptions. H11 partly rejected after SAS |
| Can the AI be trusted? | M1 results, including the critical error rate |
| Why not braille, video or labs? | Section 5, and the declared scope |

## 8. What is still assumption, not evidence

- The six dimensions come from one SAS interview and published sources, not from students.
- ERQ10 (depth setting) and ERQ11 (follow-up questions) come from published sources. No student has asked us for them directly.
- Whether students prefer HTML to their current workflow is untested.
- Raise all three openly at the defense. The course rewards limitations that are recognised and managed.
