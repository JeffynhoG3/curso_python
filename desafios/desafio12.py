# Faça um algoritmo que leia o preço de um
# produto e mostre seu novo preço, com 5% de desconto.

print('')
print('')
print('===== DESAFIO 12 =====')
print('')

p = float(input('Preço do produto: '))

d = p * (23/100)

t = p - d

print('O produto custa R${:.2f} e tem 5% de desconto.'.format(p))
print('O desconto e de R${:.2f}, você vai pagar R${:.2f}.'.format(d, t))
