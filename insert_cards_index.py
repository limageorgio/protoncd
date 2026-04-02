#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Inserir 10 cards no índice HTML de elevadores
"""
import codecs
from pathlib import Path

BASE_DIR = Path(r"h:\apps\protoncd")
INDEX_HTML = BASE_DIR / "artigos" / "elevadores" / "index.html"

# Dados dos novos cards
cards_data = [
    {
        "slug": "combustivel-cabina-interior",
        "title": "Cabina com Excesso de Material Combustível",
        "icon": "fas fa-fire",
        "color": "red",
        "description": "Riscos de propagação de fogo por excesso de revestimento inadequado."
    },
    {
        "slug": "ventilacao-poco-insuficiente",
        "title": "Ventilação Insuficiente no Topo do Poço",
        "icon": "fas fa-fan",
        "color": "orange",
        "description": "Ventilação inadequada compromete segurança operacional em emergência."
    },
    {
        "slug": "ruido-recorrente-partida",
        "title": "Elevador com Ruído Recorrente na Partida",
        "icon": "fas fa-volume-up",
        "color": "orange",
        "description": "Ruído na partida indica desgaste que precisa investigação."
    },
    {
        "slug": "protecao-modulos-eletronicos-seguranca",
        "title": "Ausência de Proteção contra Violação",
        "icon": "fas fa-lock",
        "color": "red",
        "description": "Módulos sem proteção vulneráveis a alterações de segurança."
    },
    {
        "slug": "chave-geral-identificacao",
        "title": "Falta de Identificação da Chave Geral",
        "icon": "fas fa-tag",
        "color": "blue",
        "description": "Identificação clara reduz tempo de resposta em emergência."
    },
    {
        "slug": "emergencia-alimentacao-dedicada",
        "title": "Elevador de Emergência sem Alimentação Dedicada",
        "icon": "fas fa-flash",
        "color": "red",
        "description": "Elevador de resgate precisa de alimentação contingenciada."
    },
    {
        "slug": "porta-casa-maquinas-trancada",
        "title": "Porta da Casa de Máquinas Desprotegida",
        "icon": "fas fa-door-open",
        "color": "orange",
        "description": "Acesso desprotegido aumenta risco elétrico e mecânico."
    },
    {
        "slug": "infiltracao-casa-maquinas",
        "title": "Indícios de Infiltração na Casa de Máquinas",
        "icon": "fas fa-water",
        "color": "blue",
        "description": "Infiltração acelera corrosão de componentes críticos."
    },
    {
        "slug": "limpeza-poco-periodica",
        "title": "Falta de Limpeza Periódica no Poço",
        "icon": "fas fa-broom",
        "color": "gray",
        "description": "Falta de limpeza favorece corrosão e falhas operacionais."
    },
    {
        "slug": "dispositivo-resgate-manual",
        "title": "Falta de Dispositivo de Resgate Manual",
        "icon": "fas fa-life-ring",
        "color": "red",
        "description": "Resgate manual é segurança crítica em emergência."
    }
]

# Gerar HTML dos cards
cards_html = ""
for card in cards_data:
    cards_html += f'''
                <a href="artigo-elevadores-{card['slug']}.html" class="card hover-lift" style="text-decoration:none;">
                    <div class="card-icon {card['color']}"><i class="{card['icon']}"></i></div>
                    <h3 class="card-title">{card['title']}</h3>
                    <p class="card-text">{card['description']}</p>
                </a>
'''

# Ler arquivo
with codecs.open(str(INDEX_HTML), 'r', encoding='utf-8-sig') as f:
    content = f.read()

# Encontrar a posição de inserção (antes do fechamento da grid)
# Procurar por: "            </div>" que vem após aterramento-inadequado-elevador
marker = '''                </a>

            </div>
        </div>
    </section>'''

# Substituir com os novos cards adicionados antes do fechamento
replacement = f'''                </a>
{cards_html}
            </div>
        </div>
    </section>'''

if marker in content:
    content = content.replace(marker, replacement)
    
    # Escrever arquivo atualizado
    with codecs.open(str(INDEX_HTML), 'w', encoding='utf-8-sig') as f:
        f.write(content)
    
    print("✓ 10 cards inseridos com sucesso no índice HTML!")
    print(f"✓ Archivo atualizado: artigos/elevadores/index.html")
    
    # Validar que está bem formado
    if content.count('<div class="card-icon') >= 10:
        print("✓ Validação: 10 cards confirmados no HTML")
else:
    # Tentar alternativa
    print("Tentando alternativa...")
    # Procurar simplesmente pelo último card
    alt_marker = '                </a>\n\n            </div>\n        </div>\n    </section>'
    if alt_marker in content:
        alt_replacement = f'''                </a>
{cards_html}
            </div>
        </div>
    </section>'''
        content = content.replace(alt_marker, alt_replacement)
        with codecs.open(str(INDEX_HTML), 'w', encoding='utf-8-sig') as f:
            f.write(content)
        print("✓ 10 cards inseridos (modo alternativo)!")
    else:
        print("✗ Não foi possível encontrar ponto de inserção")

print("\n" + "="*80)
print("RESUMO DA INSERÇÃO:")
print("="*80)
for idx, card in enumerate(cards_data, 1):
    print(f"{idx}. {card['title']:50} → artigo-elevadores-{card['slug']}.html")
