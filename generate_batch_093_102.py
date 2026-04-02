#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gerador de artigos elevadores elev-093 a elev-102.
"""

import json
from pathlib import Path

BASE_DIR = Path(r"h:\apps\protoncd")
ARTIGOS_DIR = BASE_DIR / "artigos" / "elevadores"

ARTICLES = [
    {
        "id": "elev-093",
        "slug": "porta-pavimento-fechamento-lento",
        "title": "Porta de Pavimento com Fechamento Lento",
        "description": "Fechamento excessivamente lento da porta amplia exposição do vão e aumenta risco operacional no tráfego diário.",
        "meta_description": "Porta de pavimento com fechamento lento exige ajuste técnico para reduzir exposição e restaurar segurança operacional.",
        "keywords": "porta de pavimento elevador, fechamento lento, regulagem de porta, risco operacional",
        "severity": "Média",
        "severity_color": "yellow",
        "probability": 63,
        "severity_level": 62,
        "exposure": 70,
        "priority": 68,
        "probability_label": "Média-Alta",
        "severity_label": "Média",
        "priority_label": "Média",
        "responsibility": "Condomínio",
        "scenario": "A porta de pavimento está levando mais tempo que o aceitável para fechar, aumentando exposição da abertura e favorecendo uso indevido.",
    },
    {
        "id": "elev-094",
        "slug": "inspecao-periodica-documentada-ausente",
        "title": "Ausência de Inspeção Periódica Documentada",
        "description": "Sem histórico formal de inspeções, a gestão técnica perde rastreabilidade e o risco jurídico do condomínio aumenta.",
        "meta_description": "Falta de inspeção periódica documentada fragiliza diligência técnica e pode gerar responsabilização em incidentes.",
        "keywords": "inspeção periódica elevador, registro de manutenção, rastreabilidade técnica, responsabilidade condomínio",
        "severity": "Alta",
        "severity_color": "orange",
        "probability": 66,
        "severity_level": 80,
        "exposure": 76,
        "priority": 84,
        "probability_label": "Média-Alta",
        "severity_label": "Alta",
        "priority_label": "Alta",
        "responsibility": "Condomínio",
        "scenario": "Não existem registros consistentes de inspeções periódicas, dificultando comprovação de diligência e resposta técnica em auditorias ou sinistros.",
    },
    {
        "id": "elev-095",
        "slug": "diferenca-tensao-cabos-tracao",
        "title": "Diferença de Tensão entre Cabos de Tração",
        "description": "Desequilíbrio de tensão entre cabos acelera desgaste, afeta nivelamento e compromete estabilidade da tração.",
        "meta_description": "Cabos de tração com tensão desigual exigem equalização técnica para evitar falhas progressivas no elevador.",
        "keywords": "cabos de tração elevador, equalização de cabos, tensão desigual, nivelamento",
        "severity": "Alta",
        "severity_color": "orange",
        "probability": 64,
        "severity_level": 82,
        "exposure": 78,
        "priority": 85,
        "probability_label": "Média-Alta",
        "severity_label": "Alta",
        "priority_label": "Alta",
        "responsibility": "Condomínio",
        "scenario": "Os cabos de tração apresentam diferença relevante de tensão, com distribuição irregular de carga e tendência de desgaste prematuro do conjunto.",
    },
    {
        "id": "elev-096",
        "slug": "protecao-ip-componentes-casa-maquinas",
        "title": "Proteção IP Inadequada em Componentes da Casa de Máquinas",
        "description": "Invólucros sem proteção IP compatível elevam vulnerabilidade a poeira e umidade, com risco de falha elétrica.",
        "meta_description": "Proteção IP inadequada em componentes eletrônicos do elevador reduz confiabilidade e demanda correção técnica.",
        "keywords": "proteção IP elevador, casa de máquinas, componentes eletrônicos, poeira e umidade",
        "severity": "Alta",
        "severity_color": "orange",
        "probability": 60,
        "severity_level": 81,
        "exposure": 75,
        "priority": 83,
        "probability_label": "Média",
        "severity_label": "Alta",
        "priority_label": "Alta",
        "responsibility": "Condomínio",
        "scenario": "Foram identificados módulos e conexões expostos a poeira e umidade por ausência de proteção IP adequada ao ambiente da casa de máquinas.",
    },
    {
        "id": "elev-097",
        "slug": "travamento-recorrente-entre-andares",
        "title": "Travamento Recorrente entre Andares",
        "description": "Paradas frequentes entre andares indicam falha sistêmica e aumentam risco de aprisionamento e pânico.",
        "meta_description": "Travamento recorrente entre andares exige bloqueio para diagnóstico estruturado e correção de causa raiz.",
        "keywords": "elevador trava entre andares, aprisionamento, falha de comando, diagnóstico elevador",
        "severity": "Alta",
        "severity_color": "orange",
        "probability": 69,
        "severity_level": 84,
        "exposure": 82,
        "priority": 88,
        "probability_label": "Alta",
        "severity_label": "Alta",
        "priority_label": "Alta",
        "responsibility": "Condomínio",
        "scenario": "O equipamento apresenta episódios repetidos de travamento entre pavimentos, com interrupção de viagem e necessidade frequente de atendimento emergencial.",
    },
    {
        "id": "elev-098",
        "slug": "sinal-luminoso-pavimento-inoperante",
        "title": "Sinal Luminoso de Pavimento Inoperante",
        "description": "Indicação visual inoperante prejudica orientação do usuário, acessibilidade e fluxo seguro de embarque.",
        "meta_description": "Falha no sinal luminoso de pavimento não é apenas conforto: afeta navegação segura e acessibilidade no elevador.",
        "keywords": "sinal luminoso elevador, indicador de pavimento, acessibilidade cognitiva, botoeira",
        "severity": "Média",
        "severity_color": "yellow",
        "probability": 58,
        "severity_level": 61,
        "exposure": 66,
        "priority": 67,
        "probability_label": "Média",
        "severity_label": "Média",
        "priority_label": "Média",
        "responsibility": "Condomínio",
        "scenario": "Os indicadores luminosos de pavimento não funcionam de forma confiável, reduzindo a orientação dos usuários durante embarque e desembarque.",
    },
    {
        "id": "elev-099",
        "slug": "acesso-quadro-comando-sem-barreira",
        "title": "Acesso ao Quadro de Comando sem Barreira Física",
        "description": "Quadro de comando sem barreira de acesso expõe leigos a risco elétrico e manipulação indevida de circuitos críticos.",
        "meta_description": "Acesso livre ao quadro de comando do elevador configura risco crítico e requer restrição física imediata.",
        "keywords": "quadro de comando elevador, acesso restrito, risco elétrico, barreira física",
        "severity": "Crítica",
        "severity_color": "red",
        "probability": 57,
        "severity_level": 95,
        "exposure": 86,
        "priority": 92,
        "probability_label": "Média",
        "severity_label": "Crítica",
        "priority_label": "CRÍTICA",
        "responsibility": "Condomínio",
        "scenario": "O quadro de comando pode ser acessado sem barreira física efetiva, permitindo contato indevido com partes energizadas e comandos essenciais.",
    },
    {
        "id": "elev-100",
        "slug": "folga-anormal-portas-pavimento",
        "title": "Folga Anormal nas Portas de Pavimento",
        "description": "Folgas acima do padrão em portas de pavimento elevam risco de aprisionamento de dedos e falhas de fechamento.",
        "meta_description": "Folga anormal em portas de pavimento exige medição e regulagem para restabelecer condição segura de operação.",
        "keywords": "folga porta elevador, porta de pavimento, aprisionamento de dedos, regulagem de porta",
        "severity": "Alta",
        "severity_color": "orange",
        "probability": 62,
        "severity_level": 82,
        "exposure": 79,
        "priority": 86,
        "probability_label": "Média",
        "severity_label": "Alta",
        "priority_label": "Alta",
        "responsibility": "Condomínio",
        "scenario": "As portas de pavimento apresentam folga superior à faixa recomendada, com risco de contato indevido com zonas perigosas do sistema.",
    },
    {
        "id": "elev-101",
        "slug": "ruido-rolamento-porta-cabina",
        "title": "Ruído de Rolamento na Porta da Cabina",
        "description": "Ruído persistente em rolamentos da porta indica desgaste e pode evoluir para travamento do conjunto.",
        "meta_description": "Rolamento ruidoso na porta da cabina sinaliza desgaste e requer manutenção corretiva sem demora.",
        "keywords": "rolamento porta cabina, ruído de porta elevador, manutenção de portas, travamento",
        "severity": "Média",
        "severity_color": "yellow",
        "probability": 61,
        "severity_level": 63,
        "exposure": 68,
        "priority": 69,
        "probability_label": "Média",
        "severity_label": "Média",
        "priority_label": "Média",
        "responsibility": "Condomínio",
        "scenario": "A porta da cabina apresenta ruído anormal no rolamento durante abertura e fechamento, com sinais de desgaste progressivo.",
    },
    {
        "id": "elev-102",
        "slug": "teste-funcional-freio-maquina-ausente",
        "title": "Ausência de Teste Funcional do Freio de Máquina",
        "description": "Sem ensaio funcional periódico, falhas do freio podem permanecer ocultas até situação crítica de segurança.",
        "meta_description": "Falta de teste funcional do freio de máquina compromete segurança do elevador e exige regularização imediata.",
        "keywords": "freio de máquina elevador, teste funcional, retenção de cabina, segurança de frenagem",
        "severity": "Crítica",
        "severity_color": "red",
        "probability": 55,
        "severity_level": 96,
        "exposure": 88,
        "priority": 93,
        "probability_label": "Média",
        "severity_label": "Crítica",
        "priority_label": "CRÍTICA",
        "responsibility": "Condomínio",
        "scenario": "Não há evidência de teste funcional recente do freio de máquina para validar capacidade de parada e retenção em condição segura.",
    },
]


def generate_html_article(article):
    return f'''<!DOCTYPE html>
<html lang="pt-BR">

<head>
    <script>(function (w, d, s, l, i) {{
            w[l] = w[l] || []; w[l].push({{'gtm.start': new Date().getTime(), event: 'gtm.js' }});
            var f = d.getElementsByTagName(s)[0], j = d.createElement(s), dl = l != 'dataLayer' ? '&l=' + l : '';
            j.async = true; j.src = 'https://www.googletagmanager.com/gtm.js?id=' + i + dl;
            f.parentNode.insertBefore(j, f);
        }})(window, document, 'script', 'dataLayer', 'GTM-5NNLDWJX');</script>
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-33VH6XTPZF"></script>
    <script>window.dataLayer = window.dataLayer || []; function gtag() {{ dataLayer.push(arguments); }} gtag('js', new Date()); gtag('config', 'G-33VH6XTPZF');</script>

    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">
    <meta name="description" content="{article['meta_description']}">
    <meta name="keywords" content="{article['keywords']}">
    <meta name="author" content="Proton Engenharia Diagnóstica">

    <title>{article['title']} | Proton Engenharia</title>
    <link rel="canonical" href="https://www.protoncd.com.br/artigos/elevadores/artigo-elevadores-{article['slug']}.html">
    <link rel="alternate" hreflang="pt-BR" href="https://www.protoncd.com.br/artigos/elevadores/artigo-elevadores-{article['slug']}.html">

    <meta property="og:type" content="article">
    <meta property="og:url" content="https://www.protoncd.com.br/artigos/elevadores/artigo-elevadores-{article['slug']}.html">
    <meta property="og:title" content="{article['title']}">
    <meta property="og:description" content="{article['meta_description']}">
    <meta property="og:site_name" content="Proton Engenharia Diagnóstica">
    <meta property="og:locale" content="pt_BR">
    <meta property="og:image" content="https://www.protoncd.com.br/img/logo_proton1x1.jpg">
    <meta property="article:published_time" content="2026-04-02">
    <meta property="article:author" content="Georgio Batista de Lima">
    <meta property="article:section" content="Elevadores">

    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{article['title']}">
    <meta name="twitter:description" content="{article['meta_description']}">

    <link rel="stylesheet" href="../../css/all.min.css">
    <link rel="icon" href="../../img/faviconb.ico" type="image/x-icon">
    <link rel="stylesheet" href="../../css/variables.css">
    <link rel="stylesheet" href="../../css/base.css">
    <link rel="stylesheet" href="../../css/components.css">
    <link rel="stylesheet" href="../../css/layout.css">
    <link rel="stylesheet" href="../../css/animations.css">

    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "Article",
      "headline": "{article['title']}",
      "description": "{article['meta_description']}",
      "datePublished": "2026-04-02",
      "dateModified": "2026-04-02",
      "inLanguage": "pt-BR",
      "author": {{ "@type": "Person", "name": "Georgio Batista de Lima" }},
      "publisher": {{ "@type": "Organization", "name": "Proton Engenharia Diagnóstica" }}
    }}
    </script>

    <style>
        .article-container {{ max-width: 900px; margin: 0 auto; padding: var(--space-8) var(--space-4); }}
        .article-hero-panel {{ background: var(--bg-card); border: 1px solid var(--border-subtle); border-radius: var(--radius-xl); padding: var(--space-6); margin-bottom: var(--space-7); }}
        .article-intro {{ max-width: 760px; margin: 0 auto var(--space-5); text-align: center; }}
        .article-mini-stats {{ display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: var(--space-3); margin: 0 0 var(--space-5); }}
        .article-mini-stat {{ background: rgba(255, 255, 255, 0.02); border: 1px solid var(--border-subtle); border-radius: var(--radius-lg); padding: var(--space-3); text-align: center; }}
        .article-mini-stat strong {{ display: block; font-size: 1.1rem; margin-bottom: 4px; }}
        .risk-chart {{ background: var(--bg-subtle); border: 1px solid var(--border-subtle); border-radius: var(--radius-xl); padding: var(--space-5); margin: var(--space-5) 0; }}
        .risk-row {{ display: grid; grid-template-columns: 180px 1fr auto; align-items: center; gap: var(--space-3); margin-bottom: var(--space-3); }}
        .risk-bar {{ height: 10px; border-radius: 999px; background: rgba(255, 255, 255, 0.08); overflow: hidden; }}
        .risk-bar span {{ display: block; height: 100%; background: linear-gradient(90deg, #f59e0b 0%, #ef4444 100%); }}
        .decision-table {{ width: 100%; border-collapse: collapse; margin: var(--space-4) 0; border: 1px solid var(--border-subtle); }}
        .decision-table th, .decision-table td {{ border: 1px solid var(--border-subtle); padding: 10px; vertical-align: top; }}
        .content-box {{ background: var(--bg-subtle); border: 1px solid var(--border-subtle); padding: var(--space-4); border-radius: var(--radius-lg); margin: var(--space-4) 0; }}
        .cta-section {{ margin-top: var(--space-8); padding: var(--space-6); border: 1px solid var(--border-subtle); border-radius: var(--radius-xl); background: linear-gradient(135deg, rgba(14, 165, 233, 0.12), rgba(14, 165, 233, 0.03)); text-align: center; }}
        @media (max-width: 900px) {{ .article-mini-stats {{ grid-template-columns: 1fr; }} .risk-row {{ grid-template-columns: 1fr; gap: 6px; }} }}
    </style>
</head>

<body>
    <nav class="nav" id="main-nav">
        <div class="nav-inner">
            <a href="../../index.html" class="nav-logo">
                <img src="../../img/logo_proton_branco.png" alt="Proton Engenharia" width="36" height="36">
                <span class="nav-logo-text">PROTON <span>Engenharia</span></span>
            </a>
            <div class="nav-links">
                <a href="../../index.html#inicio">Início</a>
                <a href="../../index.html#servicos">Serviços</a>
                <a href="../../conhecimento-tecnico/index.html">Base Técnica</a>
                <a href="../../index.html#contato" class="nav-cta"><i class="fab fa-whatsapp"></i> Contato</a>
            </div>
        </div>
    </nav>

    <main class="article-container">
        <article class="article-content">
            <div class="article-hero-panel">
                <div class="article-intro">
                    <span class="badge badge-{article['severity_color']}" style="margin-bottom: var(--space-3);">Artigo Técnico</span>
                    <h1>{article['title']}</h1>
                    <p>{article['description']}</p>
                </div>
                <div class="article-mini-stats">
                    <div class="article-mini-stat"><strong>{article['severity']}</strong><span>Gravidade</span></div>
                    <div class="article-mini-stat"><strong>{article['priority_label']}</strong><span>Prioridade</span></div>
                    <div class="article-mini-stat"><strong>{article['responsibility']}</strong><span>Responsável</span></div>
                </div>
                <div style="text-align:center; margin-top: var(--space-3);">
                    <a href="https://api.whatsapp.com/send?phone=5562992852704&text=Olá! Preciso de análise técnica sobre {article['title']}." class="btn btn-primary btn-sm" target="_blank" rel="noopener noreferrer"><i class="fab fa-whatsapp"></i> Falar com Especialista</a>
                </div>
            </div>

            <h2 id="sec-identificacao"><i class="fas fa-info-circle" style="margin-right:8px;"></i>1. Identificação Técnica</h2>
            <div class="content-box">
                <p><strong>Sintoma Observado (Linguagem Leiga):</strong></p>
                <p>{article['scenario']}</p>
                <p style="margin-top:var(--space-4);"><strong>Definição Técnica:</strong></p>
                <p>{article['scenario']}</p>
                <p style="margin-top:var(--space-4);"><strong>Localização Típica:</strong></p>
                <p>Casa de máquinas, teto da cabina, quadro de comando, poço e componentes de segurança vinculados à ocorrência.</p>
            </div>

            <h2 id="sec-contexto"><i class="fas fa-microscope" style="margin-right:8px;"></i>2. Contexto e Cenário</h2>
            <h3>O que é observado em campo</h3>
            <p>{article['scenario']}</p>
            <ul>
                <li><strong>Origem típica:</strong> ajuste inadequado, desgaste progressivo, instalação fora de especificação ou manutenção incompleta.</li>
                <li><strong>Modo de falha:</strong> perda de desempenho, acionamento anômalo de segurança ou indisponibilidade operacional.</li>
                <li><strong>Agravantes:</strong> atraso na correção, ausência de testes e falta de rastreabilidade em registros técnicos.</li>
            </ul>

            <div class="risk-chart">
                <div class="risk-row">
                    <strong>Probabilidade</strong>
                    <div class="risk-bar"><span style="width:{article['probability']}%;"></span></div>
                    <span>{article['probability_label']}</span>
                </div>
                <div class="risk-row">
                    <strong>Severidade</strong>
                    <div class="risk-bar"><span style="width:{article['severity_level']}%;"></span></div>
                    <span>{article['severity_label']}</span>
                </div>
                <div class="risk-row">
                    <strong>Exposição</strong>
                    <div class="risk-bar"><span style="width:{article['exposure']}%;"></span></div>
                    <span>Contínua</span>
                </div>
                <div class="risk-row">
                    <strong>Prioridade de ação</strong>
                    <div class="risk-bar"><span style="width:{article['priority']}%;"></span></div>
                    <span>{article['priority_label']}</span>
                </div>
            </div>

            <h2 id="sec-protocolo"><i class="fas fa-clipboard-list" style="margin-right:8px;"></i>3. Protocolo de Inspeção</h2>
            <ul>
                <li>Executar inspeção visual e funcional com checklists técnicos e evidências fotográficas.</li>
                <li>Comparar condição encontrada com requisitos normativos aplicáveis e manual do fabricante.</li>
                <li>Medir parâmetros críticos quando aplicável (temperatura, resposta de freio, nivelamento, comunicação, etc.).</li>
                <li>Classificar criticidade e emitir plano corretivo com prazos e responsáveis definidos.</li>
            </ul>

            <h2 id="sec-matriz"><i class="fas fa-table" style="margin-right:8px;"></i>4. Matriz de Decisão Corretiva</h2>
            <table class="decision-table">
                <thead>
                    <tr>
                        <th>Cenário</th>
                        <th>Ação recomendada</th>
                        <th>Prazo</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>Risco crítico confirmado</td>
                        <td>Interditar equipamento e corrigir antes da liberação</td>
                        <td>Imediato</td>
                    </tr>
                    <tr>
                        <td>Falha relevante sem risco iminente</td>
                        <td>Corrigir com priorização e validação técnica pós-serviço</td>
                        <td>Até 48h</td>
                    </tr>
                    <tr>
                        <td>Desvio de média gravidade</td>
                        <td>Programar ajuste e monitorar tendência em manutenção assistida</td>
                        <td>Até 7 dias</td>
                    </tr>
                </tbody>
            </table>

            <section class="cta-section">
                <h3>Precisa de diagnóstico técnico sobre {article['title'].lower()}?</h3>
                <p>A Proton Engenharia apoia síndicos e gestores com inspeção especializada, laudo e plano de ação com base em normas ABNT.</p>
                <div style="display:flex; gap:12px; justify-content:center; flex-wrap:wrap;">
                    <a href="https://api.whatsapp.com/send?phone=5562992852704&text=Olá! Preciso de diagnóstico técnico sobre {article['title']}." target="_blank" rel="noopener noreferrer" class="btn btn-primary btn-sm"><i class="fab fa-whatsapp"></i> Solicitar Análise</a>
                    <a href="../../conhecimento-tecnico/index.html" class="btn btn-secondary btn-sm"><i class="fas fa-book"></i> Ver Base Técnica</a>
                </div>
            </section>
        </article>
    </main>

    <footer class="footer">
        <div class="container">
            <div class="footer-bottom">
                <p>&copy; 2026 Proton Engenharia Diagnóstica. Todos os direitos reservados.</p>
            </div>
        </div>
    </footer>
    <script src="../../js/main.js"></script>
</body>

</html>'''


def main():
    ARTIGOS_DIR.mkdir(parents=True, exist_ok=True)
    created_files = []

    for article in ARTICLES:
        filename = f"artigo-elevadores-{article['slug']}.html"
        path = ARTIGOS_DIR / filename
        html = generate_html_article(article)
        path.write_text(html, encoding="utf-8")
        created_files.append({
            "id": article["id"],
            "slug": article["slug"],
            "filename": filename,
            "title": article["title"],
        })
        print(f"OK: {filename}")

    out = BASE_DIR / "batch_093_102_created_files.json"
    out.write_text(json.dumps(created_files, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\nArquivo de índice salvo em: {out.name}")


if __name__ == "__main__":
    main()
