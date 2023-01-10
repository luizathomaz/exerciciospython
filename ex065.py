n = cont = soma = 0
sair = []
maior = menor = 0
while sair != 'n':
    n = int(input('Digite um número: '))
    cont += 1
    soma += n
    if n == 1:
        maior = n
        menor = n
    elif n > maior:
        maior = n
    else:
        menor = n
    sair = str(input('Deseja continuar [S/N]: ')).strip().lower()[0]
print(f'Você digitou {cont} números e a média foi {soma/cont}.')
print(f'O maior valor foi {maior} e o menor foi {menor}')
