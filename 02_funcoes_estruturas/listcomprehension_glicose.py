glicemia = [129, 82, 60, 97, 101, 65, 62, 167, 87, 53, 58, 92, 66, 120, 109, 62, 86, 96, 103, 88, 155, 52, 89, 73]

def classificar_glicemia(valor):
    if valor <= 70:
        return 'Hipoglicemia'
    elif 70 < valor <= 99:
        return 'Glicose Normal'
    elif 99 < valor <= 125:
        return 'Glicose Alterada'
    else:
        return 'Glicose Diabetes'

# Aqui usamos list comprehension para criar a lista de tuplas de uma vez
lista_classificada = [(valor, classificar_glicemia(valor)) for valor in glicemia]

print(lista_classificada)