m= int(input('Uma distância em metros: '))
print(f'a medida de {m} corresponde a\n{m/1000}Km\n{m/100}hm')
print('{}dam\n{}dm\n{}cm\n{}mm'.format(m/10,m*10,m*100,m*1000))