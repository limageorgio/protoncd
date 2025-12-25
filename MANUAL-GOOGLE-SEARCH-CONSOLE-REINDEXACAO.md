# Manual de Reindexação no Google Search Console
**Proton Engenharia Mecânica**  
Atualizado em: 25/12/2025

---

## 📋 Índice
1. [Quando Solicitar Reindexação](#quando-solicitar-reindexacao)
2. [Acesso ao Google Search Console](#acesso-ao-google-search-console)
3. [Lista de URLs por Ordem de Prioridade](#lista-de-urls-por-ordem-de-prioridade)
4. [Procedimento de Reindexação](#procedimento-de-reindexacao)
5. [Monitoramento Pós-Reindexação](#monitoramento-pos-reindexacao)
6. [Integração com Google Analytics 4](#integracao-com-google-analytics-4)
7. [Checklist de Validação](#checklist-de-validacao)

---

## 🔄 Quando Solicitar Reindexação

### Situações que requerem reindexação:
- ✅ Atualização de meta tags (title, description, Open Graph)
- ✅ Adição ou remoção de serviços principais
- ✅ Modificação de Schema JSON-LD (LocalBusiness, Service)
- ✅ Alteração de conteúdo significativo (novos serviços, FAQs)
- ✅ Mudança de URL canonical
- ✅ Atualização de pacotes ou preços
- ✅ Expansão geográfica (novas cidades/regiões)

### Situações que NÃO requerem reindexação imediata:
- ❌ Correções ortográficas ou gramaticais
- ❌ Ajustes de CSS/design sem impacto em conteúdo
- ❌ Atualização de imagens sem alt text
- ❌ Mudanças em JavaScript (exceto Schema)

---

## 🔑 Acesso ao Google Search Console

### URL de Acesso:
```
https://search.google.com/search-console
```

### Propriedade Verificada:
```
https://www.protoncd.com.br
```

### Pré-requisitos:
1. Acesso autenticado à conta Google vinculada ao domínio
2. Propriedade verificada via arquivo `googlexxxxxxxxxx.html` na raiz
3. Sitemap.xml enviado e validado

### Verificação de Status:
- **Sitemap**: Enviar `https://www.protoncd.com.br/sitemap.xml`
- **Cobertura**: Menu lateral > Cobertura > Verificar páginas indexadas
- **URLs inspecionadas**: Usar ferramenta de inspeção de URL (lupa superior)

---

## 📊 Lista de URLs por Ordem de Prioridade

### 🥇 **PRIORIDADE 1 - Homepage (Valor Agregado: Máximo)**
**Critério:** Porta de entrada principal, taxa de conversão mais alta

| # | URL | Última Modificação | Prioridade Sitemap | Motivo |
|---|-----|-------------------|-------------------|---------|
| 1 | `https://www.protoncd.com.br/` | 2025-12-21 | 1.0 | Homepage nacional, ponto de entrada SEO |

---

### 🥇 **PRIORIDADE 2 - Páginas Locais (Valor Agregado: Alto)**
**Critério:** Conversão local, SEO geográfico, Schema LocalBusiness completo

| # | URL | Última Modificação | Prioridade Sitemap | Motivo |
|---|-----|-------------------|-------------------|---------|
| 2 | `https://www.protoncd.com.br/brasilia/inspecao-predial-brasilia.html` | 2025-12-24 | 0.93 | Capital federal, órgãos públicos, mercado premium |
| 3 | `https://www.protoncd.com.br/goiania/inspecao-predial-goiania.html` | 2025-12-24 | 0.92 | Cidade sede, maior volume de clientes |
| 4 | `https://www.protoncd.com.br/anapolis/inspecao-predial-anapolis.html` | 2025-12-24 | 0.91 | Hub industrial DAIA, condomínios verticais |
| 5 | `https://www.protoncd.com.br/rio-verde/inspecao-predial-rio-verde.html` | 2025-12-24 | 0.90 | Agroindústria, expansão regional GO |

**Atualização recente (24/12/2025):**
- ✅ Adicionados serviços de playgrounds (NBR 16071) e teste de olhais (NR-35)
- ✅ Schema expandido de 2 para 4 serviços por página
- ✅ Meta descriptions atualizadas com novos serviços
- ✅ Open Graph e Twitter Cards completos
- ✅ 8 novos FAQs (2 por cidade)

---

### 🥈 **PRIORIDADE 3 - Serviços Premium (Valor Agregado: Alto)**
**Critério:** Ticket médio elevado, margens altas, diferencial competitivo

| # | URL | Última Modificação | Prioridade Sitemap | Motivo |
|---|-----|-------------------|-------------------|---------|
| 6 | `https://www.protoncd.com.br/analise-vibracao-elevadores.html` | 2025-12-21 | 0.95 | Ensaios 360º exclusivos, maior diferencial técnico |
| 7 | `https://www.protoncd.com.br/cercon-goias.html` | 2025-12-21 | 0.95 | CERCON Goiás, conformidade CBMGO, mercado regulado |
| 8 | `https://www.protoncd.com.br/inspecao-hvac-pmoc.html` | 2025-12-21 | 0.95 | PMOC obrigatório, recorrência anual, alto volume |
| 9 | `https://www.protoncd.com.br/laudo-pericial-engenharia.html` | 2025-12-21 | 0.94 | Perícias judiciais, honorários elevados |

---

### 🥈 **PRIORIDADE 4 - Serviços Estratégicos (Valor Agregado: Médio-Alto)**
**Critério:** Obrigatoriedade normativa, recorrência, compliance

| # | URL | Última Modificação | Prioridade Sitemap | Motivo |
|---|-----|-------------------|-------------------|---------|
| 10 | `https://www.protoncd.com.br/inspecao-gas-predial.html` | 2025-12-21 | 0.93 | NR-13, NB-70, conformidade Corpo de Bombeiros |
| 11 | `https://www.protoncd.com.br/inspecao-casa-bombas.html` | 2025-12-21 | 0.93 | NBR 5626, IT-15 CBMGO, sistema crítico |
PAREI AQUI | 12 | `https://www.protoncd.com.br/inspecao-combate-incendio.html` | 2025-12-21 | 0.93 | IT-14 CBMGO, obrigatório auditorias CERCON |
| 13 | `https://www.protoncd.com.br/inspecao-pressurizacao-escadas.html` | 2025-12-21 | 0.92 | NBR 14880, IT-15 CBMGO, requisito AVCB |
| 14 | `https://www.protoncd.com.br/inspecao-playgrounds.html` | 2025-12-21 | 0.92 | NBR 16071, seguradoras, responsabilidade civil |
| 15 | `https://www.protoncd.com.br/teste-arrancamento-olhais.html` | 2025-12-21 | 0.91 | NR-35 obrigatória, teste anual, risco alto |

---

### 🥉 **PRIORIDADE 5 - Páginas Agregadoras (Valor Agregado: Médio)**
**Critério:** Funil comercial, múltiplos serviços, conversão indireta

| # | URL | Última Modificação | Prioridade Sitemap | Motivo |
|---|-----|-------------------|-------------------|---------|
| 16 | `https://www.protoncd.com.br/pacotes-servicos.html` | 2025-12-21 | 0.90 | Cross-selling, pacotes combinados |
| 17 | `https://www.protoncd.com.br/inspecao-sistemas-mecanicos.html` | 2025-12-21 | 0.90 | Landing page serviços, overview técnico |

---

### 🥉 **PRIORIDADE 6 - Base de Conhecimento Técnico (Valor Agregado: SEO + Autoridade)**
**Critério:** Conteúdo educacional, long-tail keywords, autoridade de domínio, backlinks orgânicos

| # | URL | Última Modificação | Prioridade Sitemap | Motivo |
|---|-----|-------------------|-------------------|---------|
| 18 | `https://www.protoncd.com.br/conhecimento-tecnico/` | 2025-12-25 | 0.88 | Hub central de conteúdo, SEO educacional, featured snippets |

**Atualização recente (25/12/2025):**
- ✅ Base de conhecimento técnico com 9 categorias de problemas e soluções
- ✅ Conteúdo baseado em casos reais de inspeções prediais
- ✅ Categorias: Elevadores, HVAC, Portas Corta-Fogo, Pressurizaçãio, Playgrounds, Gás, Impermeabilização, Estruturas Metálicas, Casas de Máquinas
- ✅ Schema.org FAQ e Article implementados
- ✅ Ideal para ranquear em buscas educacionais tipo "como resolver [problema]"

**Categorias da Base de Conhecimento:**
- **Elevadores:** Análise de vibração, ruídos anormais, desalinhamento
- **HVAC/Climatização:** Problemas de refrigeração, eficiência energética, manutenção PMOC
- **Portas Corta-Fogo:** Vedação, fechamento automático, conformidade NBR
- **Pressurizaçào de Escadas:** Insuficiência de pressão, exaustores
- **Playgrounds:** NBR 16071, pisos inadequados, equipamentos danificados
- **Instalações de Gás:** Vazamentos, conformidade NR-13, válvulas
- **Impermeabilização:** Infiltrações, lajes, reservatórios
- **Estruturas Metálicas:** Corrosão, soldas, estabilidade
- **Casas de Máquinas:** Ventilação inadequada, sistemas hidráulicos

**Benefícios SEO:**
- 🎯 **Long-tail keywords:** Captura buscas específicas tipo "vibração excessiva elevador condomínio"
- 📚 **Autoridade técnica:** Google reconhece expertise em engenharia mecânica
- 🔗 **Link building:** Síndicos e administradoras compartilham conteúdo educacional
- ⭐ **Featured Snippets:** Formato FAQ ideal para posições zero
- 📈 **Tráfego qualificado:** Usuários pesquisando problemas = alta intenção de conversão

---

### 🥉 **PRIORIDADE 7 - Páginas Comerciais (Valor Agregado: Baixo-Médio)**
**Critério:** Expansão de rede, parcerias, modelo de negócio

| # | URL | Última Modificação | Prioridade Sitemap | Motivo |
|---|-----|-------------------|-------------------|---------|
| 19 | `https://www.protoncd.com.br/franquias.html` | 2025-12-21 | 0.85 | Modelo de franquia, expansão nacional |

---

## 🛠️ Procedimento de Reindexação

### Método 1: Inspeção de URL Individual (Recomendado para até 10 URLs)

#### Passo a Passo:
1. **Acessar Google Search Console**
   - URL: `https://search.google.com/search-console`
   - Selecionar propriedade: `www.protoncd.com.br`

2. **Usar Ferramenta de Inspeção**
   - Clicar no ícone de lupa (🔍) no topo da página
   - Colar URL completa (ex: `https://www.protoncd.com.br/goiania/inspecao-predial-goiania.html`)
   - Pressionar Enter

3. **Solicitar Indexação**
   - Aguardar resultado da inspeção (5-10 segundos)
   - Se status for "URL não está no Google" ou "URL está no Google mas..." 
   - Clicar em **"Solicitar indexação"**
   - Aguardar validação (30-60 segundos)
   - Confirmação: "Solicitação de indexação enviada"

4. **Registrar Solicitação**
   - Anotar data/hora da solicitação
   - Monitorar em 24-72 horas

#### Tempo Estimado:
- **1-5 URLs**: 5-10 minutos
- **6-10 URLs**: 15-20 minutos

---

### Método 2: Reenvio de Sitemap (Recomendado para 10+ URLs)

#### Passo a Passo:
1. **Atualizar Sitemap Local**
   ```bash
   # Editar arquivo sitemap.xml
   # Alterar <lastmod> das URLs modificadas para data atual
   # Exemplo: <lastmod>2025-12-24</lastmod>
   ```

2. **Deploy no Servidor**
   - Upload via FTP/SFTP ou commit Git
   - Verificar acessibilidade: `https://www.protoncd.com.br/sitemap.xml`

3. **Reenviar no Search Console**
   - Menu lateral: **Sitemaps**
   - Verificar sitemap atual listado
   - Clicar em **"Adicionar novo sitemap"** (se necessário)
   - Ou aguardar crawl automático (pode levar 1-7 dias)

4. **Forçar Reprocessamento (Opcional)**
   - Remover sitemap antigo (3 pontos > Remover)
   - Adicionar novamente: `sitemap.xml`
   - Clicar em **"Enviar"**

#### Tempo Estimado:
- **Reenvio**: 2 minutos
- **Processamento Google**: 1-7 dias

---

### Método 3: API de Indexação do Google (Avançado)

#### Quando Usar:
- Reindexação massiva (50+ URLs)
- Automação contínua (CI/CD)
- Páginas dinâmicas/jobs/eventos

#### Requisitos:
- Google API Key configurada
- Service Account com permissões
- Script Python/Node.js customizado

#### Referência:
```
https://developers.google.com/search/apis/indexing-api/v3/quickstart
```

**Nota:** Não recomendado para site institucional estático.

---

## 📈 Monitoramento Pós-Reindexação

### Timeline de Resultados Esperados:

| Tempo | Ação Google | O que Verificar |
|-------|-------------|-----------------|
| 0-4h | Crawl inicial | Search Console > Cobertura > "Rastreamento solicitado" |
| 4-24h | Indexação | Inspeção de URL > "URL está no Google" |
| 24-72h | Aparição em buscas | `site:protoncd.com.br [termo-chave]` |
| 7-14 dias | Estabilização ranking | Desempenho > Consultas > Monitorar posições |
| 30 dias | ROI SEO | Analytics > Conversões > Origem orgânica |

### Ferramentas de Monitoramento:

#### 1. Google Search Console - Desempenho
```
Menu: Desempenho > Páginas
Filtro: Últimos 28 dias
Métricas: Cliques, Impressões, CTR, Posição média
```

**Páginas a Monitorar (Top 6):**
- `/` (homepage)
- `/conhecimento-tecnico/` (base de conhecimento - nova)
- `/goiania/inspecao-predial-goiania.html`
- `/analise-vibracao-elevadores.html`
- `/cercon-goias.html`
- `/inspecao-hvac-pmoc.html`

#### 2. Google Analytics
```
Aquisição > Todo o tráfego > Canais
Segmento: Organic Search
Dimensão secundária: Landing Page
```

#### 3. Teste Manual de Busca Orgânica
Verificar posições para keywords-alvo:

**Nacional:**
- "inspeção predial engenharia"
- "PMOC Goiás"
- "laudo elevador NBR 16042"
- "como resolver vibração elevador" (nova - base conhecimento)
- "problemas HVAC condomínio" (nova - base conhecimento)

**Local (Goiânia):**
- "inspeção predial Goiânia"
- "teste elevador Goiânia"
- "PMOC Goiânia"

**Local (Brasília):**
- "inspeção predial Brasília"
- "HVAC órgãos públicos Brasília"
- "teste olhais Brasília NR-35"

---

## 📊 Integração com Google Analytics 4

### Por que Integrar GA4 com Search Console?

**Benefícios:**
- 📈 Rastrear conversões de tráfego orgânico (WhatsApp, formulários, telefonemas)
- 🎯 Identificar quais páginas convertem melhor
- 💰 Calcular ROI real de SEO (valor por sessão orgânica)
- 🔍 Correlacionar queries do Search Console com comportamento no GA4
- 📊 Criar relatórios unificados de performance

---

### Passo 1: Conectar Search Console ao Google Analytics 4

#### Requisitos:
- Conta Google Analytics 4 configurada (Property ID: G-XXXXXXXX)
- Permissões de administrador em ambas ferramentas

#### Procedimento:

1. **No Google Analytics 4:**
   - Acesse: https://analytics.google.com
   - Selecione a propriedade: **Proton Engenharia (www.protoncd.com.br)**
   - Menu: **Admin** (engrenagem no canto inferior esquerdo)
   - Coluna "Propriedade": **Configurações da propriedade**

2. **Ativar Integração:**
   - Role até: **Vínculos do produto**
   - Clique em: **Vínculos do Search Console**
   - Botão: **Vincular**
   - Selecione: `https://www.protoncd.com.br`
   - Confirme: **Enviar**

3. **Verificar Integração:**
   - No GA4, acesse: **Relatórios > Aquisição > Search Console**
   - Deve aparecer dados de: Consultas, Landing Pages, Países, Dispositivos
   - Prazo para dados aparecerem: 24-48 horas

---

### Passo 2: Configurar Eventos de Conversão Personalizados

#### Eventos Críticos para Proton Engenharia:

**1. Cliques em WhatsApp (3 widgets)**
```javascript
// Adicionar no arquivo JS principal ou inline

// WhatsApp Widget 1 (Principal)
document.getElementById('whatsAppWidget').addEventListener('click', function() {
  gtag('event', 'whatsapp_click', {
    'event_category': 'conversao',
    'event_label': 'whatsapp_principal',
    'widget_position': 'principal',
    'value': 1
  });
});

// WhatsApp Widget 2
document.getElementById('whatsAppWidget2').addEventListener('click', function() {
  gtag('event', 'whatsapp_click', {
    'event_category': 'conversao',
    'event_label': 'whatsapp_secundario',
    'widget_position': 'secundario',
    'value': 1
  });
});

// WhatsApp Widget 3
document.getElementById('whatsAppWidget3').addEventListener('click', function() {
  gtag('event', 'whatsapp_click', {
    'event_category': 'conversao',
    'event_label': 'whatsapp_terciario',
    'widget_position': 'terciario',
    'value': 1
  });
});
```

**2. Visualização de Telefone**
```javascript
// Rastrear quando usuário clica no telefone
const telefones = document.querySelectorAll('a[href^="tel:"]');
telefones.forEach(tel => {
  tel.addEventListener('click', function() {
    gtag('event', 'phone_click', {
      'event_category': 'conversao',
      'event_label': this.textContent,
      'phone_number': this.href.replace('tel:', ''),
      'value': 2
    });
  });
});
```

**3. Engajamento com Base de Conhecimento**
```javascript
// Rastrear expansão de cards de problemas
if (window.location.pathname.includes('/conhecimento-tecnico')) {
  const cards = document.querySelectorAll('.problem-card');
  cards.forEach(card => {
    card.addEventListener('click', function() {
      const categoria = this.dataset.categoria;
      const problema = this.querySelector('h3').textContent;
      
      gtag('event', 'knowledge_engagement', {
        'event_category': 'conteudo',
        'event_label': categoria,
        'problem_title': problema,
        'value': 0.5
      });
    });
  });
}
```

**4. Scroll Depth (Engajamento)**
```javascript
// Rastrear quando usuário rola 75% da página
let scrolled75 = false;

window.addEventListener('scroll', function() {
  const scrollPercent = (window.scrollY / (document.body.scrollHeight - window.innerHeight)) * 100;
  
  if (scrollPercent > 75 && !scrolled75) {
    scrolled75 = true;
    gtag('event', 'scroll_depth', {
      'event_category': 'engajamento',
      'event_label': '75_percent',
      'page_path': window.location.pathname
    });
  }
});
```

**5. Tempo de Permanência (Sessões Qualificadas)**
```javascript
// Rastrear usuários que ficam mais de 60 segundos
setTimeout(function() {
  gtag('event', 'engaged_session', {
    'event_category': 'engajamento',
    'event_label': 'tempo_minimo_60s',
    'session_duration': 60
  });
}, 60000); // 60 segundos
```

---

### Passo 3: Marcar Eventos como Conversões no GA4

1. **No Google Analytics 4:**
   - Menu: **Configurar > Eventos**
   - Localizar eventos:
     - `whatsapp_click`
     - `phone_click`
     - `knowledge_engagement`
     - `engaged_session`

2. **Ativar como Conversão:**
   - Toggle **"Marcar como conversão"** para cada evento
   - Eventos marcados aparecem em: **Relatórios > Engajamento > Conversões**

3. **Definir Valores Monetários (Opcional):**
   - `whatsapp_click`: R$ 50 (lead qualificado)
   - `phone_click`: R$ 80 (intenção alta)
   - `knowledge_engagement`: R$ 10 (interesse educacional)
   - `engaged_session`: R$ 5 (engajamento)

---

### Passo 4: Criar Segmentos Personalizados

#### Segmento 1: "Tráfego Orgânico de Páginas Regionais"
```
Condições:
- Origem da sessão: google / organic
- Landing Page contém: /goiania/ OU /brasilia/ OU /anapolis/ OU /rio-verde/
```

**Uso:** Comparar conversão de tráfego local vs. nacional

#### Segmento 2: "Usuários da Base de Conhecimento"
```
Condições:
- Página visitada contém: /conhecimento-tecnico/
- Eventos incluem: knowledge_engagement
```

**Uso:** Medir eficácia do conteúdo educacional em gerar conversões

#### Segmento 3: "Conversores de Alta Intenção"
```
Condições:
- Evento de conversão: whatsapp_click OU phone_click
- Origem: google / organic
- Tempo de permanência > 60 segundos
```

**Uso:** Identificar jornada típica de leads qualificados

---

### Passo 5: Configurar Relatórios Personalizados

#### Relatório 1: "Performance SEO por Página"

**No GA4:**
1. Menu: **Explorar > Criar exploração**
2. Tipo: **Exploração de forma livre**
3. Configuração:
   ```
   Dimensões:
   - Landing page
   - País
   - Origem/Mídia (google / organic)
   
   Métricas:
   - Usuários
   - Sessões
   - Taxa de conversão de whatsapp_click
   - Taxa de conversão de phone_click
   - Receita do evento (se valores configurados)
   - Tempo médio de engajamento
   ```
4. Filtro: **Origem/Mídia = google / organic**
5. Salvar como: **"SEO - Performance por Landing Page"**

#### Relatório 2: "ROI de Páginas Regionais"
```
Dimensões:
- Landing page (filtrar: contém /goiania/, /brasilia/, etc.)
- Cidade
- Dispositivo

Métricas:
- Conversões (whatsapp + phone)
- Valor total das conversões
- Custo de aquisição: R$ 0 (orgânico)
- ROI: (Valor conversões - Custo) / Custo × 100
```

#### Relatório 3: "Funil de Conversão - Base de Conhecimento"
```
Etapas:
1. Visita /conhecimento-tecnico/ (100%)
2. Evento: knowledge_engagement (% usuários engajados)
3. Navegação para página de serviço (% interessados)
4. Conversão: whatsapp_click ou phone_click (% convertidos)
```

---

### Passo 6: Dashboards de Monitoramento

#### Dashboard Recomendado: "SEO + Conversões"

**Widgets a adicionar:**

1. **Tráfego Orgânico (30 dias)**
   - Gráfico de linha: Usuários orgânicos por dia
   - Comparação: Período anterior

2. **Top 5 Landing Pages Orgânicas**
   - Tabela: Página | Usuários | Conversões | Taxa de Conversão
   - Ordenar por: Conversões (decrescente)

3. **Conversões por Fonte (WhatsApp vs. Telefone)**
   - Gráfico de pizza: Distribuição de eventos de conversão

4. **Taxa de Rejeição por Página Regional**
   - Gráfico de barras: Goiânia, Brasília, Anápolis, Rio Verde
   - Meta: < 60%

5. **Queries do Search Console (Top 10)**
   - Tabela integrada: Query | Cliques | Impressões | CTR | Posição

6. **Valor Gerado por Tráfego Orgânico**
   - Número único: Receita total de eventos (últimos 30 dias)
   - Comparação: Mês anterior

---

### Métricas Importantes para Monitorar

| Métrica | Meta | Frequência | Ação se Abaixo da Meta |
|---------|------|------------|------------------------|
| **Taxa de Conversão Orgânica** | 3-5% | Semanal | Otimizar CTAs, testar posições de WhatsApp |
| **Tempo Médio de Engajamento** | > 90s | Semanal | Melhorar conteúdo, adicionar FAQs |
| **Taxa de Rejeição** | < 55% | Semanal | Verificar velocidade, mobile-friendly |
| **Conversões de /conhecimento-tecnico/** | 10+ por mês | Mensal | Expandir categorias, adicionar CTAs |
| **Valor por Sessão Orgânica** | R$ 5-10 | Mensal | Revisar valores de evento, qualificar tráfego |
| **Conversões Páginas Regionais** | 50+ por mês | Mensal | Reforçar SEO local, adicionar provas sociais |

---

### Passo 7: Alertas Automáticos (Opcional)

**Configure alertas para:**

1. **Queda de Tráfego Orgânico > 20%**
   - Email: (inserir email webmaster)
   - Verificar: Desindexação, penalização, problemas técnicos

2. **Taxa de Conversão < 2%**
   - Email: (inserir email marketing)
   - Verificar: CTAs, posição de WhatsApp, mobile UX

3. **Aumento de Rejeição > 70%**
   - Email: (inserir email desenvolvedor)
   - Verificar: Erros 404, velocidade, compatibilidade mobile

**Configuração no GA4:**
- Menu: **Admin > Alertas personalizados**
- Criar alerta para cada condição acima

---

### Código de Implementação Completo

**Adicionar no `<head>` de todas as páginas (se ainda não estiver):**

```html
<!-- Google Analytics 4 -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-33VH6XTPZF"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-33VH6XTPZF', {
    'send_page_view': true,
    'anonymize_ip': true
  });
</script>
```

**Adicionar no final do `<body>` (antes de `</body>`):**

```html
<!-- Eventos de Conversão GA4 -->
<script>
// WhatsApp Clicks
const whatsappWidgets = document.querySelectorAll('[id^="whatsAppWidget"]');
whatsappWidgets.forEach((widget, index) => {
  widget.addEventListener('click', function() {
    gtag('event', 'whatsapp_click', {
      'event_category': 'conversao',
      'event_label': 'widget_' + (index + 1),
      'value': 1
    });
  });
});

// Phone Clicks
const telefones = document.querySelectorAll('a[href^="tel:"]');
telefones.forEach(tel => {
  tel.addEventListener('click', function() {
    gtag('event', 'phone_click', {
      'event_category': 'conversao',
      'event_label': this.textContent.trim(),
      'value': 2
    });
  });
});

// Scroll Depth 75%
let scrolled75 = false;
window.addEventListener('scroll', function() {
  const scrollPercent = (window.scrollY / (document.body.scrollHeight - window.innerHeight)) * 100;
  if (scrollPercent > 75 && !scrolled75) {
    scrolled75 = true;
    gtag('event', 'scroll_depth', {
      'event_category': 'engajamento',
      'event_label': '75_percent'
    });
  }
});

// Engaged Session (60s)
setTimeout(function() {
  gtag('event', 'engaged_session', {
    'event_category': 'engajamento',
    'event_label': 'tempo_minimo_60s'
  });
}, 60000);
</script>
```

---

### Checklist de Implementação GA4

- [ ] **Search Console vinculado ao GA4**
- [ ] **Eventos de WhatsApp configurados** (3 widgets)
- [ ] **Eventos de telefone configurados**
- [ ] **Scroll depth implementado**
- [ ] **Engaged session implementado**
- [ ] **Eventos marcados como conversões no GA4**
- [ ] **Valores monetários definidos** (opcional)
- [ ] **Segmentos personalizados criados** (mínimo 2)
- [ ] **Relatório "SEO - Performance" criado**
- [ ] **Dashboard de monitoramento configurado**
- [ ] **Alertas automáticos ativados**
- [ ] **Teste de eventos funcionando** (usar GA4 DebugView)

---

### Teste de Validação (Após Implementação)

1. **DebugView do GA4:**
   - URL: https://analytics.google.com > DebugView
   - Navegue pelo site em modo privado adicionando `?debug=true` na URL
   - Exemplo: `https://www.protoncd.com.br/?debug=true`
   - Clique nos botões de WhatsApp e telefone
   - Verifique se eventos aparecem em tempo real

2. **Teste de Conversão:**
   - Abra o site em modo anônimo
   - Clique em WhatsApp Widget
   - Aguarde 3-5 minutos
   - Verifique: GA4 > Relatórios > Tempo real > Eventos
   - Deve aparecer: `whatsapp_click`

3. **Integração Search Console:**
   - Aguarde 48 horas após vincular
   - Acesse: GA4 > Relatórios > Aquisição > Search Console
   - Deve exibir: Consultas, Landing Pages, Países

---

## ✅ Checklist de Validação

### Antes de Solicitar Reindexação:

- [ ] **Sitemap.xml atualizado** com `<lastmod>` correto
- [ ] **Meta tags validadas**: title (50-60 chars), description (150-160 chars)
- [ ] **Open Graph completo**: og:type, og:url, og:title, og:description, og:locale
- [ ] **Schema JSON-LD válido**: testar em `https://validator.schema.org/`
- [ ] **Canonical URL correto**: `<link rel="canonical" href="...">`
- [ ] **Robots meta**: `<meta name="robots" content="index, follow">`
- [ ] **Links internos funcionando**: verificar cross-linking entre páginas regionais
- [ ] **Mobile-friendly**: testar em `https://search.google.com/test/mobile-friendly`
- [ ] **Page Speed**: > 70 no `https://pagespeed.web.dev/`

### Durante a Reindexação:

- [ ] Registrar timestamp de cada solicitação
- [ ] Screenshot da confirmação "Solicitação enviada"
- [ ] Verificar status em Cobertura após 4 horas
- [ ] Anotar erros ou avisos do Search Console

### Após Indexação (72 horas):

- [ ] Busca `site:protoncd.com.br [titulo-da-pagina]` retorna resultado atualizado
- [ ] Rich snippets aparecem nas SERPs (Schema funcionando)
- [ ] Meta description renderizada corretamente
- [ ] Posições melhoraram para keywords-alvo
- [ ] Nenhum erro 404 ou soft-404 reportado

---

## 🎯 Estratégia de Reindexação por Cenário

### Cenário 1: Atualização de Conteúdo Menor (1-3 páginas)
**Exemplo:** Correção de FAQ, adição de novo serviço em 1 cidade

**Ação:**
1. Editar arquivo(s)
2. Deploy no servidor
3. Método 1: Inspeção individual de URL
4. Tempo: 10 minutos + 24h para indexação

**URLs Prioritárias:**
- Página modificada + homepage (se houver link)

---

### Cenário 2: Atualização de SEO Massiva (4-8 páginas)
**Exemplo:** Adição de playgrounds e olhais em todas páginas regionais

**Ação:**
1. Editar 4 arquivos regionais
2. Atualizar sitemap.xml com `<lastmod>`
3. Deploy no servidor
4. Método 1: Inspeção individual das 4 páginas locais + homepage
5. Método 2: Reenvio de sitemap (backup)
6. Tempo: 20 minutos + 48h para indexação completa

**URLs Prioritárias (ordem de reindexação):**
1. `/goiania/inspecao-predial-goiania.html`
2. `/brasilia/inspecao-predial-brasilia.html`
3. `/anapolis/inspecao-predial-anapolis.html`
4. `/rio-verde/inspecao-predial-rio-verde.html`
5. `/` (homepage - se Schema areaServed foi atualizado)

---

### Cenário 3: Lançamento de Base de Conhecimento (Conteúdo Educacional)
**Exemplo:** Criação de hub de problemas técnicos e soluções (NOVO - 25/12/2025)

**Ação:**
1. Criar `/conhecimento-tecnico/index.html`
2. Adicionar 9 categorias JSON com casos reais
3. Adicionar ao `sitemap.xml` (prioridade 0.88)
4. Adicionar link no menu de navegação principal
5. Implementar Schema.org FAQPage e Article
6. Deploy completo
7. Método 1: Inspeção da página principal + homepage
8. Tempo: 10 minutos + 48-72h para indexação e ranking

**URLs Prioritárias (ordem de reindexação):**
1. `https://www.protoncd.com.br/conhecimento-tecnico/` (NOVO)
2. `/` (homepage com novo link no menu)

**Benefícios Esperados:**
- 📚 Ranqueamento para 50+ long-tail keywords educacionais
- 🎯 Featured snippets tipo "como resolver [problema]"
- 📈 Aumento de 20-30% em tráfego orgânico (30-60 dias)
- 🔗 Backlinks naturais de síndicos/administradoras
- ⭐ Autoridade de domínio E-A-T (Expertise, Authority, Trust)

**Keywords-Alvo (Base Conhecimento):**
- "vibração excessiva elevador condomínio"
- "como resolver problema HVAC"
- "porta corta fogo não fecha sozinha"
- "playground condomínio NBR 16071"
- "vazamento gás predial o que fazer"
- "infiltração laje condomínio"
- "pressurizaçào escada insuficiente"
- "corrosão estrutura metálica"

**Monitoramento Específico:**
- Google Search Console > Desempenho > Filtrar por `/conhecimento-tecnico/`
- Verificar consultas do tipo "como", "o que fazer", "resolver", "problema"
- Monitorar CTR (esperado: 8-12% vs 2-4% páginas comerciais)
- Verificar featured snippets (ferramenta: SEMrush Position Tracking)

---

### Cenário 4: Lançamento de Nova Cidade (1 página nova)
**Exemplo:** Expansão para Aparecida de Goiânia

**Ação:**
1. Criar `/aparecida-goiania/inspecao-predial-aparecida.html`
2. Adicionar ao `sitemap.xml` (prioridade 0.91)
3. Adicionar link em homepage e outras páginas regionais
4. Atualizar Schema `areaServed` na homepage
5. Deploy completo
6. Método 1: Inspeção da nova página + homepage + sitemap
7. Tempo: 15 minutos + 72h para aparecer em buscas locais

**URLs Prioritárias (ordem de reindexação):**
1. `/aparecida-goiania/inspecao-predial-aparecida.html` (NOVO)
2. `/` (homepage com novo link)
3. `/goiania/inspecao-predial-goiania.html` (cross-link)
4. Reenviar sitemap.xml

---

### Cenário 5: Mudança de Estrutura (10+ páginas)
**Exemplo:** Migração de domínio, reorganização de URLs

**Ação:**
1. Implementar 301 redirects (htaccess ou servidor)
2. Atualizar todos canonical URLs
3. Regenerar sitemap.xml completo
4. Método 2: Reenvio de sitemap
5. Método 3: API de Indexação (se disponível)
6. Tempo: 1-2 horas + 7-14 dias para re-ranking completo

**URLs Prioritárias:**
- Todas as páginas na ordem da lista de prioridade acima
- Começar por homepage, depois páginas locais, depois serviços premium

---

## 📞 Suporte e Referências

### Documentação Oficial Google:
- Search Console Help: `https://support.google.com/webmasters`
- Indexing API: `https://developers.google.com/search/apis/indexing-api`
- Schema Markup: `https://developers.google.com/search/docs/appearance/structured-data`

### Ferramentas de Validação:
- **Schema Validator**: `https://validator.schema.org/`
- **Rich Results Test**: `https://search.google.com/test/rich-results`
- **Mobile-Friendly Test**: `https://search.google.com/test/mobile-friendly`
- **PageSpeed Insights**: `https://pagespeed.web.dev/`

### Contatos:
- **Webmaster**: (inserir contato)
- **SEO Manager**: (inserir contato)
- **Suporte Google**: Através do Search Console (ícone "?" > Enviar feedback)

---

## 📝 Registro de Reindexações

### Template de Log:

```
Data: 25/12/2025
Responsável: [Nome]
Motivo: Lançamento da Base de Conhecimento Técnico com 9 categorias
URLs Reindexadas:
  1. /conhecimento-tecnico/ - [hora]
  2. / (homepage - novo link no menu) - [hora]
Método: Inspeção Individual + Atualização Sitemap
Status (72h): [A preencher]
Observações: 9 categorias JSON, Schema FAQPage, 50+ keywords educacionais
Impacto Esperado: +20-30% tráfego orgânico em 30-60 dias
```

**Exemplo anterior:**
```
Data: 24/12/2025
Responsável: [Nome]
Motivo: Adição de serviços playgrounds e olhais em páginas regionais
URLs Reindexadas:
  1. /goiania/inspecao-predial-goiania.html - 14:30
  2. /anapolis/inspecao-predial-anapolis.html - 14:32
  3. /brasilia/inspecao-predial-brasilia.html - 14:34
  4. /rio-verde/inspecao-predial-rio-verde.html - 14:36
Método: Inspeção Individual + Reenvio de Sitemap
Status (72h): [A preencher]
Observações: Schema expandido de 2 para 4 serviços, 8 novos FAQs
```

**Manter histórico em:** Google Sheets ou arquivo CSV para rastreabilidade.

---

## 🚨 Troubleshooting

### Problema 1: "URL não encontrada no Google após 72h"
**Causas:**
- Página bloqueada por robots.txt
- Meta robots com "noindex"
- URL não está no sitemap
- Página não tem links internos

**Solução:**
1. Verificar `https://www.protoncd.com.br/robots.txt` - não deve bloquear URL
2. Inspecionar HTML - remover `<meta name="robots" content="noindex">`
3. Adicionar ao sitemap.xml
4. Adicionar link na homepage ou página relacionada

---

### Problema 2: "Indexada mas não aparece em buscas"
**Causas:**
- Conteúdo duplicado
- Qualidade de conteúdo baixa (thin content)
- Competição alta para keyword
- Penalização manual ou algorítmica

**Solução:**
1. Search Console > Manual Actions - verificar penalizações
2. Verificar canonical tag - não deve apontar para outra URL
3. Enriquecer conteúdo (mínimo 800 palavras)
4. Aguardar 14-30 dias para algoritmo processar

---

### Problema 3: "Rich snippets não aparecem"
**Causas:**
- Schema JSON-LD inválido
- Faltam propriedades obrigatórias
- Tipo de Schema não elegível para rich results

**Solução:**
1. Validar em `https://validator.schema.org/`
2. Testar em `https://search.google.com/test/rich-results`
3. Verificar propriedades obrigatórias: name, @type, address (LocalBusiness)
4. Re-solicitar indexação após correção

---

## 📊 Anexo: Priorização por Valor Agregado

### Cálculo de Valor Agregado:
```
Valor Agregado = (Ticket Médio × Volume Mensal × Taxa Conversão) + (SEO Score × 10)
```

### Ranking Simplificado (escala 1-10):

| Página | Ticket | Volume | Conversão | SEO | **Total** |
|--------|--------|--------|-----------|-----|-----------|
| Homepage | 8 | 10 | 9 | 10 | **10** |
| Goiânia | 8 | 9 | 8 | 9 | **9.5** |
| Brasília | 9 | 7 | 8 | 9 | **9.3** |
| Elevadores 360º | 10 | 8 | 7 | 9 | **9.2** |
| CERCON | 9 | 7 | 8 | 8 | **9.0** |
| HVAC/PMOC | 7 | 10 | 9 | 8 | **9.0** |
| Anápolis | 7 | 8 | 7 | 8 | **8.5** |
| Laudo Pericial | 10 | 5 | 6 | 7 | **8.3** |
| Rio Verde | 7 | 6 | 7 | 8 | **8.0** |
| Gás Predial | 7 | 7 | 7 | 8 | **8.0** |

**Nota:** Valores são estimativas para priorização interna. Ajustar conforme dados reais de Analytics.

---

**Fim do Manual** | Versão 1.0 | Proton Engenharia Mecânica | 24/12/2025
