from time import sleep
c = ('\033[m',       # 0 - sem cor
    '\033[0;30;41m', # 1 - vermelho
    '\033[0;30;42m', # 2 - verde
    '\033[0;30;43m', # 3 - amarelo
    '\033[0;30;44m', # 4 - azul
    '\033[0;30;45m', # 5 - roxo
    '\033[7;30m'     # 6 - branco
    )


def linha(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)


def pyhelp():
    """
    Programa que mostra os documentos das bibliotecas ou funções
    :param a: nome da função ou biblioteca
    :return: help(a)
    NÃO PODE SER RODADO EM TERMINAL LOCAL
    """
    while True:
        a = str(input('Função ou Biblioteca > '))
        if a.upper() == 'FIM':
            linha('ATÉ LOGO', 1)
            break
        linha(f'Acessando o manual do comando {a}', 4)
        sleep(2)
        doc = help(a)
        print(c[6], end='')
        print(doc)
        print(c[0], end='')


#programa principal
linha('SISTEMA DE AJUDA PyHELP', 2)
pyhelp()
