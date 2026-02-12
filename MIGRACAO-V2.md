# MIGRAÇÃO PROTONCD v1 → v2 (Dark Blue Theme)

**Data da migração:** 2026-02-12
**Executada por:** GitHub Copilot (assistido)
**Branch:** main
**Tipo:** Completa — substituição total do front-end

---

## RESUMO DA OPERAÇÃO

Todos os arquivos do site antigo (v1 — tema claro, CSS monolítico, jQuery) foram movidos para a pasta `old/` como backup integral. O conteúdo de `v2-staging/` (tema dark azul, CSS modular, JS vanilla) foi promovido para a raiz do repositório.

---

## INVENTÁRIO DE BACKUP — Pasta `old/`

### old/ (HTMLs raiz)
| Arquivo | Descrição |
|---|---|
| `index.html` | Homepage antiga (tema claro) |
| `analise-vibracao-elevadores.html` | Análise vibração — página nacional |
| `cercon-goias.html` | Cercon Goiás |
| `franquias.html` | Página de franquias |
| `inspecao-casa-bombas.html` | Inspeção casa de bombas |
| `inspecao-combate-incendio.html` | Inspeção combate a incêndio |
| `inspecao-gas-predial.html` | Inspeção gás predial |
| `inspecao-hvac-pmoc.html` | HVAC / PMOC |
| `inspecao-playgrounds.html` | Inspeção de playgrounds |
| `inspecao-pressurizacao-escadas.html` | Pressurização de escadas |
| `inspecao-sistemas-mecanicos.html` | Sistemas mecânicos |
| `landing-servicos.html` | Landing page de serviços |
| `laudo-pericial-engenharia.html` | Laudo pericial |
| `pacotes-servicos.html` | Pacotes de serviços |
| `teste-arrancamento-olhais.html` | Teste arrancamento olhais |
| `teste-arrancamento-olhais-novo.html` | Versão nova do teste |
| `teste-arrancamento-olhais-QUEBRADO.html.bak` | Backup quebrado |
| `teste-arrancamento-olhais.html.backup` | Backup extra |
| `google-verification-example.html` | Exemplo verificação Google |

### old/css/ (CSS monolítico antigo)
| Arquivo | Função |
|---|---|
| `tailwind.css` | Tailwind CSS base |
| `tooplate-antique-cafe.css` | Template principal |
| `tooplate-antique-cafe.old.css` | Template backup |
| `all.min.css` | FontAwesome minificado |
| `core-web-vitals.css` | Otimizações CWV |
| `mobile-fix.css` | Ajustes mobile |
| `mobile-responsive.css` | Responsividade |
| `text-rendering-fix.css` | Renderização de texto |

### old/js/ (JavaScript antigo — jQuery)
| Arquivo | Função |
|---|---|
| `jquery-3.6.0.min.js` | jQuery core |
| `jquery.singlePageNav.min.js` | Navegação SPA |
| `parallax.min.js` | Efeito parallax |

### old/conhecimento-tecnico/
| Arquivo | Função |
|---|---|
| `index.html` | Página base conhecimento técnico |
| `dados/*.json` | 9 arquivos JSON de dados técnicos |

### old/player/
Cópia integral do player antigo (admin.html com tema roxo/branco).

### old/{cidades}/ (Páginas regionais v1)
| Pasta | Arquivos |
|---|---|
| `anapolis/` | `inspecao-predial-anapolis.html` |
| `belo-horizonte/` | `analise-vibracao-elevadores-bh.html` |
| `brasilia/` | `inspecao-predial-brasilia.html` |
| `curitiba/` | `analise-vibracao-elevadores-curitiba.html` |
| `goiania/` | `inspecao-predial-goiania.html` |
| `porto-alegre/` | `analise-vibracao-elevadores-poa.html` |
| `rio-de-janeiro/` | `analise-vibracao-elevadores-rj.html` |
| `rio-verde/` | `inspecao-predial-rio-verde.html` |
| `sao-paulo/` | `analise-vibracao-elevadores-sp.html` + backups |

### old/docs/ (Documentação/Estratégia antiga)
22 arquivos .md de estratégia SEO, checklists, guias e logs de correções que pertencem à v1.

### old/ (Scripts de correção)
10 arquivos Python (.py) e 1 batch (.bat) usados para correções de encoding/schema da v1.

---

## ESTRUTURA v2 ATIVA (RAIZ)

### HTML — Páginas principais
| Arquivo | Descrição | Indexar? |
|---|---|---|
| `index.html` | Homepage — Dark blue theme | ✅ |
| `analise-vibracao-elevadores.html` | Análise vibração (nacional) | ✅ |
| `cercon-goias.html` | Cercon Goiás | ✅ |
| `franquias.html` | Franquias | ✅ |
| `inspecao-casa-bombas.html` | Casa de bombas | ✅ |
| `inspecao-combate-incendio.html` | Combate a incêndio | ✅ |
| `inspecao-gas-predial.html` | Gás predial | ✅ |
| `inspecao-hvac-pmoc.html` | HVAC / PMOC | ✅ |
| `inspecao-playgrounds.html` | Playgrounds | ✅ |
| `inspecao-pressurizacao-escadas.html` | Pressurização escadas | ✅ |
| `inspecao-sistemas-mecanicos.html` | Sistemas mecânicos | ✅ |
| `landing-servicos.html` | Landing serviços | ✅ |
| `laudo-pericial-engenharia.html` | Laudo pericial | ✅ |
| `pacotes-servicos.html` | Pacotes serviços | ✅ |
| `teste-arrancamento-olhais.html` | Teste arrancamento | ✅ |

### Páginas Regionais (Cidades)
| Cidade | Arquivo | Serviço |
|---|---|---|
| Anápolis | `anapolis/inspecao-predial-anapolis.html` | Inspeção predial |
| Belo Horizonte | `belo-horizonte/analise-vibracao-elevadores-bh.html` | Vibração elevadores |
| Brasília | `brasilia/inspecao-predial-brasilia.html` | Inspeção predial |
| Brasília | `brasilia/analise-vibracao-elevadores-brasilia.html` | Vibração elevadores |
| Curitiba | `curitiba/analise-vibracao-elevadores-curitiba.html` | Vibração elevadores |
| Goiânia | `goiania/inspecao-predial-goiania.html` | Inspeção predial |
| Ibitinga | `ibitinga/inspecao-predial-ibitinga.html` | Inspeção predial + mecânica |
| Ibitinga | `ibitinga/avcb-clcb-ibitinga.html` | AVCB / CLCB |
| Ibitinga | `ibitinga/regularizacao-galpoes-ibitinga.html` | Regularização galpões |
| Porto Alegre | `porto-alegre/analise-vibracao-elevadores-poa.html` | Vibração elevadores |
| Rio de Janeiro | `rio-de-janeiro/analise-vibracao-elevadores-rj.html` | Vibração elevadores |
| Rio Verde | `rio-verde/inspecao-predial-rio-verde.html` | Inspeção predial |
| São Paulo | `sao-paulo/analise-vibracao-elevadores-sp.html` | Vibração elevadores |

### CSS — Design System Modular v2
| Arquivo | Função |
|---|---|
| `css/variables.css` | Variáveis CSS (cores, tipografia, espaçamentos) |
| `css/base.css` | Reset, tipografia base, utilitários |
| `css/components.css` | Componentes (cards, botões, badges, forms) |
| `css/layout.css` | Grid, seções, header, footer |
| `css/animations.css` | Animações e transições |

### JS — Vanilla Modern
| Arquivo | Função |
|---|---|
| `js/main.js` | Menu mobile, scroll effects, lazy loading, analytics |

### Assets Compartilhados (não alterados)
| Pasta | Conteúdo |
|---|---|
| `img/` | Imagens, logos, fotos de equipe, ícones |
| `webfonts/` | Fontes web (FontAwesome) |
| `CNAME` | Domínio personalizado GitHub Pages |

---

## PROCEDIMENTO DE ROLLBACK

Para reverter **completamente** ao site v1:

```powershell
# 1. Navegar até a raiz
cd h:\apps\protoncd

# 2. Remover arquivos v2 da raiz (HTMLs)
$v2htmls = @('index.html','analise-vibracao-elevadores.html','cercon-goias.html','franquias.html','inspecao-casa-bombas.html','inspecao-combate-incendio.html','inspecao-gas-predial.html','inspecao-hvac-pmoc.html','inspecao-playgrounds.html','inspecao-pressurizacao-escadas.html','inspecao-sistemas-mecanicos.html','landing-servicos.html','laudo-pericial-engenharia.html','pacotes-servicos.html','teste-arrancamento-olhais.html')
foreach($f in $v2htmls) { Remove-Item $f -Force }

# 3. Restaurar v1 HTMLs
Copy-Item old\*.html . -Force

# 4. Restaurar CSS antigo
Remove-Item css\* -Force
Copy-Item old\css\* css\ -Force

# 5. Restaurar JS antigo
Remove-Item js\* -Force
Copy-Item old\js\* js\ -Force

# 6. Restaurar pastas de cidades (usar versões antigas)
$cities = @('anapolis','belo-horizonte','brasilia','curitiba','goiania','porto-alegre','rio-de-janeiro','rio-verde','sao-paulo')
foreach($c in $cities) {
    Remove-Item "$c\*" -Force
    Copy-Item "old\$c\*" "$c\" -Force
}

# 7. Restaurar conhecimento-tecnico
Remove-Item "conhecimento-tecnico\*" -Recurse -Force
Copy-Item "old\conhecimento-tecnico\*" "conhecimento-tecnico\" -Recurse -Force

# 8. Restaurar player
Remove-Item "player\*" -Force
Copy-Item "old\player\*" "player\" -Force

# 9. Remover ibitinga (não existia na v1)
Remove-Item ibitinga -Recurse -Force

# 10. Restaurar scripts e docs
Copy-Item old\*.py . -Force
Copy-Item old\*.bat . -Force
Copy-Item old\docs\*.md . -Force

# 11. Restaurar robots.txt e sitemap.xml das versões antigas
# (disponíveis no git history)
git checkout HEAD~1 -- robots.txt sitemap.xml
```

### Rollback via Git (mais rápido):
```bash
git log --oneline -5    # identificar commit anterior à migração
git revert <commit_hash>
```

---

## MUDANÇAS TÉCNICAS PRINCIPAIS

| Aspecto | v1 (antigo) | v2 (novo) |
|---|---|---|
| **Tema visual** | Claro (branco/bege) | Dark (azul neon #0a0a0f) |
| **Cor principal** | Verde #00cc88 → Azul | Azul #60a5fa / #3b82f6 |
| **CSS** | Monolítico (tailwind + template) | Modular (5 arquivos) |
| **JavaScript** | jQuery + plugins | Vanilla ES6+ |
| **Hover effect** | Básico | Neon blue levitation glow |
| **Player admin** | Tema roxo/branco | Tema dark azul |
| **Cidades** | 9 cidades | 10 cidades (+Ibitinga) |
| **Brasília** | 1 página | 2 páginas (+elevadores) |
| **Ibitinga** | Inexistente | 3 páginas (predial, AVCB, galpões) |

---

## VALIDADE

Esta documentação é válida enquanto a pasta `old/` existir no repositório.
**NÃO delete a pasta `old/` antes de confirmar que a v2 está 100% funcional em produção.**
