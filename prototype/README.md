# Working release: lecture PDF to accessible HTML

This turns any lecture slide PDF into one accessible HTML page that a screen reader user can read on their own. The definition and success criteria are in `docs/impact-criteria-and-release.md`. Why it is designed this way is in `docs/design-rationale.md`.

```
PDF → page images + text layer → vision model describes each slide → accessible HTML → runs.csv (time, cost)
```

It is a fixed pipeline with one model call per slide. It is not an agent.

## Run it

Needs `poppler` (pdftoppm, pdftotext, pdfinfo) and `pandoc` (`brew install poppler pandoc`), Python 3.10 or newer, and a Gemini (or Anthropic) API key.

```bash
cd prototype
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
# put GEMINI_API_KEY=... in prototype/.env (git-ignored)
.venv/bin/python run.py path/to/lecture.pdf                 # whole lecture
.venv/bin/python run.py path/to/lecture.pdf --pages 20-25   # some slides
```

The output goes to `out/<pdf name>/<pdf name>-accessible.html`. Open it in any browser with VoiceOver or NVDA.

## Files

| File | Role |
|---|---|
| `run.py` | Command line entry. Renders pages, calls the describer, builds the page, logs the run |
| `describe.py` | Vision model call (Gemini 3.6 Flash by default; Claude Opus 5.5 with `SPLASH_BACKEND=claude`) with a fixed prompt and JSON schema. The rules come from ERQ1–ERQ4. Results are cached per page in `out/.../descriptions/`, so a re-run costs nothing |
| `build_html.py` | HTML builder: headings per slide, layered description, MathML plus LaTeX source, real tables, the original image as a separate file. A **Reading settings** panel (standard labelled controls) lets each student set the detail level, text size, high contrast, whether to include the slide text and the image, and whether to expand LaTeX. Settings are saved in the browser |
| `simulate.py` | Simulated persona pre-test (not impact evidence). See `results/sim/summary.md` |
| `runs.csv` | One row per run: time taken, tokens and cost in USD. This is the evidence for M3 and M4. Commit it |
| `make_accessible.py`, `slides.json` | **Superseded.** The Oct 25 sketch with hand-written descriptions for 3 slides. Kept as project history; `run.py --offline slides.json` uses it only to test the pipeline without an API key |

## Measured so far

| Run | Slides | Time | Failed |
|---|---|---|---|
| CS231n lecture 2, slides 22, 23, 52 | 3 | 32.8 s (one at a time) | 0 |
| CS231n lecture 2, whole lecture, fresh, 8 in parallel | 98 | 115.6 s | 0 |
| Georgia Tech computer vision lecture 2, slides 1–15 (image-heavy) | 15 | 20.1 s | 0 |

The 10:44 row in `runs.csv` was a resumed run that reused 75 cached slides. Use the 10:46 row for M3.

## Notes

- Keys: `GEMINI_API_KEY` (or `ANTHROPIC_API_KEY`) in the environment or in `prototype/.env`, which git ignores. Never commit a key.
- A slide that still fails gets a clear "could not be described" note on the page and is listed in `runs.csv`. The run does not stop.
- Cost: the Gemini price is not confirmed, so `runs.csv` shows `n/a`. Set `SPLASH_PRICE_IN` and `SPLASH_PRICE_OUT` (USD per million tokens) from Google's pricing page, then compute cost from the logged tokens. Convert to CAD in the cost sheet.
- `out/` and `.venv/` are not committed. Test outputs from course PDFs stay local.
