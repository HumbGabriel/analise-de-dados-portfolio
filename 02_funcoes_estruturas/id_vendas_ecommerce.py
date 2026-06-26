id_vendas = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
quantidade = [15, 12, 1, 15, 2, 11, 2, 12, 2, 4]
preco = [93.0, 102.0, 18.0, 41.0, 122.0, 14.0, 71.0, 48.0, 14.0, 144.0]


cabeçalho = [("ID | Quantidade | Preço | Total")]
tabela = [(i, q, p, q * p) for i, q, p in zip(id_vendas, quantidade, preco)]
print(cabeçalho + tabela)

soma_total = sum(item[3] for item in tabela)
print(f"Valor total das vendas: {soma_total}")