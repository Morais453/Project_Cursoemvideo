import random
n = random.randint(0,10)
i = int(input('Advinhe o valor de 0 a 10: '))
contador=1                                    #acertou = false while not acertou: if jogador == maquina: acertou=True
if n == i:
    print('Parabéns acertou de primeira')
else:
    while n != i:
        contador +=1
        i = int(input('Errou, tente novamente um valor de 0 a 10: '))
    print(f'Parabéns você acertou, porém foram necessarias {contador} tentativas')
