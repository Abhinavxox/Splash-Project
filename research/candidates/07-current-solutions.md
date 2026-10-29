# 07 current solutions (rough notes)

accessed 2026-10-29. all links below were opened (WebFetch) unless marked.
prices only where a page actually listed one. "not published" = i looked, nothing there.

quick gaps / dead ends:
- DocAble: searched, search returned nothing about the product itself. not included. try "DocAble Yuja" / "DocAble Blackboard" next time.
- AbleDocs: pdfa.org page 403, ESF page 404. only search snippets. snippet had $5.50/$7.00 per page but i never opened a page that confirms it, so NOT used.
- Equidox reseller price ($2,200) only seen in a search snippet, not opened. NOT used.
- Adobe's own helpx accessibility page 403'd. so Adobe's own limitation wording isn't quoted here. using Clemson + AbilityNet + Adobe Community posts instead.
- Mathpix: no official pricing page opened. only a personal guide with "10 pages/mo free" that may be old.
- veraPDF homepage had a "temporarily offline" notice when fetched.

---

### Adobe Acrobat Auto-Tag (Clemson guide + AbilityNet eval)
link: https://www.clemson.edu/accessibility/digital/guides/pdf/remediation/untagged-documents.html
link: https://abilitynet.org.uk/news-blogs/evaluating-adobes-new-cloud-based-auto-tagging-feature-pdf-accessibility
type: vendor (tool) + independent reviews
notes:
- auto tag = builds tag tree from the page. cloud version tested by abilitynet.
- price: not checked.
- clemson says "relatively quick but not 100% reliable and requires manual review".
- abilitynet: complex tables tagged poorly ("need further remediation"), reading order + heading levels get misread on complex layouts. tool adds NO alt text, human adds it.
- abilitynet also lists scope limits: files >100MB or >200 pages (100 scanned), cloud files, protected files, non-Latin alphabets, form fields, annotation text. unsupported ones fall back to old local method.
- human stuff left: alt text, complex tables, reading order, heading levels, checking the tags panel.
supports claim: 4, 6
how solid: strong for the limits (two independent sources, one is a univ). weak for anything Adobe claims itself because helpx page was blocked. no pass/fail numbers in abilitynet, just qualitative.

### Adobe Acrobat Accessibility Community threads (user complaints)
link: https://community.adobe.com/questions-9/remediating-large-document-please-help-1553185
link: https://community.adobe.com/t5/acrobat-discussions/autotagged-tags-in-tags-panel-content-panel-and-read-order-do-not-match/td-p/10624100
type: vendor forum (user complaints)
notes:
- multi-page tables: acrobat treats table continued on pg 2 as a new table. fix = move rows into first table tag by hand.
- missing rows/cells: have to check every cell is inside a row tag, reapply Table in reading order tool.
- tags panel says H1 but reading order + screen reader say paragraph (2019 thread). had to retag by hand.
- forum reply: go back to the Word/InDesign source and re-export, faster than fixing in Acrobat.
supports claim: 1, 4
how solid: medium. user posts, anecdotal, but very specific. they're complaints, not measured.

### AbilityNet / Adobe auto-tag (see above) -- merged into the first entry

### Equidox
link: https://equidox.co/blog/pdf-remediation-software-buyers-guide/
type: vendor
notes:
- annual subscription, CONCURRENT user licenses (5 concurrent ~ 20+ named in their example). also org-wide unlimited option.
- "unlimited remediation under one license, no per-doc fees" (their claim).
- price: NOT listed on the page, they say contact sales.
- software: smart zone / table / list detectors, zone transfer, built-in OCR, equidox AI for templated batches.
- humans: adjust detector sliders, check HTML preview, multi-level table headers + merged cells, edit OCR text, form tooltips, alt text.
- their own words: "not a completely automated solution". also says tools reduce LIKELIHOOD of errors, not guarantee compliance.
- compliance/perf claims are from vendor + customer testimonials, no independent check (the guide admits this).
supports claim: 4, 5, 6
how solid: medium. good that they admit it's not automated. but it is literally the vendor's own guide, so everything it says is marketing unless we find a reviewer.

### CommonLook PDF (Allyant)
link: https://allyant.com/pdf-accessibility-software-solutions/commonlook-pdf/
type: vendor
notes:
- acrobat plugin / browser / desktop. AI auto-tag "at the push of a button", tables lists forms. auto bookmarks, WCAG/PDF-UA/HHS validation w/ pass/fail/warn counts.
- price: none on the page. only free 7-day trial + demo request.
- also a 3rd party price in a MN State IT page: $322.53/yr per license for CommonLook Office (from search snippet only, not opened, not used).
- humans: pick advanced vs simple editor, fix stuff flagged "requires manual review", follow Fix Wizard, training.
- their own admission: "automation alone is not advanced enough for variable or complex content". automation-only tools usually don't give conformance guarantee, page doesn't say if they do.
supports claim: 4, 6
how solid: medium-weak. vendor page, but they say the key limit themselves, which is useful. no independent review opened.

### Mathpix (PDF/image to LaTeX/MathML) -- London Online Learning case
link: https://onlinelearning.london.ac.uk/2024/03/12/accessible-maths/
type: research-ish / user review (not Mathpix itself)
notes:
- tested on a 10-page econ chapter. exported editable LaTeX + image files in right spots.
- still needed "some tweaking" of the LaTeX to work in their VLE. subject expert has to check output.
- handwritten image conversions needed minor fixes.
- "not a complete fix for content accessibility problems, though it significantly reduces workload".
supports claim: 2, 4
how solid: medium. one author, one 10-page test, from a university online-learning blog. good for "it works but needs a human".

### Mathpix (Lane CC review)
link: https://inside.lanecc.edu/node/1073735
type: user review (college accessibility review)
notes:
- big data tables get exported as STATIC IMAGES. screen reader users can't read them and can't zoom/reflow.
- keyboard focus trap in the edit area. breaks WCAG 2.1.2 (no keyboard trap).
- only the two main problems were listed, no other SR problems mentioned.
supports claim: 1, 2, 6
how solid: medium. it's a real institutional review with specific WCAG cites. only one college though, and no date we could confirm.

### DIAGRAM Center image description guidelines (Benetech) + WGBH NCAM
link: https://www.wgbh.org/ncam-resources/2026-08-19/image-description-guidelines
type: nonprofit
notes:
- made by WGBH NCAM w/ DIAGRAM Center at Benetech. DIAGRAM est 2010. NCAM started the STEM work in 2004. Poet tool launched 2012.
- free guidelines. general part + type-specific parts (math, tables, graphs, chemistry, diagrams, maps, art, text-only images). no separate charts section, graphs is the closest.
- core ideas: brevity, focus on data, consistent language, use real lists/tables/headers.
- price: free (guidelines are a reference). no price stated because nothing to buy.
- they only tell you WHAT a good description looks like. a human still has to write each one.
supports claim: 1, 4
how solid: strong for what it is (a standards-ish guide from a known group). not a tool, so no performance claim to test.

### APH (American Printing House) accessible textbook order rules
link: https://www.aph.org/accessible-textbook-order-form/
type: nonprofit
notes:
- won't process new braille orders w/ copyright date older than 5 yrs.
- national editions only, no state editions.
- custom orders can't be cancelled/returned once pre-production starts.
- no lead time given ("estimated delivery date" after processing). no prices/fees listed on page.
- federal quota form or PO needed.
- older sources (not opened, search snippet) say conversion can take 6+ months and math/science takes longer. not used as a number.
supports claim: 3, 5
how solid: strong for the rules (it's their own page). weak for wait times (page has no numbers).

### Bookshare
link: https://www.bookshare.org/
type: nonprofit
notes:
- "world's biggest accessible ebook library", 1.3M+ titles (their claim).
- read aloud, karaoke highlight, enlarge, braille. borrow with no waits or due dates (their claim).
- ~10k public domain books free to anyone.
- eligibility + membership price NOT stated on the page. don't quote a price.
- older search snippet (2009 Flat World deal) says students wait weeks without publisher cooperation. old, not used as current.
supports claim: 1, 3, 7
how solid: medium. nonprofit site, but the speed/no-wait claims are self-reported and I couldn't check them.

### PAC PDF Accessibility Checker (PDF/UA Foundation)
link: https://tlos.vt.edu/tools/pac.html
type: free tool
notes:
- FREE ("Cost: Free"). WINDOWS ONLY. Mac listed under "not optimal".
- checks PDF/UA, reports tags, reading order, alt text, headings. AI-assisted checks (their page).
- does NOT fix anything. "cannot remediate accessibility issues", "not effective for remediation". used to verify after you fix in Acrobat.
- VT page doesn't mention manual checks itself.
supports claim: 4, 6
how solid: strong for price/platform/limits (it's a univ page that says it straight). the PAC own site was not opened.

### veraPDF
link: https://verapdf.org/home/
type: free tool (open source)
notes:
- free, open source. dual GPLv3+ and MPLv2+.
- checks all PDF/A parts + PDF/UA-1 and -2 "machine checks" only.
- CLI, desktop GUI, web GUI.
- maintained by Open Preservation Foundation (from search snippet, not on the page i opened).
- site had a "temporarily offline" notice when fetched. may be down.
- machine checks = can't tell you if alt text is GOOD or reading order makes sense. so humans still do that.
supports claim: 6
how solid: strong for license + scope (their own page). medium for maintenance since site was offline when checked.

### MathCAT (DAISY)
link: https://daisy.github.io/MathCAT
type: free tool / research-ish (open source library)
notes:
- converts MathML to speech, braille, and math navigation. open source, on GitHub. license not stated on the page i opened.
- braille: Nemeth + UEB technical (also CMU, Vietnamese, LaTeX, ASCIIMath braille).
- integrated in NVDA (built-in as of 2026.1 per their page), Orca, Dolphin EasyReader, Kurzweil 3000, BrailleBlaster. JAWS speech in English + Spanish only. MS Narrator "announced".
- limits per page: TeX + ASCIIMath INPUT still todo. braille-to-MathML + 2D multi-line braille = future work. repairs bad MathML "conservatively" and sometimes wrong.
- still needs good MathML as INPUT. that's the human/Mathpix step.
supports claim: 1, 2
how solid: strong for scope + limits (their own page, honest about gaps). no independent test opened.

### liblouis
link: https://liblouis.io/
type: free tool (open source)
notes:
- braille translator + back-translator. LGPL (library), GPL (CLI tools).
- contracted + uncontracted for many languages, hyphenation, math braille (Nemeth, Marburg).
- used by NVDA, Orca, BrailleBack, JAWS, ViewPlus.
- page lists NO stated limitations. (could be bc they just don't write them.)
- it does translation, not tagging or alt text. doesn't fix the document structure.
supports claim: 1
how solid: strong for license/use (widely reused, page checked). medium on limits (page says nothing, so absence isn't proof).

### Olli (MIT Visualization Group / CSAIL)
link: http://vis.mit.edu/pubs/olli/
type: research
notes:
- open source JS library. turns a chart into a keyboard-navigable ARIA tree w/ text descriptions, for screen reader users.
- adapters: vega-lite, vega, observable plot. others need to write an adapter.
- authors: Matt Blanco, Jonathan Zong, Arvind Satyanarayan (MIT CSAIL). IEEE VIS 2022 poster.
- price: free (BSD-3-Clause per search snippet, the GitHub license not opened).
- page doesn't list limitations or study results. says "toolkit-specific solutions can limit learnability".
- it's for charts in web pages. doesn't touch lecture PDFs or slides directly.
supports claim: 1, 2, 6
how solid: medium. it's a real academic lab tool, but poster-level evidence and the page has no user study data.

### NVDA (NV Access)
link: https://www.nvaccess.org/about-nvda/
type: free tool (screen reader)
notes:
- free, open source screen reader. "100% free to use globally" (their claim).
- Windows only (Win10/11, Server 2016+).
- developer NV Access Ltd, registered charity + dev company.
- it reads what the document structure gives it. so bad tags = bad experience. this is the reason a lot of the tagging work matters.
supports claim: 1
how solid: strong for price/platform (own site). the "free" part is easy to verify.

### Clemson PDF manual checks guide
link: https://www.clemson.edu/accessibility/digital/guides/pdf/check-accessibility/manual-checks.html
type: research/guide (univ accessibility office)
notes:
- automated checkers can't verify: color/contrast (always flagged "manually check"), descriptive links, tag order/structure, reading order, tab/form order, alt-text ACCURACY (checker only catches empty alt).
- says nothing about auto-tag reliability. just says walk the tag tree.
- basically a list of "this is what humans must do".
supports claim: 4, 6
how solid: strong. it's a university accessibility office doing a manual checklist, not selling anything.

---

## summary (3 lines)
- every tool that does tagging/remediation (Acrobat auto-tag, CommonLook, Equidox, Mathpix) says or shows a human still has to check tables, reading order, alt text, and math. the independent reviews agree; the vendor pages mostly admit it too.
- free checkers (PAC, veraPDF) only check, they don't fix, and PAC is Windows only; braille/speech tools (liblouis, MathCAT, NVDA) are strong and free but they only work if the document structure is already right.
- pricing is mostly not published (Equidox, CommonLook, Bookshare membership, Mathpix); the only confirmed public prices were free-tool ones and APH's rules (no fees listed). DocAble and AbleDocs still need better sources.
