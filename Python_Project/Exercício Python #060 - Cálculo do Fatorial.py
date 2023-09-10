numb= int(input('Digite um número e veja seu fatorial: '))
fat= 1
print(f'Calculando {numb}! = ', end='')
while numb >0 :
    print(numb,end='')
    print(' x ' if numb >1 else ' = ',end='')
    fat *= numb
    numb -= 1
print(fat)