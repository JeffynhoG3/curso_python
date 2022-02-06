# Crie um programa que leia quanto dinheiro uma pessoa
# tem na carteira e mostre quantos Dólares ela pode comprar.
# Considere
# US$1,00 = R$3,27

print('')
print('')
print('===== DESAFIO 10 =====')
print('')

re = float(input('Quantos reais você tem: '))
do = re / 3.27

print('Você pode comprar com R${} em dolares U${:.2f}.'.format(re, do))
