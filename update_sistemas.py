import re

file_path = 'inspecao-sistemas-mecanicos.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

pacotes_html = """
    <!-- ========== PACOTES ========== -->
    <section class="section bg-light" id="pacotes">
        <div class="container">
            <div class="section-header reveal">
                <span class="badge badge-blue">Escopo Integrado</span>
                <h2>Pacotes de <span class="text-gradient">Inspeção</span></h2>
                <div class="section-divider"></div>
                <p>Combinações estratégicas para laudos completos com melhor custo-benefício.</p>
            </div>
            
            <div class="table-responsive reveal" style="overflow-x: auto; margin-bottom: var(--space-6);">
                <table style="width: 100%; border-collapse: collapse; text-align: left; background: var(--bg-card); border-radius: var(--radius-lg); overflow: hidden; box-shadow: var(--shadow-md);">
                    <thead style="background: var(--primary-color); color: white;">
                        <tr>
                            <th style="padding: 1rem; border-bottom: 2px solid var(--accent-blue);">Sistemas Inclusos</th>
                            <th style="padding: 1rem; border-bottom: 2px solid var(--accent-blue);">Standard</th>
                            <th style="padding: 1rem; border-bottom: 2px solid var(--accent-blue);">Extended</th>
                            <th style="padding: 1rem; border-bottom: 2px solid var(--accent-blue);">Advanced</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr style="border-bottom: 1px solid var(--border-color);">
                            <td style="padding: 1rem;">Elevadores (Ensaios 360°)</td>
                            <td style="padding: 1rem; color: var(--accent-blue);"><i class="fas fa-check"></i></td>
                            <td style="padding: 1rem; color: var(--accent-blue);"><i class="fas fa-check"></i></td>
                            <td style="padding: 1rem; color: var(--accent-blue);"><i class="fas fa-check"></i></td>
                        </tr>
                        <tr style="border-bottom: 1px solid var(--border-color);">
                            <td style="padding: 1rem;">Bombas e Incêndio</td>
                            <td style="padding: 1rem; color: var(--accent-blue);"><i class="fas fa-check"></i></td>
                            <td style="padding: 1rem; color: var(--accent-blue);"><i class="fas fa-check"></i></td>
                            <td style="padding: 1rem; color: var(--accent-blue);"><i class="fas fa-check"></i></td>
                        </tr>
                        <tr style="border-bottom: 1px solid var(--border-color);">
                            <td style="padding: 1rem;">Gás Predial (GLP/GN)</td>
                            <td style="padding: 1rem; color: var(--text-light);"><i class="fas fa-minus"></i></td>
                            <td style="padding: 1rem; color: var(--accent-blue);"><i class="fas fa-check"></i></td>
                            <td style="padding: 1rem; color: var(--accent-blue);"><i class="fas fa-check"></i></td>
                        </tr>
                        <tr style="border-bottom: 1px solid var(--border-color);">
                            <td style="padding: 1rem;">HVAC e PMOC</td>
                            <td style="padding: 1rem; color: var(--text-light);"><i class="fas fa-minus"></i></td>
                            <td style="padding: 1rem; color: var(--text-light);"><i class="fas fa-minus"></i></td>
                            <td style="padding: 1rem; color: var(--accent-blue);"><i class="fas fa-check"></i></td>
                        </tr>
                        <tr style="border-bottom: 1px solid var(--border-color);">
                            <td style="padding: 1rem;">Pressurização de Escadas</td>
                            <td style="padding: 1rem; color: var(--text-light);"><i class="fas fa-minus"></i></td>
                            <td style="padding: 1rem; color: var(--text-light);"><i class="fas fa-minus"></i></td>
                            <td style="padding: 1rem; color: var(--accent-blue);"><i class="fas fa-check"></i></td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </section>
"""

# Insert before Parcerias
if 'id="pacotes"' not in content:
    content = re.sub(r'(<!-- ========== PARCERIAS ========== -->)', pacotes_html + r'\n    \1', content)

# I should also add Deep links. E.g. href="analise-vibracao-elevadores.html" to Elevadores.
content = content.replace('<h3>Análise de Vibração 360° em Elevadores</h3>', '<h3><a href="analise-vibracao-elevadores.html" style="color:inherit; text-decoration:underline;">Análise de Vibração 360° em Elevadores</a></h3>')
content = content.replace('<h3>Sistemas de Climatização (HVAC) / PMOC</h3>', '<h3><a href="inspecao-hvac-pmoc.html" style="color:inherit; text-decoration:underline;">Sistemas de Climatização (HVAC) / PMOC</a></h3>')
content = content.replace('<h3>Sistemas de Combate a Incêndio</h3>', '<h3><a href="inspecao-combate-incendio.html" style="color:inherit; text-decoration:underline;">Sistemas de Combate a Incêndio</a></h3>')


with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated inspecao-sistemas-mecanicos.html")
