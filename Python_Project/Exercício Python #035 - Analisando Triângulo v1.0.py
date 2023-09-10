a = int(input('Insira o comprimento do segmento de reta A: '))
b = int(input('Insira o comprimento do segmento de reta B: '))
c = int(input('Insira o comprimento do segmento de reta C: '))

if a+b>c or a+c>b or b+c>a:
    print('Os valores informados podem constituir um triângulo')
else:
    print('Forma triângulo não')