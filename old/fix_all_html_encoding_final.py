#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script otimizado para correção de encoding UTF-8 em TODOS os arquivos HTML do projeto protoncd.
Corrige caracteres corrompidos de forma completa e precisa.
"""

import os
import re
from pathlib import Path

# Dicionário completo de correções de encoding
ENCODING_FIXES = {
    # Correções de ção/çao/ção
    'í\u00edo': 'ção',
    'í\u00edes': 'ções',
    'í\u00ed': 'çã',
    'i\u00f3es': 'ções',
    
    # Correções de ã
    'N\u00c1O': 'NÃO',
    'N\u00edo': 'Não',
    'n\u00edo': 'não',
    's\u00edo': 'são',
    'S\u00edo': 'São',
    'mío': 'mão',
    'Goiínia': 'Goiânia',
    'Anípolis': 'Anápolis',
    'írgío': 'órgão',
    'írgíos': 'órgãos',
    'instal aííes': 'instalações',
    'inst alaííes': 'instalações',
    'inst ala\u00ed\u00edes': 'instalações',
    'repartiííes': 'repartições',
    'instituiííes': 'instituições',
    'edific aííes': 'edificações',
    'edifica\u00ed\u00edes': 'edificações',
    'recomendaííes': 'recomendações',
    'informa\u00ed\u00edes': 'informações',
    'adequ aííes': 'adequações',
    'adequa\u00ed\u00edes': 'adequações',
    'atualiz aííes': 'atualizações',
    'atualiza\u00ed\u00edes': 'atualizações',
    'manuten\u00ed\u00edes': 'manutenções',
    'vibr aííes': 'vibrações',
    'vibra\u00ed\u00edes': 'vibrações',
    'medií\u00edes': 'medições',
    'negocia\u00ed\u00edes': 'negociações',
    'condi\u00ed\u00edes': 'condições',
    'solu\u00ed\u00edes': 'soluções',
    'opera\u00ed\u00edes': 'operações',
    'movimenta\u00ed\u00edes': 'movimentações',
    'especifica\u00ed\u00edes': 'especificações',
    
    # Correções de á
    'ATENÇÁO': 'ATENÇÃO',
    'esten\u00e7\u00e1o': 'atenção',
    'Goi\u00e1s': 'Goiás',
    '\u00e1rea': 'área',
    '\u00e1reas': 'áreas',
    'est\u00e1': 'está',
    'est\u00e3o': 'estão',
    'ser\u00e1': 'será',
    'ser\u00e3o': 'serão',
    'j\u00e1': 'já',
    't\u00e9cnica': 'técnica',
    't\u00e9cnicas': 'técnicas',
    't\u00e9cnicos': 'técnicos',
    't\u00e9cnico': 'técnico',
    'mec\u00ednica': 'mecânica',
    'mec\u00ednicos': 'mecânicos',
    'mec\u00ednico': 'mecânico',
    'an\u00edlise': 'análise',
    'hidr\u00edulico': 'hidráulico',
    'hidr\u00edulica': 'hidráulica',
    'hidr\u00edulicos': 'hidráulicos',
    'pr\u00edpria': 'própria',
    'pr\u00edprio': 'próprio',
    'neg\u00edcio': 'negócio',
    'neg\u00edcios': 'negócios',
    'obrigat\u00edrio': 'obrigatório',
    'obrigat\u00edria': 'obrigatória',
    'necess\u00edrio': 'necessário',
    'necess\u00edria': 'necessária',
    'necess\u00edrios': 'necessários',
    'experi\u00edncia': 'experiência',
    'h\u00e1': 'há',
    'G\u00e1s': 'Gás',
    'g\u00e1s': 'gás',
    'ímb ito': 'âmbito',
    
    # Correções de é
    '\u00e9': 'é',
    'at\u00e9': 'até',
    'voc\u00ea': 'você',
    'caf\u00e9': 'café',
    'tr\u00eas': 'três',
    'inc\u00eandio': 'incêndio',
    'Bras\u00edlia': 'Brasília',
    
    # Correções de ç
    'seguran\u00eda': 'segurança',
    'aten\u00e7\u00e3o': 'atenção',
    'inspe\u00e7\u00e3o': 'inspeção',
    'manuten\u00e7\u00e3o': 'manutenção',
    'servi\u00e7o': 'serviço',
    'servi\u00e7os': 'serviços',
    'preven\u00e7\u00e3o': 'prevenção',
    'opera\u00e7\u00e3o': 'operação',
    'produ\u00e7\u00e3o': 'produção',
    'avan\u00e7ada': 'avançada',
    'avan\u00e7ado': 'avançado',
    'balan\u00e7o': 'balanço',
    'crian\u00e7a': 'criança',
    'crian\u00e7as': 'crianças',
    
    # Correções de í
    'pa\u00eds': 'país',
    'a\u00ed': 'aí',
    'da\u00ed': 'daí',
    'n\u00edveis': 'níveis',
    'dif\u00edcil': 'difícil',
    'ru\u00eddo': 'ruído',
    'ru\u00eddos': 'ruídos',
    'jur\u00eddica': 'jurídica',
    'jur\u00eddico': 'jurídico',
    'S\u00edndico': 'Síndico',
    's\u00edndico': 'síndico',
    's\u00edndicos': 'síndicos',
    
    # Correções de ó
    's\u00f3': 'só',
    'n\u00f3s': 'nós',
    'ap\u00f3s': 'após',
    '\u00f3leo': 'óleo',
    '\u00f3rg\u00e3o': 'órgão',
    '\u00f3rg\u00e3os': 'órgãos',
    'diagn\u00f3stico': 'diagnóstico',
    'diagn\u00f3stica': 'diagnóstica',
    'Catal\u00edo': 'Catalão',
    
    # Correções de ú
    '\u00faltimo': 'último',
    '\u00faltima': 'última',
    '\u00fanica': 'única',
    '\u00fanico': 'único',
    'Cuiab\u00ed': 'Cuiabá',
    
    # Correções de ê
    'voc\u00ea': 'você',
    'tr\u00eas': 'três',
    'inc\u00eandio': 'incêndio',
    
    # Correções de â
    'mec\u00e2nico': 'mecânico',
    'mec\u00e2nica': 'mecânica',
    'Anípolis': 'Anápolis',
    'Goiínia': 'Goiânia',
    '\u00e2mbito': 'âmbito',
    'inst\u00e2ncia': 'instância',
    'import\u00e2ncia': 'importância',
    
    # Correções de ô
    'av\u00f4': 'avô',
    'rob\u00f4': 'robô',
    
    # Correções de à
    '\u00ed': 'à',
    
    # Correções específicas de palavras compostas
    'Renova\u00ed\u00edo': 'Renovação',
    'renova\u00ed\u00edo': 'renovação',
    'Digitaliza\u00ed\u00edo': 'Digitalização',
    'digitaliza\u00ed\u00edo': 'digitalização',
    'Inspe\u00ed\u00edo': 'Inspeção',
    'inspe\u00ed\u00edo': 'inspeção',
    'Inspe\u00ed\u00edes': 'Inspeções',
    'inspe\u00ed\u00edes': 'inspeções',
    'Pressuriza\u00ed\u00edo': 'Pressurização',
    'pressuriza\u00ed\u00edo': 'pressurização',
    'Automa\u00ed\u00edo': 'Automação',
    'automa\u00ed\u00edo': 'automação',
    'Eletr\u00ednica': 'Eletrônica',
    'eletr\u00ednica': 'eletrônica',
    'Capacita\u00ed\u00edo': 'Capacitação',
    'capacita\u00ed\u00edo': 'capacitação',
    
    # Correções de emojis
    '??': '📋',
    '\u00ed\u00edO': 'ÇÃO',
    
    # Correções de graus
    '360\u00ed': '360°',
    '360\u00ba': '360°',
}

def fix_encoding_in_file(file_path):
    """
    Corrige encoding UTF-8 em um arquivo HTML.
    
    Args:
        file_path: Caminho do arquivo HTML
        
    Returns:
        Número de correções realizadas
    """
    try:
        # Ler arquivo
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        original_content = content
        corrections_count = 0
        
        # Aplicar todas as correções
        for wrong, correct in ENCODING_FIXES.items():
            if wrong in content:
                count = content.count(wrong)
                content = content.replace(wrong, correct)
                corrections_count += count
        
        # Salvar apenas se houve mudanças
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✓ {file_path.name}: {corrections_count} correções aplicadas")
            return corrections_count
        else:
            print(f"○ {file_path.name}: Já está correto")
            return 0
            
    except Exception as e:
        print(f"✗ ERRO em {file_path.name}: {str(e)}")
        return 0

def main():
    """Processa todos os arquivos HTML do projeto."""
    print("=" * 70)
    print("CORREÇÃO DE ENCODING UTF-8 - PROTON CD")
    print("=" * 70)
    print()
    
    # Lista de arquivos HTML para processar
    html_files = [
        "cercon-goias.html",
        "franquias.html",
        "analise-vibracao-elevadores.html",
        "inspecao-casa-bombas.html",
        "inspecao-combate-incendio.html",
        "inspecao-gas-predial.html",
        "inspecao-hvac-pmoc.html",
        "inspecao-playgrounds.html",
        "inspecao-pressurizacao-escadas.html",
        "inspecao-sistemas-mecanicos.html",
        "laudo-pericial-engenharia.html",
        "pacotes-servicos.html",
        "teste-arrancamento-olhais.html",
        "landing-servicos.html",
        "goiania/inspecao-predial-goiania.html",
        "anapolis/inspecao-predial-anapolis.html",
        "brasilia/inspecao-predial-brasilia.html",
        "rio-verde/inspecao-predial-rio-verde.html",
        "conhecimento-tecnico/index.html",
    ]
    
    base_path = Path(__file__).parent
    total_corrections = 0
    processed_files = 0
    
    for html_file in html_files:
        file_path = base_path / html_file
        if file_path.exists():
            corrections = fix_encoding_in_file(file_path)
            total_corrections += corrections
            processed_files += 1
        else:
            print(f"⚠ {html_file}: Arquivo não encontrado")
    
    print()
    print("=" * 70)
    print(f"RESUMO: {processed_files} arquivos processados | {total_corrections} correções realizadas")
    print("=" * 70)

if __name__ == "__main__":
    main()
