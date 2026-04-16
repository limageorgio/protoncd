import requests
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
    url = f'https://www.protoncd.com.br/{p}'
    if p == 'conhecimento-tecnico/index.html': url = 'https://www.protoncd.com.br/conhecimento-tecnico/'
    r = requests.get(url)
    html = r.text
    m_match = re.search(r'<meta\s+name=[\""\']description[\""\']\s+content=[\""\'](.*?)[\""\']', html, re.I | re.S)
    m = m_match.group(1).strip() if m_match else 'NO DESC'
    if not m_match:
        m_match = re.search(r'<meta\s+content=[\""\'](.*?)[\""\']\s+name=[\""\']description[\""\']', html, re.I | re.S)
        m = m_match.group(1).strip() if m_match else 'NO DESC'
    print(f'{p}: len(desc)={len(m)}, desc={m[:30]}')
