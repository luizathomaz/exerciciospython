pessoas = list()
dados = []
maior = menor = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    resp = input('Deseja adicionar outra pessoa? [S/N] ')
    if resp in 'Nn':
        break
print('=-'*30)
print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'As pessoas mais velhas tem {maior} anos. São elas: ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}]', end='')
print()
print(f'As pessoas mais novas tem {menor} anos. São elas: ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}]', end='')
