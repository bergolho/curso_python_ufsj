import numpy as np

# Criando uma matrix usando o NumPy
m = np.matrix([ [1,2], [3,4] ])
print(m) 

# Calculando sua inversa
mI = m.I
print(mI) 

# Calculando sua transposta
mT = m.T
print(mT) 

# Criando um vetor linha a partir de um array
b = np.array([2,1])
b = np.matrix(b)
print(b)

# Multiplicando um vetor e uma matriz
print(b * m) 

# Transpondo um vetor linha em coluna
b = b.T
print(b) 

# Multiplicando uma matriz e um vetor
print(m * b) 

# Verificando o produto A * A-1 = I
print(m * m.I) 

