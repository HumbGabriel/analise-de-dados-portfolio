# Lista de dicionários representando o mercado
mercado = [
    {"produto": "Curso Básico", "preco": 50, "conversao": 0.8},
    {"produto": "Consultoria Premium", "preco": 2000, "conversao": 0.05},
    {"produto": "E-book", "preco": 30, "conversao": 0.9},
    {"produto": "Mentoria Grupo", "preco": 500, "conversao": 0.2}
]

viaveis = []
for i in mercado:
    if i['preco'] < 600 and i['conversao'] > 0.1:
        viaveis.append(i['produto'])
print(viaveis)
