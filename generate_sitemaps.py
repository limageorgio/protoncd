import glob
import os
import re

base_url = "https://www.protoncd.com.br/"

# Sitemaps structure
sitemaps = {
    'sitemap-servicos.xml': [],
    'sitemap-regional.xml': [],
    'sitemap-conhecimento.xml': [],
}

def is_regional(path):
    regionals = ['goiania', 'brasilia', 'sao-paulo', 'ibitinga', 'anapolis', 'belo-horizonte', 'curitiba', 'porto-alegre', 'rio-de-janeiro', 'rio-verde']
    for r in regionals:
        if path.startswith(r): return True
    return False

# Find files
files = glob.glob('**/*.html', recursive=True)

for f in files:
    # Skip
    if 'old\\' in f or 'v2-staging\\' in f or 'player\\' in f or 'en\\' in f:
        continue
    
    # Process
    f = f.replace('\\', '/')
    if f == 'index.html':
        sitemaps['sitemap-servicos.xml'].append(f)
    elif f.startswith('conhecimento-tecnico'):
        sitemaps['sitemap-conhecimento.xml'].append(f)
    elif is_regional(f):
        sitemaps['sitemap-regional.xml'].append(f)
    else:
        # All other root html files are assumed to be services, policy or global
        sitemaps['sitemap-servicos.xml'].append(f)

# Write xmls
def write_sitemap(filename, urls):
    content = '<?xml version="1.0" encoding="UTF-8"?>\n'
    content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for u in urls:
        priority = "1.0" if u == "index.html" else ("0.9" if "servicos" in filename else "0.8")
        loc = base_url if u == "index.html" else base_url + u
        content += f'  <url>\n    <loc>{loc}</loc>\n    <changefreq>monthly</changefreq>\n    <priority>{priority}</priority>\n  </url>\n'
    content += '</urlset>'
    
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)

for sm_file, urls in sitemaps.items():
    write_sitemap(sm_file, urls)

# Write sitemap index (sitemap.xml)
index_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
index_content += '<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
for sm_file in sitemaps.keys():
    index_content += f'  <sitemap>\n    <loc>{base_url}{sm_file}</loc>\n  </sitemap>\n'
index_content += '</sitemapindex>'

with open('sitemap.xml', 'w', encoding='utf-8') as f:
    f.write(index_content)

print("Sitemaps segmented successfully.")
