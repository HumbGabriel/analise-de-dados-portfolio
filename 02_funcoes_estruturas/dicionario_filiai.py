estados = ['SP', 'ES', 'MG', 'MG', 'SP', 'MG', 'ES', 'ES', 'ES', 'SP', 'SP', 'MG', 'ES', 'SP', 'RJ', 'MG', 'RJ', 'SP', 'MG', 'SP', 'ES', 'SP', 'MG']
funcionarios = [('SP', 16), ('ES', 8), ('MG', 9), ('MG', 6), ('SP', 10), ('MG', 4), ('ES',9), ('ES', 7), ('ES', 12), ('SP', 7), ('SP', 11), ('MG',8), ('ES',8), ('SP',9), ('RJ', 13), ('MG', 5), ('RJ', 9), ('SP', 12), ('MG', 10), ('SP', 7), ('ES', 14), ('SP', 10), ('MG', 12)]
dicionario_estados = {estado: estados.count(estado) for estado in set(estados)}
dicionario_soma_funcionarios = {estado: sum(funcionario[1] for funcionario in funcionarios if funcionario[0] == estado) for estado in set(estados)}
dicionario_funcionarios = {estado: [funcionario[1] for funcionario in funcionarios if funcionario[0] == estado] for estado in set(estados)}
print(dicionario_estados)
print(dicionario_soma_funcionarios)
print(dicionario_funcionarios)  