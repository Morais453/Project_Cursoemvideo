from time import sleep
from emoji import emojize
contagem = 10
for c in range(10,-1,-1):
    print(c)
    sleep(0.5)
    contagem -=1
print(emojize(':collision:Kabummm:collision:',language='alias'))