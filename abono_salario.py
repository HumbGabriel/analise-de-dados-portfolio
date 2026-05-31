salarios = [1172, 1644, 2617, 5130, 5532, 6341, 6650, 7238, 7685, 7782, 7903]
dicionario_abonos = {}
contagem_minimo = 0

for s in salarios:
    abono = s * 0.10
    
    # Verificação do abono mínimo
    if abono < 200:
        abono = 200
        contagem_minimo += 1
    
    # Transformando em chave (salário) e valor (abono)
    dicionario_abonos[s] = abono

# Cálculos para o Financeiro
total_gastos = sum(dicionario_abonos.values())
maior_abono = max(dicionario_abonos.values())

print(f"Total de gastos com abono: R$ {total_gastos:.2f}")
print(f"Quantidade de colaboradores que receberam o mínimo (R$ 200): {contagem_minimo}")
print(f"O maior valor de abono concedido foi: R$ {maior_abono:.2f}")