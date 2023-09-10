print('Gerador de pa')
t = int(input('Primeiro termo: '))
r = int(input('Razão: '))
contagem=0
while contagem <10:
    print(t,end=' -> ')
    t += r
    contagem+=1
print('Fim')