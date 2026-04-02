#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Remove BOM from JSON file
"""
import codecs
from pathlib import Path

JSON_FILE = Path(r"h:\apps\protoncd\conhecimento-tecnico\dados\elevadores.json")

# Re-escrever JSON sem BOM
with open(str(JSON_FILE), 'r', encoding='utf-8-sig') as f:
    content = f.read()

# Escrever sem BOM (usar UTF-8 puro)
with open(str(JSON_FILE), 'w', encoding='utf-8') as f:
    f.write(content)

print("✓ BOM removido do JSON")
print("✓ Arquivo reescrito com UTF-8 puro (sem BOM)")
