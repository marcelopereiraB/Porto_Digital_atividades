#9. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius. C = 5 * ((F-32) / 9).
cel = float(input('conversor de graus celsius em Fahrenheit: '))
conv = float(cel * 1.8 +31)
conv2 = 9 * cel / 5 + 32
print('a conversão de graus celsius em Fahrenheit é {:.4} \n {} '.format(conv, conv2))