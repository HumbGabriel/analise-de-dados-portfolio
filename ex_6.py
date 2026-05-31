dia = int(input('Digite o dia do seu nascimento:'))
mes = int(input('Digite o mês do seu nascimento:'))
ano = int(input('Digite o ano do seu nascimento:'))


valida = False

if 1 <= mes <= 12:
    if mes in [1, 3, 5, 7, 8, 10, 12]: # Meses de 31
        if 1 <= dia <= 31:
            valida = True
    elif mes in [4, 6, 9, 11]: # Meses de 30
        if 1 <= dia <= 30:
            valida = True
    elif mes == 2: # Fevereiro
        # Lógica simplificada de bissexto:
        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
            if 1 <= dia <= 29:
                valida = True
        elif 1 <= dia <= 28:
            valida = True

if valida:
    print("Data válida para análise.")
else:
    print("Data inválida.")