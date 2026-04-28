from __future__ import annotations

import re
from dataclasses import dataclass, asdict
from typing import Any


@dataclass(frozen=True)
class Rule:
    pattern: re.Pattern[str]
    category: str
    severity: str
    cause: str
    recommendation: str


@dataclass(frozen=True)
class Finding:
    line: str
    category: str
    severity: str
    cause: str
    recommendation: str

    def to_dict(self) -> dict[str, str]:
        return asdict(self)


RULES: list[Rule] = [
    Rule(
        pattern=re.compile(r"TypeError: Cannot read properties of (?:undefined|null)", re.IGNORECASE),
        category="javascript-runtime",
        severity="high",
        cause="O codigo acessou um objeto inexistente antes da leitura de uma propriedade.",
        recommendation="Verifique o fluxo de dados e proteja o acesso com validacao antes de ler a propriedade.",
    ),
    Rule(
        pattern=re.compile(r"ReferenceError: .* is not defined", re.IGNORECASE),
        category="javascript-runtime",
        severity="high",
        cause="Uma variavel ou funcao foi usada antes de ser declarada ou importada.",
        recommendation="Confirme imports, nomes e ordem de carregamento dos scripts.",
    ),
    Rule(
        pattern=re.compile(r"Uncaught \(in promise\)", re.IGNORECASE),
        category="async-flow",
        severity="medium",
        cause="Uma promise foi rejeitada sem tratamento.",
        recommendation="Adicione tratamento de erro com try/except ou catch no ponto assincro apropriado.",
    ),
    Rule(
        pattern=re.compile(r"CORS policy|blocked by CORS policy", re.IGNORECASE),
        category="network-policy",
        severity="high",
        cause="O navegador bloqueou a requisicao por politica de origem cruzada.",
        recommendation="Revise os headers CORS do backend e confirme origem, metodo e credenciais.",
    ),
    Rule(
        pattern=re.compile(r"Content Security Policy|Refused to execute inline script", re.IGNORECASE),
        category="security-policy",
        severity="high",
        cause="A pagina foi bloqueada por politica de seguranca do navegador.",
        recommendation="Ajuste CSP, remova inline scripts ou use nonce/hash apropriado.",
    ),
    Rule(
        pattern=re.compile(r"Mixed Content", re.IGNORECASE),
        category="transport-security",
        severity="medium",
        cause="Conteudo inseguro foi carregado em uma pagina HTTPS.",
        recommendation="Troque as URLs para HTTPS ou sirva os recursos a partir do mesmo esquema.",
    ),
    Rule(
        pattern=re.compile(r"Failed to load resource: the server responded with a status of (4\d\d|5\d\d)", re.IGNORECASE),
        category="http-error",
        severity="high",
        cause="Um recurso requisitado retornou erro HTTP.",
        recommendation="Verifique a rota, autenticacao, cache e disponibilidade do endpoint.",
    ),
    Rule(
        pattern=re.compile(r"net::ERR_ABORTED|net::ERR_NAME_NOT_RESOLVED|net::ERR_CONNECTION_REFUSED", re.IGNORECASE),
        category="network-failure",
        severity="high",
        cause="A requisicao falhou em nivel de rede ou foi interrompida.",
        recommendation="Confira DNS, URL final, firewall, proxy e o tempo de vida da requisicao.",
    ),
    Rule(
        pattern=re.compile(r"Hydration failed|Text content does not match server-rendered HTML", re.IGNORECASE),
        category="render-mismatch",
        severity="medium",
        cause="O HTML gerado no cliente nao bate com o HTML enviado pelo servidor.",
        recommendation="Compare dados do servidor e cliente e evite depender de estado nao deterministico no primeiro render.",
    ),
]


def split_lines(raw_text: str) -> list[str]:
    return [line.strip() for line in raw_text.splitlines() if line.strip()]


def analyze_console(raw_text: str, page_url: str | None = None, source: str = "console") -> dict[str, Any]:
    lines = split_lines(raw_text)
    findings: list[Finding] = []

    for line in lines:
        matched_rule = next((rule for rule in RULES if rule.pattern.search(line)), None)
        if matched_rule is not None:
            findings.append(
                Finding(
                    line=line,
                    category=matched_rule.category,
                    severity=matched_rule.severity,
                    cause=matched_rule.cause,
                    recommendation=matched_rule.recommendation,
                )
            )
            continue

        lowered = line.lower()
        if "error" in lowered or "failed" in lowered or "exception" in lowered:
            findings.append(
                Finding(
                    line=line,
                    category="unclassified-error",
                    severity="medium",
                    cause="A linha aparenta representar um erro, mas nao ha regra especifica ainda.",
                    recommendation="Revise a mensagem completa e adicione uma regra se este padrao for recorrente.",
                )
            )

    severity_rank = {"low": 1, "medium": 2, "high": 3}
    highest_severity = "low"
    if findings:
        highest_severity = max(findings, key=lambda item: severity_rank.get(item.severity, 0)).severity

    next_actions = [
        "Reproduzir o erro em um ambiente isolado.",
        "Confirmar se a falha acontece em navegadores e paginas especificas.",
        "Correlacionar o erro com a ultima alteracao de frontend ou backend.",
    ]

    if any(f.category == "network-policy" for f in findings):
        next_actions.insert(0, "Revisar configuracao de CORS no backend.")
    if any(f.category == "http-error" for f in findings):
        next_actions.insert(0, "Inspecionar o endpoint que retornou 4xx/5xx.")

    return {
        "source": source,
        "page_url": page_url,
        "line_count": len(lines),
        "finding_count": len(findings),
        "highest_severity": highest_severity,
        "summary": summarize(findings),
        "findings": [finding.to_dict() for finding in findings],
        "next_actions": next_actions,
    }


def summarize(findings: list[Finding]) -> str:
    if not findings:
        return "Nenhum erro reconhecido automaticamente."

    categories = sorted({finding.category for finding in findings})
    if len(categories) == 1:
        return f"Foi identificado 1 tipo principal de problema: {categories[0]}."
    return f"Foram identificados problemas em {len(categories)} categorias: {', '.join(categories)}."
