s = int(input('Insira a distância da viagem: '))
if s <= 200:
    print(f'O valor de sua passagem será de R${s*0.5:0.2f}')
else:
    print(f'O valor de sua passagem será de R${s * 0.45:0.2f}')