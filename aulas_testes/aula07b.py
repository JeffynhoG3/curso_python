n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

# Obs. 3 casas decimais com ponto flutuante {:.3f}
# Para não quebrar linha de um print para outro usar -> end='' <- no final da linha
# Para quebra de linha usar \n
# print('A soma é {}, \n o produto é {} e a \n divisão é {:.3f}'.format(s, m, d), end='')

print('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(s, m, d))
print('Divisão inteira {} e potência {}'.format(di, e))
