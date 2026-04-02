#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Simple check: does conhecimento-tecnico/index.html have artigo_relacionado for elev-063 to elev-072?
"""

import os
import json

os.chdir("h:\\apps\\protoncd")

# Read HTML file
with open("conhecimento-tecnico/index.html", 'r', encoding='utf-8') as f:
    html_content = f.read()

# Check for artigo_relacionado mentions
target_ids = ['elev-063', 'elev-064', 'elev-065', 'elev-066', 'elev-067', 'elev-068', 'elev-069', 'elev-070', 'elev-071', 'elev-072']

for faq_id in target_ids:
    if f'"{faq_id}"' in html_content:
        # Find the context around this ID
        idx = html_content.find(f'"{faq_id}"')
        context = html_content[max(0, idx-100):min(len(html_content), idx+500)]
        has_artigo = 'artigo_relacionado' in context
        print(f"✓ {faq_id}: Found (artigo_relacionado exists: {has_artigo})")
    else:
        print(f"✗ {faq_id}: NOT found in HTML")

# Load main JSON to confirm it has artigo_relacionado
with open("conhecimento-tecnico/dados/elevadores.json", 'r', encoding='utf-8') as f:
    main_data = json.load(f)

print("\nMain JSON data status:")
for faq in main_data['faqs']:
    if faq.get('id') in target_ids:
        has_artigo = 'artigo_relacionado' in faq
        print(f"  {faq.get('id')}: artigo_relacionado = {has_artigo}")
        if has_artigo:
            print(f"    -> {faq['artigo_relacionado'].get('url')}")
