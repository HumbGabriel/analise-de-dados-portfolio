#Primeiro eu crio a variável que armazena a lista
lista_bacterias = [1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9]
#Crio uma variável de lista inicialmente vazia, para armazenar o crescimento percetual
lista_crescimento =[]
#Crio uma estrutura de repetição que irá calcular o crescimento percentual e adicionar os novos elementos na lista vazia.
for i in range(1, len(lista_bacterias)):
    amostra_atual = lista_bacterias[i]
    amostra_passada = lista_bacterias[i-1]
    
    # Agora a conta faz sentido
    crescimento = 100 * (amostra_atual - amostra_passada) / amostra_passada
    lista_crescimento.append(crescimento)
for porcentagem in lista_crescimento:
    print(f'Crescimento: {porcentagem:.2f}%')