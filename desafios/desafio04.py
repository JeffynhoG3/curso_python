# Faça um programa que leia algo pelo teclado e mostre
# na tela o seu tipo primitivo e todas as informações
# possíveis sobre ele.

print('')
print('')
print('===== DESAFIO 4 =====')
print('')
n1 = input('Digite algo: ')

print('Seu tipo primitivo é:', type(n1))
print('E alfanumérico:', n1.isalnum())
print('Ele e um número:', n1.isnumeric())
print('Ele e alfabético:', n1.isalpha())
print('Ele está em letras maiúsculas:', n1.isupper())
print('Ele está em letras minúsculas:', n1.islower())
print('Só tem espaços:', n1.isspace())
print('Ele pode ser impresso:', n1.isprintable())
print('Ele está captalizada: ', n1.istitle())
