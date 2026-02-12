# PLANO DE REDESIGN — PROTON ENGENHARIA v2.0
## Migração Visual Inspirada no Site Internacional (protoninusa.com)

**Data de Início:** 11/02/2026  
**Status:** 🟡 EM PLANEJAMENTO  
**Branch de trabalho:** v2-staging/  
**Site de referência visual:** https://protoninusa.com/partnership.html  
**Público-alvo:** Síndicos, administradoras e gestores condominiais em Goiás, Brasília e DF  

---

## 📋 ÍNDICE

1. [Visão Geral do Projeto](#1-visão-geral)
2. [Inventário de Páginas](#2-inventário-de-páginas)
3. [Design System — Nova Identidade Visual](#3-design-system)
4. [Arquitetura CSS](#4-arquitetura-css)
5. [Plano de Execução por Página](#5-plano-de-execução)
6. [Conteúdo — Melhorias por Página](#6-conteúdo-melhorias)
7. [SEO — Atualização Técnica](#7-seo)
8. [Checklist de Validação](#8-checklist-validação)
9. [Processo de Substituição Final](#9-processo-substituição)
10. [Controle de Progresso](#10-controle-progresso)

---

## 1. VISÃO GERAL

### Objetivo
Redesenhar completamente o site protoncd.com.br adotando o estilo visual moderno, profissional e dark-theme do site internacional (protoninusa.com), mantendo o conteúdo em português e otimizado para o público regional (Goiás, Brasília, DF).

### Princípios do Redesign
- **Dark Theme:** Fundo escuro (#0a0a0f / #0f0f1a), textos claros, gradientes verdes/azuis
- **Tipografia Premium:** Inter/Raleway com pesos variados para hierarquia
- **Cards com Glassmorphism:** Efeito de vidro fosco com backdrop-blur
- **Gradientes Profissionais:** Verde Proton (#006666 → #00cc88) e azul (#1e3a5f → #3b82f6)
- **Animações Suaves:** Scroll-reveal, hover transitions, parallax moderno
- **Mobile-First:** Design responsivo prioritário
- **Performance:** Core Web Vitals otimizados (lazy loading, CSS crítico inline)

### O que NÃO muda
- Domínio: protoncd.com.br
- Público-alvo: Goiás, Brasília, DF
- Posicionamento: Consultoria independente (não executa projetos/obras)
- Telefone/WhatsApp: +55 62 99285-2704
- E-mail: lima.georgio.eng@gmail.com
- URLs das páginas (manter canonical links)

---

## 2. INVENTÁRIO DE PÁGINAS

### Páginas Principais (Raiz)
| # | Arquivo | Função | Prioridade |
|---|---------|--------|------------|
| 1 | `index.html` | Homepage principal | 🔴 ALTA |
| 2 | `inspecao-sistemas-mecanicos.html` | Hub de sistemas mecânicos | 🔴 ALTA |
| 3 | `analise-vibracao-elevadores.html` | Ensaios 360° elevadores | 🔴 ALTA |
| 4 | `landing-servicos.html` | Landing de serviços | 🔴 ALTA |
| 5 | `pacotes-servicos.html` | Pacotes comerciais | 🔴 ALTA |
| 6 | `inspecao-hvac-pmoc.html` | HVAC/Climatização | 🟡 MÉDIA |
| 7 | `inspecao-casa-bombas.html` | Casa de bombas | 🟡 MÉDIA |
| 8 | `inspecao-combate-incendio.html` | Combate a incêndio | 🟡 MÉDIA |
| 9 | `inspecao-pressurizacao-escadas.html` | Pressurização escadas | 🟡 MÉDIA |
| 10 | `inspecao-gas-predial.html` | Gás predial | 🟡 MÉDIA |
| 11 | `inspecao-playgrounds.html` | Playgrounds | 🟡 MÉDIA |
| 12 | `laudo-pericial-engenharia.html` | Laudo pericial | 🟡 MÉDIA |
| 13 | `teste-arrancamento-olhais.html` | Teste arrancamento | 🟡 MÉDIA |
| 14 | `cercon-goias.html` | CERCON Goiás | 🟡 MÉDIA |
| 15 | `franquias.html` | Franquias/Parcerias | 🟡 MÉDIA |
| 16 | `conhecimento-tecnico/index.html` | Hub de conhecimento | 🟢 BAIXA |

### Páginas de Cidades
| # | Arquivo | Cidade |
|---|---------|--------|
| 17 | `anapolis/inspecao-predial-anapolis.html` | Anápolis-GO |
| 18 | `belo-horizonte/analise-vibracao-elevadores-bh.html` | Belo Horizonte-MG |
| 19 | `brasilia/inspecao-predial-brasilia.html` | Brasília-DF |
| 20 | `curitiba/analise-vibracao-elevadores-curitiba.html` | Curitiba-PR |
| 21 | `goiania/inspecao-predial-goiania.html` | Goiânia-GO |
| 22 | `porto-alegre/analise-vibracao-elevadores-poa.html` | Porto Alegre-RS |
| 23 | `rio-de-janeiro/analise-vibracao-elevadores-rj.html` | Rio de Janeiro-RJ |
| 24 | `rio-verde/inspecao-predial-rio-verde.html` | Rio Verde-GO |
| 25 | `sao-paulo/analise-vibracao-elevadores-sp.html` | São Paulo-SP |

**Total: 25 páginas HTML a redesenhar**

---

## 3. DESIGN SYSTEM — Nova Identidade Visual

### 3.1 Paleta de Cores

```
/* === CORES PRIMÁRIAS === */
--color-bg-primary:     #0a0a0f;      /* Fundo principal (quase preto) */
--color-bg-secondary:   #0f0f1a;      /* Fundo de seções alternadas */
--color-bg-card:        #1a1a2e;      /* Fundo de cards */
--color-bg-card-hover:  #16213e;      /* Card hover */

/* === CORES DE DESTAQUE === */
--color-accent-green:   #00cc88;      /* Verde Proton (CTA principal) */
--color-accent-green-d: #006666;      /* Verde escuro (gradiente) */
--color-accent-blue:    #3b82f6;      /* Azul para links/destaque */
--color-accent-cyan:    #22d3ee;      /* Ciano para badges */

/* === TEXTOS === */
--color-text-primary:   #f0f0f0;      /* Texto principal */
--color-text-secondary: #a0aec0;      /* Texto secundário */
--color-text-muted:     #6b7280;      /* Texto desabilitado */

/* === BORDAS E EFEITOS === */
--color-border:         rgba(255,255,255,0.08);
--color-glass:          rgba(255,255,255,0.05);
--color-glass-border:   rgba(255,255,255,0.1);

/* === GRADIENTES === */
--gradient-hero:        linear-gradient(135deg, #0a0a0f 0%, #1a1a2e 50%, #0f2027 100%);
--gradient-green:       linear-gradient(135deg, #006666 0%, #00cc88 100%);
--gradient-card:        linear-gradient(135deg, rgba(0,204,136,0.1) 0%, rgba(59,130,246,0.05) 100%);
--gradient-cta:         linear-gradient(135deg, #00cc88 0%, #006666 100%);
```

### 3.2 Tipografia

```
/* Títulos */
font-family: 'Inter', 'Raleway', sans-serif;
h1: 3.5rem (56px) — weight 800
h2: 2.5rem (40px) — weight 700  
h3: 1.5rem (24px) — weight 600
h4: 1.25rem (20px) — weight 600

/* Corpo */
body: 1rem (16px) — weight 400, line-height: 1.75
lead: 1.25rem (20px) — weight 400, line-height: 1.6

/* Labels/Badges */
badge: 0.75rem (12px) — weight 700, text-transform: uppercase, letter-spacing: 0.1em
```

### 3.3 Componentes Visuais

#### Cards (estilo glassmorphism)
```css
.card-glass {
    background: rgba(255, 255, 255, 0.03);
    backdrop-filter: blur(20px);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 16px;
    padding: 2rem;
    transition: all 0.4s ease;
}
.card-glass:hover {
    background: rgba(255, 255, 255, 0.06);
    border-color: rgba(0, 204, 136, 0.3);
    transform: translateY(-4px);
    box-shadow: 0 20px 60px rgba(0, 204, 136, 0.1);
}
```

#### Botões CTA
```css
.btn-primary {
    background: linear-gradient(135deg, #00cc88 0%, #006666 100%);
    color: #fff;
    padding: 1rem 2rem;
    border-radius: 12px;
    font-weight: 600;
    transition: all 0.3s ease;
    box-shadow: 0 4px 20px rgba(0, 204, 136, 0.3);
}
.btn-primary:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 30px rgba(0, 204, 136, 0.4);
}
```

#### Badges de Norma/Compliance
```css
.badge-compliance {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    background: rgba(0, 204, 136, 0.1);
    border: 1px solid rgba(0, 204, 136, 0.3);
    color: #00cc88;
    padding: 0.5rem 1rem;
    border-radius: 999px;
    font-size: 0.75rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.05em;
}
```

#### Seções com Dividers
```css
.section-divider {
    width: 80px;
    height: 3px;
    background: linear-gradient(90deg, #00cc88, #3b82f6);
    margin: 1.5rem auto;
    border-radius: 2px;
}
```

### 3.4 Layout de Seções (estrutura padrão)

```
┌─────────────────────────────────────────┐
│  NAV (fixo topo, glassmorphism, dark)   │
├─────────────────────────────────────────┤
│  HERO (full viewport, gradiente, CTA)   │
│  ─ H1 grande com span colorido          │
│  ─ Subtítulo secundário                 │
│  ─ 2-3 botões CTA                       │
│  ─ Badges de credibilidade              │
├─────────────────────────────────────────┤
│  SEÇÃO 1 — Cards de Serviço (grid)      │
│  ─ Ícones FontAwesome 6                 │
│  ─ Cards glassmorphism                  │
│  ─ Hover com glow verde                 │
├─────────────────────────────────────────┤
│  SEÇÃO 2 — Metodologia (steps 01-04)    │
│  ─ Timeline vertical ou horizontal      │
│  ─ Número grande + descrição            │
├─────────────────────────────────────────┤
│  SEÇÃO 3 — Diferenciais / Por quê nós   │
│  ─ Layout 2 colunas                     │
│  ─ Ícones + texto                       │
├─────────────────────────────────────────┤
│  SEÇÃO 4 — FAQ Accordion                │
│  ─ Perguntas expansíveis                │
│  ─ Schema.org FAQPage                   │
├─────────────────────────────────────────┤
│  SEÇÃO 5 — CTA Final + Contato          │
│  ─ Formulário ou WhatsApp               │
│  ─ Gradiente de fundo                   │
├─────────────────────────────────────────┤
│  FOOTER (dark, links, compliance)       │
└─────────────────────────────────────────┘
```

---

## 4. ARQUITETURA CSS

### Estrutura de arquivos CSS na v2

```
v2-staging/
├── css/
│   ├── variables.css        ← Custom properties (cores, fontes, espaçamentos)
│   ├── base.css             ← Reset, tipografia, utilitários
│   ├── components.css       ← Cards, botões, badges, nav, footer
│   ├── layout.css           ← Grid, seções, hero, responsivo
│   ├── animations.css       ← Scroll-reveal, hover, transitions
│   └── pages/
│       ├── home.css         ← Específico da homepage
│       ├── servicos.css     ← Específico de páginas de serviço
│       └── cidades.css      ← Específico de landing pages de cidades
```

### Abordagem
- **CSS puro customizado** (sem Tailwind) para controle total do dark theme
- **CSS Custom Properties** para fácil manutenção de cores/espaçamentos
- **Minimal JavaScript** — animações via CSS + IntersectionObserver
- **Font Awesome 6** para ícones (já usado)
- **Google Fonts: Inter** (principal) + Raleway (headings)

---

## 5. PLANO DE EXECUÇÃO POR PÁGINA

### FASE 1 — Fundação (Semana 1-2)
| Etapa | Tarefa | Status |
|-------|--------|--------|
| 1.1 | Criar sistema CSS (variables, base, components, layout) | ⬜ |
| 1.2 | Criar template HTML base (nav + footer + seções padrão) | ⬜ |
| 1.3 | Redesenhar `index.html` (homepage) | ⬜ |
| 1.4 | Redesenhar `inspecao-sistemas-mecanicos.html` | ⬜ |
| 1.5 | Redesenhar `analise-vibracao-elevadores.html` | ⬜ |
| 1.6 | **VALIDAÇÃO** — Revisar as 3 páginas antes de prosseguir | ⬜ |

### FASE 2 — Serviços (Semana 2-3)
| Etapa | Tarefa | Status |
|-------|--------|--------|
| 2.1 | Redesenhar `landing-servicos.html` | ⬜ |
| 2.2 | Redesenhar `pacotes-servicos.html` | ⬜ |
| 2.3 | Redesenhar `inspecao-hvac-pmoc.html` | ⬜ |
| 2.4 | Redesenhar `inspecao-casa-bombas.html` | ⬜ |
| 2.5 | Redesenhar `inspecao-combate-incendio.html` | ⬜ |
| 2.6 | Redesenhar `inspecao-pressurizacao-escadas.html` | ⬜ |
| 2.7 | Redesenhar `inspecao-gas-predial.html` | ⬜ |
| 2.8 | Redesenhar `inspecao-playgrounds.html` | ⬜ |
| 2.9 | **VALIDAÇÃO** — Revisar todas as páginas de serviço | ⬜ |

### FASE 3 — Páginas Especiais (Semana 3)
| Etapa | Tarefa | Status |
|-------|--------|--------|
| 3.1 | Redesenhar `laudo-pericial-engenharia.html` | ⬜ |
| 3.2 | Redesenhar `teste-arrancamento-olhais.html` | ⬜ |
| 3.3 | Redesenhar `cercon-goias.html` | ⬜ |
| 3.4 | Redesenhar `franquias.html` | ⬜ |
| 3.5 | Redesenhar `conhecimento-tecnico/index.html` | ⬜ |
| 3.6 | **VALIDAÇÃO** — Revisar páginas especiais | ⬜ |

### FASE 4 — Cidades (Semana 3-4)
| Etapa | Tarefa | Status |
|-------|--------|--------|
| 4.1 | Criar template base para páginas de cidades | ⬜ |
| 4.2 | Redesenhar `anapolis/inspecao-predial-anapolis.html` | ⬜ |
| 4.3 | Redesenhar `belo-horizonte/analise-vibracao-elevadores-bh.html` | ⬜ |
| 4.4 | Redesenhar `brasilia/inspecao-predial-brasilia.html` | ⬜ |
| 4.5 | Redesenhar `curitiba/analise-vibracao-elevadores-curitiba.html` | ⬜ |
| 4.6 | Redesenhar `goiania/inspecao-predial-goiania.html` | ⬜ |
| 4.7 | Redesenhar `porto-alegre/analise-vibracao-elevadores-poa.html` | ⬜ |
| 4.8 | Redesenhar `rio-de-janeiro/analise-vibracao-elevadores-rj.html` | ⬜ |
| 4.9 | Redesenhar `rio-verde/inspecao-predial-rio-verde.html` | ⬜ |
| 4.10 | Redesenhar `sao-paulo/analise-vibracao-elevadores-sp.html` | ⬜ |
| 4.11 | **VALIDAÇÃO** — Revisar todas as páginas de cidades | ⬜ |

### FASE 5 — SEO e Finalização (Semana 4)
| Etapa | Tarefa | Status |
|-------|--------|--------|
| 5.1 | Atualizar todos os Schema.org (structured data) | ⬜ |
| 5.2 | Revisar meta descriptions e titles | ⬜ |
| 5.3 | Verificar canonical links | ⬜ |
| 5.4 | Atualizar sitemap.xml | ⬜ |
| 5.5 | Testar Core Web Vitals (Lighthouse) | ⬜ |
| 5.6 | Testar mobile responsividade | ⬜ |
| 5.7 | **VALIDAÇÃO FINAL** antes da substituição | ⬜ |

### FASE 6 — Deploy (Após aprovação)
| Etapa | Tarefa | Status |
|-------|--------|--------|
| 6.1 | Backup completo do site atual (branch `v1-backup`) | ⬜ |
| 6.2 | Mover arquivos v2-staging/ para raiz | ⬜ |
| 6.3 | Testar todas as URLs no ar | ⬜ |
| 6.4 | Submeter sitemap atualizado ao Google Search Console | ⬜ |
| 6.5 | Solicitar reindexação das páginas alteradas | ⬜ |
| 6.6 | Monitorar Search Console por 7 dias | ⬜ |

---

## 6. CONTEÚDO — Melhorias por Página

### 6.1 Homepage (`index.html`)

**ANTES:** Template genérico de café com parallax  
**DEPOIS:** Homepage profissional dark-theme

#### Seções Planejadas:
1. **Hero** — "Inspeção Predial com Tecnologia 360° e Inteligência Artificial"
   - Subtítulo: "Diagnósticos exclusivos em elevadores, HVAC, bombas e sistemas mecânicos para condomínios em Goiás e Distrito Federal"
   - CTAs: "Solicitar Proposta" + "Conheça a Tecnologia"
   - Badges: CREA, ART, NBR, ISO 18738

2. **Diferenciais** — Cards glassmorphism (4 cards)
   - Ensaios 360° com IA
   - Laudos com ART-CREA
   - Consultoria Independente
   - +150 Inspeções Certificadas

3. **Serviços** — Grid de cards com ícones
   - Elevadores 360° | HVAC/PMOC | Casa de Bombas | Incêndio | Pressurização | Gás | Playgrounds

4. **Metodologia** — Steps visuais (01 → 04)
   - Coleta de Dados → Processamento IA → Diagnóstico → Laudo Técnico

5. **Área de Atuação** — Mapa/badges de cidades
   - Goiânia, Anápolis, Brasília, Rio Verde + cidades atendidas

6. **Depoimentos / Credibilidade** — Números e certificações
   - +150 inspeções | +10 anos | CREA | ART | ISO

7. **FAQ** — Perguntas frequentes accordion
   - Mantidas/melhoradas do site atual

8. **CTA Final + Contato** — WhatsApp + Formulário

9. **Footer** — Links, compliance badges, redes sociais

---

### 6.2 Inspeção de Sistemas Mecânicos (`inspecao-sistemas-mecanicos.html`)

**Melhorias de Conteúdo:**
- Reformular hero para destacar a tecnologia 360° como diferencial principal
- Adicionar seção de comparação: "Inspeção Tradicional vs. Diagnóstico 360° Proton"
- Incluir timeline da metodologia (similar ao international site)
- Melhorar FAQ com perguntas mais específicas
- Adicionar badges de normas (NBR, ABNT, ISO)
- Corrigir erros de encoding encontrados ("àltima", "Relatário", "Obrigatário")

---

### 6.3 Análise de Vibração em Elevadores (`analise-vibracao-elevadores.html`)

**Melhorias de Conteúdo:**
- Seção hero com dados técnicos impactantes
- Cards comparativos: Técnico Humano vs. Inteligência Preditiva (igual ao international)
- Seção de equipamentos/sensores utilizados
- Gráficos de vibração como evidência visual
- Seção "Marcas Atendidas" com grid de logos
- FAQ técnico expandido

---

### 6.4 Demais Páginas de Serviço

**Padrão de conteúdo para cada página:**
1. Hero com ícone + título + descrição focada
2. "Por que é importante" — contextualização da norma
3. "O que inspecionamos" — checklist detalhado
4. "Normas de referência" — badges de compliance
5. "Como funciona" — 3-4 steps visuais
6. FAQ específico do serviço (3-5 perguntas)
7. CTA — "Solicitar Inspeção" + WhatsApp
8. Links relacionados para outros serviços

---

### 6.5 Páginas de Cidades

**Padrão de conteúdo para cada cidade:**
1. Hero com nome da cidade em destaque
2. "Por que [Cidade] precisa de inspeção predial"
3. Serviços disponíveis naquela cidade
4. Normas locais aplicáveis
5. Depoimentos/casos regionais
6. CTA local com WhatsApp

---

## 7. SEO — Atualização Técnica

### 7.1 Meta Tags (todas as páginas)
- [ ] title tags otimizados (max 60 chars)
- [ ] meta description (max 155 chars, com CTA)
- [ ] canonical links corretos
- [ ] og:title, og:description, og:image (Open Graph)
- [ ] robots meta (index, follow)

### 7.2 Schema.org (Structured Data)
- [ ] Organization schema na homepage
- [ ] LocalBusiness schema com áreas atendidas
- [ ] Service schema em cada página de serviço
- [ ] FAQPage schema em páginas com FAQ
- [ ] BreadcrumbList schema em todas as páginas
- [ ] WebPage schema em todas as páginas

### 7.3 Performance
- [ ] CSS crítico inline no `<head>`
- [ ] Lazy loading de imagens
- [ ] Font-display: swap
- [ ] Preconnect para fontes Google
- [ ] Minificação de CSS/JS antes do deploy
- [ ] Lighthouse score > 90 em todas as categorias

### 7.4 Sitemap
- [ ] Atualizar sitemap.xml com todas as páginas
- [ ] Verificar lastmod dates
- [ ] Submeter ao Google Search Console

---

## 8. CHECKLIST DE VALIDAÇÃO

### Pré-deploy (para cada página)
- [ ] Visual confere com design system (dark theme, cards, tipografia)
- [ ] Todos os links internos funcionam
- [ ] Responsivo em mobile (320px, 375px, 768px, 1024px, 1440px)
- [ ] Contraste de cores acessível (WCAG AA)
- [ ] Sem erros de encoding (UTF-8)
- [ ] Schema.org válido (Google Rich Results Test)
- [ ] Meta tags preenchidas corretamente
- [ ] Imagens com alt text
- [ ] WhatsApp link funcionando
- [ ] Footer consistente em todas as páginas
- [ ] Nav consistente em todas as páginas
- [ ] Favicon presente
- [ ] GTM/GA4 tags funcionando

### Performance
- [ ] Lighthouse Performance > 90
- [ ] Lighthouse Accessibility > 90
- [ ] Lighthouse SEO > 95
- [ ] Lighthouse Best Practices > 90

---

## 9. PROCESSO DE SUBSTITUIÇÃO FINAL

### Passo a Passo para Deploy

```
1. BACKUP
   git checkout -b v1-backup
   git add -A && git commit -m "Backup v1 antes do redesign"
   git push origin v1-backup

2. PREPARAÇÃO
   git checkout main
   - Copiar CSS da v2-staging/css/ → css/
   - Substituir cada HTML da v2-staging/ → raiz
   - Manter robots.txt, CNAME, sitemap.xml atualizados

3. TESTE LOCAL
   - Abrir cada página no navegador
   - Testar todos os links
   - Verificar responsividade

4. DEPLOY
   git add -A
   git commit -m "Redesign v2.0 — Dark theme + conteúdo otimizado"
   git push origin main

5. PÓS-DEPLOY
   - Google Search Console: Submeter sitemap
   - Solicitar reindexação das top 10 páginas
   - Monitorar erros de cobertura por 7 dias
   - Testar velocidade via PageSpeed Insights
```

---

## 10. CONTROLE DE PROGRESSO

| Fase | Descrição | Páginas | Status |
|------|-----------|---------|--------|
| 1 | Fundação (CSS + 3 páginas) | 3 | ⬜ Não iniciada |
| 2 | Serviços | 8 | ⬜ Não iniciada |
| 3 | Especiais | 5 | ⬜ Não iniciada |
| 4 | Cidades | 9 | ⬜ Não iniciada |
| 5 | SEO + Finalização | — | ⬜ Não iniciada |
| 6 | Deploy | — | ⬜ Não iniciada |

**Progresso Total: 0/25 páginas redesenhadas**

---

## NOTAS IMPORTANTES

1. **NUNCA substituir o site atual antes da validação completa** — tudo fica em `v2-staging/`
2. **Cada fase tem um checkpoint de validação** — não avançar sem aprovação
3. **Erros de encoding do site atual** devem ser corrigidos na v2 (ex: "Relatário" → "Relatório")
4. **URLs devem permanecer idênticas** para preservar SEO e backlinks
5. **As pastas de cidades mantêm a mesma estrutura** (`anapolis/`, `brasilia/`, etc.)
6. **O arquivo `v2-staging/` pode ser visualizado localmente** antes do deploy

---

*Documento gerado em 11/02/2026 — Atualizar conforme progresso*
