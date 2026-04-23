import json
import re
import sys
import time
import xml.etree.ElementTree as ET
from datetime import datetime

import requests

ROOT_SITEMAP = "https://www.protoncd.com.br/sitemap.xml"
TIMEOUT = 12
UA = "Mozilla/5.0 (compatible; ProtonIndexAudit/1.0; +https://www.protoncd.com.br/)"


def fetch(url):
    return requests.get(url, timeout=TIMEOUT, headers={"User-Agent": UA}, allow_redirects=True)


def fetch_xml(url):
    r = fetch(url)
    r.raise_for_status()
    return r.text


def parse_sitemap_index(xml_text):
    root = ET.fromstring(xml_text)
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    return [n.text.strip() for n in root.findall("sm:sitemap/sm:loc", ns) if n.text]


def parse_urlset(xml_text):
    root = ET.fromstring(xml_text)
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    return [n.text.strip() for n in root.findall("sm:url/sm:loc", ns) if n.text]


def ext(pattern, text):
    m = re.search(pattern, text, flags=re.IGNORECASE | re.DOTALL)
    return m.group(1).strip() if m else ""


def normalize_text_len(text):
    import html as html_lib
    text = html_lib.unescape(text)
    return len(re.sub(r"\s+", " ", text).strip())


CHECK_NON_HTML_VARIANTS = True


def non_html_variant(url):
    if url.endswith(".html"):
        return url[:-5]
    return ""


def audit_url(url):
    out = {
        "url": url,
        "status": None,
        "final_url": "",
        "http_ok": False,
        "canonical": "",
        "canonical_self": False,
        "robots": "",
        "has_noindex": False,
        "title_len": 0,
        "desc_len": 0,
        "hreflang_count": 0,
        "x_robots_tag": "",
        "variant_without_html": "",
        "variant_status": "",
        "variant_final_url": "",
        "variant_points_to_html": False,
        "issues": [],
    }

    try:
        r = fetch(url)
        html = r.text
        out["status"] = r.status_code
        out["final_url"] = r.url
        out["http_ok"] = r.status_code == 200
        out["x_robots_tag"] = r.headers.get("X-Robots-Tag", "")

        canonical = ext(r'<link\s+rel="canonical"\s+href="([^"]+)"', html)
        robots = ext(r'<meta\s+name="robots"\s+content="([^"]+)"', html)
        title = ext(r"<title>(.*?)</title>", html)
        m_desc = re.search(r'<meta\s+name=[\""\']description[\""\']\s+content=[\""\'](.*?)[\""\']', html, re.I | re.S)
        if not m_desc:
            m_desc = re.search(r'<meta\s+content=[\""\'](.*?)[\""\']\s+name=[\""\']description[\""\']', html, re.I | re.S)
        desc = m_desc.group(1).strip() if m_desc else ""

        out["canonical"] = canonical
        out["canonical_self"] = canonical == url
        out["robots"] = robots
        out["has_noindex"] = "noindex" in robots.lower() or "noindex" in out["x_robots_tag"].lower()
        out["title_len"] = normalize_text_len(title)
        out["desc_len"] = normalize_text_len(desc)
        out["hreflang_count"] = len(re.findall(r'rel="alternate"\s+hreflang="', html, flags=re.IGNORECASE))

        if not out["http_ok"]:
            out["issues"].append("http_status_not_200")
        if not canonical:
            out["issues"].append("missing_canonical")
        if canonical and canonical != url:
            out["issues"].append("canonical_differs_from_sitemap_url")
        if out["has_noindex"]:
            out["issues"].append("has_noindex")
        if out["title_len"] < 20 or out["title_len"] > 70:
            out["issues"].append("title_len_outside_20_70")
        if out["desc_len"] < 70 or out["desc_len"] > 180:
            out["issues"].append("desc_len_outside_70_180")
        if out["hreflang_count"] == 0 and "/en/" in url:
            out["issues"].append("en_page_without_hreflang")

        if CHECK_NON_HTML_VARIANTS:
            var = non_html_variant(url)
            out["variant_without_html"] = var
            if var:
                try:
                    rv = fetch(var)
                    out["variant_status"] = rv.status_code
                    out["variant_final_url"] = rv.url
                    out["variant_points_to_html"] = rv.url == url
                    if rv.status_code == 200 and rv.url == var:
                        out["issues"].append("duplicate_variant_without_html_live_200")
                except Exception:
                    out["variant_status"] = "ERROR"

    except Exception as exc:
        out["issues"].append("crawl_error")
        out["crawl_error"] = str(exc)

    return out


def build_markdown(report):
    ts = report["generated_at"]
    total = report["summary"]["total_urls"]
    ok = report["summary"]["urls_without_issues"]
    with_issues = report["summary"]["urls_with_issues"]

    lines = []
    lines.append("# Auditoria Geral de Indexacao - Proton")
    lines.append("")
    lines.append(f"Data: {ts}")
    lines.append(f"Sitemap raiz: {ROOT_SITEMAP}")
    lines.append("")
    lines.append("## Resumo")
    lines.append("")
    lines.append(f"- URLs auditadas: {total}")
    lines.append(f"- URLs sem issues: {ok}")
    lines.append(f"- URLs com issues: {with_issues}")
    lines.append("")

    lines.append("## Issues por tipo")
    lines.append("")
    for k, v in sorted(report["summary"]["issue_counts"].items(), key=lambda x: (-x[1], x[0])):
        lines.append(f"- {k}: {v}")
    lines.append("")

    lines.append("## Checklist de Correcao (Gerenciavel)")
    lines.append("")
    lines.append("- [ ] Corrigir todas as URLs com status diferente de 200.")
    lines.append("- [ ] Remover noindex (meta ou header) de URLs que devem indexar.")
    lines.append("- [ ] Garantir canonical absoluto e consistente com URL do sitemap.")
    lines.append("- [ ] Implementar redirecionamento 301 da variante sem .html para a URL canônica .html.")
    lines.append("- [ ] Revisar titles fora de 20-70 caracteres.")
    lines.append("- [ ] Revisar descriptions fora de 70-180 caracteres.")
    lines.append("- [ ] Validar hreflang (principalmente pares PT/EN recíprocos).")
    lines.append("- [ ] Reenviar sitemap e solicitar recrawl no Search Console após ajustes.")
    lines.append("")

    lines.append("## URLs com issues")
    lines.append("")
    lines.append("| URL | Status | Canonical | Issues |")
    lines.append("|---|---:|---|---|")
    for row in report["results"]:
        if row["issues"]:
            issues = ", ".join(row["issues"])
            canonical = row["canonical"] or "(vazio)"
            lines.append(f"| {row['url']} | {row['status']} | {canonical} | {issues} |")
    lines.append("")

    lines.append("## Como rodar novamente")
    lines.append("")
    lines.append("1. Executar: python _tmp_full_indexing_audit.py")
    lines.append("2. Conferir arquivos gerados: INDEXACAO_AUDITORIA_RESULT.json e CHECKLIST-INDEXACAO-DOMINIO.md")
    lines.append("3. Aplicar correcoes")
    lines.append("4. Rodar novamente e comparar a queda das issues")

    return "\n".join(lines)


def main():
    started = time.time()

    index_xml = fetch_xml(ROOT_SITEMAP)
    sitemaps = parse_sitemap_index(index_xml)
    if not sitemaps:
        print("No child sitemaps found.")
        sys.exit(1)

    urls = []
    for sm in sitemaps:
        try:
            txt = fetch_xml(sm)
            urls.extend(parse_urlset(txt))
        except Exception as exc:
            print(f"Failed sitemap {sm}: {exc}")

    # unique preserving order
    seen = set()
    uniq = []
    for u in urls:
        if u not in seen:
            uniq.append(u)
            seen.add(u)

    results = []
    issue_counts = {}
    for i, u in enumerate(uniq, start=1):
        row = audit_url(u)
        results.append(row)
        for issue in row["issues"]:
            issue_counts[issue] = issue_counts.get(issue, 0) + 1
        if i % 20 == 0:
            print(f"Audited {i}/{len(uniq)}")

    with_issues = sum(1 for r in results if r["issues"])
    summary = {
        "total_urls": len(results),
        "urls_with_issues": with_issues,
        "urls_without_issues": len(results) - with_issues,
        "issue_counts": issue_counts,
        "duration_sec": round(time.time() - started, 2),
    }

    report = {
        "generated_at": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC"),
        "root_sitemap": ROOT_SITEMAP,
        "summary": summary,
        "results": results,
    }

    with open("INDEXACAO_AUDITORIA_RESULT.json", "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    md = build_markdown(report)
    with open("CHECKLIST-INDEXACAO-DOMINIO.md", "w", encoding="utf-8") as f:
        f.write(md)

    print("Audit complete")
    print(json.dumps(summary, ensure_ascii=False))


if __name__ == "__main__":
    main()
