n= int(input('Insira um número de 0 a 9999:  '))
u = n%10
d = ((n-u)/10)%10
c = ((n-(d*10)-u)/100)%10
m = ((n-(c*100+d*10))/1000)%10
print(f'O valor inserido tem {m:0.0f} unidade de Milhar\n{c:0.0f} unidade de centena\n{d:0.0f} unidade de dezena\n{u} unidades.')
s = str(n)
print(f' unidade: {s[3]}')
print(f' dezena: {s[2]}')
print(f' centena: {s[1]}')
print(f' milhar: {s[0]}')