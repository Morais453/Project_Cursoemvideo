nt = int(input('Quantos termos da sequiencia de fibonacci você quer mostrar? '))
n1 = 0
n2 = 1
soma = 0
contagem = 2
print(n1,' --> ',n2, end=' --> ' )
while contagem < nt:
    soma = n1 + n2
    print(soma, end=' --> ')
    contagem += 1
    n1 = n2
    n2 = soma
print('FIM')