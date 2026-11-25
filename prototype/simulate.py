"""Simulated usability test: AI personas of blind and low vision students
try each prototype variant and answer comprehension questions.

THIS IS NOT IMPACT EVIDENCE. A language model pretending to be blind is not
a blind student. We use it as a pre-test, before real sessions, to:
  - compare prototype variants cheaply and find obvious failures,
  - check that the questions and the session script work,
  - see which kinds of students a variant may fail (dimensions D1-D6 in
    docs/design-rationale.md).
Only M2 sessions with real participants count toward the impact claim.

Prototype variants (what the persona can read):
  P0  baseline: what a screen reader gets from the original PDF (text layer only)
  P1  release, full mode: overview, parts, relationships, formulas, tables
  P2  release, brief mode: overview only
  P3  brief mode plus up to 3 follow-up questions answered from the slide (R2)

Usage:
  .venv/bin/python simulate.py --run out/lecture2 --questions ../research/study/questions-draft.json
"""
import argparse
import concurrent.futures as cf
import json
import pathlib
import subprocess
import time

from google.genai import types

import describe

MODEL = "gemini-3.6-flash"

PERSONAS = {
    "A": "You were born blind (no light perception). You are a third-year computer science student and an expert NVDA screen reader user on Windows, listening at high speed. You have no visual memory, so descriptions that say what something 'looks like' or use colour mean nothing to you. You are comfortable with LaTeX.",
    "B": "You lost your sight at 19 from an illness and are now a second-year engineering student. You use VoiceOver on a Mac at an intermediate level. You remember what charts and diagrams look like, but navigating long pages is still slow for you.",
    "C": "You have low vision (legally blind, about 5 percent central vision). You are a math student. You use screen magnification at 400 percent plus speech for long text. You can see large shapes if you zoom, but small labels and numbers are unreadable for you.",
    "D": "You were born blind and read mainly in braille on a refreshable braille display. You are taking a required statistics course outside your major (sociology). You are new to most software and get frustrated when a page is long or confusing. Math notation is hard for you.",
    "E": "You are blind and an expert screen reader user in a fourth-year data science program. You are short on time: you are reading this ten minutes before the lecture and want the main idea fast, with detail only if you need it.",
}

PERSONA_RULES = """Act as this student honestly, including your frustrations. You can ONLY use the content given to you below, exactly as your screen reader or braille display presents it. You cannot see the slide. If the content does not let you answer a question, say "I can't tell from what I have" rather than guessing. Do not use outside knowledge of the topic."""

ANSWER_SCHEMA = {
    "type": "object",
    "properties": {
        "answers": {"type": "array", "items": {"type": "string"}},
        "effort": {"type": "integer", "description": "1 = effortless, 5 = exhausting"},
        "confidence": {"type": "integer", "description": "1 = not at all, 5 = fully confident in my answers"},
        "needs_sighted_help": {"type": "boolean"},
        "frustrations": {"type": "array", "items": {"type": "string"}},
        "what_worked": {"type": "array", "items": {"type": "string"}},
    },
    "required": ["answers", "effort", "confidence", "needs_sighted_help", "frustrations", "what_worked"],
}

JUDGE_SCHEMA = {
    "type": "object",
    "properties": {"scores": {"type": "array", "items": {"type": "number"}}},
    "required": ["scores"],
}

QUESTIONS_SCHEMA = {
    "type": "object",
    "properties": {"questions": {"type": "array", "items": {"type": "string"}}},
    "required": ["questions"],
}


def call(client, system, content, schema, retries=3):
    for attempt in range(retries):
        try:
            r = client.models.generate_content(
                model=MODEL, contents=content,
                config=types.GenerateContentConfig(system_instruction=system,
                                                   response_mime_type="application/json",
                                                   response_json_schema=schema))
            return json.loads(r.text)
        except Exception:
            if attempt == retries - 1:
                raise
            time.sleep(2 * (attempt + 1))


# --- what each variant gives the student -------------------------------------------------

def pdf_text(pdf, page):
    return subprocess.run(["pdftotext", "-f", str(page), "-l", str(page), pdf, "-"],
                          capture_output=True, text=True, check=True).stdout.strip()


def baseline(pdf, page):
    text = pdf_text(pdf, page)
    return (f"Screen reader output for page {page} of the original lecture PDF. "
            f"The PDF is untagged, so images are skipped and only the text layer is read:\n\n{text or '(no text)'}")


def linear(d, text, full):
    out = [f"Slide text: {text}", f"Heading: Overview. {d['overview']}"]
    if full and d["has_visual"]:
        if d["parts"]:
            out.append("Heading: Parts. List: " + " | ".join(d["parts"]))
        if d["relationships"]:
            out.append(f"Heading: How the parts relate. {d['relationships']}")
        for m in d["math"]:
            out.append(f"Heading: Formulas. {m['spoken_context']} Math: {m['latex']}")
        for t in d["tables"]:
            rows = "; ".join(f"row {i + 1}: " + ", ".join(r) for i, r in enumerate(t["rows"]))
            out.append(f"Table: {t['caption']}. {rows}")
    return "\n".join(out)


# --- one trial ----------------------------------------------------------------------------

def trial(client, persona, variant, slide, ctx):
    page, questions = slide["page"], [q["q"] for q in slide["questions"]]
    system = PERSONAS[persona] + "\n\n" + PERSONA_RULES
    d, text, image = ctx["desc"][page], ctx["text"][page], ctx["image"][page]
    followups = []
    if variant == "P0":
        content = baseline(ctx["pdf"], page)
    elif variant == "P1":
        content = linear(d, text, full=True)
    else:
        content = linear(d, text, full=False)
    if variant == "P3":
        asked = call(client, system,
                     [f"{content}\n\nYou may ask up to 3 follow-up questions about this slide to understand it. "
                      f"Ask what YOU would want to know; you have not seen any test questions."],
                     QUESTIONS_SCHEMA)["questions"][:3]
        for q in asked:
            a = call(client, "You answer a blind student's question about one lecture slide. Answer only from the slide, in plain words, without relying on colour or visual comparison. Keep it short.",
                     [types.Part.from_bytes(data=image, mime_type="image/png"), q],
                     {"type": "object", "properties": {"answer": {"type": "string"}}, "required": ["answer"]})["answer"]
            followups.append({"q": q, "a": a})
        content += "\n\nYour follow-up questions and the answers you got:\n" + "\n".join(
            f"Q: {f['q']}\nA: {f['a']}" for f in followups)
    qs = "\n".join(f"{i + 1}. {q}" for i, q in enumerate(questions))
    res = call(client, system, [f"{content}\n\nNow answer these questions, one answer per question, in order:\n{qs}\n\n"
                                f"Then rate your effort and confidence, say whether you would need a sighted person, "
                                f"and list frustrations and what worked, as this student."], ANSWER_SCHEMA)
    keys = "\n".join(f"{i + 1}. Q: {q['q']} | Correct: {q['key']} | Student: "
                     f"{res['answers'][i] if i < len(res['answers']) else '(none)'}"
                     for i, q in enumerate(slide["questions"]))
    scores = call(client, "You grade short answers against an answer key. Score 1 if correct, 0.5 if partly correct, 0 if wrong or 'can't tell'. Be strict about numbers.",
                  [keys], JUDGE_SCHEMA)["scores"][:len(questions)]
    return {"persona": persona, "variant": variant, "page": page, "score": sum(scores) / len(questions),
            "scores": scores, "followups": followups, **res}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True, help="output folder of run.py (has descriptions/ and images/)")
    ap.add_argument("--questions", required=True)
    ap.add_argument("--out", default="../results/sim")
    args = ap.parse_args()

    _, _, client = describe.load_backend()
    qfile = json.loads(pathlib.Path(args.questions).read_text())
    run = pathlib.Path(args.run)
    pdf = str((pathlib.Path(args.questions).parent / ".." / ".." / qfile["pdf"]).resolve())
    ctx = {"pdf": pdf, "desc": {}, "text": {}, "image": {}}
    for s in qfile["slides"]:
        p = s["page"]
        ctx["desc"][p] = json.loads((run / "descriptions" / f"page-{p:03d}.json").read_text())
        ctx["text"][p] = pdf_text(pdf, p)
        ctx["image"][p] = (run / "images" / f"page-{p:03d}.png").read_bytes()

    jobs = [(pe, v, s) for pe in PERSONAS for v in ["P0", "P1", "P2", "P3"] for s in qfile["slides"]]
    results = []
    with cf.ThreadPoolExecutor(8) as ex:
        futs = {ex.submit(trial, client, pe, v, s, ctx): (pe, v, s["page"]) for pe, v, s in jobs}
        for f in cf.as_completed(futs):
            try:
                results.append(f.result())
            except Exception as err:
                print("failed", futs[f], err)
    out = pathlib.Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    results.sort(key=lambda r: (r["persona"], r["variant"], r["page"]))
    (out / "trials.json").write_text(json.dumps(results, indent=2))
    print(f"{len(results)} of {len(jobs)} trials written to {out / 'trials.json'}")


if __name__ == "__main__":
    main()
