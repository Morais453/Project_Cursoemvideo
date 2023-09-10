ext = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezesete','dezoito','dezenove','vinte')
n = int(input('Insira um valor(entre 0 e 20): '))
while n < 0 or n > 20:
    n = int(input('Valor inválido. Insira o valor entre 0 e 20: '))
print(f'Seu número por extenso é {ext[n]}')