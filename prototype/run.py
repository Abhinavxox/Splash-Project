"""Turn any lecture PDF into one accessible HTML page.

Usage:
  python3 run.py LECTURE.pdf [--out DIR] [--pages 3-10] [--offline DESCRIPTIONS.json]

Steps (docs/impact-criteria-and-release.md, section 2):
  1. Render each page to an image and read its text layer (pdftoppm, pdftotext).
  2. Describe each slide with a vision model (describe.py), cached per page.
  3. Build one accessible HTML page (build_html.py).
  4. Append one row per run to runs.csv: time, pages, tokens, cost (M3, M4).

--offline takes descriptions from a JSON file ({"slides": [{"page": N, ...}]})
instead of calling the API. Use it only for testing the pipeline. Runs made
with it are marked "offline" in runs.csv and do not count as release runs.
"""
import argparse
import csv
import datetime
import json
import pathlib
import subprocess
import sys
import time

import build_html
import describe

HERE = pathlib.Path(__file__).parent


def page_count(pdf):
    info = subprocess.run(["pdfinfo", pdf], capture_output=True, text=True, check=True).stdout
    return int(next(l.split()[-1] for l in info.splitlines() if l.startswith("Pages:")))


def page_text(pdf, page):
    return subprocess.run(["pdftotext", "-layout", "-f", str(page), "-l", str(page), pdf, "-"],
                          capture_output=True, text=True, check=True).stdout.strip()


def render(pdf, page, out_dir):
    prefix = out_dir / f"page-{page:03d}"
    subprocess.run(["pdftoppm", "-png", "-r", "110", "-singlefile", "-f", str(page), "-l", str(page),
                    pdf, str(prefix)], check=True)
    return prefix.with_suffix(".png")


def parse_pages(spec, n):
    if not spec:
        return list(range(1, n + 1))
    pages = set()
    for part in spec.split(","):
        a, _, b = part.partition("-")
        pages.update(range(int(a), int(b or a) + 1))
    return sorted(p for p in pages if 1 <= p <= n)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pdf")
    ap.add_argument("--out", default=None, help="output folder (default: out/<pdf name>)")
    ap.add_argument("--pages", default=None, help="e.g. 1-5,9 (default: all)")
    ap.add_argument("--offline", default=None, help="descriptions JSON, skips the API (testing only)")
    args = ap.parse_args()

    pdf = pathlib.Path(args.pdf).resolve()
    name = pdf.stem
    out = pathlib.Path(args.out or HERE / "out" / name)
    (out / "images").mkdir(parents=True, exist_ok=True)

    offline = None
    client = None
    if args.offline:
        offline = {s["page"]: s for s in json.loads(pathlib.Path(args.offline).read_text())["slides"]}
    else:
        import anthropic
        client = anthropic.Anthropic()

    pages = parse_pages(args.pages, page_count(str(pdf)))
    start = time.time()
    slides, errors = [], []
    tokens_in = tokens_out = 0
    for p in pages:
        text = page_text(str(pdf), p)
        image = render(str(pdf), p, out / "images")
        title = next((l.strip() for l in text.splitlines() if l.strip()), f"Slide {p}")
        if offline is not None:
            d = offline.get(p)
            if d is None:
                continue
            d = {"has_visual": True, **d}
        else:
            try:
                d, usage = describe.describe(client, image, text, out / "descriptions" / f"page-{p:03d}.json")
            except describe.DescribeError as err:
                errors.append((p, str(err)))
                print(f"page {p}: {err}", file=sys.stderr)
                d = {"has_visual": False, "overview": f"This slide could not be described automatically ({err}).",
                     "parts": [], "relationships": "", "math": [], "tables": []}
                usage = {"input_tokens": 0, "output_tokens": 0}
            tokens_in += usage["input_tokens"]
            tokens_out += usage["output_tokens"]
        slides.append({"page": p, "title": title, "text": text, "description": d, "image": image})
        print(f"page {p} done", file=sys.stderr)

    html_path = out / f"{name}-accessible.html"
    display = name.split("_")[-1] if name.startswith("http") else name
    build_html.build(display.replace("_", " ").replace("-", " "), slides, html_path)
    seconds = round(time.time() - start, 1)
    cost = describe.cost_usd({"input_tokens": tokens_in, "output_tokens": tokens_out})

    log = HERE / "runs.csv"
    new = not log.exists()
    with log.open("a", newline="") as f:
        w = csv.writer(f)
        if new:
            w.writerow(["timestamp", "pdf", "pages", "mode", "model", "seconds",
                        "input_tokens", "output_tokens", "cost_usd", "failed_pages"])
        w.writerow([datetime.datetime.now().isoformat(timespec="seconds"), pdf.name, len(slides),
                    "offline" if offline is not None else "live", describe.MODEL, seconds,
                    tokens_in, tokens_out, f"{cost:.4f}", ";".join(str(p) for p, _ in errors)])

    print(f"\nWrote {html_path}\n{len(slides)} slides, {seconds}s, ${cost:.4f} USD, {len(errors)} failed")


if __name__ == "__main__":
    main()
