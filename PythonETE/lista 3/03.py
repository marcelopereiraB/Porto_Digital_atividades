#popu1 = 80.000 mias 3% ano
#Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
#popu2 = 200.000 mais 1.5% ano
from time import sleep
ano = 0
popu1 = 80000
popu2 = 200000
a = 0.015
b = 0.03
print('sabendo que a população A tem 80.000 mil habitantes e B tem 200.000 mil,'
      'vamos calcular quantos anos iria levar pra igualar')
sleep(1)
print('analisando...')
sleep(2)
while popu1 < popu2:
    popu1 = popu1 + (popu1 * a)
    popu2 = popu2 + (popu2 * b)
    ano = ano + 1
if popu1 == popu2:
    print(f'Serão necessarios {ano} para A e B ter a mesma quantidade de habitantes')



