# import math
# from math import sqrt, floor
from math import sqrt

num = int(input('Digite um número: '))

# raiz = math.sqrt(num)
raiz = sqrt(num)

# print('A raiz de {} é igual a {}'.format(num, raiz))
# print('A raiz de {} é igual a {}'.format(num, math.ceil(raiz)) #arredendo pra cima
# print('A raiz de {} é igual a {}'.format(num, math.floor(raiz)) #arredendo pra baixo
# print('A raiz de {} é igual a {}'.format(num, math.trunc(raiz)))

print('A raiz de {} é igual a {:.2f}'.format(num, (raiz)))
