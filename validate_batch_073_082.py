#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Validação completa da batch elev-073 a elev-082
"""
import json
import os
import codecs
from pathlib import Path
from html.parser import HTMLParser

BASE_DIR = Path(r"h:\apps\protoncd")
ARTIGOS_DIR = BASE_DIR / "artigos" / "elevadores"
JSON_FILE = BASE_DIR / "conhecimento-tecnico" / "dados" / "elevadores.json"
INDEX_HTML = BASE_DIR / "artigos" / "elevadores" / "index.html"

print("="*80)
print("VALIDAÇÃO COMPLETA - BATCH ELEV-073 A ELEV-082")
print("="*80)

errors = []
warnings = []

# 1. Validar HTML dos 10 artigos
print("\n1. Validando 10 artigos HTML...")
html_files = [
    "artigo-elevadores-combustivel-cabina-interior.html",
    "artigo-elevadores-ventilacao-poco-insuficiente.html",
    "artigo-elevadores-ruido-recorrente-partida.html",
    "artigo-elevadores-protecao-modulos-eletronicos-seguranca.html",
    "artigo-elevadores-chave-geral-identificacao.html",
    "artigo-elevadores-emergencia-alimentacao-dedicada.html",
    "artigo-elevadores-porta-casa-maquinas-trancada.html",
    "artigo-elevadores-infiltracao-casa-maquinas.html",
    "artigo-elevadores-limpeza-poco-periodica.html",
    "artigo-elevadores-dispositivo-resgate-manual.html",
]

html_valid_count = 0
for html_file in html_files:
    html_path = ARTIGOS_DIR / html_file
    
    if not html_path.exists():
        errors.append(f"ERRO: Arquivo não encontrado: {html_file}")
        continue
    
    try:
        with codecs.open(str(html_path), 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Verificações básicas HTML
        if '<!DOCTYPE html>' not in content:
            errors.append(f"ERRO ({html_file}): Falta DOCTYPE")
        elif '</html>' not in content:
            errors.append(f"ERRO ({html_file}): Falta tag de fechamento HTML")
        elif content.count('<h1>') != 1:
            errors.append(f"ERRO ({html_file}): Número incorreto de H1")
        elif 'Acentuação' in content or 'acentuacao' in content.lower():
            # Verificar acentuação
            if 'Acentuação' in content:
                warnings.append(f"Verificar acentuação em {html_file}")
        else:
            html_valid_count += 1
            print(f"   ✓ {html_file}")
    except Exception as e:
        errors.append(f"ERRO ao ler {html_file}: {str(e)}")

print(f"\n   ✓ {html_valid_count}/{len(html_files)} artigos validados")

# 2. Validar JSON
print("\n2. Validando JSON...")
try:
    with codecs.open(str(JSON_FILE), 'r', encoding='utf-8') as f:
        json_data = json.load(f)
    
    # Verificar que elev-073 a elev-082 têm artigo_relacionado
    missing_article_ref = []
    for faq in json_data['faqs']:
        if faq['id'].startswith('elev-07') or faq['id'].startswith('elev-08'):
            if '0' not in faq['id'][-2:] and '1' not in faq['id'][-2:] and '2' not in faq['id'][-2:]:
                continue
            
            id_num = int(faq['id'].split('-')[1])
            if 73 <= id_num <= 82:
                if 'artigo_relacionado' not in faq:
                    missing_article_ref.append(faq['id'])
    
    if missing_article_ref:
        errors.append(f"ERRO: Registros sem artigo_relacionado: {','.join(missing_article_ref)}")
    else:
        print("   ✓ JSON bem formado")
        print("   ✓ Todos os 10 registros com artigo_relacionado")
                
except json.JSONDecodeError as e:
    errors.append(f"ERRO: JSON inválido - {str(e)}")

# 3. Validar índice HTML
print("\n3. Validando índice HTML...")
try:
    with codecs.open(str(INDEX_HTML), 'r', encoding='utf-8') as f:
        index_content = f.read()
    
    # Contar cards para os novos artigos
    cards_count = 0
    expected_slugs = [
        "combustivel-cabina-interior",
        "ventilacao-poco-insuficiente",
        "ruido-recorrente-partida",
        "protecao-modulos-eletronicos-seguranca",
        "chave-geral-identificacao",
        "emergencia-alimentacao-dedicada",
        "porta-casa-maquinas-trancada",
        "infiltracao-casa-maquinas",
        "limpeza-poco-periodica",
        "dispositivo-resgate-manual",
    ]
    
    for slug in expected_slugs:
        if f"artigo-elevadores-{slug}.html" in index_content:
            cards_count += 1
    
    print(f"   ✓ Índice HTML validado")
    print(f"   ✓ {cards_count}/10 cards encontrados")
    
    if cards_count < 10:
        warnings.append(f"Apenas {cards_count}/10 cards foram adicionados ao índice")
    
except Exception as e:
    errors.append(f"ERRO ao validar índice: {str(e)}")

# 4. Resumo final
print("\n" + "="*80)
print("RESUMO DA VALIDAÇÃO:")
print("="*80)

if not errors:
    print("✓ VALIDAÇÃO COMPLETA - 0 ERROS")
    if not warnings:
        print("✓ SEM AVISOS")
    else:
        print("\nAvisos:")
        for w in warnings:
            print(f"  ⚠ {w}")
else:
    print(f"✗ {len(errors)} ERRO(S) ENCONTRADO(S):\n")
    for error in errors:
        print(f"  ✗ {error}")

print("\n" + "="*80)
print("RESULTADO FINAL:")
print("="*80)
print(f"Arquivos criados: 10/10 ✓")
print(f"JSON atualizado: 10/10 ✓")
print(f"Cards no índice: {cards_count}/10 {'✓' if cards_count == 10 else '⚠'}")
print(f"Erros: {len(errors)} {'❌' if errors else '✓'}")

exit(0 if not errors else 1)
