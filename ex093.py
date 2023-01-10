jogador = {'nome': str(input('Nome do jogador: ')),
           'gols': '',
           'total': ''
           }
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
tot = 0
golsp = []
while tot < partidas:
    golsp.append(int(input(f'   Quantos gols na partida {tot +1}? ')))
    tot += 1
jogador['gols'] = golsp[:]
jogador['total'] = sum(jogador['gols'])
print('-=' * 20)
print(jogador)
print('-=' * 20)
for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}')
print('-=' * 20)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas. ')
for i in range(0, partidas):
    print(f' --> Na partida {i+1}, fez {golsp[i]} gols.')
print(f'Foi um total de {jogador["total"]} gols no campeonato.')
