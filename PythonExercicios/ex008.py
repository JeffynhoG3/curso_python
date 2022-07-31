# Escreva um programa que leia um valor em metros
# e o exiba convertido em centimetros e milimetros.

print('')
print('')
print('===== Exercício #008 =====')
print('')

me = float(input('Uma distância em metros: '))

print('A medida de {}m correnponde a:'.format(me))
print('{}km Kilometro'.format(me/1000))
print('{}hm Hectômetro'.format(me/100))
print('{}dam Decâmetro'.format(me/10))
print('{:.0f}m Metro'.format(me))
print('{:.0f}dm Decímetro'.format(me*10))
print('{:.0f}cm Centímetro'.format(me*100))
print('{:.0f}mm Milímetro'.format(me*1000))
