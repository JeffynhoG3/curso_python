# Faça um programa que leia a largura e a altura de uma parede
# em metros. e calcule a sua ãrea e a quantidade de tinta necessára
# para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m2.

print('')
print('')
print('===== Exercício #011 =====')
print('')

larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))

area = larg * alt
tinta = area / 2

print('Sua parede tem a dimensão de {}x{} e sua área e de {}m².'.format(larg, alt, area))
print('Para pintar essa parede, você precisará de {}Lt de tinta.'.format(tinta))
