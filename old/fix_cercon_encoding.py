#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

# Script para corrigir encoding do cercon-goias.html

filepath = r'h:\apps\protoncd\cercon-goias.html'

try:
    # Ler arquivo
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remover BOM se existir
    if content.startswith('\ufeff'):
        content = content[1:]

    # Corrigir double-encoding: encode como latin-1, decode como UTF-8
    content_bytes = content.encode('latin-1')
    content_fixed = content_bytes.decode('utf-8')
    
    # Escrever arquivo corrigido
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content_fixed)
    
    print(f"SUCESSO: {filepath} corrigido!")
    sys.exit(0)
    
except Exception as e:
    print(f"ERRO: {str(e)}")
    sys.exit(1)
