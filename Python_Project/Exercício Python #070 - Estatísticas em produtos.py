nome = preco = somat = cont = np = pm = cm = 0

while True:

    nome = input('Informe o nome do produto: ')
    preco = int(input('Informe o preço do produto: R$'))
    somat += preco
    cm +=1

    if pm > preco or cm == 1:
        np = nome
        pm = preco

    if preco > 1000:
        cont += 1

    loop = input('Quer continuar? [S/N] ').upper()
    while (loop != 'S') and (loop != 'N'):
        loop = input('Quer continuar? [S/N] ').upper()
    if loop == 'N':
        break

print(f'O valor total a ser pago é de R${somat:.2f}, foram {cont} maiores que R$1000.00 e o produto mais barato foi {np} que custa R${pm:.2f}')