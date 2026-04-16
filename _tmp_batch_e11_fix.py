import re
import os

fixes = {
    "artigos/playgrounds/artigo-playground-presenca-de-sujeira-umidade-ou-falta-de-condicoes-de-uso-no-piso.html": {
        "title": "Playgrounds: Pisos com Sujeira ou Umidade",
        "desc": "Conheça os perigos de pisos em playgrounds com sujeira, umidade e poças d'água. Saiba como a manutenção previne escorregões e garante proteção."
    },
    "artigos/playgrounds/artigo-playground-protuberancias-afiadas-curvatura.html": {
        "title": "Protuberâncias e Curvaturas Afiadas em Brinquedos",
        "desc": "Entenda os riscos de parafusos expostos, pontas e curvaturas afiadas com menos de 3mm em playgrounds. Guia prático de adequação à norma NBR 16071."
    },
    "artigos/playgrounds/artigo-playground-rotas-acesso-livres-niveladas.html": {
        "title": "Acesso a Playgrounds: Rotas Livres e Niveladas",
        "desc": "Veja as regras de acessibilidade e mobilidade. Descubra a importância técnica das rotas de acesso sem desníveis ou obstáculos nas áreas de lazer."
    },
    "artigos/playgrounds/artigo-playground-rotas-acesso-obstruidas-irregulares.html": {
        "title": "Playgrounds: Rotas de Acesso Obstruídas e Riscos",
        "desc": "Crianças sofrem acidentes graves em rotas de acesso obstruídas. Entenda o diagnóstico técnico sobre desníveis e degraus inadequados em parquinhos."
    },
    "artigos/playgrounds/artigo-playground-secao-de-entrada-deve-ter-barra-para-forcar-a-sentar.html": {
        "title": "Escorregadores: Barra para Forçar Sentar | Proton",
        "desc": "Por que todo escorregador precisa de uma barra superior na seção de entrada? Proteja as crianças forçando a postura sentada conforme manda a norma técnica."
    },
    "artigos/playgrounds/artigo-playground-secao-de-saida-do-escorregador-curta-300-500mm.html": {
        "title": "Escorregadores: Seção de Saída Curta (300-500mm)",
        "desc": "Diagnóstico de escorregadores com saídas curtas fora da regra de 300mm a 500mm. Saiba avaliar a falha que aumenta lesões por impacto na área de queda."
    },
    "artigos/playgrounds/artigo-playground-superficies-expostas-ao-sol-que-podem-causar-queimaduras.html": {
        "title": "Playgrounds: Queimaduras por Superfícies Expostas",
        "desc": "O sol superaquece metais e plásticos nos playgrounds gerando queimaduras infantis sérias. Descubra as recomendações sobre sombreamento e segurança."
    },
    "artigos/playgrounds/artigo-playground-suportes-manuais-pegada-completa-fora-de-16-45-mm.html": {
        "title": "Suportes e Corrimãos de Playgrounds: 16 a 45 mm",
        "desc": "Guia técnico para dimensionar suportes manuais de pegada completa em parquinhos. Entenda a regra de 16mm a 45mm que impede quedas durante escaladas."
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
