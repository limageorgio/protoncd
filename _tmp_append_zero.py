import datetime
# Append the final result to PLANO-INDEXACAO-CICLOS.md
with open('PLANO-INDEXACAO-CICLOS.md', 'a', encoding='utf-8') as f:
    f.write('\n## Resultado Final - Pos-Lotes E9, E10, E11 e E12 (2026-04-16)\n\n')
    f.write('- URLs auditadas (sitemap): 283\n')
    f.write('- URLs com issues: 0 ??\n')
    f.write('- URLs sem issues: 283\n')
    f.write('- Delta vs Pos-lote E8:\n')
    f.write('  - URLs com issues: -29\n')
    f.write('  - title_len_outside_20_70: 21 -> 0 (-21)\n')
    f.write('  - desc_len_outside_70_180: 29 -> 0 (-29)\n')
    f.write('\n**Meta Atingida!** O site esta 100% com titulos e descricoes adequados aos padroes de SEO (20-70 caracteres para titulos e 70-180 para descricoes).\n')

# Check off things in CHECKLIST-INDEXACAO-DOMINIO.md
with open('CHECKLIST-INDEXACAO-DOMINIO.md', 'r', encoding='utf-8') as f:
    text = f.read()
text = text.replace('- [ ] Revisar titles muito curtos ou longos (< 20 ou > 70 chars)', '- [x] Revisar titles muito curtos ou longos (< 20 ou > 70 chars)')
text = text.replace('- [ ] Revisar descriptions ausentes, curtas ou longas (< 70 ou > 180 chars)', '- [x] Revisar descriptions ausentes, curtas ou longas (< 70 ou > 180 chars)')
with open('CHECKLIST-INDEXACAO-DOMINIO.md', 'w', encoding='utf-8') as f:
    f.write(text)
