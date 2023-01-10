frase = str(input('Digite uma frase: ')).upper().strip().split()
frase = ''.join(frase)
#print(frase)
inverso = ''
for c in range(len(frase)-1, -1, -1):
    inverso += frase[c]
print(f'A frase {frase} ao contrário é {inverso}')
if frase == inverso:
    print('A frase digitada é um políndromo')
else:
    print('A frase digitada não é um políndromo')
