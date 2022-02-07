# Faça um algoritmo que leia o preço de um
# produto e mostre seu novo preço, com 5% de desconto.

print('')
print('')
print('===== Exercício #012 =====')
print('')

preco = float(input('Preço do produto: R$'))

novo = preco - (preco * (5/100))

print('O produto custa R${:.2f} e tem 5% de desconto.'.format(preco))
print('Você vai pagar R${:.2f}.'.format(novo))
