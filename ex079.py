lista = []
print('Para parar de digitar números escreva "999". ')
while True:
    lista.append(int(input('Digite um número: ')))
    if 999 in lista:
        break
lista.remove(999)
lista.sort()
listafinal = []
for i in lista:
    if i not in listafinal:
        listafinal.append(i)
print(f'A lista em ordem crescente sem valores repitidos é {listafinal}')
# como o professor fez:
'''numeros = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Número adicionado com sucesso!')
    else: 
        print('Valor duplicado! Não vou adicionar...')
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
numeros.sort()
print('=' *30)
print(f'Você digitou os valores: {numeros}') '''
