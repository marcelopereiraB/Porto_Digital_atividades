#Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for lido um número negativo.
n = int(input("Quantos números: "))
i = 0
a = 0
b = 0
c = 0
d = 0
while i < n:
    numero = int(input("Insira número:"))
    i = i + 1
    print(i)
    if numero < 0:
        break
    if 0 <= numero <= 25:
        a = a + 1
    if 26 <= numero <= 50:
        b = b + 1
    if 51 <= numero <= 75:
        c = c + 1
    if 76 <= numero <= 100:
        d = d + 1
print(f'Intervalo1: {a}')
print(f'Intervalo2: {b}')
print(f'Intervalo3: {c}')
