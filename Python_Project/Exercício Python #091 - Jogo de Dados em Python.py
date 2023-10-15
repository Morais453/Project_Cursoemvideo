from random import randint
from time import sleep
from operator import itemgetter
jogo = {'Jogador1' : randint(1,6),
        'Jogador2' : randint(1,6),
        'Jogador3' : randint(1,6),
        'Jogador4' : randint(1,6)}

print('Valores Sorteados')
    
for k, v in jogo.items():
    print(f'O {k} tirou {v} no dado.')
    sleep(0.5)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('RANKING DOS JOGADORES')
for r,k in enumerate(ranking):
    print(f'O {k[0]} tirou {k[1]} e ficou em {r+1}° Lugar')