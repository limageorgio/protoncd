#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Final comprehensive validation of batch elev-063 to elev-072.
"""

import os
import json

os.chdir("h:\\apps\\protoncd")

print("=" * 70)
print("FINAL VALIDATION - BATCH elev-063 to elev-072")
print("=" * 70)

# Check 1: Verify 10 new HTML files exist
print("\n✓ CHECK 1: New HTML article files")
html_articles = [
    "artigos/elevadores/artigo-elevadores-visor-vidro-porta-pavimento.html",
    "artigos/elevadores/artigo-elevadores-piso-cabina-liso.html",
    "artigos/elevadores/artigo-elevadores-para-choques-buffers-ressecados.html",
    "artigos/elevadores/artigo-elevadores-corrimao-cabina-padrao.html",
    "artigos/elevadores/artigo-elevadores-assento-basculante-acessibilidade.html",
    "artigos/elevadores/artigo-elevadores-iluminacao-emergencia-cabina.html",
    "artigos/elevadores/artigo-elevadores-sensor-porta-deteccao-pessoa.html",
    "artigos/elevadores/artigo-elevadores-vibracao-lateral-excessiva.html",
    "artigos/elevadores/artigo-elevadores-fiacao-conectores-expostos-quadro.html",
    "artigos/elevadores/artigo-elevadores-aterramento-inadequado-elevador.html",
]

created_count = 0
for filepath in html_articles:
    if os.path.exists(filepath):
        print(f"  ✓ {os.path.basename(filepath)}")
        created_count += 1
    else:
        print(f"  ✗ {os.path.basename(filepath)} NOT FOUND")

print(f"  → {created_count}/10 files created")

# Check 2: Verify JSON has artigo_relacionado for all 10
print("\n✓ CHECK 2: JSON elevadores.json with artigo_relacionado URLs")
with open("conhecimento-tecnico/dados/elevadores.json", 'r', encoding='utf-8') as f:
    json_data = json.load(f)

updated_count = 0
for faq in json_data['faqs']:
    faq_id = faq.get('id')
    if faq_id and 63 <= int(faq_id.split('-')[1]) <= 72:
        if 'artigo_relacionado' in faq:
            url = faq['artigo_relacionado'].get('url', '')
            print(f"  ✓ {faq_id}: {url}")
            updated_count += 1
        else:
            print(f"  ✗ {faq_id}: Missing artigo_relacionado")

print(f"  → {updated_count}/10 entries updated")

# Check 3: Verify index.html has 10 cards
print("\n✓ CHECK 3: artigos/elevadores/index.html cards")
with open("artigos/elevadores/index.html", 'r', encoding='utf-8') as f:
    index_content = f.read()

card_count = 0
article_names = [
    "visor-vidro-porta-pavimento",
    "piso-cabina-liso",
    "para-choques-buffers-ressecados",
    "corrimao-cabina-padrao",
    "assento-basculante-acessibilidade",
    "iluminacao-emergencia-cabina",
    "sensor-porta-deteccao-pessoa",
    "vibracao-lateral-excessiva",
    "fiacao-conectores-expostos-quadro",
    "aterramento-inadequado-elevador",
]

for article_name in article_names:
    if f"artigo-elevadores-{article_name}.html" in index_content:
        print(f"  ✓ Card for {article_name}")
        card_count += 1
    else:
        print(f"  ✗ Card for {article_name} NOT found")

print(f"  → {card_count}/10 cards added")

# Check 4: Verify conhecimento-tecnico/index.html has artigo_relacionado
print("\n✓ CHECK 4: conhecimento-tecnico/index.html embedded JSON")
with open("conhecimento-tecnico/index.html", 'r', encoding='utf-8') as f:
    tech_index = f.read()

html_json_count = 0
for article_name in article_names:
    if f"/artigos/elevadores/artigo-elevadores-{article_name}.html" in tech_index:
        print(f"  ✓ Reference to {article_name}")
        html_json_count += 1
    else:
        print(f"  ✗ Reference to {article_name} NOT found in HTML")

print(f"  → {html_json_count}/10 embedded JSON references updated")

# Check 5: No syntax errors in key files
print("\n✓ CHECK 5: JSON syntax validation")
try:
    json.load(open("conhecimento-tecnico/dados/elevadores.json", 'r', encoding='utf-8'))
    print("  ✓ elevadores.json: Valid JSON")
except Exception as e:
    print(f"  ✗ elevadores.json: Invalid JSON - {str(e)}")

# Summary
print("\n" + "=" * 70)
print("BATCH COMPLETION SUMMARY")
print("=" * 70)
print(f"HTML Articles Created:      {created_count}/10")
print(f"JSON Entries Updated:       {updated_count}/10")
print(f"Index Cards Added:          {card_count}/10")
print(f"HTML JSON References:       {html_json_count}/10")

if created_count == 10 and updated_count == 10 and card_count == 10 and html_json_count == 10:
    print("\n✓✓✓ ALL TASKS COMPLETED SUCCESSFULLY ✓✓✓")
else:
    print("\n⚠ Some tasks have not been completed fully")
