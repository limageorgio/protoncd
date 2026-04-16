import sys
import re
import html

files = [
    'artigos/playgrounds/artigo-playground-laterais-do-deslize-entre-100-e-500mm.html',
    'artigos/playgrounds/artigo-playground-madeira-apodrecida-ou-rachaduras-8mm.html',
    'artigos/playgrounds/artigo-playground-malha-de-aco-solta-assentos-pneus-cabos.html',
    'artigos/playgrounds/artigo-playground-mecanismos-emperrados-ou-desprotegidos.html',
    'artigos/playgrounds/artigo-playground-molas-sem-limitadores.html',
    'artigos/playgrounds/artigo-playground-outras-irregularidades-relevantes-de-ambiente.html',
    'artigos/playgrounds/artigo-playground-outras-irregularidades-relevantes-do-equipamento.html',
    'artigos/playgrounds/artigo-playground-parafusos-porcas-sobressaindo-mais-de-8mm.html'
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
