#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Script para corrigir encoding misto no cercon-goias.html

filepath = r'h:\apps\protoncd\cercon-goias.html'

# Mapeamento de caracteres com double-encoding para UTF-8 correto
encoding_fixes = {
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
    'Ã§Ã£': 'ção',
    'Ã§Ãµ': 'ções',
    'Â°': '°',
    'â ': '⚠',
    '�': 'í',  # fallback para caracteres genéricos quebrados
}

try:
    # Ler arquivo
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Aplicar correções
    for wrong, correct in encoding_fixes.items():
        content = content.replace(wrong, correct)
    
    # Escrever arquivo corrigido
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✓ {filepath} corrigido com sucesso!")
    
except Exception as e:
    print(f"✗ Erro: {str(e)}")
