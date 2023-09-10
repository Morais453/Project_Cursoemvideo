numb = int(input('Insira um valor: '))
cabeçalho = print("""Escolha uma das bases para conversão:
[1] para binário
[2] para octal
[3] para hexadecimal""")
c = int(input('Sua opção:'))

if c == 1:
    print(f'{numb} convertido para binário é igual a ',bin(numb)[2:])
elif c == 2:
    print(f'{numb} convertido para octal é igual a ',oct(numb)[2:])
elif c ==3:
    print(f'{numb} convertido para hexadecimal é igual a ',hex(numb)[2:])
else:
    print('Operação inválida tente novamente')