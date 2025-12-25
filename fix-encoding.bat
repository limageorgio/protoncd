@echo off
chcp 65001 >nul
echo Corrigindo encoding dos arquivos HTML...
echo.

powershell -Command "$enc1252 = [System.Text.Encoding]::GetEncoding('Windows-1252'); $encUTF8 = [System.Text.Encoding]::UTF8; $files = @('analise-vibracao-elevadores.html', 'cercon-goias.html', 'franquias.html', 'inspecao-casa-bombas.html', 'inspecao-combate-incendio.html', 'inspecao-gas-predial.html', 'inspecao-hvac-pmoc.html', 'inspecao-playgrounds.html', 'inspecao-pressurizacao-escadas.html', 'inspecao-sistemas-mecanicos.html', 'laudo-pericial-engenharia.html', 'pacotes-servicos.html', 'teste-arrancamento-olhais.html', 'landing-servicos.html'); foreach ($f in $files) { $path = \"h:\apps\protoncd\$f\"; if (Test-Path $path) { try { $content = [System.IO.File]::ReadAllText($path, $enc1252); [System.IO.File]::WriteAllText($path, $content, $encUTF8); Write-Host \"✓ $f\" -ForegroundColor Green } catch { Write-Host \"✗ $f\" -ForegroundColor Red } } }"

echo.
echo Concluído!
pause
