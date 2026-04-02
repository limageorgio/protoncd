#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Add 10 new cards to artigos/elevadores/index.html for elev-063 to elev-072.
"""

import re

# Define new cards data
new_cards = [
    {
        "slug": "visor-vidro-porta-pavimento",
        "title": "Visor de Vidro Inadequado",
        "excerpt": "Vidro inadequado em porta de pavimento eleva risco de quebra e estilhaçamento.",
        "icon": "fas fa-window-close",
        "icon_class": "red"
    },
    {
        "slug": "piso-cabina-liso",
        "title": "Piso da Cabina Liso",
        "excerpt": "Piso muito liso aumenta risco de escorregamento em embarque e desembarque.",
        "icon": "fas fa-shoe-prints",
        "icon_class": "orange"
    },
    {
        "slug": "para-choques-buffers-ressecados",
        "title": "Para-choques Deteriorados",
        "excerpt": "Buffers ressecados perdem capacidade de amortecimento em final de curso.",
        "icon": "fas fa-compress",
        "icon_class": "red"
    },
    {
        "slug": "corrimao-cabina-padrao",
        "title": "Corrimão da Cabina",
        "excerpt": "Corrimão fora de padrão compromete apoio seguro durante movimentação.",
        "icon": "fas fa-grip-horizontal",
        "icon_class": "orange"
    },
    {
        "slug": "assento-basculante-acessibilidade",
        "title": "Assento Basculante",
        "excerpt": "Assento de acessibilidade inadequado limita uso e cria obstáculos.",
        "icon": "fas fa-chair",
        "icon_class": "blue"
    },
    {
        "slug": "iluminacao-emergencia-cabina",
        "title": "Iluminação de Emergência",
        "excerpt": "Falta de luz de emergência compromete segurança em apagão.",
        "icon": "fas fa-lightbulb",
        "icon_class": "red"
    },
    {
        "slug": "sensor-porta-deteccao-pessoa",
        "title": "Sensor de Detecção",
        "excerpt": "Falha de sensor pode resultar em porta fechando sobre passageiro.",
        "icon": "fas fa-door-closed",
        "icon_class": "red"
    },
    {
        "slug": "vibracao-lateral-excessiva",
        "title": "Vibração Lateral",
        "excerpt": "Vibração indica desalinhamento ou desgaste que acelera deterioração.",
        "icon": "fas fa-wave-square",
        "icon_class": "orange"
    },
    {
        "slug": "fiacao-conectores-expostos-quadro",
        "title": "Fiação Exposta",
        "excerpt": "Fios e conectores soltos representam risco de choque e incêndio.",
        "icon": "fas fa-plug",
        "icon_class": "red"
    },
    {
        "slug": "aterramento-inadequado-elevador",
        "title": "Aterramento Inadequado",
        "excerpt": "Aterramento deficiente expõe usuários a risco de choque elétrico.",
        "icon": "fas fa-bolt",
        "icon_class": "red"
    }
]

# Read the index file
import os
os.chdir("h:\\apps\\protoncd")
with open("artigos/elevadores/index.html", 'r', encoding='utf-8') as f:
    content = f.read()

# Create HTML for new cards
cards_html = ""
for card in new_cards:
    cards_html += f'''
                <a href="artigo-elevadores-{card['slug']}.html" class="card hover-lift" style="text-decoration:none;">
                    <div class="card-icon {card['icon_class']}"><i class="{card['icon']}"></i></div>
                    <h3 class="card-title">{card['title']}</h3>
                    <p class="card-text">{card['excerpt']}</p>
                </a>
'''

# Find the last card and insert new cards before the closing </div> of the grid
# The pattern is: last article card followed by closing div
# We need to find the last </a> tag in the grid and add new cards after it

# Find the position of the last card before the closing grid div
# Look for the pattern: artigo-elevadores-aterramento-equipotencializacao.html
pattern = r'(<a href="artigo-elevadores-aterramento-equipotencializacao\.html".*?</a>)'
match = re.search(pattern, content, re.DOTALL)

if match:
    insert_pos = match.end()
    new_content = content[:insert_pos] + cards_html + content[insert_pos:]
    
    # Write back the file
    with open("artigos/elevadores/index.html", 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print("✓ Successfully added 10 new cards to index.html")
    print("\nNew cards added for:")
    for i, card in enumerate(new_cards, 1):
        print(f"  {i}. {card['title']}")
else:
    print("✗ Could not find insertion point in index.html")
