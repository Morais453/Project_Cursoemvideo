n = 0
while True:
    n = int(input('Insira o valor a qual sera atribuido a tabuada(para sair insira um valor negativo): '))
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n}  X {c:2} = {n * c}')
print('Fim')