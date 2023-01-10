from datetime import date
atual = date.today().year
ano = int(input('Ano de nascimento: '))
idade = atual - ano
print(f'Quem nasceu em {ano} tem {idade} em {atual}.')
if idade < 18:
    print('Ainda faltam {} ano(s) para o alistamento.'.format(18 - idade))
    print('Seu alistamento será em {}.'.format(atual + (18 - idade)))
elif idade > 18:
    print('Você deveria ter se alistado há {} anos.'.format(idade - 18))
    print(f'Seu alistamento foi em {atual - (idade - 18)}.')
elif idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
