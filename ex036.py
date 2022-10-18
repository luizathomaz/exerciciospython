casa = int(input('Valor da casa: R$ '))
sal = int(input('Salário do comprador: R$ '))
ano = int(input('Quantos anos de financiamento: '))
prest = casa / (ano * 12)
trintasal = sal * 0.3
print(f'Para pagar uma casa de R${casa} em {ano} anos a prestação será de R${prest:.2f}.')
if prest > trintasal:
    print('Empréstimo NEGADO!')
else:
    print('Empréstimo APROVADO!')
