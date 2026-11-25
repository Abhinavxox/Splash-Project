# Simulated usability pre-test, Nov 25, 2026

**Not impact evidence.** These are AI personas, not blind students. The test was run to compare prototype variants and catch problems before real sessions (M2). Method: `prototype/simulate.py`. Raw trials: `trials.json`.

## Setup

- **Slides:** CS231n lecture 2, slides 22 (labelled diagram), 23 (worked example with grids) and 52 (diagram with an equation). The descriptions came from the live Gemini run (`prototype/runs.csv`, first row).
- **Questions:** 4 per slide, from `research/study/questions-draft.json`. **These are a draft, not the frozen questions.**
- **Personas:** 5, built from the ways students differ in `docs/design-rationale.md`:

  | Persona | Profile |
  |---|---|
  | A | Born blind, expert NVDA user, CS |
  | B | Lost sight at 19, intermediate VoiceOver user, engineering |
  | C | Low vision, uses magnification plus speech, math |
  | D | Born blind, braille display, new to software, required stats course |
  | E | Blind, expert user, short on time before the lecture |

- **Model:** Gemini 3.6 Flash, used for the personas, the follow-up answers and the grading.
- **Scale:** 5 personas × 4 variants × 3 slides = 60 trials, 2 minutes in total.

## Variants

| | What the persona gets |
|---|---|
| P0 | The original PDF as a screen reader reads it (text layer only, images skipped) |
| P1 | Our release, full mode (overview, parts, relationships, formulas, tables) |
| P2 | Our release, brief mode (overview only) |
| P3 | Brief mode plus up to 3 follow-up questions answered from the slide image (R2) |

## Results

| Variant | Correct answers | Effort (1 easy – 5 exhausting) | Confidence (1–5) | Said they need sighted help |
|---|---|---|---|---|
| P0 original PDF | 35% | 4.3 | 2.0 | 11 of 15 |
| **P1 full** | **92%** | **2.4** | **4.6** | **0 of 15** |
| P2 brief | 55% | 3.7 | 3.1 | 10 of 15 |
| P3 brief plus follow-up questions | 88% | 2.7 | 4.5 | 5 of 15 |

| Slide | P0 | P1 | P2 | P3 |
|---|---|---|---|---|
| 22 diagram | 5% | 75% | 45% | 65% |
| 23 grids | 0% | 100% | 20% | 100% |
| 52 equation | 100% | 100% | 100% | 100% |

## What we learned

1. **Full mode was the strongest variant.** Brief mode alone lost most of the detail, so it should stay a setting, not the default.
2. **The follow-up questions (P3) recovered most of what brief mode lost.** That supports keeping R2, but it did not beat full mode, and 5 of 15 personas still wanted help.
3. **The original PDF is not always unreadable.** Slide 52 put its equation in the text layer, so P0 scored 100%. The gap appears on diagrams and grids (slides 22 and 23). Our claim has to be specific to visuals, not to "PDFs" in general.
4. **There is a defect in our draft questions.** Question 4 of slide 22 (the decision rule) is not on the slide. Even the description model said the slide does not state it. The question tests knowledge of the course, not access to the slide. Rewrite it before freezing.
5. **There is a possible design issue for braille readers (persona D).** Raw LaTeX was hard to read. In the real page, LaTeX is folded away and screen readers speak MathML, so this may be an artefact of how the simulation flattens the page. Check it with a real braille user.
6. **The personas barely differed** (P1 scored 92% for every persona). The simulation does **not** capture how students differ. That is a known weakness of simulated users, and the reason real sessions are needed.

## Limitations

- The same model family wrote the descriptions, played the students and graded the answers, so the results may be biased in favour of our output.
- There were 3 slides, from one lecture, with draft questions.
- The personas read a flattened text version, not the page in a real screen reader.
