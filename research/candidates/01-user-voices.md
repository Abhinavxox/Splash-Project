# 01 user voices - candidates (rough notes)

heads up: only got 5 sources I could actually open. most of the youtube / podcast / applevis / reddit r/Blind stuff either 403'd, cert-errored, or didn't show up in search. search for youtube only gave text forum threads, no real video titles. so this is thin. see "not opened" at bottom.

---

### WebAIM Screen Reader User Survey #10 (results page)
https://webaim.org/blog/screen-reader-user-survey-10-results/
type: survey
notes:
- survey #10, 1539 respondents. latest one I could find, didnt see a newer edition
- NO PDF / document / table / math data on the page. checked, nothing. only a reader comment asking about PDF bookmarks, quoting HHS
- biggest barrier called out = CAPTCHA. "by far the most problematic barrier"
- only 34.6% said web access improved over last year (39.3% in 2021)
supports claim: 1 (users rely on screen readers)
how solid: strong for "people use screen readers" (big n, real survey). weak for our actual claim since it says nothing about PDFs/slides. dont cite it for slides.

### UW CSE 443 "Accessibility-Preserving Presentation-to-HTML Converter" readme
https://courses.cs.washington.edu/courses/cse443/26wi/projects/slides/readme.html
type: survey? no -> this is a student project writeup (kinda a tool proposal). list it under forum-ish/other
notes:
- says UW CSE lecture slide PDFs are "built for sighted viewing"
- 3 named problems: slides "lack proper heading structure for individual slides"; tables "with no screen reader navigation support"; images/charts "without meaningful alt text"
- its a student team project, not a user quote. they dont quote a blind student
supports claim: 2 (slides lose formulas tables diagrams)
how solid: weak-medium. matches exactly what we are claiming, but it is other students describing the problem, not users. good for showing the problem exists, bad as "users said". (also note: that project is basically our idea, could be seen as competition / overlap)

### r/Professors thread on new accessibility rules (snapshot)
https://reddit.sentinel-team.org/posts/1qcqf6v/snapshots/2026-01-15T05%3A00%3A22.463814Z
type: forum
notes:
- NOT a blind student, its instructors. subreddit is r/Professors
- instructor: google slides "cannot save to digitally accessible PDFs at this point", suggests saving from recent powerpoint instead
- canvas accessibility score "~67%, mostly because not all of my slides have titles"; accessibility office said "don't stress about this"
- one commenter: a blind student can currently get human help for stuff the screen reader cant handle, asks if the new rules take that away. one says their college "believe[s] nobody will actually hit the April deadline"
supports claim: 4 (manual fixing costly), 5 (institutions required)
how solid: medium. real, specific, shows the slide-title problem and the workload. but it is instructors, so its their view, not student view. also the "nobody will hit deadline" line goes a bit against urgency.

### NABS-L mailing list msg (blind CS course / screen reader tutorials)
https://nfbnet.org/pipermail/nabs-l_nfbnet.org/2024-February/052731.html
type: forum (mailing list, NFB NABS-L)
notes:
- student asking about a college computer concepts course; she says screen reader / braille youtube tutorials are "made for sighted teachers" so they didnt help her
- repliers: course relies heavily on the mouse, will likely be ineffective. JAWS can analyze Word formatting to find problems
- nothing about PDFs or slides directly
supports claim: 1 (users rely on screen readers) and 6 (current tools fall short - general, not slides)
how solid: medium. real first-person user voice, its a list so sort of public. off topic from PDFs though. good for "students rely on help from others" flavour.

### APH Connect Center - Accessible Teaching Strategies for Blind College Students
https://aphconnectcenter.org/accommodation/accessible-teaching-strategies-for-blind-college-students/
type: other (guidance page, not user voices)
notes:
- says "dont use images [on your lecture slides] - use words!" (prof quote)
- lists PDF as ONE of several formats to offer (word, pdf, print, large print). does not say PDFs are inaccessible
- says develop syllabus and reading materials ahead of semester in formats all students can use
supports claim: 5 (institutions required) kinda, 2 (slides)
how solid: medium as guidance, weak as user voice. it mostly tells profs to adjust, which is kinda against "its a fundamental problem".

---

## not opened (dont cite yet)
- OSU "providing accessible course content for blind low vision students" (.pdf and .docx) -> cert rejected both. only saw search snippet saying Word->PDF is searchable by default and flat PDFs need OCR. NOT verified.
- AppleVis "last update inserting equations pages not accessible" -> 403. snippet only: 2018-ish post about Pages VoiceOver equations. about Pages not PDFs, old.
- NFB Access On episode list (mypodcastdata) -> 403. search snippet mentions a Scribe for Documents episode, not verified
- UNT lecture slides accommodation PDF -> cert rejected. snippet only: slides as accommodation limited to private study
- Tyndale slide accommodation guide -> not opened
- Axessibility (unito) paper -> got binary pdf back, couldnt read. dont cite
- Medium "key findings WebAIM 2024" -> 403
- YouTube: search returned no real blind-student CS / NVDA math videos with titles. need another try with different queries or a logged-in search

## goes against us
- WebAIM survey #10 has nothing on PDFs/docs. dont claim survey data on slides
- APH guidance treats PDF as one of several normal formats, and the r/Professors thread shows a sighted-side view that it's "okay to just do your best"
- the UW project is basically the same problem statement, so its not clear what's new
- a blind student in the r/Professors thread already gets human help for stuff the SR cant handle, so "students wait forever" might be overstated. need actual wait-time evidence (nothing found yet)

## 3 line summary
1. only 5 real sources opened. the strongest one for our claim is the UW slides readme (problem stated but its students not users), and the r/Professors thread (instructors saying slides lack titles and workload is high).
2. actual blind-user voices on PDFs/math/diagrams are basically missing from what I could reach. youtube, applevis, reddit r/Blind, access on are all blocked or empty so far.
3. WebAIM survey doesnt cover documents at all, so we need another source for "PDFs are a problem" and for the wait time claim.
