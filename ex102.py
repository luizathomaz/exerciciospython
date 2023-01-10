def fatorial(n, show=False):
    """
    Função para calculo de fatorial: 
    :param n: número a ser calculado 
    :param show: (opicional) mostra ou não a conta
    :return: o valor fatorial do número n
    """
    fa = 1
    for cont in range(n, 0, -1):
        fa *= cont
        if show:
            print(cont, end='')
            if cont > 1: 
                print(' x ', end='')
            else:
                print(' = ', end='')
    return fa




print(fatorial(5, show=True))
