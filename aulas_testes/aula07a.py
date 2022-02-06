nome = input('Qual é seu nome: ')

# Nome em 20 caracteres
print('Prazer em te conhecer {:20}!'.format(nome))

# Alinhado a direito em 20 espaços
print('Prazer em te conhecer {:>20}!'.format(nome))

# Alinhado a esquerda em 20 espaços
print('Prazer em te conhecer {:<20}!'.format(nome))

# Centralizado em 20 espaços
print('Prazer em te conhecer {:^20}!'.format(nome))

# Nome em 20 espaços centralizado com igual
print('Prazer em te conhecer {:=^20}!'.format(nome))
