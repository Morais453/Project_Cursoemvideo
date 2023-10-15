from datetime import date
Ano = date.today().year
Trabalhador = {}

Trabalhador['Nome'] = input('Nome: ').capitalize()
Trabalhador['Idade'] = Ano - int(input('Ano de Nascimento: '))
Trabalhador['CTPS'] = int(input('Carteira de trabalho (0 não tem): '))

if Trabalhador['CTPS'] > 0:
    Trabalhador['Contrato'] = int(input('Ano de contratação: '))
    Trabalhador['Salario'] = int(input('Salário: '))
    Trabalhador['Aposentadoria'] = Trabalhador['Idade'] + ((Trabalhador['Contrato'] + 35) - date.today().year)

print('-='*20)
print(f'O nome do trabalhador inserido foi {Trabalhador["Nome"]}\n'
      f'Com idade igual a {Trabalhador["Idade"]}\n'
      f'N° da CTPS {Trabalhador["CTPS"]}\n')
if Trabalhador['CTPS'] > 0:
    print(f'Contratado desde {Trabalhador["Contrato"]}\n'
          f'Sálario de R${Trabalhador["Salario"]}\n'
          f'Com aposentadoria prevista para {Trabalhador["Aposentadoria"]} anos\n')
