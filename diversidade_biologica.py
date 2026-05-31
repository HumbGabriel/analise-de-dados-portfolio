dados = {
    'Área Norte': [2819, 7236],
    'Área Leste': [1440, 9492],
    'Área Sul': [5969, 7496],
    'Área Oeste': [14446, 49688],
    'Área Centro': [22558, 45148]
}

# Criamos um dicionário para guardar as somas totais de cada área
diversidade_total = {}

for area, especies in dados.items():
    # 'especies' é a lista [plantas, animais]
    soma = sum(especies) 
    media = soma / len(especies)
    
    # Guardamos a soma para identificar o vencedor depois
    diversidade_total[area] = soma
    
    print(f"A média de espécies na {area} é: {media}")

# Identificando a maior diversidade usando o que aprendemos no exercício anterior
vencedor = max(diversidade_total, key=diversidade_total.get)
print(f"\nA área com maior diversidade biológica é a {vencedor} com {diversidade_total[vencedor]} espécies.")