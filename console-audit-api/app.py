from __future__ import annotations

from pathlib import Path
from typing import Any

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

from analyzer import RULES, analyze_console


BASE_DIR = Path(__file__).resolve().parent
WEB_DIR = BASE_DIR / "web"


class AnalyzeRequest(BaseModel):
    console_text: str = Field(..., min_length=1, description="Texto bruto copiado do console do navegador")
    page_url: str | None = Field(default=None, description="URL da pagina analisada")
    source: str = Field(default="console", description="Origem do log, por exemplo console ou search-console")


class AnalyzeResponse(BaseModel):
    source: str
    page_url: str | None
    line_count: int
    finding_count: int
    highest_severity: str
    summary: str
    findings: list[dict[str, str]]
    next_actions: list[str]


app = FastAPI(
    title="Console Audit API",
    version="1.0.0",
    description="API para analisar erros de console e devolver uma triagem automatica com proximos passos.",
)

if WEB_DIR.exists():
    app.mount("/static", StaticFiles(directory=WEB_DIR), name="static")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/", response_class=HTMLResponse)
def home() -> HTMLResponse:
    index_file = WEB_DIR / "index.html"
    if not index_file.exists():
        return HTMLResponse(
            "<h1>Console Audit API</h1><p>UI nao encontrada. Verifique a pasta web.</p>",
            status_code=200,
        )

    return HTMLResponse(index_file.read_text(encoding="utf-8"))


@app.get("/rules")
def rules() -> dict[str, Any]:
    return {
        "count": len(RULES),
        "rules": [
            {
                "category": rule.category,
                "severity": rule.severity,
                "cause": rule.cause,
                "recommendation": rule.recommendation,
                "pattern": rule.pattern.pattern,
            }
            for rule in RULES
        ],
    }


@app.post("/analyze", response_model=AnalyzeResponse)
def analyze(payload: AnalyzeRequest) -> dict[str, Any]:
    return analyze_console(
        raw_text=payload.console_text,
        page_url=payload.page_url,
        source=payload.source,
    )


@app.post("/analyze/batch")
def analyze_batch(payload: list[AnalyzeRequest]) -> list[dict[str, Any]]:
    return [
        analyze_console(
            raw_text=item.console_text,
            page_url=item.page_url,
            source=item.source,
        )
        for item in payload
    ]
