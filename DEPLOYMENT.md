# 🚀 Instruções de Deployment - Página CERCON Goiás

## ✅ Arquivos Criados/Modificados

### Novos Arquivos
- **cercon-goias.html** - Landing page de alta conversão para renovação de CERCON em Goiás

### Arquivos Atualizados
- **index.html** - Adicionados 2 links para a página CERCON (card destaque + lista "Outras atuações")
- **sitemap.xml** - Adicionada nova página com prioridade 0.95
- **robots.txt** - Permitido acesso à nova página

---

## 📋 Checklist de Deployment

### 1. Testar Localmente ✓
```bash
cd h:\apps\protoncd
python -m http.server 8000
```
Acesse: http://localhost:8000/cercon-goias.html

### 2. Validar Conteúdo
- [ ] Verificar se todas as seções estão visíveis
- [ ] Testar formulário de contato (deve abrir WhatsApp)
- [ ] Verificar links de navegação
- [ ] Testar responsividade mobile
- [ ] Conferir ortografia e gramática

### 3. Git Commit e Push
```bash
cd h:\apps\protoncd
git add .
git commit -m "feat: adiciona landing page CERCON Goiás com SEO completo e integração NT 01/2025"
git push origin main
```

### 4. Aguardar Deploy Automático do GitHub Pages
- GitHub Pages faz deploy automático após push
- Aguarde 2-5 minutos
- Acesse: https://www.protoncd.com.br/cercon-goias.html

### 5. Google Search Console
Após deploy, submeta nova página:
1. Acesse: https://search.google.com/search-console
2. Vá em "Inspeção de URL"
3. Cole: https://www.protoncd.com.br/cercon-goias.html
4. Clique em "Solicitar Indexação"
5. Aguarde 24-48h para indexação completa

Alternativamente, submeta o sitemap atualizado:
- URL do sitemap: https://www.protoncd.com.br/sitemap.xml

---

## 🎯 Características da Página CERCON

### SEO Otimizado
- ✅ Meta tags (title, description, keywords)
- ✅ Open Graph (Facebook/LinkedIn)
- ✅ Twitter Cards
- ✅ Schema.org JSON-LD (Service + LocalBusiness)
- ✅ Geo tags (Goiânia, Goiás)
- ✅ Canonical URL

### Conteúdo Estratégico
- ✅ Headline de conversão
- ✅ Seção de URGÊNCIA destacada (NT 01/2025 - prazo 01/01/2027)
- ✅ 4 serviços detalhados (CERCON, Digitalização, Inspeções, Predial)
- ✅ Perfil do Eng. Georgio Lima
- ✅ Formulário de contato integrado com WhatsApp
- ✅ WhatsApp widget flutuante

### Terminologia Correta
- ✅ Usa "CERCON" (correto para Goiás)
- ✅ Menciona "AVCB/CLCB" apenas como referência genérica
- ✅ Destaca NT 01/2025 do CBMGO
- ✅ Enfatiza prazo legal de digitalização

### Design Responsivo
- ✅ Mobile-first
- ✅ Parallax scrolling
- ✅ Smooth scroll navigation
- ✅ Cores da marca (#006666 verde Proton)
- ✅ Animações CSS (pulse-border)

---

## 📊 Monitoramento

### Google Analytics
Acompanhe métricas em: https://analytics.google.com
- Visualizações de página
- Taxa de conversão (cliques em WhatsApp)
- Tempo médio na página
- Taxa de rejeição

### Google Tag Manager
ID: GTM-5NNLDWJX (já integrado)
ID Analytics: G-66FH56TVDP (já integrado)

---

## 🔗 Links Importantes

- **Página Principal:** https://www.protoncd.com.br/
- **Página CERCON:** https://www.protoncd.com.br/cercon-goias.html
- **Página Elevadores:** https://www.protoncd.com.br/analise-vibracao-elevadores.html
- **WhatsApp Georgio:** https://api.whatsapp.com/send?phone=5562992852704

---

## 📱 WhatsApp de Contato

**Eng. Georgio Batista de Lima**
- Telefone: +55 (62) 99285-2704
- Mensagem automática: "Olá Eng.Georgio, preciso de orçamento para renovação de CERCON!"

---

## 🎨 Imagens Utilizadas

- **Hero Section:** img/eng_fundo_azul.png
- **Seção Urgência:** img/antique-cafe-bg-02.jpg
- **Seção Serviços:** img/montagem1.jpg
- **Seção Time:** img/eng_fundo_calculos.jpg
- **Seção Contato:** img/projeto.jpg
- **Perfil Georgio:** img/Georgio_lima.jpg

---

## 📝 Próximos Passos Sugeridos

1. **Campanhas Google Ads:**
   - Palavras-chave: "renovação cercon goiânia", "digitalização projetos incêndio", "nt 01/2025"
   - Região: Goiânia, Anápolis, Aparecida de Goiânia

2. **Marketing de Conteúdo:**
   - Blog posts sobre NT 01/2025
   - Infográfico sobre prazo de digitalização
   - Vídeo explicativo sobre o processo

3. **Redes Sociais:**
   - Compartilhar página em grupos de síndicos do Facebook
   - Posts no Instagram/LinkedIn sobre urgência da NT 01/2025
   - Stories com depoimentos de clientes

4. **Email Marketing:**
   - Newsletter para condomínios em Goiânia
   - Template destacando prazo legal

---

**Página criada em:** 05/12/2025  
**Última atualização:** 05/12/2025  
**Status:** ✅ Pronta para deploy
