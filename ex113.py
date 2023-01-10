def leiaInt(mensagem):
    while True:
        try: 
            a = int(input(mensagem))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Por favor digite um número inteiro válido.\033[m')
        except KeyboardInterrupt:
            print('Entrada de dados interrompida pelo usuário.')
            break
        else:
            return a


def leiaFloat(mensagem):
    while True:
        try: 
            a = float(input(mensagem))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Por favor digite um número real válido.\033[m')
        except KeyboardInterrupt:
            print('Entrada de dados interrompida pelo usuário.')
            break
        else:
            return a


#programa principal:
i = leiaInt('Digite um número inteiro: ')
r = leiaFloat('Digite um número real: ')

print(f'O número inteiro digitado foi {i} e o real foi {r}')
