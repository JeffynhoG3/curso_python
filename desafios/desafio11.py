# Faça um programa que leia a largura e a altura de uma parede
# em metros. e calcule a sua ãrea e a quantidade de tinta necessára
# para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m2.

print('')
print('')
print('===== DESAFIO 11 =====')
print('')

al = float(input('Quantos metros tem a altura: '))
la = float(input('Quantos metros tem a largura: '))

ar = al * la
tin = ar / 2

print('A Altura e {} a Largura {} a Area {}.'.format(al, la, ar))
print('Você precisa de {}lt de tinta para pintar {}m²'.format(tin, ar))
