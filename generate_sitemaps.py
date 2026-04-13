from datetime import date
from pathlib import Path

BASE_URL = "https://www.protoncd.com.br/"
TODAY = date.today().isoformat()

REGIONAL_PREFIXES = {
    "goiania",
    "brasilia",
    "sao-paulo",
    "ibitinga",
    "anapolis",
    "belo-horizonte",
    "curitiba",
    "porto-alegre",
    "rio-de-janeiro",
    "rio-verde",
}

EXCLUDED_DIRS = {"old", "v2-staging", ".git", ".vscode"}
EXCLUDED_FILES = {"player/admin.html"}

# Keep segmentation explicit to avoid accidental omissions.
SITEMAPS = {
    "sitemap-servicos.xml": [],
    "sitemap-regional.xml": [],
    "sitemap-conhecimento.xml": [],
    "sitemap-internacional.xml": [],
}


def to_rel(path: Path) -> str:
    return path.as_posix()


def is_excluded(rel_path: str) -> bool:
    parts = set(rel_path.split("/"))
    if parts.intersection(EXCLUDED_DIRS):
        return True
    return rel_path in EXCLUDED_FILES


def to_loc(rel_path: str) -> str:
    if rel_path == "index.html":
        return BASE_URL
    if rel_path.endswith("/index.html"):
        return BASE_URL + rel_path[:-10]
    return BASE_URL + rel_path


def classify(rel_path: str) -> str:
    top = rel_path.split("/")[0]
    if rel_path.startswith("conhecimento-tecnico/"):
        return "sitemap-conhecimento.xml"
    if rel_path.startswith("en/"):
        return "sitemap-internacional.xml"
    if rel_path.startswith("player/"):
        return ""
    if top in REGIONAL_PREFIXES:
        return "sitemap-regional.xml"
    return "sitemap-servicos.xml"


def priority_for(rel_path: str, sitemap_name: str) -> str:
    if rel_path == "index.html":
        return "1.0"
    if sitemap_name == "sitemap-servicos.xml":
        return "0.9"
    return "0.8"


files = sorted(Path(".").rglob("*.html"))

for file_path in files:
    rel = to_rel(file_path)
    if is_excluded(rel):
        continue
    sitemap_name = classify(rel)
    if not sitemap_name:
        continue
    SITEMAPS[sitemap_name].append(rel)


def write_sitemap(filename: str, urls: list[str]) -> None:
    with open(filename, "w", encoding="utf-8") as file:
        file.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        file.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        for rel in sorted(set(urls)):
            loc = to_loc(rel)
            priority = priority_for(rel, filename)
            file.write("  <url>\n")
            file.write(f"    <loc>{loc}</loc>\n")
            file.write(f"    <lastmod>{TODAY}</lastmod>\n")
            file.write("    <changefreq>monthly</changefreq>\n")
            file.write(f"    <priority>{priority}</priority>\n")
            file.write("  </url>\n")
        file.write("</urlset>\n")


for sm_file, urls in SITEMAPS.items():
    write_sitemap(sm_file, urls)

with open("sitemap.xml", "w", encoding="utf-8") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    f.write('<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
    for sm_file in sorted(SITEMAPS.keys()):
        f.write("  <sitemap>\n")
        f.write(f"    <loc>{BASE_URL}{sm_file}</loc>\n")
        f.write(f"    <lastmod>{TODAY}</lastmod>\n")
        f.write("  </sitemap>\n")
    f.write("</sitemapindex>\n")

print("Sitemaps segmented successfully.")
for name, urls in SITEMAPS.items():
    print(f"{name}: {len(set(urls))} URLs")
