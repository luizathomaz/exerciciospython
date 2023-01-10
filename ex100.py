from random import randint
lista = []
pares = []


def linha():
    print('-=' * 25)


def sorteia():
    cont = 1
    while cont <= 5:
        lista.append(randint(0, 10))
        cont += 1
    linha()
    print(f'Os números sorteados foram: {lista}')


def somaPar():
    for n in lista:
        if n % 2 == 0:
            pares.append(n)
    soma = sum(pares)
    linha()
    print(f'A soma dos números pares foi {soma}')
    linha()


sorteia()
somaPar()
