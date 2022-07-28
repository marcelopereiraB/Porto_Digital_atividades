#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
n = int(input('digite um valor pra analise de sinal: '))
if n > 0:
    print(f'o valor {n} é positivo!!!')
elif n == 0:
    print(f' o valor {n} é um número neutro!!')
else:
    print(f'o valor {n} é negativo!!!')
