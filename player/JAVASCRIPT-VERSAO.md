# 📖 VERSÃO JAVASCRIPT - GUIA COMPLETO

## ✨ Mudança de Arquitetura

O sistema foi convertido para **100% JavaScript** no cliente (navegador), eliminando a necessidade de PHP no servidor.

---

## 🎯 O Que Mudou

### Antes (Com PHP)
```
Upload → admin-upload.php → Validação servidor → Salvar arquivo
```

### Agora (100% JavaScript)
```
Upload → JavaScript → Validação cliente → Salvar em IndexedDB/LocalStorage
```

---

## ✅ Funcionalidades JavaScript

### 1. **Autenticação SHA-256**
```javascript
async function generateSHA256(message) {
    const msgBuffer = new TextEncoder().encode(message);
    const hashBuffer = await crypto.subtle.digest('SHA-256', msgBuffer);
    // Retorna hash seguro
}
```

### 2. **Validação de Conteúdo HTML**
```javascript
function validateHTMLContent(content) {
    // Detecta:
    - ❌ Scripts inline (<script>)
    - ❌ JavaScript protocol
    - ❌ Event handlers (onclick=)
    - ❌ iframes
    - ❌ PHP/ASP tags
    // Retorna true/false
}
```

### 3. **Armazenamento em IndexedDB**
```javascript
async function saveFileToStorage(filename, content) {
    // Salva em banco de dados local
    // Persiste dados mesmo fechando navegador
    // Suporta até vários GB
}
```

---

## 🗂️ Arquivos Atualizados

| Arquivo | Status | Mudança |
|---------|--------|---------|
| `admin.html` | ✅ Atualizado | Inclui validação + armazenamento |
| `admin-upload.php` | ❌ Removido | Não é mais necessário |
| `.htaccess` | ✅ Mantido | Regras de segurança continuam |
| `validate-html.php` | ⚠️ Opcional | Convertido para validate-html.js |

---

## 🚀 Como Usar

### 1. Acessar Interface Admin
```
https://seu-site.com/player/admin.html
```

### 2. Autenticar
```
Senha padrão: trocar_senha_aqui_123
(Altere em admin.html, linha ~20)
```

### 3. Fazer Upload
1. Selecione arquivo `.html`
2. Clique "Validar e Enviar"
3. Validação acontece no cliente
4. Arquivo é salvo em IndexedDB

### 4. Acessar Arquivo
```javascript
// JavaScript pode acessar do IndexedDB
const files = await getAllFilesFromStorage();

// Ou em outro navegador/aba
// Os dados persistem localmente
```

---

## 💾 Armazenamento

### IndexedDB
- **Vantagem:** Persiste dados localmente
- **Tamanho:** Vários GB por site
- **Acesso:** Rápido e assíncrono
- **Seguro:** Isolado por domínio

### LocalStorage (Alternativa)
```javascript
// Se preferir usar localStorage
localStorage.setItem('file_' + filename, content);
```

---

## 🔐 Segurança

### Validações Implementadas

| Validação | Local | Como |
|-----------|-------|------|
| Extensão .html | Cliente | Regex |
| Tamanho < 5MB | Cliente | Propriedade file.size |
| Conteúdo | Cliente | Regex patterns |
| Scripts | Cliente | Busca `<script` |
| Handlers | Cliente | Busca `onclick=` |
| PHP/ASP | Cliente | Busca `<?php` |
| Autenticação | Cliente | SHA-256 |

---

## 📝 Configuração

### Alterar Senha

**Arquivo:** `admin.html` (linha ~20)

```javascript
const ADMIN_PASSWORD = 'trocar_senha_aqui_123';
```

**Mudança:**

```javascript
const ADMIN_PASSWORD = 'SenhaForte2025!';
```

---

## 🧪 Testes

### Testar Validação
```javascript
// Console do navegador
const content = '<html><body>Teste</body></html>';
console.log(validateHTMLContent(content)); // true

// Com script malicioso
const bad = '<script>alert("xss")</script>';
console.log(validateHTMLContent(bad)); // false
```

### Testar Autenticação
```javascript
// Console
const hash = await generateSHA256('teste');
console.log(hash); // Exibe hash SHA-256
```

### Testar Armazenamento
```javascript
// Verificar dados salvos
const db = await indexedDB.databases();
console.log(db); // Mostra bancos de dados
```

---

## 🎨 Personalização

### Mudar Senha Padrão
```javascript
// admin.html, linha ~20
const ADMIN_PASSWORD = 'sua_senha_nova';
```

### Aumentar Limite de Tamanho
```javascript
// admin.html, linha ~21
const MAX_FILE_SIZE = 10 * 1024 * 1024; // 10MB
```

### Adicionar Validações Extras
```javascript
function validateHTMLContent(content) {
    // ... validações existentes ...
    
    // Adicione suas validações:
    if (content.includes('malicious')) {
        return false;
    }
    
    return true;
}
```

---

## 🔄 Recuperar Arquivos Salvos

### JavaScript para Acessar
```javascript
function getAllFilesFromStorage() {
    return new Promise((resolve, reject) => {
        const request = indexedDB.open('ProtonCDPlayer', 1);
        
        request.onsuccess = function(event) {
            const db = event.target.result;
            const transaction = db.transaction(['files'], 'readonly');
            const store = transaction.objectStore('files');
            const allRequest = store.getAll();
            
            allRequest.onsuccess = function() {
                resolve(allRequest.result);
            };
        };
    });
}
```

### Uso
```javascript
const files = await getAllFilesFromStorage();
files.forEach(file => {
    console.log(file.name);
    console.log(file.content);
    console.log(file.timestamp);
});
```

---

## 🌐 Servir Arquivos

### Opção 1: Service Worker
```javascript
// service-worker.js
self.addEventListener('fetch', event => {
    if (event.request.url.includes('/player/')) {
        event.respondWith(
            indexedDB.open('ProtonCDPlayer')
                .then(db => {
                    const file = db.transaction(['files']).objectStore('files');
                    return file.get(filename);
                })
                .then(file => new Response(file.content))
        );
    }
});
```

### Opção 2: Blob URL
```javascript
// Gerar URL temporária
const blob = new Blob([content], { type: 'text/html' });
const url = URL.createObjectURL(blob);
// Usar: <a href={url}>Download</a>
```

---

## ⚠️ Limitações JavaScript

### ❌ Não é Possível
- Salvar no servidor (sem backend)
- Acessar arquivo direto via URL (sem Service Worker)
- Persistir além do navegador
- Servir a outros usuários

### ✅ É Possível
- Validar arquivo
- Autenticar usuário
- Armazenar localmente
- Converter para download
- Compartilhar via URL blob

---

## 💡 Soluções Alternativas

### Se Precisar de Servidor

#### Com Node.js
```javascript
// Simples servidor Express
const express = require('express');
const app = express();

app.post('/upload', (req, res) => {
    // Validação e armazenamento
});
```

#### Com PHP (Simples)
```php
<?php
if ($_FILES['file']) {
    $content = file_get_contents($_FILES['file']['tmp_name']);
    if (validateHTML($content)) {
        file_put_contents('storage/' . $_FILES['file']['name'], $content);
    }
}
?>
```

---

## 📚 Referências

### APIs Utilizadas
- **Crypto API** - Hash SHA-256
- **File API** - Ler arquivos
- **IndexedDB** - Armazenamento local
- **Fetch API** - Requisições HTTP (opcional)

### Documentação
- [MDN - SubtleCrypto](https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto)
- [MDN - IndexedDB](https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API)
- [MDN - File API](https://developer.mozilla.org/en-US/docs/Web/API/File)

---

## 🎯 Próximos Passos

1. **Testar localmente**
   - Abra `admin.html` no navegador
   - Tente fazer upload de arquivo HTML

2. **Customizar senha**
   - Edite `admin.html` linha ~20
   - Mude `ADMIN_PASSWORD`

3. **Ampliar funcionalidade**
   - Adicione Service Worker (opcional)
   - Implemente download dos arquivos
   - Crie interface para gerenciar arquivos salvos

---

## 🔗 Integração com Backend (Opcional)

Se depois quiser salvar no servidor:

```javascript
// Adicione ao final da validação
const formData = new FormData();
formData.append('file', content);
formData.append('filename', filename);

fetch('/api/save-player', {
    method: 'POST',
    body: formData
});
```

---

**Versão:** 1.0 JavaScript  
**Status:** ✅ Pronto para uso  
**Compatibilidade:** Chrome 37+, Firefox 32+, Safari 11+, Edge 79+
