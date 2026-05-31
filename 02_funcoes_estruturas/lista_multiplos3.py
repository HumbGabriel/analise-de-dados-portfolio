# 1. Definimos a função que recebe uma lista como parâmetro
def achar_multiplos_3(lista_numeros):
    multiplos_3 = []
    
    for i in lista_numeros:
        if i % 3 == 0:
            multiplos_3.append(i)
            
    # O return vai aqui, DEVOLVENDO a lista para quem chamou a função
    return multiplos_3

# --- Fora da função: o fluxo principal do programa ---

lista_original = [97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]

# 2. Chamamos a função passando a lista e salvando o retorno na variável exigida
mult_3 = achar_multiplos_3(lista_original)

# 3. Agora você pode dar um print para conferir o resultado na tela
print(mult_3)