lista = []
pares = []
impares = []
for c in range(0, 7):
    lista.append(int(input(f'Digite o {c+1}º valor: ')))
    if lista[0] % 2 == 0:
        pares.append(lista[:])
    else:
        impares.append(lista[:])
    lista.clear()
print('=-'*30)
print(f'Os valores pares digitados foram: {sorted(pares)}')
print(f'OS valores ímpares digitados foram: {sorted(impares)}')

#como o professor fez:
'''núm = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        núm[0].append(valor)
    else:
        núm[1].append(valor)
print('=-'*30)
print(f'OS valores pares foram: {sorted(núm[0])}')
print(f'OS valores impares foram: {sorted(núm[1])}')'''
