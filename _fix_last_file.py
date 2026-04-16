import re

fp = 'artigos/playgrounds/artigo-playground-todo-contato-manual-deve-ter-acabamento-atoxico-preservado.html'

with open(fp, 'r', encoding='utf-8') as f:
    text = f.read()

text = re.sub(
    r'<title>.*?</title>',
    '<title>Acabamento Atóxico em Contato Manual no Playground</title>',
    text,
    flags=re.IGNORECASE|re.DOTALL
)

text = re.sub(
    r'<meta\s+name=\"description\"\s+content=\"[^\"]+\">',
    '<meta name=\"description\" content=\"Entenda a exigência da Norma ABNT NBR 16071 sobre acabamento atóxico em locais de contato manual nos playgrounds e evite riscos químicos.\">',
    text,
    flags=re.IGNORECASE|re.DOTALL
)

with open(fp, 'w', encoding='utf-8') as f:
    f.write(text)
