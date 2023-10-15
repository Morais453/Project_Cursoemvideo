from random import randint
from time import sleep
listGeral = []

quant = int(input('Informe quantos jogos você quer mostrar: '))

for i in range(1,quant + 1):
    i = []
    for n in range(0,6): #sorteia os 6 números
        numb  =  randint(1, 60)
        if numb in i: #se o número ja estiver na lista o 'continue' faz voltar ao sorteio sem contar a vez
            continue
        else: #se não estiver na lista, adicione
            i.append(numb)
     
    i.sort() #ordena a lista
    listGeral.append(i) #adiciona na lista geral

print('Sorteando os Jogos')
sleep(0.5)
for i in range(quant): #mostra as listas
    print(f'O jogo {i+1}:{listGeral[i]}')
    sleep(0.5)