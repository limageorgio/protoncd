#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate missing playground articles from FAQ JSON
"""
import json
import os
from datetime import datetime
from pathlib import Path

# Configuration
JSON_PATH = r"h:\apps\protoncd\conhecimento-tecnico\dados\playgrounds.json"
PLAYGROUNDS_DIR = r"h:\apps\protoncd\artigos\playgrounds"

# Load JSON
with open(JSON_PATH, 'r', encoding='utf-8') as f:
    data = json.load(f)

faqs_by_id = {faq['id']: faq for faq in data['faqs']}

# Missing articles mapping
missing_ids = [
    ("play-001", "ferrugem-desgaste"),
    ("play-002", "abertura-piso"),
    ("play-003", "impacto-assentos"),
    ("play-004", "acumulo-agua"),
    ("play-006", "alcas-suspensas"),
    ("play-007", "cordas-cabos"),
    ("play-008", "acessibilidade"),
    ("play-009", "altura-assentos"),
    ("play-010", "piso-queda"),
    ("play-011", "borda-saida-escorregador")
]

def generate_html(faq_id, slug, faq_data):
    """Generate HTML article from FAQ data"""
    
    pergunta = faq_data.get('pergunta', '')
    resposta = faq_data.get('resposta', '')
    normas = faq_data.get('normas', [])
    gravidade = faq_data.get('gravidade', 'Média')
    responsabilidade = faq_data.get('responsabilidade', '')
    
    # Extract title from question
    title = pergunta.split('?')[0].strip()
    if title.startswith("'") or title.startswith("Essa situação de") or title.startswith("Com"):
        # Clean up title
        parts = title.split("'")
        if len(parts) > 1:
            title = parts[1]
    
    # Create canonical and URLs
    canonical = f"https://www.protoncd.com.br/artigos/playgrounds/artigo-playground-{slug}.html"
    file_path = os.path.join(PLAYGROUNDS_DIR, f"artigo-playground-{slug}.html")
    
    # Build HTML
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
    <meta name="description" content="{title}: análise técnica de segurança infantil em playgrounds conforme ABNT NBR 16071.">
    <meta name="keywords" content="playground, segurança infantil, ABNT NBR 16071, inspeção, {slug.replace('-', ', ')}">
    <meta name="author" content="Proton Engenharia Diagnóstica">

    <title>{title} | Proton Engenharia</title>

    <!-- Canonical -->
    <link rel="canonical" href="{canonical}">
    <link rel="alternate" hreflang="pt-BR" href="{canonical}">

    <!-- Open Graph -->
    <meta property="og:type" content="article">
    <meta property="og:url" content="{canonical}">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{title}: protocolo técnico conforme ABNT NBR 16071.">
    <meta property="og:site_name" content="Proton Engenharia Diagnóstica">
    <meta property="og:locale" content="pt_BR">
    <meta property="og:image" content="https://www.protoncd.com.br/img/logo_proton1x1.jpg">
    <meta property="article:published_time" content="2026-04-02">
    <meta property="article:author" content="Georgio Batista de Lima">
    <meta property="article:section" content="Playgrounds">

    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{title}">
    <meta name="twitter:description" content="Análise técnica de segurança: {title}">

    <!-- CSS -->
    <link rel="stylesheet" href="../../css/all.min.css">
    <link rel="icon" href="../../img/faviconb.ico" type="image/x-icon">
    <link rel="stylesheet" href="../../css/variables.css">
    <link rel="stylesheet" href="../../css/base.css">
    <link rel="stylesheet" href="../../css/components.css">
    <link rel="stylesheet" href="../../css/layout.css">
    <link rel="stylesheet" href="../../css/animations.css">

    <!-- Schema.org -->
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@graph": [
        {{
          "@type": "BreadcrumbList",
          "itemListElement": [
            {{ "@type": "ListItem", "position": 1, "name": "Início", "item": "https://www.protoncd.com.br/" }},
            {{ "@type": "ListItem", "position": 2, "name": "Artigos", "item": "https://www.protoncd.com.br/artigos/" }},
            {{ "@type": "ListItem", "position": 3, "name": "Playgrounds", "item": "https://www.protoncd.com.br/artigos/playgrounds/" }},
            {{ "@type": "ListItem", "position": 4, "name": "{title}", "item": "{canonical}" }}
          ]
        }},
        {{
          "@type": "Article",
          "@id": "{canonical}",
          "headline": "{title}",
          "description": "Análise técnica de segurança infantil baseada em normativa ABNT NBR 16071.",
          "datePublished": "2026-04-02",
          "dateModified": "2026-04-02",
          "inLanguage": "pt-BR",
          "author": {{
            "@type": "Person",
            "name": "Georgio Batista de Lima",
            "affiliation": {{ "@type": "Organization", "name": "Proton Engenharia Diagnóstica" }}
          }},
          "publisher": {{
            "@type": "Organization",
            "name": "Proton Engenharia Diagnóstica",
            "url": "https://www.protoncd.com.br",
            "logo": {{ "@type": "ImageObject", "url": "https://www.protoncd.com.br/img/logo.webp" }}
          }},
          "articleSection": "Playgrounds",
          "articleBody": "Artigo técnico sobre segurança infantil em playgrounds."
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
        .content-box {{
            background: var(--bg-subtle);
            border: 1px solid var(--border-subtle);
            padding: var(--space-4);
            border-radius: var(--radius-lg);
            margin: var(--space-4) 0;
        }}
        .cta-section {{
            background: linear-gradient(135deg, #1d4ed8 0%, #0ea5e9 100%);
            color: white;
            padding: var(--space-8);
            border-radius: var(--radius-xl);
            text-align: center;
            margin: var(--space-10) 0 var(--space-8);
        }}
        .cta-section h3 {{
            color: white;
            margin-bottom: var(--space-3);
        }}
    </style>
</head>

<body>
    <!-- Google Tag Manager (noscript) -->
    <noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-5NNLDWJX" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>

    <main>
        <div class="article-container">
            <article class="article-hero-panel">
                <div class="article-intro">
                    <h1>{title}</h1>
                    <p>Análise técnica conforme ABNT NBR 16071 - Segurança de Playgrounds</p>
                </div>

                <div class="article-meta">
                    <span>📅 Publicado: 02/04/2026</span>
                    <span>🏷️ ID FAQ: {faq_id}</span>
                    <span>⚠️ Gravidade: {gravidade}</span>
                </div>
            </article>

            <div class="article-content">
                <h2>Sobre esta Irregularidade</h2>
                <p>{resposta}</p>

                <div class="content-box">
                    <h3>Normas Técnicas Aplicáveis</h3>
                    <ul style="list-style: disc; margin-left: 20px;">
'''
    
    for norma in normas:
        html += f"                        <li>{norma}</li>\n"
    
    html += f'''                    </ul>
                </div>

                <div class="content-box">
                    <h3>Responsabilidade</h3>
                    <p><strong>{responsabilidade}</strong></p>
                    <p>Conforme ABNT NBR 16071, a adequação de playgrounds é responsabilidade compartilhada entre proprietários, construtoras e gestores, com exigências específicas de inspeção e manutenção.</p>
                </div>

                <h2>Protocolo de Ação</h2>
                <p>Para resolver esta irregularidade:</p>
                <ol style="margin-left: 20px; line-height: 1.8;">
                    <li>Confirmar o desvio através de inspeção técnica em campo</li>
                    <li>Registrar evidências fotográficas</li>
                    <li>Executar adequação conforme requisito normativo</li>
                    <li>Documentar as ações tomadas</li>
                    <li>Realizar inspeção de conformidade</li>
                </ol>

                <div class="content-box">
                    <h3>Referência Principal</h3>
                    <p>ABNT NBR 16071 - Segurança de Playgrounds - Requisitos de Segurança e Métodos de Ensaio</p>
                </div>
            </div>

            <section class="cta-section">
                <h3>Precisa de Ajuda com Conformidade de Playgrounds?</h3>
                <p>Nossa equipe de engenheiros especializados em segurança infantil está pronta para realizar inspeções completas e implementar soluções de conformidade técnica.</p>
                <div style="margin-top: var(--space-5); display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap;">
                    <a href="https://wa.me/5562991234567?text=Tenho%20dúvidas%20sobre%20playground" style="display: inline-block; padding: 12px 24px; background: white; color: #1d4ed8; border-radius: 8px; text-decoration: none; font-weight: 600;">
                        💬 Fale com Especialista
                    </a>
                    <a href="https://www.protoncd.com.br/artigos/playgrounds/" style="display: inline-block; padding: 12px 24px; background: rgba(255,255,255,0.2); color: white; border-radius: 8px; text-decoration: none; font-weight: 600; border: 1px solid white;">
                        📚 Mais Artigos
                    </a>
                </div>
            </section>
        </div>
    </main>

    <!-- Tracking pixels and analytics -->
</body>

</html>'''
    
    return html, file_path

# Generate HTML files
created_files = []
for faq_id, slug in missing_ids:
    if faq_id in faqs_by_id:
        faq = faqs_by_id[faq_id]
        html_content, file_path = generate_html(faq_id, slug, faq)
        
        # Write file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        created_files.append((faq_id, slug, file_path))
        print(f"✓ Generated: {faq_id} -> {slug}")
    else:
        print(f"✗ FAQ not found: {faq_id}")

# Print summary
print(f"\n{'='*60}")
print(f"Generated {len(created_files)} articles")
print(f"\nFiles created:")
for faq_id, slug, path in created_files:
    print(f"  {faq_id}: {path}")
print(f"\nArticles Generation Complete!")
