import re

fixes = {
    'conhecimento-tecnico/index.html': {
        'title': 'Base de Conhecimento Técnico | Proton Engenharia',
        'desc': 'Base de conhecimento técnico Proton Engenharia com FAQs e artigos sobre inspeção predial, elevadores, HVAC, playgrounds, gás e normas ABNT para condomínios.'
    },
    'artigos/elevadores/artigo-elevadores-slack-rope-cabo-frouxo.html': {
        'title': 'Slack Rope: Cabo Frouxo no Elevador | Proton Engenharia',
        'desc': 'Entenda o que é a falha de Slack Rope (cabo frouxo) no elevador, seus riscos de segurança e como uma inspeção técnica pode prevenir acidentes estruturais.'
    },
    'artigos/elevadores/artigo-elevadores-teste-funcional-freio-maquina-ausente.html': {
        'title': 'Teste Funcional de Freio no Elevador Ausente | Proton',
        'desc': 'Saiba os riscos da ausência do teste funcional de freio na máquina de tração do elevador e entenda a importância dessa avaliação na manutenção contínua.'
    },
    'artigos/playgrounds/artigo-playground-design-do-guarda-corpo-permite-escala-travessas-horizontais.html': {
        'title': 'Guarda-Corpo com Travessas Escaláveis em Playgrounds',
        'desc': 'Analise tecnica de guarda-corpo com travessas que permitem escala, com criterios ABNT NBR 16071 e plano de adequacao em playground.'
    },
    'artigos/playgrounds/artigo-playground-distanciamento-entre-equipamentos.html': {
        'title': 'Distanciamento Insuficiente Entre Equipamentos | Proton',
        'desc': 'Guia técnico sobre as normas de distanciamento entre equipamentos em playgrounds, focando na conformidade com a ABNT NBR 16071 para garantir a segurança livre.'
    },
    'artigos/playgrounds/artigo-playground-eixos-e-rolamentos-com-movimento-travado-ou-seco.html': {
        'title': 'Playground: Eixos e Rolamentos Travados | Proton Engenharia',
        'desc': 'Análise técnica da não conformidade relacionada a eixos e rolamentos com movimento travado ou seco em equipamentos de playgrounds e as correções essenciais.'
    },
    'artigos/playgrounds/artigo-playground-escorregador-com-calos-parafusos-expostos-ou-degraus.html': {
        'title': 'Atenção: Parafusos Expostos e Calos no Escorregador | Proton',
        'desc': 'Guia técnico sobre os riscos de parafusos expostos, calos ou degraus irregulares em escorregadores e a fiscalização rigorosa baseada nas normas da ABNT.'
    },
    'artigos/playgrounds/artigo-playground-falta-de-segunda-rota-de-evacuacao-em-brinquedao.html': {
        'title': 'Playground: Rota de Evacuação em Brinquedão | Proton',
        'desc': 'Guia técnico alertando para os perigos da ausência de uma segunda rota de evacuação em brinquedões de playground, exigência crucial da norma de segurança.'
    }
}

for path, data in fixes.items():
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Apply title
    html = re.sub(r'<title>.*?</title>', f"<title>{data['title']}</title>", html, flags=re.IGNORECASE | re.DOTALL)

    # Apply meta description
    if re.search(r'<meta\s+name=[\""\']description[\""\']\s+content=[\""\'].*?[\""\']', html, re.I | re.S):
        html = re.sub(
            r'(<meta\s+name=[\""\']description[\""\']\s+content=[\""\']).*?([\""\'])',
            rf'\1{data["desc"]}\2',
            html,
            flags=re.IGNORECASE | re.DOTALL
        )
    elif re.search(r'<meta\s+content=[\""\'].*?[\""\']\s+name=[\""\']description[\""\']', html, re.I | re.S):
        html = re.sub(
            r'(<meta\s+content=[\""\']).*?([\""\']\s+name=[\""\']description[\""\'])',
            rf'\1{data["desc"]}\2',
            html,
            flags=re.IGNORECASE | re.DOTALL
        )
    else:
        # Se não há tag description, cria uma (não deve ser o caso)
        pass

    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
        
    print(f"Updated {path}")
