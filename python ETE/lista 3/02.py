#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
nome = str(input('\033[5;49;96m Digite seu nome de usuario: ')).upper().strip()
senha = str(input('\033[5;49;96m Digite sua senha: ')).upper().strip()
while senha == nome:
    print('\033[5;49;91m Sua senha ou nome de usuario está errado!!!')
    nome = str(input('\033[5;49;96m Digite seu nome de usuario: '))
    senha = str(input('\033[5;49;96m Digite sua senha: '))
if nome != senha:
    print('\033[5;49;92m Login feito com sucesso!')
