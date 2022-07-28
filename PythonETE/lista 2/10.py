#Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.
import time
from datetime import date
ano = int(input('qual ano deseja analisar? '))
if ano == 0:
    ano = date.today().year
print('analisando...')
time.sleep(2)
if ano % 4 == 0 and ano % 100 != 0 or ano %400 == 0:
    print(f'{ano} é um ano bissexto!!')
else:
    print(f'{ano} não é bissexto!!')
