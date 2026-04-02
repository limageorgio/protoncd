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
$identificacao = 'Identifica' + [char]0x00E7 + [char]0x00E3 + 'o T' + [char]0x00E9 + 'cnica'
$cenario = 'Cen' + [char]0x00E1 + 'rio'
$protocolo = 'Inspe' + [char]0x00E7 + [char]0x00E3 + 'o'
$decisao = 'Decis' + [char]0x00E3 + 'o Corretiva'

foreach ($file in $files) {
    if (-not (Test-Path $file)) { continue }
    $text = [IO.File]::ReadAllText($file, [Text.Encoding]::UTF8)
    $text = $text.Replace('IdentificaÃ§Ã£o TÃ©cnica', $identificacao)
    $text = $text.Replace('CenÃ¡rio', $cenario)
    $text = $text.Replace('InspeÃ§Ã£o', $protocolo)
    $text = $text.Replace('DecisÃ£o Corretiva', $decisao)
    [IO.File]::WriteAllText($file, $text, $encoding)
}
Write-Output 'Fixed heading encoding in 23 files.'