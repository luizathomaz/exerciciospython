'''from math import cos, tan, sin
ang = int(input('Digite um angulo em °: '))
print('O valor do seno é {:.2f}, cosseno é {:.2f} e da tangente é {:.2f}'.format(sin(ang), cos(ang), tan(ang)))'''
import math
ang = float(input('Digite o angulo que voce deseja: '))
seno = math.sin(math.radians(ang))
coss = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print('O angulo {} tem o seno de {:.2f}'
      'O cosseno de {:.2f} e a tangente de {:.2f}'.format(ang, seno, coss, tan))
