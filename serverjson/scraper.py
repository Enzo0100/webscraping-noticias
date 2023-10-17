import requests
import json
from bs4 import BeautifulSoup

resposta = requests.get("https://www.infomoney.com.br/ultimas-noticias/")  # Substitua "URL_DO_SITE" pela URL que deseja analisar
conteudo = resposta.content

site = BeautifulSoup(conteudo, "html.parser")

noticias = site.find_all('div', id=lambda x: x and x.startswith('post-'))

# for noticia in noticias:
#     link = noticia.find('a')  # Encontra a primeira tag <a> dentro da div
#     if link:
#         title = link.get('title')  # Obtém o atributo 'title' da tag <a>
#         href = link.get('href')    # Obtém o atributo 'href' da tag <a>
#         print(f"Title: {title}, Link: {href}")


resultados = []

for noticia in noticias:
    link = noticia.find('a')
    data_elemento = noticia.find('span', class_='posted-diff')  # Procura pelo elemento com a classe "posted-diff"
    
    if link and data_elemento:
        title = link.get('title')
        href = link.get('href')
        data = data_elemento.text.strip()  # Obtém o texto associado ao elemento e remove espaços desnecessários
        resultados.append({"title": title, "link": href, "data": data})

print(json.dumps(resultados))