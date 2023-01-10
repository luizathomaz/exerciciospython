print('   GERADOR DE PA   ')
print('='*20)
pri = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
print(pri, end=' - ')
n = 1
mais = 1
for i in range(0, 9):
    pri += razao
    print(f'{pri}', end=' - ')
print('PAUSA')
while mais != 0:
    mais = int(input('\nQuantos termos você quer mostrar a mais? '))
    for n in range(1, mais+1):
        pri += razao
        n += 1
        print(f'{pri}', end=' - ')
    print('PAUSA')
    if mais == 0:
        print('FIM')

# O que o professor fez:
'''print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont<= total:
        print('{} -'.format(termo), end='')
        termo += razao
        cont += 1
        print('PAUSA')
        mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados'.format(total))
print('FIM')
'''