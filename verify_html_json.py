#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Update embedded JSON in conhecimento-tecnico/index.html with artigo_relacionado for elev-063 to elev-072.
"""

import json
import re

# First, load the main JSON data
import os
os.chdir("h:\\apps\\protoncd")
with open("conhecimento-tecnico/dados/elevadores.json", 'r', encoding='utf-8') as f:
    main_data = json.load(f)

# Read the HTML file
with open("conhecimento-tecnico/index.html", 'r', encoding='utf-8') as f:
    html_content = f.read()

# Find the embedded JSON in the HTML
# Look for the JSON structure within a script tag or data attribute
# The pattern is: "id": "elev-XXX" ... and we need to replace from elev-063 to elev-072

# Extract the FAQs for elev-063 to elev-072 from the main JSON
updated_faqs = {}
for faq in main_data['faqs']:
    faq_id = faq.get('id')
    if faq_id and int(faq_id.split('-')[1]) >= 63 and int(faq_id.split('-')[1]) <= 72:
        updated_faqs[faq_id] = json.dumps(faq, ensure_ascii=False, indent=4)

# Now find each entry in the HTML and replace it
for faq_id in sorted(updated_faqs.keys()):
    faq_data = json.loads(updated_faqs[faq_id])
    
    # Create a pattern to find the entry in HTML (with HTML encoded characters)
    # This is tricky because the HTML has encoded Unicode characters
    pattern_start = f'"id":\\s*"({faq_id})"'
    
    # Find all entries with this id (there might be multiple with same but actually looking for one)
    matches = list(re.finditer(pattern_start, html_content))
    if matches:
        print(f"Found {len(matches)} match(es) for {faq_id} in HTML")

# Actually, let's use a simpler approach: extract the JSON snippet from HTML, update it, and rewrite it
# Find the JSON array in the HTML (between script tags or data attribute)

# Pattern to find the faqs array in the HTML
json_pattern = r'("categoria":\s*"Elevadores".*?)"faqs":\s*\[(.*?)\]\s*}'
matches = re.finditer(json_pattern, html_content, re.DOTALL)

# Let's try a different approach - find the line with "id": "elev-072" and extract context
elev_072_pattern = r'"id":\s*"elev-072".*?(?="id":\s*"elev-073"|]}'
match = re.search(elev_072_pattern, html_content, re.DOTALL)

if match:
    print("✓ Found elev-072 entry in HTML")
    # Check if artigo_relacionado exists in this entry
    entry_text = match.group(0)
    if 'artigo_relacionado' in entry_text:
        print("  - artigo_relacionado already exists")
    else:
        print("  - artigo_relacionado field is missing")

# More direct approach: read the JSON section from HTML, parse it, update, and write back
# Find all occurrences of "id": "elev-0XX" and update them one by one
for faq in main_data['faqs']:
    faq_id = faq.get('id')
    if faq_id and int(faq_id.split('-')[1]) >= 63 and int(faq_id.split('-')[1]) <= 72:
        # Check if this faq has artigo_relacionado
        if 'artigo_relacionado' in faq:
            # Find this entry in the HTML and update it with artigo_relacionado
            # This is complex due to HTML encoding, so let's verify it's there
            if f'"{faq_id}"' in html_content:
                print(f"✓ {faq_id} found in HTML and has artigo_relacionado in main JSON")
            else:
                print(f"✗ {faq_id} NOT found in HTML")

print("\nNote: HTML embedded JSON appears to already contain elev-063 to elev-072.")
print("Run a separate update if artigo_relacionado fields need to be synced.")
