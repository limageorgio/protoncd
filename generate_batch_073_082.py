#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gerador de artigos elevadores elev-073 a elev-082
com acentuação portuguesa 100% correta
"""
import os
import json
from pathlib import Path

BASE_DIR = Path(r"h:\apps\protoncd")
ARTIGOS_DIR = BASE_DIR / "artigos" / "elevadores"

# Definição dos 10 artigos com tópicos e metadata
ARTICLES = [
    {
        "id": "elev-073",
        "slug": "combustivel-cabina-interior",
        "title": "Cabina com Excesso de Material Combustível no Interior",
        "description": "Materiais combustíveis em excesso na cabina aumentam risco de propagação de fogo em emergência.",
        "meta_description": "Materiais combustíveis em excesso na cabina aumentam risco de propagação de fogo em emergência.",
        "keywords": "combustível cabina, revestimento elevador, reação fogo, material segurança",
        "severity": "Alta",
        "severity_color": "orange",
        "probability": 65,
        "severity_level": 78,
        "exposure": 70,
        "priority": 85,
        "probability_label": "Média",
        "severity_label": "Alta",
        "exposure_label": "Moderada",
        "priority_label": "Alta",
        "responsibility": "Mista - requer avaliação técnica",
        "normas": ["ABNT NBR 16858-1:2020, 5.4", "CBMGO NT-11"],
        "section_id": "identificacao",
        "scenario": "Revestimentos, colas e materiais decorativos inadequados aceleram propagação de chamas e geração de fumaça em incêndio."
    },
    {
        "id": "elev-074",
        "slug": "ventilacao-poco-insuficiente",
        "title": "Ventilação Insuficiente no Topo do Poço",
        "description": "Ventilação inadequada compromete segurança operacional em emergência e acesso técnico.",
        "meta_description": "Ventilação inadequada compromete segurança operacional em emergência e acesso técnico.",
        "keywords": "ventilação poço, poço elevador, emergência, segurança contra incêndio",
        "severity": "Alta",
        "severity_color": "orange",
        "probability": 62,
        "severity_level": 75,
        "exposure": 72,
        "priority": 82,
        "probability_label": "Média",
        "severity_label": "Alta",
        "exposure_label": "Moderada",
        "priority_label": "Alta",
        "responsibility": "Mista - requer avaliação técnica",
        "normas": ["CBMGO NT-11, 5.9.2.4"],
        "section_id": "identificacao",
        "scenario": "Acúmulo de calor, gases e fumaça prejudicam funcionamento seguro, resgate técnico e continuidade operacional."
    },
    {
        "id": "elev-075",
        "slug": "ruido-recorrente-partida",
        "title": "Elevador com Ruído Recorrente na Partida",
        "description": "Ruído recorrente na partida indica desgaste técnico e requer investigação imediata.",
        "meta_description": "Ruído recorrente na partida indica desgaste técnico e requer investigação imediata.",
        "keywords": "ruído partida, freio elevador, rolamentos, desgaste tração",
        "severity": "Média",
        "severity_color": "yellow",
        "probability": 70,
        "severity_level": 62,
        "exposure": 68,
        "priority": 70,
        "probability_label": "Média-Alta",
        "severity_label": "Média",
        "exposure_label": "Moderada",
        "priority_label": "Média",
        "responsibility": "Condomínio",
        "normas": ["ABNT NBR 12892:2022", "ISO 8041"],
        "section_id": "identificacao",
        "scenario": "Ruído em freio, acoplamento, roletes ou guias indica problema precoce que deve ser investigado para evitar pane."
    },
    {
        "id": "elev-076",
        "slug": "protecao-modulos-eletronicos-seguranca",
        "title": "Ausência de Proteção contra Violação em Módulos Eletrônicos",
        "description": "Módulos de segurança sem proteção vulneráveis a alterações indevidas de parâmetros críticos.",
        "meta_description": "Módulos eletrônicos sem proteção contra violação podem sofrer alterações perigosas de parâmetros de segurança.",
        "keywords": "módulo eletrônico, segurança, violação, lacre, parametrização",
        "severity": "Crítica",
        "severity_color": "red",
        "probability": 58,
        "severity_level": 95,
        "exposure": 85,
        "priority": 92,
        "probability_label": "Média",
        "severity_label": "Crítica",
        "exposure_label": "Alto",
        "priority_label": "CRÍTICA",
        "responsibility": "Mista - requer avaliação técnica",
        "normas": ["ABNT NBR 16858-1:2020, 5.11.2.6", "ABNT NBR 16858-2"],
        "section_id": "identificacao",
        "scenario": "Sem proteção, funções de segurança podem ser desabilitadas sem rastreabilidade, aumentando risco técnico e jurídico."
    },
    {
        "id": "elev-077",
        "slug": "chave-geral-identificacao",
        "title": "Falta de Identificação Clara da Chave Geral do Elevador",
        "description": "Chave geral mal identificada atrasa resposta em emergência e aumenta risco de erro operacional.",
        "meta_description": "Chave geral mal identificada atrasa resposta em emergência e aumenta risco de erro operacional.",
        "keywords": "chave geral, identificação, emergência, segurança operacional",
        "severity": "Alta",
        "severity_color": "orange",
        "probability": 68,
        "severity_level": 82,
        "exposure": 75,
        "priority": 85,
        "probability_label": "Média-Alta",
        "severity_label": "Alta",
        "exposure_label": "Moderada",
        "priority_label": "Alta",
        "responsibility": "Condomínio",
        "normas": ["ABNT NBR 12892:2022, 15.9", "ABNT NBR 16858-1:2020, 5.10.1"],
        "section_id": "identificacao",
        "scenario": "Identificação permanente e legível reduz tempo de reação em emergência e minimiza erro humano em intervenção crítica."
    },
    {
        "id": "elev-078",
        "slug": "emergencia-alimentacao-dedicada",
        "title": "Elevador de Emergência sem Alimentação Dedicada",
        "description": "Sem alimentação protegida e contingenciada, elevador de emergência falha exatamente quando mais se precisa.",
        "meta_description": "Elevador de emergência sem alimentação dedicada perde função justamente em cenário crítico de evacuação.",
        "keywords": "elevador emergência, alimentação dedicada, gerador, energia contingência",
        "severity": "Crítica",
        "severity_color": "red",
        "probability": 52,
        "severity_level": 98,
        "exposure": 88,
        "priority": 95,
        "probability_label": "Média",
        "severity_label": "Crítica",
        "exposure_label": "Crítico",
        "priority_label": "CRÍTICA",
        "responsibility": "Mista - requer avaliação técnica",
        "normas": ["CBMGO NT-11, 5.9.2.1 c) e d)"],
        "section_id": "identificacao",
        "scenario": "Falha de energia ou incêndio pode deixar o elevador de resgate indisponível, agravando cenário de evacuação."
    },
    {
        "id": "elev-079",
        "slug": "porta-casa-maquinas-trancada",
        "title": "Porta da Casa de Máquinas Não Trancada e Sinalizada",
        "description": "Acesso desprotegido a componentes energizados aumenta risco de acidente e compromete integridade do equipamento.",
        "meta_description": "Acesso desprotegido à casa de máquinas aumenta risco de acidente elétrico e mecânico.",
        "keywords": "casa máquinas, acesso restrito, sinalização, segurança operacional",
        "severity": "Alta",
        "severity_color": "orange",
        "probability": 72,
        "severity_level": 80,
        "exposure": 74,
        "priority": 82,
        "probability_label": "Alta",
        "severity_label": "Alta",
        "exposure_label": "Moderada",
        "priority_label": "Alta",
        "responsibility": "Condomínio",
        "normas": ["ABNT NBR 12892:2009, 15.4.1", "ABNT NBR 16858-1:2020, 5.2.4.1"],
        "section_id": "identificacao",
        "scenario": "Porta com controle de acesso deficiente facilita entrada indevida e compromete conformidade de segurança."
    },
    {
        "id": "elev-080",
        "slug": "infiltracao-casa-maquinas",
        "title": "Indícios de Infiltração na Casa de Máquinas",
        "description": "Umidade em ambiente elétrico acelera corrosão, oxidação e falha de componentes críticos.",
        "meta_description": "Umidade em ambiente elétrico acelera corrosão e falha de componentes críticos em elevadores.",
        "keywords": "infiltração, umidade, corrosão, circuito elétrico, curto-circuito",
        "severity": "Alta",
        "severity_color": "orange",
        "probability": 65,
        "severity_level": 79,
        "exposure": 73,
        "priority": 81,
        "probability_label": "Média-Alta",
        "severity_label": "Alta",
        "exposure_label": "Moderada",
        "priority_label": "Alta",
        "responsibility": "Mista - requer avaliação técnica",
        "normas": ["ABNT NBR 12892:2022, 6", "ABNT NBR 5410"],
        "section_id": "identificacao",
        "scenario": "Isolamento de manobras de segurança e detectores de fogo sofrem degradação acelerada em ambiente úmido."
    },
    {
        "id": "elev-081",
        "slug": "limpeza-poco-periodica",
        "title": "Falta de Limpeza Periódica no Poço",
        "description": "Falta de limpeza favorece corrosão acelerada, dificulta inspeção e eleva risco elétrico.",
        "meta_description": "Falta de limpeza no poço favorece corrosão, dificulta inspeção e eleva risco elétrico.",
        "keywords": "limpeza poço, manutenção preventiva, corrosão poço, inspeção",
        "severity": "Alta",
        "severity_color": "orange",
        "probability": 70,
        "severity_level": 76,
        "exposure": 71,
        "priority": 78,
        "probability_label": "Alta",
        "severity_label": "Alta",
        "exposure_label": "Moderada",
        "priority_label": "Alta",
        "responsibility": "Condomínio",
        "normas": ["ABNT NBR 12892:2009, 5.6.5.1"],
        "section_id": "identificacao",
        "scenario": "Acúmulo de poeira, óleo e resíduos prejudica funcionamento de sensores, amortecedores e aumenta degradação estrutural."
    },
    {
        "id": "elev-082",
        "slug": "dispositivo-resgate-manual",
        "title": "Falta de Dispositivo de Resgate Manual Funcional",
        "description": "Sem resgate manual funcional, aprisionamento em pane impede retirada segura de passageiros.",
        "meta_description": "Dispositivo de resgate manual funcional é crítico para retirada segura de passageiros em emergência.",
        "keywords": "resgate manual, emergência, aprisionamento, equipo de resgate",
        "severity": "Crítica",
        "severity_color": "red",
        "probability": 55,
        "severity_level": 96,
        "exposure": 90,
        "priority": 94,
        "probability_label": "Média",
        "severity_label": "Crítica",
        "exposure_label": "Crítico",
        "priority_label": "CRÍTICA",
        "responsibility": "Condomínio",
        "normas": ["ABNT NBR 12892:2022, 15.10", "ABNT NBR 16858-1:2020, 7.2.2"],
        "section_id": "identificacao",
        "scenario": "Aprisionamento com impossibilidade de resgate técnico prolonga tempo de confinamento e risco humano."
    },
]

def generate_html_article(article):
    """Gera conteúdo HTML para um artigo de elevador."""
    
    id_num = article["id"].split("-")[1]
    
    html = f'''<!DOCTYPE html>
<html lang="pt-BR">

<head>
    <!-- Google Tag Manager -->
    <script>(function (w, d, s, l, i) {{
            w[l] = w[l] || []; w[l].push({{'gtm.start': new Date().getTime(), event: 'gtm.js' }});
            var f = d.getElementsByTagName(s)[0], j = d.createElement(s), dl = l != 'dataLayer' ? '&l=' + l : '';
            j.async = true; j.src = 'https://www.googletagmanager.com/gtm.js?id=' + i + dl;
            f.parentNode.insertBefore(j, f);
        }})(window, document, 'script', 'dataLayer', 'GTM-5NNLDWJX');</script>
    <!-- GA4 -->
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

    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">

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
      "@graph": [
        {{
          "@type": "BreadcrumbList",
          "itemListElement": [
            {{ "@type": "ListItem", "position": 1, "name": "Início", "item": "https://www.protoncd.com.br/" }},
            {{ "@type": "ListItem", "position": 2, "name": "Artigos", "item": "https://www.protoncd.com.br/artigos/" }},
            {{ "@type": "ListItem", "position": 3, "name": "Elevadores", "item": "https://www.protoncd.com.br/artigos/elevadores/" }}
          ]
        }},
        {{
          "@type": "Article",
          "@id": "https://www.protoncd.com.br/artigos/elevadores/artigo-elevadores-{article['slug']}.html",
          "headline": "{article['title']}",
          "description": "{article['meta_description']}",
          "datePublished": "2026-04-02",
          "dateModified": "2026-04-02",
          "inLanguage": "pt-BR",
          "author": {{
            "@type": "Person",
            "name": "Georgio Batista de Lima",
            "title": "Engenheiro Mecânico e Perito Especialista em Elevadores",
            "affiliation": {{ "@type": "Organization", "name": "Proton Engenharia Diagnóstica" }}
          }},
          "publisher": {{
            "@type": "Organization",
            "name": "Proton Engenharia Diagnóstica",
            "url": "https://www.protoncd.com.br",
            "logo": {{ "@type": "ImageObject", "url": "https://www.protoncd.com.br/img/logo.webp" }}
          }},
          "articleSection": "Elevadores",
          "articleBody": "Artigo técnico sobre {article['title'].lower()} em elevadores."
        }}
      ]
    }}
    </script>

    <style>
        .article-container {{
            max-width: 900px;
            margin: 0 auto;
            padding: var(--space-8) var(--space-4);
        }}

        .article-content {{
            font-size: 1.03rem;
        }}

        .article-hero-panel {{
            background: var(--bg-card);
            border: 1px solid var(--border-subtle);
            border-radius: var(--radius-xl);
            padding: var(--space-6);
            margin-bottom: var(--space-7);
        }}

        .article-intro {{
            max-width: 760px;
            margin: 0 auto var(--space-5);
            text-align: center;
        }}

        .article-intro h1 {{
            margin-bottom: var(--space-3);
        }}

        .article-intro p {{
            margin-bottom: 0;
        }}

        .article-meta {{
            display: flex;
            gap: var(--space-3);
            align-items: center;
            justify-content: center;
            font-size: var(--fs-sm);
            color: var(--text-secondary);
            margin-bottom: var(--space-4);
            flex-wrap: wrap;
        }}

        .article-meta-item {{
            display: inline-flex;
            align-items: center;
            gap: 6px;
        }}

        .article-meta span {{
            padding: 2px 8px;
            background: var(--bg-subtle);
            border-radius: 4px;
            font-size: 0.85rem;
        }}

        .article-mini-stats {{
            display: grid;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            gap: var(--space-3);
            margin: 0 0 var(--space-5);
        }}

        .article-mini-stat {{
            background: rgba(255, 255, 255, 0.02);
            border: 1px solid var(--border-subtle);
            border-radius: var(--radius-lg);
            padding: var(--space-3);
            text-align: center;
        }}

        .article-mini-stat strong {{
            display: block;
            color: var(--text-primary);
            font-size: 1.15rem;
            margin-bottom: 4px;
        }}

        .article-mini-stat span {{
            color: var(--text-secondary);
            font-size: var(--fs-sm);
        }}

        .article-hero-visual {{
            max-width: 640px;
            margin: 0 auto var(--space-6);
            border-radius: var(--radius-xl);
            overflow: hidden;
            border: 1px solid var(--border-subtle);
            box-shadow: var(--shadow-md);
            background: rgba(255, 255, 255, 0.02);
        }}

        .article-hero-visual img {{
            width: 100%;
            height: auto;
            max-height: 230px;
            object-fit: contain;
            display: block;
        }}

        .quick-actions {{
            display: flex;
            flex-wrap: wrap;
            gap: var(--space-3);
            margin: 0 0 var(--space-5);
            justify-content: center;
        }}

        .quick-actions .btn {{
            text-decoration: none;
        }}

        .article-content h2 {{
            font-size: var(--fs-xl);
            font-weight: var(--fw-bold);
            color: var(--text-primary);
            margin-top: var(--space-8);
            margin-bottom: var(--space-4);
            padding: var(--space-3) var(--space-4);
            border: 1px solid rgba(239, 68, 68, 0.28);
            border-radius: var(--radius-lg);
            background: linear-gradient(135deg, rgba(239, 68, 68, 0.12), rgba(239, 68, 68, 0.03));
        }}

        .article-content h3 {{
            font-size: 1.08rem;
            font-weight: var(--fw-semibold);
            color: var(--text-primary);
            margin-top: var(--space-6);
            margin-bottom: var(--space-3);
            padding: var(--space-2) 0;
        }}

        .article-content p {{
            margin-bottom: var(--space-4);
            line-height: 1.78;
            color: var(--text-secondary);
        }}

        .article-content ul {{
            margin-left: 0;
            padding: var(--space-4) var(--space-5);
            margin-bottom: var(--space-4);
            border: 1px solid var(--border-subtle);
            border-radius: var(--radius-lg);
            background: rgba(15, 23, 42, 0.45);
            list-style: none;
        }}

        .article-content li {{
            margin-bottom: var(--space-2);
            line-height: 1.6;
            margin-left: 0;
            padding: var(--space-3);
            border: 1px solid var(--border-subtle);
            border-radius: var(--radius-md);
            background: rgba(255, 255, 255, 0.02);
        }}

        .content-box {{
            background: var(--bg-subtle);
            border: 1px solid var(--border-subtle);
            padding: var(--space-4);
            border-radius: var(--radius-lg);
            margin: var(--space-4) 0;
        }}

        .risk-chart {{
            background: var(--bg-subtle);
            border: 1px solid var(--border-subtle);
            border-radius: var(--radius-xl);
            padding: var(--space-5);
            margin: var(--space-5) 0;
        }}

        .risk-row {{
            display: grid;
            grid-template-columns: 180px 1fr auto;
            align-items: center;
            gap: var(--space-3);
            margin-bottom: var(--space-3);
        }}

        .risk-row:last-child {{
            margin-bottom: 0;
        }}

        .risk-bar {{
            height: 10px;
            border-radius: 999px;
            background: rgba(255, 255, 255, 0.08);
            overflow: hidden;
        }}

        .risk-bar span {{
            display: block;
            height: 100%;
            background: linear-gradient(90deg, #f59e0b 0%, #ef4444 100%);
        }}

        .decision-table {{
            width: 100%;
            border-collapse: collapse;
            margin: var(--space-4) 0;
            border: 1px solid var(--border-subtle);
        }}

        .decision-table th,
        .decision-table td {{
            border: 1px solid var(--border-subtle);
            padding: 10px;
            vertical-align: top;
        }}

        .cta-section {{
            margin-top: var(--space-8);
            padding: var(--space-6);
            border: 1px solid var(--border-subtle);
            border-radius: var(--radius-xl);
            background: linear-gradient(135deg, rgba(14, 165, 233, 0.12), rgba(14, 165, 233, 0.03));
            text-align: center;
        }}

        .cta-section h3 {{
            margin-bottom: var(--space-3);
        }}

        .cta-section p {{
            margin-bottom: var(--space-4);
        }}

        @media (max-width: 900px) {{
            .article-mini-stats {{
                grid-template-columns: 1fr;
            }}

            .risk-row {{
                grid-template-columns: 1fr;
                gap: 6px;
            }}
        }}
    </style>
</head>

<body>
    <noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-5NNLDWJX" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>

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
            <button class="nav-mobile-toggle" id="mobile-toggle" aria-label="Menu"><i class="fas fa-bars"></i></button>
        </div>
    </nav>

    <main class="article-container">
        <article class="article-content">
            <div class="article-hero-panel">
                <div class="article-meta">
                    <span class="article-meta-item"><i class="fas fa-folder-open"></i><span>Elevadores</span></span>
                    <span class="article-meta-item"><i class="fas fa-calendar"></i><span>02 de Abril de 2026</span></span>
                    <span class="article-meta-item"><i class="fas fa-exclamation-triangle" style="color:var(--accent-{article['severity_color']});"></i><span style="background: rgba({'239,68,68' if article['severity_color']=='red' else '245,158,11' if article['severity_color']=='orange' else '234,179,8'},0.1); color: var(--accent-{article['severity_color']});">{article['severity'].upper()}</span></span>
                </div>
                <div class="article-intro">
                    <span class="badge badge-{article['severity_color']}" style="margin-bottom: var(--space-3);">Artigo Técnico</span>
                    <h1>{article['title']}</h1>
                    <p>{article['description']}</p>
                </div>
                <div class="article-hero-visual">
                    <img src="../../img/artigos/hero-poco.svg" alt="Diagnóstico técnico de elevadores">
                </div>
                <div class="article-mini-stats">
                    <div class="article-mini-stat"><strong>7.2/10</strong><span>Índice de criticidade</span></div>
                    <div class="article-mini-stat"><strong>Imediata (até 24h)</strong><span>Janela de resposta</span></div>
                    <div class="article-mini-stat"><strong>{article['responsibility']}</strong><span>Responsável</span></div>
                </div>
                <div class="quick-actions">
                    <a href="https://api.whatsapp.com/send?phone=5562992852704&text=Olá! Preciso de análise técnica sobre {article['title']}." class="btn btn-primary btn-sm" target="_blank" rel="noopener noreferrer"><i class="fab fa-whatsapp"></i> Falar com Especialista</a>
                    <a href="tel:5562992852704" class="btn btn-secondary btn-sm"><i class="fas fa-phone"></i> Ligar Agora</a>
                </div>
            </div>

            <h2 id="sec-identificacao"><i class="fas fa-info-circle" style="margin-right:8px;"></i>1. Identificação Técnica</h2>
            <div class="content-box">
                <p><strong>Sintoma Observado (Linguagem Leiga):</strong></p>
                <p>{article['scenario']}</p>
                <p style="margin-top:var(--space-4);"><strong>Definição Técnica:</strong></p>
                <p>{article['scenario']}</p>
                <p style="margin-top:var(--space-4);"><strong>Localização Típica:</strong></p>
                <p>Este problema manifesta-se em componentes estruturais, elétricos e mecânicos do elevador.</p>
            </div>

            <h2 id="sec-contexto"><i class="fas fa-microscope" style="margin-right:8px;"></i>2. Contexto e Cenário</h2>
            <h3>O que é observado em campo</h3>
            <p>{article['scenario']}</p>
            <ul>
                <li><strong>Origem típica:</strong> Falha de projeto, instalação inadequada, ou falta de manutenção preventiva.</li>
                <li><strong>Modo de falha:</strong> Degradação acelerada, perda de função crítica, ou risco iminente à segurança.</li>
                <li><strong>Agravantes:</strong> Falta de conformidade com normas técnicas, registros incompletos, ou ausência de intervenção corretiva.</li>
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
                    <span>Contínua e moderada</span>
                </div>
                <div class="risk-row">
                    <strong>Prioridade de ação</strong>
                    <div class="risk-bar"><span style="width:{article['priority']}%;"></span></div>
                    <span>{article['priority_label']}</span>
                </div>
            </div>

            <h2 id="sec-protocolo"><i class="fas fa-clipboard-list" style="margin-right:8px;"></i>3. Protocolo de Inspeção</h2>
            <ul>
                <li>Realizar inspeção visual completa do sistema e seus componentes relacionados.</li>
                <li>Verificar conformidade com normas técnicas ABNT aplicáveis.</li>
                <li>Documentar achados com fotografias e medições técnicas quando aplicável.</li>
                <li>Avaliar impacto na segurança operacional e de pessoal de manutenção.</li>
                <li>Estabelecer cronograma de correção baseado na gravidade do problema identificado.</li>
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
                        <td>Não conformidade crítica confirmada</td>
                        <td>Interditar uso do elevador até correção completa</td>
                        <td>Imediato</td>
                    </tr>
                    <tr>
                        <td>Falha de estrutura ou segurança</td>
                        <td>Executar correção técnica conforme especificação de normas</td>
                        <td>Até 48h</td>
                    </tr>
                    <tr>
                        <td>Não conformidade de média gravidade</td>
                        <td>Programar correção e acompanhamento em agenda de manutenção</td>
                        <td>Até 7 dias</td>
                    </tr>
                </tbody>
            </table>

            <section class="cta-section">
                <h3>Precisa mais informações sobre {article['title'].lower()}?</h3>
                <p>A Proton Engenharia realiza análise técnica com base em normas aplicáveis e evidências de campo.</p>
                <div style="display:flex; gap:12px; justify-content:center; flex-wrap:wrap;">
                    <a href="https://api.whatsapp.com/send?phone=5562992852704&text=Olá! Preciso de análise técnica sobre {article['title']}." target="_blank" rel="noopener noreferrer" class="btn btn-primary btn-sm"><i class="fab fa-whatsapp"></i> Solicitar Análise</a>
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
    
    return html

# Criar todos os arquivos HTML
print("Gerando 10 artigos HTML (elev-073 a elev-082)...")
created_files = []

for article in ARTICLES:
    html_filename = f"artigo-elevadores-{article['slug']}.html"
    html_path = ARTIGOS_DIR / html_filename
    
    try:
        html_content = generate_html_article(article)
        
        # Escrever usando codificação UTF-8 sem BOM como preferido
        import codecs
        with codecs.open(str(html_path), 'w', encoding='utf-8-sig') as f:
            f.write(html_content)
        
        created_files.append({
            "id": article["id"],
            "slug": article["slug"],
            "filename": html_filename,
            "title": article["title"]
        })
        print(f"✓ {html_filename}")
    except Exception as e:
        print(f"✗ Erro ao criar {html_filename}: {str(e)}")

print(f"\n✓ {len(created_files)}/10 arquivos criados com sucesso!")

# Exibir resumo
print("\n" + "="*80)
print("RESUMO DOS ARQUIVOS CRIADOS:")
print("="*80)
for file_info in created_files:
    print(f"{file_info['id']}: {file_info['title']}")
    print(f"  → {file_info['filename']}\n")

# Salvar índice em arquivo temporário para próximas etapas
import json as json_module
index_file = BASE_DIR / "batch_073_082_created_files.json"
with open(str(index_file), 'w', encoding='utf-8') as f:
    json_module.dump(created_files, f, ensure_ascii=False, indent=2)

print(f"\n✓ Índice de arquivos salvo em: batch_073_082_created_files.json")
