#10. Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
cel = float(input('conversor de Fahrenheit em graus celsius: '))
conv = float(5 * (cel - 32) / 9)
print('a conversão de Fahrenheit em Graus celsius é {:.4}'.format(conv))
