#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gerador de artigos elevadores elev-103 a elev-112.
"""

import json
from pathlib import Path

BASE_DIR = Path(r"h:\apps\protoncd")
ARTIGOS_DIR = BASE_DIR / "artigos" / "elevadores"

ARTICLES = [
    {
        "id": "elev-103",
        "slug": "comando-inspecao-sem-codificacao-rotulos",
        "title": "Comando de Inspeção sem Codificação Clara de Cores e Rótulos",
        "description": "Comandos sem identificação visual clara aumentam erro humano durante manutenção e inspeção técnica.",
        "meta_description": "Comando de inspeção sem codificação de cores e rótulos eleva risco operacional e exige padronização imediata.",
        "keywords": "comando de inspeção elevador, rotulagem técnica, codificação de cores, erro humano manutenção",
        "severity": "Alta",
        "severity_color": "orange",
        "probability": 64,
        "severity_level": 82,
        "exposure": 77,
        "priority": 86,
        "probability_label": "Média-Alta",
        "severity_label": "Alta",
        "priority_label": "Alta",
        "responsibility": "Condomínio",
        "scenario": "O comando de inspeção apresenta botões e seletores sem codificação clara de cores e rótulos, criando ambiguidade para a equipe técnica em condição de risco.",
    },
    {
        "id": "elev-104",
        "slug": "elevador-emergencia-sem-painel-pavimento-descarga",
        "title": "Elevador de Emergência sem Painel de Controle no Pavimento de Descarga",
        "description": "Sem painel dedicado no pavimento de descarga, a resposta operacional dos bombeiros fica comprometida.",
        "meta_description": "Falta de painel no pavimento de descarga compromete uso do elevador de emergência e requer adequação urgente.",
        "keywords": "elevador de emergência, pavimento de descarga, painel de bombeiro, controle de emergência",
        "severity": "Crítica",
        "severity_color": "red",
        "probability": 58,
        "severity_level": 95,
        "exposure": 88,
        "priority": 93,
        "probability_label": "Média",
        "severity_label": "Crítica",
        "priority_label": "CRÍTICA",
        "responsibility": "Mista - avaliação técnica",
        "scenario": "O elevador classificado para emergência não possui painel de controle no pavimento de descarga, dificultando tomada de comando pelas equipes de socorro.",
    },
    {
        "id": "elev-105",
        "slug": "caixa-elevador-emergencia-sem-compartimentacao-corta-fogo",
        "title": "Caixa do Elevador de Emergência sem Compartimentação Corta-Fogo",
        "description": "Ausência de compartimentação favorece entrada de fumaça e fogo na caixa, reduzindo segurança de resgate.",
        "meta_description": "Caixa do elevador de emergência sem compartimentação corta-fogo representa não conformidade crítica de incêndio.",
        "keywords": "compartimentação corta-fogo, caixa do elevador, elevador de emergência, segurança contra incêndio",
        "severity": "Crítica",
        "severity_color": "red",
        "probability": 56,
        "severity_level": 96,
        "exposure": 90,
        "priority": 94,
        "probability_label": "Média",
        "severity_label": "Crítica",
        "priority_label": "CRÍTICA",
        "responsibility": "Mista - avaliação técnica",
        "scenario": "Foi identificada ausência de compartimentação corta-fogo adequada na caixa do elevador de emergência, com risco de propagação de fumaça para a rota de resgate.",
    },
    {
        "id": "elev-106",
        "slug": "velocidade-insuficiente-elevador-emergencia-predio-alto",
        "title": "Velocidade Insuficiente do Elevador de Emergência em Prédio Alto",
        "description": "Velocidade abaixo do parâmetro mínimo reduz eficiência de resposta em situação crítica.",
        "meta_description": "Elevador de emergência com velocidade insuficiente em prédio alto deve passar por ensaio e ajuste de desempenho.",
        "keywords": "velocidade elevador de emergência, desempenho elevador, ensaio de velocidade, prédio alto",
        "severity": "Alta",
        "severity_color": "orange",
        "probability": 60,
        "severity_level": 83,
        "exposure": 80,
        "priority": 87,
        "probability_label": "Média",
        "severity_label": "Alta",
        "priority_label": "Alta",
        "responsibility": "Mista - avaliação técnica",
        "scenario": "A velocidade de operação do elevador de emergência está abaixo da faixa esperada para a altura da edificação, aumentando tempo de resposta em ocorrências.",
    },
    {
        "id": "elev-107",
        "slug": "sinalizacao-capacidade-divergente-elevador",
        "title": "Sinalização de Capacidade Divergente da Realidade do Elevador",
        "description": "Indicação incorreta de capacidade induz sobrecarga e amplia risco operacional do sistema.",
        "meta_description": "Capacidade nominal divergente na sinalização do elevador aumenta risco de sobrecarga e responsabilização civil.",
        "keywords": "capacidade elevador, placa de lotação, sobrecarga elevador, sinalização técnica",
        "severity": "Alta",
        "severity_color": "orange",
        "probability": 63,
        "severity_level": 84,
        "exposure": 81,
        "priority": 88,
        "probability_label": "Média-Alta",
        "severity_label": "Alta",
        "priority_label": "Alta",
        "responsibility": "Mista - avaliação técnica",
        "scenario": "A sinalização de capacidade em kg/pessoas diverge dos dados nominais homologados do equipamento, favorecendo uso acima do limite seguro.",
    },
    {
        "id": "elev-108",
        "slug": "ausencia-checklist-formal-pos-manutencao-corretiva",
        "title": "Ausência de Checklist Formal após Manutenção Corretiva",
        "description": "Sem checklist pós-serviço, falhas de ajuste e testes podem passar sem rastreabilidade.",
        "meta_description": "Ausência de checklist formal após manutenção corretiva reduz governança técnica e segurança operacional.",
        "keywords": "checklist manutenção elevador, pós-manutenção corretiva, rastreabilidade técnica, governança condominial",
        "severity": "Média",
        "severity_color": "yellow",
        "probability": 61,
        "severity_level": 64,
        "exposure": 71,
        "priority": 70,
        "probability_label": "Média",
        "severity_label": "Média",
        "priority_label": "Média",
        "responsibility": "Condomínio",
        "scenario": "Após intervenções corretivas, não há checklist formal de verificação funcional e de segurança, comprometendo validação final do serviço executado.",
    },
    {
        "id": "elev-109",
        "slug": "folga-critica-cabina-contrapeso-poco",
        "title": "Folga Crítica entre Cabina e Contrapeso no Poço",
        "description": "Folga insuficiente entre cabina e contrapeso pode gerar contato indevido e dano progressivo.",
        "meta_description": "Folga crítica entre cabina e contrapeso no poço exige verificação dimensional e correção imediata.",
        "keywords": "folga cabina contrapeso, poço do elevador, volume de segurança, contato indevido",
        "severity": "Crítica",
        "severity_color": "red",
        "probability": 57,
        "severity_level": 95,
        "exposure": 89,
        "priority": 93,
        "probability_label": "Média",
        "severity_label": "Crítica",
        "priority_label": "CRÍTICA",
        "responsibility": "Mista - avaliação técnica",
        "scenario": "A distância crítica entre cabina e contrapeso no poço está abaixo da condição segura, com potencial de contato em operação anormal.",
    },
    {
        "id": "elev-110",
        "slug": "abertura-porta-emergencia-sem-instrucao",
        "title": "Dispositivo de Abertura de Porta de Emergência sem Instrução",
        "description": "Sem instrução clara, o acionamento indevido em pânico aumenta risco de queda no poço.",
        "meta_description": "Dispositivo de abertura de emergência sem instruções claras eleva risco de acidente e deve ser corrigido.",
        "keywords": "abertura de emergência elevador, instrução de uso, risco de queda no poço, sinalização de segurança",
        "severity": "Alta",
        "severity_color": "orange",
        "probability": 62,
        "severity_level": 83,
        "exposure": 80,
        "priority": 87,
        "probability_label": "Média",
        "severity_label": "Alta",
        "priority_label": "Alta",
        "responsibility": "Condomínio",
        "scenario": "O dispositivo de abertura de porta de emergência não possui instruções objetivas de uso, aumentando probabilidade de acionamento inadequado por não treinados.",
    },
    {
        "id": "elev-111",
        "slug": "acabamento-solto-paineis-internos-cabina",
        "title": "Cabina com Acabamento Solto em Painéis Internos",
        "description": "Painéis internos soltos podem desprender, causar lesão e interferir no funcionamento das portas.",
        "meta_description": "Acabamentos soltos na cabina representam risco ao usuário e indicam falha de fixação e manutenção.",
        "keywords": "painel interno cabina, acabamento solto elevador, risco ao usuário, manutenção interna",
        "severity": "Média",
        "severity_color": "yellow",
        "probability": 59,
        "severity_level": 62,
        "exposure": 69,
        "priority": 68,
        "probability_label": "Média",
        "severity_label": "Média",
        "priority_label": "Média",
        "responsibility": "Mista - avaliação técnica",
        "scenario": "Foram observados painéis internos da cabina com fixação comprometida e acabamento solto, com potencial de desprendimento por vibração.",
    },
    {
        "id": "elev-112",
        "slug": "vibracao-excessiva-contrapeso",
        "title": "Excesso de Vibração no Contrapeso",
        "description": "Vibração elevada no contrapeso indica desalinhamento ou desgaste e acelera degradação do sistema.",
        "meta_description": "Excesso de vibração no contrapeso pode comprometer a corrida do elevador e requer diagnóstico dinâmico.",
        "keywords": "vibração contrapeso elevador, desalinhamento, trilhos, guiamento do elevador",
        "severity": "Alta",
        "severity_color": "orange",
        "probability": 65,
        "severity_level": 84,
        "exposure": 82,
        "priority": 88,
        "probability_label": "Média-Alta",
        "severity_label": "Alta",
        "priority_label": "Alta",
        "responsibility": "Condomínio",
        "scenario": "O contrapeso apresenta vibração excessiva durante a corrida, sugerindo desalinhamento, fixação inadequada ou desgaste no guiamento.",
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

    out = BASE_DIR / "batch_103_112_created_files.json"
    out.write_text(json.dumps(created_files, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\nArquivo de índice salvo em: {out.name}")


if __name__ == "__main__":
    main()
