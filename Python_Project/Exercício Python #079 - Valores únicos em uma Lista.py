List= []
opc = 'S'
while opc in 'S':
    v = int(input('Insira um valor: '))
    for i,n in enumerate(List):
        if (n == v) and (i >= 0):
            print('Número duplicado, não irei salvar')
            break
        if (List[i] == List[-1]) and (n != v):
            List.append(v)
            print('Valor registrado com sucesso')
            break
    if len(List) == 0:
        List.append(v)
        print('Primeiro valor adicionado com sucesso')

    opc = input('Gostaria de continuar?[S/N]').upper()
    while opc not in 'SN':
        opc = input('Informe uma opção válida[S/N]').upper()
List.sort()
print(f'Os valores inseridos foram {List}')
