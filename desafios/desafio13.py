# Faça um algoritmo que leia o salário de um funcionário
# e mostre seu novo salário, com 15% de aumento.

print('')
print('')
print('===== DESAFIO 13 =====')
print('')

sal = float(input('Qual e o Salário atual: '))

aum = sal * (15/100)

nov = sal + aum

print('O salário atual e R${:.2f} e com 15% de aumento ficará R${:.2f}.'.format(sal, nov))
