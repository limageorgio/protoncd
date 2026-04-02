#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Validação do lote elev-083 a elev-092.
"""

import json
import sys
from pathlib import Path

BASE_DIR = Path(r"h:\apps\protoncd")
ARTIGOS_DIR = BASE_DIR / "artigos" / "elevadores"
JSON_FILE = BASE_DIR / "conhecimento-tecnico" / "dados" / "elevadores.json"
KT_INDEX_FILE = BASE_DIR / "conhecimento-tecnico" / "index.html"
ELEV_INDEX_FILE = BASE_DIR / "artigos" / "elevadores" / "index.html"
CREATED_FILE = BASE_DIR / "batch_083_092_created_files.json"

BAD_TERMS = ["TÃ", "Nao", "Correcao", "Inspecao", "Tecnico", "emergencia"]
ALLOWED_ASCII_WORDS = {"inspecao", "tecnico", "emergencia"}


def main():
    errors = []

    if not CREATED_FILE.exists():
        errors.append("Arquivo batch_083_092_created_files.json não encontrado")
        print_report(errors)
        return 1

    created = json.loads(CREATED_FILE.read_text(encoding="utf-8"))
    if len(created) != 10:
        errors.append(f"Quantidade de arquivos no índice diferente de 10: {len(created)}")

    for item in created:
        file_path = ARTIGOS_DIR / item["filename"]
        if not file_path.exists():
            errors.append(f"Arquivo HTML ausente: {item['filename']}")
            continue

        text = file_path.read_text(encoding="utf-8")
        required_markers = [
            "<meta name=\"description\"",
            "<h1>",
            "article-mini-stats",
            "risk-chart",
            "decision-table",
            "cta-section",
        ]
        for marker in required_markers:
            if marker not in text:
                errors.append(f"{item['filename']}: marcador ausente -> {marker}")

        for term in BAD_TERMS:
            if term in text:
                if term.lower() in ALLOWED_ASCII_WORDS:
                    continue
                errors.append(f"{item['filename']}: termo possivelmente corrompido -> {term}")

    data = json.loads(JSON_FILE.read_text(encoding="utf-8-sig"))
    faqs = {faq["id"]: faq for faq in data.get("faqs", [])}

    for item in created:
        faq = faqs.get(item["id"])
        if not faq:
            errors.append(f"JSON: ID ausente -> {item['id']}")
            continue
        rel = faq.get("artigo_relacionado")
        if not rel:
            errors.append(f"JSON: artigo_relacionado ausente -> {item['id']}")
            continue
        expected_url = f"/artigos/elevadores/{item['filename']}"
        if rel.get("url") != expected_url:
            errors.append(f"JSON: URL divergente em {item['id']} -> {rel.get('url')} != {expected_url}")

    kt_text = KT_INDEX_FILE.read_text(encoding="utf-8-sig")
    for item in created:
        expected_url = f"/artigos/elevadores/{item['filename']}"
        if item["id"] not in kt_text:
            errors.append(f"Snapshot: ID ausente no conhecimento-tecnico/index.html -> {item['id']}")
        if expected_url not in kt_text:
            errors.append(f"Snapshot: URL ausente no conhecimento-tecnico/index.html -> {expected_url}")

    elev_text = ELEV_INDEX_FILE.read_text(encoding="utf-8-sig")
    for item in created:
        if item["filename"] not in elev_text:
            errors.append(f"Índice de elevadores: card/link ausente -> {item['filename']}")

    print_report(errors)
    return 1 if errors else 0


def print_report(errors):
    print("=" * 80)
    print("VALIDAÇÃO FINAL - LOTE ELEV-083 A ELEV-092")
    print("=" * 80)
    if errors:
        print(f"\nERROS ({len(errors)}):")
        for err in errors:
            print(f"- {err}")
        print("\nSTATUS: FALHOU")
    else:
        print("\nSTATUS: OK - 0 erros")


if __name__ == "__main__":
    sys.exit(main())
