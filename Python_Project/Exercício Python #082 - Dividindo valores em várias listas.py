Geral = []
impar = []
par = []

while True:
    numb = int(input('Insira um valor: '))
    Geral.append(numb)

    Escolha = input('Deseja continuar?[S/N]').upper()
    while Escolha not in 'SN':
        Escolha = input('Deseja continuar?[S/N]').upper()

    if Escolha in 'N':
        break

for i in Geral:
    if i % 2 == 0:
        par.append(i)
    else:
        impar.append(i)
print(f'os numeros inseridos são{Geral}\nOs pares {par}\nOs impares {impar}')