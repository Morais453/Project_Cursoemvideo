frase = input('Digite uma frase: ').strip().split()
j = ''.join(frase).upper()
ij = j[::-1]
print(f'A frase {j} tem como inversa {ij}')
if j == ij:
    print('É palindromo')
else:
    print('Não é palindromo')
