# Faça um programa que leia a largura e a altura de uma parede
# em metros. e calcule a sua ãrea e a quantidade de tinta necessára
# para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m2.

print('')
print('')
print('===== DESAFIO 11 =====')
print('')

al = float(input('Altura da parede: '))
la = float(input('Largura da parede: '))

ar = al * la
tin = ar / 2

print('Sua parede tem a dimensão de {}x{} e sua área e de {}m².'.format(al, la, ar))
print('Para pintar essa parede, você precisará de {}Lt de tinta.'.format(tin))
