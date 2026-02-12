# Manual de Indexação da Base de Conhecimento Técnico

## Objetivo
Garantir que a página **/conhecimento-tecnico/** e seus conteúdos sejam descobertos, rastreados e indexados pelos mecanismos de busca, especialmente o Google.

---

## Visão Geral dos Ajustes já Implementados
- Link direto para a base de conhecimento adicionado no menu principal e no herói da home page (arquivo `index.html`).
- Entrada específica criada no `sitemap.xml` com `lastmod` atualizado para facilitar o rastreamento.
- Página serve conteúdo via JSON embutido, mantendo acesso mesmo quando o site é aberto localmente.

> **Observação:** Sempre que houver alterações relevantes (novas FAQs, categorias ou conteúdos), repita a rotina abaixo para acelerar a reindexação.

---

## Pré-requisitos
1. Acesso ao Google Search Console da propriedade `https://www.protoncd.com.br/`.
2. Permissão para publicar os arquivos atualizados no servidor de produção.
3. Navegador com modo "Análise de URL" disponível (Google Chrome recomendado).

---

## Passo a Passo para Reforçar a Indexação

### 1. Publicar os Arquivos
- Envie para o servidor os seguintes arquivos atualizados:
  - `index.html`
  - `conhecimento-tecnico/index.html`
  - `sitemap.xml`
- Limpe o cache do CDN/servidor, se existir.

### 2. Validar Acessibilidade
1. Acesse `https://www.protoncd.com.br/` e confirme se os links "Base de Conhecimento" (menu superior e botão no herói) direcionam corretamente para `https://www.protoncd.com.br/conhecimento-tecnico/`.
2. Abra `https://www.protoncd.com.br/conhecimento-tecnico/` e verifique se o conteúdo carrega normalmente (cards de categorias e FAQs). Utilize o console para garantir ausência de erros de JS.

### 3. Atualizar o Sitemap no Search Console
1. Entre no [Google Search Console](https://search.google.com/search-console).
2. Na propriedade do domínio, acesse **Sitemaps**.
3. Em "Adicionar um novo sitemap", digite `sitemap.xml` e clique em **Enviar** (mesmo já cadastrado, isso força reprocessamento).
4. Aguarde a confirmação do status **"Sucesso"**.

### 4. Solicitar Indexação da Página
1. Ainda no Search Console, abra **Inspeção de URL**.
2. Cole `https://www.protoncd.com.br/conhecimento-tecnico/` e pressione Enter.
3. Clique em **"Testar URL ativa"**.
4. Se o status indicar "URL não está no Google" ou "Cobertura desconhecida", clique em **Solicitar indexação**.
5. Aguarde a confirmação de que o pedido foi enviado.
6. Repita a inspeção para garantir que o Google consegue renderizar o conteúdo (se houver aviso de recursos bloqueados, verifique `robots.txt`).

### 5. Monitorar Cobertura e Desempenho
- Após alguns dias, acesse **Cobertura** → **Páginas** no Search Console e filtre por `conhecimento-tecnico`.
- Verifique se a URL aparece como **Indexada**. Caso contrário, revise logs para ver se existem erros de rastreamento.
- Em **Resultados de pesquisa**, crie um filtro por Página para monitorar impressões e cliques da base de conhecimento.

### 6. Boas Práticas Contínuas
1. **Sempre que atualizar as FAQs**:
   - Ajuste `sitemap.xml` com nova data no campo `<lastmod>`.
   - Suba os arquivos `conhecimento-tecnico/dados/*.json` e `conhecimento-tecnico/index.html`.
   - Repita os passos 3 e 4.
2. **Interligue conteúdos**:
   - Quando publicar artigos ou páginas de serviço relevantes, inclua links para seções da base de conhecimento.
3. **Structured Data (opcional avançado)**:
   - Avaliar implantação de marcação `FAQPage` segmentada por categoria usando `<script type="application/ld+json">` gerado server-side.
   - Testar no [Rich Results Test](https://search.google.com/test/rich-results) antes de publicar.
4. **Monitoramento técnico**:
   - Verificar periodicamente se o JavaScript carrega sem erros na página da base usando o modo "Ver código-fonte renderizado" do Search Console.

---

## Checklist Rápido
- [ ] Arquivos publicados em produção.
- [ ] Link interno funcionando na home.
- [ ] Sitemap reenviado.
- [ ] Solicitação de indexação realizada.
- [ ] Cobertura monitorada após 3 a 7 dias.

---

## Contatos e Ferramentas Úteis
- Google Search Console: <https://search.google.com/search-console>
- Teste de URL: `Ctrl + Shift + I` (DevTools) para verificar erros de console.
- Validator XML Sitemap: <https://www.xml-sitemaps.com/validate-xml-sitemap.html>
- Rich Results Test: <https://search.google.com/test/rich-results>

---

> **Recomendação:** mantenha este manual versionado no repositório para que futuros ajustes na base de conhecimento sigam a mesma rotina de indexação.
