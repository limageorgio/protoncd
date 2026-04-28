#!/usr/bin/env python3
"""
Fix sitemap URLs to include .html extension.
Converts URLs like /artigos/elevadores/artigo-* to /artigos/elevadores/artigo-*.html
Also updates other article URLs without extension.
"""

import glob
import re
from pathlib import Path

def fix_sitemap(filepath):
    """Fix sitemap XML by adding .html to article URLs"""
    content = Path(filepath).read_text(encoding='utf-8-sig')
    original = content
    
    # Pattern: <loc>...URL</loc> where URL is an article without .html
    # Matches: /artigos/... paths that don't end with .html, .xml, .json, etc
    pattern = r'(<loc>https://www\.protoncd\.com\.br/artigos/[^<]+?)(?<!\.html)(?<!\.xml)(?<!\.json)(/\</loc>)'
    
    # Replace: add .html before the closing </loc> if not present
    fixed = re.sub(
        r'(<loc>https://www\.protoncd\.com\.br/artigos/[^<]+?)(?<!\.html)(?<!/)(\</loc>)',
        r'\1.html\2',
        content
    )
    
    if original != fixed:
        Path(filepath).write_text(fixed, encoding='utf-8')
        lines_changed = len(re.findall(r'\.html\</loc>', fixed)) - len(re.findall(r'\.html\</loc>', original))
        print(f"✓ {Path(filepath).name}: {lines_changed:+d} URLs fixed")
        return lines_changed
    else:
        print(f"  {Path(filepath).name}: No changes needed")
        return 0

# Fix all sitemap XMLs
total = 0
for sitemap in sorted(glob.glob('sitemap*.xml')):
    total += fix_sitemap(sitemap)

print(f"\n📊 Total URLs fixed: {total}")
