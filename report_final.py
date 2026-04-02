#!/usr/bin/env python3
import json

json_path = r"h:\apps\protoncd\conhecimento-tecnico\dados\playgrounds.json"
with open(json_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

specific_count = 0
fallback_count = 0
total = len(data['faqs'])

for faq in data['faqs']:
    ref = faq['referencias'][0] if faq['referencias'] else ""
    if 'index.html' in ref:
        fallback_count += 1
    else:
        specific_count += 1

print(f"Total: {total}")
print(f"Específicos: {specific_count}")
print(f"Fallbacks: {fallback_count}")
