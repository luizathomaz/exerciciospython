from datetime import date
pessoa = {'nome': str(input('Nome: ')), 'idade': '', 'ctps': '', 'contratação': '', 'salário': '', 'aposentadoria': ''}
nasc = int(input('Ano de nascimento: '))
pessoa['ctps'] = int(input('Carteira de trabalho: (0 se não tiver) '))
today = date.today()
year = today.year
# ano = datetime.now().year - como o professor pegou o ano (from datetime import datetime)
pessoa['idade'] = year - nasc
if pessoa['ctps'] == 0:
    print(f'nome tem o valor de {pessoa["nome"]}')
    print(f'idade tem o valor de {pessoa["idade"]}')
    print(f'ctps tem o valor de não possui')
else:
    pessoa['contratação'] = int(input('Ano de contratação: '))
    pessoa['salário'] = float(input('Salário: R$'))
    pessoa['aposentadoria'] = (pessoa['contratação'] + 35) - nasc
    print('-=' * 15)
    for k, v in pessoa.items():
        print(f' - {k} tem o valor {v}')
