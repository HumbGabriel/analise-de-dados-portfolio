while True:
    usuario = input('Digite seu nome de usuário: ')
    senha = input('Digite sua senha: ')  # Sem o int(), entra como texto!

    # Verifica a primeira regra
    if len(usuario) < 5:
        print('O nome de usuário deve ter pelo menos 5 caracteres.')
    
    # Verifica a segunda regra
    elif len(senha) < 8:
        print('A senha deve ter pelo menos 8 caracteres.')
    
    # Se passou pelas duas validações, o cadastro deu certo!
    else:
        print('Cadastro realizado com sucesso!')
        break  # Esse break quebra o "while True" e finaliza o programa