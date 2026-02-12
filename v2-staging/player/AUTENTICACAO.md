# Autenticação com Token do GitHub

## Por Que Token Manual?

O sistema usa **token manual** em vez de OAuth Device Flow porque:

1. **CORS Bloqueado**: O navegador bloqueia requisições diretas aos endpoints OAuth do GitHub (`github.com/login/*`) por política de segurança CORS
2. **Simplicidade**: Para ferramenta administrativa, token manual é mais direto e confiável
3. **Sem Backend**: Mantém 100% JavaScript client-side conforme requisito

## Como Gerar Token

### Passo 1: Acessar GitHub Settings
1. Faça login no GitHub
2. Vá em **Settings** → **Developer settings** → **Personal access tokens** → **Tokens (classic)**
3. Clique em **"Generate new token"** → **"Generate new token (classic)"**

### Passo 2: Configurar Permissões
- **Note**: `ProtonCD Upload` (ou nome descritivo)
- **Expiration**: Escolha validade (recomendado: 90 dias)
- **Scopes**: Marque apenas:
  - ✅ `repo` (acesso completo a repositórios privados)
    - ✅ `repo:status`
    - ✅ `repo_deployment`
    - ✅ `public_repo`
    - ✅ `repo:invite`
    - ✅ `security_events`

### Passo 3: Gerar e Copiar
1. Clique em **"Generate token"** no final da página
2. **IMPORTANTE**: Copie o token imediatamente (formato: `ghp_xxxxxxxxxxxxxxxxxxxx`)
3. **Guarde em local seguro** - não será exibido novamente

## Como Usar no Sistema

### 1. Acessar Admin
Abra: `https://www.protoncd.com.br/player/admin.html`

### 2. Colar Token
- Cole o token no campo **"Token de Acesso GitHub"**
- Token deve começar com `ghp_` ou `github_pat_`

### 3. Validar
- Clique em **"🔐 Validar Acesso"**
- Sistema verifica:
  - ✅ Token válido
  - ✅ Acesso ao repositório `limageorgio/protoncd`
  - ✅ Permissão de escrita (push)

### 4. Upload
- Após validação bem-sucedida, botão **"Enviar para GitHub"** será habilitado
- Selecione arquivo `.html` (máximo 5MB)
- Clique em **"Enviar para GitHub"**

## Segurança do Token

### ✅ Boas Práticas
- **Nunca compartilhe** o token com outras pessoas
- **Não commite** o token em repositórios
- **Revogue** tokens antigos quando não usar mais
- **Use tokens** com validade limitada (30-90 dias)
- **Regenere** periodicamente

### ⚠️ Se Token Vazou
1. Acesse: GitHub → Settings → Developer settings → Personal access tokens
2. Encontre o token comprometido
3. Clique em **"Delete"** ou **"Revoke"**
4. Gere novo token seguindo passos acima

### 🔒 O Que o Sistema Valida
```javascript
// 1. Autenticação do usuário
GET https://api.github.com/user
→ Verifica se token é válido

// 2. Acesso ao repositório
GET https://api.github.com/repos/limageorgio/protoncd
→ Confirma acesso ao repo

// 3. Permissão de escrita
repo.permissions.push === true
→ Garante permissão de upload
```

## Fluxo de Validação

```
┌─────────────────────┐
│ Colar Token         │
│ (ghp_xxx...)        │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Validar Formato     │
│ - Começa com ghp_?  │
│ - Não vazio?        │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Validar GitHub API  │
│ - User válido?      │
│ - Acesso ao repo?   │
│ - Permissão push?   │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ ✅ Token Validado   │
│ Botão habilitado    │
└─────────────────────┘
```

## Troubleshooting

### ❌ "Token inválido ou expirado"
- **Causa**: Token revogado ou deletado
- **Solução**: Gere novo token

### ❌ "Sem acesso ao repositório"
- **Causa**: Token não tem acesso ao `limageorgio/protoncd`
- **Solução**: 
  1. Verifique se você é colaborador do repositório
  2. Se for privado, garanta que token tem scope `repo`

### ❌ "Token sem permissão de escrita"
- **Causa**: Token tem apenas leitura (`read:repo`)
- **Solução**: Gere novo token com scope `repo` completo

### ❌ "Token deve começar com ghp_"
- **Causa**: Formato incorreto ou token Fine-grained
- **Solução**: Use **Personal access tokens (classic)**, não Fine-grained

## Tokens Fine-grained vs Classic

| Tipo | Formato | Recomendado? |
|------|---------|--------------|
| **Classic** | `ghp_xxxxx` | ✅ **Sim** - Funciona perfeitamente |
| **Fine-grained** | `github_pat_xxxxx` | ⚠️ Pode funcionar mas requer config adicional |

**Recomendação**: Use **Classic tokens** para simplicidade.

## Comparação: OAuth vs Token Manual

| Aspecto | OAuth Device Flow | Token Manual |
|---------|-------------------|--------------|
| **Implementação** | Complexa | Simples |
| **CORS** | ❌ Bloqueado pelo navegador | ✅ Funciona |
| **Backend** | ❌ Necessário (proxy) | ✅ Não necessário |
| **UX** | Melhor (automático) | Razoável (colar token) |
| **Segurança** | Alta | Alta (se token bem guardado) |
| **Validade** | Renovação automática | Manual (30-90 dias) |
| **Para Admin Tool** | Overkill | ✅ **Ideal** |

## Conclusão

Para ferramenta administrativa de upload de arquivos HTML:
- ✅ **Token manual** é abordagem **correta e segura**
- ✅ Evita complexidade de backend/proxy
- ✅ Mantém 100% JavaScript client-side
- ✅ Funcionamento confiável sem problemas CORS

---

**Documentação atualizada**: 29/12/2024  
**Sistema**: ProtonCD HTML Upload Tool  
**Repositório**: limageorgio/protoncd
