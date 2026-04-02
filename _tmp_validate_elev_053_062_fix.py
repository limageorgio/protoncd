import json
from pathlib import Path

root = Path(r"h:/apps/protoncd")
slug_by_id = {
    "elev-053": "artigo-elevadores-nivelamento-preciso-parada",
    "elev-054": "artigo-elevadores-porta-abre-fora-nivel",
    "elev-055": "artigo-elevadores-desgaste-guias-cabina-contrapeso",
    "elev-056": "artigo-elevadores-freio-maquina-ajuste-folga",
    "elev-057": "artigo-elevadores-ruido-polias-rolamentos",
    "elev-058": "artigo-elevadores-torque-fixacoes-maquina-base",
    "elev-059": "artigo-elevadores-corrosao-estrutura-casa-maquinas",
    "elev-060": "artigo-elevadores-quadro-comando-sobreaquecimento",
    "elev-061": "artigo-elevadores-inversor-frequencia-falhas-intermitentes",
    "elev-062": "artigo-elevadores-aterramento-equipotencializacao",
}

errors = []

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

jpath = root / "conhecimento-tecnico" / "dados" / "elevadores.json"
data = json.loads(jpath.read_text(encoding="utf-8"))
faqs = {f["id"]: f for f in data["faqs"]}
for fid, slug in slug_by_id.items():
    rel = faqs[fid].get("artigo_relacionado", {})
    if rel.get("url") != f"/artigos/elevadores/{slug}.html":
        errors.append(f"elevadores.json {fid}: url")
    if rel.get("categoria") != "Elevadores":
        errors.append(f"elevadores.json {fid}: categoria")

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

idx_path = root / "artigos" / "elevadores" / "index.html"
idx_txt = idx_path.read_text(encoding="utf-8")
for fid, slug in slug_by_id.items():
    if f'href="{slug}.html"' not in idx_txt:
        errors.append(f"artigos/elevadores/index.html {fid}: card/link")

if errors:
    print("VALIDACAO_FALHOU")
    for e in errors:
        print(e)
else:
    print("VALIDACAO_OK")
