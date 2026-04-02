$utf8NoBom = New-Object System.Text.UTF8Encoding($false)

function S {
    param([int[]]$Codes)
    return -join ($Codes | ForEach-Object { [char]$_ })
}

$badMarker1 = S 0x00C3
$badMarker2 = S 0x00E2
$badMarker3 = S 0x00C2

$replacements = @(
    @{ From = S 0x00C3, 0x00A1; To = S 0x00E1 },
    @{ From = S 0x00C3, 0x00A2; To = S 0x00E2 },
    @{ From = S 0x00C3, 0x00A3; To = S 0x00E3 },
    @{ From = S 0x00C3, 0x00A4; To = S 0x00E4 },
    @{ From = S 0x00C3, 0x00A7; To = S 0x00E7 },
    @{ From = S 0x00C3, 0x00A9; To = S 0x00E9 },
    @{ From = S 0x00C3, 0x00AA; To = S 0x00EA },
    @{ From = S 0x00C3, 0x00AB; To = S 0x00EB },
    @{ From = S 0x00C3, 0x00AD; To = S 0x00ED },
    @{ From = S 0x00C3, 0x00AE; To = S 0x00EE },
    @{ From = S 0x00C3, 0x00B3; To = S 0x00F3 },
    @{ From = S 0x00C3, 0x00B4; To = S 0x00F4 },
    @{ From = S 0x00C3, 0x00B5; To = S 0x00F5 },
    @{ From = S 0x00C3, 0x00B6; To = S 0x00F6 },
    @{ From = S 0x00C3, 0x00BA; To = S 0x00FA },
    @{ From = S 0x00C3, 0x00BB; To = S 0x00FB },
    @{ From = S 0x00C3, 0x00BC; To = S 0x00FC },
    @{ From = S 0x00C3, 0x0087; To = S 0x00C7 },
    @{ From = S 0x00C3, 0x0089; To = S 0x00C9 },
    @{ From = S 0x00C3, 0x008D; To = S 0x00CD },
    @{ From = S 0x00C3, 0x0093; To = S 0x00D3 },
    @{ From = S 0x00C3, 0x0094; To = S 0x00D4 },
    @{ From = S 0x00C3, 0x0095; To = S 0x00D5 },
    @{ From = S 0x00C3, 0x009A; To = S 0x00DA },
    @{ From = S 0x00C3, 0x009C; To = S 0x00DC },
    @{ From = S 0x00C2, 0x00A0; To = S 0x0020 },
    @{ From = S 0x00E2, 0x0080, 0x0094; To = S 0x2014 },
    @{ From = S 0x00E2, 0x0080, 0x0093; To = S 0x2013 },
    @{ From = S 0x00E2, 0x0080, 0x0098; To = S 0x2018 },
    @{ From = S 0x00E2, 0x0080, 0x0099; To = S 0x2019 },
    @{ From = S 0x00E2, 0x0080, 0x009C; To = S 0x201C },
    @{ From = S 0x00E2, 0x0080, 0x009D; To = S 0x201D },
    @{ From = S 0x00E2, 0x0086, 0x0092; To = S 0x2192 },
    @{ From = S 0x00E2, 0x0086, 0x0091; To = S 0x2191 },
    @{ From = S 0x00E2, 0x0086, 0x0093; To = S 0x2193 },
    @{ From = S 0x00E2, 0x0080, 0x00A6; To = S 0x2026 }
)

$paths = Get-ChildItem -Path 'H:\apps\protoncd\artigos\elevadores\*.html', 'H:\apps\protoncd\img\artigos\*.svg' -File

foreach ($file in $paths) {
    $text = [System.IO.File]::ReadAllText($file.FullName)
    if ($text.Length -gt 0 -and $text[0] -eq [char]0xFEFF) {
        $text = $text.Substring(1)
    }

    if ($text.Contains($badMarker1) -or $text.Contains($badMarker2) -or $text.Contains($badMarker3)) {
        foreach ($entry in $replacements) {
            $text = $text.Replace($entry.From, $entry.To)
        }
    }

    [System.IO.File]::WriteAllText($file.FullName, $text, $utf8NoBom)
}