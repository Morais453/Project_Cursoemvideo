OBJ = ('Arara', 'Besouro', 'Setembro', 'Cama')
for i in OBJ:
    print(f'\nPara a palavra {i} temos como vogais:', end= " ")
    for c in range(len(i)):
        if i[c] in 'AaEeIiOoUu':
            print(i[c],end= " ")
            if c == len(i):
                print(" \n ")
