idades = {'Setor A': [22, 26, 30, 30, 35, 38, 40, 56, 57, 65],
 'Setor B': [22, 24, 26, 33, 41, 49, 50, 54, 60, 64],
 'Setor C': [23, 26, 26, 29, 34, 35, 36, 41, 52, 56],
 'Setor D': [19, 20, 25, 27, 34, 39, 42, 44, 50, 65]}

todas_idades = []

for setores, lista in idades.items():
    media_setor = sum(lista) / len(lista)
    print(f'Média do {setores}: {media_setor}')

    todas_idades.extend(lista)

media_geral = sum(todas_idades) / len(todas_idades)
print(f"\nA média geral da empresa é: {media_geral:.2f}")

acima_da_media = 0
for idade in todas_idades:
    if idade > media_geral:
        acima_da_media += 1

print(f"Quantidade de pessoas acima da média geral: {acima_da_media}")