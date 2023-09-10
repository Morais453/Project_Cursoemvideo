n1 = float(input('Insira sua primeira nota: '))
n2 = float(input('Insira sua segunda nota: '))
media = (n1+n2) / 2
print('Sua média foi {}'.format(media))
if media >= 7.0:
    print('Aprovado')
elif media >= 5 and media < 7:
    print('Recuperação')
else:
    print('Reprovado')