gastos = [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]
quantidade = len(gastos)
print(f"A quantidade de itens é: {quantidade}")
soma = sum(gastos)
media = soma / quantidade
compras_caras = []
print(f'A média de gastos da empresa é :{media:.2f}')

for elemento in gastos:
    if elemento > 3000.00:
        compras_caras.append(elemento)
        quantidade_maior_3k = len(compras_caras)

porcentagem = (quantidade_maior_3k/quantidade)*100
      
print(f'Houveram {quantidade_maior_3k} compras acima de R$3000. A porcentagem em relação ao total de compras foi de: {porcentagem} ')


