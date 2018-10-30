import numpy as np

# Cria um array de 24 posicoes
a = np.arange(24)
print a

# Reconstroi o array unidimensional em um bidimensional
a = a.reshape((4,6))
print a

# Imprime um elemnto especifico
print a[2,4]

# Imprime a segunda linha da matriz
print a[1]

# Imprime a ultima linha da matriz
print a[-1]

# Imprime a segunda coluna
print a[:,1]

# Imprime todas as colunas da linha 1 ate a linha 2
print a[1:3,:]

# Imprime as colunas 2 ate a 4, indo da linha 1 ate a 2
print a[1:4,2:5]

# Imprima as linhas de 2 em 2 e as colunas de 3 em 3
print a[::2,::3]


