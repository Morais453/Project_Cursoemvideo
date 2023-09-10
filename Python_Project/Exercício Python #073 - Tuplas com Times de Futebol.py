TB = ('Botafogo','Palmeiras','Grêmio','Flamengo','Bragantino','Athletico-PR','Fluminense','Cuiabá','São Paulo','Atlético-MG','Fortaleza','Cruzeiro','Internacional','Corinthians','Goiás','Bahia','Santos','Coritiba','Vasco da Gama','América-MG')
print('Os 5 primeiros colocados são:')
for c in range(0,5):
    print(f'O {c+1}° é o {TB[c]}')

print('E os 4 ultimos colocados são:')
for u in range(-4,):
    print(f'Em {u+1}° temos o {TB[u]}')

print(sorted(TB))

print(f'O chapeco está na posição {TB.index("Chapecoense")}')