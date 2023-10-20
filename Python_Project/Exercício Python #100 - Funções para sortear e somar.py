from random import randint
from time import sleep
def sorteia(l:list):
    print('Sorteando 5 valores: ', end=' ')
    for i in range(5):
        i = randint(1,10)
        l.append(i)
        print(i,end=' ', flush= True)
        sleep(0.7)
    print("PRONTO")

def somaP(l:list):
    soma = 0
    for i in l:
        if i % 2 == 0:
            soma += i
    print(f'Somando os valores pares de {l} temos como resultado: {soma}')
    

a = []
sorteia(a)
somaP(a)

