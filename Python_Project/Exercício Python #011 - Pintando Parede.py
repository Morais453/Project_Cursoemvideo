l= int(input('Largura da parede: '))
h= int(input('Altura da parede: '))
a=l*h
print(f'Sua parede tem a dimensão de {l}x{h} e sua área total é de {a}m².')
print('Para pintar essa parede, você precisará de {}l de tinta'.format(a/2))