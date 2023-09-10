a = int(input('Insira o comprimento do lado A: '))
b = int(input('Insira o comprimento do lado B: '))
c = int(input('Insira o comprimento do lado C: '))

if a+b > c and b+c> a and a+c > b:
    print('De acordo com as medidas informadas temos que a condição de existência é verdadeira')
    if a == b == c:
        print('A classificação do triângulo é equilátero')
    elif a == b or a == c or b == c:
        print('A classificação do triângulo é isósceles')
    else:
        print('A classificação do triângulo é escaleno')
else:
    print('De acordo com as medidas informadas temos que a condição de existência do triãngulo é falsa')