"""
Sistema de raspagem de dados nas lojas: Mercado Livre, Submarino e Amazon em
busca de análise de preços dos livros de Python cujo código ISBN constam no
site https://servicos.cbl.org.br/
"""

import json
import requests
from bs4 import BeautifulSoup as BS


# MERCADO LIVRE

urls_mercado_livre = [
    'https://lista.mercadolivre.com.br/livros-de-python#D[A:livros%20de%20python]',
    'https://livros.mercadolivre.com.br/livros/livros-de-python_Desde_49',
    'https://livros.mercadolivre.com.br/livros/livros-de-python_Desde_97',
]

responses_mercado_livre = []
[ responses_mercado_livre.append(requests.get(url)) for url in urls_mercado_livre ]


info_mercado_livre = {
    'livros': [],
    'precos': [],
    'imagens': [],
    'link': []
}

for resp in responses_mercado_livre:
    soup_merc = BS(resp.content, 'html.parser')
    info_mercado_livre['livros'] += soup_merc.select("h2.ui-search-item__title.ui-search-item__group__element")
    info_mercado_livre['precos'] += soup_merc.select("div.ui-search-price.ui-search-price--size-medium.ui-search-item__group__element")
    info_mercado_livre['imagens'] += soup_merc.select("img.ui-search-result-image__element")
    info_mercado_livre['link'] += soup_merc.select("a.ui-search-result__content.ui-search-link") 


json_mercado_livre = []
for l in range(len(info_mercado_livre['livros'])):
    json_mercado_livre.append({
        'livro': info_mercado_livre['livros'][l].text,
        'preco': info_mercado_livre['precos'][l].text,
        'imagem': info_mercado_livre['imagens'][l]['data-src'],    
        'link': info_mercado_livre['link'][l]['href'],
        'loja': 'Mercado Livre'
    })

        
with open('conteudo.json', 'w', encoding="utf-8") as json_file:
    json.dump(json_mercado_livre, json_file, ensure_ascii=False)

print("JSON Mercado Livre criado com sucesso!")


# AMAZON


# SUBMARINO
