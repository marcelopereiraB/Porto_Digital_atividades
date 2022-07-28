#Faça um Programa que leia três números e mostre-os em ordem decrescente.
m1 = float(input('primeiro numero: '))
m2 = float(input('segundo numero: '))
m3 = float(input('terceiro numero: '))
if m1 > m2 > m3:
    print(m1, m2, m3)
if m1 > m3 > m2:
    print(m1, m3, m2)
if m2 > m1 > m3:
    print(m2, m1, m3)
if m2 > m3 > m1:
    print(m2, m3, m1)
if m3 > m2 > m1:
    print(m3, m2, m1)
if m3 > m1 > m2:
    print(m3, m1, m3)
elif m1 == m2 == m3:
    print('ta bebo???')
