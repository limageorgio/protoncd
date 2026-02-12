# 📘 Manual Completo: Google Search Console e Ferramentas SEO

## 🎯 Objetivo
Este manual ensina passo a passo como configurar e otimizar o site da Proton Engenharia nas principais ferramentas de SEO para garantir máxima visibilidade nos mecanismos de busca.

---

## 📋 Índice
1. [Google Search Console](#1-google-search-console)
2. [Google Analytics](#2-google-analytics)
3. [Google Meu Negócio (Google Business Profile)](#3-google-meu-negócio)
4. [Bing Webmaster Tools](#4-bing-webmaster-tools)
5. [Schema.org Validator](#5-schemaorg-validator)
6. [Checklist de Verificação](#6-checklist-de-verificação)

---

## 1. Google Search Console

### 📌 O que é?
Ferramenta gratuita do Google que monitora e mantém a presença do seu site nos resultados de pesquisa.

### ✅ Passo a Passo

#### **1.1 Acessar o Google Search Console**
1. Acesse: https://search.google.com/search-console
2. Faça login com uma conta Google (usar conta empresarial se possível)
3. Clique em **"Adicionar propriedade"**

#### **1.2 Adicionar a Propriedade**
Você tem duas opções:

**Opção A - Domínio (Recomendado)**
- Selecione "Domínio"
- Digite: `protoncd.com.br`
- Clique em **Continuar**

**Opção B - Prefixo do URL**
- Selecione "Prefixo do URL"
- Digite: `https://www.protoncd.com.br`
- Clique em **Continuar**

#### **1.3 Verificar a Propriedade**

**Método 1: Verificação por DNS (Mais Seguro - Recomendado)**
1. O Google fornecerá um código TXT
2. Acesse o painel de controle do seu domínio (Registro.br, HostGator, etc.)
3. Vá em **"Gerenciar DNS"** ou **"Zona DNS"**
4. Adicione um novo registro:
   - **Tipo:** TXT
   - **Nome/Host:** @ ou deixe em branco
   - **Valor:** Cole o código fornecido pelo Google
   - **TTL:** 3600 (ou deixe padrão)
5. Clique em **Salvar**
6. Volte ao Google Search Console e clique em **"Verificar"**
   - Pode levar até 24 horas, mas geralmente é instantâneo

**Método 2: Upload de Arquivo HTML**
1. Baixe o arquivo HTML fornecido pelo Google (ex: `google1234567890abcdef.html`)
2. Faça upload deste arquivo na raiz do seu site via FTP/SFTP
   - Caminho: `public_html/` ou `www/`
3. Verifique se está acessível: `https://www.protoncd.com.br/google1234567890abcdef.html`
4. Volte ao Google Search Console e clique em **"Verificar"**

**Método 3: Tag HTML no `<head>`**
1. Copie o código meta tag fornecido
2. Abra o arquivo `index.html` do site
3. Cole o código dentro da tag `<head>`, antes do `</head>`
   ```html
   <meta name="google-site-verification" content="SEU-CODIGO-AQUI" />
   ```
4. Salve e faça upload do arquivo
5. Volte ao Google Search Console e clique em **"Verificar"**

#### **1.4 Enviar o Sitemap**
1. Após verificação bem-sucedida, no menu lateral clique em **"Sitemaps"**
2. No campo "Adicionar um novo sitemap", digite: `sitemap.xml`
3. Clique em **"Enviar"**
4. Status deve aparecer como **"Sucesso"** em alguns minutos

#### **1.5 Solicitar Indexação de URLs Importantes**
1. No menu lateral, clique em **"Inspeção de URL"**
2. Cole a URL completa (ex: `https://www.protoncd.com.br/cercon-goias.html`)
3. Clique em **"Testar URL ativa"**
4. Se não estiver indexada, clique em **"Solicitar indexação"**
5. Repita para as páginas mais importantes:
   - `/index.html` (ou `/`)
   - `/cercon-goias.html`
   - `/inspecao-hvac-pmoc.html`
   - `/analise-vibracao-elevadores.html`
   - `/teste-arrancamento-olhais.html`

#### **1.6 Configurações Importantes**
1. **Configurações → Informações de propriedade**
   - Proprietário: Seu email
   - Data de verificação: Automática
2. **Experiência → Usabilidade em dispositivos móveis**
   - Verificar se não há erros
3. **Melhorias → Dados estruturados**
   - Verificar se Schema.org está sendo reconhecido

---

## 2. Google Analytics

### 📌 O que é?
Ferramenta de análise de tráfego e comportamento dos visitantes do site.

### ✅ Passo a Passo

#### **2.1 Verificar se já está instalado**
✅ **SEU SITE JÁ TEM GOOGLE ANALYTICS INSTALADO!**
- ID de acompanhamento: `G-33VH6XTPZF`
- Google Tag Manager: `GTM-5NNLDWJX`

#### **2.2 Acessar o Google Analytics**
1. Acesse: https://analytics.google.com
2. Faça login com a mesma conta Google usada no Search Console
3. Você deve ver a propriedade "Proton Engenharia" ou similar
4. Se não aparecer, solicite acesso ao proprietário da conta

#### **2.3 Configurações Importantes**
1. **Administração → Informações de propriedade**
   - Nome: Proton Engenharia
   - Fuso horário: (UTC-03:00) Brasília
   - Moeda: Real (BRL)

2. **Administração → Configurações de dados**
   - Coleta de dados: Ativada ✓
   - Melhorar a precisão dos dados: Ativada ✓

3. **Eventos → Todos os eventos**
   - Configurar eventos personalizados:
     - `whatsapp_click` (clique no botão WhatsApp)
     - `form_submit` (envio de formulário)
     - `phone_click` (clique no telefone)

#### **2.4 Vincular ao Search Console**
1. No Google Analytics: **Administração → Links do Search Console**
2. Clique em **"Vincular"**
3. Selecione a propriedade `www.protoncd.com.br`
4. Clique em **"Confirmar"**
5. Clique em **"Enviar"**

---

## 3. Google Meu Negócio (Google Business Profile)

### 📌 O que é?
Perfil comercial que aparece no Google Maps e nas pesquisas locais.

### ✅ Passo a Passo

#### **3.1 Criar/Reivindicar o Perfil**
1. Acesse: https://business.google.com
2. Faça login com conta Google
3. Clique em **"Gerenciar agora"** ou **"Adicionar empresa"**

#### **3.2 Informações Básicas**
```
Nome da empresa: Proton Engenharia - Inspeção Predial Goiânia
Categoria principal: Engenheiro Mecânico
Categorias adicionais:
  - Serviços de engenharia
  - Consultoria de engenharia
  - Engenheiro
```

#### **3.3 Endereço**
**Se tiver endereço físico:**
```
Rua/Avenida: [Seu endereço]
Cidade: Goiânia
Estado: GO
CEP: [Seu CEP]
País: Brasil
```

**Se for home office ou não atender no local:**
- Marque "Não tenho um endereço com atendimento ao cliente"
- Defina área de atendimento: Goiânia, Anápolis, Brasília, etc.

#### **3.4 Informações de Contato**
```
Telefone: +55 62 99285-2704
WhatsApp: +55 62 99285-2704
Website: https://www.protoncd.com.br
Email: lima.georgio.eng@gmail.com
```

#### **3.5 Horário de Funcionamento**
```
Segunda a Sexta: 08:00 - 18:00
Sábado: 08:00 - 12:00
Domingo: Fechado
```

#### **3.6 Descrição (750 caracteres)**
```
A Proton Engenharia é especialista em inspeção predial de sistemas mecânicos em todo Brasil, com base em Goiânia-GO. Oferecemos laudos técnicos com ART do CREA para HVAC/PMOC (Lei 13.589), análise de vibração em elevadores, sistemas de combate a incêndio, renovação de CERCON/AVCB, inspeção de gás predial, casa de bombas, pressurização de escadas, playgrounds NBR 16071 e teste de arrancamento de olhais (NR-35). Atendemos condomínios, empresas e órgãos públicos em Goiás, Brasília, São Paulo, Rio de Janeiro e demais estados. Engenharia Mecânica com precisão e tecnologia 360º exclusiva.
```

#### **3.7 Verificação**
1. Google enviará uma carta com código PIN (10-14 dias) OU
2. Verificação por telefone/email se disponível
3. Insira o código no painel quando receber
4. Perfil ficará verificado ✓

#### **3.8 Fotos (IMPORTANTE!)**
Faça upload de pelo menos 10 fotos:
- Logo da empresa (quadrada, 720x720px)
- Foto de capa (1024x576px)
- Equipamentos (dinamômetro, medidores, etc.)
- Equipe realizando inspeções
- Laudos/certificados (sem dados sensíveis)
- Projetos/obras concluídas
- Escritório (se aplicável)

#### **3.9 Posts Semanais**
Crie posts regulares (1-2 por semana):
- "Prazo de digitalização do CERCON até 2027 - NT 01/2025 CBMGO"
- "Inspeção de elevadores: como evitar ruídos e vibrações"
- "PMOC obrigatório: evite multas de até R$ 1,5 milhão"
- "Renovação de AVCB em Goiânia: documentos necessários"

---

## 4. Bing Webmaster Tools

### 📌 O que é?
Ferramenta da Microsoft (Bing) similar ao Google Search Console.

### ✅ Passo a Passo

#### **4.1 Acessar o Bing Webmaster**
1. Acesse: https://www.bing.com/webmasters
2. Faça login com conta Microsoft (ou crie uma)
3. Clique em **"Adicionar um site"**

#### **4.2 Importar do Google Search Console (RÁPIDO)**
1. Clique em **"Importar do Google Search Console"**
2. Autorize o acesso
3. Selecione `www.protoncd.com.br`
4. Clique em **"Importar"**
5. Pronto! Sitemap e configurações serão copiadas automaticamente

#### **4.3 Método Manual (alternativo)**
1. Digite o URL: `https://www.protoncd.com.br`
2. Adicione o sitemap: `https://www.protoncd.com.br/sitemap.xml`
3. Verifique por:
   - Upload de arquivo XML
   - Meta tag no HTML
   - DNS CNAME
4. Envie

#### **4.4 Configurações**
- **Configurar → Sitemap**: Verificar se `sitemap.xml` foi detectado
- **Relatórios → Páginas indexadas**: Monitorar crescimento
- **Diagnósticos → Rastreamento**: Verificar erros

---

## 5. Schema.org Validator

### 📌 O que é?
Validador de dados estruturados (Rich Snippets) para melhorar exibição nos resultados de busca.

### ✅ Passo a Passo

#### **5.1 Testar Dados Estruturados**
1. Acesse: https://validator.schema.org
2. Cole a URL: `https://www.protoncd.com.br/cercon-goias.html`
3. Clique em **"Run Test"**
4. Verifique se aparecem sem erros:
   - ✓ Service (Serviço)
   - ✓ LocalBusiness (Empresa)
   - ✓ FAQPage (Perguntas Frequentes)
   - ✓ BreadcrumbList (Navegação)

#### **5.2 Teste de Resultado Rico do Google**
1. Acesse: https://search.google.com/test/rich-results
2. Cole a URL: `https://www.protoncd.com.br`
3. Clique em **"Testar URL"**
4. Verificar resultados:
   - ✓ Sem erros críticos
   - ✓ Dados estruturados detectados
   - ⚠️ Avisos (podem ser ignorados se não forem críticos)

---

## 6. Checklist de Verificação

### ✅ Google Search Console
- [ ] Propriedade adicionada e verificada
- [ ] Sitemap.xml enviado e aceito
- [ ] URLs principais solicitadas para indexação
- [ ] Vinculado ao Google Analytics
- [ ] Monitoramento de erros configurado

### ✅ Google Analytics
- [ ] Código de rastreamento instalado (já está!)
- [ ] Propriedade configurada
- [ ] Eventos personalizados criados
- [ ] Vinculado ao Search Console

### ✅ Google Meu Negócio
- [ ] Perfil criado/reivindicado
- [ ] Informações completas preenchidas
- [ ] 10+ fotos adicionadas
- [ ] Verificação solicitada/concluída
- [ ] Postagens semanais agendadas

### ✅ Bing Webmaster Tools
- [ ] Site adicionado
- [ ] Sitemap enviado
- [ ] Verificação concluída
- [ ] Sem erros críticos

### ✅ Schema.org / Rich Snippets
- [ ] Dados estruturados testados
- [ ] Sem erros críticos
- [ ] FAQPage configurada
- [ ] LocalBusiness configurado

---

## 📊 Monitoramento Contínuo

### Diário
- [ ] Verificar posicionamento de palavras-chave principais no Google

### Semanal
- [ ] Criar 1-2 posts no Google Meu Negócio
- [ ] Responder avaliações (se houver)
- [ ] Verificar erros no Search Console

### Mensal
- [ ] Revisar relatório de desempenho do Search Console
- [ ] Analisar tráfego no Google Analytics
- [ ] Atualizar sitemap.xml se houver novas páginas
- [ ] Verificar posição de palavras-chave (Google Search Console)

---

## 🆘 Suporte

### Problemas Comuns

**1. "Sitemap não pode ser lido"**
- Verificar se `sitemap.xml` está acessível: https://www.protoncd.com.br/sitemap.xml
- Validar XML em: https://www.xml-sitemaps.com/validate-xml-sitemap.html
- Verificar permissões do arquivo (644)

**2. "URL não indexada"**
- Aguardar 1-2 semanas após solicitar indexação
- Verificar se `robots.txt` não está bloqueando
- Verificar se página tem conteúdo suficiente (300+ palavras)

**3. "Propriedade não verificada"**
- Verificar se arquivo HTML não foi deletado
- Verificar se meta tag está no `<head>`
- Verificar DNS (pode levar até 24h)

**4. "Dados estruturados com erros"**
- Usar validador: https://validator.schema.org
- Corrigir erros no código Schema.org
- Re-enviar sitemap após correção

---

## 📞 Contatos Úteis

**Google Search Console Ajuda:**
https://support.google.com/webmasters

**Google Analytics Ajuda:**
https://support.google.com/analytics

**Google Meu Negócio Ajuda:**
https://support.google.com/business

**Bing Webmaster Ajuda:**
https://www.bing.com/webmasters/help

---

## 🎯 Próximos Passos (Avançado)

1. **Backlinks de Qualidade**
   - Cadastrar em diretórios: CREA, sindicatos, associações
   - Parcerias com administradoras de condomínios
   - Guest posts em blogs de engenharia

2. **Conteúdo Regular (Blog)**
   - Criar seção de blog no site
   - Publicar 2-4 artigos por mês
   - Temas: CERCON, PMOC, elevadores, NRs, NBRs

3. **Redes Sociais**
   - LinkedIn empresarial
   - Instagram com cases e bastidores
   - Facebook com posts educativos

4. **Anúncios Pagos (Opcional)**
   - Google Ads para palavras-chave estratégicas
   - Facebook/Instagram Ads para região de Goiânia
   - Remarketing para visitantes do site

---

**Data de Criação:** 21/12/2025  
**Última Atualização:** 21/12/2025  
**Versão:** 1.0
