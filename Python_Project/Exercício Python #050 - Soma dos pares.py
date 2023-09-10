d= int()
print('Digite seis números e verá a soma dos pares')
numb1 = int(input('Digite um número: '))
numb2 = int(input('Digite mais um número: '))
numb3 = int(input('Digite outro número: '))
numb4 = int(input('Digite mais um número: '))
numb5 = int(input('Digite outro: '))
numb6 = int(input('Digite o ultimo número: '))
l = [numb6,numb5,numb4,numb3,numb2,numb1]
for c in range(0,6,):
    l[c] % 2
    if l[c] % 2 == 0:
        dd = l[c]
        d += dd
print(d)