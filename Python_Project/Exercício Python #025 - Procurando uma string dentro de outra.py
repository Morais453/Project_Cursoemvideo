nome = input('Insira seu nome completo:  ').upper()
n= nome.strip() and nome.split()
print(f"""O seu nome tem MORAIS: {'MORAIS' in n}
O seu nome tem PEREIRA: {'PEREIRA' in n}""")