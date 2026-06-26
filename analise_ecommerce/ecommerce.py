import pandas as pd
df = pd.read_csv('ecommerce_orders_dataset.csv') # Substitua 'ecommerce_data.csv' pelo caminho do seu arquivo CSV
print(df.head()) # Isso vai te mostrar as primeiras 5 linhas

# 1. Verifica valores nulos
print("Dados faltantes:")
print(df.isnull().sum())

# 2. Verifica tipos das colunas
print("\nTipos de dados:")
print(df.dtypes)

# 3. Verifica duplicatas
print("\nQuantidade de duplicatas:")
print(df.duplicated().sum())

# Ver o resumo estatístico (média, valor máximo, etc.)
print(df['Profit_Amount'].describe())

# Ver quantos pedidos foram de 'High_Value_Order' (Sim ou Não)
print(df['High_Value_Order'].value_counts())

# Agrupa por Season e conta os valores da coluna High_Value_Order
analise_estacional = df.groupby('Season')['High_Value_Order'].value_counts()
print(analise_estacional)

lucro_medio = df.groupby('High_Value_Order')['Profit_Amount'].mean()
print(lucro_medio)

top_clientes = df.groupby('Customer_ID')['Profit_Amount'].sum().sort_values(ascending=False).head(5)
print(top_clientes)

# Conta quantas vezes cada produto aparece no dataset e mostra os 10 mais vendidos
mais_vendidos = df['Product_Subcategory'].value_counts().head(10)
print(mais_vendidos)

# Conta quantas vezes cada categoria aparece
contagem_produtos = df['Product_Subcategory'].value_counts()

# Pega os 10 últimos (os que menos aparecem)
piores_vendidos = contagem_produtos.tail(10)

print(piores_vendidos)

import sqlite3

# 1. Cria a conexão com o banco (ele cria o arquivo .db se não existir)
conn = sqlite3.connect('ecommerce.db')

# 2. Envia o seu dataframe para o banco como uma tabela chamada 'vendas'
df.to_sql('vendas', conn, if_exists='replace', index=False)

# 3. Agora você pode fazer consultas SQL no seu arquivo!
cursor = conn.cursor()
query = "SELECT Country, SUM(Profit_Amount) as Total_Lucro FROM vendas GROUP BY Country ORDER BY Total_Lucro DESC"
cursor.execute(query)

# Exibe os resultados
for linha in cursor.fetchall():
    print(linha)

conn.close()