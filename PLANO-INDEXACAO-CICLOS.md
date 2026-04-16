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

## Pos-lote 2 (2026-04-16 18:38:42 UTC)

- URLs auditadas (sitemap): 283
- URLs com issues: 178
- URLs sem issues: 105
- Delta vs baseline:
  - URLs com issues: -34
  - title_len_outside_20_70: 179 -> 150 (-29)
  - desc_len_outside_70_180: 112 -> 83 (-29)
- Delta vs pos-deploy anterior:
  - URLs com issues: -1
  - title_len_outside_20_70: -1
  - desc_len_outside_70_180: -1

## Pos-push lote 2 (2026-04-16 18:37:31 UTC)

- URLs auditadas (sitemap): 283
- URLs com issues: 168
- URLs sem issues: 115
- Delta vs baseline:
  - URLs com issues: -44
  - title_len_outside_20_70: 179 -> 140 (-39)
  - desc_len_outside_70_180: 112 -> 73 (-39)
- Delta vs pos-lote 2 anterior:
  - URLs com issues: -10
  - title_len_outside_20_70: -10
  - desc_len_outside_70_180: -10

## Pos-lote 3 (2026-04-16 18:57:58 UTC)

- URLs auditadas (sitemap): 283
- URLs com issues: 161
- URLs sem issues: 122
- Delta vs baseline:
  - URLs com issues: -51
  - title_len_outside_20_70: 179 -> 133 (-46)
  - desc_len_outside_70_180: 112 -> 67 (-45)
- Delta vs pos-push lote 2:
  - URLs com issues: -7
  - title_len_outside_20_70: -7
  - desc_len_outside_70_180: -6

## Pos-lote 4 (2026-04-16 18:44:46 UTC)

- URLs auditadas (sitemap): 283
- URLs com issues: 150
- URLs sem issues: 133
- Delta vs baseline:
  - URLs com issues: -62
  - title_len_outside_20_70: 179 -> 125 (-54)
  - desc_len_outside_70_180: 112 -> 64 (-48)
- Delta vs pos-lote 3:
  - URLs com issues: -11
  - title_len_outside_20_70: -8
  - desc_len_outside_70_180: -3

## Pos-lote 5 (2026-04-16 18:48:50 UTC)

- URLs auditadas (sitemap): 283
- URLs com issues: 141
- URLs sem issues: 142
- Delta vs baseline:
  - URLs com issues: -71
  - title_len_outside_20_70: 179 -> 116 (-63)
  - desc_len_outside_70_180: 112 -> 64 (-48)
- Delta vs pos-lote 4:
  - URLs com issues: -9
  - title_len_outside_20_70: -9
  - desc_len_outside_70_180: 0

## Pos-lote 6 (2026-04-16 18:55:22 UTC)

- URLs auditadas (sitemap): 283
- URLs com issues: 131
- URLs sem issues: 152
- Delta vs baseline:
  - URLs com issues: -81
  - title_len_outside_20_70: 179 -> 107 (-72)
  - desc_len_outside_70_180: 112 -> 63 (-49)
- Delta vs pos-lote 5:
  - URLs com issues: -10
  - title_len_outside_20_70: -9
  - desc_len_outside_70_180: -1

## Pos-lote 7 (2026-04-16 19:59:09 UTC)

- URLs auditadas (sitemap): 283
- URLs com issues: 121
- URLs sem issues: 162
- Delta vs baseline:
  - URLs com issues: -91
  - title_len_outside_20_70: 179 -> 97 (-82)
  - desc_len_outside_70_180: 112 -> 63 (-49)
- Delta vs pos-lote 6:
  - URLs com issues: -10
  - title_len_outside_20_70: -10
  - desc_len_outside_70_180: 0

## Pos-lote 8 (2026-04-16 20:07:17 UTC)

- URLs auditadas (sitemap): 283
- URLs com issues: 111
- URLs sem issues: 172
- Delta vs baseline:
  - URLs com issues: -101
  - title_len_outside_20_70: 179 -> 87 (-92)
  - desc_len_outside_70_180: 112 -> 63 (-49)
- Delta vs pos-lote 7:
  - URLs com issues: -10
  - title_len_outside_20_70: -10
  - desc_len_outside_70_180: 0

## Pos-lote 9 (2026-04-16 21:48:17 UTC)

- URLs auditadas (sitemap): 283
- URLs com issues: 87
- URLs sem issues: 196
- Delta vs baseline:
  - URLs com issues: -125
  - title_len_outside_20_70: 179 -> 63 (-116)
  - desc_len_outside_70_180: 112 -> 60 (-52)
- Delta vs pos-lote 8:
  - URLs com issues: -24
  - title_len_outside_20_70: -24
  - desc_len_outside_70_180: -3

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
- [x] Corrigir próximo lote até completar 60 URLs prioritárias (concluido: 118/60)
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
