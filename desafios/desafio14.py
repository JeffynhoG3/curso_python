# Escreva um programa que converta uma tempetura
# digitada em ºC e converta para ºF.

c = float(input('Informe a temperatuda em ºC: '))
f = ((c * 9) / 5) + 32

print('A temperatura de {}ºC corresponde a {}ºF!'.format(c, f))
