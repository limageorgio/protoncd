import json
from pathlib import Path

root = Path(r"h:/apps/protoncd")
ids = [
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
]
slug_by_id = {
    "elev-043": "artigo-elevadores-chicote-cabos-manobra-nos-abrasao",
    "elev-044": "artigo-elevadores-ventilacao-cabina-obstruida",
    "elev-045": "artigo-elevadores-sinalizacao-carro-aqui-porta-manual",
    "elev-046": "artigo-elevadores-interruptor-principal-bloqueio-loto",
    "elev-047": "artigo-elevadores-painel-tecnico-rotulos",
    "elev-048": "artigo-elevadores-porta-casa-maquinas-fechadura-segura",
    "elev-049": "artigo-elevadores-livro-registro-manutencao",
    "elev-050": "artigo-elevadores-esquema-eletrico-hidraulico-disponivel",
    "elev-051": "artigo-elevadores-iluminacao-emergencia-cabina",
    "elev-052": "artigo-elevadores-alarme-sonoro-emergencia-cabina",
}

errors = []

# Validate new html metadata
for fid, slug in slug_by_id.items():
    p = root / "artigos" / "elevadores" / f"{slug}.html"
    if not p.exists():
        errors.append(f"{p.name}: arquivo ausente")
        continue
    txt = p.read_text(encoding="utf-8")
    expected = f"https://www.protoncd.com.br/artigos/elevadores/{slug}.html"
    if f'<link rel="canonical" href="{expected}">' not in txt:
        errors.append(f"{p.name}: canonical")
    if f'<meta property="og:url" content="{expected}">' not in txt:
        errors.append(f"{p.name}: og:url")
    if f'"@id": "{expected}"' not in txt:
        errors.append(f"{p.name}: jsonld @id")

# Validate JSON file artigo_relacionado for IDs
jpath = root / "conhecimento-tecnico" / "dados" / "elevadores.json"
data = json.loads(jpath.read_text(encoding="utf-8"))
faqs = {f["id"]: f for f in data["faqs"]}
for fid, slug in slug_by_id.items():
    rel = faqs[fid].get("artigo_relacionado", {})
    if rel.get("url") != f"/artigos/elevadores/{slug}.html":
        errors.append(f"elevadores.json {fid}: url")
    if rel.get("categoria") != "Elevadores":
        errors.append(f"elevadores.json {fid}: categoria")

# Validate snapshot blocks in conhecimento-tecnico/index.html
kpath = root / "conhecimento-tecnico" / "index.html"
ktext = kpath.read_text(encoding="utf-8")
for fid, slug in slug_by_id.items():
    anchor = f'"id":  "{fid}"'
    pos = ktext.find(anchor)
    if pos == -1:
        errors.append(f"conhecimento-tecnico/index.html {fid}: id ausente")
        continue
    end = ktext.find('"id":  "elev-', pos + 1)
    block = ktext[pos : end if end != -1 else pos + 3500]
    if f'/artigos/elevadores/{slug}.html' not in block:
        errors.append(f"conhecimento-tecnico/index.html {fid}: url")
    if '"categoria":  "Elevadores"' not in block:
        errors.append(f"conhecimento-tecnico/index.html {fid}: categoria")

# Validate cards inserted in artigos/elevadores/index.html
elev_idx = (root / "artigos" / "elevadores" / "index.html").read_text(encoding="utf-8")
for fid, slug in slug_by_id.items():
    if f'href="{slug}.html"' not in elev_idx:
        errors.append(f"artigos/elevadores/index.html {fid}: card/link")

if errors:
    print("VALIDACAO_FALHOU")
    for e in errors:
        print(e)
else:
    print("VALIDACAO_OK")
