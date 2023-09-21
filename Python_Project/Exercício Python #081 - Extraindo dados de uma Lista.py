lista = []

while True:
    valor = int(input('Insira o valor: '))
    if valor not in lista:  # verificar se já tem

        if len(lista) > 0:

            for ind, num in enumerate(lista):

                if num < valor and ind == 0:  # Se (o valor for menor que o número e se o index for 0) insira-o no index 0
                    lista.insert(ind, valor)
                    break
                else:  # Se não, verificar:
                    if num < valor:  # se o valor for menor que o numero insira na posição do numero
                        lista.insert(ind, valor)
                        break
                    if num > valor:  # se o valor for maior que o número, verifique
                        if num == lista[-1]:  # se o numero for igual o ultimo numero da lista, apenas adicionar no final
                            lista.append(valor)
                            break
                        else:  # se não for o ultimo número
                            if valor < lista[ind + 1]:  # verificar se o valor é menor que o proximo item da lista, se True adicione no lugar
                                lista.insert(ind + 2, valor)
                                break
                            else:  # se não, continuar verificando
                                continue
        else:
            lista.append(valor)
            print('Primeiro valor adicionado')
    else:
        print('Valor repetido não será adicionado')

    esc = input('Você quer continuar?[S/N] ').upper()

    while esc not in 'SN':
        esc = input('Você quer continuar?[S/N] ').upper()

    if esc in 'N':
        break

print(f'A quantidade de itens em lista é {len(lista)},a ordem de números é {lista}, 5 faz parte da lista? {5 in lista}')
