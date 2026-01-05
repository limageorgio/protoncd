# Validação de Arquivos HTML

## ⚠️ Mudança Importante na Estratégia de Validação

### Problema Anterior

A validação estava **muito restritiva** e bloqueava HTML legítimo:

```javascript
// ❌ BLOQUEAVA TUDO (versão antiga)
/<script[^>]*>.*?<\/script>/is,    // Bloqueava TODOS os scripts
/on\w+\s*=/i,                      // Bloqueava TODOS event handlers
/<iframe[^>]*>/i,                  // Bloqueava TODOS iframes
```

**Resultado**: Arquivos HTML válidos como `player-torre-c1-2.html` eram rejeitados.

### Nova Estratégia: Validação Inteligente

Agora validamos apenas **padrões verdadeiramente perigosos**:

## ✅ O Que É Permitido

### Scripts Legítimos
```html
<!-- ✅ PERMITIDO: Scripts normais -->
<script src="jquery.min.js"></script>
<script src="https://cdn.example.com/lib.js"></script>
<script>
  console.log('Hello World');
  const data = { x: 10 };
</script>
```

### Event Handlers Legítimos
```html
<!-- ✅ PERMITIDO: Event handlers normais -->
<button onclick="handleClick()">Clique</button>
<body onload="init()">
<img onerror="handleError()">
```

### iFrames Legítimos
```html
<!-- ✅ PERMITIDO: iframes de vídeos, mapas, etc -->
<iframe src="https://www.youtube.com/embed/VIDEO_ID"></iframe>
<iframe src="https://www.google.com/maps/embed"></iframe>
```

## ❌ O Que É Bloqueado

### 1. Scripts com Protocolos Perigosos
```html
<!-- ❌ BLOQUEADO: javascript: protocol -->
<script src="javascript:alert('XSS')"></script>

<!-- ❌ BLOQUEADO: data: protocol -->
<script src="data:text/javascript,alert('XSS')"></script>

<!-- ❌ BLOQUEADO: about: protocol -->
<script src="about:blank"></script>
```

**Padrão**: `/<script[^>]*src\s*=\s*["'](?:javascript:|data:|about:)/i`

### 2. Uso de eval()
```html
<!-- ❌ BLOQUEADO: eval() é perigoso -->
<script>
  eval(userInput);  // Executa código arbitrário
</script>
```

**Padrão**: `/<script[^>]*>\s*eval\s*\(/i`

**Por quê?**: `eval()` pode executar código malicioso de strings.

### 3. document.write() Suspeito
```html
<!-- ❌ BLOQUEADO: document.write pode injetar HTML -->
<script>
  document.write('<script src="evil.js"></script>');
</script>
```

**Padrão**: `/<script[^>]*>\s*document\.write\s*\(/i`

**Por quê?**: Pode sobrescrever todo o documento com conteúdo malicioso.

### 4. PHP e ASP Tags
```html
<!-- ❌ BLOQUEADO: Server-side code -->
<?php system($_GET['cmd']); ?>
<% Response.Write(Request("data")) %>
```

**Padrões**: 
- `/<?php/i` - PHP tags
- `/<%[^=]/i` - ASP tags (exceto `<%=` que é comum em templates)

**Por quê?**: Podem executar comandos no servidor se houver vulnerabilidade.

### 5. Redirecionamentos Suspeitos
```html
<!-- ❌ BLOQUEADO: Redirecionamentos automáticos -->
<script>
  window.location = 'http://phishing-site.com';
  location.href = 'http://malware.com';
</script>
```

**Padrões**:
- `/<script[^>]*>\s*window\.location/i`
- `/<script[^>]*>\s*location\.href/i`

**Por quê?**: Podem redirecionar usuários para sites maliciosos.

### 6. Meta Refresh com URL
```html
<!-- ❌ BLOQUEADO: Redirecionamento via meta tag -->
<meta http-equiv="refresh" content="0;url=http://evil.com">
```

**Padrão**: `/<meta[^>]*http-equiv\s*=\s*["']refresh["'][^>]*url=/i`

**Por quê?**: Redirecionamento automático pode ser usado em phishing.

## 🔍 Validação de HTML Válido

O arquivo deve conter pelo menos uma destas tags:
```html
<!DOCTYPE html>   <!-- ✅ -->
<html>           <!-- ✅ -->
<head>           <!-- ✅ -->
<body>           <!-- ✅ -->
```

**Padrão**: `/<!DOCTYPE/i || /<html/i || /<head/i || /<body/i`

## 📋 Checklist de Segurança

### Antes de Fazer Upload

- [ ] Remover `eval()` do código
- [ ] Evitar `document.write()` (use `appendChild` ou `innerHTML`)
- [ ] Não usar `javascript:`, `data:`, `about:` em src de scripts
- [ ] Remover redirecionamentos automáticos (`window.location`, `location.href`)
- [ ] Não incluir tags PHP (`<?php`) ou ASP (`<%`)
- [ ] Não usar `<meta refresh>` com URL

### ✅ Boas Práticas

```javascript
// ❌ NÃO USE eval()
eval(userCode);

// ✅ USE Function constructor (mais seguro)
const fn = new Function('return ' + userCode);

// ❌ NÃO USE document.write()
document.write('<p>Hello</p>');

// ✅ USE innerHTML ou appendChild
document.body.innerHTML += '<p>Hello</p>';
// ou
const p = document.createElement('p');
p.textContent = 'Hello';
document.body.appendChild(p);
```

## 🛡️ Por Que Esta Abordagem?

### Antiga: Lista Negra Ampla
- ❌ Bloqueia funcionalidades legítimas
- ❌ Frustra usuários com HTML válido
- ❌ Não distingue uso legítimo de malicioso

### Nova: Lista Negra Específica
- ✅ Permite HTML/JS legítimo
- ✅ Bloqueia apenas padrões verdadeiramente perigosos
- ✅ Equilibra segurança e usabilidade
- ✅ Foco em vetores de ataque reais (XSS, injeção, phishing)

## 🔐 Camadas de Segurança

Nossa segurança não depende apenas da validação de conteúdo:

### 1. Validação de Conteúdo (esta)
- Bloqueia padrões perigosos conhecidos

### 2. Autenticação GitHub
- Apenas usuários autorizados podem fazer upload
- Token com permissões específicas

### 3. GitHub Pages
- Conteúdo servido de domínio isolado (`github.io`)
- Não tem acesso a cookies do domínio principal

### 4. Apache .htaccess
- Bloqueia tipos de arquivo executáveis
- Headers de segurança (X-Frame-Options, CSP)

### 5. Limite de Tamanho
- Máximo 5MB por arquivo
- Previne upload de arquivos gigantes

## 📊 Comparação de Padrões

| Padrão | Antiga | Nova | Por quê? |
|--------|--------|------|----------|
| `<script>` | ❌ Bloqueava TODOS | ✅ Permite normal | Scripts legítimos são necessários |
| `onclick=` | ❌ Bloqueava TODOS | ✅ Permite | Event handlers são comuns |
| `<iframe>` | ❌ Bloqueava TODOS | ✅ Permite | Vídeos/mapas usam iframes |
| `javascript:` | ❌ Bloqueava | ❌ Bloqueia | Vetor de XSS real |
| `eval()` | ✅ Permitia | ❌ Bloqueia | Execução de código arbitrário |
| `window.location` | ✅ Permitia | ❌ Bloqueia | Redirecionamento malicioso |

## 🧪 Testando a Validação

### Teste 1: HTML Legítimo
```html
<!DOCTYPE html>
<html>
<head>
  <script src="jquery.min.js"></script>
</head>
<body onload="init()">
  <button onclick="alert('OK')">Clique</button>
</body>
</html>
```
**Resultado**: ✅ PASSA

### Teste 2: eval() Malicioso
```html
<!DOCTYPE html>
<html>
<body>
  <script>eval(userInput);</script>
</body>
</html>
```
**Resultado**: ❌ BLOQUEADO (eval detectado)

### Teste 3: Redirecionamento Suspeito
```html
<!DOCTYPE html>
<html>
<body>
  <script>window.location = 'http://evil.com';</script>
</body>
</html>
```
**Resultado**: ❌ BLOQUEADO (redirecionamento detectado)

## 💡 Dicas para Desenvolvedores

### Se Seu HTML for Rejeitado

1. **Verifique o console do navegador** (F12)
   - A validação loga qual padrão foi detectado
   - `console.warn('⚠️ Padrão perigoso detectado:', pattern)`

2. **Remova padrões perigosos**:
   - Substitua `eval()` por `Function()` ou JSON.parse()
   - Substitua `document.write()` por DOM manipulation
   - Remova redirecionamentos automáticos
   - Use CDNs confiáveis (não `javascript:` protocol)

3. **Valide localmente**:
   ```bash
   node validate-html.js seu-arquivo.html
   ```

## 📝 Arquivos Relacionados

- [admin.html](admin.html) - Interface de upload (validação embutida)
- [validate-html.js](validate-html.js) - Validador standalone
- [AUTENTICACAO.md](AUTENTICACAO.md) - Guia de autenticação
- [README-JAVASCRIPT.md](README-JAVASCRIPT.md) - Documentação técnica

---

**Última atualização**: 05/01/2026  
**Sistema**: ProtonCD HTML Upload Tool  
**Versão da Validação**: 2.0 (Validação Inteligente)
