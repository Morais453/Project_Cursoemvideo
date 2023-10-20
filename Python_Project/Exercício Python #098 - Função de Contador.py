from time import sleep
def contador(i:int,f:int,p:int):
    if p == 0:
        p = 1

    print(f'Contagem de {i} até {f} de {p} em {p}')

    if f < i:
        if p > 0:
            p = -p

        for i in range(i, f-1, p):
            print(i, end= " ", flush=True)
            sleep(0.4)
        print('FIM')

    else:

        for i in range(i, f+1, p):
            print(i, end=' ', flush=True)
            sleep(0.4)
        print('FIM')

contador(1, 10, 1)

contador(10, 0, 2)

print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Inicio: '))
fim = int(input('Final: '))
passo = int(input('Passo: '))

contador(inicio, fim, passo)
