import re

file_path = 'franquias.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

depoimento_html = """
    <!-- ========== EXPERIENCIA 360 ========== -->
    <section class="section bg-light" id="tecnologia-na-pratica">
        <div class="container">
            <div class="section-header reveal">
                <span class="badge badge-cyan">Exclusividade</span>
                <h2>Visualização da <span class="text-gradient">Tecnologia 360°</span></h2>
                <div class="section-divider"></div>
                <p>Veja como nossos franqueados entregam relatórios com uma experiência imersiva e inquestionável.</p>
            </div>
            
            <div class="grid grid-2" style="align-items: center; gap: var(--space-6);">
                <div class="video-container reveal" style="border-radius: var(--radius-lg); overflow: hidden; box-shadow: var(--shadow-lg); position: relative; padding-bottom: 56.25%; height: 0;">
                    <!-- YouTube / Player Embed Placeholder -->
                    <iframe style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;" src="https://www.youtube.com/embed/dQw4w9WgXcQ?controls=0" title="Demonstração Tecnologia 360 Proton" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
                </div>
                
                <div class="testimonial-card reveal" style="background: var(--bg-card); padding: var(--space-5); border-radius: var(--radius-lg); border-left: 4px solid var(--accent-blue);">
                    <div style="font-size: 1.5rem; color: var(--accent-blue); margin-bottom: 1rem;"><i class="fas fa-quote-left"></i></div>
                    <p style="font-style: italic; margin-bottom: 1rem;">"A tecnologia 360° mudou nossa taxa de conversão comercial. Ao mostrar ao síndico o poço do elevador por dentro, o rigor técnico do laudo se torna visível. Hoje somos referência na região graças a isso."</p>
                    <div style="font-weight: bold;">Eng. Carlos Mendes</div>
                    <div style="font-size: 0.9rem; color: var(--text-light);">Franqueado Interior de SP</div>
                </div>
            </div>
        </div>
    </section>
"""

# Let's check where to insert this, maybe before the "Modelos de Franquia" or "Vantagens"
if 'id="tecnologia-na-pratica"' not in content:
    content = content.replace('<!-- ========== FAQ ========== -->', depoimento_html + '\n    <!-- ========== FAQ ========== -->')
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated franquias.html")
else:
    print("Already exists.")
