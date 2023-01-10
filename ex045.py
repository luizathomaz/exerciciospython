from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
comp = randint(0 , 2)
print('''Suas opções: 
[ 0 ] PEDRA
[ 1 ] PAPEL 
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('Computador jogou {}'.format(itens[comp]))
print('Jogador jogou {}'.format(itens[jogador]))
if jogador == 0 and comp == 2 or jogador == 1 and comp == 0 or jogador == 2 and comp == 1:
    print('PARABÉNS! Você ganhou da máquina! ')
elif jogador == comp:
    print('Empate')
else:
    print('Você perdeu. ')
