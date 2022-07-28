#Faça um Programa que leia três números e mostre o maior e o menor deles.
n1 = int(input('digite um número: '))
n2 = int(input('digite um número: '))
n3 = int(input('digite um número: '))
maior = n1
if n2 > n3 and n2 > n1:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print(f'o menor número digitando foi {menor}')
print(f'o maior número digitado foi {maior}')
