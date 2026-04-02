# Compliance Checklist para Artigos da Base Técnica

**Objetivo:** Garantir que todos os artigos criados na pasta `/conhecimento-tecnico/artigos/` estejam em conformidade com o escopo de serviços da Proton Engenharia (diagnóstico apenas, não manutenção/reparação).

---

## 1. Garantias de Escopo de Serviço

### ✓ Requisito 1.1: Disclaimer Obrigatório
- [ ] Artigo contém disclaimer explícito declarando que Proton é empresa de **diagnóstico e parecer técnico** apenas
- [ ] Disclaimer aparece em local visível (caixa destacada — `content-box warning`) no início da Seção 6 (Recomendações)
- [ ] Texto do disclaimer inclui: "A Proton Engenharia realiza diagnóstico e parecer técnico. As recomendações abaixo devem ser executadas pelo condomínio ou terceiros contratados."
- [ ] Exemplo de implementação:
```html
<div class="content-box warning" style="margin-bottom: var(--space-6);">
    <p><i class="fas fa-info-circle"></i><strong>Importante:</strong> A Proton Engenharia realiza <strong>diagnóstico e parecer técnico</strong>. As recomendações abaixo devem ser executadas pelo condomínio ou terceiros contratados, conforme orientação do laudo técnico.</p>
</div>
```

### ✓ Requisito 1.2: Responsabilidades Atribuídas Explicitamente
- [ ] Cada recomendação técnica inclui linha **"Responsável:"** ao final
- [ ] Responsáveis identificados claramente como um dos:
  - `Proton Engenharia (neste estágio)` — apenas para diagnóstico/inspeção
  - `Condomínio/Empresa contratada` — para ações de manutenção/reparação
  - `Empresa de elevadores/manutenção certificada (ABNT)` — para serviços especializado
- [ ] Exemplo:
```html
<li><strong>Responsável:</strong> <strong>Proton Engenharia (neste estágio)</strong> — oferece diagnóstico completo em 24 horas.</li>
<li><strong>Responsável:</strong> Empresa de elevadores/manutenção certificada, coordenada pelo condomínio.</li>
```

### ✓ Requisito 1.3: Nunca Implicar que Proton Executa Serviços Fora do Escopo
- [ ] **PROIBIDO**: Linguagem que implica Proton oferece manutenção, reparação, limpeza, drenagem, instalação, substituição, levantamento, afinação, etc.
- [ ] **PROIBIDO**: Usar termos como "Fase de Resolução" sem clareza: renomear para "Recomendação 3 (Resolução)" com aviso de responsabilidade
- [ ] **PERMITIDO**: "diagnóstico", "parecer técnico", "inspeção", "análise", "avaliação", "recomendação", "protocolo de ação"
- [ ] Checklist de palavras proibidas (buscar no artigo):
  - [ ] "Proton realiza limpeza" → ❌ ERRADO
  - [ ] "Proton executa substituição" → ❌ ERRADO
  - [ ] "Plano de Ação" (sem context) → ⚠️ USE "Recomendações Técnicas" ou "Protocolo"
  - [ ] "Proton faz drenagem" → ❌ ERRADO

---

## 2. Linguagem de CTA (Call-to-Action)

### ✓ Requisito 2.1: CTA Deve Reforçar Diagnóstico
- [ ] CTA principal menciona especificamente "diagnóstico técnico", "parecer técnico", ou "inspeção"
- [ ] CTA NÃO menciona "plano de ação", "solução", "execução", ou implica que Proton fará o trabalho
- [ ] Exemplo CORRETO: "A Proton Engenharia oferece **diagnóstico técnico completo em 24 horas** com recomendações prioritizadas."
- [ ] Exemplo INCORRETO: "A Proton Engenharia oferece diagnóstico em 24 horas e **plano de ação**." (ambíguo sobre quem executa)

### ✓ Requisito 2.2: Mensagem WhatsApp
- [ ] Mensagem começa com diagnóstico/inspeção, não com problema (evita parecer que Proton vai consertar)
- [ ] Exemplo CORRETO: `"Preciso de diagnóstico técnico urgente."`
- [ ] Exemplo INCORRETO: `"Preciso de inspeção URGENTE!"` (muito genérico, vague sobre escopo)

### ✓ Requisito 2.3: Botões de CTA
- [ ] Botão WhatsApp/telefone diz "Solicitar **Diagnóstico** Urgente", não "Solicitar Inspeção Urgente" ou "Solicitar Serviço"
- [ ] Rótulo do botão alinha com escopo: diagnóstico, parecer, avaliação, ou inspeção

---

## 3. Conteúdo Técnico

### ✓ Requisito 3.1: Seção de Recomendações Renomeada
- [ ] Seção 6 é intitulada "Recomendações Técnicas e Protocolo" OU "Recomendações para Ação Correta" — NÃO "Plano de Ação"
- [ ] Sustitulos de fases devem ser nomeados como "Recomendação 1", "Recomendação 2", "Recomendação 3" — NÃO "Fase 1", "Fase 2", "Fase 3"

### ✓ Requisito 3.2: Linguagem de Recomendação (não Prescrição)
- [ ] Texto usa modo imperativo para ações recomendadas, mas sempre com responsabilidade clara:
  - ✅ "Recomendação 1 (Contenção): Drenar água acumulada. **Responsável:** Condomínio/Empresa contratada."
  - ❌ "Fase 1: Drenar água acumulada. A Proton fará isso..."
- [ ] Cada recomendação começa com **"Objetivo:"** dizendo por quê essa ação é necessária

### ✓ Requisito 3.3: Avisos Especiais para Serviços que Proton NÃO Fornece
- [ ] Se recomendação envolve serviço especializado (substituição de cabos, reparação mecânica, instalação), adicionar linha tipo:
  - "**Atenção:** Execução responsabilidade de empresa elevatória certificada (ABNT), não Proton."
  - Ou: "**Nota:** Este serviço deve ser executado por terceiro certificado, conforme parecer técnico."

---

## 4. SEO e Metadados

### ✓ Requisito 4.1: Meta Descrição Alinha com Escopo
- [ ] Meta description não promete serviços além de diagnóstico
- [ ] Exemplo CORRETO: `"Diagnóstico de elevadores: como identificar cabos enferrujados e arames rompidos. Parecer técnico da Proton."`
- [ ] Exemplo INCORRETO: `"Substituição de cabos de elevadores: serviço completo da Proton com garantia."`

### ✓ Requisito 4.2: Título SEO Alinha com Escopo
- [ ] Título (H1/meta title) menciona diagnóstico, inspeção, ou parecer — não "solução" ou "serviço completo"
- [ ] Evitar: "Como consertar cabos de elevador" (implica Proton faz conserto)
- [ ] Preferir: "Como diagnosticar cabos de elevador corrosivos" (diagnóstico focus)

---

## 5. Validação Técnica

### ✓ Requisito 5.1: Sem Erros HTML
- [ ] Executar `get_errors` nos arquivo — deve retornar "No errors found"

### ✓ Requisito 5.2: Links Internos Funcionam
- [ ] Links para página de contato: `../../#contato`
- [ ] Links para base técnica: `../`
- [ ] Links para homepage: `../../`
- [ ] Todos os links foram testados e funcionam

### ✓ Requisito 5.3: Schema.org e Metadata
- [ ] Schema.org inclui "@type": "Article" com author = "protoncd.com.br"
- [ ] Open Graph tags presentes (og:title, og:description, og:image, og:url)
- [ ] Canonical URL definido corretamente

---

## 6. Revisão Final

### ✓ Requisito 6.1: Leitura de Compliance
- [ ] Ler artigo completamente com foco em: Proton promete serviços fora do escopo? Responsabilidades estão claras?
- [ ] Pergunta-chave: *"Se um leitor tivesse que resumir em uma frase o que Proton faz, diria diagnóstico/parecer ou algo mais?"*

### ✓ Requisito 6.2: Teste de Liability
- [ ] Imaginar cenário: Cliente lê artigo, pensa Proton fará reparação X, contrata Proton esperando isso, depois descobre que Proton só faz diagnóstico. Artigo cria essa confusão? **Sim = FAIL, Não = PASS**

### ✓ Requisito 6.3: Aprovação
- [ ] [ ] Artigo aprovado por revisor (compliance)
- [ ] [ ] Artigo pronto para publicação/SEO

---

## Checklist de Implementação

Ao criar um novo artigo, usar este template:

```html
<!-- SECTION 6 TEMPLATE -->
<h2><i class="fas fa-tasks" style="margin-right:8px;"></i>6. Recomendações Técnicas e Protocolo</h2>

<div class="content-box warning" style="margin-bottom: var(--space-6);">
    <p><i class="fas fa-info-circle" style="margin-right:8px; color:var(--accent-red);"></i><strong>Importante:</strong> A Proton Engenharia realiza <strong>diagnóstico e parecer técnico</strong>. As recomendações abaixo devem ser executadas pelo condomínio ou terceiros contratados, conforme orientação do laudo técnico.</p>
</div>

<h3 style="background: var(--accent-red); color: white; padding: var(--space-3) var(--space-4); border-radius: var(--radius-lg); display: inline-block; margin-bottom: var(--space-4);">Recomendação 1 (Contenção Imediata)</h3>
<p><strong>Objetivo:</strong> [PREENCHER]</p>
<ul style="margin-bottom: var(--space-6);">
    <li>[RECOMENDAÇÕES]</li>
    <li><strong>Responsável:</strong> [Condomínio/Empresa contratada OU Proton Engenharia (neste estágio) OU Empresa certificada ABNT]</li>
</ul>

<!-- ... resto das recomendações ... -->

<!-- CTA TEMPLATE -->
<div class="cta-section">
    <h3><i class="fas fa-exclamation-circle"></i> [PERGUNTA DE GATILHO]?</h3>
    <p>[SITUAÇÃO CRÍTICA]. A Proton Engenharia oferece <strong>diagnóstico técnico completo em 24 horas</strong> com recomendações prioritizadas.</p>
    <div class="cta-buttons">
        <a href="https://api.whatsapp.com/send?phone=5562992852704&text=Olá! [PROBLEMA]. Preciso de diagnóstico técnico urgente."
            target="_blank" rel="noopener noreferrer" class="btn-cta whatsapp">
            <i class="fab fa-whatsapp"></i> Solicitar Diagnóstico Urgente
        </a>
        <a href="tel:5562992852704" class="btn-cta">
            <i class="fas fa-phone"></i> Ligar Agora
        </a>
    </div>
</div>
```

---

## Histórico de Conformidade

| Data       | Artigo                                    | Status          | Notas |
|------------|-------------------------------------------|-----------------|-------|
| 2024-01-XX | artigo-elevadores-poco-contaminado.html  | ✅ CORRIGIDO    | Retirada referência "plano de ação", added disclaimer, clarified responsibilities |
| 2024-01-XX | artigo-elevadores-cabos-aco.html         | ✅ CORRIGIDO    | Retirada referência "plano de ação", added disclaimer, added cable-specific warning |

---

**Criado por:** GitHub Copilot (Compliance Audit)  
**Data:** Sessão Atual  
**Versão:** 1.0
