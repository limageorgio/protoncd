import json
import re
from pathlib import Path

root = Path(r"h:/apps/protoncd")
ids = ["elev-033","elev-034","elev-035","elev-036","elev-037","elev-038","elev-039","elev-040","elev-041","elev-042"]
slug_by_id = {
"elev-033":"artigo-elevadores-chicotes-cabos-controle-protecao-inspecao",
"elev-034":"artigo-elevadores-placa-capacidade-cabina",
"elev-035":"artigo-elevadores-ventilacao-cabina",
"elev-036":"artigo-elevadores-chave-triangular-destravamento-emergencia",
"elev-037":"artigo-elevadores-vidros-espelhos-cabina-padrao",
"elev-038":"artigo-elevadores-interfone-emergencia-cabina",
"elev-039":"artigo-elevadores-saia-protecao-avental-cabina",
"elev-040":"artigo-elevadores-protecao-antissalto-cabos-polias",
"elev-041":"artigo-elevadores-fim-de-curso-limitador-final",
"elev-042":"artigo-elevadores-chave-triangular-sem-aviso-seguranca",
}

errors = []

# Validate new html metadata
for fid, slug in slug_by_id.items():
    p = root / "artigos" / "elevadores" / f"{slug}.html"
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
        errors.append(f"index.html {fid}: id ausente")
        continue
    end = ktext.find('"id":  "elev-', pos + 1)
    block = ktext[pos:end if end != -1 else pos + 3500]
    if f'/artigos/elevadores/{slug}.html' not in block:
        errors.append(f"index.html {fid}: url")
    if '"categoria":  "Elevadores"' not in block:
        errors.append(f"index.html {fid}: categoria")

if errors:
    print("VALIDACAO_FALHOU")
    for e in errors:
        print(e)
else:
    print("VALIDACAO_OK")
