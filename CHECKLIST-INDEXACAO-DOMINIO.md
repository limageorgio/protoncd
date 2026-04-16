# Auditoria Geral de Indexacao - Proton

Data: 2026-04-16 23:52:14 UTC
Sitemap raiz: https://www.protoncd.com.br/sitemap.xml

## Resumo

- URLs auditadas: 283
- URLs sem issues: 283
- URLs com issues: 0

## Issues por tipo


## Checklist de Correcao (Gerenciavel)

- [ ] Corrigir todas as URLs com status diferente de 200.
- [ ] Remover noindex (meta ou header) de URLs que devem indexar.
- [ ] Garantir canonical absoluto e consistente com URL do sitemap.
- [ ] Implementar redirecionamento 301 da variante sem .html para a URL canônica .html.
- [ ] Revisar titles fora de 20-70 caracteres.
- [ ] Revisar descriptions fora de 70-180 caracteres.
- [ ] Validar hreflang (principalmente pares PT/EN recíprocos).
- [ ] Reenviar sitemap e solicitar recrawl no Search Console após ajustes.

## URLs com issues

| URL | Status | Canonical | Issues |
|---|---:|---|---|

## Como rodar novamente

1. Executar: python _tmp_full_indexing_audit.py
2. Conferir arquivos gerados: INDEXACAO_AUDITORIA_RESULT.json e CHECKLIST-INDEXACAO-DOMINIO.md
3. Aplicar correcoes
4. Rodar novamente e comparar a queda das issues