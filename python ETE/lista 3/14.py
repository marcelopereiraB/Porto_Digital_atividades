# Faça um programa que mostre os n termos da Série a seguir:
 # S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m. Imprima no final a soma da série.
def fatorial_for(numero):
    resultado = 1
    for k in range(1, numero + 1):
        resultado *= k
    return resultado

n = int(input('Digite um número inteiro positivo: '))
s = 0
for i in range(0, n + 1):
    s += i / fatorial_for(i * 2)
print(s)
