Dados_Aluno = {}
Dados_Aluno['Nome'] = input('Informe o nome do aluno: ').capitalize()
Dados_Aluno['Media'] = float(input('Informe a média do aluno: '))
if Dados_Aluno['Media'] >= 7:
    Dados_Aluno['Declaration'] = 'Aprovado'
elif 5 <= Dados_Aluno['Media'] < 7:
    Dados_Aluno['Declaration'] = 'Recuperação'
else:
    Dados_Aluno['Declaration'] = 'Reprovado'


print(f'O aluno {Dados_Aluno["Nome"]} teve média igual a {Dados_Aluno["Media"]} e sua situação final é {Dados_Aluno["Declaration"]}')