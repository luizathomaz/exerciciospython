a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
menu = []
while menu != 5:
    menu = int(input('''\n[1] somar\n[2] multiplicar\n[3] maior\n[4] novos números\n[5] sair do programa 
Digite sua opção: '''))
    if menu == 1:
        print('A soma de {} e {} é {}!'.format(a, b, (a+b)))
    elif menu == 2:
        print('{} multiplicado por {} é {}!'.format(a, b, (a*b)))
    elif menu == 3:
        if a > b:
            print(f'O maior número é {a}')
        elif b > a:
            print('O maior número é {}'.format(b))
        else:
            print('Os números digitados são iguais. ')
    elif menu == 4:
        a = int(input('Digite outro primeiro número: '))
        b = int(input('Digite outro segundo número: '))
print('Você saiu do programa. ')
