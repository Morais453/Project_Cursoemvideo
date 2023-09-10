print('Gerador de pa')
t = int(input('Primeiro termo: '))
r = int(input('Razão: '))
contagem=0
n = 10
while contagem < n: #ou v != 0
    while contagem <n:
        print(t,end=' -> ')
        t += r
        contagem+=1
    print('Pausa')
    v = int(input('Quantos valores mais você quer ver: '))
    n +=v
print(f'o total de valores da pa exibidos foram {contagem}')