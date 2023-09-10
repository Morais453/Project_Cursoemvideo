numb1 = int(input('Informe o primeiro valor: '))
numb2 = int(input('Informe o segundo valor: '))
op = 0
while op != 5:
    print('''[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa''')
    op = int(input('Informe a opção desejada:'))
    if op == 1:
        print(f'O resultado da soma de {numb1} e {numb2} é {numb1+numb2}')
    if op == 2:
        print('O resultado da multiblicação de {} e {} é {}'.format(numb1,numb2,numb1*numb2))
    if op == 3:
        if numb1>numb2:
            print('O número maior é {}'.format(numb1))
        elif numb2>numb1:
            print('O número maior é {}'.format(numb2))
        else:
            print('Números iguais')
    elif op == 4:
        print('Nova inserção de números')
        numb1 = int(input('Informe o primeiro valor: '))
        numb2 = int(input('Informe o segundo valor: '))
    elif op == 5:
        print('Encerrando')
    else:
        print('Número não reconhecido, tente novamente')
print('Programa encerrado, obrigado pela preferência.')