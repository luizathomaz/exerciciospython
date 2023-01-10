print('='*25)
print('   10 TERMOS DE UMA PA   ')
print('='*25)
pri = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
n = 1
print(pri, end=' - ')
while n < 10:
    pri += razao
    n += 1
    print(f'{pri}', end=' - ')
print('ACABOU')
