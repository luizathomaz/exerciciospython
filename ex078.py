lista = list()
for cont in range(0, 5):
    lista.append(int(input('Digite um valor: ')))
print(lista)
maximo = max(lista)
minimo = min(lista)
for i in range(0, 5):
    if lista[i] == maximo:
        print(f'O maior valor é {maximo} na posição {i+1}')
    if lista[i] == minimo:
        print(f'O menor valor é {minimo} na posição {i+1}')
