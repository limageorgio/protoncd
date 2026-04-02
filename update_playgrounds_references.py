#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import os
import re
import unicodedata
import sys

try:
    def remove_accents(text):
        """Remove acentuação e converte para slug."""
        text = unicodedata.normalize('NFKD', text)
        text = ''.join([c for c in text if not unicodedata.combining(c)])
        return text

    def convert_to_slug(text):
        """Converte texto em slug."""
        # Tentar extrair texto entre aspas simples (onde está a irregularidade)
        match = re.search(r"'([^']+)'", text)
        if match:
            text = match.group(1)
        
        text = remove_accents(text).lower()
        text = re.sub(r"['\"()_-]", " ", text)
        text = re.sub(r"[^a-z0-9\s]", "", text)
        text = re.sub(r"\s+", " ", text).strip()
        text = text.replace(" ", "-")
        text = re.sub(r"-+", "-", text)
        return text.strip("-")

    json_path = r"h:\apps\protoncd\conhecimento-tecnico\dados\playgrounds.json"
    playgrounds_dir = r"h:\apps\protoncd\artigos\playgrounds"
    base_url = "https://www.protoncd.com.br/artigos/playgrounds"
    special_file_by_id = {
        "play-081": "artigo-playground-superficie-acesso-risco-escorregamento.html",
        "play-082": "artigo-playground-suspensao-rigida-balanco-tradicional.html",
        "play-083": "artigo-playground-presenca-plantas-toxicas-espinhosas.html",
        "play-084": "artigo-playground-extremidades-tubos-sem-vedacao-tampao.html",
        "play-085": "artigo-playground-vao-inferior-carrossel-60mm-400mm.html",
        "play-086": "artigo-playground-vao-solo-inadequado.html",
        "play-087": "artigo-playground-vegetacao-espinhos-frutos-venenosos.html",
        "play-088": "artigo-playground-velocidade-tirolesa-acima-7ms.html",
        "play-089": "artigo-playground-velocidade-carrossel-acima-5ms.html",
        "play-090": "artigo-playground-seccao-transversal-fechada-sem-visibilidade.html"
    }

    print("Lendo JSON...")
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    specific_count = 0
    fallback_count = 0
    total = len(data['faqs'])

    print(f"Total de FAQs: {total}\n")

    for i, faq in enumerate(data['faqs'], 1):
        faq_id = faq['id']
        pergunta = faq['pergunta']
        
        try:
            slug = convert_to_slug(pergunta)
            expected_file = special_file_by_id.get(faq_id, f"artigo-playground-{slug}.html")
            full_path = os.path.join(playgrounds_dir, expected_file)
            
            if os.path.exists(full_path):
                faq['referencias'] = [f"Veja também em nosso artigo: {base_url}/{expected_file}"]
                specific_count += 1
                status = "ESPECÍFICO"
            else:
                faq['referencias'] = [f"Veja também em nosso artigo: {base_url}/index.html"]
                fallback_count += 1
                status = "FALLBACK"
            
            print(f"{i:3d}. {faq_id} → {slug:40s} [{status}]")
        except Exception as e:
            print(f"ERRO em {faq_id}: {str(e)}")
            faq['referencias'] = [f"Veja também em nosso artigo: {base_url}/index.html"]
            fallback_count += 1

    print("\n" + "="*70)
    print(f"Salvando JSON...")
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print(f"JSON validado...")
    with open(json_path, 'r', encoding='utf-8') as f:
        json.load(f)

    print("\n" + "="*70)
    print("✓ SUCESSO!")
    print(f"\n  Total de FAQs: {total}")
    print(f"  Links específicos: {specific_count}")
    print(f"  Fallbacks (index.html): {fallback_count}")
    print("\n  JSON salvo em UTF-8 sem BOM")
    print("="*70)

except Exception as e:
    print(f"ERRO FATAL: {str(e)}", file=sys.stderr)
    sys.exit(1)
