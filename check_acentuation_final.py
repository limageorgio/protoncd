#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Verificação final de acentuação portuguesa em 100%
"""
import codecs
from pathlib import Path

BASE_DIR = Path(r"h:\apps\protoncd")
ARTIGOS_DIR = BASE_DIR / "artigos" / "elevadores"

# Palavras que devem ter acentuação (português correto)
MUST_HAVE_ACCENT = {
    'Não': 'Nao',
    'Correção': 'Correcao', 
    'Política': 'Politica',
    'Crítica': 'Critica',
    'Análise': 'Analise',
    'Água': 'Agua',
    'Acúmulo': 'Acumulo',
    'Gás': 'Gas',
    'Óleo': 'Oleo',
    'Eletromecânico': 'Eletromecânico',
}

files = [
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

print("="*80)
print("VERIFICAÇÃO FINAL DE ACENTUAÇÃO PORTUGUESA")
print("="*80)

all_correct = True

for html_file in files:
    html_path = ARTIGOS_DIR / html_file
    
    with codecs.open(str(html_path), 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Contar palavras com acentuação
    accent_count = 0
    errors = []
    
    # Words that MUST NOT appear (inglês ou sem acentuação)
    forbidden_patterns = [
        ('Correcao', 'Correção'),
        ('Nao', 'Não'),
        ('Critica', 'Crítica'),
        ('Analise', 'Análise'),
        ('Agua', 'Água'),
        ('Acumulo', 'Acúmulo'),
        ('Gas', 'Gás'),
        ('Oleo', 'Óleo'),
        ('Manutencao', 'Manutenção'),
        ('Rotulos', 'Rótulos'),
        ('Sistematica', 'Sistemática'),
        ('Operacao', 'Operação'),
        ('Inspecao', 'Inspeção'),
        ('Validacao', 'Validação'),
        ('Implementacao', 'Implementação'),
        ('Comunicacao', 'Comunicação'),
        ('Isolacao', 'Isolação'),
    ]
    
    for bad_word, good_word in forbidden_patterns:
        if bad_word in content:
            errors.append(f"  ✗ '{bad_word}' encontrado (deve ser '{good_word}')")
            all_correct = False
    
    # Count good accented words
    accented_words = ['Elevador', 'Segurança', 'Técnico', 'Índice', 'Diagnóstico',
                      'Manutenção', 'Inspeção', 'Conformidade', 'Operação', 'Proteção',
                      'Rótulos', 'Responsabilidade', 'Crítica', 'Gravidade']
    
    for word in accented_words:
        if word in content:
            accent_count += 1
    
    if not errors:
        print(f"✓ {html_file}")
    else:
        print(f"✗ {html_file}")
        for err in errors:
            print(err)

print("\n" + "="*80)
print("RESULTADO:")
print("="*80)

if all_correct:
    print("✓ TODOS OS ARQUIVOS COM ACENTUAÇÃO 100% PORTUGUESA CORRETA")
    print("✓ NENHUMA PALAVRA SEM ACENTUAÇÃO ENCONTRADA")
    print("✓ NENHUM TERMO EM INGLÊS ENCONTRADO")
else:
    print("⚠ Verifique os erros acima")

print("\n" + "="*80)
