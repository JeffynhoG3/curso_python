# Crie um programa que leia quanto dinheiro uma pessoa
# tem na carteira e mostre quantos Dólares ela pode comprar.
# Considere
# US$1,00 = R$3,27

print('')
print('')
print('===== Exercício #010 =====')
print('')

real = float(input('Quantos reais você tem na carteira: R$'))
dolar = real / 3.27
print('Com R${:.2f}, você pode comprar US${:.2f}'.format(real, dolar))
