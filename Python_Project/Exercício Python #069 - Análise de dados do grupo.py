idade = sexo = conti = conth = contm = loop = 0
while True:

    print('Cadastre uma pessoa')
    idade = int(input('Idade: '))
    sexo = input('Sexo: [M/F]').upper()

    while (sexo != 'M') and (sexo != 'F'):  #sexo not in 'MF'#
        sexo = input('Sexo: [M/F]').upper()

    if idade > 18:
        conti += 1

    if 'M' in sexo:
        conth += 1

    if 'F' in sexo and idade < 20:
        contm += 1

    loop = input('Quer continuar? [S/N] ').upper()
    while (loop != 'S') and (loop != 'N'):
        loop = input('Quer continuar? [S/N] ').upper()
    if loop == 'S':
        continue
    if loop == 'N':
        break

print(f'{conti} pessoas tem mais de 18\nForam inseridos {conth} homens\n{contm} mulheres tem menos de 20 anos')
