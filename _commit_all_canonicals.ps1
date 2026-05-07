$root = 'd:\apps\protoncd-1'
$patterns = @(
    'artigos\elevadores\*.html',
    'goiania\*.html',
    'brasilia\*.html',
    'sao-paulo\*.html',
    'belo-horizonte\*.html',
    'curitiba\*.html',
    'porto-alegre\*.html',
    'rio-de-janeiro\*.html',
    'ibitinga\*.html',
    'anapolis\*.html',
    'rio-verde\*.html'
)

$files = @()
foreach ($pattern in $patterns) {
    $fullPattern = Join-Path $root $pattern
    $files += Get-ChildItem -Path $fullPattern -ErrorAction SilentlyContinue
}

if ($files.Count -eq 0) {
    Write-Output 'NO_FILES_TO_COMMIT'
    exit 0
}

git add -- @($files.FullName)
$msg = "fix: canonical URLs for elevator and regional articles ($(($files | Measure-Object).Count) files)"
git commit -m $msg
git push origin main
