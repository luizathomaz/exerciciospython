import random
from time import sleep
num = random.randint(0, 5) #O número que o computador vai gerar
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('--' * 28)
sleep(2)
chance = int(input('Em que número eu pensei? ')) #o número do jogador
print('PROCESSANDO...')
sleep(3)
if num == chance:
    print('Parabéns! O núemero que eu estava pensando também era {}!'.format(chance))
else:
    print(f'GANHEI! Eu pensei no número {num} e não no {chance}!')
