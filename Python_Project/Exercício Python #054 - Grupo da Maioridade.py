from datetime import date
veio=0
novo=0
for c in range(1,8):
    k = int(input(f'Em que ano a pessoa {c} nasceu? '))
    idade = date.today().year-k
    if idade >= 18:
        veio += 1
    else:
        novo +=1
print(f'Tivemos {veio} pessoas maiores de idade e {novo} que ainda não')