lista = []
listapares = []
listaimpares = []
while True:
    a = lista.append(int(input('Digite um número: ')))
    resposta = input('Quer continuar? [S/N] ')
    if resposta in 'Nn':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        listapares.append(v)
    else:
        listaimpares.append(v)
print('=-'*30)
print(f'A lista completa é {lista}')
print(f'Os números pares são: {listapares}')
print(f'Os números impares são: {listaimpares}')
