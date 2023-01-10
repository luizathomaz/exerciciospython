soma = maisde1000 = maisbarato = 0
nomebarato = ''
cont = 1
continuar = ''
print('-'*30)
print('LOJA SUPER BARATÃO')
print('-'*30)
while True:
    nome = str(input('Nome do produto: '))
    valor = float(input('Preço: R$ '))
    soma += valor
    cont += 1
    if valor > 1000:
        maisde1000 +=1
    if cont == 1:
        maisbarato = valor
        nomebarato = nome
    if valor < maisbarato:
        maisbarato = valor
        nomebarato = nome
    continuar = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
    while continuar not in 'sn':
        continuar = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
    if 'n' in continuar:
        print('----- FIM DO PROGRAMA -----')
        break
print(f'O total da compra foi R$ {soma:.2f}')
print(f'Temos {maisde1000} procutos custando mais de R$1000.00')
print(f'O produto mais barato foi {nomebarato} que custa R$ {maisbarato:.2f}')
