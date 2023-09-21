Maior = menor = 0
List= []
for i in range(5):
    valor = int(input(f'Insira o valor na posição {i}: '))
    List.append(valor)
    if i == 0 or valor < menor:
        menor = valor
    if i == 0 or valor > Maior:
        Maior = valor
print('-='*30)

print(f'O maior valor inserido foi {Maior} e apareceu nas posições',end=" ")
for c in range(len(List)):
    if List[c] == Maior:
        print(f'{c:.<3}', end=" ")
print("\n",'-=' * 30)

print(f'O menor valor inserido foi {menor} e apareceu nas posições',end=" ")
for c in range(len(List)):
    if List[c] == menor:
        print(f'{c:.<3}', end=" ")
