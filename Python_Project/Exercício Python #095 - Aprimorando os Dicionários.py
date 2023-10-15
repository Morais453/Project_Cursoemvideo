Jogador = dict()
Lista_Time = []
Lista_Gols = []


while True:
    Jogador['Nome'] = input('Nome do jogador: ').capitalize()
    Jogador['Partidas'] = int(input(f'Quantas partidas {Jogador["Nome"]} jogou? '))

    for i in range(Jogador['Partidas']):
        Gols = int(input(f'Na partida {i+1}, fez quantos gols? '))
        Lista_Gols.append(Gols)

    Jogador['Gols'] = Lista_Gols[:]
    Lista_Time.append(Jogador.copy())

    Lista_Gols.clear()


    Escolha = input('Quer continuar? [S/N] ').upper()
    while Escolha not in 'SN':
        Escolha = input('Quer continuar? [S/N] ').upper()
    if Escolha in 'N':
        break


print('-='*30)
print('COD  NOME       GOLS')
for k,v in enumerate(Lista_Time):
    print(f'{k:^5}{v["Nome"]:<10}{v["Gols"]}')


Cod = int(input('Mostrar dados de qual jogador? (999 para parar) '))
while Cod < 999:
    while len(Lista_Time) <= Cod:
        print(f'Erro! Não existe jogador com Codigo {Cod}')
        Cod = int(input('Mostrar dados de qual jogador? (999 para parar) '))

    print(f'Levantamento do jogador {Lista_Time[Cod]["Nome"]}: ')
    Gols = 0
    for k,v in enumerate(Lista_Time[Cod]['Gols']):

        print(f'Na partida {k + 1}, fez {v} gols.')
        Gols += v
    print(f'Totalizando {Gols} gols.')

    Cod = int(input('Mostrar dados de qual jogador? (999 para parar) '))
