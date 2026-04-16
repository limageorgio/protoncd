import re
paths = [
    'conhecimento-tecnico/index.html',
    'artigos/elevadores/artigo-elevadores-slack-rope-cabo-frouxo.html',
    'artigos/elevadores/artigo-elevadores-teste-funcional-freio-maquina-ausente.html',
    'artigos/playgrounds/artigo-playground-design-do-guarda-corpo-permite-escala-travessas-horizontais.html',
    'artigos/playgrounds/artigo-playground-distanciamento-entre-equipamentos.html',
    'artigos/playgrounds/artigo-playground-eixos-e-rolamentos-com-movimento-travado-ou-seco.html',
    'artigos/playgrounds/artigo-playground-escorregador-com-calos-parafusos-expostos-ou-degraus.html',
    'artigos/playgrounds/artigo-playground-falta-de-segunda-rota-de-evacuacao-em-brinquedao.html'
]

for p in paths:
    with open(p, 'r', encoding='utf-8') as f:
        html = f.read()
    t = re.search(r'<title>(.*?)</title>', html, re.I | re.S).group(1).strip()
    m_match = re.search(r'<meta\s+name=[\""\']description[\""\']\s+content=[\""\'](.*?)[\""\']', html, re.I | re.S)
    m = m_match.group(1).strip() if m_match else 'NO DESC'
    if not m_match:
        m_match = re.search(r'content=[\""\'](.*?)[\""\']\s+name=[\""\']description[\""\']', html, re.I | re.S)
        m = m_match.group(1).strip() if m_match else 'NO DESC'
        
    print(f'File: {p}')
    print(f'  T ({len(t)}): {t}')
    print(f'  D ({len(m)}): {m}')
