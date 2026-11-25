"""Describe one slide image with a vision model (release step 2).

Returns the same structure the HTML builder uses: overview, parts,
relationships, math (LaTeX), tables. Results are cached per page so a
re-run of the same PDF costs nothing.

Two backends, chosen with SPLASH_BACKEND (default: gemini):
  gemini  Google Gemini, key in GEMINI_API_KEY (same setup as the Margati backend)
  claude  Anthropic Claude, key in ANTHROPIC_API_KEY

Keys are read from the environment or from prototype/.env (git-ignored).

The rules in PROMPT come from docs/design-rationale.md:
  ERQ1 three layers, ERQ2 no visual analogies or colour-only meaning,
  ERQ3 formulas as LaTeX, ERQ4 table values.
"""
import json
import os
import pathlib

HERE = pathlib.Path(__file__).parent

BACKEND = None  # set by load_backend()
MODELS = {"gemini": "gemini-3.6-flash", "claude": "claude-opus-5-5"}
# USD per million tokens (input, output). The Claude price is the list price.
# The Gemini price is not confirmed: set SPLASH_PRICE_IN / SPLASH_PRICE_OUT
# from Google's pricing page before reporting M4. Unset means cost is "n/a".
PRICES = {"claude": (4.00, 20.00), "gemini": None}

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


def _load_dotenv():
    env = HERE / ".env"
    if env.exists():
        for line in env.read_text().splitlines():
            k, sep, v = line.partition("=")
            if sep and k.strip() and not k.startswith("#"):
                os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))


def load_backend():
    """Return (name, model, client) for the chosen backend."""
    global BACKEND
    _load_dotenv()
    BACKEND = os.environ.get("SPLASH_BACKEND", "gemini")
    if BACKEND == "gemini":
        from google import genai
        if not os.environ.get("GEMINI_API_KEY"):
            raise SystemExit("GEMINI_API_KEY is not set (environment or prototype/.env)")
        return BACKEND, MODELS[BACKEND], genai.Client(api_key=os.environ["GEMINI_API_KEY"])
    if BACKEND == "claude":
        import anthropic
        return BACKEND, MODELS[BACKEND], anthropic.Anthropic()
    raise SystemExit(f"unknown SPLASH_BACKEND {BACKEND!r}; use gemini or claude")


def _gemini(client, image, slide_text):
    from google.genai import errors, types
    try:
        r = client.models.generate_content(
            model=MODELS["gemini"],
            contents=[types.Part.from_bytes(data=image, mime_type="image/png"),
                      f"Text layer of this slide (may be empty or incomplete):\n{slide_text}"],
            config=types.GenerateContentConfig(
                system_instruction=PROMPT,
                response_mime_type="application/json",
                response_json_schema=SCHEMA,
            ),
        )
    except errors.APIError as e:
        raise DescribeError(f"Gemini API error {e.code}: {e.message}") from e
    if not r.text:
        reason = r.candidates[0].finish_reason if r.candidates else "no candidates"
        raise DescribeError(f"empty response ({reason})")
    u = r.usage_metadata
    out_tokens = (u.candidates_token_count or 0) + (getattr(u, "thoughts_token_count", 0) or 0)
    return r.text, {"input_tokens": u.prompt_token_count or 0, "output_tokens": out_tokens}


def _claude(client, image, slide_text):
    import base64
    import anthropic
    try:
        response = client.beta.messages.create(
            model=MODELS["claude"],
            max_tokens=16000,
            output_config={"effort": "medium", "format": {"type": "json_schema", "schema": SCHEMA}},
            # On a policy decline, the API retries on a fallback model in the same call.
            betas=["server-side-fallback-2026-07-01"],
            fallbacks="default",
            system=PROMPT,
            messages=[{"role": "user", "content": [
                {"type": "image", "source": {"type": "base64", "media_type": "image/png",
                                             "data": base64.standard_b64encode(image).decode()}},
                {"type": "text", "text": f"Text layer of this slide (may be empty or incomplete):\n{slide_text}"},
            ]}],
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
    return text, {"input_tokens": response.usage.input_tokens, "output_tokens": response.usage.output_tokens}


def describe(client, image_path, slide_text, cache_path):
    """Return (description dict, usage dict). Uses the cache when present."""
    cache_path = pathlib.Path(cache_path)
    if cache_path.exists():
        return json.loads(cache_path.read_text()), {"input_tokens": 0, "output_tokens": 0}
    image = pathlib.Path(image_path).read_bytes()
    call = _gemini if BACKEND == "gemini" else _claude
    text, usage = call(client, image, slide_text)
    try:
        result = json.loads(text)
    except json.JSONDecodeError as e:
        raise DescribeError(f"model returned invalid JSON: {e}") from e
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    cache_path.write_text(json.dumps(result, indent=2))
    return result, usage


def cost_usd(usage):
    """USD cost, or None when the price for this backend is not set."""
    price = PRICES.get(BACKEND)
    if os.environ.get("SPLASH_PRICE_IN") and os.environ.get("SPLASH_PRICE_OUT"):
        price = (float(os.environ["SPLASH_PRICE_IN"]), float(os.environ["SPLASH_PRICE_OUT"]))
    if price is None:
        return None
    return usage["input_tokens"] / 1e6 * price[0] + usage["output_tokens"] / 1e6 * price[1]
