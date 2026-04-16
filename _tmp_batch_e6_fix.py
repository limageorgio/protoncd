import os
import re

fixed = {
    'artigo-playground-base-piso-escoamento-agua.html': {
        'title': 'Piso de Playground sem Escoamento Rápido de Água',
        'description': 'Problemas de drenagem em pisos de playground criam poças que reduzem a absorção de impacto. Conheça as exigências da norma NBR 16071 para áreas seguras.'
    },
    'artigo-playground-buraco-fresta-8-25.html': {
        'title': 'Frestas e Buracos (8 a 25mm) em Playgrounds',
        'description': 'Riscos de aprisionamento de dedos em buracos e frestas de 8mm a 25mm. Saiba como realizar inspeções em brinquedos infantis de acordo com a NBR 16071.'
    },
    'artigo-playground-cama-de-areia-cascalho-300mm-de-profundidade.html': {
        'title': 'Cama de Areia Menor que 30cm no Playground',
        'description': 'A espessura de caixas de areia abaixo de 300mm não amortece quedas altas. Veja os cálculos, ensaios de impacto (HIC) e recomendações da NBR 16071.'
    },
    'artigo-playground-concreto-armadura-exposta.html': {
        'title': 'Armadura de Concreto Exposta em Playgrounds',
        'description': 'Alerta de segurança: estruturas com armaduras de concreto expostas em playgrounds causam acidentes severos. Avaliação técnica e laudo NBR 16071.'
    },
    'artigo-playground-cordas-rompimento-desgaste-excessivo.html': {
        'title': 'Cordas Desgastadas em Brinquedos: Avaliação',
        'description': 'Rompimento de cordas em redes de escalada reduz o limite de carga e causa acidentes estruturais. Regras de manutenção e inspeção pela ABNT NBR 16071.'
    },
    'artigo-playground-corrimao-ausente-altura-600-850.html': {
        'title': 'Corrimão Inadequado ou Ausente (600 a 850mm)',
        'description': 'Corrimãos ausentes em escadas ou rampas de brinquedos comprometem a segurança infantil. Diretrizes da NBR 16071 para altura (600-850mm) no playground.'
    },
    'artigo-playground-deformacoes-quebras-estruturais.html': {
        'title': 'Deformações Estruturais em Brinquedos',
        'description': 'Inspeção de trincas, quebras e deformações que comprometem a estabilidade de balanços e escorregadores (ABNT NBR 16071). Prevenção e laudo técnico.'
    },
    'artigo-playground-desgaste-do-gel-com-fibra-de-vidro-exposta.html': {
        'title': 'Fibra de Vidro Exposta em Escorregadores',
        'description': 'Desgaste do gel coat deixa a fibra de vidro exposta, causando coceiras e lacerações nas crianças. Restauração técnica de escorregadores e NBR 16071.'
    }
}

for filename, data in fixed.items():
    filepath = os.path.join('artigos', 'playgrounds', filename)
    if not os.path.exists(filepath): continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = re.sub(
        r'<title>.*?</title>',
        f'<title>{data["title"]}</title>',
        content,
        flags=re.IGNORECASE | re.DOTALL
    )
    
    new_content = re.sub(
        r'<meta name="description"[\s\S]*?content=".*?"\s*>',
        f'<meta name="description" content="{data["description"]}">',
        new_content,
        flags=re.IGNORECASE
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print(f"Updated {filename}")
