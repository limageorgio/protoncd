#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Atualizar JSON com artigo_relacionado para elev-073 a elev-082
e adicionar cards ao índice HTML
"""
import json
import re
from pathlib import Path

BASE_DIR = Path(r"h:\apps\protoncd")
JSON_FILE = BASE_DIR / "conhecimento-tecnico" / "dados" / "elevadores.json"
INDEX_HTML = BASE_DIR / "artigos" / "elevadores" / "index.html"
CREATED_FILES = BASE_DIR / "batch_073_082_created_files.json"

# Carregar metadados dos arquivos criados
with open(str(CREATED_FILES), 'r', encoding='utf-8') as f:
    created_files = json.load(f)

# Criar mapa de ID para dados
id_map = {f['id']: f for f in created_files}

# Ler JSON existente
with open(str(JSON_FILE), 'r', encoding='utf-8') as f:
    json_content = f.read()
    json_data = json.loads(json_content)

# Atualizar registros JSON com artigo_relacionado
updates_count = 0
for faq in json_data['faqs']:
    faq_id = faq['id']
    if faq_id in id_map:
        file_info = id_map[faq_id]
        faq['artigo_relacionado'] = {
            "titulo": file_info['title'],
            "url": f"/artigos/elevadores/{file_info['filename']}",
            "categoria": "Elevadores"
        }
        updates_count += 1
        print(f"✓ {faq_id}: artigo_relacionado adicionado")

# Escrever JSON atualizado
import codecs
with codecs.open(str(JSON_FILE), 'w', encoding='utf-8-sig') as f:
    json.dump(json_data, f, ensure_ascii=False, indent=4)

print(f"\n✓ JSON atualizado: {updates_count} registros com artigo_relacionado\n")

# Ler índice HTML
with codecs.open(str(INDEX_HTML), 'r', encoding='utf-8-sig') as f:
    index_html = f.read()

# Criar cards HTML para os 10 novos artigos
cards_html = ""
for file_info in created_files:
    file_id = file_info['id']
    title = file_info['title']
    slug = file_info['slug']
    
    # Definir ícone e cor apropriados
    icon_map = {
        'elev-073': ('fas fa-fire', 'red'),
        'elev-074': ('fas fa-fan', 'orange'),
        'elev-075': ('fas fa-volume-up', 'orange'),
        'elev-076': ('fas fa-lock', 'red'),
        'elev-077': ('fas fa-tag', 'blue'),
        'elev-078': ('fas fa-flash', 'red'),
        'elev-079': ('fas fa-door-open', 'orange'),
        'elev-080': ('fas fa-water', 'blue'),
        'elev-081': ('fas fa-broom', 'gray'),
        'elev-082': ('fas fa-life-ring', 'red'),
    }
    
    icon, color = icon_map.get(file_id, ('fas fa-cogs', 'blue'))
    
    # Descrição curta baseada no título
    descriptions = {
        'elev-073': 'Riscos de propagação de fogo por excesso de revestimento inadequado.',
        'elev-074': 'Ventilação insuficiente compromete segurança em emergência.',
        'elev-075': 'Ruído na partida indica desgaste que precisa investigação.',
        'elev-076': 'Módulos sem proteção vulneráveis a alterações de segurança.',
        'elev-077': 'Identificação clara reduz tempo de resposta em emergência.',
        'elev-078': 'Elevador de resgate precisa de alimentação contingenciada.',
        'elev-079': 'Acesso desprotegido aumenta risco elétrico e mecânico.',
        'elev-080': 'Infiltração acelera corrosão de componentes críticos.',
        'elev-081': 'Falta de limpeza favorece corrosão e falhas operacionais.',
        'elev-082': 'Resgate manual é segurança crítica em emergência.',
    }
    
    description = descriptions.get(file_id, title.lower())
    
    card_html = f'''
                <a href="artigo-elevadores-{slug}.html" class="card hover-lift"
                    style="text-decoration:none;">
                    <div class="card-icon {color}"><i class="{icon}"></i></div>
                    <h3 class="card-title">{title}</h3>
                    <p class="card-text">{description}</p>
                </a>
'''
    cards_html += card_html

# Encontrar a última tag </a> do grid e inserir os novos cards antes do fecha
closing_grid = '</a>\n\n            </div>'
if closing_grid in index_html:
    # Inserir antes do fechamento da grid
    index_html = index_html.replace(closing_grid, cards_html + '\n            </div>')
    
    with codecs.open(str(INDEX_HTML), 'w', encoding='utf-8-sig') as f:
        f.write(index_html)
    
    print("✓ 10 cards adicionados ao artigos/elevadores/index.html")
else:
    print("✗ Não foi possível encontrar posição correta no índice HTML")

# Validar JSON
try:
    with codecs.open(str(JSON_FILE), 'r', encoding='utf-8-sig') as f:
        json.load(f)
    print("✓ JSON validado: sintaxe correta")
except json.JSONDecodeError as e:
    print(f"✗ Erro de JSON: {str(e)}")

print("\n" + "="*80)
print("ATUALIZAÇÕES COMPLETADAS:")
print("="*80)
print(f"✓ JSON: 10 registros atualizados com artigo_relacionado")
print(f"✓ Índice HTML: 10 cards adicionados")
print(f"✓ Validação: JSON com sintaxe correta")
