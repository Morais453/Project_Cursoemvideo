valor = int(input('Insira o valor do produto: '))
print("""Como forma de pagamento temos:
[1] à vista dinheiro/cheque com 10% de desconto
[2] à vista no cartão com 5% de desconto
[3] em até 2x no cartão
[4] 3x ou mais no cartão com 20% de juros""")
o= int(input('Insira sua opção desejada: '))

if o == 1:
    print(f'O valor a ser pago com o desconto já contabilizado é de R${valor-(valor*0.10):.2f}')
elif o == 2:
    print(f'O valor a ser pago com o desconto já contabilizado é de R${valor-(valor*0.05):.2f}')
elif o == 3:
    print(f'O valor a ser pago é de R${valor:.2f} em 2x de R${valor/2:.2f} no cartão sem juros')
elif o == 4:
    total = valor+(valor*0.20)
    parcela = int(input('Quantas parcelas?'))
    tp = total/parcela
    print('O valor a ser pago é de R${} em {}x de R${} no cartão, já com os 20% de juros'.format(total,parcela,tp))
else:
    print('Opção não reconhecida, tente novamente')