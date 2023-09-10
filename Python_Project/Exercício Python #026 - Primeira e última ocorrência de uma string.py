f = input('Insira uma frase: ').lower().strip()

print(f'A letra A aparece {f.count("a")} vezes')
print(f'O primeiro A apareceu na posição {f.find("a")+1}')
print(f'E o ultimo em {f.rfind("a")+1}')