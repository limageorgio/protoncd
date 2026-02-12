#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para remover toda indentação excessiva do HTML
"""

import re

def clean_html(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove espaços em branco excessivos no início das linhas
    lines = content.split('\n')
    cleaned_lines = []
    
    for line in lines:
        # Remove todos os espaços do início
        stripped = line.lstrip()
        
        if not stripped:
            cleaned_lines.append('')
            continue
        
        # Reconstrói com indentação mínima baseado no contexto
        # Tags que devem começar na coluna 0
        if re.match(r'^<!DOCTYPE|^<html|^</html>', stripped):
            cleaned_lines.append(stripped)
        # Tags dentro de <head> ou no início de <body>
        elif re.match(r'^<head|^</head>|^<body|^</body>', stripped):
            cleaned_lines.append('    ' + stripped if not stripped.startswith('</') else stripped)
        # Conteúdo normal
        else:
            # Conta quantas tags de abertura vs fechamento temos até agora
            cleaned_lines.append(stripped)
    
    # Junta tudo
    result = '\n'.join(cleaned_lines)
    
    # Remove linhas vazias múltiplas
    result = re.sub(r'\n\n\n+', '\n\n', result)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(result)
    
    print(f"✓ Arquivo limpo salvo em: {output_file}")
    print(f"  Linhas originais: {len(lines)}")
    print(f"  Linhas limpas: {len(cleaned_lines)}")

if __name__ == '__main__':
    input_file = 'H:/apps/protoncd/teste-arrancamento-olhais.html'
    output_file = 'H:/apps/protoncd/teste-arrancamento-olhais.html'
    
    clean_html(input_file, output_file)
    print("\n✓ Limpeza concluída!")
