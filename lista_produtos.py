lista_doces = []
lista_amargos = []
for i in range(10):
    ID = int(input(f'Digite o {i+1}º ID: '))
    if ID % 2 == 0:
        lista_doces.append(ID)
    else:
        lista_amargos.append(ID)
quantidade_doces = len(lista_doces)
quantidade_amargos = len(lista_amargos)

print(f'Quantidade de produtos doces: {quantidade_doces} \nQuantidade de produtos amargos: {quantidade_amargos}')
