import requests
from bs4 import BeautifulSoup
import pandas as pd

urls = [
    "https://theceolibrary.com/books-recommended-by/tony-robbins",
    "https://theceolibrary.com/books-recommended-by/walter-isaacson",
    "https://theceolibrary.com/books-recommended-by/naval-ravikant",
    "https://theceolibrary.com/books-recommended-by/barack-obama",
    "https://theceolibrary.com/books-recommended-by/bill-gates",
    "https://theceolibrary.com/books-recommended-by/elon-musk",
    "https://theceolibrary.com/books-recommended-by/jeff-bezos",
    "https://theceolibrary.com/books-recommended-by/warren-buffett",
    "https://theceolibrary.com/books-recommended-by/the-ceo-library-community-through-anonymous-form",
    "https://theceolibrary.com/books-recommended-by/ryan-holiday"
]

headers = {'User-Agent': 'Mozilla/5.0'}
todos_livros = []

for url in urls:
    nome_recomendador = url.split('/')[-1].replace('-', ' ').title()
    print(f"Minerando: {nome_recomendador}...")
    
    resposta = requests.get(url, headers=headers)
    soup = BeautifulSoup(resposta.text, 'html.parser')
    
    # No The CEO Library, os títulos geralmente estão dentro de links ou tags h
    # Vamos buscar os containers que costumam agrupar os livros
    containers = soup.find_all(['h2', 'h3']) 
    
    for item in containers:
        titulo = item.get_text(strip=True)
        # Filtro básico: se o título não for vazio e for longo o suficiente para ser um livro
        if len(titulo) > 5:
            todos_livros.append({
                'titulo': titulo,
                'recomendado_por': nome_recomendador
            })

# Exportar para CSV
df = pd.DataFrame(todos_livros)
df.to_csv('base_recomendacoes_ceos.csv', index=False)
print("Mineração concluída! Arquivo 'base_recomendacoes_ceos.csv' gerado.")