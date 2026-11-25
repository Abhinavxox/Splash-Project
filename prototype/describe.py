"""Describe one slide image with a vision model (release step 2).

Returns the same structure the HTML builder uses: overview, parts,
relationships, math (LaTeX), tables. Results are cached per page so a
re-run of the same PDF costs nothing.

The rules in PROMPT come from docs/design-rationale.md:
  ERQ1 three layers, ERQ2 no visual analogies or colour-only meaning,
  ERQ3 formulas as LaTeX, ERQ4 table values.
"""
import base64
import json
import pathlib

import anthropic

MODEL = "claude-opus-5-5"
# USD per million tokens for MODEL (input, output). Used for the run log (M4).
PRICE = (4.00, 20.00)

PROMPT = """You are describing one lecture slide for a university student who is blind or has low vision and uses a screen reader. The student must be able to learn everything a sighted classmate learns from this slide.

Rules:
- Describe what the slide teaches, not how it looks.
- Never rely on visual comparison ("looks like a tree") or colour alone. If colour carries meaning, say what it encodes ("the weights, shown in red").
- State structure, position and relationships explicitly: what connects to what, what points where, what is inside what, what is larger or smaller.
- Read every label, number and axis exactly as written. Do not invent anything you cannot see. If something is unreadable, say so.
- overview: 1-3 sentences, what the visual is and its main point.
- parts: one entry per labelled element, in a sensible reading order.
- relationships: how the parts work together, i.e. the idea the visual teaches. Include a worked example if the slide shows one.
- math: every formula as LaTeX, with one plain sentence of context.
- tables: every grid of values, row by row.
- If the slide is text only with no meaningful visual, set has_visual to false and leave parts, relationships, math and tables empty."""

SCHEMA = {
    "type": "object",
    "properties": {
        "has_visual": {"type": "boolean"},
        "overview": {"type": "string"},
        "parts": {"type": "array", "items": {"type": "string"}},
        "relationships": {"type": "string"},
        "math": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "latex": {"type": "string"},
                    "spoken_context": {"type": "string"},
                },
                "required": ["latex", "spoken_context"],
                "additionalProperties": False,
            },
        },
        "tables": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "caption": {"type": "string"},
                    "rows": {"type": "array", "items": {"type": "array", "items": {"type": "string"}}},
                },
                "required": ["caption", "rows"],
                "additionalProperties": False,
            },
        },
    },
    "required": ["has_visual", "overview", "parts", "relationships", "math", "tables"],
    "additionalProperties": False,
}


class DescribeError(Exception):
    pass


def describe(client, image_path, slide_text, cache_path):
    """Return (description dict, usage dict). Uses the cache when present."""
    cache_path = pathlib.Path(cache_path)
    if cache_path.exists():
        return json.loads(cache_path.read_text()), {"input_tokens": 0, "output_tokens": 0, "cached": True}

    data = base64.standard_b64encode(pathlib.Path(image_path).read_bytes()).decode()
    try:
        response = client.beta.messages.create(
            model=MODEL,
            max_tokens=16000,
            output_config={"effort": "medium", "format": {"type": "json_schema", "schema": SCHEMA}},
            # On a policy decline, the API retries on a fallback model in the same call.
            betas=["server-side-fallback-2026-07-01"],
            fallbacks="default",
            system=PROMPT,
            messages=[{
                "role": "user",
                "content": [
                    {"type": "image", "source": {"type": "base64", "media_type": "image/png", "data": data}},
                    {"type": "text", "text": f"Text layer of this slide (may be empty or incomplete):\n{slide_text}"},
                ],
            }],
        )
    except anthropic.RateLimitError as e:
        raise DescribeError(f"rate limited: {e}") from e
    except anthropic.APIStatusError as e:
        raise DescribeError(f"API error {e.status_code}: {e.message}") from e
    except anthropic.APIConnectionError as e:
        raise DescribeError(f"connection failed: {e}") from e

    if response.stop_reason == "refusal":
        raise DescribeError("model declined to describe this slide")
    if response.stop_reason == "max_tokens":
        raise DescribeError("description was cut off (max_tokens)")

    text = next(b.text for b in response.content if b.type == "text")
    result = json.loads(text)
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    cache_path.write_text(json.dumps(result, indent=2))
    usage = {"input_tokens": response.usage.input_tokens,
             "output_tokens": response.usage.output_tokens, "cached": False}
    return result, usage


def cost_usd(usage):
    return usage["input_tokens"] / 1e6 * PRICE[0] + usage["output_tokens"] / 1e6 * PRICE[1]
