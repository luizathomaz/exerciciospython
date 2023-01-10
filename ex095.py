time = list()
while True:
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
    time.append(jogador.copy())
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break

print('-=' * 20)
for i, v in enumerate(time):
    print(f'{i:>4} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-=' * 20)

while True:
    opc = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if opc == 999:
        break
    if opc <= (len(time)):
        print(f'Levantamento do jogador {time[opc]["nome"]}')
        for i, g in enumerate(time[opc]['gols']):
            print(f'  No jogo {i+1} tem {g} gols')

print('Volte sempre!')
