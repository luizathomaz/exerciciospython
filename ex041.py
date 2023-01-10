from datetime import date
ano = date.today().year
nasc = int(input('Digite o ano de nascimento: '))
idade = ano - nasc
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('MIRIM')
elif 9 < idade <= 14:
    print('INFANTIL')
elif 14 < idade <= 19:
    print('JÚNIOR')
elif 19 < idade <= 25:
    print('SÊNIOR')
elif idade > 25:
    print('MASTER')
