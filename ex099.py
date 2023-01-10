def linha():
    print('-=' * 20)


def maior(* num):
        maiornum = max(num)
        linha()
        print('Analisando os valores passados: ')
        print(num)
        print(f'Foram informados {len(num)} valores ao todo.')
        print(f'O maior valor informado foi {maiornum}.')


maior(4, 6, 3, 9)
maior(3.1415, 12, 8)
maior(0)
maior(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    