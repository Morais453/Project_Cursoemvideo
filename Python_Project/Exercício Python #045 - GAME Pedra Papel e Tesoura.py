from random import randint
from time import sleep
print("""Vamos jogar pedra papel e tesoura?
Para pedra digite [1]
Para papel digite [2]
Para tesoura digite [3]""")

pc = randint(1,3)

humam = int(input('Insira sua opção: '))

print('Carregando resultado...')
sleep(3)
x = ['pedra' , 'papel' , 'tesoura']
y = ['pedra', 'papel' , 'tesoura']

#op humano
if humam == 1:
    y = y[0]
elif humam == 2:
    y = y[1]
elif humam == 3:
    y = y[2]
#op pc
if pc == 1:
    x = x[0]
elif pc == 2:
    x = x[1]
elif pc == 3:
    x = x[2]

print('-'*33)
print(f'A minha opção foi {x} e a sua foi {y}')
if humam == pc:
    print('empate')
elif humam == 1 and pc == 3 or humam == 2 and pc == 1 or humam == 3 and pc == 2:
    print('Você ganhou, parabéns')
elif pc == 1 and humam == 3 or pc == 2 and humam == 1 or pc == 3 and humam == 2:
    print('Eu ganhei haha!')
else:
    print('Jogada invalida')
print('-'*33)