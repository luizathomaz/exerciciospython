num = int(input('Digite um número inteiro: '))
print('''Escolha uma desses para a conversão: 
[1] converter para BINÁRIO 
[2] converter para OCTAL 
[3] converter para HEXADECIMAL''')
opção = int(input('Opção escolhida: '))
if opção == 1:
    print('{} convertido para binário é igual a {}.'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} convertido para octal é igual a {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para hexadecimal é igual a {}.'.format(num, hex(num)[2:]))
else:
    print('Opção inválida.')
