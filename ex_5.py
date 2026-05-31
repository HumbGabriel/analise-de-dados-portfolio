num = int(input('Digite um número qualquer: '))
lista_primos = []
for i in range(1,num):
    if i % 2 != 0:
        lista_primos.append(i)  
print(f'Lista de números primos entre 1 e {num} = {lista_primos} ')

