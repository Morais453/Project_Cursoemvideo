matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


for linha in range(0, 3):  #alimentação
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Insira um valor para [{linha, coluna}]: '))

for linha in range(0, 3):  #mostrar
    for coluna in range(0, 3):
        print(f'{matriz[linha][coluna]:^5}', end='')
    print()