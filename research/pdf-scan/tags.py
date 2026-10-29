"""Count Figure and Formula tags in each PDF's structure tree and how many carry alt text."""
import csv, glob, pikepdf

def walk(node, out, seen):
    og = getattr(node, "objgen", (0, 0))
    if og != (0, 0):
        if og in seen: return
        seen.add(og)
    if isinstance(node, pikepdf.Dictionary):
        s = str(node.get("/S", ""))
        if s in ("/Figure", "/Formula"):
            out[s][0] += 1
            if "/Alt" in node and str(node.Alt).strip():
                out[s][1] += 1
        k = node.get("/K")
        if k is not None: walk(k, out, seen)
    elif isinstance(node, pikepdf.Array):
        for x in node: walk(x, out, seen)

rows = []
for f in sorted(glob.glob("pdfs/*.pdf")):
    out = {"/Figure": [0, 0], "/Formula": [0, 0]}
    with pikepdf.open(f) as pdf:
        root = pdf.Root.get("/StructTreeRoot")
        if root is not None: walk(root, out, set())
    rows.append(dict(file=f[5:], figure_tags=out["/Figure"][0], figures_with_alt=out["/Figure"][1],
                     formula_tags=out["/Formula"][0], formulas_with_alt=out["/Formula"][1]))
with open("tag-results.csv", "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
F = sum(r["figure_tags"] for r in rows); A = sum(r["figures_with_alt"] for r in rows)
print(f"figure tags {F}, with alt text {A}")
print(f"formula tags {sum(r['formula_tags'] for r in rows)}, with alt text {sum(r['formulas_with_alt'] for r in rows)}")
print(f"files with any figure alt text {sum(1 for r in rows if r['figures_with_alt'])} of {len(rows)}")
