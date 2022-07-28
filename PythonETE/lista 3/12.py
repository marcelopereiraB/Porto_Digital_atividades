#Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.
lst = []
num = int(input('quantidade de alunos: '))
for n in range(num):
    numbe = float(input('sua altura: '))
    lst.append(numbe)

print(f'O elemento máximo na lista é : {max(lst)} \nO elemento mínimo na lista é : {min(lst)}')
