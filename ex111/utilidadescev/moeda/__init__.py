def moeda(p = 0, m = "R$"):
    """
    Programa para manipular dados monetários, dobrando valores, calculando taxa
    de aumento e redução e metade.
    :param p: preço
    :param m: moeda, caso não informada se utiliza o Real R$
    :param v: valor, mesmo do preço
    :param n: taxa
    """
    return (f'{m}{p:.2f}').replace('.', ',')


def aumentar(v, n):
    f = (v * (n/100)) + v
    return moeda(f) 


def diminuir(v, n):
    f = v - (v * n/100)
    return moeda(f)


def dobro(v):
    res = v * 2
    return moeda(res)


def metade(v):
    res = v / 2
    return moeda(res)


def linha():
    print('-'*30)


def resumo(preço=0, taxaa=10, taxad=5):
    linha()
    print(f'RESUMO DO VALOR'.center(30))
    linha()
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço)}')
    print(f'Metade do preço: \t{metade(preço)}')
    print(f'Com {taxaa}% de aumento: \t{aumentar(preço, taxaa)}')
    print(f'Com {taxad}% de redução: \t{diminuir(preço, taxad)}')
    linha()
