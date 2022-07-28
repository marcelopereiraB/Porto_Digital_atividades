#Faça um Programa que leia três números e mostre o maior deles.
n1 = int(input('digite o primeiro numero: '))
n2 = int(input('digite o segundo numero: '))
n3 = int(input('digite o terceiro número: '))
if n1 > n2 or n1 > n3:
    print(f'seu maior número é {n1}')
if n2 > n1 or n2 > n3:
    print(f'seu maior número é {n2}')
if n3 > n1 or n3 > n2:
    print(f'seu maior número é {n3}')
