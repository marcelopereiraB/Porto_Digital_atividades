#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

al = float(input('Qual é sua altura? '))
form = float((72.7 * al) - 58)
print('com a altura {} e o peso 58kl seu peso ideal é {:.2f} '.format(al, form))

