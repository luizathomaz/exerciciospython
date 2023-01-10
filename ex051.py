print('='*25)
print('   10 TERMOS DE UMA PA   ')
print('='*25)
pri = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
print(pri)
for i in range(0, 9):
    pri += razao
    print(f'{pri}', end=' - ')
print('ACABOU')
