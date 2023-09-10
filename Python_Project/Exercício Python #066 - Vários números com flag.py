soma = cont = 0
while True:
    print('Para encerrar o programa digite [999]')
    n= int(input('Insira um número: '))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'Você digitou {cont} números e a soma deles foi {soma}')

