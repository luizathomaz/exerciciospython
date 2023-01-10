from datetime import date
ano = int(input('Digite um ano: '))
if ano == 0:
    ano = date.today().year
if (2020 - ano) % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é bissexto.')
else:
    print('O ano {} não é bissexto.'.format(ano))
