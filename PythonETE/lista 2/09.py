# Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
es = str(input('Em que turno você estuda? ')).upper().strip()
na = str(input('qual é o seu nome? ')).strip()

if es == 'MANHÃ' and 'MANHA':
    print(f'bom dia, {na}')
if es == 'TARDE':
    print(f'Boa tarde, {na}')
elif es == 'NOTURNO' and 'NOITE':
    print(f'Boa noite, {na}')
else:
    print('não sabes oq turno significa?')
