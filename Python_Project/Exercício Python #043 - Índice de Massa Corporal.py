peso = int(input('Insira seu peso: '))
altura = float(input('Insira sua altura: '))
imc = peso / pow(altura,2)
print(f'Seu imc é {imc:0.2f}')
if imc < 18.5:
    print('Você está abaixo do peso')
elif imc < 25:
    print('Você está no peso ideal')
elif imc <= 30:
    print('Você está com sobrepeso')
elif imc <= 40:
    print('Você está obeso')
else:
    print('Você está com obesidade morbida')