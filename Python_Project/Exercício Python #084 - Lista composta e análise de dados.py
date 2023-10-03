pessoas = []
gordo = []
magro = []
leve = pesado = 0
while True:
    nome = input('Informe o nome: ').upper()
    Peso = int(input('Informe a Peso: '))
    if len(pessoas) == 0 or Peso > pesado:
        pesado = Peso
    if len(pessoas) == 0 or Peso < leve:
        leve = Peso
    pessoas.append([nome, Peso])

    esc = input('Quer continuar?[S/N]').upper()
    while esc not in 'SN':
        esc = input('Quer continuar?[S/N]').upper()
    if esc in 'N':
        break

for i in pessoas:
    if i[1] == pesado:
        gordo.append(i[0])
    if i[1] == leve:
        magro.append(i[0])

print(f'Foram inseridas {len(pessoas)}, o maior peso foi {pesado} e seu/seus respectivo nome {gordo}, o mais leve foi {leve} com nome {magro}')
