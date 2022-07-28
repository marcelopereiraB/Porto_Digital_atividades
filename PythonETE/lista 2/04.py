# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
pa = str(input('digite uma letra: ')).lower()
if pa == 'a' or pa == 'e' or pa == 'i' or pa== 'o' or pa == 'u':
    print('é uma vogal')
else:
    print('é uma consoante')