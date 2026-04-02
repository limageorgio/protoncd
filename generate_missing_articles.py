#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import os
import re
import unicodedata
from pathlib import Path

# Paths
json_path = r"h:\apps\protoncd\conhecimento-tecnico\dados\playgrounds.json"
playgrounds_dir = r"h:\apps\protoncd\artigos\playgrounds"

# Load JSON
with open(json_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

faqs = data['faqs']

def slugify(text):
    """Convert text to slug format"""
    # Normalize unicode
    text = unicodedata.normalize('NFKD', text)
    text = text.encode('ASCII', 'ignore').decode('ASCII')
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'\s+', '-', text)
    text = re.sub(r'-+', '-', text)
    text = text.strip('-')
    return text[:50]

def extract_slug_from_question(pergunta):
    """Extract slug from quoted text in question"""
    match = re.search(r"'([^']+|\u0027[^\u0027]+\u0027)", pergunta)
    if match:
        quoted = match.group(1)
        return slugify(quoted)
    else:
        # Fallback: use first part of question
        return slugify(pergunta.split('?')[0])

# Get existing files
existing_slugs = set()
for file in os.listdir(playgrounds_dir):
    if file.startswith('artigo-playground-') and file.endswith('.html'):
        slug = file.replace('artigo-playground-', '').replace('.html', '')
        existing_slugs.add(slug)

print(f"Total FAQs: {len(faqs)}")
print(f"Existing articles: {len(existing_slugs)}")

# Find missing
missing_faqs = []
for faq in faqs:
    slug = extract_slug_from_question(faq['pergunta'])
    if slug not in existing_slugs:
        faq['slug'] = slug
        missing_faqs.append(faq)

print(f"Missing articles: {len(missing_faqs)}")
print("\nMissing IDs and slugs:")
for faq in missing_faqs:
    print(f"  {faq['id']}: {faq['slug']}")

# Save to file for reference
with open(r"h:\apps\protoncd\missing_faqs.txt", 'w', encoding='utf-8') as f:
    for faq in missing_faqs:
        f.write(f"{faq['id']}: {faq['slug']}\n")

print(f"\nSalvo em: h:\\apps\\protoncd\\missing_faqs.txt")
