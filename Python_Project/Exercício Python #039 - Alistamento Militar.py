from datetime import date
genero = int(input('Para se informar sobre o alistamento digite 0 se você for Homem, e se for mulher digite 1:'))

if genero == 0:
    ano = int(input('insira seu ano '))
    idade = date.today().year - ano
    anoa = date.today().year
    print(f'O cara que nasceu em {ano} tem {idade} em {anoa}')
    if idade < 18:
        print("Ainda faltam {} para seu alistamento\nseu alistamento será em {}".format(18-idade,anoa+(18-idade)))
    elif idade == 18:
        print('Chegou o seu ano de se alistar, procure a junta militar mais proxima de você')
    else:
        print(f'Você deveria ter se alistado a {idade-18}ano\nSeu ano de alistamento foi {ano+18}')
elif genero == 1:
    print('Você não precisa participar do alistamento obrigatorio')
else:
    print('Comando incorreto tente novamente')