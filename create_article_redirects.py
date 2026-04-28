#!/usr/bin/env python3
"""
Create redirect pages for all articles from URL without .html to URL with .html
For Jekyll redirect_from plugin on GitHub Pages
"""

import json
from pathlib import Path

# Read all article metadata
articles = []

# Buscar todos os arquivos HTML de artigos
import glob
for html_file in sorted(glob.glob('artigos/**/*.html', recursive=True)):
    if html_file.endswith('index.html'):
        continue  # Skip index files
    
    filename = Path(html_file).name
    if not filename.startswith('artigo-'):
        continue
    
    # Extract slug from filename (remove .html)
    slug = filename.replace('.html', '')
    
    # Get category from path
    parts = Path(html_file).parts
    if len(parts) >= 2:
        category = parts[1]  # artigos
        subcategory = parts[2] if len(parts) > 2 else None  # elevadores, etc
        
        articles.append({
            'filename': html_file,
            'slug': slug,
            'category': category,
            'subcategory': subcategory,
        })

print(f"Encontrados {len(articles)} artigos")

# Create redirect pages
count = 0
for article in articles:
    # Create directory: artigos/{subcategory}/{slug}/
    redirect_dir = Path('artigos') / (article['subcategory'] or '') / article['slug']
    redirect_dir.mkdir(parents=True, exist_ok=True)
    
    # Create index.html with Jekyll redirect
    redirect_file = redirect_dir / 'index.html'
    redirect_url = f"/artigos/{article['subcategory']}/{article['slug']}.html"
    
    content = f"""---
redirect_to: {redirect_url}
---
"""
    
    redirect_file.write_text(content)
    count += 1
    print(f"✓ {redirect_dir}")

print(f"\n✅ Criadas {count} páginas de redirect")
