#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
m = str(input('digite F ou M para identificarmos seu sexo: ')).upper()
if m == 'F':
  print('Feminino!')
elif m == 'M':
  print('Masculino!')
else:
  print('sexo invalido')
