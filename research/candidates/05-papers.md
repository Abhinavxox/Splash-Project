# 05 papers - PDF / slides / math accessibility for BLV students

rough notes, not polished. only included papers i actually opened (abstract or page). no years in headings since the brief said no dates. numbers copied from abstract/page, not checked against full text unless noted.

### Uncovering the New Accessibility Crisis in Scholarly PDFs (arXiv preprint, cs.DL/cs.HC; ASSETS 24 cited by other sources, not confirmed on arxiv page)
https://arxiv.org/abs/2410.03022 (accessed 2026-10-29)
type: paper
notes: ~20,000 open + closed access scholarly PDFs, broad fields. checked 6 things: default language, nesting, tagged, table headers, tab order, alt-text. used automated checks + manual alt-text review + 2nd checker + manual screen reader testing.
main finding: <3.2% pass all 6, 74.9% fail every criterion. accessibility dropped after 2019, mostly open access papers. field, platform, publishing model all linked to compliance.
supports claim: 2 (no, that's slides/formulas, not really), 7 (scale), 6 (current tools/practice fall short), 1 (indirect - screen reader testing done)
how solid: strong on scale and measurement (big n, automated + manual). medium on venue since page says arxiv preprint only, not peer reviewed as shown. the claim list is about pdf structure, not formulas/tables specifically (tables only as table headers).
goes against us: none of their 6 criteria are about formulas or diagrams, so this doesnt directly prove formulas fail. also they measure compliance with checklist, not that a student actually struggles.

### Improving the Accessibility of Scientific Documents: Current State, User Needs, and a System Solution (SciA11y; Wang et al.; arXiv)
https://arxiv.org/abs/2105.00076 (accessed 2026-10-29)
type: paper
notes: 11,397 scientific PDFs (2010-2019 range), measured against criteria. also qualitative user study with BLV researchers (n not stated in abstract). also tested HTML render quality.
main finding: only 2.4% of PDFs met all criteria. 87% of SciA11y HTML renders had none or only some readability issues. users said they'd likely use it. 5 design recs.
supports claim: 7 (scale), 6 (tools fall short - they built SciA11y because pdf is bad), 4 (manual fixing - implied, not measured), 1 (BLV researchers needs)
how solid: strong for the 2.4% number (large sample). weak-medium for user side (qualitative, n unknown from abstract, self-selected positive response).
goes against us: 87% render result is the tool's own output, authors built it, so not independent. "users said would use" is stated intention not usage.

### Uncovering the (scholarly PDF / math) - Mathematical Content Browsing for Print-disabled Readers Based on Virtual-world Exploration and Audio-visual Sensory Substitution (Kruger, De Wet, Niesler; ACM TACCESS)
https://doi.org/10.1145/3584365 (accessed 2026-10-29)
type: paper (but i read it through a secondary literature review page, not the paper itself - the review is at https://a11y-paradise.onrender.com/reviews/69cb2f3779c4830052f7733c, CC BY-SA, by bob dodd. re-check numbers against DOI)
notes: 25 participants (11 blind, 14 sighted), 12 equations. text-adventure style nav + vOICe sonification.
main finding: 78% fully correct overall (74% blind, 83% sighted); 95.4% with partial credit. graphical mode helped. matrices hardest. 8 of 11 blind users said spatial layout got clearer.
supports claim: 2 (formulas lost in pdf - "most equations in scientific PDFs lack semantic markup"), 1 (blind users reading math), 6 (tools fall short - screen reader reads equations as jumbled text)
how solid: medium. small n, prototype system, and i didnt open the paper, only the review. good for the "equations read as jumbled text" point if we can get the paper.
goes against us: it's a research prototype. 74% correct for blind users = still ~1 in 4 wrong, but that's an argument for tools not against the problem. also their system is the fix not the baseline, so no baseline numbers from it.

### Towards More Accessible Scientific PDFs for People with Visual Impairments: Step-by-Step PDF Remediation to Improve Tag Accuracy (PAVE 2.0; CHI 25 per arxiv page)
https://arxiv.org/abs/2503.22216 (accessed 2026-10-29)
type: paper
notes: 19 participants, remediation task, prototype PAVE 2.0 vs Adobe Acrobat Pro. split into experienced vs novice remediators. also alt-text for math formulas without expert knowledge.
main finding: tag score experienced 42.0% -> 80.1%; novice 39.2% -> 75.2% (with PAVE 2.0). 15 said they'd prefer PAVE in future.
supports claim: 4 (manual fixing costly - they measure how hard tagging is by hand), 6 (current tools fall short - acrobat baseline ~42%/39%), 7 (scale - scientific pdfs)
how solid: medium. decent n, direct baseline comparison. but participants were remediators, NOT screen reader users, per abstract. so it doesnt show blind users struggle.
goes against us: they fixed it to 75-80% with their own tool, so tagging is partly fixable with tools. also the 42% baseline is for people doing the task, not a measure of how much a student is hurt.

### Screen-Reader Based Contextual Exploration of Mathematical Formulas in Brazilian Portuguese (Access8Math-NavMatBR; Guedes et al.; Journal on Interactive Systems)
https://journals-sol.sbc.org.br/index.php/jis/article/view/3325 (accessed 2026-10-29)
type: paper
notes: 6 people with visual disabilities, usability tests (think-aloud) + teaching scenario in numerical analysis. extended NVDA add-on Access8Math. web formulas, not pdf.
main finding: improved understanding of formulas and access to elements. 52 usability issues found (commands, verbalization, platform structure). design implications for brazilian formula reading.
supports claim: 1 (screen reader users dealing with math), 6 (tools still have 52 issues), 2 (formulas)
how solid: weak-medium. only 6 people, portuguese context, web not pdf. but it's a real measurement of problems.
goes against us: it's about web math, not slides/pdf. and the add-on works - "improved understanding" - so tools exist that help.

### Understanding the Practice, Perception, and Challenge of Blind or Low Vision Students Learning through Accessible Technologies in Non-Inclusive "Blind Colleges" (arXiv)
https://arxiv.org/abs/2501.07736 (accessed 2026-10-29)
type: paper
notes: BLV students at a chinese "blind college". "two-part empirical approach". n not stated in abstract.
main finding: tactile + digital tech helps but hard to integrate. early education matters. systemic obstacles. want more inclusive environments.
supports claim: 1 (students rely on screen readers/braille), 5 (institutional/systemic barriers - loosely)
how solid: weak. n not in abstract, context is a special school, not regular university. good for "users rely on AT" flavour only.
goes against us: it's about a segregated blind college, so it may not generalise to mainstream university students with slides/pdf. abstract doesnt mention pdf or slides at all.

### Students with disabilities in higher education: challenges and tactile solutions (Petrie, Power, Swallow; Art Libraries Journal, 2009 published online 2016)
https://www.cambridge.org/core/journals/art-libraries-journal/article/students-with-disabilities-in-higher-education-challenges-and-tactile-solutions/7712B42AE0F5ACF880295B2099161305 (accessed 2026-10-29)
type: paper
notes: "international online surveys" of students with disabilities and disability professionals. no n in abstract.
main finding: alt format + enhanced materials not provided as well as they should be. tactile images/graphics especially badly provided. number of students with disabilities going up.
supports claim: 5 (institutions not providing), 2 (graphics/images poorly provided), 4 (indirect)
how solid: weak-medium. older, n unknown from what i could read, but its an actual survey of the people affected. abstract-level only.
goes against us: 2009-ish data, pre-current screen reader/pdf tools. also talks about tactile more than screen reader access.

### Alternate Format Production Service in Nova Scotia: A University and Community College Collaborative Study (Stenstrom; Collections 2007; E-LIS)
https://eprints.rclis.org/3849/ (accessed 2026-10-29)
type: paper (feasibility report / conference paper, canadian)
notes: interviews w disability staff, library reps, orgs in NS. reviewed services in BC, MB, ON. roundtable. NO numbers reported on page.
main finding: "students aren't receiving consistent service across the province". alt format still a problem. proposed consortial model.
supports claim: 5 (institutions required/expected to provide - they're not doing it consistently), 3 (no), 4 (efficiency not realized - qualitative)
how solid: weak. no numbers at all, qualitative, canadian, old (2007). use only as context.
goes against us: no numbers, so cant say how many students or how long waits. and its about print disabled students generally, not stem or pdf specifically.

### Access to Academic Materials for Post-Secondary Students with Print Disabilities: Service Provider Survey (NEADS; Canada)
https://neads.ca/en/about/projects/atam/provider_details_C.php (accessed 2026-10-29)
type: survey report (web page of results)
notes: survey of service providers (alt format offices). year not on page. respondent n not stated, only percentages. 77% produce alt format in-house.
main finding: self-rated production knowledge ~60% said needs improvement or average. 18.7% have a process to evaluate production, 64% dont. 
supports claim: 4 (manual production costly/effort - in-house, staff knowledge gaps), 5 (institutions - no evaluation process at most), 6 (staff knowledge limits quality - loosely)
how solid: weak-medium. good detail on institutional practice, but n not stated and its self-rated knowledge, so not a real measure of quality.
goes against us: self-rated knowledge isnt a measure of output quality. also canadian. the 77% in-house figure could be read as "institutions are handling it" which weakens the "institutions dont care" angle.

### Notes for the team (not papers)
- couldnt open these, so left out: iTagPDF (CHI 26) - pdf download was too big for webfetch; Fan et al. concurrent slide exploration (ASSETS 23) - only a mirror link came up; Slide Gestalt (CHI 23); Thai 2010 math/ebook paper - scitepress pdf failed; the 2022 SchmittKoopmann STEM pdfs paper - host not reachable. worth grabbing these by hand.
- searches for lecture slides + screen reader gave mostly student projects, guidance pages, and tool pages. no measured study of PowerPoint/slide accessibility for BLV users found yet. that is a gap for claim 2.
- nothing found yet on "how long students wait" (claim 3) - no paper with wait-time numbers in what i opened.
- found only 9 papers i could verify, short of the 10-20 target. the rest of the list was search snippets only, which the brief excludes.
