#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
c = int(input('Digite um uma nota de 0 a 10: '))
while c > 10:
    c = int(input('nota invalida! Digite novamente: '))
if c <= 10:
    print(f'a nota {c} é valida!')


