from datetime import date
anon= int(input('Insira seu ano de nascimento: '))
idade = date.today().year - anon
if idade <= 9:
    print('Analisando o seu ano e vendo que sua idade é de {} anos concluimos que pode competir na modalidade mirim'.format(idade))
elif idade <= 14:
    print('Analisando o seu ano e vendo que sua idade é de {} anos concluimos que pode competir na modalidade infantil'.format(idade))
elif idade <= 19:
    print('Analisando o seu ano e vendo que sua idade é de {} anos concluimos que pode competir na modalidade júnior'.format(idade))
elif idade <= 25:
    print('Analisando o seu ano e vendo que sua idade é de {} anos concluimos que pode competir na modalidade sênior'.format(idade))
elif idade > 25:
    print('Analisando o seu ano e vendo que sua idade é de {} anos concluimos que pode competir na modalidade master'.format(idade))