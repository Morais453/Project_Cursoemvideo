from random import randint
from time import sleep
print('Adivinhe o número que a máquina pensar(de 0 a 10)')
p = int(input('Press a key: '))
m = randint(0,10)
t = 0

if p == m:
    print('Processando o resultado...')
    sleep(0.5)
    print(f'Meu número foi {m} e o seu foi {p}')
    print('Parabéns, Você acertou')
t += 1

while t<3 and p!=m:

    if p > 10:
        print(f'Tenten novamente restan {3-t} tentativas')
        t = t + 1
        p = int(input('Número não reconhecido tente novamente: '))

    elif p <= 10:
        print('Processando o resultado...')
        sleep(0.5)
        print(f'Número incorreto')
        print(f'Tenten novamente restan {3 - t} tentativas')
        t = t + 1
        p = int(input('tente novamente: '))

if p == m:
    print('Processando o resultado...')
    sleep(0.5)
    print(f'Meu número foi {m} e o seu foi {p}')
    print('Parabéns, Você acertou')

elif t==3:
    print(f'Acabaram as tentativas, o número era {m}')
