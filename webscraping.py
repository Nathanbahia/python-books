import json
import requests
from bs4 import BeautifulSoup as BS


page = requests.get("https://lista.mercadolivre.com.br/livro-de-python#D[A:livro%20de%20python]")
sopa = BS(page.content, 'html.parser')

livros = sopa.select("h2.ui-search-item__title")
imagens = sopa.select("img.ui-search-result-image__element")

conteudo = []

for i in range(len(livros)):
    conteudo.append(
        {
            'livro': livros[i].text,
            'imagem': imagens[i]['data-src']
        }
    )

with open('conteudo.json', 'w', encoding='utf-8') as json_file:
    json.dump(conteudo, json_file, indent=4, ensure_ascii=False)