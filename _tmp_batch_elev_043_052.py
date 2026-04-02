import json
import re
from pathlib import Path
from datetime import date

root = Path(r"h:/apps/protoncd")
json_path = root / "conhecimento-tecnico" / "dados" / "elevadores.json"
kt_index_path = root / "conhecimento-tecnico" / "index.html"
elev_index_path = root / "artigos" / "elevadores" / "index.html"
artigos_dir = root / "artigos" / "elevadores"


def norm_title(s: str) -> str:
    return s.replace("ABNT ", "").strip()


batch = {
    "elev-043": {
        "slug": "artigo-elevadores-chicote-cabos-manobra-nos-abrasao",
        "rel_title": "Chicote de Cabos de Manobra com Nos e Abrasao: Risco de Pane",
        "card_title": "Chicote com Nos e Abrasao",
        "card_text": "Dano no chicote pode gerar falha intermitente, curto e parada inesperada.",
        "icon": "fas fa-link",
        "icon_color": "red",
        "hero": "hero-cabos.svg"
    },
    "elev-044": {
        "slug": "artigo-elevadores-ventilacao-cabina-obstruida",
        "rel_title": "Ventilacao da Cabina Obstruida: Conforto e Seguranca em Risco",
        "card_title": "Ventilacao da Cabina Obstruida",
        "card_text": "Respiros bloqueados pioram qualidade do ar e elevam risco em aprisionamento.",
        "icon": "fas fa-wind",
        "icon_color": "blue",
        "hero": "hero-poco.svg"
    },
    "elev-045": {
        "slug": "artigo-elevadores-sinalizacao-carro-aqui-porta-manual",
        "rel_title": "Sinalizacao Carro Aqui em Porta Manual: Prevencao de Quedas",
        "card_title": "Sinalizacao Carro Aqui",
        "card_text": "Indicacao ausente aumenta chance de abertura indevida e risco de queda no vao.",
        "icon": "fas fa-exclamation-circle",
        "icon_color": "red",
        "hero": "hero-poco.svg"
    },
    "elev-046": {
        "slug": "artigo-elevadores-interruptor-principal-bloqueio-loto",
        "rel_title": "Interruptor Principal com Bloqueio LOTO: Seguranca na Manutencao",
        "card_title": "Bloqueio LOTO no Interruptor",
        "card_text": "Sem trava por cadeado, existe risco de religamento acidental durante servico.",
        "icon": "fas fa-lock",
        "icon_color": "red",
        "hero": "hero-poco.svg"
    },
    "elev-047": {
        "slug": "artigo-elevadores-painel-tecnico-rotulos",
        "rel_title": "Painel Tecnico com Rotulos: Reducao de Erro em Emergencia",
        "card_title": "Painel Tecnico Rotulado",
        "card_text": "Rotulos legiveis reduzem manobras incorretas e agilizam resposta tecnica.",
        "icon": "fas fa-tags",
        "icon_color": "blue",
        "hero": "hero-poco.svg"
    },
    "elev-048": {
        "slug": "artigo-elevadores-porta-casa-maquinas-fechadura-segura",
        "rel_title": "Porta da Casa de Maquinas com Fechadura Segura: Controle de Acesso",
        "card_title": "Porta da Casa de Maquinas",
        "card_text": "Fechamento inadequado facilita acesso indevido e aumenta risco ocupacional.",
        "icon": "fas fa-door-closed",
        "icon_color": "orange",
        "hero": "hero-poco.svg"
    },
    "elev-049": {
        "slug": "artigo-elevadores-livro-registro-manutencao",
        "rel_title": "Livro de Registro de Manutencao: Rastreabilidade Tecnica do Elevador",
        "card_title": "Livro de Registro",
        "card_text": "Historico de manutencao e falhas e essencial para controle tecnico e juridico.",
        "icon": "fas fa-book",
        "icon_color": "orange",
        "hero": "hero-poco.svg"
    },
    "elev-050": {
        "slug": "artigo-elevadores-esquema-eletrico-hidraulico-disponivel",
        "rel_title": "Esquema Eletrico e Hidraulico Disponivel: Base para Manutencao Segura",
        "card_title": "Esquemas Tecnicos Disponiveis",
        "card_text": "Documentacao tecnica acessivel acelera diagnostico e evita intervencoes erradas.",
        "icon": "fas fa-project-diagram",
        "icon_color": "blue",
        "hero": "hero-poco.svg"
    },
    "elev-051": {
        "slug": "artigo-elevadores-iluminacao-emergencia-cabina",
        "rel_title": "Iluminacao de Emergencia da Cabina: Visibilidade em Pane",
        "card_title": "Iluminacao de Emergencia",
        "card_text": "Sem luz de emergencia funcional, pane eleva panico e risco aos ocupantes.",
        "icon": "fas fa-lightbulb",
        "icon_color": "red",
        "hero": "hero-poco.svg"
    },
    "elev-052": {
        "slug": "artigo-elevadores-alarme-sonoro-emergencia-cabina",
        "rel_title": "Alarme Sonoro de Emergencia da Cabina: Comunicacao Critica",
        "card_title": "Alarme Sonoro de Emergencia",
        "card_text": "Dispositivo de alarme e essencial para acionar ajuda em aprisionamento.",
        "icon": "fas fa-bell",
        "icon_color": "red",
        "hero": "hero-poco.svg"
    },
}

sev_cfg = {
    "Crítica": {
        "score": "9.5/10",
        "window": "Imediata (0-24h)",
        "tag": "CRITICA",
        "risk": (94, 96, 92, 98),
        "priority": "Correcao imediata",
    },
    "Alta": {
        "score": "8.4/10",
        "window": "Curta (ate 72h)",
        "tag": "ALTA",
        "risk": (82, 86, 80, 90),
        "priority": "Acao urgente",
    },
    "Média": {
        "score": "6.4/10",
        "window": "Programada (ate 30 dias)",
        "tag": "MEDIA",
        "risk": (62, 58, 60, 66),
        "priority": "Plano corretivo",
    },
}

with json_path.open("r", encoding="utf-8") as f:
    elev_data = json.load(f)

faqs = elev_data["faqs"]
faqs_by_id = {item["id"]: item for item in faqs}

today_iso = date.today().isoformat()
pretty_date = "02 de Abril de 2026"

for fid, cfg in batch.items():
    faq = faqs_by_id[fid]
    faq["artigo_relacionado"] = {
        "titulo": cfg["rel_title"],
        "url": f"/artigos/elevadores/{cfg['slug']}.html",
        "categoria": "Elevadores",
    }

with json_path.open("w", encoding="utf-8", newline="\n") as f:
    json.dump(elev_data, f, ensure_ascii=False, indent=4)
    f.write("\n")

# Update conhecimento-tecnico/index.html blocks for 043..052
kt_html = kt_index_path.read_text(encoding="utf-8")

for fid, cfg in batch.items():
    anchor = f'"id":  "{fid}"'
    start = kt_html.find(anchor)
    if start == -1:
        continue

    obj_start = kt_html.rfind("{", 0, start)
    i = obj_start
    depth = 0
    in_str = False
    esc = False
    obj_end = -1
    while i < len(kt_html):
        ch = kt_html[i]
        if in_str:
            if esc:
                esc = False
            elif ch == "\\":
                esc = True
            elif ch == '"':
                in_str = False
        else:
            if ch == '"':
                in_str = True
            elif ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
                if depth == 0:
                    obj_end = i
                    break
        i += 1
    if obj_end == -1:
        continue

    block = kt_html[obj_start : obj_end + 1]
    rel_block = (
        '"artigo_relacionado":  {\n'
        f'                                                                        "titulo":  "{cfg["rel_title"]}",\n'
        f'                                                                        "url":  "/artigos/elevadores/{cfg["slug"]}.html",\n'
        '                                                                        "categoria":  "Elevadores"\n'
        '                                                                    },\n'
    )

    if '"artigo_relacionado"' in block:
        block_new = re.sub(
            r'"artigo_relacionado":\s*\{[\s\S]*?\},\n',
            rel_block,
            block,
            count=1,
        )
    else:
        block_new = re.sub(
            r'("normas":\s*\[[\s\S]*?\]\s*,\n)',
            r"\1                                             " + rel_block,
            block,
            count=1,
        )

    kt_html = kt_html[:obj_start] + block_new + kt_html[obj_end + 1 :]

kt_index_path.write_text(kt_html, encoding="utf-8", newline="\n")

# Generate 10 HTML articles
for fid, cfg in batch.items():
    faq = faqs_by_id[fid]
    question = faq["pergunta"].strip()
    answer = faq["resposta"].strip()
    normas = faq.get("normas", [])
    responsabilidade = faq.get("responsabilidade", "Mista - requer avaliação técnica")
    gravidade = faq.get("gravidade", "Média")

    sev = sev_cfg.get(gravidade, sev_cfg["Média"])
    w1, w2, w3, w4 = sev["risk"]

    normas_li = "\n".join([f"                        <li>{n}</li>" for n in normas])
    normas_join = "; ".join([norm_title(n) for n in normas])

    seo_title = question[:-1] if question.endswith("?") else question
    canonical = f"https://www.protoncd.com.br/artigos/elevadores/{cfg['slug']}.html"
    short_desc = answer[:180].replace('"', "'")

    html = f'''<!DOCTYPE html>
<html lang="pt-BR">

<head>
    <!-- Google Tag Manager -->
    <script>(function (w, d, s, l, i) {{
            w[l] = w[l] || []; w[l].push({{ 'gtm.start': new Date().getTime(), event: 'gtm.js' }});
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
    <meta name="description" content="{short_desc}">
    <meta name="keywords" content="elevadores, inspeção técnica, engenharia diagnóstica, {fid}, {cfg['slug'].replace('-', ', ')}">
    <meta name="author" content="Proton Engenharia Diagnóstica">

    <title>{seo_title} | Proton Engenharia</title>
    <link rel="canonical" href="{canonical}">
    <link rel="alternate" hreflang="pt-BR" href="{canonical}">

    <meta property="og:type" content="article">
    <meta property="og:url" content="{canonical}">
    <meta property="og:title" content="{seo_title}">
    <meta property="og:description" content="{short_desc}">
    <meta property="og:site_name" content="Proton Engenharia Diagnóstica">
    <meta property="og:locale" content="pt_BR">
    <meta property="og:image" content="https://www.protoncd.com.br/img/logo_proton1x1.jpg">
    <meta property="article:published_time" content="{today_iso}">
    <meta property="article:author" content="Georgio Batista de Lima">
    <meta property="article:section" content="Elevadores">

    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{seo_title}">
    <meta name="twitter:description" content="{short_desc}">

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
          "@id": "{canonical}",
          "headline": "{seo_title}",
          "description": "{short_desc}",
          "datePublished": "{today_iso}",
          "dateModified": "{today_iso}",
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
          "articleBody": "{answer[:220].replace('"', "'")}"
        }}
      ]
    }}
    </script>

    <style>
        .article-container {{ max-width: 900px; margin: 0 auto; padding: var(--space-8) var(--space-4); }}
        .article-content {{ font-size: 1.03rem; }}
        .article-hero-panel {{ background: var(--bg-card); border: 1px solid var(--border-subtle); border-radius: var(--radius-xl); padding: var(--space-6); margin-bottom: var(--space-7); }}
        .article-intro {{ max-width: 760px; margin: 0 auto var(--space-5); text-align: center; }}
        .article-intro h1 {{ margin-bottom: var(--space-3); }}
        .article-intro p {{ margin-bottom: 0; }}
        .article-meta {{ display: flex; gap: var(--space-3); align-items: center; justify-content: center; font-size: var(--fs-sm); color: var(--text-secondary); margin-bottom: var(--space-4); flex-wrap: wrap; }}
        .article-meta-item {{ display: inline-flex; align-items: center; gap: 6px; }}
        .article-meta span {{ padding: 2px 8px; background: var(--bg-subtle); border-radius: 4px; font-size: 0.85rem; }}
        .article-mini-stats {{ display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: var(--space-3); margin: 0 0 var(--space-5); }}
        .article-mini-stat {{ background: rgba(255, 255, 255, 0.02); border: 1px solid var(--border-subtle); border-radius: var(--radius-lg); padding: var(--space-3); text-align: center; }}
        .article-mini-stat strong {{ display: block; color: var(--text-primary); font-size: 1.15rem; margin-bottom: 4px; }}
        .article-mini-stat span {{ color: var(--text-secondary); font-size: var(--fs-sm); }}
        .article-hero-visual {{ max-width: 640px; margin: 0 auto var(--space-6); border-radius: var(--radius-xl); overflow: hidden; border: 1px solid var(--border-subtle); box-shadow: var(--shadow-md); background: rgba(255, 255, 255, 0.02); }}
        .article-hero-visual img {{ width: 100%; height: auto; max-height: 230px; object-fit: contain; display: block; }}
        .quick-actions {{ display: flex; flex-wrap: wrap; gap: var(--space-3); margin: 0 0 var(--space-5); justify-content: center; }}
        .quick-actions .btn {{ text-decoration: none; }}
        .article-content h2 {{ font-size: var(--fs-xl); font-weight: var(--fw-bold); color: var(--text-primary); margin-top: var(--space-8); margin-bottom: var(--space-4); padding: var(--space-3) var(--space-4); border: 1px solid rgba(239, 68, 68, 0.28); border-radius: var(--radius-lg); background: linear-gradient(135deg, rgba(239, 68, 68, 0.12), rgba(239, 68, 68, 0.03)); }}
        .article-content h3 {{ font-size: 1.08rem; font-weight: var(--fw-semibold); color: var(--text-primary); margin-top: var(--space-6); margin-bottom: var(--space-3); padding: var(--space-2) 0; }}
        .article-content p {{ margin-bottom: var(--space-4); line-height: 1.78; color: var(--text-secondary); }}
        .article-content ul {{ margin-left: 0; padding: var(--space-4) var(--space-5); margin-bottom: var(--space-4); border: 1px solid var(--border-subtle); border-radius: var(--radius-lg); background: rgba(15, 23, 42, 0.45); list-style: none; }}
        .article-content li {{ margin-bottom: var(--space-2); line-height: 1.6; margin-left: 0; padding: var(--space-3); border: 1px solid var(--border-subtle); border-radius: var(--radius-md); background: rgba(255, 255, 255, 0.02); }}
        .content-box {{ background: var(--bg-subtle); border: 1px solid var(--border-subtle); padding: var(--space-4); border-radius: var(--radius-lg); margin: var(--space-4) 0; }}
        .risk-chart {{ background: var(--bg-subtle); border: 1px solid var(--border-subtle); border-radius: var(--radius-xl); padding: var(--space-5); margin: var(--space-5) 0; }}
        .risk-row {{ display: grid; grid-template-columns: 180px 1fr auto; align-items: center; gap: var(--space-3); margin-bottom: var(--space-3); }}
        .risk-row:last-child {{ margin-bottom: 0; }}
        .risk-bar {{ height: 10px; border-radius: 999px; background: rgba(255, 255, 255, 0.08); overflow: hidden; }}
        .risk-bar span {{ display: block; height: 100%; background: linear-gradient(90deg, #f59e0b 0%, #ef4444 100%); }}
        .decision-table {{ width: 100%; border-collapse: collapse; margin: var(--space-4) 0; border: 1px solid var(--border-subtle); }}
        .decision-table th, .decision-table td {{ border: 1px solid var(--border-subtle); padding: 10px; vertical-align: top; }}
        .cta-section {{ margin-top: var(--space-8); padding: var(--space-6); border: 1px solid var(--border-subtle); border-radius: var(--radius-xl); background: linear-gradient(135deg, rgba(14, 165, 233, 0.12), rgba(14, 165, 233, 0.03)); text-align: center; }}
        .cta-section h3 {{ margin-bottom: var(--space-3); }}
        .cta-section p {{ margin-bottom: var(--space-4); }}
        @media (max-width: 900px) {{ .article-mini-stats {{ grid-template-columns: 1fr; }} .risk-row {{ grid-template-columns: 1fr; gap: 6px; }} }}
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
                    <span class="article-meta-item"><i class="fas fa-calendar"></i><span>{pretty_date}</span></span>
                    <span class="article-meta-item"><i class="fas fa-exclamation-triangle" style="color:var(--accent-red);"></i><span style="background: rgba(220,38,38,0.1); color: var(--accent-red);">{sev['tag']}</span></span>
                </div>
                <div class="article-intro">
                    <span class="badge badge-red" style="margin-bottom: var(--space-3);">Artigo Técnico</span>
                    <h1>{seo_title}</h1>
                    <p>{question}</p>
                </div>
                <div class="article-hero-visual">
                    <img src="../../img/artigos/{cfg['hero']}" alt="Diagnóstico técnico de elevadores sobre {seo_title.lower()}">
                </div>
                <div class="article-mini-stats">
                    <div class="article-mini-stat"><strong>{sev['score']}</strong><span>Índice de criticidade</span></div>
                    <div class="article-mini-stat"><strong>{sev['window']}</strong><span>Janela de resposta</span></div>
                    <div class="article-mini-stat"><strong>{responsabilidade}</strong><span>Responsável principal</span></div>
                </div>
                <div class="quick-actions">
                    <a href="https://api.whatsapp.com/send?phone=5562992852704&text=Olá! Preciso de análise técnica sobre {seo_title.lower()}." class="btn btn-primary btn-sm" target="_blank" rel="noopener noreferrer"><i class="fab fa-whatsapp"></i> Falar com Especialista</a>
                    <a href="tel:5562992852704" class="btn btn-secondary btn-sm"><i class="fas fa-phone"></i> Ligar Agora</a>
                </div>
            </div>

            <h2 id="sec-identificacao"><i class="fas fa-info-circle" style="margin-right:8px;"></i>1. Identificação Técnica</h2>
            <div class="content-box">
                <p><strong>Pergunta de referência:</strong></p>
                <p>{question}</p>
                <p style="margin-top:var(--space-4);"><strong>Resposta técnica consolidada:</strong></p>
                <p>{answer}</p>
                <p style="margin-top:var(--space-4);"><strong>Normas aplicáveis:</strong></p>
                <ul>
{normas_li}
                </ul>
            </div>

            <h2 id="sec-contexto"><i class="fas fa-microscope" style="margin-right:8px;"></i>2. Contexto e Cenário</h2>
            <h3>Leitura prática para operação predial</h3>
            <p>Este tema exige avaliação técnica orientada por evidências de campo, histórico de manutenção e aderência às normas. A não conformidade tende a elevar risco operacional, impacto jurídico e custo corretivo quando postergada.</p>
            <ul>
                <li><strong>Gravidade classificada:</strong> {gravidade}.</li>
                <li><strong>Responsabilidade principal:</strong> {responsabilidade}.</li>
                <li><strong>Base normativa:</strong> {normas_join}.</li>
            </ul>

            <div class="risk-chart">
                <div class="risk-row"><strong>Probabilidade</strong><div class="risk-bar"><span style="width:{w1}%;"></span></div><span>{gravidade}</span></div>
                <div class="risk-row"><strong>Severidade</strong><div class="risk-bar"><span style="width:{w2}%;"></span></div><span>{gravidade}</span></div>
                <div class="risk-row"><strong>Exposição</strong><div class="risk-bar"><span style="width:{w3}%;"></span></div><span>Contínua</span></div>
                <div class="risk-row"><strong>Prioridade de ação</strong><div class="risk-bar"><span style="width:{w4}%;"></span></div><span>{sev['priority']}</span></div>
            </div>

            <h2 id="sec-protocolo"><i class="fas fa-clipboard-list" style="margin-right:8px;"></i>3. Protocolo de Inspeção</h2>
            <ul>
                <li>Registrar condição atual com evidências fotográficas e identificação do equipamento.</li>
                <li>Conferir aderência às exigências normativas e aos critérios de segurança aplicáveis.</li>
                <li>Classificar risco residual e definir prioridade de ação corretiva.</li>
                <li>Emitir recomendação técnica com prazo, responsável e validação pós-correção.</li>
            </ul>

            <h2 id="sec-matriz"><i class="fas fa-table" style="margin-right:8px;"></i>4. Matriz de Decisão Corretiva</h2>
            <table class="decision-table">
                <thead>
                    <tr><th>Cenário</th><th>Ação recomendada</th><th>Prazo</th></tr>
                </thead>
                <tbody>
                    <tr><td>Não conformidade crítica identificada</td><td>Bloqueio/mitigação imediata e plano de correção assistido</td><td>0-24h</td></tr>
                    <tr><td>Não conformidade relevante com controle temporário</td><td>Correção técnica com validação documental e nova vistoria</td><td>Até 7 dias</td></tr>
                    <tr><td>Condição em monitoramento com risco moderado</td><td>Plano corretivo programado e acompanhamento técnico</td><td>Até 30 dias</td></tr>
                </tbody>
            </table>

            <section class="cta-section">
                <h3>Precisa de diagnóstico técnico em elevadores com base normativa?</h3>
                <p>A Proton Engenharia realiza inspeção especializada com foco em segurança, responsabilidade e decisão técnica defensável.</p>
                <div style="display:flex; gap:12px; justify-content:center; flex-wrap:wrap;">
                    <a href="https://api.whatsapp.com/send?phone=5562992852704&text=Olá! Preciso de apoio técnico para inspeção de elevadores." target="_blank" rel="noopener noreferrer" class="btn btn-primary btn-sm"><i class="fab fa-whatsapp"></i> Solicitar Análise</a>
                    <a href="tel:5562992852704" class="btn btn-secondary btn-sm"><i class="fas fa-phone"></i> Ligar Agora</a>
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

</html>
'''

    (artigos_dir / f"{cfg['slug']}.html").write_text(html, encoding="utf-8", newline="\n")

# Update elevadores index cards
elev_idx = elev_index_path.read_text(encoding="utf-8")

new_cards = []
for fid in [
    "elev-043",
    "elev-044",
    "elev-045",
    "elev-046",
    "elev-047",
    "elev-048",
    "elev-049",
    "elev-050",
    "elev-051",
    "elev-052",
]:
    cfg = batch[fid]
    card = f'''                <a href="{cfg['slug']}.html" class="card hover-lift" style="text-decoration:none;">
                    <div class="card-icon {cfg['icon_color']}"><i class="{cfg['icon']}"></i></div>
                    <h3 class="card-title">{cfg['card_title']}</h3>
                    <p class="card-text">{cfg['card_text']}</p>
                </a>
'''
    new_cards.append(card)

cards_blob = "\n" + "\n".join(new_cards)
insert_marker = "            </div>\n        </div>\n    </section>"
if cards_blob not in elev_idx and insert_marker in elev_idx:
    elev_idx = elev_idx.replace(insert_marker, cards_blob + "            </div>\n        </div>\n    </section>", 1)

elev_index_path.write_text(elev_idx, encoding="utf-8", newline="\n")

print("Batch elev-043..052 aplicado com sucesso.")
