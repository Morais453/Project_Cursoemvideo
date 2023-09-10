num= int(input('digite um numero: '))
lista = [num]
soma = num
cont = 1
escolha = input('Deseja continuar?[S/N] ').upper()
while escolha in 'S':
    num = int(input('digite um numero: '))
    lista.append(num)
    soma += num
    cont +=1
    escolha = input('Deseja continuar?[S/N] ').upper()
print(f'Você inseriu {cont} números a média deles foi {soma/cont}\nO maior foi {max(lista)} e o menor foi {min(lista)}')