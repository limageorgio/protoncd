# -*- coding: utf-8 -*-
"""
Script para adicionar Schema.org e melhorias de SEO nas páginas das cidades
"""

#  Dados de cada cidade
cidades = {
    "rio-de-janeiro": {
        "nome": "Rio de Janeiro",
        "sigla": "RJ",
        "lat": "-22.9068",
        "lng": "-43.1729",
        "tribunal": "TJRJ",
        "destaque": "segunda maior concentração de elevadores do Brasil",
        "regioes": "Zona Sul (Copacabana, Ipanema, Leblon, Botafogo), Barra da Tijuca, Tijuca, Centro, Niterói",
        "regioes_detalhadas": "Copacabana • Ipanema • Leblon • Botafogo • Flamengo • Tijuca • Barra da Tijuca • Recreio • Jacarepaguá • Centro • Niterói • São Gonçalo"
    },
    "belo-horizonte": {
        "nome": "Belo Horizonte",
        "sigla": "MG",
        "lat": "-19.9167",
        "lng": "-43.9345",
        "tribunal": "TJMG",
        "destaque": "principal centro urbano de Minas Gerais",
        "regioes": "Savassi, Lourdes, Funcionários, Pampulha, Nova Lima, Contagem",
        "regioes_detalhadas": "Savassi • Lourdes • Funcionários • Pampulha • Santo Agostinho • Serra • Buritis • Nova Lima • Contagem • Betim • Região Metropolitana"
    },
    "curitiba": {
        "nome": "Curitiba",
        "sigla": "PR",
        "lat": "-25.4284",
        "lng": "-49.2733",
        "tribunal": "TJPR",
        "destaque": "capital com maior IDH do sul do Brasil",
        "regioes": "Batel, Água Verde, Ecoville, Bigorrilho, São José dos Pinhais",
        "regioes_detalhadas": "Batel • Água Verde • Ecoville • Bom Retiro • Bigorrilho • Centro • Portão • São José dos Pinhais • Pinhais • Araucária • Colombo"
    },
    "porto-alegre": {
        "nome": "Porto Alegre",
        "sigla": "RS",
        "lat": "-30.0346",
        "lng": "-51.2177",
        "tribunal": "TJRS",
        "destaque": "principal centro urbano do Rio Grande do Sul",
        "regioes": "Moinhos de Vento, Bela Vista, Petrópolis, Auxiliadora, Canoas",
        "regioes_detalhadas": "Moinhos de Vento • Bela Vista • Petrópolis • Auxiliadora • Mont'Serrat • Centro • Canoas • Novo Hamburgo • São Leopoldo • Região Metropolitana"
    }
}

# Template do Schema.org para cada cidade
def gerar_schema(cidade_key, dados):
    return f'''    <!-- Schema.org Service + LocalBusiness -->
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "Service",
      "serviceType": "Análise de Vibração e Ruídos em Elevadores",
      "provider": {{
        "@type": "LocalBusiness",
        "name": "Proton Engenharia Mecânica - {dados['nome']}",
        "@id": "https://www.protoncd.com.br/{cidade_key}/analise-vibracao-elevadores-{dados['sigla'].lower()}.html",
        "image": "https://www.protoncd.com.br/img/logo_proton.png",
        "telephone": "+55-62-99285-2704",
        "email": "lima.georgio.eng@gmail.com",
        "priceRange": "$$$",
        "address": {{
          "@type": "PostalAddress",
          "addressLocality": "{dados['nome']}",
          "addressRegion": "{dados['sigla']}",
          "addressCountry": "BR"
        }},
        "geo": {{
          "@type": "GeoCoordinates",
          "latitude": "{dados['lat']}",
          "longitude": "{dados['lng']}"
        }},
        "areaServed": {{
          "@type": "City",
          "name": "{dados['nome']}"
        }}
      }},
      "description": "Análise diagnóstica avançada de vibração e ruídos em elevadores com tecnologia 360° exclusiva em {dados['nome']}. Laudo técnico assinado por Engenheiro Mecânico com ART-CREA. Atendemos {dados['regioes']}.",
      "offers": {{
        "@type": "Offer",
        "availability": "https://schema.org/InStock",
        "priceSpecification": {{
          "@type": "PriceSpecification",
          "priceCurrency": "BRL"
        }}
      }}
    }}
    </script>
    
    <!-- Schema.org FAQPage -->
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "FAQPage",
      "mainEntity": [
        {{
          "@type": "Question",
          "name": "Vocês analisam elevadores de quais marcas em {dados['nome']}?",
          "acceptedAnswer": {{
            "@type": "Answer",
            "text": "Realizamos análise de vibração e ruídos em todas as marcas de elevadores em {dados['nome']}, incluindo Otis, Atlas Schindler, ThyssenKrupp, Contratto, Arsenal Elevadores, Elevadores Villarta, Elevadores Everest, Elevadores Tacla, e demais fabricantes. Nossa análise é independente e utiliza instrumentação calibrada com tecnologia 360°."
          }}
        }},
        {{
          "@type": "Question",
          "name": "Atendem quais regiões de {dados['nome']}?",
          "acceptedAnswer": {{
            "@type": "Answer",
            "text": "Atendemos toda a região metropolitana de {dados['nome']}, incluindo {dados['regioes_detalhadas']}."
          }}
        }},
        {{
          "@type": "Question",
          "name": "O laudo serve para perícia judicial em {dados['nome']}?",
          "acceptedAnswer": {{
            "@type": "Answer",
            "text": "Sim. O laudo técnico é assinado por Engenheiro Mecânico com ART-CREA e pode ser utilizado para perícias técnicas judiciais e extrajudiciais, processos no {dados['tribunal']} (Tribunal de Justiça de {dados['nome']}), certificação TÜV Rheinland, Bureau Veritas, além de atender exigências de seguradoras e normas técnicas."
          }}
        }},
        {{
          "@type": "Question",
          "name": "Quanto tempo leva a análise em {dados['nome']}?",
          "acceptedAnswer": {{
            "@type": "Answer",
            "text": "A análise técnica com instrumentação 360° leva de 2 a 4 horas por elevador, dependendo da complexidade do sistema. Agendamos conforme disponibilidade do condomínio em {dados['nome']}. O laudo completo com análise espectral, gráficos e recomendações é entregue em até 7 dias úteis após a inspeção."
          }}
        }},
        {{
          "@type": "Question",
          "name": "A análise previne acidentes com elevador em {dados['nome']}?",
          "acceptedAnswer": {{
            "@type": "Answer",
            "text": "Sim. Nossa análise diagnóstica identifica falhas mecânicas, vibrações excessivas, desalinhamentos e componentes desgastados antes que evoluam para situações críticas. Como {dados['destaque']}, a detecção precoce de anomalias é essencial para a prevenção de acidentes e manutenção da segurança operacional dos usuários."
          }}
        }}
      ]
    }}
    </script>'''

# Gera arquivos com os schemas
import os

base_path = r"h:\apps\protoncd"

# Mapeamento correto dos nomes de arquivos
nomes_arquivos = {
    "rio-de-janeiro": "rj",
    "belo-horizonte": "bh",
    "curitiba": "curitiba",
    "porto-alegre": "poa"
}

for cidade_key, dados in cidades.items():
    nome_arquivo = nomes_arquivos[cidade_key]
    arquivo = f"{base_path}\\{cidade_key}\\analise-vibracao-elevadores-{nome_arquivo}.html"
    
    if os.path.exists(arquivo):
        print(f"✅ Processando {dados['nome']}...")
        
        with open(arquivo, 'r', encoding='utf-8') as f:
            conteudo = f.read()
        
        # Verifica se já tem Schema.org
        if '"@context": "https://schema.org"' in conteudo:
            print(f"   ⚠️  {dados['nome']} já possui Schema.org, pulando...")
            continue
        
        # Procura onde inserir (antes do primeiro <link rel="stylesheet")
        marcador = '<link rel="stylesheet" href="../css/all.min.css">'
        
        if marcador in conteudo:
            schema = gerar_schema(cidade_key, dados)
            conteudo_novo = conteudo.replace(marcador, f"{schema}\n    \n    {marcador}")
            
            with open(arquivo, 'w', encoding='utf-8') as f:
                f.write(conteudo_novo)
            
            print(f"   ✅ Schema.org adicionado para {dados['nome']}!")
        else:
            print(f"   ❌ Marcador não encontrado em {dados['nome']}")
    else:
        print(f"❌ Arquivo não encontrado: {arquivo}")

print("\n🎉 Processo concluído!")
