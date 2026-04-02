#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gerador de artigos elevadores elev-113 a elev-122.
"""

import json
from pathlib import Path

BASE_DIR = Path(r"h:\apps\protoncd")
ARTIGOS_DIR = BASE_DIR / "artigos" / "elevadores"

ARTICLES = [
    {
        "id": "elev-113",
        "slug": "sensor-porta-bypass-temporario",
        "title": "Sensor de Porta em Bypass Temporário",
        "description": "Bypass de sensor de porta remove proteção essencial e expõe passageiros a risco imediato.",
        "meta_description": "Operar elevador com sensor de porta em bypass temporário eleva risco crítico e exige retirada imediata de serviço.",
        "keywords": "sensor de porta elevador, bypass temporário, segurança de portas, risco crítico elevador",
        "severity": "Crítica",
        "severity_color": "red",
        "probability": 66,
        "severity_level": 95,
        "exposure": 90,
        "priority": 94,
        "probability_label": "Média-Alta",
        "severity_label": "Crítica",
        "priority_label": "CRÍTICA",
        "responsibility": "Condomínio",
        "scenario": "Foi identificado bypass temporário no sensor de porta para manter operação do elevador, removendo proteção de fechamento seguro e elevando risco imediato a usuários.",
    },
    {
        "id": "elev-114",
        "slug": "comando-prioridade-bombeiro-inoperante",
        "title": "Comando de Prioridade de Bombeiro Inoperante",
        "description": "Sem comando funcional de bombeiro, o elevador de emergência perde capacidade de resposta em incêndio.",
        "meta_description": "Comando de prioridade de bombeiro inoperante compromete estratégia de resgate e caracteriza não conformidade crítica.",
        "keywords": "prioridade de bombeiro, elevador de emergência, pavimento de descarga, resgate em incêndio",
        "severity": "Crítica",
        "severity_color": "red",
        "probability": 61,
        "severity_level": 95,
        "exposure": 88,
        "priority": 93,
        "probability_label": "Média",
        "severity_label": "Crítica",
        "priority_label": "CRÍTICA",
        "responsibility": "Mista - requer avaliação técnica",
        "scenario": "O comando de prioridade de bombeiro não assume controle no pavimento de descarga conforme requisito operacional de emergência, comprometendo o plano de resposta do edifício.",
    },
    {
        "id": "elev-115",
        "slug": "ausencia-redundancia-circuitos-criticos-seguranca",
        "title": "Ausência de Redundância em Circuitos Críticos de Segurança",
        "description": "Sem redundância mínima, uma falha única pode evoluir para condição insegura no sistema.",
        "meta_description": "Ausência de redundância em circuitos críticos de segurança aumenta vulnerabilidade do elevador e exige revisão de arquitetura.",
        "keywords": "redundância elevador, circuitos críticos, falha única, arquitetura de segurança",
        "severity": "Crítica",
        "severity_color": "red",
        "probability": 58,
        "severity_level": 94,
        "exposure": 86,
        "priority": 92,
        "probability_label": "Média",
        "severity_label": "Crítica",
        "priority_label": "CRÍTICA",
        "responsibility": "Mista - requer avaliação técnica",
        "scenario": "Na análise de segurança, verificou-se ausência de redundância e monitoramento adequado em circuitos críticos, reduzindo tolerância a falhas e capacidade de entrada em estado seguro.",
    },
    {
        "id": "elev-116",
        "slug": "falha-recorrente-nivelamento-elevador",
        "title": "Falha Recorrente de Nivelamento do Elevador",
        "description": "Desnível recorrente de parada eleva risco de queda e compromete acessibilidade dos usuários.",
        "meta_description": "Falha recorrente de nivelamento exige ação imediata e pode demandar restrição de operação até correção técnica.",
        "keywords": "nivelamento elevador, desnível de parada, risco de queda, acessibilidade",
        "severity": "Alta",
        "severity_color": "orange",
        "probability": 67,
        "severity_level": 84,
        "exposure": 82,
        "priority": 88,
        "probability_label": "Média-Alta",
        "severity_label": "Alta",
        "priority_label": "Alta",
        "responsibility": "Condomínio",
        "scenario": "O elevador apresenta falha recorrente de nivelamento em mais de um pavimento, gerando degrau de embarque e risco de tropeço para usuários.",
    },
    {
        "id": "elev-117",
        "slug": "bateria-emergencia-sem-autonomia-comprovada",
        "title": "Bateria de Emergência sem Autonomia Comprovada",
        "description": "Sem comprovação de autonomia, iluminação e comunicação de emergência podem falhar durante pane.",
        "meta_description": "Bateria de emergência sem testes e autonomia comprovada fragiliza o plano de segurança do elevador.",
        "keywords": "bateria de emergência elevador, autonomia, iluminação de emergência, comunicação de pane",
        "severity": "Alta",
        "severity_color": "orange",
        "probability": 63,
        "severity_level": 83,
        "exposure": 79,
        "priority": 86,
        "probability_label": "Média-Alta",
        "severity_label": "Alta",
        "priority_label": "Alta",
        "responsibility": "Condomínio",
        "scenario": "Não há registro técnico recente que comprove autonomia real da bateria de emergência para manter iluminação e comunicação mínimas em evento de falha de energia.",
    },
    {
        "id": "elev-118",
        "slug": "ruido-acima-padrao-multiplos-pavimentos",
        "title": "Ruído Acima do Padrão em Múltiplos Pavimentos",
        "description": "Ruído recorrente em vários trechos da corrida indica potencial falha sistêmica do conjunto.",
        "meta_description": "Ruído acima do padrão em múltiplos pavimentos exige diagnóstico sistêmico com correlação de vibração.",
        "keywords": "ruído elevador, vibração elevador, falha sistêmica, diagnóstico de corrida",
        "severity": "Média",
        "severity_color": "yellow",
        "probability": 64,
        "severity_level": 66,
        "exposure": 74,
        "priority": 72,
        "probability_label": "Média-Alta",
        "severity_label": "Média",
        "priority_label": "Média",
        "responsibility": "Condomínio",
        "scenario": "Foram reportados níveis de ruído acima do padrão em múltiplos pavimentos, sugerindo causa sistêmica associada à tração, guiamento ou sistema de portas.",
    },
    {
        "id": "elev-119",
        "slug": "falta-trava-eletrica-acesso-tecnico-poco",
        "title": "Falta de Trava Elétrica em Acesso Técnico ao Poço",
        "description": "Sem intertravamento elétrico no acesso técnico, há risco crítico de movimento indevido.",
        "meta_description": "Acesso técnico ao poço sem trava elétrica é falha crítica de segurança e requer correção imediata.",
        "keywords": "trava elétrica elevador, intertravamento, acesso ao poço, segurança de manutenção",
        "severity": "Crítica",
        "severity_color": "red",
        "probability": 59,
        "severity_level": 95,
        "exposure": 89,
        "priority": 93,
        "probability_label": "Média",
        "severity_label": "Crítica",
        "priority_label": "CRÍTICA",
        "responsibility": "Condomínio",
        "scenario": "O acesso técnico ao poço não possui intertravamento elétrico eficaz, permitindo condição em que o elevador pode operar com abertura em estado inseguro.",
    },
    {
        "id": "elev-120",
        "slug": "ausencia-plano-manutencao-preventiva-formal",
        "title": "Ausência de Plano de Manutenção Preventiva Formal",
        "description": "Sem plano formal, a gestão fica reativa e o risco de panes e custos cresce.",
        "meta_description": "Ausência de plano de manutenção preventiva formal reduz previsibilidade técnica e conformidade operacional do elevador.",
        "keywords": "manutenção preventiva elevador, plano formal, conformidade ABNT, gestão condominial",
        "severity": "Alta",
        "severity_color": "orange",
        "probability": 68,
        "severity_level": 82,
        "exposure": 81,
        "priority": 87,
        "probability_label": "Média-Alta",
        "severity_label": "Alta",
        "priority_label": "Alta",
        "responsibility": "Condomínio",
        "scenario": "O condomínio não mantém plano formal de manutenção preventiva, com rotina predominantemente reativa e baixa rastreabilidade de intervenções técnicas.",
    },
    {
        "id": "elev-121",
        "slug": "controle-sobrecarga-sem-teste-periodico",
        "title": "Controle de Sobrecarga sem Teste Periódico",
        "description": "Sem teste funcional periódico, o controle de sobrecarga pode falhar sem alerta prévio.",
        "meta_description": "Controle de sobrecarga sem teste periódico aumenta risco de operação acima da capacidade nominal.",
        "keywords": "sobrecarga elevador, teste periódico, capacidade nominal, segurança operacional",
        "severity": "Alta",
        "severity_color": "orange",
        "probability": 65,
        "severity_level": 83,
        "exposure": 80,
        "priority": 87,
        "probability_label": "Média-Alta",
        "severity_label": "Alta",
        "priority_label": "Alta",
        "responsibility": "Condomínio",
        "scenario": "O sistema de controle de sobrecarga não possui evidência de teste funcional periódico, permitindo degradação silenciosa até ocorrência real.",
    },
    {
        "id": "elev-122",
        "slug": "revalidacao-itens-criticos-apos-modernizacao",
        "title": "Revalidação de Itens Críticos após Modernização do Elevador",
        "description": "Modernização sem revalidação completa pode deixar defeitos de integração ocultos.",
        "meta_description": "Após modernização, a revalidação dos itens críticos é indispensável para liberar operação com segurança.",
        "keywords": "modernização elevador, comissionamento, revalidação de segurança, integração de sistemas",
        "severity": "Crítica",
        "severity_color": "red",
        "probability": 57,
        "severity_level": 94,
        "exposure": 87,
        "priority": 92,
        "probability_label": "Média",
        "severity_label": "Crítica",
        "priority_label": "CRÍTICA",
        "responsibility": "Mista - requer avaliação técnica",
        "scenario": "Após modernização relevante do sistema, não foi apresentada revalidação técnica completa dos itens críticos de segurança antes da liberação operacional.",
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

    out = BASE_DIR / "batch_113_122_created_files.json"
    out.write_text(json.dumps(created_files, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\nArquivo de índice salvo em: {out.name}")


if __name__ == "__main__":
    main()
