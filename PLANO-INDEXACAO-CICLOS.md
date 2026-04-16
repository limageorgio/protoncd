# Plano de Indexacao - Ciclo Operacional

Data base da auditoria: 2026-04-16 18:07:54 UTC
Origem: INDEXACAO_AUDITORIA_RESULT.json

## Baseline atual

- URLs auditadas (sitemap): 283
- URLs com issues: 212
- URLs sem issues: 71
- Issues encontradas:
  - title_len_outside_20_70: 179
  - desc_len_outside_70_180: 112
  - variantes sem .html ativas em 200: 277 de 277 URLs .html auditadas

## Pos-deploy (2026-04-16 18:29:15 UTC)

- URLs auditadas (sitemap): 283
- URLs com issues: 179
- URLs sem issues: 104
- Delta vs baseline:
  - URLs com issues: -33
  - title_len_outside_20_70: 179 -> 151 (-28)
  - desc_len_outside_70_180: 112 -> 84 (-28)

## Prioridade de execucao

1. Implementar redirecionamento 301 global de URL sem .html para URL .html
2. Ajustar title tags fora da faixa 20-70 caracteres
3. Ajustar meta descriptions fora da faixa 70-180 caracteres
4. Revalidar em lote por sitemap no Search Console
5. Reexecutar auditoria e comparar queda das issues

## Checklist gerenciavel por sprint

### Sprint 1 - Titles

- [x] Implementar regra de redirecionamento 301 para variantes sem .html (deploy realizado)
- [x] Validar amostra de 50 URLs em produção após o deploy (validação por auditoria completa: 283 URLs)
- [x] Corrigir lote prioritário inicial (34 URLs: home, regionais, serviços e EN) no repositório
- [ ] Corrigir próximo lote até completar 60 URLs prioritárias
- [ ] Garantir unicidade por pagina
- [ ] Evitar repeticao de padrao em massa

### Sprint 2 - Descriptions

- [ ] Corrigir 60 URLs com maior impressao no Search Console
- [ ] Garantir resumo util e orientado ao usuario
- [ ] Evitar excesso de palavras-chave

### Sprint 3 - Consolidacao

- [ ] Revisar URLs restantes de title
- [ ] Revisar URLs restantes de description
- [ ] Atualizar lastmod nos sitemaps alterados
- [ ] Solicitar recrawl/indexing no Search Console

## Criterio de aceite por ciclo

- 0 URLs com status diferente de 200 no sitemap
- 0 URLs com noindex indevido
- 0 URLs sem canonical valido
- 0 variantes sem .html retornando 200 em URL canônica .html
- Reducao continua de title_len_outside_20_70
- Reducao continua de desc_len_outside_70_180

## Comandos de revalidacao

1. Rodar auditoria geral

python _tmp_full_indexing_audit.py

2. Comparar resultados

- Abrir INDEXACAO_AUDITORIA_RESULT.json
- Comparar summary.issue_counts com o ciclo anterior
- Atualizar este plano com os novos numeros

## Observacoes

- Este ciclo mediu principalmente prontidao de indexacao on-page via sitemap.
- Para diagnostico completo de "Crawled - currently not indexed", combinar com:
  - URL Inspection por amostra de URLs prioritarias
  - Relatorio de canonical selecionada pelo Google
  - Verificacao de conteudo duplicado entre paginas regionais
