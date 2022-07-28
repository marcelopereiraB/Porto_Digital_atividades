#Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique o programa para que ele mostre os números um ao lado do outro.
contador = 0
while contador <= 19:
    contador = contador + 1
    print(contador)

for i in range(21):
    print(i)
print(list(range(1, 21)))
