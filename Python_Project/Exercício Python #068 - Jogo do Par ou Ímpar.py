from random import randint
Pc = Humano = Vitorias = resultado = 0
escolha = ''

while True:

    escolha = str(input('Escolha par ou ímpar:[P/I] ')).upper()

    if (escolha != 'P') and (escolha != 'I'):
        print('Entrada incorreta')
        continue

    Pc = randint(0,11)
    Humano = int(input('Escolha seu número de 0 a 10: '))
    resultado = (Pc + Humano)%2

    if 'P' in escolha:
        if resultado == 0:
            print('Você ganhou')
            Vitorias +=1
        else:
            print(f'Eu ganhei e a sua sequencia de vitórias consecutivas foi {Vitorias}')
            break

    if 'I' in escolha:
        if resultado != 0:
            print('Você ganhou')
            Vitorias +=1
        else:
            print(f'Eu ganhei e a sua sequencia de vitórias consecutivas foi {Vitorias}')
            break
