times = ('Atletico Mineiro', 'Flamengo', 'Cruzeiro', 'Naútico', 'Chapecoense', 'Corinthias', 'Fluminense', 'Atlético Paranaense',
         'São Paulo', 'Vasco', 'Bahia', 'Vitória', 'Grémio', 'Sport', 'Internacional', 'Paisandu', 'Palmeiras', 'América MG',
         'Botafogo', 'Santos')
print(f'Os primeiros colocados são: {times[0:5]}')
print(f'Os últimos colocados são: {times[-4:]}')
print(f'Os times em ordem alfabética: {sorted(times)}')
print(f'O time da Chapecoense está na posição: {times.index("Chapecoense")+1}')
