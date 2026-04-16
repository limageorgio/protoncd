import sys
import re
import html

files = [
    'artigos/playgrounds/artigo-playground-piso-queda.html',
    'artigos/playgrounds/artigo-playground-pisos-soltos-devem-ser-aerados-borrachas-devem-ter-laudo-hic.html',
    'artigos/playgrounds/artigo-playground-pisos-soltos-muito-compactados-borrachas-sem-laudo-hic.html',
    'artigos/playgrounds/artigo-playground-placa-visivel-com-fabricante-data-norma-e-faixa-etaria.html',
    'artigos/playgrounds/artigo-playground-plano-formal-de-manutencao-com-livros-de-registro.html',
    'artigos/playgrounds/artigo-playground-plastico-com-trincas-ou-quebras.html',
    'artigos/playgrounds/artigo-playground-plastico-esbranquicado-ressecado-perda-de-propriedade-estrutural.html',
    'artigos/playgrounds/artigo-playground-presenca-de-farpas-ou-lascas-na-superficie-da-madeira.html'
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