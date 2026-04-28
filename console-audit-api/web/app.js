const sampleLogs = `ReferenceError: tracker is not defined
Failed to load resource: the server responded with a status of 404 ()
Access to fetch at https://api.example.com from origin https://www.example.com was blocked by CORS policy`;

const elements = {
    healthState: document.getElementById('health-state'),
    pageUrl: document.getElementById('page-url'),
    source: document.getElementById('source'),
    fileInput: document.getElementById('file-input'),
    consoleText: document.getElementById('console-text'),
    analyzeBtn: document.getElementById('analyze-btn'),
    saveRun: document.getElementById('save-run'),
    clearInput: document.getElementById('clear-input'),
    loadSample: document.getElementById('load-sample'),
    downloadJson: document.getElementById('download-json'),
    clearHistory: document.getElementById('clear-history'),
    metricLines: document.getElementById('metric-lines'),
    metricFindings: document.getElementById('metric-findings'),
    metricSeverity: document.getElementById('metric-severity'),
    summary: document.getElementById('summary'),
    nextActions: document.getElementById('next-actions'),
    findings: document.getElementById('findings'),
    history: document.getElementById('history'),
};

let lastResult = null;

function loadHistory() {
    try {
        return JSON.parse(localStorage.getItem('console-audit-history') || '[]');
    } catch {
        return [];
    }
}

function saveHistory(items) {
    localStorage.setItem('console-audit-history', JSON.stringify(items.slice(0, 12)));
}

function severityLabel(value) {
    return value || 'low';
}

function renderTags(value) {
    const tag = document.createElement('span');
    tag.className = `tag ${severityLabel(value)}`;
    tag.textContent = severityLabel(value);
    return tag;
}

function renderResult(result) {
    lastResult = result;
    elements.metricLines.textContent = result.line_count;
    elements.metricFindings.textContent = result.finding_count;
    elements.metricSeverity.textContent = result.highest_severity;
    elements.summary.textContent = result.summary;

    elements.nextActions.innerHTML = '';
    result.next_actions.forEach((action) => {
        const item = document.createElement('li');
        item.textContent = action;
        elements.nextActions.appendChild(item);
    });

    elements.findings.innerHTML = '';
    if (!result.findings.length) {
        const empty = document.createElement('div');
        empty.className = 'finding';
        empty.textContent = 'Nenhum erro classificado automaticamente.';
        elements.findings.appendChild(empty);
        return;
    }

    result.findings.forEach((finding) => {
        const card = document.createElement('article');
        card.className = 'finding';

        const top = document.createElement('div');
        top.className = 'finding-top';

        const title = document.createElement('strong');
        title.textContent = finding.category;

        top.append(title, renderTags(finding.severity));

        const line = document.createElement('div');
        line.className = 'finding-line';
        line.textContent = finding.line;

        const cause = document.createElement('p');
        cause.className = 'history-meta';
        cause.textContent = finding.cause;

        const recommendation = document.createElement('p');
        recommendation.className = 'history-meta';
        recommendation.textContent = finding.recommendation;

        card.append(top, line, cause, recommendation);
        elements.findings.appendChild(card);
    });
}

function renderHistory() {
    const history = loadHistory();
    elements.history.innerHTML = '';

    if (!history.length) {
        const empty = document.createElement('div');
        empty.className = 'history-item';
        empty.textContent = 'Nenhuma análise salva ainda.';
        elements.history.appendChild(empty);
        return;
    }

    history.forEach((item, index) => {
        const card = document.createElement('article');
        card.className = 'history-item';

        const top = document.createElement('div');
        top.className = 'history-top';

        const title = document.createElement('strong');
        title.textContent = item.page_url || 'Sem URL informada';

        const time = document.createElement('span');
        time.className = 'history-meta';
        time.textContent = new Date(item.created_at).toLocaleString('pt-BR');

        top.append(title, time);

        const meta = document.createElement('div');
        meta.className = 'history-meta';
        meta.textContent = `${item.finding_count} achados | ${item.highest_severity}`;

        const button = document.createElement('button');
        button.className = 'ghost';
        button.textContent = 'Reabrir';
        button.addEventListener('click', () => {
            elements.pageUrl.value = item.page_url || '';
            elements.source.value = item.source || 'console';
            elements.consoleText.value = item.console_text || '';
            renderResult(item.result);
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });

        const remove = document.createElement('button');
        remove.className = 'ghost';
        remove.textContent = 'Remover';
        remove.addEventListener('click', () => {
            const next = loadHistory();
            next.splice(index, 1);
            saveHistory(next);
            renderHistory();
        });

        card.append(top, meta, button, remove);
        elements.history.appendChild(card);
    });
}

async function checkHealth() {
    try {
        const response = await fetch('/health');
        if (!response.ok) throw new Error('bad response');
        elements.healthState.textContent = 'online';
        elements.healthState.classList.remove('loading');
    } catch {
        elements.healthState.textContent = 'offline';
        elements.healthState.classList.add('loading');
    }
}

async function analyze() {
    const consoleText = elements.consoleText.value.trim();
    if (!consoleText) {
        elements.summary.textContent = 'Cole ou carregue um log antes de analisar.';
        return;
    }

    elements.analyzeBtn.disabled = true;
    elements.analyzeBtn.textContent = 'Analisando...';

    try {
        const response = await fetch('/analyze', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                console_text: consoleText,
                page_url: elements.pageUrl.value || null,
                source: elements.source.value || 'console',
            }),
        });

        if (!response.ok) {
            const errorText = await response.text();
            throw new Error(errorText || 'Falha ao analisar');
        }

        const result = await response.json();
        renderResult(result);
    } catch (error) {
        elements.summary.textContent = `Nao foi possivel analisar: ${error.message}`;
    } finally {
        elements.analyzeBtn.disabled = false;
        elements.analyzeBtn.textContent = 'Analisar agora';
    }
}

function saveCurrentRun() {
    if (!lastResult) return;

    const history = loadHistory();
    history.unshift({
        created_at: new Date().toISOString(),
        page_url: elements.pageUrl.value || null,
        source: elements.source.value || 'console',
        console_text: elements.consoleText.value,
        result: lastResult,
        finding_count: lastResult.finding_count,
        highest_severity: lastResult.highest_severity,
    });
    saveHistory(history);
    renderHistory();
}

function downloadJson() {
    if (!lastResult) return;

    const payload = JSON.stringify(lastResult, null, 2);
    const blob = new Blob([payload], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const anchor = document.createElement('a');
    anchor.href = url;
    anchor.download = 'console-audit-result.json';
    anchor.click();
    URL.revokeObjectURL(url);
}

function wireEvents() {
    elements.analyzeBtn.addEventListener('click', analyze);
    elements.saveRun.addEventListener('click', saveCurrentRun);
    elements.clearInput.addEventListener('click', () => {
        elements.consoleText.value = '';
        elements.pageUrl.value = '';
        elements.source.value = 'console';
    });
    elements.loadSample.addEventListener('click', () => {
        elements.consoleText.value = sampleLogs;
        elements.pageUrl.value = 'https://www.protoncd.com.br/';
        elements.source.value = 'chrome-console';
    });
    elements.downloadJson.addEventListener('click', downloadJson);
    elements.clearHistory.addEventListener('click', () => {
        saveHistory([]);
        renderHistory();
    });
    elements.fileInput.addEventListener('change', async (event) => {
        const file = event.target.files?.[0];
        if (!file) return;
        const content = await file.text();
        elements.consoleText.value = content;
        if (!elements.pageUrl.value) {
            elements.pageUrl.value = 'https://www.protoncd.com.br/';
        }
        if (!elements.source.value) {
            elements.source.value = 'local-file';
        }
    });
}

renderHistory();
wireEvents();
checkHealth();
