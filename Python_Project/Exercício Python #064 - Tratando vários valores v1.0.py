contagem = 0
soma = 0
n = int(input('Informe um valor[para encerrar insira 999]: '))
while n < 998:
    contagem += 1
    soma += n
    n = int(input('Informe um valor[para encerrar insira 999]: '))
print(f'foram inseridos {contagem} e sua soma foi de {soma}')