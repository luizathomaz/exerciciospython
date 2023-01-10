from random import randint
cont = jogador = 0
resultado = []
print('=-'*15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 15)
while True:
    jogador = int(input('Diga um valor: '))
    qual = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    computador = randint(0, 10)
    total = jogador + computador
    if total % 2 == 0:
        resultado = 'P'
        print('-'*30)
        print(f'Você jogou {jogador} e o computador {computador}. Total de {total} DEU PAR')
        print('-'*30)
    else:
        resultado = 'I'
        print('-' * 30)
        print(f'Você jogou {jogador} e o computador {computador}. Total de {total} DEU ÍMPAR')
        print('-' * 30)
    if qual == resultado:
        cont += 1
        print('Você venceu!')
        print('Vamos jogar novamente')
        print('=-'*15)
    else:
        break
print('Você perdeu!')
print('=-'*15)
print(f'GAME OVER! Você venceu {cont} vezes.')
