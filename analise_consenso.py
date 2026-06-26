import pandas as pd

# Carrega os dados coletados da mineração
df = pd.read_csv('base_recomendacoes_ceos.csv')

# Identifica livros que aparecem em mais de uma lista de recomendação
consenso_livros = df[df.duplicated(subset=['titulo'], keep=False)]

# Exibe a contagem de recomendações para cada livro do consenso
resumo = consenso_livros['titulo'].value_counts()

print("--- Livros com maior consenso entre os líderes ---")
print(resumo.head(10))

# Salva o resultado do consenso em um arquivo consolidado
consenso_livros.to_csv('livros_ouro_consenso.csv', index=False)

print(f"Total de livros minerados na base bruta: {len(df)}")
print(f"Total de livros únicos encontrados: {df['titulo'].nunique()}")

# Lista dos títulos identificados como consenso para detalhamento
titulos_consenso = ["The Moment of Lift: How Empowering Women Changes the World", 
                    "Principles for Success", 
                    "Tools and Weapons: The Promise and the Peril of the Digital Age",
                    "The New Digital Age: Transforming Nations, Businesses, and Our Lives",
                    "In the Shadow of Statues: A White Southerner Confronts History"]

# Agrupa títulos e lista os respectivos recomendadores
detalhes_consenso = df[df['titulo'].isin(titulos_consenso)].groupby('titulo')['recomendado_por'].apply(list)

print("--- Quem recomendou o quê? ---")
print(detalhes_consenso)

# Calcula e exibe o escopo do estudo com base nos recomendadores únicos
total_recomendadores = df['recomendado_por'].nunique()
lista_recomendadores = df['recomendado_por'].unique()

print(f"\n--- Escopo do Estudo ---")
print(f"Total de bibliotecas pessoais analisadas: {total_recomendadores}")
print("Recomendadores incluídos:")
for nome in lista_recomendadores:
    print(f"- {nome}")