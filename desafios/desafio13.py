# Faça um algoritmo que leia o salário de um funcionário
# e mostre seu novo salário, com 15% de aumento.

print('')
print('')
print('===== DESAFIO 13 =====')
print('')

salario = float(input('Qual e o Salário atual: R$'))

aumento = salario + (salario * (15/100))

print('O salário atual e R${:.2f}, com 15% de aumento ficará R${:.2f}.'.format(salario, aumento))
