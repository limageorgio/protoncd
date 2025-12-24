# Guia Prático de Melhoria SEO, UX e Conteúdo

## Objetivo
Fornecer diretrizes concretas para transformar o site da Proton Engenharia em referência nacional em inspeções prediais e serviços técnicos correlatos, com foco em ranquear organicamente por cidade, serviço e intenção de busca.

---

## 1. Arquitetura de Conteúdo
- **Páginas Pilares por Serviço:** Cada serviço principal deve possuir página própria longa (800–1.200 palavras) com: contexto legal, riscos, passo a passo, diferenciais tecnológicos, FAQ.
- **Páginas Locais:** Criar páginas por região prioritária (Goiânia, Anápolis, Rio Verde, Brasília) reutilizando a estrutura de serviços, porém com legislação, exemplos e clientes locais.
- **Serviços Não Prediais:** Manter rotas individuais para análises industriais, perícias e consultorias, interligando-as às páginas prediais via seções “Serviços Complementares”.
- **Blog/Guia Técnico:** Reservar espaço para artigos que respondam dúvidas comuns (ex.: "Como regularizar o PMOC atrasado"), alimentando a autoridade temática.

## 2. SEO On-Page
- **URLs Amigáveis:** Remover extensões `.html` na publicação. Estrutura recomendada: `/servicos/inspecao-hvac`, `/goiania/inspecao-predial`.
- **Headings Hierárquicos:** Um único `H1` com palavra-chave central. `H2` e `H3` para dúvidas e sub-serviços.
- **Metadados:** Titles < 60 caracteres + CTAs fortes. Descriptions 150–160 caracteres com intenção local.
- **Schema JSON-LD:** Utilizar `ProfessionalService`, `Service`, `FAQPage` e `Review` quando houver depoimentos. Atualizar sempre que abrir nova praça.

## 3. Experiência do Usuário & Acessibilidade
- **Contraste e Legibilidade:** Evitar texto claro sobre fundo claro. Utilizar checker WCAG para garantir AA.
- **Componentes Reutilizáveis:** Consolidar botões WhatsApp em menu único acessível e responsivo.
- **Imagens Otimizadas:** Preferir `.webp` com `loading="lazy"` e textos alternativos descritivos.
- **Formulários Inclusivos:** Labels vinculados, placeholders informativos, instruções visuais e auditivas.

## 4. Core Web Vitals
- **LCP (Largest Contentful Paint):** Priorizar carregamento da imagem hero de cada página com `fetchpriority="high"`.
- **JS & CSS:** Minificar e diferir scripts não críticos (parallax, jQuery). Usar CSS crítico inline < 14 KB.
- **Media Queries Mobile First:** Garantir layout fluido em telas de 320px sem elementos sobrepostos.

## 5. Linkagem Interna Planejada
- **Menus e Rodapés:** Incluir rotas para cada cidade alvo e serviços não prediais.
- **Callouts nos Textos:** Inserir caixas "Serviços Conectados" com links para inspeção de bombas, combate a incêndio, etc.
- **Breadcrumbs Opcional:** Para páginas locais, seguir padrão `/Serviços > Inspeção Predial > Goiânia`.

## 6. Conteúdo Comercial
- **Pacotes de Sistemas Mecânicos:** Destaque os descontos combinados (HVAC + Elevadores + Bombas). Explicar cenários de economia e compliance.
- **Parcerias Multidisciplinares:** Inserir seção discreta destacando rede de parceiros (elétrica, estrutural, incêndio) garantindo cobertura total.
- **CTA Estratégico:** Botões com benefício (“Agendar diagnóstico em Goiânia”) + opção de contato multicanal.

## 7. Governança e Atualização
- **Sitemap e Robots:** Atualizar `sitemap.xml` a cada nova página. Manter `robots.txt` liberado para `/goiania/*`, `/anapolis/*`, etc.
- **Analytics:** Configurar GA4 e Google Search Console para monitorar performance por URL e query local.
- **Revisão Periódica:** Checklists trimestrais para rever leis, normas técnicas e depoimentos.

---

## Próximos Passos Operacionais
1. Criar páginas de destino locais utilizando o layout base deste repositório (ver `/goiania/inspecao-predial-goiania.html`, etc.).
2. Ajustar links internos em `index.html`, `landing-servicos.html` e rodapé para apontar para novas páginas.
3. Expandir metadados e Schema conforme seções indicadas.
4. Monitorar indexação no Search Console, realizando submissão manual quando necessário.

> Use este guia como checklist durante as implementações. Ajustes adicionais devem ser registrados nesta mesma file para garantir rastreabilidade.
