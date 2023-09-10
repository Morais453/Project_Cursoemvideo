hv = 0
soma = 0
mm20 = 0
nomev = str
qm= 0

for p in range(1,5):
    print("-"*15,f'Dados da {p} pessoa',"-"*15)
    sexo = input('Informe seu sexo,[M/F]: ')
    nome = input('Informe seu nome: ').strip()
    idade = int(input('Informe sua idade: '))
    if sexo in 'Mm':
        if idade>hv:
            hv = idade
            nomev = nome
    elif sexo in 'Ff':
        qm +=1
        if idade < 20:
            mm20 += 1
    soma += idade
print('A média de idade é {}'.format(soma/p))
print(f'O homem mais velho tem {hv} anos e seu nome é {nomev}')
if qm>0:
    print(f'De {qm} mulheres, {mm20} tem menos de 20 anos')
else:
    print('Nenhuma mulher na lista')