import glob, re
html_files = glob.glob('**/*.html', recursive=True)
bad_canonicals = []
for f in html_files:
    if 'old\\' in f or 'v2-staging\\' in f or 'player\\' in f: continue
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
        match = re.search(r'<link rel="canonical" href="([^"]+)">', content)
        if match:
            canonical_url = match.group(1)
            path_part = f.replace('\\', '/')
            if path_part.endswith('index.html'):
               expected_canonical = 'https://www.protoncd.com.br/' + path_part.replace('index.html', '')
            else:
               expected_canonical = 'https://www.protoncd.com.br/' + path_part
            if canonical_url != expected_canonical:
                content = content.replace(f'<link rel="canonical" href="{canonical_url}">', f'<link rel="canonical" href="{expected_canonical}">')
                with open(f, 'w', encoding='utf-8') as fh:
                    fh.write(content)
                print(f'Fixed canonical for {f}')
