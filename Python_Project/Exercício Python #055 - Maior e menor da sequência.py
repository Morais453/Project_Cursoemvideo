maior = 0
menor = 0
for p in range(1,6):
    peso= float(input('Insira o peso da p{}: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de  {} e o menor foi de {}'.format(maior,menor))

"""
p=[]
for c in range(1,6):
    peso= float(input('Insira o peso da p{}: '.format(c)))
    p.append(peso)
print(f'o maior peso é {max(p)} e o menor é {min(p)}')"""