$pathsToCheck = @(
    @{ path = 'd:\apps\protoncd-1\artigos\elevadores'; pattern = 'artigo-elevadores-' },
    @{ path = 'd:\apps\protoncd-1\goiania'; pattern = 'goiania' },
    @{ path = 'd:\apps\protoncd-1\brasilia'; pattern = 'brasilia' },
    @{ path = 'd:\apps\protoncd-1\sao-paulo'; pattern = 'paulo' },
    @{ path = 'd:\apps\protoncd-1\belo-horizonte'; pattern = 'horizonte' },
    @{ path = 'd:\apps\protoncd-1\curitiba'; pattern = 'curitiba' },
    @{ path = 'd:\apps\protoncd-1\porto-alegre'; pattern = 'alegre' },
    @{ path = 'd:\apps\protoncd-1\rio-de-janeiro'; pattern = 'janeiro' }
)

$totalFiles = 0
$totalMissingHtml = 0
$missingHtmlList = @()

foreach ($item in $pathsToCheck) {
    if (-not (Test-Path $item.path)) { continue }
    
    $files = Get-ChildItem -Path $item.path -Filter '*.html' -File
    foreach ($file in $files) {
        $content = Get-Content -Path $file.FullName -Raw
        
        if ($content -match '<link\b[^>]*\brel="canonical"[^>]*\bhref="([^"]+)"') {
            $url = $matches[1]
            $totalFiles++
            
            if ($url -match '/[^/]+$' -and -not $url.EndsWith('.html')) {
                $missingHtmlList += "$($file.Name): $url"
                $totalMissingHtml++
            }
        }
    }
}

Write-Output "TOTAL_FILES=$totalFiles"
Write-Output "MISSING_HTML_CANONICAL=$totalMissingHtml"
if ($missingHtmlList.Count -gt 0) {
    Write-Output "ISSUES:"
    $missingHtmlList | ForEach-Object { Write-Output "  $_" }
}
