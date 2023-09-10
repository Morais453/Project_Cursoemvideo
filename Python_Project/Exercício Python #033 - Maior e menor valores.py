p1 = int(input('Insira o valor:  '))
p2 = int(input('Insira o valor:  '))
p3 = int(input('Insira o valor:  '))

l = [p1, p2, p3]

print(f'\033[4;31;40mO valor maior é {max(l)} e o menor é {min(l)}\033[m')
