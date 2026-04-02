$ErrorActionPreference = 'Stop'
$root = 'H:/apps/protoncd'
$kbPath = "$root/conhecimento-tecnico/index.html"
$hubPath = "$root/artigos/playgrounds/index.html"
$enc = New-Object System.Text.UTF8Encoding($false)

function To-Ascii([string]$s) {
    if ([string]::IsNullOrWhiteSpace($s)) { return '' }
    $norm = $s.Normalize([Text.NormalizationForm]::FormD)
    $sb = New-Object System.Text.StringBuilder
    foreach ($ch in $norm.ToCharArray()) {
        $uc = [Globalization.CharUnicodeInfo]::GetUnicodeCategory($ch)
        if ($uc -ne [Globalization.UnicodeCategory]::NonSpacingMark) { [void]$sb.Append($ch) }
    }
    $t = $sb.ToString().Normalize([Text.NormalizationForm]::FormC)
    $t = $t -replace '[“”"`´]', ''
    $t = $t -replace '’', "'"
  return $t
}

$items = @(
  [ordered]@{
    id='play-071'; slug='pisos-soltos-devem-ser-aerados-borrachas-devem-ter-laudo-hic'; title='Pisos soltos devem ser aerados; borrachas devem ter laudo HIC'; fileTitle='Playground: Pisos soltos devem ser aerados; borrachas devem ter laudo HIC'; grav='Alta'; resp='Mista - requer avaliacao tecnica'; score='7.8/10';
    pregunta="Com 'Pisos soltos devem ser aerados; borrachas devem ter laudo HIC', o piso do playground fica inseguro para quedas?";
    resposta="A irregularidade 'Pisos soltos devem ser aerados; borrachas devem ter laudo HIC' indica nao conformidade tecnica identificada no PlaygroundScan. Em linguagem simples, isso eleva o risco de acidente e exige correcao com base na ABNT NBR 16071. Na pratica, a inspecao deve confirmar o desvio em campo, registrar evidencias fotograficas e executar adequacao conforme requisito normativo aplicavel. Referencia principal: Parte 3 e Parte 7. Citacao tecnica: Parte 3, 4.2 / Parte 7, 4.2-k.";
    normes='ABNT NBR 16071 | ABNT NBR 16071-3';
    p2='Quando o piso solto e compactado demais, ele perde a capacidade de absorver energia de impacto e passa a funcionar como um bloco rigido sob queda. Em paralelo, a ausencia de laudo HIC impede provar que a combinacao material/espessura ainda atende a altura critica do brinquedo.';
    b1='Recalque, compactacao excessiva e recarga de material sem reensaio.'; b2='Pico de aceleracao acima do aceitavel em queda real.'; b3='Umidade, mistura de camadas e espessura util reduzida.';
    p31='Conferir laudo HIC, validade, altura critica e correspondencia com a altura de queda real.'; p32='Inspecionar zonas endurecidas, ondulacao e perda de resiliencia do material.'; p33='Medir espessura util e continuidade da camada de amortecimento em varios pontos.'; p34='Sem comprovacao valida, restringir uso e programar reensaio e recuperacao do piso.';
    m1c='Piso sem laudo HIC e com compactacao elevada'; m1a='Restricao imediata e recertificacao'; m1p='0-24h';
    m2c='Material degradado com perda de desempenho'; m2a='Recuperacao prioritaria e ensaio novo'; m2p='Ate 7 dias';
    m3c='Desgaste inicial controlavel'; m3a='Aeração/ajuste e monitoramento'; m3p='Ate 30 dias'
  },
  [ordered]@{
    id='play-072'; slug='presenca-de-sujeira-umidade-ou-falta-de-condicoes-de-uso-no-piso'; title='Presenca de sujeira, umidade ou falta de condicoes de uso no piso'; fileTitle='Playground: Presenca de sujeira, umidade ou falta de condicoes de uso no piso'; grav='Media'; resp='Condominio'; score='6.0/10';
    pregunta="Com 'Presença de sujeira, umidade ou falta de condições de uso no piso', o piso do playground fica inseguro para quedas?";
    resposta="A irregularidade 'Presença de sujeira, umidade ou falta de condições de uso no piso' indica nao conformidade tecnica identificada no PlaygroundScan. Em linguagem simples, isso eleva o risco de acidente e exige correcao com base na ABNT NBR 16071. Na pratica, a inspecao deve confirmar o desvio em campo, registrar evidencias fotograficas e executar adequacao conforme requisito normativo aplicavel. Referencia principal: Parte 5 e Parte 7. Citacao tecnica: Parte 5, item 4.5 / Parte 7, itens 4.2-k, 5-f e 5-g.";
    normes='ABNT NBR 16071 | ABNT NBR 16071-5';
    p2='Piso molhado, com sujeira ou sem condicao de uso amplia o coeficiente de escorregamento e reduz a previsibilidade da marcha infantil. O risco e multiplo: queda por escorregamento, perda de apoio na frenagem e transferencia de lama/umidade para outras areas do playground.';
    b1='Lavagem sem secagem, drenagem deficiente e falha de rotina de limpeza.'; b2='Escorregamento ou tropeço por contaminacao superficial.'; b3='Fluxo intenso, sombra permanente e acumulo de particulas.';
    p31='Verificar condicao superficial, grau de umidade e presença de contaminantes no piso.'; p32='Checar se ha drenagem obstruida, poças, limo ou material solto aderido.'; p33='Comparar o estado do piso com o nivel de uso previsto e a facilidade de limpeza.'; p34='Definir limpeza tecnica, secagem e ajuste de drenagem antes da reabertura.';
    m1c='Piso contaminado com risco imediato de escorregamento'; m1a='Interdicao e limpeza imediata'; m1p='0-24h';
    m2c='Umidade recorrente por falha de drenagem'; m2a='Correcao de drenagem e rotina reforcada'; m2p='Ate 7 dias';
    m3c='Sujidade isolada sem perda estrutural'; m3a='Limpeza preventiva e monitoramento'; m3p='Ate 30 dias'
  },
  [ordered]@{
    id='play-073'; slug='plastico-esbranquicado-ressecado-perda-de-propriedade-estrutural'; title='Plastico esbranquicado/ressecado (perda de propriedade estrutural)'; fileTitle='Playground: Plastico esbranquicado/ressecado (perda de propriedade estrutural)'; grav='Media'; resp='Mista - requer avaliacao tecnica'; score='6.0/10';
    pregunta="'Plástico esbranquiçado/ressecado (perda de propriedade estrutural)' no playground é só detalhe ou é um problema de segurança que precisa corrigir?";
    resposta="A irregularidade 'Plástico esbranquiçado/ressecado (perda de propriedade estrutural)' indica nao conformidade tecnica identificada no PlaygroundScan. Em linguagem simples, isso eleva o risco de acidente e exige correcao com base na ABNT NBR 16071. Na pratica, a inspecao deve confirmar o desvio em campo, registrar evidencias fotograficas e executar adequacao conforme requisito normativo aplicavel. Referencia principal: Parte 2. Citacao tecnica: Parte 2, item 4.5.";
    normes='ABNT NBR 16071 | ABNT NBR 16071-2';
    p2='Plastico esbranquiçado normalmente sinaliza envelhecimento por UV, perda de plastificantes e inicio de fragilizacao do material. Nao e apenas mudanca visual: a perda de ductilidade pode preceder trinca, quebra e liberação de bordas cortantes.';
    b1='Exposicao solar, intemperismo e fim de vida do composto plastico.'; b2='Fragilizacao, trinca e ruptura sob impacto ou flexao.'; b3='Lavagem agressiva, calor acumulado e ausencia de protecao UV.';
    p31='Inspecionar cor, brilho, textura e sinais de craquelamento em toda a superficie plastica.'; p32='Verificar se a peca continua com flexibilidade minima para o uso previsto.'; p33='Conferir zonas expostas ao sol e proximidade de fixacoes que aceleram fadiga.'; p34='Substituir a peca quando houver perda estrutural perceptivel ou fissuras iniciais.';
    m1c='Plastico fragilizado com fissura ativa'; m1a='Interdicao parcial e substituicao'; m1p='0-24h';
    m2c='Esbranquiçamento com perda de ductilidade'; m2a='Troca prioritaria da peca'; m2p='Ate 7 dias';
    m3c='Desgaste inicial sem quebra'; m3a='Protecao UV e monitoramento'; m3p='Ate 30 dias'
  },
  [ordered]@{
    id='play-074'; slug='plastico-com-trincas-ou-quebras'; title='Plastico com trincas ou quebras'; fileTitle='Playground: Plastico com trincas ou quebras'; grav='Media'; resp='Mista - requer avaliacao tecnica'; score='6.0/10';
    pregunta="Brinquedo com 'Plástico com trincas ou quebras' pode machucar as crianças?";
    resposta="A irregularidade 'Plástico com trincas ou quebras' indica nao conformidade tecnica identificada no PlaygroundScan. Em linguagem simples, isso eleva o risco de acidente e exige correcao com base na ABNT NBR 16071. Na pratica, a inspecao deve confirmar o desvio em campo, registrar evidencias fotograficas e executar adequacao conforme requisito normativo aplicavel. Referencia principal: Parte 2. Citacao tecnica: Parte 2, item 4.4.";
    normes='ABNT NBR 16071 | ABNT NBR 16071-2';
    p2='Trincas em plastico sao criticas porque concentram tensao nas extremidades e podem transformar um componente aparentemente estavel em um ponto de ruptura repentina. Em brinquedo infantil, a falha ocorre sob carga dinamica, nao apenas em repouso.';
    b1='Impacto repetitivo, fadiga e montagem com interferencia.'; b2='Rompimento abrupto, aresta viva e queda de componente.'; b3='Sol, calor, envelhecimento e limpeza inadequada.';
    p31='Localizar todas as trincas, com fotos e indicacao de comprimento, abertura e localizacao.'; p32='Verificar se a fissura atravessa zona de carga ou apenas acabamento superficial.'; p33='Executar teste controlado de estabilidade da peca para evitar ruptura em uso.'; p34='Substituir o componente caso a trinca comprometa a resistencia ou gere aresta viva.';
    m1c='Trinca estrutural com risco de ruptura'; m1a='Interdicao imediata e substituicao'; m1p='0-24h';
    m2c='Quebra parcial com borda agressiva'; m2a='Correcao prioritaria e bloqueio local'; m2p='Ate 7 dias';
    m3c='Fissura inicial sem perda de integridade'; m3a='Monitoramento e reforco preventivo'; m3p='Ate 30 dias'
  },
  [ordered]@{
    id='play-075'; slug='afastamento-insuficiente-entre-partes-moveis-12mm'; title='Afastamento insuficiente entre partes moveis (< 12mm)'; fileTitle='Playground: Afastamento insuficiente entre partes moveis (< 12mm)'; grav='Critica'; resp='Mista - requer avaliacao tecnica'; score='9.0/10';
    pregunta="'Afastamento insuficiente entre partes móveis (< 12mm)' no playground é só detalhe ou é um problema de segurança que precisa corrigir?";
    resposta="A irregularidade 'Afastamento insuficiente entre partes móveis (< 12mm)' indica nao conformidade tecnica identificada no PlaygroundScan. Em linguagem simples, isso eleva o risco de acidente e exige correcao com base na ABNT NBR 16071. Na pratica, a inspecao deve confirmar o desvio em campo, registrar evidencias fotograficas e executar adequacao conforme requisito normativo aplicavel. Referencia principal: Parte 2. Citacao tecnica: Parte 2, item 6.3 e Anexo E.1.5.";
    normes='ABNT NBR 16071 | ABNT NBR 16071-2';
    p2='O afastamento inferior a 12 mm entre partes moveis cria a janela classica de aprisionamento e esmagamento. O problema se agrava porque o vão pode variar com vibracao, flexao e desgaste, fazendo a tolerancia desaparecer durante o uso.';
    b1='Projeto com folga insuficiente e tolerancias mal definidas.'; b2='Pinçamento progressivo de dedo/pele entre componentes em movimento.'; b3='Vibracao, folga de fixacao e corrosao dos elementos de contato.';
    p31='Medir o afastamento em repouso e sob acao dinamica representativa do uso.'; p32='Verificar a menor abertura em toda a trajetória de movimento do conjunto.'; p33='Confirmar se existe protecao adicional que impeça acesso ao vao perigoso.'; p34='Sem afastamento seguro, bloquear o equipamento e corrigir geometria ou protecao.';
    m1c='Afastamento abaixo de 12 mm em movimento'; m1a='Interdicao imediata e adequacao estrutural'; m1p='0-24h';
    m2c='Folga limite com risco de reducao dinamica'; m2a='Correcao prioritaria da geometria'; m2p='Ate 7 dias';
    m3c='Distancia aceitavel com monitoramento'; m3a='Reinspecao curta e ajuste preventivo'; m3p='Ate 30 dias'
  },
  [ordered]@{
    id='play-076'; slug='cama-de-areia-cascalho-300mm-de-profundidade'; title='Cama de areia/cascalho < 300mm de profundidade'; fileTitle='Playground: Cama de areia/cascalho < 300mm de profundidade'; grav='Media'; resp='Mista - requer avaliacao tecnica'; score='6.0/10';
    pregunta="Com 'Cama de areia/cascalho < 300mm de profundidade', o piso do playground fica inseguro para quedas?";
    resposta="A irregularidade 'Cama de areia/cascalho < 300mm de profundidade' indica nao conformidade tecnica identificada no PlaygroundScan. Em linguagem simples, isso eleva o risco de acidente e exige correcao com base na ABNT NBR 16071. Na pratica, a inspecao deve confirmar o desvio em campo, registrar evidencias fotograficas e executar adequacao conforme requisito normativo aplicavel. Referencia principal: Parte 3. Citacao tecnica: Parte 3, Tabela A.1.";
    normes='ABNT NBR 16071 | ABNT NBR 16071-3';
    p2='Areia ou cascalho com profundidade inferior ao especificado perde capacidade de deslocamento e amortecimento, reduzindo a dissipacao de energia em queda. O material pode parecer solto, mas a camada superficial nao sustenta o desempenho requerido.';
    b1='Perda de volume por arraste, compactacao e reposicao insuficiente.'; b2='Queda com amortecimento reduzido e contato rigido com o subleito.'; b3='Lixeira, drenagem inadequada e escavacao por uso intenso.';
    p31='Medir profundidade em pontos distribuídos e verificar uniformidade da camada.'; p32='Confirmar se ha area de subleito exposto ou mistura com material compactado.'; p33='Analisar se a profundidade atende a altura critica associada ao brinquedo.'; p34='Repor material, nivelar e registrar nova medicao antes da reabertura.';
    m1c='Profundidade critica abaixo do minimo'; m1a='Restricao imediata e recomposicao'; m1p='0-24h';
    m2c='Perda significativa de volume na zona de impacto'; m2a='Reposicao prioritaria da camada'; m2p='Ate 7 dias';
    m3c='Desgaste moderado com controle possivel'; m3a='Nivelamento e monitoramento'; m3p='Ate 30 dias'
  },
  [ordered]@{
    id='play-077'; slug='laterais-do-deslize-entre-100-e-500mm'; title='Laterais do deslize entre 100 mm e 500 mm'; fileTitle='Playground: Laterais do deslize entre 100 mm e 500 mm'; grav='Media'; resp='Mista - requer avaliacao tecnica'; score='6.0/10';
    pregunta="'Laterais do deslize entre 100 mm e 500 mm' no playground é só detalhe ou é um problema de segurança que precisa corrigir?";
    resposta="A irregularidade 'Laterais do deslize entre 100 mm e 500 mm' indica nao conformidade tecnica identificada no PlaygroundScan. Em linguagem simples, isso eleva o risco de acidente e exige correcao com base na ABNT NBR 16071. Na pratica, a inspecao deve confirmar o desvio em campo, registrar evidencias fotograficas e executar adequacao conforme requisito normativo aplicavel. Referencia principal: Parte 2. Citacao tecnica: Parte 2, Anexo B.2.6 e Tab. B.2.";
    normes='ABNT NBR 16071 | ABNT NBR 16071-2';
    p2='Laterais mal dimensionadas no escorregador criam uma faixa ambigua: pequenas demais expõem a crianca, grandes demais alteram o controle do movimento. O risco e de saida lateral, desequilibrio e impacto fora da pista.';
    b1='Geometria fora do envelope, laterais baixas ou mal posicionadas.'; b2='Desvio lateral na descida com queda fora do plano de seguranca.'; b3='Alta velocidade, superficie lisa e ausencia de transicao correta.';
    p31='Medir altura e continuidade das laterais em toda a extensao da pista.'; p32='Verificar se o corredor lateral realmente impede saida do corpo em uso real.'; p33='Conferir bordas, fixacoes e transicao para zona de chegada.'; p34='Corrigir geometria e reforcar laterais antes de liberar o brinquedo.';
    m1c='Laterais insuficientes com saida lateral'; m1a='Interdicao e adequacao geometrica'; m1p='0-24h';
    m2c='Laterais fora da faixa com risco de contato'; m2a='Correcao prioritaria do perfil'; m2p='Ate 7 dias';
    m3c='Desvio leve sem saida confirmada'; m3a='Ajuste preventivo e reinspecao'; m3p='Ate 30 dias'
  },
  [ordered]@{
    id='play-078'; slug='falta-de-segunda-rota-de-evacuacao-em-brinquedao'; title='Falta de segunda rota de evacuacao em Brinquedao'; fileTitle='Playground: Falta de segunda rota de evacuacao em Brinquedao'; grav='Media'; resp='Mista - requer avaliacao tecnica'; score='6.0/10';
    pregunta="Com 'Falta de segunda rota de evacuação em Brinquedão', o espaço do playground fica perigoso em uso e emergência?";
    resposta="A irregularidade 'Falta de segunda rota de evacuação em Brinquedão' indica não conformidade técnica identificada no PlaygroundScan. Em linguagem simples, isso eleva o risco de acidente e exige correção com base na ABNT NBR 16071. Na prática, a inspeção deve confirmar o desvio em campo, registrar evidências fotográficas e executar adequação conforme requisito normativo aplicável. Referência principal: Parte 2. Citação técnica: Parte 2, item 5.3.";
    normes='ABNT NBR 16071 | ABNT NBR 16071-2';
    p2='A falta de segunda rota transforma um evento localizado em problema de seguranca de fluxo. Em caso de panico, obstrucao ou usuario com mobilidade reduzida, a unica saida pode virar ponto de congestionamento e aumentar o tempo de resposta.';
    b1='Layout único de saida, sem redundancia operacional.'; b2='Gargalo de fuga em caso de incendio, obstrucao ou emergencia.'; b3='Brinquedao fechado, fluxo intenso e baixa visibilidade interna.';
    p31='Mapear a rota primaria e identificar se existe rota secundaria real e utilizavel.'; p32='Simular evacuação com obstrucao de um dos caminhos para validar redundancia.'; p33='Verificar larguras livres, sinalizacao e continuidade até area segura.'; p34='Criar segunda rota ou reorganizar layout para garantir saida alternativa.';
    m1c='Sem rota secundaria e com congestionamento potencial'; m1a='Interdicao parcial e adequacao de saida'; m1p='0-24h';
    m2c='Uma saida com gargalo e baixa redundancia'; m2a='Reorganizar layout e sinalizacao'; m2p='Ate 7 dias';
    m3c='Rota unica mas funcional em cenario controlado'; m3a='Plano de melhoria e simulacao periodica'; m3p='Ate 30 dias'
  },
  [ordered]@{
    id='play-079'; slug='secao-de-saida-do-escorregador-curta-300-500mm'; title='Secao de saida do escorregador curta (< 300/500mm)'; fileTitle='Playground: Secao de saida do escorregador curta (< 300/500mm)'; grav='Media'; resp='Mista - requer avaliacao tecnica'; score='6.0/10';
    pregunta="Com 'Seção de saída do escorregador curta (< 300/500mm)', existe risco real de queda no brinquedo?";
    resposta="A irregularidade 'Seção de saída do escorregador curta (< 300/500mm)' indica não conformidade técnica identificada no PlaygroundScan. Em linguagem simples, isso eleva o risco de acidente e exige correção com base na ABNT NBR 16071. Na prática, a inspeção deve confirmar o desvio em campo, registrar evidências fotográficas e executar adequação conforme requisito normativo aplicável. Referência principal: Parte 2. Citação técnica: Parte 2, Anexo B.2.5 e Tab. B.1.";
    normes='ABNT NBR 16071 | ABNT NBR 16071-2';
    p2='Uma seção de saída curta não permite dissipar a velocidade final da descida. Sem essa área de transição, a criança sai do escorregador ainda em postura desbalanceada, o que eleva o risco de tombamento ao tocar o piso.';
    b1='Curvatura final insuficiente e comprimento reduzido da zona de chegada.'; b2='Saida abrupta com projecao para frente ou lateral.'; b3='Piso rigido, inclinacao excessiva e ausencia de amortecimento na boca de saida.';
    p31='Medir o comprimento util da saida e comparar com a faixa minima aplicada ao equipamento.'; p32='Verificar se a transicao final estabiliza a postura antes do contato com o piso.'; p33='Checar bordas, altura e continuidade com a zona de impacto do escorregador.'; p34='Readequar a saida com prolongamento e nova validacao funcional.';
    m1c='Saida curta com desequilibrio de desembarque'; m1a='Interdicao e prolongamento da saida'; m1p='0-24h';
    m2c='Comprimento abaixo do ideal com queda recorrente'; m2a='Correcao prioritaria da transicao'; m2p='Ate 7 dias';
    m3c='Pequeno desvio sem perda de controle'; m3a='Ajuste preventivo e reinspecao'; m3p='Ate 30 dias'
  },
  [ordered]@{
    id='play-080'; slug='escorregador-com-calos-parafusos-expostos-ou-degraus'; title='Escorregador com calos, parafusos expostos ou degraus'; fileTitle='Playground: Escorregador com calos, parafusos expostos ou degraus'; grav='Media'; resp='Mista - requer avaliacao tecnica'; score='6.0/10';
    pregunta="Com 'Escorregador com calos, parafusos expostos ou degraus', existe risco real de queda no brinquedo?";
    resposta="A irregularidade 'Escorregador com calos, parafusos expostos ou degraus' indica não conformidade técnica identificada no PlaygroundScan. Em linguagem simples, isso eleva o risco de acidente e exige correção com base na ABNT NBR 16071. Na prática, a inspeção deve confirmar o desvio em campo, registrar evidências fotográficas e executar adequação conforme requisito normativo aplicável. Referência principal: Parte 2. Citação técnica: Parte 2, Anexo B.2.7.";
    normes='ABNT NBR 16071 | ABNT NBR 16071-2';
    p2='Calos na pista, parafusos expostos ou degraus internos quebram a continuidade de deslizamento e introduzem pontos de impacto e engate. O usuario pode perder velocidade de forma brusca, bater partes do corpo na irregularidade ou ser projetado fora da linha correta.';
    b1='Montagem inadequada, manutencao parcial e fixacoes aparentes.'; b2='Engate, impacto seco e desvio de trajeto na descida.'; b3='Calos, desgaste localizado e ausencia de acabamento liso.';
    p31='Inspecionar a continuidade da pista e localizar qualquer saliencia, parafuso ou transicao abrupta.'; p32='Verificar se ha degraus improvisados, emendas ou desníveis na superfície de deslize.'; p33='Conferir se a fixacao dos elementos expostos pode ser embutida ou coberta tecnicamente.'; p34='Remover saliencias, nivelar a pista e reinspecionar a qualidade da descida.';
    m1c='Saliencia ou parafuso em zona de deslize'; m1a='Interdicao imediata e correcao da pista'; m1p='0-24h';
    m2c='Degrau/irregularidade com impacto recorrente'; m2a='Adequacao prioritaria da superficie'; m2p='Ate 7 dias';
    m3c='Calo superficial sem exposicao direta'; m3a='Acabamento preventivo e monitoramento'; m3p='Ate 30 dias'
  }
)

$html = [IO.File]::ReadAllText($kbPath,[Text.Encoding]::UTF8)
$rx = '(?s)<script[^>]*id="dados-embed"[^>]*>(.*?)</script>'
$mScript = [regex]::Match($html,$rx)
if(-not $mScript.Success){ throw 'dados-embed not found' }
$data = $mScript.Groups[1].Value | ConvertFrom-Json
$allFaqs = $data.'playgrounds.json'.faqs
$batch = $allFaqs | Where-Object { $_.id -in $items.id }
if($batch.Count -ne 10){ throw "batch count unexpected: $($batch.Count)" }

$created=@(); $refsAdded=0; $cards=@()
foreach($item in $items){
  $faq = $allFaqs | Where-Object { $_.id -eq $item.id }
  if(-not $faq){ throw "FAQ not found: $($item.id)" }
  $fileName = "artigo-playground-$($item.slug).html"
  $fullPath = "$root/artigos/playgrounds/$fileName"
  $url = "/artigos/playgrounds/$fileName"
  $topicTitle = To-Ascii $item.title
  $fileTitle = To-Ascii $item.fileTitle
  $preg = To-Ascii $item.pregunta
  $resp = To-Ascii $item.resposta
  $normes = To-Ascii $item.normes
  $grav = To-Ascii $item.grav
  $respType = To-Ascii $item.resp
  $sevLabel = if($grav -match 'Critica'){ 'Critica' } elseif($grav -match 'Alta'){ 'Alta' } else { 'Media' }
  $pProb = if($grav -match 'Critica'){ 90 } else { 78 }
  $pSev = if($grav -match 'Critica'){ 92 } else { 84 }
  $pExp = if($grav -match 'Critica'){ 82 } else { 74 }
  $pAct = if($grav -match 'Critica'){ 96 } else { 88 }
  $p = @{}
  $p.p2 = To-Ascii $item.p2
  $p.b1 = To-Ascii $item.b1
  $p.b2 = To-Ascii $item.b2
  $p.b3 = To-Ascii $item.b3
  $p.p31 = To-Ascii $item.p31
  $p.p32 = To-Ascii $item.p32
  $p.p33 = To-Ascii $item.p33
  $p.p34 = To-Ascii $item.p34
  $p.m1c = To-Ascii $item.m1c
  $p.m1a = To-Ascii $item.m1a
  $p.m1p = To-Ascii $item.m1p
  $p.m2c = To-Ascii $item.m2c
  $p.m2a = To-Ascii $item.m2a
  $p.m2p = To-Ascii $item.m2p
  $p.m3c = To-Ascii $item.m3c
  $p.m3a = To-Ascii $item.m3a
  $p.m3p = To-Ascii $item.m3p

  $doc = @"
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Guia tecnico sobre '$topicTitle' com criterios ABNT NBR 16071, mecanismo de falha, protocolo de ensaio e matriz de acao para playgrounds.">
    <title>$fileTitle | Proton Engenharia</title>
    <link rel="canonical" href="https://www.protoncd.com.br/artigos/playgrounds/$fileName">
    <link rel="stylesheet" href="../../css/all.min.css">
    <link rel="icon" href="../../img/faviconb.ico" type="image/x-icon">
    <link rel="stylesheet" href="../../css/variables.css">
    <link rel="stylesheet" href="../../css/base.css">
    <link rel="stylesheet" href="../../css/components.css">
    <link rel="stylesheet" href="../../css/layout.css">
    <link rel="stylesheet" href="../../css/animations.css">
    <style>
    .article-container { max-width: 920px; margin: 0 auto; padding: var(--space-8) var(--space-4); }
    .article-content { font-size: 1.03rem; }
    .article-hero-panel { background: var(--bg-card); border: 1px solid var(--border-subtle); border-radius: var(--radius-xl); padding: var(--space-6); margin-bottom: var(--space-7); }
    .article-intro { max-width: 760px; margin: 0 auto var(--space-5); text-align: center; }
    .article-mini-stats { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: var(--space-3); margin: 0 0 var(--space-5); }
    .article-mini-stat { background: rgba(255, 255, 255, 0.02); border: 1px solid var(--border-subtle); border-radius: var(--radius-lg); padding: var(--space-3); text-align: center; }
    .article-mini-stat strong { display: block; color: var(--text-primary); font-size: 1.12rem; margin-bottom: 4px; }
    .article-mini-stat span { color: var(--text-secondary); font-size: var(--fs-sm); }
    .risk-chart { background: var(--bg-subtle); border: 1px solid var(--border-subtle); border-radius: var(--radius-xl); padding: var(--space-5); margin: var(--space-5) 0; }
    .risk-row { display: grid; grid-template-columns: 200px 1fr auto; align-items: center; gap: var(--space-3); margin-bottom: var(--space-3); }
    .risk-row:last-child { margin-bottom: 0; }
    .risk-bar { height: 10px; border-radius: 999px; background: rgba(255, 255, 255, 0.08); overflow: hidden; }
    .risk-bar span { display: block; height: 100%; background: linear-gradient(90deg, #f59e0b 0%, #ef4444 100%); }
            .article-content h2 { font-size: var(--fs-xl); font-weight: var(--fw-bold); color: var(--text-primary); margin-top: var(--space-8); margin-bottom: var(--space-4); padding: var(--space-3) var(--space-4); border: 1px solid rgba(239, 68, 68, 0.28); border-radius: var(--radius-lg); background: linear-gradient(135deg, rgba(239, 68, 68, 0.12), rgba(239, 68, 68, 0.03)); }
            .article-content p { margin-bottom: var(--space-4); line-height: 1.78; color: var(--text-secondary); }
            .article-content ul { margin-left: 0; padding: var(--space-4) var(--space-5); margin-bottom: var(--space-4); border: 1px solid var(--border-subtle); border-radius: var(--radius-lg); background: rgba(15, 23, 42, 0.45); list-style: none; }
            .article-content li { margin-bottom: var(--space-2); line-height: 1.6; padding: var(--space-3); border: 1px solid var(--border-subtle); border-radius: var(--radius-md); background: rgba(255, 255, 255, 0.02); }
            .content-box { background: var(--bg-subtle); border: 1px solid var(--border-subtle); padding: var(--space-4); border-radius: var(--radius-lg); margin: var(--space-4) 0; }
            .decision-table { width: 100%; border-collapse: collapse; margin: var(--space-4) 0; border: 1px solid var(--border-subtle); }
            .decision-table th, .decision-table td { border: 1px solid var(--border-subtle); padding: 10px; text-align: left; }
            .decision-table th { background: rgba(239, 68, 68, 0.08); color: var(--text-primary); }
            @media (max-width: 900px) { .article-mini-stats { grid-template-columns:1fr; } .risk-row { grid-template-columns:1fr; } }
            </style>
            </head>
            <body>
            <nav class="nav" id="main-nav">
            <div class="nav-inner">
            <a href="../../index.html" class="nav-logo">
            <img src="../../img/logo_proton_branco.png" alt="Proton Engenharia" width="36" height="36">
            <span class="nav-logo-text">PROTON <span>Engenharia</span></span>
            </a>
            <div class="nav-links">
            <a href="../../index.html#inicio">Inicio</a>
            <a href="../../index.html#servicos">Servicos</a>
            <a href="../../index.html#contato" class="nav-cta"><i class="fab fa-whatsapp"></i> Contato</a>
            </div>
            <button class="nav-mobile-toggle" id="mobile-toggle" aria-label="Menu"><i class="fas fa-bars"></i></button>
            </div>
            </nav>

            <main class="article-container">
            <article class="article-content">
            <div class="article-hero-panel">
            <div class="article-intro">
            <h1>$fileTitle</h1>
            <p>Conteudo tecnico para decisao rapida em seguranca de playgrounds, com base normativa e plano corretivo.</p>
            </div>
            <div class="article-mini-stats">
            <div class="article-mini-stat"><strong>$($item.score)</strong><span>Indice de criticidade</span></div>
            <div class="article-mini-stat"><strong>$(if($grav -match 'Alta|Critica'){'Prioritaria (ate 7 dias)'}else{'Programada (ate 30 dias)'})</strong><span>Janela de resposta</span></div>
            <div class="article-mini-stat"><strong>$respType</strong><span>Responsavel principal</span></div>
            </div>
            </div>

            <h2>1. Diagnostico tecnico da nao conformidade</h2>
            <div class="content-box">
            <p><strong>Pergunta de campo:</strong> $preg</p>
            <p><strong>Interpretacao tecnica:</strong> $resp</p>
            <p><strong>Referencias normativas:</strong> $normes</p>
            </div>

            <h2>2. Mecanismo de falha e risco operacional</h2>
            <p>$($p.p2)</p>
            <ul>
            <li><strong>Origem recorrente:</strong> $($p.b1)</li>
            <li><strong>Modo de falha:</strong> $($p.b2)</li>
            <li><strong>Agravantes:</strong> $($p.b3)</li>
            </ul>

            <div class="risk-chart">
            <div class="risk-row"><strong>Probabilidade</strong><div class="risk-bar"><span style="width:$pProb%;"></span></div><span>$sevLabel</span></div>
            <div class="risk-row"><strong>Severidade</strong><div class="risk-bar"><span style="width:$pSev%;"></span></div><span>$sevLabel</span></div>
            <div class="risk-row"><strong>Exposicao</strong><div class="risk-bar"><span style="width:$pExp%;"></span></div><span>Continua</span></div>
            <div class="risk-row"><strong>Prioridade de acao</strong><div class="risk-bar"><span style="width:$pAct%;"></span></div><span>Tratamento tecnico</span></div>
            </div>

            <h2>3. Protocolo de inspecao e evidencias minimas</h2>
            <ul>
            <li>$($p.p31)</li>
            <li>$($p.p32)</li>
            <li>$($p.p33)</li>
            <li>$($p.p34)</li>
            </ul>

            <h2>4. Matriz de decisao corretiva</h2>
            <table class="decision-table">
            <thead><tr><th>Cenario</th><th>Acao recomendada</th><th>Prazo</th></tr></thead>
            <tbody>
            <tr><td>$($p.m1c)</td><td>$($p.m1a)</td><td>$($p.m1p)</td></tr>
            <tr><td>$($p.m2c)</td><td>$($p.m2a)</td><td>$($p.m2p)</td></tr>
            <tr><td>$($p.m3c)</td><td>$($p.m3a)</td><td>$($p.m3p)</td></tr>
            </tbody>
            </table>

            <section class="cta-section" style="margin-top: var(--space-8); padding: var(--space-6); border: 1px solid var(--border-subtle); border-radius: var(--radius-xl); background: linear-gradient(135deg, rgba(14,165,233,0.12), rgba(14,165,233,0.03)); text-align: center;">
            <h3 style="margin-bottom: var(--space-3);">Precisa de inspecao tecnica no seu playground?</h3>
            <p style="margin-bottom: var(--space-4);">A Proton Engenharia realiza diagnostico com base na ABNT NBR 16071, priorizacao de risco e plano de acao executavel.</p>
            <div style="display:flex; gap:12px; justify-content:center; flex-wrap:wrap;">
            <a href="https://api.whatsapp.com/send?phone=5562992852704&text=Ola! Preciso de inspecao tecnica de playground." target="_blank" rel="noopener noreferrer" class="btn btn-primary btn-sm">
            <i class="fab fa-whatsapp"></i> Solicitar Inspecao
            </a>
            <a href="tel:5562992852704" class="btn btn-secondary btn-sm">
            <i class="fas fa-phone"></i> Ligar Agora
            </a>
            </div>
            </section>
            </article>
            </main>

            <footer class="footer">
            <div class="container">
            <div class="footer-bottom">
            <p>&copy; 2026 Proton Engenharia Diagnostica. Todos os direitos reservados.</p>
            </div>
            </div>
            </footer>

            <script src="../../js/main.js"></script>
            </body>
            </html>
            "@

  [IO.File]::WriteAllText($fullPath,$doc,$enc)
  $created += $fileName

  if(-not $faq.artigo_relacionado){
    $faq | Add-Member -NotePropertyName artigo_relacionado -NotePropertyValue ([pscustomobject]@{
      titulo = "Playground: $fileTitle"
      url = $url
      categoria = 'Playgrounds'
    }) -Force
    $refsAdded++
  }

  $icon = if($grav -match 'Critica|Alta'){ 'fas fa-exclamation-triangle' } else { 'fas fa-balance-scale' }
  $cardTitle = if($topicTitle.Length -gt 46){ $topicTitle.Substring(0,46).Trim() + '...' } else { $topicTitle }
  $cards += @"
            <a href="$fileName" class="card hover-lift" style="text-decoration:none;">
            <div class="card-icon red"><i class="$icon"></i></div>
            <h3 class="card-title">$cardTitle</h3>
            <p class="card-text">Diagnostico tecnico, risco operacional e acao corretiva conforme NBR 16071.</p>
            </a>
            "@
}

$newJsonText = ($data | ConvertTo-Json -Depth 35)
$newScript = "<script type=`"application/json`" id=`"dados-embed`">`r`n$newJsonText`r`n</script>"
$newHtml = [regex]::Replace($html,$rx,[System.Text.RegularExpressions.MatchEvaluator]{ param($m) $newScript },1)
[IO.File]::WriteAllText($kbPath,$newHtml,$enc)

$hub = [IO.File]::ReadAllText($hubPath,[Text.Encoding]::UTF8)
$toAdd = @()
foreach($c in $cards){
  if($c -match 'href="([^"]+)"'){
    $h = $matches[1]
    if($hub -notmatch [regex]::Escape("href=`"$h`"")){ $toAdd += $c }
  }
}
if($toAdd.Count -gt 0 -and $hub -match '<script src="../../js/main.js"></script>'){
  $insert = ($toAdd -join "`r`n")
  $hub = $hub -replace '(?s)\s*<script src="../../js/main\.js"></script>', "`r`n$insert`r`n    <script src=`"../../js/main.js`"></script>"
  [IO.File]::WriteAllText($hubPath,$hub,$enc)
}

"CREATED_COUNT=$($created.Count)"
$created | ForEach-Object { "CREATED: $_" }
"REFS_ADDED=$refsAdded"
"CARDS_ADDED=$($toAdd.Count)"
