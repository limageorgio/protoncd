import re

file_path = 'laudo-pericial-engenharia.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

html_to_add = """                
                <div class="faq-item reveal">
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

if 'Quais são os prazos processuais' not in content:
    # Let's insert before the end of the section
    # Actually just search for the last closing div before the end of the section id="faq"
    faq_section = re.search(r'(id="faq".*?</section>)', content, re.DOTALL)
    if faq_section:
        original_section = faq_section.group(1)
        # Find the div closing the accordion/list
        new_section = original_section.replace('</div>\n            </div>\n        </div>\n    </section>', html_to_add + '</div>\n            </div>\n        </div>\n    </section>')
        content = content.replace(original_section, new_section)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Updated HTML FAQ")
