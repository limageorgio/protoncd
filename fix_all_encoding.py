#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para corrigir encoding UTF-8 em todos os arquivos HTML
Baseado no padrão correto do index.html
"""

import os
import glob
import re
from pathlib import Path

# Mapeamento completo de caracteres corrompidos -> corretos
ENCODING_FIXES = {
    # Caracteres individuais mais comuns
    'Ã§': 'ç',
    'Ã£': 'ã',
    'Ã¡': 'á',
    'Ã©': 'é',
    'Ã³': 'ó',
    'Ã­': 'í',
    'Ãº': 'ú',
    'Ã¢': 'â',
    'Ãª': 'ê',
    'Ã´': 'ô',
    'Ã': 'Ã',
    'Â°': '°',
    'Ã‡': 'Ç',
    'Ã': 'Á',
    'É': 'É',
    'Ã"': 'Ó',
    'Ãš': 'Ú',
    
    # Sequências compostas (importantes!)
    'Ã§Ã£': 'ção',
    'Ã§Ãµ': 'ções',
    'Ã§Ã£o': 'ção',
    'Ã§Ãµes': 'ções',
    
    # Caracteres especiais corrompidos
    'â€¢': '•',
    'â€"': '—',
    'â€"': '–',
    'â€˜': ''',
    'â€™': ''',
    'â€œ': '"',
    'â€': '"',
    'â€¦': '…',
    'â ': '⚠',
    'âœ"': '✓',
    'âœ…': '✅',
    'â­': '⭐',
    
    # Padrões específicos encontrados
    '�': 'í',  # Fallback genérico
    'mecÃ¢nico': 'mecânico',
    'mecÃ¢nicos': 'mecânicos',
    'tÃ©cnico': 'técnico',
    'tÃ©cnicos': 'técnicos',
    'tÃ©cnica': 'técnica',
    'tÃ©cnicas': 'técnicas',
    'inspeÃ§Ã£o': 'inspeção',
    'inspeÃ§Ãµes': 'inspeções',
    'elevaÃ§Ã£o': 'elevação',
    'prevenÃ§Ã£o': 'prevenção',
    'manutenÃ§Ã£o': 'manutenção',
    'soluÃ§Ã£o': 'solução',
    'soluÃ§Ãµes': 'soluções',
    'construÃ§Ã£o': 'construção',
    'operaÃ§Ã£o': 'operação',
    'edificaÃ§Ã£o': 'edificação',
    'edificaÃ§Ãµes': 'edificações',
    'instalaÃ§Ã£o': 'instalação',
    'instalaÃ§Ãµes': 'instalações',
    'regularizaÃ§Ã£o': 'regularização',
    'digitalizaÃ§Ã£o': 'digitalização',
    'renovaÃ§Ã£o': 'renovação',
    'adequaÃ§Ã£o': 'adequação',
    'adequaÃ§Ãµes': 'adequações',
    'locaÃ§Ã£o': 'locação',
    'protocolaÃ§Ã£o': 'protocolação',
    'documentaÃ§Ã£o': 'documentação',
    'especificaÃ§Ã£o': 'especificação',
    'especificaÃ§Ãµes': 'especificações',
    'certificaÃ§Ã£o': 'certificação',
    'verificaÃ§Ã£o': 'verificação',
    'pressÃµes': 'pressões',
    'pressÃ£o': 'pressão',
    'dimensÃµes': 'dimensões',
    'dimensÃ£o': 'dimensão',
    'condiÃ§Ãµes': 'condições',
    'condiÃ§Ã£o': 'condição',
    'informaÃ§Ãµes': 'informações',
    'informaÃ§Ã£o': 'informação',
    'orientaÃ§Ãµes': 'orientações',
    'orientaÃ§Ã£o': 'orientação',
    'recomendaÃ§Ãµes': 'recomendações',
    'recomendaÃ§Ã£o': 'recomendação',
    'prevÃªs': 'prevês',
    'inglÃªs': 'inglês',
    'portuguÃªs': 'português',
    'atravÃ©s': 'através',
    'apÃ³s': 'após',
    'jÃ¡': 'já',
    'sÃ³': 'só',
    'atÃ©': 'até',
    'nÃ£o': 'não',
    'sÃ£o': 'são',
    'Ã©': 'é',
    'serÃ¡': 'será',
    'estarÃ¡': 'estará',
    'farÃ¡': 'fará',
    'terÃ¡': 'terá',
    'poderÃ¡': 'poderá',
    'deverÃ¡': 'deverá',
    'condomÃ­nio': 'condomínio',
    'condomÃ­nios': 'condomínios',
    'indÃºstria': 'indústria',
    'histÃ³ria': 'história',
    'memÃ³ria': 'memória',
    'prÃ³prio': 'próprio',
    'prÃ³pria': 'própria',
    'prÃ³prios': 'próprios',
    'prÃ³xima': 'próxima',
    'prÃ³ximo': 'próximo',
    'Ãºltimo': 'último',
    'Ãºltima': 'última',
    'Ãºnicos': 'únicos',
    'Ãºnica': 'única',
    'obrigatÃ³rio': 'obrigatório',
    'obrigatÃ³ria': 'obrigatória',
    'necessÃ¡rio': 'necessário',
    'necessÃ¡ria': 'necessária',
    'necessÃ¡rios': 'necessários',
    'incÃªndio': 'incêndio',
    'incÃªndios': 'incêndios',
    'GÃ¡s': 'Gás',
    'gÃ¡s': 'gás',
    'GLP': 'GLP',
    'HÃ­drico': 'Hídrico',
    'hidrÃ¡ulico': 'hidráulico',
    'hidrÃ¡ulica': 'hidráulica',
    'hidrÃ¡ulicos': 'hidráulicos',
    'elÃ©trico': 'elétrico',
    'elÃ©trica': 'elétrica',
    'elÃ©tricos': 'elétricos',
    'GeiÃ¢nia': 'Goiânia',
    'GoiÃ¢nia': 'Goiânia',
    'Goiínia': 'Goiânia',
    'GoiÃ¡s': 'Goiás',
    'Goiís': 'Goiás',
    'AnÃ¡polis': 'Anápolis',
    'Anípolis': 'Anápolis',
    'BrasÃ­lia': 'Brasília',
    'Brasília': 'Brasília',
    'pÃ¡gina': 'página',
    'PÃ¡gina': 'Página',
    'Pígina': 'Página',
    'orÃ§amento': 'orçamento',
    'oriamento': 'orçamento',
    'serviÃ§o': 'serviço',
    'serviÃ§os': 'serviços',
    'seriios': 'serviços',
    'experiÃªncia': 'experiência',
    'anÃ¡lise': 'análise',
    'diagnÃ³stico': 'diagnóstico',
    'diagnóstico': 'diagnóstico',
    'Ã¡rea': 'área',
    'Ã¡reas': 'áreas',
    'prÃ¡tica': 'prática',
    'prÃ¡tico': 'prático',
    'bÃ¡sico': 'básico',
    'bÃ¡sica': 'básica',
    'fÃ­sico': 'físico',
    'fÃ­sica': 'física',
    'fÃ­sicos': 'físicos',
    'mÃ©dio': 'médio',
    'mÃ©dia': 'média',
    'Ã¡gil': 'ágil',
    'fÃ¡cil': 'fácil',
    'difÃ­cil': 'difícil',
    'pÃºblico': 'público',
    'pÃºblica': 'pública',
    'estÃ¡': 'está',
    'serÃ£o': 'serão',
    'tambÃ©m': 'também',
    'vocÃª': 'você',
    'sÃ­ndico': 'síndico',
    'sÃ­ndicos': 'síndicos',
    'lÃ­quido': 'líquido',
    'sÃ³lido': 'sólido',
    'vÃ¡lido': 'válido',
    'vÃ¡lida': 'válida',
    'cÃ³digo': 'código',
    'licenÃ§a': 'licença',
    'licenía': 'licença',
    'nÃ­vel': 'nível',
    'nÃ­veis': 'níveis',
    'veÃ­culo': 'veículo',
    'veÃ­culos': 'veículos',
    'ImÃ³vel': 'Imóvel',
    'imÃ³vel': 'imóvel',
    'imÃ³veis': 'imóveis',
    'mÃ³vel': 'móvel',
    'mÃ³veis': 'móveis',
    'negÃ³cio': 'negócio',
    'negÃ³cios': 'negócios',
    'Ã­ndice': 'índice',
    'Ã­ndices': 'índices',
    'anÃºncio': 'anúncio',
    'anÃºncios': 'anúncios',
    'perÃ­cia': 'perícia',
    'perÃ­cias': 'perícias',
    'sÃ©rie': 'série',
    'sÃ©ries': 'séries',
    'famÃ­lia': 'família',
    'famÃ­lias': 'famílias',
    'garantÃ­a': 'garantia',
    'tÃ­tulo': 'título',
    'tÃ­tulos': 'títulos',
    'autÃ´nomo': 'autônomo',
    'autÃ´noma': 'autônoma',
    'econÃ´mico': 'econômico',
    'econÃ´mica': 'econômica',
    'mÃ­nimo': 'mínimo',
    'mÃ­nima': 'mínima',
    'mÃ¡ximo': 'máximo',
    'mÃ¡xima': 'máxima',
    'Ã³timo': 'ótimo',
    'Ã³tima': 'ótima',
    'rÃ¡pido': 'rápido',
    'rÃ¡pida': 'rápida',
    'prÃ¡tico': 'prático',
    'prÃ¡tica': 'prática',
    'ímóvel': 'imóvel',
    'ímóveis': 'imóveis',
}

def fix_encoding(text):
    """
    Corrige encoding UTF-8 corrompido no texto
    Aplica substituições em ordem (mais específicas primeiro)
    """
    # Ordenar por tamanho (maior primeiro) para evitar substituições parciais
    sorted_fixes = sorted(ENCODING_FIXES.items(), key=lambda x: len(x[0]), reverse=True)
    
    for wrong, right in sorted_fixes:
        if wrong in text:
            text = text.replace(wrong, right)
            
    return text

def process_html_file(file_path):
    """
    Processa um arquivo HTML corrigindo o encoding
    """
    try:
        # Ler arquivo
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        # Guardar conteúdo original para comparação
        original_content = content
        
        # Aplicar correções
        fixed_content = fix_encoding(content)
        
        # Só escrever se houver mudanças
        if fixed_content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(fixed_content)
            
            # Contar quantas substituições foram feitas
            changes = sum(1 for w, r in ENCODING_FIXES.items() if w in original_content)
            print(f"✓ {file_path}: {changes} tipos de correções aplicadas")
            return True
        else:
            print(f"○ {file_path}: já está correto")
            return False
            
    except Exception as e:
        print(f"✗ Erro em {file_path}: {str(e)}")
        return False

def main():
    """
    Processa todos os arquivos HTML no diretório
    """
    base_dir = Path(__file__).parent
    
    # Encontrar todos os arquivos HTML
    html_files = []
    html_files.extend(glob.glob(str(base_dir / "*.html")))
    html_files.extend(glob.glob(str(base_dir / "*" / "*.html")))
    html_files.extend(glob.glob(str(base_dir / "*" / "*" / "*.html")))
    
    # Excluir google-verification-example.html
    html_files = [f for f in html_files if 'google-verification-example' not in f]
    
    print(f"\n{'='*70}")
    print(f"CORREÇÃO DE ENCODING UTF-8 - TODOS OS ARQUIVOS HTML")
    print(f"{'='*70}\n")
    print(f"Encontrados {len(html_files)} arquivos HTML para processar\n")
    
    fixed_count = 0
    already_ok_count = 0
    error_count = 0
    
    for html_file in sorted(html_files):
        result = process_html_file(html_file)
        if result:
            fixed_count += 1
        elif result is False:
            already_ok_count += 1
        else:
            error_count += 1
    
    print(f"\n{'='*70}")
    print(f"RESULTADO:")
    print(f"  ✓ Arquivos corrigidos: {fixed_count}")
    print(f"  ○ Arquivos já corretos: {already_ok_count}")
    if error_count > 0:
        print(f"  ✗ Erros: {error_count}")
    print(f"{'='*70}\n")

if __name__ == "__main__":
    main()
