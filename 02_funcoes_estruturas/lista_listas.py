nomes = [('João', 'J720'), ('Maria', 'M205'), ('José', 'J371'), ('Cláudia', 'C546'), ('Ana', 'A347')]
notas = [[8.0, 9.0, 10.0], [9.0, 7.0, 6.0], [3.4, 7.0, 7.0], [5.5, 6.6, 8.0], [6.0, 10.0, 9.5]]
medias = [9.0, 7.3, 5.8, 6.7, 8.5]

lista_nomes = [item[0] for item in nomes]
lista_codigos = [item[1] for item in nomes]
lista_medias = [media for media in medias]
lista_situacao = ['Aprovado' if media >= 6 else 'Reprovado' for media in medias]
lista_notas = [nota for nota in notas]
lista_listas = list(zip(lista_nomes, lista_codigos, notas, medias, lista_situacao))
lista_listas

