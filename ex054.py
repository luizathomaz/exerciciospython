from datetime import date
hoje = date.today().year
print(hoje)
totalmaior = 0
totalmenor = 0
for pessoa in range(1, 8):
    ano = int(input('Em que ano a {}° pessoa nasceu? '.format(pessoa)))
    if hoje - ano >= 21:
        totalmaior += 1
    else:
        totalmenor += 1
print('Ao todos tivemos {} pessoas maiores de idade'.format(totalmaior))
print(f'Ao todos tivemos {totalmenor} pessoas menores de idade')

'''for c in range(pessoa):
    if hoje - ano >= 18:

        print('A pessoa {} é menor de idade'.format(pessoa))
    elif hoje - ano >= 18:
        print('A pessoa {} é maior de idade'.format(pessoa))'''
