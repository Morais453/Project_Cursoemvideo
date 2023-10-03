matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = 0
soma_c3 = 0
maior_l2 = 0


for linha in range(0, 3):  #alimentação
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Insira um valor para [{linha, coluna}]: '))
        soma += matriz[linha][coluna]
        if coluna == 2:
            soma_c3 += matriz[linha][coluna]
        if linha == 1:
            if coluna == 0 or matriz[linha][coluna] > maior_l2:
                maior_l2 = matriz[linha][coluna]

for linha in range(0, 3):  #mostrar
    for coluna in range(0, 3):
        print(f'{matriz[linha][coluna]:^5}', end='')
    print()

print(f'A soma dos valores informados é igual a {soma}\nA soma dos valores da coluna 3 é {soma_c3}\nO maior valor da linha 2 é {maior_l2}')