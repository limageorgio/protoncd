# 🤖 Instruções para IA Geradora de Código - Upload Direto no GitHub

## 📋 Contexto

Este documento contém as instruções que você deve fornecer a uma IA geradora de código (como GitHub Copilot, Claude, ChatGPT, etc.) para que ela salve arquivos HTML diretamente no seu repositório GitHub.

---

## 🎯 Prompt para a IA

### Versão Completa (Copiar e Colar)

```
Preciso que você gere código HTML e salve diretamente no meu repositório GitHub.

INFORMAÇÕES DO REPOSITÓRIO:
- Owner: limageorgio
- Repositório: protoncd
- Branch: main
- Pasta de destino: player/
- Nome do arquivo: [ESPECIFIQUE O NOME, ex: player-elevador-abc-123.html]

TOKEN DE ACESSO:
- Token: [COLE SEU TOKEN ghp_xxxxx AQUI]
- Permissões necessárias: repo (full control)

MÉTODO DE UPLOAD:
Use a GitHub REST API com o endpoint:
PUT https://api.github.com/repos/limageorgio/protoncd/contents/player/[NOME_ARQUIVO]

REQUISIÇÃO:
Headers:
  Authorization: Bearer [SEU_TOKEN]
  Content-Type: application/json
  Accept: application/vnd.github.v3+json

Body JSON:
{
  "message": "Upload: [NOME_ARQUIVO]",
  "content": "[CONTEÚDO_HTML_EM_BASE64]",
  "branch": "main",
  "committer": {
    "name": "Elevator Inspektor AI",
    "email": "admin@protoncd.com.br"
  }
}

IMPORTANTE:
1. Converta o HTML para Base64 antes de enviar
2. Use btoa(unescape(encodeURIComponent(htmlContent))) para encoding
3. Retorne a URL pública após upload: https://limageorgio.github.io/protoncd/player/[NOME_ARQUIVO]
4. Confirme o sucesso do upload mostrando a URL

VALIDAÇÕES DE SEGURANÇA (aplicar antes do upload):
- Não usar eval()
- Não usar document.write()
- Não usar redirecionamentos automáticos (window.location, location.href)
- Não usar protocolos perigosos em scripts (javascript:, data:, about:)
- Não incluir meta refresh com URL
- Não incluir tags PHP ou ASP

Após gerar e fazer upload do HTML, me informe:
1. Nome do arquivo salvo
2. URL pública de acesso
3. Tamanho do arquivo em KB
4. SHA do commit (se disponível)
```

---

## 🔑 Informações de Acesso

### Dados do Repositório
```yaml
Owner: limageorgio
Repositório: protoncd
Branch: main
Pasta: player/
URL Base GitHub Pages: https://limageorgio.github.io/protoncd/player/
```

### Token de Acesso
Seu token pessoal do GitHub (formato: `ghp_xxxxxxxxxxxxx`)
- **Permissões**: `repo` (controle total de repositórios)
- **Geração**: https://github.com/settings/tokens
- **⚠️ NUNCA compartilhe publicamente ou em commits**

---

## 📝 Exemplo de Conversa com a IA

### Você pergunta:
```
Crie um player HTML interativo para visualização de vídeo de elevador
com controles de play/pause e timeline.

Salve diretamente no GitHub:
- Repositório: limageorgio/protoncd
- Pasta: player/
- Nome: player-elevador-torre-a-2025.html
- Token: ghp_[SEU_TOKEN_AQUI]
```

### IA deve responder com:
```
✅ Arquivo criado e salvo com sucesso!

📄 Nome: player-elevador-torre-a-2025.html
📊 Tamanho: 15.3 KB
🔗 URL Pública: https://limageorgio.github.io/protoncd/player/player-elevador-torre-a-2025.html
🆔 Commit SHA: abc123def456...

O player HTML foi gerado com:
- Controles de vídeo interativos
- Timeline com marcadores
- Design responsivo
- Validações de segurança aplicadas
```

---

## 🛠️ Código de Referência (Para a IA Usar)

### JavaScript para Upload

```javascript
async function uploadToGitHub(filename, htmlContent, githubToken) {
    const GITHUB_OWNER = 'limageorgio';
    const GITHUB_REPO = 'protoncd';
    const GITHUB_BRANCH = 'main';
    const GITHUB_FOLDER = 'player';
    
    const url = `https://api.github.com/repos/${GITHUB_OWNER}/${GITHUB_REPO}/contents/${GITHUB_FOLDER}/${filename}`;
    
    // Converter HTML para Base64
    const encoded = btoa(unescape(encodeURIComponent(htmlContent)));
    
    const payload = {
        message: `Upload: ${filename}`,
        content: encoded,
        branch: GITHUB_BRANCH,
        committer: {
            name: "Elevator Inspektor AI",
            email: "admin@protoncd.com.br"
        }
    };
    
    const response = await fetch(url, {
        method: 'PUT',
        headers: {
            'Authorization': `Bearer ${githubToken}`,
            'Content-Type': 'application/json',
            'Accept': 'application/vnd.github.v3+json'
        },
        body: JSON.stringify(payload)
    });
    
    if (!response.ok) {
        const error = await response.json();
        throw new Error(error.message || 'Erro ao enviar para GitHub');
    }
    
    const data = await response.json();
    
    return {
        success: true,
        filename: filename,
        sha: data.content.sha,
        url: `https://limageorgio.github.io/protoncd/player/${filename}`,
        rawUrl: `https://raw.githubusercontent.com/${GITHUB_OWNER}/${GITHUB_REPO}/${GITHUB_BRANCH}/${GITHUB_FOLDER}/${filename}`
    };
}
```

### Python para Upload

```python
import requests
import base64

def upload_to_github(filename, html_content, github_token):
    GITHUB_OWNER = 'limageorgio'
    GITHUB_REPO = 'protoncd'
    GITHUB_BRANCH = 'main'
    GITHUB_FOLDER = 'player'
    
    url = f"https://api.github.com/repos/{GITHUB_OWNER}/{GITHUB_REPO}/contents/{GITHUB_FOLDER}/{filename}"
    
    # Converter HTML para Base64
    encoded = base64.b64encode(html_content.encode('utf-8')).decode('utf-8')
    
    payload = {
        "message": f"Upload: {filename}",
        "content": encoded,
        "branch": GITHUB_BRANCH,
        "committer": {
            "name": "Elevator Inspektor AI",
            "email": "admin@protoncd.com.br"
        }
    }
    
    headers = {
        'Authorization': f'Bearer {github_token}',
        'Content-Type': 'application/json',
        'Accept': 'application/vnd.github.v3+json'
    }
    
    response = requests.put(url, json=payload, headers=headers)
    
    if response.status_code not in [200, 201]:
        raise Exception(f"Erro: {response.json()}")
    
    data = response.json()
    
    return {
        'success': True,
        'filename': filename,
        'sha': data['content']['sha'],
        'url': f"https://limageorgio.github.io/protoncd/player/{filename}",
        'raw_url': f"https://raw.githubusercontent.com/{GITHUB_OWNER}/{GITHUB_REPO}/{GITHUB_BRANCH}/{GITHUB_FOLDER}/{filename}"
    }
```

---

## 🔒 Segurança

### O Token Permite:
✅ Upload de arquivos na pasta `player/`  
✅ Commit e push no branch `main`  
✅ Leitura de repositórios  
✅ Criação e exclusão de arquivos  

### O Token NÃO Permite (se configurado corretamente):
❌ Acesso a outros repositórios (a menos que tenha permissão explícita)  
❌ Acesso a repositórios privados de terceiros  
❌ Modificação de settings do repositório  
❌ Gerenciamento de usuários  

### Boas Práticas:
1. **Use token com escopo limitado**: Apenas `repo` para repositórios públicos
2. **Não exponha o token**: Nunca coloque em código público ou commits
3. **Defina expiração**: Configure validade de 30-90 dias
4. **Revogue se comprometido**: Acesse GitHub → Settings → Tokens → Delete
5. **Use .env ou variáveis de ambiente** quando possível

---

## 🌐 Acesso a Outros Repositórios

### Mesmo Autor (Você)
✅ **Sim, é possível!** O token `repo` dá acesso a TODOS os repositórios que você possui.

Para acessar outro repositório seu:
```javascript
// Repositório original
const REPO1 = {
    owner: 'limageorgio',
    repo: 'protoncd',
    folder: 'player'
};

// Outro repositório seu
const REPO2 = {
    owner: 'limageorgio',
    repo: 'meu-outro-projeto',
    folder: 'uploads'
};

// Use o mesmo token para ambos!
await uploadToGitHub(REPO1, filename, content, token);
await uploadToGitHub(REPO2, filename, content, token);
```

### Outro Autor (Terceiros)
❌ **Não diretamente.** Você precisaria:
1. Ser adicionado como **colaborador** do repositório
2. Ter um **fork** do repositório
3. Usar **GitHub Apps** com permissões específicas

---

## 📊 Exemplo de Resposta da API

### Sucesso (201 Created)
```json
{
  "content": {
    "name": "player-elevador-abc.html",
    "path": "player/player-elevador-abc.html",
    "sha": "abc123def456...",
    "size": 15673,
    "url": "https://api.github.com/repos/limageorgio/protoncd/contents/player/player-elevador-abc.html",
    "html_url": "https://github.com/limageorgio/protoncd/blob/main/player/player-elevador-abc.html",
    "git_url": "https://api.github.com/repos/limageorgio/protoncd/git/blobs/abc123def456...",
    "download_url": "https://raw.githubusercontent.com/limageorgio/protoncd/main/player/player-elevador-abc.html"
  },
  "commit": {
    "sha": "def789ghi012...",
    "message": "Upload: player-elevador-abc.html"
  }
}
```

### Erro (422 Unprocessable Entity) - Arquivo já existe
```json
{
  "message": "Invalid request.\n\n\"sha\" wasn't supplied.",
  "documentation_url": "https://docs.github.com/rest/reference/repos#create-or-update-file-contents"
}
```

**Solução**: Para sobrescrever, precisa fornecer o `sha` atual do arquivo.

---

## 🧪 Testando a Integração

### 1. Teste Manual com cURL
```bash
curl -X PUT \
  https://api.github.com/repos/limageorgio/protoncd/contents/player/teste.html \
  -H "Authorization: Bearer ghp_SEU_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "message": "Teste de upload",
    "content": "PCFET0NUWVBFIGh0bWw+CjxodG1sPgo8aGVhZD48dGl0bGU+VGVzdGU8L3RpdGxlPjwvaGVhZD4KPGJvZHk+PGgxPk9sw6EhPC9oMT48L2JvZHk+CjwvaHRtbD4=",
    "branch": "main"
  }'
```

### 2. Verifique o Resultado
- Acesse: https://github.com/limageorgio/protoncd/blob/main/player/teste.html
- URL Pública: https://limageorgio.github.io/protoncd/player/teste.html

### 3. Delete o Teste (se necessário)
Use a interface admin.html ou:
```bash
curl -X DELETE \
  https://api.github.com/repos/limageorgio/protoncd/contents/player/teste.html \
  -H "Authorization: Bearer ghp_SEU_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "message": "Delete teste",
    "sha": "SHA_DO_ARQUIVO",
    "branch": "main"
  }'
```

---

## 📚 Documentação Oficial

- **GitHub REST API - Contents**: https://docs.github.com/en/rest/repos/contents
- **GitHub Pages**: https://docs.github.com/en/pages
- **Personal Access Tokens**: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token

---

## ✅ Checklist para a IA

A IA geradora de código deve:

- [ ] Gerar código HTML válido e funcional
- [ ] Aplicar validações de segurança (sem eval, document.write, etc.)
- [ ] Converter conteúdo para Base64
- [ ] Fazer requisição PUT para API do GitHub
- [ ] Usar token de autenticação fornecido
- [ ] Especificar committer (name e email)
- [ ] Confirmar sucesso do upload
- [ ] Retornar URL pública do GitHub Pages
- [ ] Informar SHA do commit
- [ ] Tratar erros (arquivo já existe, token inválido, etc.)

---

## 🎓 Dicas de Uso

### Para Claude/ChatGPT/Copilot:
```
"Após gerar o código HTML, execute a função de upload usando a API do GitHub
e me confirme a URL pública onde o arquivo está disponível."
```

### Para Copilot Workspace:
```
"Crie um novo arquivo HTML em player/ com o nome [NOME] e faça commit
diretamente no branch main do repositório limageorgio/protoncd."
```

### Para GitHub Actions (Automação):
Crie um workflow que aceita HTML via input e faz upload automaticamente.

---

**Última atualização**: 05/01/2026  
**Repositório**: limageorgio/protoncd  
**Sistema**: Elevator Inspektor Player
