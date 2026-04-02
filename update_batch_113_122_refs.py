#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Atualiza artigo_relacionado de elev-113..122 em:
- conhecimento-tecnico/dados/elevadores.json
- conhecimento-tecnico/index.html (snapshot embed)
- artigos/elevadores/index.html (cards)
"""

import json
import re
from pathlib import Path

BASE_DIR = Path(r"h:\apps\protoncd")
CREATED_FILE = BASE_DIR / "batch_113_122_created_files.json"
JSON_FILE = BASE_DIR / "conhecimento-tecnico" / "dados" / "elevadores.json"
INDEX_KT_FILE = BASE_DIR / "conhecimento-tecnico" / "index.html"
ELEVADORES_INDEX_FILE = BASE_DIR / "artigos" / "elevadores" / "index.html"


def load_created_map():
    items = json.loads(CREATED_FILE.read_text(encoding="utf-8"))
    return {item["id"]: item for item in items}


def inject_artigo_relacionado(text: str, item_map: dict, target_name: str):
    updates = 0

    for faq_id, item in item_map.items():
        id_pattern = re.compile(rf'"id"\s*:\s*"{re.escape(faq_id)}"|"id"\s*:\s*\s+"{re.escape(faq_id)}"')
        match = id_pattern.search(text)
        if not match:
            print(f"WARN [{target_name}]: ID não encontrado: {faq_id}")
            continue

        start = text.rfind("{", 0, match.start())
        if start == -1:
            print(f"WARN [{target_name}]: início de objeto não encontrado para {faq_id}")
            continue

        in_string = False
        escaped = False
        depth = 0
        end = None
        for i in range(start, len(text)):
            ch = text[i]
            if in_string:
                if escaped:
                    escaped = False
                elif ch == "\\":
                    escaped = True
                elif ch == '"':
                    in_string = False
                continue

            if ch == '"':
                in_string = True
                continue
            if ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
                if depth == 0:
                    end = i
                    break

        if end is None:
            print(f"WARN [{target_name}]: fim de objeto não encontrado para {faq_id}")
            continue

        obj = text[start:end + 1]
        if '"artigo_relacionado"' in obj:
            continue

        resp_match = re.search(r'\n([ \t]*)"responsabilidade"\s*:', obj)
        if not resp_match:
            print(f"WARN [{target_name}]: responsabilidade não encontrada para {faq_id}")
            continue

        indent = resp_match.group(1)
        insertion = (
            f'\n{indent}"artigo_relacionado": {{\n'
            f'{indent}    "titulo": "{item["title"]}",\n'
            f'{indent}    "url": "/artigos/elevadores/{item["filename"]}",\n'
            f'{indent}    "categoria": "Elevadores"\n'
            f'{indent}}},'
        )

        obj_new = re.sub(r'(\n[ \t]*"responsabilidade"\s*:)', insertion + r'\1', obj, count=1)
        text = text[:start] + obj_new + text[end + 1:]
        updates += 1

    print(f"OK [{target_name}]: {updates} inserções de artigo_relacionado")
    return text, updates


def update_elevadores_index_cards(text: str, item_map: dict):
    if any(item_map[k]["filename"] in text for k in item_map):
        print("OK [artigos/elevadores/index.html]: cards já presentes")
        return text, 0

    card_specs = {
        "elev-113": ("fas fa-door-open", "red", "Bypass no sensor de porta remove proteção e eleva risco imediato."),
        "elev-114": ("fas fa-fire-extinguisher", "red", "Sem prioridade de bombeiro funcional, o resgate fica comprometido."),
        "elev-115": ("fas fa-project-diagram", "red", "Sem redundância mínima, falha única pode gerar condição insegura."),
        "elev-116": ("fas fa-level-up-alt", "orange", "Falha recorrente de nivelamento aumenta risco de tropeço e queda."),
        "elev-117": ("fas fa-battery-half", "orange", "Sem autonomia comprovada, bateria de emergência pode falhar."),
        "elev-118": ("fas fa-volume-up", "blue", "Ruído em múltiplos pavimentos aponta possível falha sistêmica."),
        "elev-119": ("fas fa-lock", "red", "Sem trava elétrica no acesso técnico ao poço, risco é crítico."),
        "elev-120": ("fas fa-clipboard-list", "orange", "Sem plano preventivo formal, manutenção fica reativa e frágil."),
        "elev-121": ("fas fa-weight-hanging", "orange", "Controle de sobrecarga sem teste periódico pode falhar sem aviso."),
        "elev-122": ("fas fa-check-double", "red", "Após modernização, revalidação técnica é indispensável."),
    }

    cards = []
    for faq_id in sorted(item_map.keys()):
        item = item_map[faq_id]
        icon, color, desc = card_specs[faq_id]
        cards.append(
            f'''\n                <a href="{item["filename"]}" class="card hover-lift"
                    style="text-decoration:none;">
                    <div class="card-icon {color}"><i class="{icon}"></i></div>
                    <h3 class="card-title">{item["title"]}</h3>
                    <p class="card-text">{desc}</p>
                </a>\n'''
        )

    marker = "\n            </div>\n        </div>\n    </section>"
    if marker not in text:
        raise RuntimeError("Marcador de fechamento da grade não encontrado em artigos/elevadores/index.html")

    text = text.replace(marker, "".join(cards) + marker, 1)
    print("OK [artigos/elevadores/index.html]: 10 cards adicionados")
    return text, 10


def main():
    item_map = load_created_map()

    json_text = JSON_FILE.read_text(encoding="utf-8-sig")
    json_text, _ = inject_artigo_relacionado(json_text, item_map, "elevadores.json")
    JSON_FILE.write_text(json_text, encoding="utf-8")

    kt_text = INDEX_KT_FILE.read_text(encoding="utf-8-sig")
    kt_text, _ = inject_artigo_relacionado(kt_text, item_map, "conhecimento-tecnico/index.html")
    INDEX_KT_FILE.write_text(kt_text, encoding="utf-8")

    elev_idx_text = ELEVADORES_INDEX_FILE.read_text(encoding="utf-8-sig")
    elev_idx_text, _ = update_elevadores_index_cards(elev_idx_text, item_map)
    ELEVADORES_INDEX_FILE.write_text(elev_idx_text, encoding="utf-8")


if __name__ == "__main__":
    main()
