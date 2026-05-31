dados_vendas = {'Produto A': 300, 'Produto B': 80, 'Produto C': 60,
 'Produto D': 200, 'Produto E': 250, 'Produto F': 30}

lista_vendas = list(dados_vendas.values()) # Transforma em lista real
lista_vendas.sort(reverse=True)            # Ordena do maior para o menor
lista_produtos = list(dados_vendas.keys())
lista_produtos.sort()
print(lista_vendas)
soma = sum(lista_vendas)


mais_vendido = max(dados_vendas, key=dados_vendas.get)


print(f'O total de vendas foi: {soma} e o produto mais vendido foi: {mais_vendido} ')