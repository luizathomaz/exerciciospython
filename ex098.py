from time import sleep


def linha():
    print('-=' * 20)


def cont(i, f, c):
    linha()
    print(f'Contagem de {i} até {f} de {c} em {c}: ')
    sleep(2)
    if c == 0 or c < 0:
        print('ERRO')
    if f > i:
        for d in range(i, f+1, c):
            print(d, end=' ')
            sleep(0.5)
        print('FIM!')
        print()
    elif i > f:
        for d in range(i, f-1, -c):
            print(d, end=' ')
            sleep(0.5)
        print('FIM!')
        print()


cont(1, 10, 1)
cont(10, 0, 2)
linha()
print('Agora é sua vez de personalizar a contagem!')
cont(int(input('Início: ')), int(input('Fim: ')), int(input('Passo: ')))

