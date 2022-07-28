from time import sleep
lista = []
while True:
    v = lista.append(int(input('digite um valor: ')))

    if v:
        print('Valor duplicado! Não vou adicionar...')
        lista.count(v)
        lista.pop()
    else:
        print('adicionado com sucesso...')
        sleep(1)

    m = str(input('Quer continuar? [S/N]')).strip().upper()[0]

    if m == 'N':
        break

print(sorted(lista))
