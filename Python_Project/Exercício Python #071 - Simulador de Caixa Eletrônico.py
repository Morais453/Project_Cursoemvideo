total = int(input('Que valor você quer sacar? R$'))
ced = 100
totalced = 0
while True:
    if total >= ced and totalced < 10:
        total -= ced
        totalced += 1
    else:
        if totalced > 0:
            print(f'Seram necessárias {totalced} de R${ced:.2f}')
        totalced = 0
        if ced == 100:
            ced = 50
            continue
        elif ced == 50:
            ced = 20
            continue
        elif ced == 20:
            ced = 10
            continue
        elif ced == 10:
            ced = 1
            continue
        if total == 0:
            break
