"""Second search round. Three year/topic groups, then a rule-based screen.

The screen only applies mechanical rules (abstract present, venue present,
mentions software and a management or leadership role). Choosing the final
30 is left to the team.
"""
import csv, json, os, re, time, urllib.parse, urllib.request
from datetime import date

MAILTO = "student@example.com"
GROUPS = {
    "before_2020": {"to": "2019-12-31", "from": "2000-01-01", "per": 15, "queries": [
        '"software engineer" "software manager"', '"engineering manager" software',
        '"software project manager" role', '"technical lead" software team']},
    "2020_onward": {"from": "2020-01-01", "per": 12, "queries": [
        '"software engineer" "software manager"', '"engineering manager" software',
        '"software engineering management"', '"technical lead" software team']},
    "llm_agentic": {"from": "2022-01-01", "per": 10, "queries": [
        '"large language models" software engineering roles',
        '"AI agents" software development team management',
        '"generative AI" software engineers managers']},
}
ROLE = re.compile(r"manag|leader|lead\b|leads\b|supervis", re.I)
SOFT = re.compile(r"software", re.I)

def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": f"coursework-fetch (mailto:{MAILTO})"})
    with urllib.request.urlopen(req, timeout=60) as r: return r.read()

def abstract(inv):
    if not inv: return ""
    return " ".join(w for _, w in sorted((p, w) for w, ps in inv.items() for p in ps))

os.makedirs("pdfs_v2", exist_ok=True)
rows, log, seen = [], [], set()
for g, cfg in GROUPS.items():
    for q in cfg["queries"]:
        f = f"from_publication_date:{cfg['from']},type:article|proceedings-article"
        if "to" in cfg: f += f",to_publication_date:{cfg['to']}"
        url = "https://api.openalex.org/works?" + urllib.parse.urlencode(
            {"search": q, "filter": f, "per-page": cfg["per"], "mailto": MAILTO}, safe=":|,")
        data = json.loads(get(url))
        log.append({"date": date.today().isoformat(), "database": "OpenAlex", "group": g, "query": q,
                    "filters": f, "total_hits": data["meta"]["count"]})
        for w in data["results"]:
            if w["id"] in seen: continue
            seen.add(w["id"])
            src = (w.get("primary_location") or {}).get("source") or {}
            ab = abstract(w.get("abstract_inverted_index"))
            text = (w.get("title") or "") + " " + ab
            reasons = []
            if not ab: reasons.append("no abstract")
            if not src.get("display_name"): reasons.append("no venue")
            if not SOFT.search(text): reasons.append("no mention of software")
            if not ROLE.search(text): reasons.append("no management or leadership role")
            rows.append({"group": g, "title": w.get("title"), "year": w.get("publication_year"),
                         "authors": "; ".join(a["author"]["display_name"] for a in w.get("authorships", [])),
                         "venue": src.get("display_name", ""), "venue_type": src.get("type", ""),
                         "doi": w.get("doi") or "", "cited_by": w.get("cited_by_count"),
                         "open_access": (w.get("open_access") or {}).get("is_oa"),
                         "pdf_url": (w.get("best_oa_location") or {}).get("pdf_url") or "",
                         "passes_screen": "yes" if not reasons else "no",
                         "screen_reason": "; ".join(reasons), "query": q, "abstract": ab, "pdf_file": ""})
        time.sleep(1)

for i, r in enumerate(rows, 1):
    if r["passes_screen"] != "yes" or not r["pdf_url"]: continue
    name = f"{r['group']}_{i:03d}_" + re.sub(r"[^A-Za-z0-9]+", "_", r["title"] or "paper")[:55] + ".pdf"
    try:
        b = get(r["pdf_url"])
        if b[:4] == b"%PDF": open(os.path.join("pdfs_v2", name), "wb").write(b); r["pdf_file"] = name
    except Exception: pass

for fn, d in (("papers_v2.csv", rows), ("search_log_v2.csv", log)):
    with open(fn, "w", newline="") as fh:
        wr = csv.DictWriter(fh, fieldnames=list(d[0].keys())); wr.writeheader(); wr.writerows(d)
from collections import Counter
print("total", len(rows))
for g in GROUPS:
    gr = [r for r in rows if r["group"] == g]
    print(g, "found", len(gr), "pass screen", sum(r["passes_screen"]=="yes" for r in gr), "pdfs", sum(bool(r["pdf_file"]) for r in gr))
