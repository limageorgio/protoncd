import re
paths = [
    'artigos/elevadores/artigo-elevadores-chicotes-cabos-controle-protecao-inspecao.html',
    'artigos/playgrounds/artigo-playground-circulacao-livre-1-50m-no-entorno.html',
    'artigos/playgrounds/artigo-playground-falta-de-sinalizacao-de-seguranca-regras.html',
    'artigos/playgrounds/artigo-playground-ferrugem-desgaste.html',
    'artigos/playgrounds/artigo-playground-h-600-mm-exige-barreira-fechada-min-900-mm-para-3-anos.html',
    'artigos/playgrounds/artigo-playground-inclinacao-escorregador-acima-60.html',
    'artigos/playgrounds/artigo-playground-inclinacao-maxima-da-gangorra-acima-de-25.html',
    'artigos/playgrounds/artigo-playground-incompatibilidade-piso-aql.html'
]
for p in paths:
    with open(p, 'r', encoding='utf-8') as f:
        html = f.read()
    t = re.search(r'<title>(.*?)</title>', html, re.I | re.S).group(1).strip()
    d = re.search(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']', html, re.I | re.S)
    if not d:
        d = re.search(r'<meta\s+content=["\'](.*?)["\']\s+name=["\']description["\']', html, re.I | re.S)
    desc = d.group(1).strip() if d else ''
    print('FILE:', p)
    print('TITLE', len(t), t)
    print('DESC', len(desc), desc)
