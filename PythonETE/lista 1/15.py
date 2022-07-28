# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
do = float(input('qual é o tamanho do arquivo? em MB/s '))
de = float(input('qual a velocidade da conexão '))

print(f'com a velocidade de {do} seu download terminará em {do / (de / 8)}')
