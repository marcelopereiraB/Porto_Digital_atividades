#Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.
from time import sleep

ano = 0
popu1 = float(input('digite a população do primeiro pais: '))
popu2 = float(input('Digite a população do segundo pais: '))
a = float(input('me diga a % do crecimento inicial do primeiro pais: '))
b = float(input('me diga a % do crecimento inicial do segundo pais: '))
sleep(1)
print('analisando...')
sleep(2)
while popu1 < popu2:
    popu1 = (popu1 * a / 100)
    popu2 = (popu2 * b / 100)
    ano = ano + 1
if popu1 == popu2:
    print(f'Serão necessarios {ano} Anos para o primeiro chegar proximo do segundo em  quantidade de habitantes')
