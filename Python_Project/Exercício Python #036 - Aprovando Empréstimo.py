Vc = int(input('Insira o valor da casa: '))
Vs = int(input('Insira seu salário: '))
t = int(input('Quer pagar em quantos anos? '))

pc = (Vc/t)/12
ps = Vs * 0.30

print(f'Para pagar a casa de R${Vc:0.2f} em {t} anos a prestação será de R${pc:0.2f}')
if pc > ps:
    print('Emprestimo negado')
else:
    print('Emprestimo concedido')
