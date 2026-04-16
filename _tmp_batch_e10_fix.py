import re
import os

fixes = {
    "artigos/playgrounds/artigo-playground-piso-queda.html": {
        "title": "Piso de Playground e AQL: Diagnóstico de Queda",
        "desc": "Entenda a compatibilidade entre pisos de playground e a Altura de Queda Livre (AQL). Veja os riscos, normas da ABNT NBR 16071 e como prevenir lesões."
    },
    "artigos/playgrounds/artigo-playground-pisos-soltos-devem-ser-aerados-borrachas-devem-ter-laudo-hic.html": {
        "title": "Pisos Soltos e de Borracha: Aerados e Laudo HIC",
        "desc": "Conheça a exigência do laudo HIC para pisos de borracha e a aeração de pisos soltos em playgrounds, fundamentais para absorção de impacto normatizada."
    },
    "artigos/playgrounds/artigo-playground-pisos-soltos-muito-compactados-borrachas-sem-laudo-hic.html": {
        "title": "Piso Compactado e Borrachas sem Laudo HIC",
        "desc": "Saiba por que pisos de playground soltos muito compactados e borrachas sem laudo HIC reprovam nas inspeções e não absorvem quedas adequadamente."
    },
    "artigos/playgrounds/artigo-playground-placa-visivel-com-fabricante-data-norma-e-faixa-etaria.html": {
        "title": "Playground Sem Placa de Fabricante e Faixa Etária",
        "desc": "Veja as regras de rastreabilidade para brinquedos. A falta de placas com dados do fabricante e limite de idade configura grave risco operacional normativo."
    },
    "artigos/playgrounds/artigo-playground-plano-formal-de-manutencao-com-livros-de-registro.html": {
        "title": "Playgrounds: Plano de Manutenção e Registros",
        "desc": "Entenda por que a ausência de plano formal de manutenção e livros de registro aumenta responsabilidades civis e como se adequar às normas brasileiras."
    },
    "artigos/playgrounds/artigo-playground-plastico-com-trincas-ou-quebras.html": {
        "title": "Playgrounds: Plásticos com Trincas e Quebras",
        "desc": "Identifique danos estruturais graves em componentes plásticos de playgrounds. Trincas e quebras comprometem a segurança e causam cortes nas crianças."
    },
    "artigos/playgrounds/artigo-playground-plastico-esbranquicado-ressecado-perda-de-propriedade-estrutural.html": {
        "title": "Plásico de Brinquedos: Ressecado e Esbranquiçado",
        "desc": "Entenda como a degradação UV resseca e esbranquiça o plástico em playgrounds, enfraquecendo a estrutura e exigindo manutenção ou substituição urgente."
    },
    "artigos/playgrounds/artigo-playground-presenca-de-farpas-ou-lascas-na-superficie-da-madeira.html": {
        "title": "Farpas e Lascas em Madeira de Playgrounds",
        "desc": "Aprenda a inspecionar brinquedos de madeira para evitar farpas e lascas que causam perfurações infantis. Guia completo para laudos de segurança."
    }
}

for fp, tags in fixes.items():
    if not os.path.exists(fp):
        print(f"File not found: {fp}")
        continue
    with open(fp, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Substituir title
    content = re.sub(r'(?i)(<title>)(.*?)(</title>)', r'\g<1>' + tags["title"] + r'\g<3>', content)
    
    # Substituir description
    meta_desc_pattern = re.compile(r'<meta[^>]+name="description"[^>]+content="([^"]*)"|<meta[^>]+content="([^"]*)"[^>]+name="description"', re.IGNORECASE)
    def repl_desc(match):
        return f'<meta name="description" content="{tags["desc"]}">'
        
    content = meta_desc_pattern.sub(repl_desc, content)
    
    with open(fp, "w", encoding="utf-8") as f:
        f.write(content)
        print(f"Updated {fp}\nTitle: {tags['title']} ({len(tags['title'])})\nDesc: {tags['desc']} ({len(tags['desc'])})\n")
