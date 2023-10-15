lista_geral = []
Pessoa = {}
totalid = 0
while True:
    Pessoa['Nome'] = input('Nome: ').capitalize()
    Pessoa['Sexo'] = input('Sexo: [M/F] ').upper()

    while Pessoa['Sexo'] not in 'MF':
        Pessoa['Sexo'] = input('Sexo: [M/F] ').upper()
    Pessoa['Idade'] = int(input('Idade: '))
    lista_geral.append(Pessoa.copy())

    esc = input('Quer continuar? [S/N] ').upper()
    while esc not in 'SN':
        esc = input('Quer continuar? [S/N] ').upper()
    if esc in 'N':
        break

print(f'A) Ao todo remos {len(lista_geral)} pessoas cadastradas.')

for i in lista_geral:
    totalid += i['Idade']
media = totalid / len(lista_geral)

print(f'B) A média de idade é de {media:0.2f}')

print('As mulheres cadastradas foram: ', end=' ')
for i in lista_geral:
    if i['Sexo'] in 'F':
        print(i['Nome'],end=' ')
print()

print('D) Lista de pessoas que estão acima da média de idade: ')
for i in lista_geral:
    if i['Idade'] >= media:
        print(i)
print('FIM')


