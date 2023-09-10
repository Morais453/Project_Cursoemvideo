numb= int(input('Digite um número: '))
div = []
nd= []
for c in range(1,numb+1):
    if numb%c==0:
        div.append(c)
    else:
        nd.append(c)
print(f'{numb} foi dividido {len(div)}x e não divisivel {len(nd)}, sendo divisivel por {div}')
if len(div)<=2:
    print('Por tanto é número primo')
else:
    print('Não primo')