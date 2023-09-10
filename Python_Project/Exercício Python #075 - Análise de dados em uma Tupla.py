CntN  = ind = 0
pt = False
T = ()
Pares = ()
for i in range(0, 4):
    n = int(input(f'Insira o valor {i+1} da tupla: '))

    if n == 9:
        CntN += 1
    if n % 2 == 0:
        Pares.append(n)
    T.append(n)
# if 3 in T:
for i in range(len(T)):
    if T[i] == 3:
        pt = True
        ind = i
if pt == True:
    print(f'analisando a procura do número 3 temos que {ind} é sua localização')
else:
    print('Valor 3 não encontrado')

print(f'O número 9 apareceu {CntN}x e foram {Pares} os pares inseridos')

