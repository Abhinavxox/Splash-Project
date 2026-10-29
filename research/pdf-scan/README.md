# Lecture PDF scan

Public lecture PDFs from Stanford (CS231n, CS229), CMU (15-213), Princeton (COS 226), UBC (CPSC 340), Berkeley (CS 189) and Georgia Tech (computer vision). Links that worked are in `urls.txt`, `urls2.txt` and `urls-ok.txt`. The PDFs are not committed. Run the download loop again to get them.

Scripts
- `scan.py` pages, tagged or not, images per page, pages that are mostly picture (images and under 25 words of text)
- `tags.py` Figure and Formula tags in the structure tree and how many carry alt text

Results from 27 files and 1852 pages, run 2026-10-29

- 12 of 27 files have no tags at all, so a screen reader gets no structure and no image descriptions
- 855 of 1852 pages have images
- 376 of 1852 pages are mostly picture, so their main content is in images
- 7293 figure tags across the tagged files, only 237 have alt text, about 3 percent
- only 6 formula tags in all 27 files and none have alt text
- 11 of 27 files have any figure alt text at all

Limits
- 27 files from 7 computer science courses, not a random sample of all lectures
- we did not check whether the alt text that exists is actually useful
- formulas drawn as text or images are not counted as formulas, so the formula numbers understate the problem
- the mostly picture threshold of 25 words is our own choice
