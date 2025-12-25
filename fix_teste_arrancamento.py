#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script para corrigir encoding e remover duplicações em teste-arrancamento-olhais.html
"""

import re

file_path = 'teste-arrancamento-olhais.html'

# Ler arquivo
with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Remover linhas duplicadas consecutivas
cleaned_lines = []
prev_line = None
for line in lines:
    if line != prev_line:
        cleaned_lines.append(line)
    prev_line = line

# Juntar linhas
content = ''.join(cleaned_lines)

# Mapa completo de correções
replacements = {
    # Erros "tàcnico/tàcnica"
    'tàcnico': 'técnico',
    'tàcnica': 'técnica',
    'Tàcnico': 'Técnico',
    'Tàcnica': 'Técnica',
    
    # Erros "sàndico"
    'sàndico': 'síndico',
    'sàndicos': 'síndicos',
    'Sàndico': 'Síndico',
    'Sàndicos': 'Síndicos',
    'SàNDICO': 'SÍNDICO',
    
    # Erros "edifàcio"
    'edifàcio': 'edifício',
    'edifàcios': 'edifícios',
    'Edifàcio': 'Edifício',
    'Edifàcios': 'Edifícios',
    
    # Erros "dinamàmetro"
    'dinamàmetro': 'dinamômetro',
    'Dinamàmetro': 'Dinamômetro',
    
    # Outros erros comuns
    'vàlid': 'válid',
    'vàlid': 'válid',
    'fotogràfico': 'fotográfico',
    'Fotogràfico': 'Fotográfico',
    'oràamento': 'orçamento',
    'Oràamento': 'Orçamento',
    'preào': 'preço',
    'Preào': 'Preço',
    'metàlico': 'metálico',
    'Metàlico': 'Metálico',
    
    # Verbos e outras palavras
    'està': 'está',
    'Està': 'Está',
    'atà': 'até',
    'Atà': 'Até',
    'àteis': 'úteis',
    'apàs': 'após',
    'Apàs': 'Após',
    'resistància': 'resistência',
    'Resistància': 'Resistência',
    'màdio': 'médio',
    'màdia': 'média',
    'milhào': 'milhão',
    'milhàes': 'milhões',
    'irreversàvel': 'irreversível',
    'responsàvel': 'responsável',
    'responsàveis': 'responsáveis',
    'famàlias': 'famílias',
    'Famàlias': 'Famílias',
    'condomànio': 'condomínio',
    'condomànios': 'condomínios',
    'Condomànio': 'Condomínio',
    'Condomànios': 'Condomínios',
    'condàminos': 'condôminos',
    'Condàminos': 'Condôminos',
    'milionària': 'milionária',
    'milionàrias': 'milionárias',
    'Càdigo': 'Código',
    'càdigo': 'código',
    'ilàcito': 'ilícito',
    'Homicàdio': 'Homicídio',
    'homicàdio': 'homicídio',
    'RESPONSABILIZAçãO': 'RESPONSABILIZAÇÃO',
    'Obrigatàrio': 'Obrigatório',
    'obrigatàrio': 'obrigatório',
    'obrigatària': 'obrigatária',
    'reincidància': 'reincidência',
    'questàes': 'questões',
    'dàvidas': 'dúvidas',
    'Dàvidas': 'Dúvidas',
    'Alàm': 'Além',
    'alàm': 'além',
    'apàlice': 'apólice',
    'màximo': 'máximo',
    'mànimo': 'mínimo',
    'Màximo': 'Máximo',
    'Mànimo': 'Mínimo',
    'periàdicos': 'periódicos',
    'Periàdicos': 'Periódicos',
    'critàrios': 'critérios',
    'Critàrios': 'Critérios',
    'Nàmero': 'Número',
    'nàmero': 'número',
    'sàrie': 'série',
    'Sàrie': 'Série',
    'responsàvel': 'responsável',
    'Responsàvel': 'Responsável',
    'màsico': 'mínimo',
    'intermedi àrias': 'intermediárias',
    'espaàamento': 'espaçamento',
    'rodapà': 'rodapé',
    'màltipla': 'múltipla',
    'usuàrios': 'usuários',
    'Usuàrios': 'Usuários',
    'càlculo': 'cálculo',
    'Càlculo': 'Cálculo',
    'aplicàveis': 'aplicáveis',
    'Seguranàa': 'Segurança',
    'seguranàa': 'segurança',
    'dinàmicas': 'dinâmicas',
    'Dinàmicas': 'Dinâmicas',
    'admissàveis': 'admissíveis',
    'Admissàveis': 'Admissíveis',
    'màsicos': 'mínimos',
}

# Aplicar substituições
for old, new in replacements.items():
    content = content.replace(old, new)

# Escrever arquivo corrigido
with open(file_path, 'w', encoding='utf-8', newline='') as f:
    f.write(content)

print(f"✅ Arquivo {file_path} corrigido com sucesso!")
print(f"   - Linhas processadas: {len(lines)}")
print(f"   - Linhas após limpeza: {len(cleaned_lines)}")
print(f"   - Substituições aplicadas: {len(replacements)}")
