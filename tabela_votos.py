tabela_votos = {'Design 1' : 1334 , 
                'Design 2' : 982, 'Design 3' : 1751,
                'Design 4' : 210,'Design 5' : 1811 }

vencedor = max(tabela_votos, key=tabela_votos.get)
votos = list(tabela_votos.values())
soma = sum(votos)
media = (tabela_votos[vencedor] / soma) * 100
print(f'O design vencedor foi: {vencedor} com {media:.2f}% dos votos;')

#eu preciso dar um jeito de "chamar " o valor da chave vencedora.