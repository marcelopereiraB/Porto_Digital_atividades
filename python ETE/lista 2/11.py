# Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
dia = int(input('digite um dia do mes: '))
mes = int(input('digite um mes do ano: '))
ano: int = int(input('digite um ano: '))
caso1 = [1, 3, 5, 8, 10, 12]
caso2 = [4, 6, 9, 11]

if (mes in caso1) and (1 <= dia <= 31) and ano != 0:
    print(f'{dia}/{mes}/{ano} é valida')
elif (mes in caso2) and (1 <= dia <= 30) and ano != 0:
    print(f'{dia}/{mes}/{ano} é sim uma data valida!')
elif (mes == 2) and (1 <= dia <= 29) and ano != 0:
    print(f'{dia}/{mes}/{ano} é valido!!')
else:
    print('data invalida!!')
