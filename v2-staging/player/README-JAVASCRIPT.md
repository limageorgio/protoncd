# 🎬 Pasta Player - ProtonCD

Sistema seguro **100% JavaScript** para upload de players HTML direto no GitHub.

---

## 📌 O Que É

Repositório isolado para hospedar players HTML validados com:
- 🎥 Análise de elevadores e estruturas
- 📊 Visualizadores técnicos
- 📄 Apresentações interativas
- 🎨 Demonstrações

Todos os arquivos são **validados no navegador**, enviados direto para o **GitHub** via API, e acessíveis automaticamente pelo **GitHub Pages**.

---

## 🚀 Como Usar

### 1. Acessar Interface Admin
```
https://limageorgio.github.io/protoncd/player/admin.html
```

### 2. Autenticar com Senha Admin
```
Senha padrão: trocar_senha_aqui_123
(Altere em admin.html linha ~381 - ADMIN_PASSWORD)
```

### 3. Adicionar Token GitHub
1. Acesse https://github.com/settings/tokens
2. Clique "Generate new token (classic)"
3. Habilite escopo: `repo`
4. Copie o token (começa com `ghp_`)
5. Cole em "Token de Acesso Pessoal GitHub"

### 4. Fazer Upload
1. Selecione arquivo `.html`
2. Clique "Validar e Enviar para GitHub"
3. Arquivo é validado no navegador
4. Enviado via GitHub API REST
5. Cria commit automático
6. Gera 2 URLs de acesso

### 5. Acessar Arquivo Publicado
```
https://limageorgio.github.io/protoncd/player/seu-arquivo.html
```

---

## 🔐 Segurança

### ✅ Validações Implementadas
- Extensão `.html` obrigatória
- Tamanho máximo: 5MB
- Detecção de scripts maliciosos
- Bloqueio de event handlers suspeitos
- Bloqueio de iframes e embeds
- Bloqueio de PHP/ASP tags
- Autenticação SHA-256
- **Validação ocorre 100% no navegador** (zero exposição no servidor)

---

## 📂 Estrutura

```
player/
├── admin.html                    ← Interface de upload (100% JS)
├── validate-html.js              ← Validador JavaScript
├── player-torre-c1-2.html        ← Exemplo
├── .htaccess                     ← Segurança Apache
├── JAVASCRIPT-VERSAO.md          ← Guia técnico
├── JAVASCRIPT-IMPLEMENTACAO.md   ← Detalhes implementação
├── GUIA-RAPIDO.md               ← Manual rápido
└── README-JAVASCRIPT.md          ← Este arquivo
```

---

## 🔧 Configuração

### Alterar Senha Admin

Edite [admin.html](admin.html) linha ~381:

```javascript
const ADMIN_PASSWORD = 'SUA_SENHA_FORTE!';
```

### GitHub Configuration

A configuração do GitHub está no admin.html (linhas ~385-388):

```javascript
const GITHUB_OWNER = 'limageorgio';
const GITHUB_REPO = 'protoncd';
const GITHUB_BRANCH = 'main';
const GITHUB_FOLDER = 'player';
```

---

## 🧪 Testar Arquivo Localmente

```bash
# Validar antes de fazer upload
node validate-html.js seu-arquivo.html

# Resultado esperado
✅ RESULTADO: ARQUIVO PASSOU EM TODAS AS VALIDAÇÕES
```

---

## 📊 Fluxo de Upload

```
1. Usuário acessa admin.html
   ↓
2. Autentica com senha (SHA-256)
   ↓
3. Fornece token GitHub
   ↓
4. Seleciona arquivo .html
   ↓
5. Validações no cliente (JavaScript)
   ↓
6. Detecta conteúdo malicioso?
   ├─ SIM → Rejeita arquivo
   └─ NÃO → Faz upload via GitHub API
   ↓
7. GitHub cria commit
   ↓
8. GitHub Pages publica automaticamente
   ↓
9. Gera 2 URLs (Pages + Raw)
```

---

## 🌐 URLs de Acesso

Após upload bem-sucedido, você recebe 2 URLs:

### 🎯 GitHub Pages (Recomendado)
```
https://limageorgio.github.io/protoncd/player/seu-arquivo.html
```
- ✅ Melhor performance
- ✅ Incluído em GitHub Pages
- ✅ Atualiza em segundos

### 📝 GitHub Raw Content
```
https://raw.githubusercontent.com/limageorgio/protoncd/main/player/seu-arquivo.html
```
- ✅ Sempre o arquivo mais recente
- ✅ Sem processamento
- ✅ Pode ser mais lento

---

## 📚 Documentação

| Documento | Descrição |
|-----------|-----------|
| **JAVASCRIPT-VERSAO.md** | Guia técnico completo |
| **JAVASCRIPT-IMPLEMENTACAO.md** | Detalhes da implementação |
| **GUIA-RAPIDO.md** | Manual para usuários |
| **admin.html** | Interface de upload |
| **validate-html.js** | Validador (Node.js ou navegador) |

---

## ⚠️ O Que Fazer

### ✅ Permitido
- Arquivos HTML válidos
- Imagens, vídeos, CSS
- Conteúdo sem malware

### ❌ Bloqueado
- Scripts `<script>`
- Event handlers `onclick=`
- iframes `<iframe>`
- PHP/ASP tags
- Código malicioso

---

## 🌐 Compatibilidade

| Navegador | Suporte |
|-----------|---------|
| Chrome | ✅ 37+ |
| Firefox | ✅ 32+ |
| Safari | ✅ 11+ |
| Edge | ✅ 79+ |
| IE | ❌ Não |

---

## 🎯 Começar Agora

1. **Abra:** https://limageorgio.github.io/protoncd/player/admin.html
2. **Senha:** `trocar_senha_aqui_123`
3. **Token:** Gere em https://github.com/settings/tokens
4. **Arquivo:** Selecione `.html`
5. **Envie:** Clique "Validar e Enviar para GitHub"

---

## ⚙️ Como Funciona

1. **Validação de Segurança** (JavaScript)
   - Verifica scripts maliciosos
   - Bloqueia event handlers
   - Detecta PHP/ASP tags

2. **Autenticação** (SHA-256)
   - Valida senha admin
   - Hash gerado no navegador
   - Zero transmissão de senha

3. **Upload para GitHub** (REST API)
   - Usa token de acesso pessoal
   - Cria commit automaticamente
   - Publica via GitHub Pages

4. **Acesso Público**
   - GitHub Pages: segundos
   - Raw: imediato
   - Ambas com HTTPS

---

**Última atualização:** 5 de janeiro de 2026  
**Versão:** 2.1 GitHub Pages  
**Status:** ✅ Pronto para produção
