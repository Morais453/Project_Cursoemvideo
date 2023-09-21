variavel = input('Insira uma expressão:  ')
lista = []

for i in variavel:
    if i in '(':
        lista.append('(')
    elif i in ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break

if len(lista) == 0:
    print('Expressão válida')
else:
    print('Expressão inválida')
