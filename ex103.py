def ficha(nome=0, gols=0):
    if nome and gols:
        print(f'O jogador {nome} fez {gols} gols no campeonato.')
    elif gols:
        print(f'O jogador <desconhecido> fez {gols} gols no campeonato.')
    elif nome:
        print(f'O jogador {nome} fez 0 gols no campeonato. ')
    else:
        print(f'O jogador <desconhecido> fez 0 gols no campeonato. ')


ficha(str(input('Digite o nome do jogador: ')), str(input('Digite o número de gols: ')))
