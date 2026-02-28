import json
import re

file_path = 'laudo-pericial-engenharia.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Update Schema
# Find the line with FAQPage
schema_match = re.search(r'\{"@context":"https://schema\.org","@type":"FAQPage","mainEntity":\[.*?\]\}', content)

if schema_match:
    schema_str = schema_match.group(0)
    schema_json = json.loads(schema_str)
    
    # Check if the new questions are already there
    has_prazos = any('prazos' in q['name'].lower() for q in schema_json['mainEntity'])
    
    if not has_prazos:
        schema_json['mainEntity'].extend([
            {
                "@type": "Question",
                "name": "Quais são os prazos processuais para apresentação de quesitos e assistente técnico?",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": "De acordo com o Art. 465 do Novo Código de Processo Civil (CPC/2015), as partes têm o prazo de 15 (quinze) dias, contados da intimação do despacho de nomeação do perito, para arguir impedimento ou suspeição, indicar assistente técnico e apresentar quesitos."
                }
            },
            {
                "@type": "Question",
                "name": "Como são calculados os honorários periciais em engenharia?",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": "Os honorários são calculados com base nas horas técnicas estimadas para a execução do trabalho, complexidade da matéria (ex: análise de vibração em equipamentos), nível de risco e despesas de deslocamento, seguindo as diretrizes do IBAPE e tabelas de referência dos regionais do CREA."
                }
            }
        ])
        
        new_schema_str = json.dumps(schema_json, separators=(',', ':'))
        content = content.replace(schema_str, new_schema_str)

# Add to HTML
html_to_add = """                <div class="faq-item reveal">
                    <div class="faq-question" onclick="toggleFaq(this)">
                        <h3>Quais são os prazos processuais para quesitos?</h3><span class="faq-toggle"><i
                                class="fas fa-plus"></i></span>
                    </div>
                    <div class="faq-answer">
                        <div class="faq-answer-inner">
                            <p>De acordo com o Art. 465 do Novo Código de Processo Civil (CPC/2015), as partes têm o prazo de 15 (quinze) dias, contados da intimação do despacho de nomeação do perito, para arguir impedimento ou suspeição, indicar assistente técnico e apresentar quesitos.</p>
                        </div>
                    </div>
                </div>
                <div class="faq-item reveal">
                    <div class="faq-question" onclick="toggleFaq(this)">
                        <h3>Como são calculados os honorários periciais?</h3><span class="faq-toggle"><i
                                class="fas fa-plus"></i></span>
                    </div>
                    <div class="faq-answer">
                        <div class="faq-answer-inner">
                            <p>Os honorários são calculados com base nas horas técnicas estimadas, complexidade da matéria, necessidade de instrumentos específicos e deslocamento, em conformidade com as diretrizes do IBAPE e CREA.</p>
                        </div>
                    </div>
                </div>
"""

content = content.replace('<!-- FAQ -->', '<!-- FAQ -->\n' + '    <style>\n' + '        .faq-item { border-bottom: 1px solid var(--border-color); margin-bottom: 0.5rem; }\n' + '        .faq-question { cursor: pointer; display: flex; justify-content: space-between; align-items: center; padding: 1rem 0; }\n' + '        .faq-answer { display: none; padding-bottom: 1rem; }\n' + '    </style>')

# Insert before the last closing FAQ item Div (which is just before </section> or similar)
# Let's find end of FAQ list.
if 'Quais são os prazos processuais para quesitos?' not in content:
    content = content.replace('<div class="faq-item reveal">\n                    <div class="faq-question" onclick="toggleFaq(this)">\n                        <h3>Onde vocês atendem?</h3>', html_to_add + '\n                <div class="faq-item reveal">\n                    <div class="faq-question" onclick="toggleFaq(this)">\n                        <h3>Onde vocês atendem?</h3>')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated laudo-pericial-engenharia.html FAQ.")

