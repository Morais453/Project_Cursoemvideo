OBJ = ('Lápis', 0.5, 'Caneta', 1, 'Borracha', 0.5, 'caderno', 15)
print(f'{"TABELA DE PREÇOS":-^32}')
for i in range(len(OBJ)):
    if i % 2 == 0:
        print(f'{OBJ[i]:.<25}', end='')
    if i % 2 == 1:
        print(f'R${OBJ[i]:>5.2f}')