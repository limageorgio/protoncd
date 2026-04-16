import sys
import re
import html

files = [
    'artigos/playgrounds/artigo-playground-presenca-de-sujeira-umidade-ou-falta-de-condicoes-de-uso-no-piso.html',
    'artigos/playgrounds/artigo-playground-protuberancias-afiadas-curvatura.html',
    'artigos/playgrounds/artigo-playground-rotas-acesso-livres-niveladas.html',
    'artigos/playgrounds/artigo-playground-rotas-acesso-obstruidas-irregulares.html',
    'artigos/playgrounds/artigo-playground-secao-de-entrada-deve-ter-barra-para-forcar-a-sentar.html',
    'artigos/playgrounds/artigo-playground-secao-de-saida-do-escorregador-curta-300-500mm.html',
    'artigos/playgrounds/artigo-playground-superficies-expostas-ao-sol-que-podem-causar-queimaduras.html',
    'artigos/playgrounds/artigo-playground-suportes-manuais-pegada-completa-fora-de-16-45-mm.html'
]

for fp in files:
    try:
        with open(fp, 'r', encoding='utf-8') as f:
            content = f.read()
            title_m = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
            title = html.unescape(title_m.group(1).strip() if title_m else 'None')
            desc_m = re.search(r'<meta[^>]+name=[\'"]description[\'"][^>]+content=[\'"]([^\'"]+)[\'"]|<meta[^>]+content=[\'"]([^\'"]+)[\'"][^>]+name=[\'"]description[\'"]', content, re.IGNORECASE)
            desc = html.unescape((desc_m.group(1) or desc_m.group(2)).strip()) if desc_m else 'None'
            print(f'FILE: {fp}')
            print(f'TITLE_LEN: {len(title)} | {title}')
            print(f'DESC_LEN:  {len(desc)} | {desc}')
            print('-'*40)
    except Exception as e:
        pass