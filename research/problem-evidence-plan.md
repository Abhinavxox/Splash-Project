# Problem evidence research plan

Goal. Show with evidence that lecture slides without meaning are a real problem for real blind and low vision students, how big it is, and why current fixes are not enough.

This document is the plan only. What we actually find and read goes in `evidence-register.md`, one row per source, with the link and who checked it.

## Claims we need to support

1. Blind and low vision students use screen readers and braille displays to study.
2. Lecture slides and PDFs often lose formulas, tables and diagrams for these users.
3. Students wait a long time for accessible versions.
4. Fixing files by hand is slow and costly.
5. Institutions are required to provide accessible material.
6. Existing tools and services do not fully solve this for lecture slides.
7. Enough students are affected for this to matter.

## Where to look and what to search

### 1. What users say

YouTube
- blind student university screen reader
- blind computer science student how I study
- screen reader reading PDF demo
- NVDA math reading demo
- blind student STEM accessibility
- how blind people read diagrams tactile graphics

Forums and communities
- AppleVis forums, search PDF, lecture slides, math
- NVDA users mailing list (groups.io nvda)
- Reddit r/Blind and r/Blindness, search lecture slides, PDF, professor, accessibility office
- NFB and ACB student division pages and blogs

Podcasts
- NFB Access On
- Double Tap
- AFB blog and podcasts

Large surveys
- WebAIM Screen Reader User Survey, the latest edition, questions on PDFs and documents

Record. What the person says, which claim it supports, date, link.

### 2. What institutions say

- University accessibility office pages on alternate format turnaround. Search alternate format request turnaround university, accessible course materials request how long
- University of Windsor Student Accessibility Services pages
- Job postings for alternate format specialist or accessibility remediation specialist on Indeed, LinkedIn and university job boards
- Annual accessibility reports from Ontario universities

Record. Turnaround time stated, number of students or documents if given, what work is done by hand.

### 3. Laws, rules and complaints

- AODA Integrated Accessibility Standards, education section, Ontario
- Accessible Canada Act
- US ADA Title II web accessibility rule from April 2024 and its compliance dates
- US Department of Education Office for Civil Rights resolution agreements with universities about inaccessible course material
- UN Convention on the Rights of Persons with Disabilities, Article 24 on education

Record. What the rule requires, the date, and any named university cases.

### 4. Numbers on who is affected

- Statistics Canada Canadian Survey on Disability, seeing disabilities and education
- WHO World Report on Vision
- CNIB and NFB reports on education and employment
- Ontario or Canadian data on postsecondary students with disabilities

Record. The figure, the year, and whether it is direct or indirect evidence.

### 5. Research papers

Search Google Scholar, Semantic Scholar, ACM Digital Library and arXiv for
- accessibility of PDF documents large scale study
- accessibility of scholarly PDFs
- blind students STEM barriers
- math accessibility screen reader
- lecture slides accessibility screen reader
- alternative format production higher education

Start from the papers already in `references.md` and follow their references.

Record. Title, year, venue, what they measured, sample size, main finding, which claim it supports.

### 6. News

- News on blind students and inaccessible courses
- News on lawsuits or complaints about course material accessibility
- News on universities preparing for the 2026 ADA deadlines and AODA

Record. Headline, outlet, date, and the facts it reports with its own sources.

### 7. Current solutions and who is working on it

- Vendors. Adobe Acrobat auto tag, Equidox, CommonLook, DocAble, Mathpix, AbleDocs
- Nonprofits. Benetech and the DIAGRAM Center, APH, Bookshare, DAISY Consortium
- Research groups. MIT Visualization Group (Olli), authors of the STEM PDF papers
- Free tools. PAC checker, veraPDF, NVDA, MathCAT, Liblouis

Record. What it does, price, what it claims, what independent sources or users say, what it leaves to people.

### 8. Our own measurements

- Scan 50 to 100 public lecture PDFs from several universities. Count untagged files, slides with formulas or tables as images, and images with no description.
- Record what a screen reader actually says on sample slides with VoiceOver or NVDA.
- Fix five slides each by hand with free tools and time it.

Record. Scripts in the repository, raw outputs, and the summary numbers.

## How strong each type is

- Strongest. Our own measurements, laws and complaints, institutions' own statements, large surveys.
- Medium. Research papers close to our problem, several user voices that agree.
- Weakest alone. One video or news story, broad statistics.

Aim for at least one strong source for each claim, from two or three different types.

## Who does what

| Person | Evidence types |
|---|---|
| Abhinav | 8 own measurements |
| Shrijana | 1 user voices |
| Aakriti | 2 institutions and 3 laws |
| Khemraj | 4 numbers, 5 papers and 7 current solutions |

News (6) is shared. Anyone who finds a relevant story adds it.

## Rules

- Only add a source to the register after someone has opened and read or watched it.
- Every row has a link and the name of the person who checked it.
- Write what the source actually says, not what we hope it says.
- Note sources that go against our assumptions too.
