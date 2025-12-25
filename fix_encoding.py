#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

# Lista de arquivos HTML para corrigir
files = [
    "analise-vibracao-elevadores.html",
    "cercon-goias.html",
    "franquias.html",
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
    "landing-servicos.html"
]

base_path = r"h:\apps\protoncd"
corrigidos = 0

for filename in files:
    filepath = os.path.join(base_path, filename)
    if os.path.exists(filepath):
        try:
            # Ler como UTF-8 (arquivo tem UTF-8 double-encoded)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Converter UTF-8 double-encoded para correto
            # Codificar em latin-1 e decodificar em UTF-8 novamente
            try:
                # Remove BOM se existir
                if content.startswith('\ufeff'):
                    content = content[1:]
                
                # Tenta corrigir double-encoding
                content_bytes = content.encode('latin-1')
                content_fixed = content_bytes.decode('utf-8')
                
                # Salvar corrigido
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content_fixed)
                
                corrigidos += 1
                print(f"✓ {filename}")
            except (UnicodeDecodeError, UnicodeEncodeError):
                print(f"⚠ {filename}: Já está correto ou outro problema")
        except Exception as e:
            print(f"✗ {filename}: {str(e)}")
    else:
        print(f"✗ {filename}: Arquivo não encontrado")

print(f"\n{corrigidos}/{len(files)} arquivos corrigidos com sucesso")
