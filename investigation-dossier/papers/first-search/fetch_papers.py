"""Fetch open access papers from OpenAlex for given search strings.

Edit QUERIES with your own search strings. Writes papers.csv, search_log.csv
and downloads legally free PDFs into pdfs/. Does not rank or select papers
beyond the database's own relevance order.
"""
import csv, json, os, re, time, urllib.parse, urllib.request
from datetime import date

QUERIES = [
    '"software engineer" "software manager"',
    '"engineering manager" software',
    '"software engineering management"',
    '"technical lead" software team',
]
FROM_YEAR = 2015
PER_QUERY = 15
MAILTO = "student@example.com"

def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": f"coursework-fetch (mailto:{MAILTO})"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()

def abstract(inv):
    if not inv: return ""
    pos = sorted((p, w) for w, ps in inv.items() for p in ps)
    return " ".join(w for _, w in pos)

os.makedirs("pdfs", exist_ok=True)
rows, log, seen = [], [], set()
for q in QUERIES:
    params = {"search": q, "filter": f"from_publication_date:{FROM_YEAR}-01-01,type:article|proceedings-article,is_oa:true",
              "per-page": PER_QUERY, "mailto": MAILTO}
    url = "https://api.openalex.org/works?" + urllib.parse.urlencode(params, safe=":|,")
    data = json.loads(get(url))
    log.append({"date": date.today().isoformat(), "database": "OpenAlex", "query": q,
                "filters": f"from {FROM_YEAR}, articles and proceedings, open access", "total_hits": data["meta"]["count"]})
    for w in data["results"]:
        if w["id"] in seen: continue
        seen.add(w["id"])
        src = (w.get("primary_location") or {}).get("source") or {}
        pdf = (w.get("best_oa_location") or {}).get("pdf_url") or ""
        rows.append({"title": w.get("title"), "year": w.get("publication_year"),
                     "authors": "; ".join(a["author"]["display_name"] for a in w.get("authorships", [])),
                     "venue": src.get("display_name", ""), "doi": w.get("doi") or "",
                     "cited_by": w.get("cited_by_count"), "query": q, "pdf_url": pdf,
                     "abstract": abstract(w.get("abstract_inverted_index")), "pdf_file": ""})
    time.sleep(1)

for i, r in enumerate(rows, 1):
    if not r["pdf_url"]: continue
    name = f"{i:02d}_" + re.sub(r"[^A-Za-z0-9]+", "_", r["title"] or "paper")[:60] + ".pdf"
    try:
        b = get(r["pdf_url"])
        if b[:4] == b"%PDF":
            open(os.path.join("pdfs", name), "wb").write(b); r["pdf_file"] = name
    except Exception:
        pass

for f, data in (("papers.csv", rows), ("search_log.csv", log)):
    with open(f, "w", newline="") as fh:
        wr = csv.DictWriter(fh, fieldnames=list(data[0].keys())); wr.writeheader(); wr.writerows(data)
print(len(rows), "papers,", sum(1 for r in rows if r["pdf_file"]), "PDFs downloaded")
