# Faça um programa que leia a largura e a altura de uma parede
# em metros. e calcule a sua ãrea e a quantidade de tinta necessára
# para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m2.

print('')
print('')
print('===== DESAFIO 11 =====')
print('')

alt = float(input('Altura da parede: '))
lar = float(input('Largura da parede: '))

area = alt * lar
tint = area / 2

print('Sua parede tem a dimensão de {}x{} e sua área e de {}m².'.format(alt, lar, area))
print('Para pintar essa parede, você precisará de {}Lt de tinta.'.format(tint))
