#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Atualizar JSON elevadores.json com artigo_relacionado para elev-063 a elev-072.
"""

import json

# Mapping de IDs para slugs
artigo_mapping = {
    "elev-063": "visor-vidro-porta-pavimento",
    "elev-064": "piso-cabina-liso",
    "elev-065": "para-choques-buffers-ressecados",
    "elev-066": "corrimao-cabina-padrao",
    "elev-067": "assento-basculante-acessibilidade",
    "elev-068": "iluminacao-emergencia-cabina",
    "elev-069": "sensor-porta-deteccao-pessoa",
    "elev-070": "vibracao-lateral-excessiva",
    "elev-071": "fiacao-conectores-expostos-quadro",
    "elev-072": "aterramento-inadequado-elevador"
}

# Títulos dos artigos
titles_mapping = {
    "elev-063": "Visor de Vidro Inadequado em Porta de Pavimento",
    "elev-064": "Piso da Cabina Muito Liso",
    "elev-065": "Para-choques (Buffers) Ressecados ou Deteriorados",
    "elev-066": "Corrimão da Cabina Fora de Padrão",
    "elev-067": "Assento Basculante de Acessibilidade Fora do Padrão",
    "elev-068": "Falta de Iluminação de Emergência na Cabina",
    "elev-069": "Sensor da Porta Não Detecta Pessoa no Fechamento",
    "elev-070": "Vibração Lateral Excessiva do Elevador",
    "elev-071": "Fiação e Conectores Expostos no Quadro de Comando",
    "elev-072": "Aterramento Inadequado do Elevador"
}

# Carregar JSON
json_path = "conhecimento-tecnico/dados/elevadores.json"
with open(json_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Update each FAQ entry
updated = 0
for faq in data['faqs']:
    faq_id = faq.get('id')
    if faq_id in artigo_mapping:
        slug = artigo_mapping[faq_id]
        title = titles_mapping[faq_id]
        
        # Add artigo_relacionado if not exists
        if 'artigo_relacionado' not in faq:
            faq['artigo_relacionado'] = {}
        
        faq['artigo_relacionado']['titulo'] = title
        faq['artigo_relacionado']['url'] = f"/artigos/elevadores/artigo-elevadores-{slug}.html"
        faq['artigo_relacionado']['categoria'] = "Elevadores"
        
        updated += 1
        print(f"✓ Updated {faq_id}: {title}")

# Save updated JSON
with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print(f"\n✓ Total updated: {updated}")
print("✓ JSON file saved successfully!")
