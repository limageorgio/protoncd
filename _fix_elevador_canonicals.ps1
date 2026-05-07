$root = 'd:\apps\protoncd-1\artigos\elevadores'
$pattern = '(<link\b[^>]*\brel=["'']canonical["''][^>]*\bhref=["''])(https://www\.protoncd\.com\.br/artigos/elevadores/[^"'']+)(["''][^>]*>)'
$files = Get-ChildItem -Path $root -Filter '*.html' -File -Recurse | Where-Object { $_.Name -ne 'index.html' }
$changed = @()

foreach ($file in $files) {
    $content = Get-Content -Path $file.FullName -Raw
    $newContent = [regex]::Replace($content, $pattern, {
        param($match)
        $url = $match.Groups[2].Value
        if ($url.EndsWith('.html')) {
            $match.Value
        } else {
            $match.Groups[1].Value + $url + '.html' + $match.Groups[3].Value
        }
    }, 1)

    if ($newContent -ne $content) {
        Set-Content -Path $file.FullName -Value $newContent -Encoding UTF8
        $changed += $file.Name
    }
}

Write-Output ("CHANGED={0}" -f $changed.Count)
$changed | ForEach-Object { Write-Output $_ }
