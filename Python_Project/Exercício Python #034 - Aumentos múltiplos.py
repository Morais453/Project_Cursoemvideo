n = int(input('Insira seu salário: R$'))
if n>1250:
    print(f'seu sálario será R${(n/10)+n:0.2f}')
else:
    print(f'seu salario será R${(n*0.15)+n}')