list_geral = []
Escolha = 'S'
while Escolha in 'S':
    Name = input('Insira o nome: ')
    Nota1 = float(input('Insira a nota da primeira avaliação: '))
    Nota2 = float(input('Insira a nota da segunda avaliação: '))
    list_geral.append([Name,Nota1,Nota2])

    Escolha = input('Deseja continuar?[S/N]').upper()
    while Escolha not in 'SN':
        Escolha = input('Deseja continuar?[S/N]').upper()

print('-='*20)
print('N°                NOME             MÉDIA')
for i in range(len(list_geral)):
    print(f'{i:<10}{list_geral[i][0]:^20}{(list_geral[i][1]+list_geral[i][2])/2:>10}')
print('-='*20)

while True:
    Esc =  input('Deseja ver a nota de algum aluno?[S/N] ').upper()
    while Esc not in 'SN':
        Esc = input('Deseja ver a nota de algum aluno?[S/N] ').upper()
    if Esc in 'N':
        break

    print('-='*20)
    Aluno = int(input('Insira o número do aluno conforme a tabela acima: '))
    print(f'{list_geral[Aluno][0]} teve como notas {list_geral[Aluno][1]} e {list_geral[Aluno][2]}')
    print('-='*20)
    