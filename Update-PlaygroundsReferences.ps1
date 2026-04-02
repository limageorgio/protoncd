# Script PowerShell para atualizar playgrounds.json com referências de artigos

$ErrorActionPreference = "Stop"

# Função para remover acentos e gerar slug
function ConvertTo-Slug {
    param([string]$Text)
    
    # Remover aspas Unicode e caracteres especiais
    $Text = $Text -replace "`u{2018}", "'" -replace "`u{2019}", "'"
    $Text = $Text -replace '[''""()–—\-]', ' '
    
    # Normalizações de acentos
    $Text = $Text -replace '[àáâãäå]', 'a'
    $Text = $Text -replace '[èéêë]', 'e'
    $Text = $Text -replace '[ìíîï]', 'i'
    $Text = $Text -replace '[òóôõö]', 'o'
    $Text = $Text -replace '[ùúûü]', 'u'
    $Text = $Text -replace '[ñ]', 'n'
    $Text = $Text -replace '[ç]', 'c'
    
    # Minúsculas
    $Text = $Text.ToLower()
    
    # Remover caracteres especiais
    $Text = $Text -replace '[^a-z0-9\s]', ''
    
    # Normalizar espaços
    $Text = $Text -replace '\s+', ' '
    $Text = $Text.Trim()
    
    # Espaços para hífens
    $Text = $Text -replace ' ', '-'
    
    # Remover hífens duplicados
    $Text = $Text -replace '-+', '-'
    
    return $Text
}

$jsonPath = "h:\apps\protoncd\conhecimento-tecnico\dados\playgrounds.json"
$playgroundsDir = "h:\apps\protoncd\artigos\playgrounds"
$baseUrl = "https://www.protoncd.com.br/artigos/playgrounds"

Write-Host "Carregando JSON..." -ForegroundColor Cyan

# Ler JSON com encoding UTF-8
$jsonContent = [IO.File]::ReadAllText($jsonPath, [Text.Encoding]::UTF8)
$data = ConvertFrom-Json -InputObject $jsonContent

$specificCount = 0
$fallbackCount = 0
$total = $data.faqs.Count

Write-Host "Total de FAQs: $total`n" -ForegroundColor Cyan

$i = 0
foreach ($faq in $data.faqs) {
    $i++
    $faqId = $faq.id
    $pergunta = $faq.pergunta
    
    # Gerar slug
    $slug = ConvertTo-Slug -Text $pergunta
    
    # Construir nome do arquivo
    $expectedFile = "artigo-playground-$slug.html"
    $fullPath = Join-Path -Path $playgroundsDir -ChildPath $expectedFile
    
    # Verificar se existe
    if (Test-Path -LiteralPath $fullPath) {
        $referenceLink = "Veja também em nosso artigo: $baseUrl/$slug.html"
        Write-Host "$i. $faqId → $slug (ESPECÍFICO)" -ForegroundColor Green
        $specificCount++
    }
    else {
        $referenceLink = "Veja também em nosso artigo: $baseUrl/index.html"
        Write-Host "$i. $faqId → $slug (FALLBACK)" -ForegroundColor Yellow
        $fallbackCount++
    }
    
    # Atualizar referências
    $faq.referencias = @($referenceLink)
}

Write-Host "`n" + "="*70 -ForegroundColor Cyan
Write-Host "Salvando JSON..." -ForegroundColor Cyan

# Salva com UTF-8 sem BOM
$json = ConvertTo-Json -InputObject $data -Depth 10
$utf8NoBom = New-Object System.Text.UTF8Encoding($false)
[IO.File]::WriteAllText($jsonPath, $json, $utf8NoBom)

Write-Host "Validando JSON..." -ForegroundColor Cyan
$validContent = [IO.File]::ReadAllText($jsonPath, [Text.Encoding]::UTF8)
$validData = ConvertFrom-Json -InputObject $validContent

Write-Host "`n" + "="*70 -ForegroundColor Green
Write-Host "✓ SUCESSO!" -ForegroundColor Green
Write-Host ""
Write-Host "Resumo:" -ForegroundColor Cyan
Write-Host "  Total de FAQs: $total" -ForegroundColor White
Write-Host "  Links específicos: $specificCount" -ForegroundColor Green
Write-Host "  Fallbacks: $fallbackCount" -ForegroundColor Yellow
Write-Host ""
Write-Host "JSON salvo em UTF-8 sem BOM" -ForegroundColor Green
Write-Host "="*70 -ForegroundColor Green
