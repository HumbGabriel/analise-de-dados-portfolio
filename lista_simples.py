lista = []
for i in range(5):
    num = int(input(f'Digite o {i+1}º número: '))
    lista.append(num)

lista.reverse()

print(f'A listá de números coletados é: {lista}')