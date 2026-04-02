#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import unicodedata

def remove_accents(text):
    text = unicodedata.normalize('NFKD', text)
    return ''.join([c for c in text if not unicodedata.combining(c)])

def convert_to_slug(text):
    text = remove_accents(text).lower()
    text = re.sub(r"['\"()_-]", " ", text)
    text = re.sub(r"\s+essa\s+situacao\s+de\s+", " ", text)
    text = re.sub(r"\s+brinquedo\s+com\s+", " ", text)
    text = re.sub(r"\s+quando\s+ha\s+", " ", text)
    text = re.sub(r"[^a-z0-9\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    text = text.replace(" ", "-")
    text = re.sub(r"-+", "-", text)
    return text.strip("-")

# Testes com perguntas reais
perguntas = [
    "'Agarras Frouxas' no playground é só detalhe ou é um problema de segurança que precisa corrigir?",
    "'Abertura Piso Correr Larga' pode prender dedo, cabeça ou roupa da criança?",
    "Brinquedo com 'Falta de revestimento ou presença de ferrugem' pode machucar as crianças?",
]

print("Testando slugs gerados:\n")
for pergunta in perguntas:
    slug = convert_to_slug(pergunta)
    print(f"Pergunta: {pergunta}")
    print(f"Slug: {slug}")
    print(f"Arquivo esperado: artigo-playground-{slug}.html")
    print()
