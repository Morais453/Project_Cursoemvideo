Jogador = dict()
Lista_Gols = []

Jogador['Nome'] = input('Nome do jogador: ')
Jogador['Partidas'] = int(input(f'Quantas partidas {Jogador["Nome"]} jogou? '))

for i in range(Jogador['Partidas']):
    Gols = int(input(f'Na partida {i}, fez quantos gols? '))
    Lista_Gols.append(Gols)
Gols = 0

Jogador['Gols'] = Lista_Gols
print(Jogador)
print(f'O jogador {Jogador["Nome"]} jogou {Jogador["Partidas"]}:')
for k,v in enumerate(Jogador['Gols']):
    print(f'Na partida {k}, fez {v} gols.')
    Gols += v
print(f'Totalizando {Gols} gols.')
