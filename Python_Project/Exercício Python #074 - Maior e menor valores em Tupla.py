from random import randint
n = M = m = 0
T = []
for i in range(0, 5):
    n = randint(-100, 100)
    if (i == 0) or (n < m):
        m = n
    if (i == 0) or (n > M):
        M =n
    T.append(n)

print(f'Os números sorteados foram:\n{T}')

print(f'O menor número sorteado foi {m} e o maior foi {M}')