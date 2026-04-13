import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
import ssl

ROOT = Path('.')
SITEMAPS = [
    ROOT / 'sitemap-servicos.xml',
    ROOT / 'sitemap-regional.xml',
    ROOT / 'sitemap-conhecimento.xml',
]

EXCLUDE_PARTS = {'old', 'v2-staging', '.git', '.vscode'}

ns = {'sm': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
urls = []
for sp in SITEMAPS:
    if not sp.exists():
        continue
    tree = ET.parse(sp)
    root = tree.getroot()
    for loc in root.findall('.//sm:loc', ns):
        u = (loc.text or '').strip()
        if u:
            urls.append(u)

seen = set()
ordered = []
for u in urls:
    if u not in seen:
        ordered.append(u)
        seen.add(u)


def url_from_file(path: Path) -> str:
    rel = path.as_posix()
    if rel == 'index.html':
        return 'https://www.protoncd.com.br/'
    if rel.endswith('/index.html'):
        return 'https://www.protoncd.com.br/' + rel[:-10] + '/'
    return 'https://www.protoncd.com.br/' + rel


local_urls = []
for html in ROOT.rglob('*.html'):
    parts = set(html.parts)
    if parts.intersection(EXCLUDE_PARTS):
        continue
    local_urls.append(url_from_file(html))

seen_local = set()
ordered_local = []
for u in local_urls:
    if u not in seen_local:
        ordered_local.append(u)
        seen_local.add(u)

ctx = ssl.create_default_context()

def check(url: str):
    for method in ('HEAD', 'GET'):
        req = Request(
            url,
            method=method,
            headers={'User-Agent': 'Mozilla/5.0 (compatible; ProtonCD-Availability-Audit/1.0)'},
        )
        try:
            with urlopen(req, timeout=20, context=ctx) as r:
                code = getattr(r, 'status', None) or r.getcode()
                final_url = r.geturl()
                if 200 <= code < 400:
                    return {
                        'url': url,
                        'ok': True,
                        'status': code,
                        'method': method,
                        'final_url': final_url,
                        'error': '',
                    }
                return {
                    'url': url,
                    'ok': False,
                    'status': code,
                    'method': method,
                    'final_url': final_url,
                    'error': f'Status {code}',
                }
        except HTTPError as e:
            if method == 'HEAD' and e.code in (400, 403, 405, 501):
                continue
            return {
                'url': url,
                'ok': False,
                'status': e.code,
                'method': method,
                'final_url': url,
                'error': f'HTTPError {e.code}',
            }
        except URLError as e:
            if method == 'HEAD':
                continue
            return {
                'url': url,
                'ok': False,
                'status': None,
                'method': method,
                'final_url': url,
                'error': f'URLError {e.reason}',
            }
        except Exception as e:
            if method == 'HEAD':
                continue
            return {
                'url': url,
                'ok': False,
                'status': None,
                'method': method,
                'final_url': url,
                'error': f'{type(e).__name__}: {e}',
            }

    return {
        'url': url,
        'ok': False,
        'status': None,
        'method': 'GET',
        'final_url': url,
        'error': 'Falha de conexao',
    }

results = []
with ThreadPoolExecutor(max_workers=12) as ex:
    futures = {ex.submit(check, u): u for u in ordered}
    for f in as_completed(futures):
        results.append(f.result())

results_local = []
with ThreadPoolExecutor(max_workers=12) as ex:
    futures = {ex.submit(check, u): u for u in ordered_local}
    for f in as_completed(futures):
        results_local.append(f.result())

results.sort(key=lambda x: x['url'])
missing = [r for r in results if not r['ok']]

results_local.sort(key=lambda x: x['url'])
missing_local = [r for r in results_local if not r['ok']]

now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
out = []
out.append('# Paginas que deveriam estar online e nao estao')
out.append('')
out.append(f'- Gerado em: {now}')
out.append('- Fonte esperada: sitemap-servicos.xml, sitemap-regional.xml, sitemap-conhecimento.xml')
out.append(f'- URLs esperadas auditadas: {len(ordered)}')
out.append(f'- URLs indisponiveis encontradas: {len(missing)}')
out.append(f'- URLs de HTML local auditadas: {len(ordered_local)}')
out.append(f'- URLs de HTML local indisponiveis: {len(missing_local)}')
out.append('')

if missing:
    out.append('## Lista de paginas indisponiveis')
    out.append('')
    out.append('| URL | Status | Metodo | Observacao |')
    out.append('|---|---:|---|---|')
    for r in missing:
        st = '' if r['status'] is None else str(r['status'])
        obs = r['error'].replace('|', '\\|')
        out.append(f"| {r['url']} | {st} | {r['method']} | {obs} |")
else:
    out.append('## Resultado')
    out.append('')
    out.append('Nenhuma URL indisponivel foi encontrada na verificacao dos sitemaps.')

out.append('')
out.append('## Lista de paginas indisponiveis (base: HTML local de producao)')
out.append('')

if missing_local:
    out.append('| URL | Status | Metodo | Observacao |')
    out.append('|---|---:|---|---|')
    for r in missing_local:
        st = '' if r['status'] is None else str(r['status'])
        obs = r['error'].replace('|', '\\|')
        out.append(f"| {r['url']} | {st} | {r['method']} | {obs} |")
else:
    out.append('Nenhuma URL indisponivel foi encontrada na verificacao dos HTML locais de producao.')

out.append('')
out.append('## Observacoes')
out.append('')
out.append('- URLs com status 200-399 foram consideradas disponiveis.')
out.append('- Quando HEAD falhou, foi feito fallback para GET.')

report_path = ROOT / 'PAGINAS-INDISPONIVEIS.md'
report_path.write_text('\n'.join(out), encoding='utf-8')
print(f'REPORT={report_path.as_posix()}')
print(f'TOTAL={len(ordered)}')
print(f'INDISPONIVEIS={len(missing)}')
print(f'TOTAL_LOCAL={len(ordered_local)}')
print(f'INDISPONIVEIS_LOCAL={len(missing_local)}')
