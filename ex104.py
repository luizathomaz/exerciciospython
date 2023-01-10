def leiaInt(a):
    while True:
        a = input('Digite um número:')
        if a.isnumeric():
            return a
            break
        else:
            print('\033[0;31mERRO! Por favor digite um número.\033[m')
        

#programa principal:
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
