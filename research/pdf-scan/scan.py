"""Scan lecture PDFs for what a screen reader can use.

For each file: pages, tagged or not, whether a structure tree exists,
images per page, and pages that are mostly picture (images present
and under 25 words of real text). Untagged files cannot carry alt text,
so every image in them is announced without a description.
"""
import csv, glob, re, subprocess, collections

def run(*a):
    return subprocess.run(a, capture_output=True, text=True).stdout

rows = []
for f in sorted(glob.glob("pdfs/*.pdf")):
    info = run("pdfinfo", f)
    pages = int(re.search(r"Pages:\s+(\d+)", info).group(1))
    tagged = "yes" in re.search(r"Tagged:\s+(\w+)", info).group(1)
    struct = bool(run("pdfinfo", "-struct", f).strip())
    imgs = collections.Counter()
    for line in run("pdfimages", "-list", f).splitlines()[2:]:
        p = line.split()
        if len(p) > 2 and p[2] == "image":
            imgs[int(p[0])] += 1
    picture_pages = 0
    pages_with_images = 0
    for pg in range(1, pages + 1):
        if imgs[pg] == 0:
            continue
        pages_with_images += 1
        words = len(run("pdftotext", "-f", str(pg), "-l", str(pg), f, "-").split())
        if words < 25:
            picture_pages += 1
    rows.append(dict(file=f[5:], pages=pages, tagged=tagged, structure_tree=struct,
                     images=sum(imgs.values()), pages_with_images=pages_with_images,
                     mostly_picture_pages=picture_pages))

with open("scan-results.csv", "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=rows[0].keys())
    w.writeheader(); w.writerows(rows)

n = len(rows); P = sum(r["pages"] for r in rows)
print(f"files {n}  pages {P}")
print(f"tagged files {sum(r['tagged'] for r in rows)} of {n}")
print(f"files with structure tree {sum(r['structure_tree'] for r in rows)} of {n}")
print(f"images total {sum(r['images'] for r in rows)}")
print(f"pages with images {sum(r['pages_with_images'] for r in rows)} of {P}")
print(f"mostly picture pages {sum(r['mostly_picture_pages'] for r in rows)} of {P}")
