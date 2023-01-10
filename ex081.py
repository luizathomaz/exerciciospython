lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    a = input('Quer continuar? [S/N] ')
    if a in 'Nn':
        break
print('=-'*30)
print(f'Você digitou {len(lista)} elementos. ')
print(f'Os valores em ordem decrescente são {sorted(lista, reverse=True)}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')
print(lista)
