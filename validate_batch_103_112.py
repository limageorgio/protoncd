#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Validação final do lote elev-103 a elev-112.
"""

import json
from pathlib import Path

BASE_DIR = Path(r"h:\apps\protoncd")
BATCH_FILE = BASE_DIR / "batch_103_112_created_files.json"
JSON_FILE = BASE_DIR / "conhecimento-tecnico" / "dados" / "elevadores.json"
KT_INDEX_FILE = BASE_DIR / "conhecimento-tecnico" / "index.html"
ELEV_INDEX_FILE = BASE_DIR / "artigos" / "elevadores" / "index.html"


def main():
    errors = []

    items = json.loads(BATCH_FILE.read_text(encoding="utf-8"))
    if len(items) != 10:
        errors.append(f"batch_103_112_created_files.json deveria ter 10 itens e tem {len(items)}")

    for item in items:
        p = BASE_DIR / "artigos" / "elevadores" / item["filename"]
        if not p.exists():
            errors.append(f"arquivo HTML ausente: {p.name}")

    data = json.loads(JSON_FILE.read_text(encoding="utf-8"))
    faqs = {faq.get("id"): faq for faq in data.get("faqs", [])}

    for item in items:
        faq = faqs.get(item["id"])
        if not faq:
            errors.append(f"ID não encontrado em elevadores.json: {item['id']}")
            continue
        art = faq.get("artigo_relacionado")
        if not art:
            errors.append(f"artigo_relacionado ausente em elevadores.json: {item['id']}")
            continue
        expected_url = f"/artigos/elevadores/{item['filename']}"
        if art.get("titulo") != item["title"]:
            errors.append(f"titulo divergente em elevadores.json para {item['id']}")
        if art.get("url") != expected_url:
            errors.append(f"url divergente em elevadores.json para {item['id']}")

    kt_text = KT_INDEX_FILE.read_text(encoding="utf-8")
    elev_index_text = ELEV_INDEX_FILE.read_text(encoding="utf-8")

    for item in items:
        rel_url = f"/artigos/elevadores/{item['filename']}"
        if rel_url not in kt_text:
            errors.append(f"referência ausente em conhecimento-tecnico/index.html: {rel_url}")
        if item["filename"] not in elev_index_text:
            errors.append(f"card ausente em artigos/elevadores/index.html: {item['filename']}")

    mojibake_files = [JSON_FILE, KT_INDEX_FILE, ELEV_INDEX_FILE]
    for fp in mojibake_files:
        text = fp.read_text(encoding="utf-8")
        if "�" in text:
            errors.append(f"caractere de substituição detectado em {fp.name}")

    if errors:
        print("VALIDAÇÃO: FALHOU")
        for err in errors:
            print(f"- {err}")
        raise SystemExit(1)

    print("VALIDAÇÃO: OK")
    print(f"Arquivos HTML: {len(items)}/10")
    print("JSON + snapshot + index de elevadores: OK")


if __name__ == "__main__":
    main()
