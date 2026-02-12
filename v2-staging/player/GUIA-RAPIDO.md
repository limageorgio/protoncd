# 📖 GUIA RÁPIDO DE USO

## Para Administradores

### 🎯 Objetivo
Fazer upload de arquivos HTML (players) de forma segura na pasta player do ProtonCD.

---

## 📋 Antes de Começar

1. ✅ Você tem a **senha de administrador**
2. ✅ Você tem um arquivo **`.html`** pronto
3. ✅ Você tem **acesso à internet** em seu navegador

---

## 🚀 Passo a Passo - Upload

### PASSO 1️⃣ : Preparar Arquivo

Prepare seu arquivo HTML localmente.

**Validar antes de enviar:**

```bash
# Windows PowerShell ou Terminal
php player/validate-html.php seu-arquivo.html
```

Deve retornar:
```
✅ RESULTADO: ARQUIVO PASSOU EM TODAS AS VALIDAÇÕES
```

Se tiver erros, corrija o HTML.

---

### PASSO 2️⃣ : Acessar Interface Admin

Abra seu navegador e acesse:

```
https://www.protoncd.com.br/player/admin.html
```

**Você deve ver:**
- Formulário de login
- Campo para senha
- Campo para selecionar arquivo
- Botão de upload

---

### PASSO 3️⃣ : Autenticar

1. Digite a **senha de administrador** no campo "Senha de Administrador"
2. O campo está vazio por padrão, deixe em branco se não tiver alterado

**⚠️ Nota importante:**
Se a senha foi alterada, a padrão NÃO funciona. Use a senha correta.

---

### PASSO 4️⃣ : Selecionar Arquivo

1. Clique em "Selecione o arquivo HTML"
2. Navegue até seu arquivo `.html`
3. Selecione e clique "Abrir"

**Você verá:**
- Nome do arquivo
- Tamanho em KB

---

### PASSO 5️⃣ : Fazer Upload

1. Clique em "**Validar e Enviar**"
2. Aguarde a validação (alguns segundos)
3. Observe a **barra de progresso**

**Possíveis mensagens:**

#### ✅ Sucesso
```
✅ RESULTADO: ARQUIVO ENVIADO COM SUCESSO!

Arquivo: seu-arquivo.html
URL de Acesso: /player/seu-arquivo.html
Tamanho: 150 KB
```

#### ❌ Erro
```
Erro: Arquivo contém conteúdo suspeito ou malicioso
```

**O que fazer:**
1. Verifique o HTML procurando por:
   - `<script>` tags
   - `onclick=`, `onerror=`
   - `<iframe>`
   - Código malicioso

2. Remova o conteúdo suspeito
3. Salve e tente novamente

---

### PASSO 6️⃣ : Copiar URL

Após sucesso, você receberá a **URL de acesso**:

```
https://www.protoncd.com.br/player/seu-arquivo.html
```

**Botão "Copiar"** ao lado da URL para copiar automaticamente.

---

### PASSO 7️⃣ : Compartilhar

Envie a URL para o cliente ou use internamente:

```
https://www.protoncd.com.br/player/seu-arquivo.html
```

---

## 📊 Exemplo Prático

### Cenário: Fazer Upload de Player de Torre C1

1. **Arquivo pronto:** `torre-c1-novo.html` (500 KB)

2. **Acessar admin:**
   ```
   https://www.protoncd.com.br/player/admin.html
   ```

3. **Preencher:**
   - Senha: (deixar em branco ou usar a nova)
   - Arquivo: selecionar `torre-c1-novo.html`

4. **Clicar:** "Validar e Enviar"

5. **Resultado:**
   ```
   ✅ Arquivo enviado com sucesso!
   
   Arquivo: torre-c1-novo.html
   URL: https://www.protoncd.com.br/player/torre-c1-novo.html
   ```

6. **Compartilhar URL:**
   ```
   https://www.protoncd.com.br/player/torre-c1-novo.html
   ```

---

## ⚠️ Problemas Comuns

### Problema: "Acesso negado. Token de autenticação inválido"

**Causa:** Senha incorreta

**Solução:**
1. Verifique a senha
2. Se a alterou, use a nova
3. Se esqueceu, peça ao administrador do servidor

### Problema: "Arquivo contém conteúdo suspeito"

**Causa:** HTML tem código malicioso detectado

**Solução:**
1. Abra o arquivo em editor de texto
2. Procure por:
   - `<script>`
   - `javascript:`
   - `onclick=`, `onerror=`
   - `<iframe>`
3. Remova essas partes
4. Salve e tente novamente

### Problema: "Apenas arquivos .html são permitidos"

**Causa:** Arquivo não é HTML

**Solução:**
1. Verifique extensão do arquivo (deve ser `.html`)
2. Renomeie se necessário: `arquivo.html`
3. Tente novamente

### Problema: Upload completa mas arquivo não aparece

**Causa:** Pode ser nome duplicado

**Solução:**
1. Aguarde 10 segundos
2. Atualize a página
3. Tente acessar: `https://www.protoncd.com.br/player/nome-arquivo.html`
4. Se ainda não aparece, verifique o log

---

## 🔍 Verificar Upload

### Método 1: Acessar Direto
```
https://www.protoncd.com.br/player/seu-arquivo.html
```

Se carregar, upload funcionou! ✅

### Método 2: Verificar Log
```
https://www.protoncd.com.br/player/.upload_log.txt
```

Procure pela última linha com seu arquivo:
```
[2025-01-05 14:30:21] IP: 192.168.1.1 | Ação: UPLOAD | Arquivo: seu-arquivo.html | Status: SUCESSO | Detalhes: Arquivo validado e salvo
```

---

## 🎨 Características do Player

Seus players podem ter:

✅ **Permitido:**
- HTML e CSS
- JavaScript (eventos validados)
- Imagens
- Vídeos
- Gráficos
- Interatividade

❌ **Bloqueado:**
- Scripts com `<script>` tag
- Event handlers diretos (`onclick=`)
- iframes
- Código PHP/ASP
- Conteúdo malicioso

---

## 💡 Dicas

### 1. Teste Localmente Primeiro
```bash
php player/validate-html.php seu-arquivo.html
```

### 2. Use HTML5 Puro
Evite HTML antigo ou frameworks pesados.

### 3. Comprima Imagens
Reduza tamanho de assets antes de incluir.

### 4. Valide Estrutura
Certifique-se que `<html>` e `<body>` existem.

### 5. Backup Local
Mantenha cópia do arquivo em seu computador.

---

## 📞 Suporte Rápido

**Para dúvidas técnicas:**
1. Veja [SEGURANCA.md](SEGURANCA.md)
2. Consulte [DEPLOY.md](DEPLOY.md)
3. Use validador local

**Para problemas de upload:**
1. Verifique mensagem de erro
2. Corrija o HTML
3. Valide localmente
4. Tente novamente

---

## 📋 Checklist Antes de Upload

- [ ] Arquivo é `.html`
- [ ] Arquivo validou localmente
- [ ] Sem `<script>` tags
- [ ] Sem `onclick=`, `onerror=`
- [ ] Sem `<iframe>`
- [ ] Sem código PHP/ASP
- [ ] Tem estrutura HTML válida
- [ ] Tamanho < 5MB
- [ ] Testou em navegador local

---

**Pronto para fazer upload? Comece em:**
```
https://www.protoncd.com.br/player/admin.html
```

---

**Última atualização:** 5 de janeiro de 2026  
**Versão:** 1.0
