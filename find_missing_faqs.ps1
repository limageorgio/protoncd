$jsonPath = "h:\apps\protoncd\conhecimento-tecnico\dados\playgrounds.json"
$playgroundsDir = "h:\apps\protoncd\artigos\playgrounds"

# Ler JSON
$json = [IO.File]::ReadAllText($jsonPath, [Text.Encoding]::UTF8) | ConvertFrom-Json
$allFaqs = $json.faqs

# Contar arquivos
$existingFiles = Get-ChildItem -Path $playgroundsDir -Filter "artigo-playground-*.html"
$existingCount = $existingFiles.Count

Write-Host "Total de FAQs: $($allFaqs.Count)"
Write-Host "Total de arquivos: $existingCount"
Write-Host "Faltantes esperados: $($allFaqs.Count - $existingCount)"

# Criar lista simples de IDs
$allIds = $allFaqs | ForEach-Object { $_.id } | Sort-Object

# Salvar em arquivo
$allIds | Out-File -Path "h:\apps\protoncd\all_faq_ids.txt" -Encoding UTF8
Write-Host "`nSalvo em all_faq_ids.txt"
Write-Host "Primeiros 10 IDs:"
$allIds | Select-Object -First 10 | ForEach-Object { Write-Host "  $_" }
