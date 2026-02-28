import re

file_path = 'laudo-pericial-engenharia.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

faq_html = """
    <!-- FAQ Section -->
    <section class="section bg-light" id="faq">
        <div class="container">
            <h2 class="section-title">Perguntas Frequentes (FAQ) - Perícia de Engenharia</h2>
            <div class="accordion">
                <div class="accordion-item" style="margin-bottom: 1rem; border: 1px solid var(--border-color); padding: 1rem; border-radius: var(--radius-md);">
                    <h3 style="font-size: 1.1rem; margin-bottom: 0.5rem; color: var(--primary-color);">Quais são os prazos processuais para apresentação de quesitos e assistente técnico?</h3>
                    <p>De acordo com o Art. 465 do Novo Código de Processo Civil (CPC/2015), as partes têm o prazo de 15 (quinze) dias, contados da intimação do despacho de nomeação do perito, para arguir impedimento ou suspeição, indicar assistente técnico e apresentar quesitos.</p>
                </div>
                <div class="accordion-item" style="margin-bottom: 1rem; border: 1px solid var(--border-color); padding: 1rem; border-radius: var(--radius-md);">
                    <h3 style="font-size: 1.1rem; margin-bottom: 0.5rem; color: var(--primary-color);">Como são calculados os honorários periciais?</h3>
                    <p>Os honorários são calculados com base nas horas técnicas estimadas para a execução do trabalho, complexidade da matéria, necessidade de equipamentos especiais (como acelerômetros para análise de vibração) e despesas de deslocamento, em conformidade com as diretrizes do IBAPE e tabelas de referência regionais do CREA.</p>
                </div>
                <div class="accordion-item" style="border: 1px solid var(--border-color); padding: 1rem; border-radius: var(--radius-md);">
                    <h3 style="font-size: 1.1rem; margin-bottom: 0.5rem; color: var(--primary-color);">A Proton Engenharia atua em outros estados além de Goiás?</h3>
                    <p>Sim, atuamos nacionalmente. Apesar de termos base em Goiânia e Brasília, realizamos perícias em sistemas mecânicos complexos em todas as capitais do Brasil, especialmente casos envolvendo elevadores, escadas rolantes e sistemas de climatização (HVAC) de grande porte.</p>
                </div>
            </div>
        </div>
    </section>
    
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "FAQPage",
      "mainEntity": [{
        "@type": "Question",
        "name": "Quais são os prazos processuais para apresentação de quesitos e assistente técnico?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "De acordo com o Art. 465 do Novo Código de Processo Civil (CPC/2015), as partes têm o prazo de 15 (quinze) dias, contados da intimação do despacho de nomeação do perito, para arguir impedimento ou suspeição, indicar assistente técnico e apresentar quesitos."
        }
      }, {
        "@type": "Question",
        "name": "Como são calculados os honorários periciais?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Os honorários são calculados com base nas horas técnicas estimadas para a execução do trabalho, complexidade da matéria, necessidade de equipamentos especiais (como acelerômetros para análise de vibração) e despesas de deslocamento, em conformidade com as diretrizes do IBAPE e tabelas de referência regionais do CREA."
        }
      }, {
        "@type": "Question",
        "name": "A Proton Engenharia atua em outros estados além de Goiás?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Sim, atuamos nacionalmente. Apesar de termos base em Goiânia e Brasília, realizamos perícias em sistemas mecânicos complexos em todas as capitais do Brasil, especialmente casos envolvendo elevadores, escadas rolantes e sistemas de climatização (HVAC) de grande porte."
        }
      }]
    }
    </script>

"""

if 'id="faq"' not in content:
    content = content.replace('<footer class="footer">', faq_html + '<footer class="footer">')
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("FAQ and Schema added successfully.")
else:
    print("FAQ already exists.")
