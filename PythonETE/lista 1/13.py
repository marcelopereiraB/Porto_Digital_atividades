#. Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas: Para homens: (72.7*h) - 58.  Para mulheres: (62.1*h) - 44.7
al = float(input('me diga sua altura: '))
se = str(input('me diga seu genero: ')).strip().upper()

if se == 'MASCULINO':
  print('seu peso ideal é {:.2f}'.format((72.7 * al) - 58))
else:
  print('seu peso ideal é {:.2f}'.format((62.1 * al) - 44.7))
