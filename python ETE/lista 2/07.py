# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
mec1 = float(input('primeiro produto: '))
mec2 = float(input('segundo produto: '))
mec3 = float(input('terceiro produto: '))
if mec1 < mec2 and mec1 < mec3:
    menor = mec1
    print(f'seu primeiro produto é o mais barato com o valor de R${menor}')
if mec2 < mec3 and mec2 < mec1:
    menor = mec2
    print(f'seu segundo produto é o mais barato com o valor de R${menor}')
if mec3 < mec1 and mec3 < mec2:
    menor = mec3
    print(f'seu terceiro produto é o mais barato com o valor de R${menor}')

