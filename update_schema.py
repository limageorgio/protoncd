import glob
import re

files = glob.glob('*.html') + glob.glob('*/*.html')
count = 0
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Let's check how many files have ProfessionalService with founder.
    if '"founder": {' in content:
        # Regex to match the founder block correctly with nested objects
        pattern = r'"founder":\s*\{\s*"@type":\s*"Person".*?\}'
        old_founder = re.search(pattern, content, re.MULTILINE | re.DOTALL)
        if old_founder:
            new_founder = '''"founder": {
          "@type": "Person",
          "name": "Georgio Batista de Lima",
          "jobTitle": "Engenheiro Mecânico e Perito Judicial",
          "honorificPrefix": "Eng.",
          "knowsAbout": ["Engenharia Diagnóstica", "Perícia Mecânica", "Análise de Vibração"],
          "identifier": {
             "@type": "PropertyValue",
             "name": "CREA-GO",
             "value": "1018779540D-GO"
          },
          "sameAs": "https://www.linkedin.com/in/georgiolima/"
        }'''
            content = content.replace(old_founder.group(0), new_founder)
            with open(f, 'w', encoding='utf-8') as file:
                file.write(content)
            count += 1
            print(f"Updated founder in {f}")

print(f"Total files updated: {count}")
