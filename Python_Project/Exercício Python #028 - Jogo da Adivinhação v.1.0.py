import random
n = random.randint(0,5)
i = int(input('Advinhe o valor de 0 a 5: '))
print(f'O valor sorteado foi {n}')
if n == i:
    print('Você acertou')
else:
    print('Errou')