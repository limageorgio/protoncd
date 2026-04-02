$files = @(
    'H:\apps\protoncd\artigos\playgrounds\artigo-playground-abertura-piso-correr-larga.html',
    'H:\apps\protoncd\artigos\playgrounds\artigo-playground-assento-pesado-aceleracao.html',
    'H:\apps\protoncd\artigos\playgrounds\artigo-playground-falta-revestimento-ferrugem.html',
    'H:\apps\protoncd\artigos\playgrounds\artigo-playground-acumulo-agua-tubos-tuneis.html',
    'H:\apps\protoncd\artigos\playgrounds\artigo-playground-alcas-suspensas-desgastadas.html',
    'H:\apps\protoncd\artigos\playgrounds\artigo-playground-corda-alma-exposta-fios-metalicos.html',
    'H:\apps\protoncd\artigos\playgrounds\artigo-playground-altura-acesso-cadeirante.html',
    'H:\apps\protoncd\artigos\playgrounds\artigo-playground-altura-assento-movimento-alta.html',
    'H:\apps\protoncd\artigos\playgrounds\artigo-playground-incompatibilidade-piso-aql.html',
    'H:\apps\protoncd\artigos\playgrounds\artigo-playground-borda-saida-escorregador-max.html',
    'H:\apps\protoncd\artigos\playgrounds\artigo-playground-ferrugem-desgaste-missing.html',
    'H:\apps\protoncd\artigos\playgrounds\artigo-playground-agarras-frouxas.html',
    'H:\apps\protoncd\artigos\playgrounds\artigo-playground-apoios-frouxos.html',
    'H:\apps\protoncd\artigos\playgrounds\artigo-playground-superficie-acesso-risco-escorregamento.html',
    'H:\apps\protoncd\artigos\playgrounds\artigo-playground-suspensao-rigida-balanco-tradicional.html',
    'H:\apps\protoncd\artigos\playgrounds\artigo-playground-presenca-plantas-toxicas-espinhosas.html',
    'H:\apps\protoncd\artigos\playgrounds\artigo-playground-extremidades-tubos-sem-vedacao-tampao.html',
    'H:\apps\protoncd\artigos\playgrounds\artigo-playground-vao-inferior-carrossel-60mm-400mm.html',
    'H:\apps\protoncd\artigos\playgrounds\artigo-playground-vao-solo-inadequado.html',
    'H:\apps\protoncd\artigos\playgrounds\artigo-playground-vegetacao-espinhos-frutos-venenosos.html',
    'H:\apps\protoncd\artigos\playgrounds\artigo-playground-velocidade-tirolesa-acima-7ms.html',
    'H:\apps\protoncd\artigos\playgrounds\artigo-playground-velocidade-carrossel-acima-5ms.html',
    'H:\apps\protoncd\artigos\playgrounds\artigo-playground-seccao-transversal-fechada-sem-visibilidade.html'
)

$encoding = New-Object System.Text.UTF8Encoding($false)
$cssPattern = '(?s)\.article-content h2\s*\{.*?\}'
$cssReplacement = @'
        .article-content h2 {
            font-size: var(--fs-xl);
            font-weight: var(--fw-bold);
            color: var(--text-primary);
            margin-top: var(--space-8);
            margin-bottom: var(--space-4);
            padding: var(--space-3) var(--space-4);
            border: 1px solid rgba(239, 68, 68, 0.28);
            border-radius: var(--radius-lg);
            background: linear-gradient(135deg, rgba(239, 68, 68, 0.12), rgba(239, 68, 68, 0.03));
        }
'@

$replacements = @(
    @{ Pattern = '<h2>1\.[^<]*</h2>'; Replacement = '<h2 id="sec-identificacao"><i class="fas fa-info-circle" style="margin-right:8px;"></i>1. Identificação Técnica</h2>' },
    @{ Pattern = '<h2>2\.[^<]*</h2>'; Replacement = '<h2 id="sec-contexto"><i class="fas fa-microscope" style="margin-right:8px;"></i>2. Contexto e Cenário</h2>' },
    @{ Pattern = '<h2>3\.[^<]*</h2>'; Replacement = '<h2 id="sec-protocolo"><i class="fas fa-clipboard-list" style="margin-right:8px;"></i>3. Protocolo de Inspeção</h2>' },
    @{ Pattern = '<h2>4\.[^<]*</h2>'; Replacement = '<h2 id="sec-matriz"><i class="fas fa-table" style="margin-right:8px;"></i>4. Matriz de Decisão Corretiva</h2>' }
)

$updatedCount = 0
foreach ($file in $files) {
    if (-not (Test-Path $file)) {
        Write-Warning "Missing file: $file"
        continue
    }
    $original = [IO.File]::ReadAllText($file, [Text.Encoding]::UTF8)
    $updated = [regex]::Replace($original, $cssPattern, $cssReplacement, 1)
    foreach ($item in $replacements) {
        $updated = [regex]::Replace($updated, $item.Pattern, $item.Replacement, 1)
    }
    if ($updated -ne $original) {
        [IO.File]::WriteAllText($file, $updated, $encoding)
        $updatedCount++
    }
}

Write-Output "Updated $updatedCount files."