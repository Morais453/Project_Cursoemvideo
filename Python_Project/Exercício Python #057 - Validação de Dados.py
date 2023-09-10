sexo = input('Qual o seu sexo [M/F]: ').upper().strip()
while sexo != 'F' and sexo != 'M':   #while sexo not in 'FM':
    print('Dados inválidos')
    sexo = input('Por favor informe novamente [M/F]: ').upper().strip
print('Sexo {} registrado com sucesso'.format(sexo))