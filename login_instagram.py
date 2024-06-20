
LOGIN_CORRETO = 'laryssa'
SENHA_CORRETA = '123'

isLogged = False
limite_tentativas = 3
tentativas_login = 0

if (not isLogged):
    
    while True:
        login = input("\nDigite seu username / email / phone number\n").lower()
        senha = input("Digite sua senha: ")
        print()

        tentativas_login += 1

        if ((login == LOGIN_CORRETO) and (senha == SENHA_CORRETA)):
            print('Voce logou')
            isLogged = True
            break
        else:
            print('Credenciais inválidas')
            if tentativas_login == limite_tentativas:
                print("\nLimite de tentativas excedido\n")
                break

        print(f"\nTentativas restantes 0{limite_tentativas - tentativas_login}\n")

if (isLogged):
    print('---feed---')
