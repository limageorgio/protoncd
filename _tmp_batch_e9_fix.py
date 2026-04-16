import re
import os

fixes = {
    "artigos/playgrounds/artigo-playground-laterais-do-deslize-entre-100-e-500mm.html": {
        "title": "Laterais do Deslize 100mm a 500mm em Playgrounds",
        "desc": "Descubra as regras para laterais do deslize entre 100 e 500mm em escorregadores conforme a NBR 16071. Garanta a segurança infantil no playground."
    },
    "artigos/playgrounds/artigo-playground-madeira-apodrecida-ou-rachaduras-8mm.html": {
        "title": "Playground: Madeira Apodrecida ou Rachaduras (>8mm)",
        "desc": "Riscos de madeira apodrecida e rachaduras maiores de 8mm em playgrounds. Entenda as inspeções normativas da NBR 16071 para garantir segurança."
    },
    "artigos/playgrounds/artigo-playground-malha-de-aco-solta-assentos-pneus-cabos.html": {
        "title": "Playground: Malha de Aço em Assentos e Cabos",
        "desc": "Assentos de pneus e cabos com malha de aço solta expõem crianças a riscos de corte. Saiba identificar as falhas e como fazer manutenção no playground."
    },
    "artigos/playgrounds/artigo-playground-mecanismos-emperrados-ou-desprotegidos.html": {
        "title": "Mecanismos Emperrados e Desprotegidos em Playgrounds",
        "desc": "Proteja as crianças de esmagamentos devido a mecanismos desprotegidos ou áreas emperradas. Veja dicas de inspeção técnica baseada na NBR 16071."
    },
    "artigos/playgrounds/artigo-playground-molas-sem-limitadores.html": {
        "title": "Molas sem Limitadores de Contato com Solo | Proton",
        "desc": "Guia técnico de molas sem limitadores em brinquedos de balanço. Foco na regra de 12 mm entre espiras e controle de esmagamento conforme NBR 16071-2."
    },
    "artigos/playgrounds/artigo-playground-outras-irregularidades-relevantes-de-ambiente.html": {
        "title": "Playgrounds: Irregularidades Relevantes de Ambiente",
        "desc": "Conheça os perigos estruturais e ambientais nas áreas de lazer infantil, incluindo nivelamento de piso e instalações elétricas, essenciais na perícia."
    },
    "artigos/playgrounds/artigo-playground-outras-irregularidades-relevantes-do-equipamento.html": {
        "title": "Playgrounds: Riscos e Irregularidades de Equipamentos",
        "desc": "Entenda as irregularidades mecânicas focadas em componentes de parquinhos. Identifique desgastes severos, falhas de solda e manutenções críticas de uso."
    },
    "artigos/playgrounds/artigo-playground-parafusos-porcas-sobressaindo-mais-de-8mm.html": {
        "title": "Playgrounds: Parafusos Sobressaindo Mais de 8mm",
        "desc": "Riscos de parafusos e porcas saltando mais de 8mm em brinquedos. Proteja crianças verificando as quinas vivas e desgastes estruturais nos equipamentos."
    }
}

for fp, tags in fixes.items():
    if not os.path.exists(fp):
        print(f"File not found: {fp}")
        continue
    with open(fp, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Substituir title
    # re_title captura o conteúdo exato
    content = re.sub(r'(?i)(<title>)(.*?)(</title>)', r'\g<1>' + tags["title"] + r'\g<3>', content)
    
    # Substituir description
    # Achar e substituir a meta tag de description inteira para padronizar
    meta_desc_pattern = re.compile(r'<meta[^>]+name="description"[^>]+content="([^"]*)"|<meta[^>]+content="([^"]*)"[^>]+name="description"', re.IGNORECASE)
    
    def repl_desc(match):
        return f'<meta name="description" content="{tags["desc"]}">'
        
    content = meta_desc_pattern.sub(repl_desc, content)
    
    with open(fp, "w", encoding="utf-8") as f:
        f.write(content)
        print(f"Updated {fp}\nTitle: {tags['title']}\nDesc: {tags['desc']}\n")
