import math
n = float(input('digite o angulo que deseja: '))
n1 = math.sin(math.radians(n))
n2 = math.cos(math.radians(n))
n3 = math.tan(math.radians(n))
print('O angulo de {} tem o SENO de {:.2f} \n O angulo de {} tem o Cosseno de {:.2f} \n O anfulo de {} tem a TANGENTE é {:.2f}'.format(n, n1, n, n2, n, n3))
#alternativa
n = float( input('digite o angulo que deseja: '))
seno = math.sin(math.radians(n))
print('O angulo de {:.2f} tem o SENO de {:.2f}'.format(n, seno))
coseno = math.cos(math.radians(n))
print('O angulo de {} tem o cosseno de {:.2f}'.format(n, coseno))
tangente = math.tan(math.radians(n))
print(' o angulo de {} tem a tangente {:.2f}'.format(n,tangente))
# 3 forma
from math import sin, cos, tan, radians
n = float( input('digite o angulo que deseja: '))
seno = sin(radians(n))
print('O angulo de {:.2f} tem o SENO de {:.2f}'.format(n, seno))
coseno = cos(radians(n))
print('O angulo de {} tem o cosseno de {:.2f}'.format(n, coseno))
tangente = tan(radians(n))
print(' o angulo de {} tem a tangente {:.2f}'.format(n,tangente)) pow()

