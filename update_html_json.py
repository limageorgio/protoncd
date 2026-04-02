#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Update the embedded JSON in conhecimento-tecnico/index.html to include artigo_relacionado for elev-063 to elev-072.
"""

import os
import json
import re

os.chdir("h:\\apps\\protoncd")

# Read main JSON
with open("conhecimento-tecnico/dados/elevadores.json", 'r', encoding='utf-8') as f:
    main_data = json.load(f)

# Read HTML file
with open("conhecimento-tecnico/index.html", 'r', encoding='utf-8-sig') as f:
    html_content = f.read()

# Create a map of target FAQs from main JSON
target_faqs = {}
for faq in main_data['faqs']:
    faq_id = faq.get('id')
    if faq_id and 63 <= int(faq_id.split('-')[1]) <= 72:
        target_faqs[faq_id] = faq

print(f"✓ Loaded {len(target_faqs)} target FAQs from main JSON")

# For each target FAQ, find it in the HTML and update it
# HTML uses HTMLentities for special characters, so we need to handle that
# We'll search for the pattern and replace the entire entry

for faq_id in sorted(target_faqs.keys()):
    faq_data = target_faqs[faq_id]
    
    # Find the entry in HTML - look for "id":\s*"faq_id"
    pattern = r'\{\s*"id":\s*"' + re.escape(faq_id) + r'"[^}]*?"gravidade":\s*"[^"]*?"(\s*)(}|\})'
    
    # Find where this entry is
    match = re.search(pattern, html_content, re.DOTALL)
    
    if match:
        # Build replacement with artigo_relacionado if it has it
        old_entry = match.group(0)
        
        # Insert artigo_relacionado before closing brace
        if 'artigo_relacionado' in faq_data:
            artigo = faq_data['artigo_relacionado']
            # Create HTML-safe JSON representation with entities
            artigo_json = json.dumps(artigo, ensure_ascii=True)
            # Now we need to HTML-encode the Unicode, but keep it readable
            # Actually, just use ensure_ascii=False and let Python handle it
            
            # Insert the artigo_relacionado field
            # Find the last closing brace and insert before it
            insert_text = f''',
                                                                    "artigo_relacionado":  {{
                                                                        "titulo":  "{artigo['titulo']}",
                                                                        "url":  "{artigo['url']}",
                                                                        "categoria":  "{artigo['categoria']}"
                                                                    }}'''
            
            new_entry = old_entry.replace(match.group(2), insert_text + match.group(2))
            html_content = html_content.replace(old_entry, new_entry)
            print(f"✓ Updated {faq_id}")
        else:
            print(f"- {faq_id} has no artigo_relacionado in main JSON")
    else:
        print(f"✗ Could not find {faq_id} in HTML")

# Write updated HTML back
with open("conhecimento-tecnico/index.html", 'w', encoding='utf-8') as f:
    f.write(html_content)

print("\n✓ HTML file updated successfully!")
