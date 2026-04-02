#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate missing playground articles based on FAQs and existing files
"""
import json
import os
import re
import unicodedata
from pathlib import Path

# Configuration
JSON_PATH = r"h:\apps\protoncd\conhecimento-tecnico\dados\playgrounds.json"
PLAYGROUNDS_DIR = r"h:\apps\protoncd\artigos\playgrounds"
OUTPUT_FILE = r"h:\apps\protoncd\missing_articles_report.txt"

def slugify(text):
    """Convert text to slug format"""
    if not text:
        return ""
    
    # Normalize unicode
    text = unicodedata.normalize('NFKD', str(text))
    text = text.encode('ASCII', 'ignore').decode('ASCII')
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'\s+', '-', text)
    text = re.sub(r'-+', '-', text)
    text = text.strip('-')
    if len(text) > 50:
        text = text[:50]
    return text

def extract_slug_from_question(pergunta):
    """Extract slug from quoted text in question"""
    if not pergunta:
        return ""
    
    # Try to find quoted text
    match = re.search(r"'([^']+)'", pergunta)
    if match:
        quoted = match.group(1)
        return slugify(quoted)
    
    # Fallback: use first part of question
    return slugify(pergunta.split('?')[0])

try:
    # Load JSON
    with open(JSON_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    faqs = data.get('faqs', [])
    
    # Get existing files
    existing_slugs = set()
    if os.path.exists(PLAYGROUNDS_DIR):
        for file in os.listdir(PLAYGROUNDS_DIR):
            if file.startswith('artigo-playground-') and file.endswith('.html'):
                slug = file.replace('artigo-playground-', '').replace('.html', '')
                existing_slugs.add(slug)
    
    # Find missing
    missing_faqs = []
    for faq in faqs:
        slug = extract_slug_from_question(faq.get('pergunta', ''))
        faq_id = faq.get('id', 'unknown')
        
        if slug and slug not in existing_slugs:
            missing_faqs.append({
                'id': faq_id,
                'slug': slug,
                'pergunta': faq.get('pergunta', ''),
                'resposta': faq.get('resposta', ''),
                'normas': faq.get('normas', []),
                'gravidade': faq.get('gravidade', ''),
                'responsabilidade': faq.get('responsabilidade', '')
            })
    
    # Write report
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(f"Missing Playground Articles Report\n")
        f.write(f"===================================\n\n")
        f.write(f"Total FAQs: {len(faqs)}\n")
        f.write(f"Existing articles: {len(existing_slugs)}\n")
        f.write(f"Missing articles: {len(missing_faqs)}\n\n")
        f.write(f"Missing IDs and Slugs:\n")
        f.write(f"-" * 60 + "\n")
        
        for faq in missing_faqs:
            f.write(f"{faq['id']}: {faq['slug']}\n")
        
        f.write(f"\n\nDetailed Information:\n")
        f.write(f"-" * 60 + "\n\n")
        
        for i, faq in enumerate(missing_faqs, 1):
            f.write(f"{i}. {faq['id']}\n")
            f.write(f"   Slug: {faq['slug']}\n")
            f.write(f"   Pergunta: {faq['pergunta']}\n")
            f.write(f"   Gravidade: {faq['gravidade']}\n")
            f.write(f"   Normas: {', '.join(faq['normas'])}\n\n")
    
    print(f"Report saved to: {OUTPUT_FILE}")
    print(f"I found {len(missing_faqs)} missing articles out of {len(faqs)} FAQs")
    
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
