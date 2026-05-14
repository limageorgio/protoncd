$paths = @(
    'd:\apps\protoncd-1\goiania',
    'd:\apps\protoncd-1\brasilia',
    'd:\apps\protoncd-1\sao-paulo',
    'd:\apps\protoncd-1\belo-horizonte',
    'd:\apps\protoncd-1\curitiba',
    'd:\apps\protoncd-1\porto-alegre',
    'd:\apps\protoncd-1\rio-de-janeiro',
    'd:\apps\protoncd-1\ibitinga',
    'd:\apps\protoncd-1\anapolis',
    'd:\apps\protoncd-1\rio-verde'
)

$pattern = '(<link\b[^>]*\brel=["'']canonical["''][^>]*\bhref=["''])(https://www\.protoncd\.com\.br/[^"'']+?/[^"'']+)(["''][^>]*>)'
$total_changed = 0

foreach ($dir in $paths) {
    if (Test-Path $dir) {
        $files = Get-ChildItem -Path $dir -Filter '*.html' -File
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
                $total_changed++
            }
        }
    }
}

Write-Output ("TOTAL_CHANGED={0}" -f $total_changed)
