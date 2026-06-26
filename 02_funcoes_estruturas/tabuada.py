numero = int(input("De qual número você gostaria de saber a tabuada?"))
multiplicador = 0
print(f'Tabuada do {numero}:')
# O range(0, 11) vai de 0 até 10 (o 11 fica de fora)
for multiplicador in range(0, 11):
    multiplicacao = numero*multiplicador   
    print(f'{numero} * {multiplicador} = {multiplicacao}')
    multiplicador += 1
    
