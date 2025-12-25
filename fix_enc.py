#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

file_path = 'inspecao-gas-predial.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = {
    'à ': 'á ',  # à + espaço
    'Àrea': 'Área',
    'à': 'á',  # resto
    'frequância': 'frequência',
    'périodica': 'periódica',
    'vàlvulas': 'válvulas',
    'tàcnico': 'técnico',
    'tàcnica': 'técnica',
    'Exigância': 'Exigência',
    'Homicàdio': 'Homicídio',
    'Incàndio': 'Incêndio',
    'Negligância': 'Negligência',
    'estàticos': 'estáticos',
    'apàlice': 'apólice',
    'pràmio': 'prêmio',
    'gestào': 'gestão',
    'condomànio': 'condomínio',
    'sàndico': 'síndico',
    'condàminos': 'condomínios',
    'responsàvel': 'responsável',
    'responsàveis': 'responsáveis',
    'ausância': 'ausência',
    'especàfica': 'específica',
    'Tàcnica': 'Técnica',
    'Pràticas': 'Práticas',
    'Patrim à nios': 'Patrimônio',
    'Patrim àonio': 'Patrimônio',
    'diligância': 'diligência',
    'gàs': 'gás',
    'combustàvel': 'combustível',
}

for old, new in replacements.items():
    content = content.replace(old, new)

# Limpar mais acentos incorretos
content = content.replace('à', 'á')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print('✓ Arquivo corrigido com sucesso!')

