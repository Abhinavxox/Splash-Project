# Working release: lecture PDF to accessible HTML

This turns any lecture slide PDF into one accessible HTML page that a screen reader user can read on their own. The definition and success criteria are in `docs/impact-criteria-and-release.md`. Why it is designed this way is in `docs/design-rationale.md`.

```
PDF → page images + text layer → vision model describes each slide → accessible HTML → runs.csv (time, cost)
```

It is a fixed pipeline with one model call per slide. It is not an agent.

## Run it

Needs `poppler` (pdftoppm, pdftotext, pdfinfo) and `pandoc` (`brew install poppler pandoc`), Python 3.10 or newer, and an Anthropic API key.

```bash
cd prototype
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
export ANTHROPIC_API_KEY=...        # your own key; never commit it
.venv/bin/python run.py path/to/lecture.pdf                 # whole lecture
.venv/bin/python run.py path/to/lecture.pdf --pages 20-25   # some slides
```

The output goes to `out/<pdf name>/<pdf name>-accessible.html`. Open it in any browser with VoiceOver or NVDA.

## Files

| File | Role |
|---|---|
| `run.py` | Command line entry. Renders pages, calls the describer, builds the page, logs the run |
| `describe.py` | Vision model call (Claude Opus 5.5) with a fixed prompt and JSON schema. The rules come from ERQ1–ERQ4. Results are cached per page in `out/.../descriptions/`, so a re-run costs nothing |
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

- The model is `claude-opus-5-5` with server-side fallback on: if the model declines a slide, the API retries it on a fallback model in the same call. A slide that still fails gets a clear "could not be described" note on the page and is listed in `runs.csv`. The run does not stop.
- Cost uses the list price in `describe.py` (USD 4 per million input tokens, USD 20 per million output tokens). Convert to CAD in the cost sheet.
- `out/` and `.venv/` are not committed. Test outputs from course PDFs stay local.
