# Writing the Technical Paper

Theme. Software Engineer or Software Management, similarities and differences.
Deadline. October 28, 23:59. Hard deadline, group submission on Brightspace.

## 1. What we are submitting

1. The technical paper (required). IEEE conference format, two columns, at least 6 to 7 pages and at most 8, not counting references.
2. The video podcast (required). 10 minutes maximum.
3. The poster (optional bonus). 48 x 36 inches landscape or 36 x 48 portrait.
4. Appendices. Raw interview transcripts and signed consent forms.
5. A separate confidential document with each interviewee's name, company and job title. Only the instructors see this. It never goes in the paper, video or poster.

## 2. Where our material is

| What | Where in this repo |
|---|---|
| Paper summaries from each member | `summaries/` |
| Interview transcripts (anonymized) | `interviews/` |
| All papers found, with abstracts | `papers/papers_v2.csv` |
| The 79 screened papers and keep decisions | `papers/candidates_to_review.csv` |
| Search log (queries, filters, hit counts) | `papers/search_log_v2.csv` and `papers/first-search/search_log.csv` |
| Paper PDFs | `papers/pdfs/` |
| Who read which paper | `papers/assignments.md` |

## 3. Before anyone writes (team meeting, about 1 hour)

1. Each member shares 2 or 3 key points from their papers.
2. Group the findings into 3 or 4 themes. Possible themes are who makes decisions, how performance is judged, skills each role needs, how the roles talk to each other, and the effect of AI tools.
3. For each theme write three lines.
   - What the papers say (theory).
   - What the interviewees said (practice).
   - Where they differ and why.
4. Agree on the final research question, word for word.
5. Agree on the hypothesis we had before reading. It must include a reason ("because ...").
6. Pick the final 20 to 30 papers to cite. Each must be peer reviewed and actually read.

This one page of themes is the backbone of the whole paper, the video and the poster.

## 4. Writing the raw draft first

We will first write a raw draft in a plain doc, then move it into the IEEE template.

Exact team note:

> we will be creating a raw doc format first where the instructions need to be nice format, small grammar mistakres will be there, and things like no overuse of struccute like bold big fonts for title all same it will be. And then use of things like :, ;, -, "", captile words in the middle of the senetec,e and don't written as dont, things like this

What this means for the raw draft
- Plain text. Same font and size for everything, titles included. No bold, no big headings.
- Small grammar mistakes are fine at this stage.
- Avoid colons, semicolons, dashes and quotation marks.
- No capital words in the middle of sentences unless it is a name.
- Write contractions without the apostrophe, like dont instead of don't.
- Keep sentences short and simple. Use fewer commas.

## 5. Format rules for the final paper

- IEEE conference template, two columns. LaTeX template is on Brightspace. Use Overleaf so everyone can edit.
- At least 6 to 7 pages, references not included. The maximum is 8 pages.
- Citations are a simple number in square brackets right after the word or sentence it supports, like this [1]. No author names and no et al in the text. Just the number and move on.
- Use Zotero or Mendeley to manage references and export a `.bib` file.
- Formal and impersonal tone. Write "The data suggests" and not "I think".
- Run a spell checker before submitting.

## 6. Sections of the paper

### Abstract (about 150 words, write it last)
- The problem.
- The research question.
- How we investigated (literature plus interviews).
- The main gap we found.
- The main recommendation.

### 1. Introduction (about 0.75 page)
- Why the difference between software engineers and software managers matters in industry.
- The research question. It must be specific and falsifiable, meaning the answer could turn out to be no.
- The a priori hypothesis, written before reading the literature, with its explanation (the "because").
- A short outline of the rest of the paper.

### 2. Methodology (about 1 page)
Literature search
- Databases used (OpenAlex, plus IEEE Xplore and ACM through Leddy Library if we used them).
- The exact search strings. Copy them from the search log.
- Date of the search.
- Inclusion and exclusion rules, with a reason for each. For example peer reviewed only, articles and conference papers only, must mention software and a management or leadership role.
- The numbers at each step. For example 137 found, 79 passed the screen, final number kept. A small table works well here.
- How the papers were split among members and summarized.

Interviews
- How many professionals were interviewed.
- Why each person was chosen, for example years of experience and type of role. No names, no company names.
- Their qualification (P.Eng, or B.Eng with business and technical responsibility).
- How the interview was done (spoken or written, how long, open questions).
- That consent was obtained before recording.
- That it was run as a student project under the TCPS 2 rules and the university REB exemption.
- That questions were about general industry practice and not their own company.

### 3. State of the Art, what the literature says (about 1.5 to 2 pages)
- Organize by theme, not paper by paper.
- Group authors who agree and show where authors disagree. For example, several studies report X [3], [7], [12] while another found Y [5].
- Do not write Paper A says X then Paper B says Y one after another. That is listing and loses marks.
- Point out key references that many papers cite.

### 4. State of Practice, what the professionals said (about 1 page)
- Report the interview findings theme by theme.
- Report the constraints, messiness and shortcuts without judging.
- Use short quotes, attributed only as Professional A, Professional B and so on.

### 5. Gap Analysis and Discussion (about 1.5 pages, the most important section)
For each theme
- What is different between theory and practice.
- Why the gap exists. The root cause, such as time pressure, budget, company size, culture, legacy systems or tooling.
- How we know that is the cause.
- What the consequences are, such as technical debt, burnout, security risk or cost.
- Whether our hypothesis was confirmed or not.
- What theory has missed, the new problem practice shows.

Rules for this section
- Act as an analyst, not a reporter.
- Never call anyone lazy, wrong or incompetent. Use words like constrained, pragmatic or optimized for speed.
- Do not declare theory or practice the winner. Explain why each is the way it is.

### 6. Conclusion and Future Work (about 0.5 page)
- Summary of the main findings.
- At least one concrete recommendation for industry.
- What the theory should update.
- Future work, for example more interviews or a specific study.

### References
- 20 to 30 citations in IEEE style.
- Every one real, checked, and actually read.
- Every reference must be cited in the text.

## 7. Who writes what

| Part | Owner |
|---|---|
| Introduction and abstract | [name] |
| Methodology | [name] |
| State of the Art | [name] and [name], two themes each |
| State of Practice | [name] |
| Gap analysis and conclusion | Whole team in one call |
| References and final formatting | [name] |
| Final read through for one consistent voice | [name] |

## 8. Order of writing

1. Everyone writes their part in the raw draft doc first.
2. Methodology first. It is facts only and the easiest.
3. State of the Art and State of Practice in parallel.
4. Gap analysis together as a team.
5. Introduction and conclusion.
6. Abstract last.
7. One person reads the whole paper top to bottom, fixes the flow, checks citations and checks the page count.
8. Move the final text into the IEEE two column template.

## 9. Ethics rules (breaking any of these gives a 0)

- Interviews were presented as a student project, never as research.
- No interviewee name, company or job title anywhere in the paper, video or poster.
- Signed or recorded consent exists for every interview, and for any clip used in the video.
- Interviewees are not friends, family or former MAC students.
- Raw transcripts and consent forms are submitted as appendices.
- Questions were about opinions on general practice, never about salary, private life or company secrets.

## 10. Final checklist before submitting

- [ ] IEEE two column template
- [ ] At least 6 to 7 pages without references, 8 maximum
- [ ] Abstract about 150 words
- [ ] Research question is specific and falsifiable
- [ ] Hypothesis stated with its "because"
- [ ] Search strings, databases and inclusion rules written so someone could repeat the search
- [ ] Interviewee selection explained without revealing identity
- [ ] Literature organized by theme, not listed paper by paper
- [ ] Gap analysis explains root causes and consequences
- [ ] At least one concrete recommendation
- [ ] 20 to 30 real, read, peer reviewed references in IEEE style
- [ ] In text citations are just [1] style numbers, no author names or et al
- [ ] Raw draft written first, then moved into the template
- [ ] Formal tone throughout
- [ ] No names or company names of interviewees
- [ ] Raw transcripts and consent forms ready as appendices
- [ ] Confidential interviewee document ready for instructors
- [ ] Spell checked
- [ ] Submitted on Brightspace before October 28, 23:59
