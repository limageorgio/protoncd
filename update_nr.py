import re

file_path = 'goiania/treinamentos-nr-goiania.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Add detail to NR-11
content = content.replace(
'''<li>Parte prática com avaliação do operador</li>
                    </ul>''',
'''<li>Parte prática com avaliação do operador</li>
                    </ul>
                    <div style="margin-top: 1.5rem; padding-top: 1rem; border-top: 1px solid var(--border-color); font-size: 0.9rem;">
                        <p style="margin-bottom: 0.5rem;"><strong><i class="fas fa-users" style="color:var(--accent-blue);"></i> Público-alvo:</strong> Operadores de movimentação logística, almoxarifes e profissionais de armazéns, frigoríficos e centros de distribuição.</p>
                        <p><strong><i class="fas fa-history" style="color:var(--accent-blue);"></i> Periodicidade:</strong> Anual (sugerida para reciclagem) ou quando ocorrerem acidentes/mudança de equipamento.</p>
                    </div>'''
)

# And similarly for others, wait, the easiest way is to target the specific h3 inside the card and replace its text context or ul end.
# Let's write rules. I'll search for regex like `(<h3 class="card-title">NR-XX.*?</h3[^>]*>.*?</ul>)` and append the extra HTML.

updates = {
    'NR-11': {
        'publico': 'Operadores de movimentação logística, almoxarifes, trabalhadores de armazéns, frigoríficos e centros de distribuição.',
        'period': 'Anual (sugerida para reciclagem) ou quando ocorrerem acidentes e mudança de equipamento.',
        'color': 'blue'
    },
    'NR-12': {
        'publico': 'Operadores de máquinas e prensas industriais, equipe de manutenção mecânica e elétrica, e supervisores de produção.',
        'period': 'Na admissão e reciclagem quando houver mudança de função, adaptação do equipamento ou afastamento superior a 90 dias.',
        'color': 'red'
    },
    'NR-20': {
        'publico': 'Trabalhadores em postos de combustíveis, refinarias, indústrias químicas, do agronegócio e locais com armazenamento de líquidos inflamáveis.',
        'period': 'Anual, Bienal ou Trienal, dependendo da classe da instalação e do nível do treinamento (Integração, Básico, Intermediário, Avançado).',
        'color': 'yellow'
    },
    'NR-33': {
        'publico': 'Trabalhadores autorizados que adentram silos, tanques, galerias subterrâneas (Saneamento), poços de elevadores profundos, além de Vigias e Supervisores.',
        'period': 'Anual obrigatória (reciclagem com carga horária mínima de 8 horas).',
        'color': 'cyan'
    },
    'NR-35': {
        'publico': 'Profissionais de telecomunicações, construção civil, manutenção de fachadas, limpadores de vidro e eletricistas executando tarefas acima de 2 metros do nível inferior.',
        'period': 'Bienal (obrigatória a cada 2 anos) ou de imediato em caso de mudança de empresa, condição de trabalho ou novo procedimento.',
        'color': 'blue'
    },
    'NR-10': {
        'publico': 'Eletricistas, técnicos de manutenção predial/industrial, e todos os profissionais que interagem direta ou indiretamente com instalações elétricas.',
        'period': 'Bienal (obrigatória a cada 2 anos) ou quando houver retorno de afastamento (superior a três meses) e mudança de empresa.',
        'color': 'red'
    }
}

for nr, info in updates.items():
    pattern = re.compile(rf'(<h3 class="card-title">{nr}.*?</ul>)', re.DOTALL)
    match = pattern.search(content)
    if match:
        extra_html = f'''
                    <div style="margin-top: 1.5rem; padding-top: 1rem; border-top: 1px solid var(--border-color); font-size: 0.9rem;">
                        <p style="margin-bottom: 0.5rem; line-height: 1.4;"><strong><i class="fas fa-users" style="color:var(--accent-{info['color']}); margin-right:4px;"></i> Público-alvo:</strong> {info['publico']}</p>
                        <p style="line-height: 1.4;"><strong><i class="fas fa-history" style="color:var(--accent-{info['color']}); margin-right:4px;"></i> Periodicidade Mínima:</strong> {info['period']}</p>
                    </div>'''
        # ensure we don't duplicate
        if "Público-alvo:" not in match.group(1) and f"<!-- {nr} INFO -->" not in content:
            new_block = match.group(1) + f"\n                    <!-- {nr} INFO -->" + extra_html
            content = content.replace(match.group(1), new_block)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated NRs in treinamentos-nr-goiania.html")
