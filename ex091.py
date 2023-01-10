from random import randint

rodada = {'jogador1': randint(1, 6),
          'jogador2': randint(1, 6),
          'jogador3': randint(1, 6),
          'jogador4': randint(1, 6)
          }
for k, v in rodada.items():
    print(f'{k} tirou {v} no dado.')
print('-=' * 15)
print(f'{"RANKING DOS JOGADORES":^15}')


def value_getter(item):
    return item[1]


print(sorted(rodada.items(), key=value_getter, reverse=True, ))

#como o professor fez:
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1, 6),
          'jogador2': randint(1, 6),
          'jogador3': randint(1, 6),
          'jogador4': randint(1, 6)
          }
ranking = list()
print('Valores sorteados: ')
for k, v in jogo.items():
    print(f'{k} tiou {v} no dado')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')
    sleep(1)
