# Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#a. "Telefonou para a vítima?"
#b. "Esteve no local do crime?"
#c. "Mora perto da vítima?"
#d. "Devia para a vítima?"
#e. "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
pontos = 0
print('responda apenas com sim ou não! ')
a = str(input('Telefonou para a vitima? ')).lower()
if a == 'sim':
    pontos = pontos + 1
else:
    pontos = pontos + 0
b = str(input('esteve no local do crime? ')).lower()
if b == 'sim':
    pontos = pontos + 1
else:
    pontos = pontos + 0
c = str(input('mora perto da vitima? ')).lower()
if c == 'sim':
    pontos = pontos + 1
else:
    pontos = pontos + 0
d = str(input('devia para a vitima? ')).lower()
if d == 'sim':
    pontos = pontos + 1
else:
    pontos = pontos + 0
e = str(input('já trabalhou com a vitima? ')).lower()
if e == 'sim':
    pontos = pontos + 1
else:
    pontos = pontos + 0
if pontos == 2:
    print('Suspeita!!')
if pontos == 3 or pontos == 4:
    print('cúmplice!!')
if pontos == 5:
    print('Assasino safado!!!! Pode prender esse puto!')
elif pontos == 0:
    print('inocente!!')