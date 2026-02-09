# -*- coding: utf-8 -*-
"""
Corrigir dados do Schema.org nas páginas das cidades
"""
import re

cidadesFiles = {
    "h:\\apps\\protoncd\\rio-de-janeiro\\analise-vibracao-elevadores-rj.html": {
        "nome": "Rio de Janeiro",
        "sigla": "RJ",
        "lat": "-22.9068",
        "lng": "-43.1729",
        "areaServed": '["Rio de Janeiro", "Niterói", "São Gonçalo", "Duque de Caxias"]'
    },
    "h:\\apps\\protoncd\\belo-horizonte\\analise-vibracao-elevadores-bh.html": {
        "nome": "Belo Horizonte",
        "sigla": "MG",
        "lat": "-19.9167",
        "lng": "-43.9345",
        "areaServed": '["Belo Horizonte", "Contagem", "Betim", "Nova Lima"]'
    },
    "h:\\apps\\protoncd\\curitiba\\analise-vibracao-elevadores-curitiba.html": {
        "nome": "Curitiba",
        "sigla": "PR",
        "lat": "-25.4284",
        "lng": "-49.2733",
        "areaServed": '["Curitiba", "São José dos Pinhais", "Pinhais", "Colombo"]'
    },
    "h:\\apps\\protoncd\\porto-alegre\\analise-vibracao-elevadores-poa.html": {
        "nome": "Porto Alegre",
        "sigla": "RS",
        "lat": "-30.0346",
        "lng": "-51.2177",
        "areaServed": '["Porto Alegre", "Canoas", "Novo Hamburgo", "São Leopoldo"]'
    }
}

for arquivo, dados in cidadesFiles.items():
    print(f"📝 Corrigindo: {dados['nome']}...")
    
    try:
        with open(arquivo, 'r', encoding='utf-8') as f:
            conteudo = f.read()
        
        # Substituições no Schema.org
        conteudo = re.sub(
            r'"addressLocality": "Goiânia"',
            f'"addressLocality": "{dados["nome"]}"',
            conteudo
        )
        conteudo = re.sub(
            r'"addressRegion": "GO"',
            f'"addressRegion": "{dados["sigla"]}"',
            conteudo
        )
        conteudo = re.sub(
            r'"latitude": "-16\.686882"',
            f'"latitude": "{dados["lat"]}"',
            conteudo
        )
        conteudo = re.sub(
            r'"longitude": "-49\.264357"',
            f'"longitude": "{dados["lng"]}"',
            conteudo
        )
        conteudo = re.sub(
            r'"areaServed": \[\s*"Goiânia",\s*"Anápolis",\s*"Brasília",\s*"Rio Verde"\s*\]',
            f'"areaServed": {dados["areaServed"]}',
            conteudo
        )
        
        # Salva
        with open(arquivo, 'w', encoding='utf-8') as f:
            f.write(conteudo)
        
        print(f"   ✅ Corrigido!")
        
    except Exception as e:
        print(f"   ❌ Erro: {e}")

print("\n🎉 Correções concluídas!")
