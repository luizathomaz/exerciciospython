'''from random import random
nomeum = str(input('Digite o nome do aluno um: '))
nomedois = str(input('Digite o nome do aluno dois: '))
nometres = str(input('Digite o nome do aluno três: '))
nomequatro = str(input('Digite o nome do aluno quatro: '))
random(nomeum, nomedois, nometres, nomequatro)
print('O aluno selecionado foi {}.'.format(random))'''
import random
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno:'))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}.'.format(escolhido))
