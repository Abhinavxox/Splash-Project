"""Build one accessible HTML page for a lecture (release step 3).

Per-student settings from docs/design-rationale.md:
  ERQ3  MathML for screen readers, plus the LaTeX source
  ERQ4  real tables with header cells
  ERQ5  plain semantic HTML, one heading per slide, no plugin
  ERQ6  the original slide image kept, zoomable, for low vision readers
  ERQ10 brief/full depth setting, remembered between visits
"""
import base64
import html
import pathlib
import re
import subprocess

e = html.escape


def latex_to_mathml(latex):
    out = subprocess.run(
        ["pandoc", "-f", "markdown", "-t", "html", "--math-method=mathml"],
        input=f"$${latex}$$", capture_output=True, text=True, check=True).stdout
    m = re.search(r"<math.*</math>", out, re.S)
    return m.group(0) if m else f"<code>{e(latex)}</code>"


def table_html(t):
    rows = t["rows"]
    if not rows:
        return ""
    width = max(len(r) for r in rows)
    head = "".join(f'<th scope="col">Column {c + 1}</th>' for c in range(width))
    body = "".join(
        f'<tr><th scope="row">Row {r + 1}</th>' + "".join(f"<td>{e(str(v))}</td>" for v in row) + "</tr>"
        for r, row in enumerate(rows))
    return (f'<div class="wrap"><table><caption>{e(t["caption"])}</caption>'
            f'<thead><tr><td></td>{head}</tr></thead><tbody>{body}</tbody></table></div>')


def slide_html(page, title, text, d, image_path):
    sid = f"s{page}"
    img = base64.standard_b64encode(pathlib.Path(image_path).read_bytes()).decode()
    parts = "".join(f"<li>{e(p)}</li>" for p in d["parts"])
    maths = "".join(
        f'<p>{e(m["spoken_context"])}</p>{latex_to_mathml(m["latex"])}'
        f'<details><summary>LaTeX source</summary><pre><code>{e(m["latex"])}</code></pre></details>'
        for m in d["math"])
    tables = "".join(table_html(t) for t in d["tables"])
    detail = ""
    if d["has_visual"]:
        detail = f"""<div class="full">
  {'<h3>Parts</h3><ul>' + parts + '</ul>' if parts else ''}
  {'<h3>How the parts relate</h3><p>' + e(d['relationships']) + '</p>' if d['relationships'] else ''}
  {'<h3>Formulas</h3>' + maths if maths else ''}
  {'<h3>Tables</h3>' + tables if tables else ''}
</div>"""
    slide_text = f"<h3>Slide text</h3><p>{e(text)}</p>" if text else ""
    return f"""
<section aria-labelledby="{sid}">
  <h2 id="{sid}">Slide {page}: {e(title)}</h2>
  {slide_text}
  <h3>Overview</h3><p>{e(d['overview'])}</p>
  {detail}
  <details class="img"><summary>Original slide image</summary>
    <a href="data:image/png;base64,{img}" target="_blank"><img src="data:image/png;base64,{img}" alt="Original image of slide {page}. The description above gives its content."></a>
  </details>
</section>"""


PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} (accessible version)</title>
<style>
:root{{--bg:#fff;--fg:#1b1f23;--line:#c9ced3;--accent:#0b5cad}}
@media (prefers-color-scheme:dark){{:root{{--bg:#16191c;--fg:#e7eaed;--line:#3a4046;--accent:#7ab7ff;color-scheme:dark}}}}
:root.contrast{{--bg:#000;--fg:#fff;--line:#fff;--accent:#ff0;color-scheme:dark}}
body{{background:var(--bg);color:var(--fg);font:1.0625rem/1.6 system-ui,sans-serif;margin:0;padding:2rem 1rem}}
main{{max-width:48rem;margin:0 auto}}
section{{border-top:1px solid var(--line);padding-top:.75rem;margin-top:1.5rem}}
.wrap{{overflow-x:auto}} table{{border-collapse:collapse;margin:.6rem 0}}
th,td{{border:1px solid var(--line);padding:.25rem .5rem;text-align:right}}
caption{{text-align:left;font-weight:600;padding:.25rem 0}}
img{{max-width:100%;height:auto;border:1px solid var(--line)}}
button{{font:inherit;padding:.4rem .8rem;margin-right:.5rem;border:2px solid var(--accent);background:transparent;color:var(--fg);border-radius:.3rem}}
:focus-visible{{outline:3px solid var(--accent);outline-offset:2px}}
.brief .full{{display:none}}
.sr{{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)}}
</style>
</head>
<body>
<main>
<h1>{title}, accessible version</h1>
<p>Generated automatically from the original PDF. Each slide has a heading. Under it are the slide text, an overview of any visual, then the parts, how they relate, formulas and tables.</p>
<div role="group" aria-label="Reading settings">
  <button id="depth" aria-pressed="false">Brief mode (overview only)</button>
  <button id="contrast" aria-pressed="false">High contrast</button>
</div>
<p id="status" role="status" class="sr"></p>
{body}
</main>
<script>
(function(){{
  var root=document.documentElement, st=document.getElementById('status');
  function bind(id,cls,el,msgOn,msgOff){{
    var b=document.getElementById(id), on=localStorage.getItem(id)==='1';
    function set(v){{on=v;el.classList.toggle(cls,v);b.setAttribute('aria-pressed',v);localStorage.setItem(id,v?'1':'0');}}
    set(on);
    b.addEventListener('click',function(){{set(!on);st.textContent=on?msgOn:msgOff;}});
  }}
  bind('depth','brief',document.body,'Brief mode on. Only overviews are shown.','Full mode on. All details are shown.');
  bind('contrast','contrast',root,'High contrast on.','High contrast off.');
}})();
</script>
</body>
</html>"""


def build(title, slides, out_path):
    """slides: list of dicts with page, title, text, description, image."""
    body = "".join(slide_html(s["page"], s["title"], s["text"], s["description"], s["image"]) for s in slides)
    pathlib.Path(out_path).write_text(PAGE.format(title=e(title), body=body))
