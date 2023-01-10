import random
print('Vou pensar em um número, tente acertar! ')
comp = random.randint(0, 10)
jogador = []
palpite = 0
while jogador != comp:
    jogador = int(input('Digite um número de 0 a 10: '))
    #if jogador != comp:
    palpite += 1
if palpite == 1:
    print(f'Você acertou de primeira, parabéns! ')
elif palpite > 1:
    print('Você acertou! Infelizmente você precisou de {} palpites.'.format(palpite))
