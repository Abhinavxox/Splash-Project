# How a PDF reaches a screen reader

1. A PDF holds drawing instructions. It can also hold tags that say what each part is and in which order to read it. Most lecture PDFs have no tags.
2. The viewer builds an accessibility tree from the tags. Without tags it guesses from the drawing order, and pictures with no description are announced as a graphic or skipped.
3. The screen reader (NVDA, JAWS, VoiceOver) reads that tree as speech. The same text goes to a braille display through Liblouis. Math stored as MathML is read through MathCAT.

There is no special NVDA format. The screen reader reads whatever the file contains, so the missing meaning has to be added to the file itself.
