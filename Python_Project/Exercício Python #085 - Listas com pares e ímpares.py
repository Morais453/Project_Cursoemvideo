lista = [[],[]]
for i in range(0,5):
    valor = int(input(f'Insira o valor {i+1}°: '))

    if (valor % 2) == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
lista[0].sort()
 lista[1].sort()
print(f'Os números pares são {lista[0]}\nE os ímpares são {lista[1]}')