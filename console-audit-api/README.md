# Console Audit API

API isolada com interface web local para receber logs de console, analisar automaticamente e salvar o histórico no navegador.

## Estrutura

- `app.py`: API FastAPI e rota da UI local
- `analyzer.py`: regras de detecao e resumo
- `web/index.html`: interface web
- `web/styles.css`: estilos da interface
- `web/app.js`: logica do frontend local
- `test_analyzer.py`: teste basico do motor de analise
- `demo.py`: execucao local simples

## Como executar

```powershell
cd h:\apps\protoncd\console-audit-api
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app:app --reload --port 8001
```

Depois abra http://127.0.0.1:8001/ no navegador.

## O que a interface faz

- Cola logs do console manualmente.
- Importa arquivos locais do tipo `.txt`, `.log`, `.json`, `.html`, `.csv` ou `.md`.
- Envia os dados para a API local e mostra o resumo, os achados e as ações sugeridas.
- Salva o histórico no `localStorage` do navegador.
- Permite baixar o resultado em JSON.

## Exemplo de uso via API

```bash
curl -X POST http://127.0.0.1:8001/analyze \
  -H "Content-Type: application/json" \
  -d "{\"page_url\":\"https://www.protoncd.com.br\",\"console_text\":\"ReferenceError: foo is not defined\nFailed to load resource: the server responded with a status of 404 ()\"}"
```

## Teste rapido

```powershell
cd h:\apps\protoncd\console-audit-api
python -m unittest test_analyzer.py
```
