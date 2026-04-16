import re
fixes = {
    'artigos/elevadores/artigo-elevadores-chicotes-cabos-controle-protecao-inspecao.html': {
        'title': 'Chicotes de Controle no Poço: Proteção e Inspeção | Proton',
        'desc': 'Os chicotes e cabos de controle no poço do elevador merecem atenção redobrada. Descubra os padrões de proteção e como inspecioná-los para evitar curtos.'
    },
    'artigos/playgrounds/artigo-playground-circulacao-livre-1-50m-no-entorno.html': {
        'title': 'Playground: Circulação livre de 1,50m no entorno | Proton',
        'desc': 'Guia técnico detalhado sobre por que os playgrounds exigem no mínimo 1,50m de circulação livre no entorno para evitar acidentes e choques entre crianças.'
    },
    'artigos/playgrounds/artigo-playground-falta-de-sinalizacao-de-seguranca-regras.html': {
        'title': 'Playground: Falta de Sinalização e Regras | Proton',
        'desc': 'A falta de sinalização de segurança ou regras nos playgrounds expõe condomínios a riscos legais. Entenda o que deve constar na placa obrigatória.'
    },
    'artigos/playgrounds/artigo-playground-ferrugem-desgaste.html': {
        'title': 'Ferrugem em Brinquedos: Prevenção e Diagnóstico Técnico',
        'desc': 'Brinquedos com ferrugem e desgaste: entenda o risco real para crianças e o protocolo técnico de inspeção de corrosão e integridade estrutural.'
    },
    'artigos/playgrounds/artigo-playground-h-600-mm-exige-barreira-fechada-min-900-mm-para-3-anos.html': {
        'title': 'Playground: Barreira Fechada em H >= 600mm | Proton',
        'desc': 'Análise técnica da norma: plataformas de altura 600mm exigem barreira fechada mínima de 900mm em brinquedos para crianças menores de 3 anos de idade.'
    },
    'artigos/playgrounds/artigo-playground-inclinacao-escorregador-acima-60.html': {
        'title': 'Inclinação do Escorregador Acima de 60 Graus | Proton Engenharia',
        'desc': 'Guia técnico alertando sobre os perigos mortais da inclinação de escorregadores acima de 60 graus. Veja os limites de graus aceitos pela ABNT NBR 16071.'
    },
    'artigos/playgrounds/artigo-playground-inclinacao-maxima-da-gangorra-acima-de-25.html': {
        'title': 'Playground: Inclinação Máxima da Gangorra | Proton',
        'desc': 'Guia técnico completo sobre a inclinação máxima da gangorra. Entenda porque ultrapassar ângulos de 25 graus cria risco extremo de compressão e queda livre.'
    },
    'artigos/playgrounds/artigo-playground-incompatibilidade-piso-aql.html': {
        'title': 'Incompatibilidade Piso x Altura de Queda: Diagnóstico AQL',
        'desc': 'Entenda o risco da incompatibilidade do piso de amortecimento com a AQL (Altura de Queda Livre). Grama ou areia nem sempre são suficientes para quedas altas.'
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

    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
        
    print(f"Updated {path}")
