# 🔧 Guia: Upload para GitHub

Como usar o sistema de upload direto para GitHub via GitHub API.

---

## 📋 Pré-Requisitos

1. **Conta GitHub** (precisa ter permissão no repositório `limageorgio/protoncd`)
2. **Token de Acesso Pessoal** (GitHub Personal Access Token)
3. **Navegador moderno** (Chrome, Firefox, Safari, Edge)

---

## 🔑 Gerar Token GitHub

### Passo 1: Ir para GitHub Settings
```
https://github.com/settings/tokens
```

### Passo 2: Criar novo token
- Clique "Generate new token (classic)"
- Dê um nome descritivo: `ProtonCD Player Upload`

### Passo 3: Escolher escopos
Selecione **apenas** `repo`:
```
✅ repo (Full control of private repositories)
   ├─ repo:status
   ├─ repo_deployment
   ├─ public_repo
   └─ repo:invite
```

### Passo 4: Gerar e copiar
1. Role para baixo
2. Clique "Generate token"
3. **Copie o token** (formato: `ghp_xxxxxxxxxxxxxx`)
4. ⚠️ **Nunca compartilhe esse token**

---

## 🚀 Fazer Upload

### 1. Abrir Interface Admin
```
https://limageorgio.github.io/protoncd/player/admin.html
```

### 2. Preencher Campos

#### Campo: Senha de Administrador
```
trocar_senha_aqui_123
```
(Padrão - altere em admin.html se desejar)

#### Campo: Token de Acesso Pessoal GitHub
```
ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```
(Cole o token que você gerou)

### 3. Selecionar Arquivo HTML
- Clique "Selecione o arquivo HTML"
- Escolha seu arquivo `.html`

### 4. Enviar
- Clique "Validar e Enviar para GitHub"
- Aguarde a barra de progresso completar

---

## ✅ Sucesso!

Após envio bem-sucedido, você receberá:

### 🌐 GitHub Pages URL
```
https://limageorgio.github.io/protoncd/player/seu-arquivo.html
```
**Use esta URL** - é a mais rápida e melhor para compartilhar.

### 📝 GitHub Raw URL
```
https://raw.githubusercontent.com/limageorgio/protoncd/main/player/seu-arquivo.html
```
Use se a primeira não funcionar.

---

## 🔄 Atualizar Arquivo

Para **atualizar um arquivo existente**:

1. Faça o upload com o **mesmo nome do arquivo**
2. O sistema pedirá confirmação
3. Clique "Confirmar"
4. Arquivo será **sobrescrito** no repositório

---

## ⚠️ Troubleshooting

### Erro: "Erro GitHub: 401 Unauthorized"
**Causa:** Token inválido ou expirado

**Solução:**
1. Gere um novo token em https://github.com/settings/tokens
2. Revogue o token antigo
3. Use o novo token

### Erro: "Erro GitHub: 403 Forbidden"
**Causa:** Permissões insuficientes

**Solução:**
1. Verifique se tem permissão no repo `limageorgio/protoncd`
2. Certifique-se de selecionar escopo `repo`
3. Teste com escopo `repo` apenas

### Erro: "Arquivo contém conteúdo suspeito"
**Causa:** Arquivo HTML tem conteúdo malicioso

**Detecção:**
- Scripts `<script>`
- Event handlers `onclick=`
- iframes `<iframe>`
- PHP/ASP tags
- XML processing instructions

**Solução:**
1. Revise o arquivo HTML
2. Remova conteúdo suspeito
3. Tente fazer upload novamente

### Página em branco ou não carrega
**Causa:** GitHub Pages pode levar alguns segundos para publicar

**Solução:**
1. Aguarde 30-60 segundos
2. Recarregue a página (Ctrl+F5)
3. Verifique em incógnito se há cache

---

## 🔐 Segurança

### ✅ O que é seguro
- Token é **usado apenas no seu navegador**
- Nunca é enviado para servidores de terceiros
- Validação ocorre **100% localmente**
- Senha de admin é **hasheada com SHA-256**

### ⚠️ Boas práticas
- **Não compartilhe seu token**
- **Use tokens com escopo limitado** (apenas `repo`)
- **Revogue tokens antigos** após gerar novos
- **Considere usar Fine-grained tokens** (beta) para mais controle

---

## 📊 Exemplos

### Exemplo 1: Upload simples
```
Arquivo: player-novo.html
Tamanho: 150 KB
Token: ghp_xxxx...
Resultado: https://limageorgio.github.io/protoncd/player/player-novo.html
```

### Exemplo 2: Atualizar arquivo
```
Arquivo: player-novo.html (já existe)
Ação: Sobrescrever
Resultado: Versão anterior é substituída
```

---

## 🔗 Links Úteis

- **GitHub Token Settings:** https://github.com/settings/tokens
- **Documentação GitHub API:** https://docs.github.com/rest
- **GitHub Pages Docs:** https://pages.github.com

---

## 💡 Dicas

1. **Copie a URL:** Use o botão "Copiar" após upload bem-sucedido
2. **Teste antes:** Use `validate-html.js` localmente antes de enviar
3. **Nomeie bem:** Use nomes descritivos e sem espaços
4. **Versione:** Considere adicionar versão no nome (ex: `player-v1.html`)
5. **Documente:** Mantenha registro de arquivos enviados

---

**Última atualização:** 5 de janeiro de 2026  
**Versão:** 1.0  
**Status:** ✅ Pronto para uso
