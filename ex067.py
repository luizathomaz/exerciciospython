n = 0
while True:
    print('-'*30)
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-'*30)
    if n < 0:
        print('PROGRAMA ENCERRADO. Volte sempre!')
        break
    for i in range(1, 11):
        print(f'{n} x {i}  = {n*i}')
