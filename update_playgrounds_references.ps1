# Script para atualizar referências de artigos no playgrounds.json

$jsonPath = "h:\apps\protoncd\conhecimento-tecnico\dados\playgrounds.json"
$playgroundsDir = "h:\apps\protoncd\artigos\playgrounds"
$baseUrl = "https://www.protoncd.com.br/artigos/playgrounds"

# Função para remover acentos e gerar slug
function ConvertTo-Slug {
    param([string]$Text)
    
    # Remover caracteres especiais e acentos
    $Text = [System.Text.RegularExpressions.Regex]::Replace($Text, "[à|á|â|ã|ä]", "a")
    $Text = [System.Text.RegularExpressions.Regex]::Replace($Text, "[è|é|ê|ë]", "e")
    $Text = [System.Text.RegularExpressions.Regex]::Replace($Text, "[ì|í|î|ï]", "i")
    $Text = [System.Text.RegularExpressions.Regex]::Replace($Text, "[ò|ó|ô|õ|ö]", "o")
    $Text = [System.Text.RegularExpressions.Regex]::Replace($Text, "[ù|ú|û|ü]", "u")
    $Text = [System.Text.RegularExpressions.Regex]::Replace($Text, "[ñ]", "n")
    $Text = [System.Text.RegularExpressions.Regex]::Replace($Text, "[ç]", "c")
    
    # Converter para minúsculas
    $Text = $Text.ToLower()
    
    # Remover aspas e caracteres especiais, mantendo apenas letras, números e hífen
    $Text = [System.Text.RegularExpressions.Regex]::Replace($Text, "['\""()–—\-]", " ")
    
    # Remover caracteres especiais
    $Text = [System.Text.RegularExpressions.Regex]::Replace($Text, "[^a-z0-9\s]", "")
    
    # Normalizar múltiplos espaços para único espaço
    $Text = [System.Text.RegularExpressions.Regex]::Replace($Text, "\s+", " ")
    
    # Remover espaços no início e fim
    $Text = $Text.Trim()
    
    # Substituir espaços por hífens
    $Text = $Text -replace ' ', '-'
    
    # Remover hífens duplicados
    $Text = [System.Text.RegularExpressions.Regex]::Replace($Text, "-+", "-")
    
    return $Text
}

# Ler o JSON com encoding UTF-8
Write-Host "Lendo arquivo JSON..." -ForegroundColor Cyan
$jsonContent = [IO.File]::ReadAllText($jsonPath, [Text.Encoding]::UTF8)
$data = $jsonContent | ConvertFrom-Json

# Inicializar contadores
$updatedCount = 0
$specificCount = 0
$fallbackCount = 0
$totalFAQs = $data.faqs.Count

Write-Host "Total de FAQs: $totalFAQs" -ForegroundColor Cyan
Write-Host ""

# Processar cada FAQ
foreach ($faq in $data.faqs) {
    $faqId = $faq.id
    $pergunta = $faq.pergunta
    
    # Gerar slug da pergunta
    $slug = ConvertTo-Slug -Text $pergunta
    
    # Remover prefixo comum da pergunta (se existir)
    $slug = $slug -replace "^essa-situacao-de-", ""
    $slug = $slug -replace "^brinquedo-com-", ""
    $slug = $slug -replace "^quando-ha-", ""
    $slug = $slug -replace "^-", ""
    
    # Construir nome do arquivo esperado
    $expectedFile = "artigo-playground-$slug.html"
    $fullPath = Join-Path -Path $playgroundsDir -ChildPath $expectedFile
    
    # Verificar se o arquivo existe
    $fileExists = Test-Path -Path $fullPath
    
    if ($fileExists) {
        $referenceLink = "Veja também em nosso artigo: $baseUrl/$slug.html"
        Write-Host "$faqId → $slug (ESPECÍFICO)" -ForegroundColor Green
        $specificCount++
    }
    else {
        $referenceLink = "Veja também em nosso artigo: $baseUrl/index.html"
        Write-Host "$faqId → $slug (FALLBACK - arquivo não encontrado)" -ForegroundColor Yellow
        $fallbackCount++
    }
    
    # Atualizar referências
    $faq.referencias = @($referenceLink)
    $updatedCount++
}

Write-Host ""
Write-Host "Salvando JSON atualizado..." -ForegroundColor Cyan

# Converter para JSON com encoding UTF-8 sem BOM
$jsonOutput = $data | ConvertTo-Json -Depth 10
$utf8NoBom = New-Object System.Text.UTF8Encoding($false)
[IO.File]::WriteAllText($jsonPath, $jsonOutput, $utf8NoBom)

Write-Host "Validando JSON..." -ForegroundColor Cyan
$validatedContent = [IO.File]::ReadAllText($jsonPath, [Text.Encoding]::UTF8)
$validatedData = $validatedContent | ConvertFrom-Json

Write-Host ""
Write-Host "✓ PROCESSO CONCLUÍDO COM SUCESSO!" -ForegroundColor Green
Write-Host ""
Write-Host "Resumo:" -ForegroundColor Cyan
Write-Host "  Total de FAQs atualizadas: $updatedCount" -ForegroundColor White
Write-Host "  Links específicos (artigos): $specificCount" -ForegroundColor Green
Write-Host "  Fallbacks (index.html): $fallbackCount" -ForegroundColor Yellow
Write-Host ""
Write-Host "JSON validado e salvo em UTF-8 sem BOM" -ForegroundColor Green
