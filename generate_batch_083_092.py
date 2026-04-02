#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gerador de artigos elevadores elev-083 a elev-092.
"""

import json
from pathlib import Path

BASE_DIR = Path(r"h:\apps\protoncd")
ARTIGOS_DIR = BASE_DIR / "artigos" / "elevadores"

ARTICLES = [
    {
        "id": "elev-083",
        "slug": "botao-stop-inspecao-teto-cabina",
        "title": "Comando de Inspeção no Teto da Cabina sem Botão STOP Adequado",
        "description": "Sem botão STOP funcional no modo inspeção, o risco de movimento inesperado aumenta e a manutenção fica insegura.",
        "meta_description": "Botão STOP ausente ou ineficaz no teto da cabina é falha crítica de segurança ocupacional durante inspeção.",
        "keywords": "botão stop elevador, inspeção teto cabina, manutenção segura, parada de emergência",
        "severity": "Crítica",
        "severity_color": "red",
        "probability": 64,
        "severity_level": 96,
        "exposure": 88,
        "priority": 94,
        "probability_label": "Média-Alta",
        "severity_label": "Crítica",
        "priority_label": "CRÍTICA",
        "responsibility": "Condomínio",
        "scenario": "No comando de inspeção do teto da cabina, o STOP não atua corretamente ou está ausente, expondo o técnico a risco de esmagamento por movimento inesperado.",
    },
    {
        "id": "elev-084",
        "slug": "deslizamento-tracao-polias",
        "title": "Deslizamento na Tração das Polias do Elevador",
        "description": "Perda de aderência entre cabos e polias compromete frenagem, aceleração e nivelamento, exigindo ação imediata.",
        "meta_description": "Deslizamento na tração é sinal grave de risco operacional e desgaste acelerado no conjunto de cabos e polias.",
        "keywords": "deslizamento tração elevador, polias, cabos de aço, aderência",
        "severity": "Crítica",
        "severity_color": "red",
        "probability": 60,
        "severity_level": 95,
        "exposure": 84,
        "priority": 93,
        "probability_label": "Média",
        "severity_label": "Crítica",
        "priority_label": "CRÍTICA",
        "responsibility": "Condomínio",
        "scenario": "Há patinamento no conjunto de tração, com perda de desempenho na partida e na parada, elevando risco de pane e desgaste progressivo dos cabos.",
    },
    {
        "id": "elev-085",
        "slug": "freio-seguranca-retardamento-fora-faixa",
        "title": "Retardamento do Freio de Segurança Fora da Faixa",
        "description": "Desaceleração fora da faixa técnica pode causar lesão em ocupantes e falha de proteção em emergência.",
        "meta_description": "Freio de segurança descalibrado, com retardamento fora da faixa, representa risco humano e não conformidade crítica.",
        "keywords": "freio de segurança elevador, retardamento, desaceleração, ensaio de segurança",
        "severity": "Crítica",
        "severity_color": "red",
        "probability": 56,
        "severity_level": 97,
        "exposure": 82,
        "priority": 92,
        "probability_label": "Média",
        "severity_label": "Crítica",
        "priority_label": "CRÍTICA",
        "responsibility": "Mista - requer avaliação técnica",
        "scenario": "O freio de segurança apresenta resposta fora da curva esperada, com desaceleração excessiva ou insuficiente em situação de emergência.",
    },
    {
        "id": "elev-086",
        "slug": "guias-deformacao-fixacao-comprometida",
        "title": "Guias com Deformação ou Fixação Comprometida",
        "description": "Deformações e ancoragens deficientes em guias afetam estabilidade e desempenho de frenagem de emergência.",
        "meta_description": "Guias deformadas ou mal fixadas comprometem segurança estrutural da cabina e atuação de dispositivos de emergência.",
        "keywords": "guias elevador, deformação trilhos, fixação guias, frenagem emergência",
        "severity": "Crítica",
        "severity_color": "red",
        "probability": 52,
        "severity_level": 96,
        "exposure": 80,
        "priority": 91,
        "probability_label": "Média",
        "severity_label": "Crítica",
        "priority_label": "CRÍTICA",
        "responsibility": "Mista - requer avaliação técnica",
        "scenario": "Foram identificadas guias com desvios geométricos e pontos de fixação comprometidos, reduzindo a confiabilidade da movimentação e da frenagem de segurança.",
    },
    {
        "id": "elev-087",
        "slug": "vazamento-circuito-hidraulico-continuo",
        "title": "Vazamento Contínuo no Circuito Hidráulico",
        "description": "Vazamento no sistema hidráulico reduz confiabilidade de operação e pode agravar risco ambiental e mecânico.",
        "meta_description": "Vazamento contínuo em elevador hidráulico exige correção imediata para preservar segurança e desempenho do sistema.",
        "keywords": "elevador hidráulico vazamento, circuito hidráulico, válvula de segurança, óleo no poço",
        "severity": "Alta",
        "severity_color": "orange",
        "probability": 68,
        "severity_level": 81,
        "exposure": 74,
        "priority": 84,
        "probability_label": "Alta",
        "severity_label": "Alta",
        "priority_label": "Alta",
        "responsibility": "Condomínio",
        "scenario": "Há perda contínua de fluido no circuito hidráulico, com impacto na descida controlada e risco de contaminação do poço.",
    },
    {
        "id": "elev-088",
        "slug": "falha-watchdog-seguranca-eletronica",
        "title": "Falha no Watchdog do Sistema Eletrônico de Segurança",
        "description": "Sem watchdog funcional, falhas latentes de segurança podem passar despercebidas e evoluir sem bloqueio.",
        "meta_description": "Falha de watchdog em circuito eletrônico de segurança é condição crítica e requer diagnóstico especializado imediato.",
        "keywords": "watchdog elevador, segurança eletrônica, circuito de segurança, falha latente",
        "severity": "Crítica",
        "severity_color": "red",
        "probability": 50,
        "severity_level": 98,
        "exposure": 83,
        "priority": 93,
        "probability_label": "Média",
        "severity_label": "Crítica",
        "priority_label": "CRÍTICA",
        "responsibility": "Mista - requer avaliação técnica",
        "scenario": "O monitoramento watchdog não valida corretamente o estado do sistema eletrônico, permitindo comportamento anômalo sem reação de proteção.",
    },
    {
        "id": "elev-089",
        "slug": "alarme-sobretemperatura-recorrente",
        "title": "Alarme de Sobretemperatura Recorrente",
        "description": "Alarmes repetidos de temperatura indicam degradação de componentes e risco de pane súbita.",
        "meta_description": "Sobretemperatura recorrente em elevador é sinal de anomalia progressiva e exige análise de causa raiz.",
        "keywords": "sobretemperatura elevador, alarme térmico, motor, inversor de frequência",
        "severity": "Alta",
        "severity_color": "orange",
        "probability": 66,
        "severity_level": 79,
        "exposure": 72,
        "priority": 82,
        "probability_label": "Média-Alta",
        "severity_label": "Alta",
        "priority_label": "Alta",
        "responsibility": "Condomínio",
        "scenario": "Eventos de sobretemperatura se repetem em operação normal, sugerindo falha progressiva em motor, inversor ou freio.",
    },
    {
        "id": "elev-090",
        "slug": "oscilacao-cabina-parada",
        "title": "Oscilação da Cabina na Parada",
        "description": "Oscilação recorrente na parada reduz conforto, afeta acessibilidade e acelera desgaste mecânico.",
        "meta_description": "Oscilação perceptível da cabina na parada indica necessidade de ajuste técnico em nivelamento e guiamento.",
        "keywords": "oscilação cabina, parada elevador, nivelamento, roletes",
        "severity": "Média",
        "severity_color": "yellow",
        "probability": 58,
        "severity_level": 62,
        "exposure": 64,
        "priority": 66,
        "probability_label": "Média",
        "severity_label": "Média",
        "priority_label": "Média",
        "responsibility": "Condomínio",
        "scenario": "A cabina apresenta balanço perceptível ao parar no pavimento, com indícios de ajuste inadequado em guias, roletes ou amortecimento.",
    },
    {
        "id": "elev-091",
        "slug": "contraste-visual-botoeiras-pavimento",
        "title": "Falta de Contraste Visual nas Botoeiras de Pavimento",
        "description": "Contraste insuficiente nas botoeiras compromete acessibilidade e aumenta erro de acionamento.",
        "meta_description": "Botoeiras sem contraste adequado prejudicam usuários com baixa visão e geram não conformidade de acessibilidade.",
        "keywords": "botoeira elevador contraste, acessibilidade elevadores, baixa visão, sinalização",
        "severity": "Média",
        "severity_color": "yellow",
        "probability": 62,
        "severity_level": 60,
        "exposure": 67,
        "priority": 68,
        "probability_label": "Média",
        "severity_label": "Média",
        "priority_label": "Média",
        "responsibility": "Construtora",
        "scenario": "Os comandos de pavimento não possuem contraste visual suficiente entre fundo, símbolos e números, dificultando leitura e autonomia do usuário.",
    },
    {
        "id": "elev-092",
        "slug": "intermitencia-interfone-emergencia",
        "title": "Intermitência no Interfone de Emergência",
        "description": "Falhas intermitentes de comunicação de emergência configuram não conformidade e elevam risco em aprisionamento.",
        "meta_description": "Interfone de emergência com cortes de áudio ou falha de chamada deve ser corrigido antes de operação regular.",
        "keywords": "interfone de emergência elevador, comunicação bidirecional, aprisionamento, segurança",
        "severity": "Crítica",
        "severity_color": "red",
        "probability": 54,
        "severity_level": 95,
        "exposure": 86,
        "priority": 92,
        "probability_label": "Média",
        "severity_label": "Crítica",
        "priority_label": "CRÍTICA",
        "responsibility": "Condomínio",
        "scenario": "O interfone da cabina apresenta ruído, queda de áudio ou ausência de chamada, comprometendo suporte remoto durante emergência.",
    },
]


def generate_html_article(article):
    color_rgb = {
        "red": "239,68,68",
        "orange": "245,158,11",
        "yellow": "234,179,8",
        "blue": "14,165,233",
    }
    rgb = color_rgb.get(article["severity_color"], "14,165,233")

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

    out = BASE_DIR / "batch_083_092_created_files.json"
    out.write_text(json.dumps(created_files, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\nArquivo de índice salvo em: {out.name}")


if __name__ == "__main__":
    main()
