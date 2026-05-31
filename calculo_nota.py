respostas = []
gabarito = ['D', 'A', 'C', 'B', 'A', 'D', 'C', 'C', 'A', 'B']

for i in range(10):
    resposta = input(f'Digite a {i+1}ª resposta: ').upper() 
    respostas.append(resposta)

nota = 0

for i in range(len(respostas)):
    if respostas[i] == gabarito[i]:
        nota += 1

print(f'Nota final do aluno: {nota}')